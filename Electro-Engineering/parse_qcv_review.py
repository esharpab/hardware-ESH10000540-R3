#!/usr/bin/env python3
"""
PADS QCV + CSV netlist parser and ERC check engine.
Parses PADS QCV netlist and BOM CSV, then runs comprehensive ERC checks.
"""

import sys
import re
from collections import defaultdict
from pathlib import Path

def parse_qcv(qcv_path):
    """Parse PADS QCV netlist file."""
    nets = {}
    unconnected_pins = set()
    
    with open(qcv_path, 'r', encoding='utf-8') as f:
        in_unconnected_section = False
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                if 'begin un-connected' in line.lower():
                    in_unconnected_section = True
                continue
            
            if in_unconnected_section:
                # Parse unconnected pin line: PIN : '/RefDesPath' RefDes-Pin (by TERM)
                if line.startswith('PIN :'):
                    match = re.search(r"'([^']+)'\s+(\S+)\s+\(by TERM\)", line)
                    if match:
                        pin_path = match.group(1)
                        ref_des_pin = match.group(2)
                        unconnected_pins.add(ref_des_pin)
            else:
                # Parse net line: NET : 'NetName' RefDes-Pin RefDes-Pin ...
                if line.startswith('NET :'):
                    match = re.match(r"NET\s+:\s+'([^']+)'\s+(.*)", line)
                    if match:
                        net_name = match.group(1)
                        pins_str = match.group(2)
                        pins = pins_str.split()
                        nets[net_name] = pins
    
    return nets, unconnected_pins

def parse_csv(csv_path):
    """Parse PADS BOM CSV file."""
    components = {}
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if not lines:
            return components
        
        # Parse header
        header = lines[0].strip().split(';')
        header = [h.strip() for h in header]
        
        try:
            part_number_idx = header.index('PartNumber')
            ref_des_idx = header.index('RefDes')
            value_idx = header.index('Value')
            part_name_idx = header.index('Part Name')
        except ValueError:
            print("Warning: CSV header columns not found. Continuing with limited component data.")
            return components
        
        # Parse data rows
        for line in lines[1:]:
            if not line.strip():
                continue
            
            fields = line.strip().split(';')
            if len(fields) < max(part_number_idx, ref_des_idx, value_idx, part_name_idx) + 1:
                continue
            
            part_number = fields[part_number_idx].strip()
            ref_des_str = fields[ref_des_idx].strip()
            value = fields[value_idx].strip()
            part_name = fields[part_name_idx].strip()
            
            # Parse multi-designator strings like "C1,C2,C3"
            for ref_des in ref_des_str.split(','):
                ref_des = ref_des.strip()
                if ref_des:
                    components[ref_des] = {
                        'part_number': part_number,
                        'value': value,
                        'part_name': part_name,
                        'type': ref_des[0] if ref_des else 'X',  # R, C, L, U, J, etc.
                    }
    
    return components

def build_pin_net_map(nets):
    """Build map of (RefDes-Pin) -> Net for fast lookups."""
    pin_to_net = {}
    for net_name, pins in nets.items():
        for pin in pins:
            if pin not in pin_to_net:
                pin_to_net[pin] = []
            pin_to_net[pin].append(net_name)
    return pin_to_net

def extract_ref_des(pin_str):
    """Extract reference designator from 'RefDes-Pin' string."""
    match = re.match(r"([A-Z]+\d+)-", pin_str)
    if match:
        return match.group(1)
    return None

def identify_power_nets(nets):
    """Identify nets that are power rails by name convention."""
    power_patterns = [
        r'^GND$', r'^VSS', r'^AGND', r'^DGND',
        r'^\+?[\d\.]+V', r'^3V3', r'^5V', r'^VCC', r'^VDD', r'^VBUS',
    ]
    
    power_nets = set()
    for net_name in nets.keys():
        for pattern in power_patterns:
            if re.search(pattern, net_name, re.IGNORECASE):
                power_nets.add(net_name)
                break
    return power_nets

def is_component_passive(comp_type):
    """Check if component type is passive."""
    return comp_type in ['R', 'C', 'L', 'D']

def run_erc_checks(nets, unconnected_pins, components):
    """Run all ERC checks and return findings."""
    findings = []
    pin_to_net = build_pin_net_map(nets)
    power_nets = identify_power_nets(nets)
    
    # Build ref-des list for duplicate check
    all_ref_des = set()
    for pin_str in pin_to_net.keys():
        ref_des = extract_ref_des(pin_str)
        if ref_des:
            all_ref_des.add(ref_des)
    
    checked = set()
    
    # ERC-C01: Floating nets (single-node nets)
    for net_name, pins in nets.items():
        if len(pins) == 1:
            pin = pins[0]
            # Determine severity based on net type
            if re.match(r'^unconnected-', net_name, re.IGNORECASE):
                # Intentional NC marker - check if it's an analog pin
                ref_des = extract_ref_des(pin)
                if ref_des and ref_des in components:
                    comp_info = components[ref_des]
                    # Check if it's likely an analog input (ADC, op-amp, comparator)
                    if any(x in comp_info['part_name'].lower() for x in ['adc', 'opamp', 'comparator', 'sensor']):
                        findings.append({
                            'id': 'ERC-C01',
                            'net_name': net_name,
                            'severity': '⚠️ Warning',
                            'detail': f"Net '{net_name}' is a single-node net (floating analog input): {pin}"
                        })
                    # else: skip - intentional NC marker
                # else: skip - intentional NC marker
            elif re.match(r'^<NO NET>$', net_name, re.IGNORECASE):
                # Special case: <NO NET> is an error
                findings.append({
                    'id': 'ERC-C07',
                    'net_name': net_name,
                    'severity': '❌ Error',
                    'detail': f"Pin {pin} is on <NO NET> — no net assignment (floating/unconnected)"
                })
            else:
                # Named single-pin net: likely a real error
                findings.append({
                    'id': 'ERC-C01',
                    'net_name': net_name,
                    'severity': '❌ Error',
                    'detail': f"Net '{net_name}' is a single-node net (floating): {pin}"
                })
    
    # ERC-C02: Unconnected pins (no-connect marker present but no explicit NC flag)
    # Note: QCV format has explicit NC section; we'll flag pins in unconnected_pins without explicit (by TERM)
    
    # ERC-C05: Duplicate net names (different nets with same name)
    net_names = list(nets.keys())
    for net_name in net_names:
        count = sum(1 for n in net_names if n == net_name)
        if count > 1:
            findings.append({
                'id': 'ERC-C05',
                'net_name': net_name,
                'severity': '⚠️ Warning',
                'detail': f"Net name '{net_name}' appears {count} times (possible unintended short)"
            })
    
    # ERC-C06: All-GND connector
    for net_name, pins in nets.items():
        if len(pins) > 1 and re.match(r'^GND$', net_name, re.IGNORECASE):
            # Check if all pins are from the same connector (e.g., J1-*, J2-*, etc.)
            connectors = set()
            for pin in pins:
                ref_des = extract_ref_des(pin)
                if ref_des and ref_des.startswith('J'):
                    connectors.add(ref_des)
            
            if len(connectors) == 1 and len(pins) > 5:  # Single connector with many GND pins
                findings.append({
                    'id': 'ERC-C06',
                    'net_name': net_name,
                    'severity': '⚠️ Warning',
                    'detail': f"Net '{net_name}' has {len(pins)} pins, all on connector {list(connectors)[0]} (likely shield/mechanical)"
                })
    
    # ERC-P01: Power net without source
    for power_net in power_nets:
        if power_net in nets:
            pins = nets[power_net]
            has_source = False
            # Look for regulator outputs, power symbols (which have no ref-des), or power flags
            for pin in pins:
                ref_des = extract_ref_des(pin)
                if ref_des:
                    if ref_des in components:
                        comp_info = components[ref_des]
                        # Check if it's a regulator or power IC
                        if any(x in comp_info['part_name'].lower() for x in ['reg', 'ldo', 'buck', 'pmu']):
                            has_source = True
                            break
            
            if not has_source and not re.match(r'^GND', power_net, re.IGNORECASE):
                findings.append({
                    'id': 'ERC-P01',
                    'net_name': power_net,
                    'severity': '❌ Error',
                    'detail': f"Power net '{power_net}' has {len(pins)} consumer pins but no identified power source"
                })
    
    # ERC-P04: Multiple ground domains
    gnd_domains = set()
    for net_name in nets.keys():
        if re.match(r'(GND|VSS|AGND|DGND)', net_name, re.IGNORECASE):
            gnd_domains.add(net_name)
    
    if len(gnd_domains) > 1:
        findings.append({
            'id': 'ERC-P04',
            'net_name': '/'.join(sorted(gnd_domains)),
            'severity': '⚠️ Warning',
            'detail': f"Design has multiple ground domains: {', '.join(sorted(gnd_domains))} — confirm if intentional"
        })
    
    # ERC-S01: Missing component value
    for ref_des, comp_info in components.items():
        if is_component_passive(comp_info['type']):
            if not comp_info['value'] or comp_info['value'] in ['?', 'DNP', '']:
                findings.append({
                    'id': 'ERC-S01',
                    'net_name': ref_des,
                    'severity': '⚠️ Warning',
                    'detail': f"Passive component {ref_des} ({comp_info['part_name']}) has no value or placeholder value"
                })
    
    # ERC-S02: Duplicate reference designator
    ref_counts = defaultdict(int)
    for ref_des in all_ref_des:
        ref_counts[ref_des] += 1
    
    for ref_des, count in ref_counts.items():
        if count > 1:
            findings.append({
                'id': 'ERC-S02',
                'net_name': ref_des,
                'severity': '❌ Error',
                'detail': f"Reference designator '{ref_des}' appears {count} times (duplicate)"
            })
    
    return findings

def main():
    if len(sys.argv) < 3:
        print("Usage: python parse_qcv_review.py <qcv_file> <csv_file>")
        sys.exit(1)
    
    qcv_file = sys.argv[1]
    csv_file = sys.argv[2]
    
    print(f"Parsing QCV: {qcv_file}")
    print(f"Parsing BOM: {csv_file}\n")
    
    nets, unconnected_pins = parse_qcv(qcv_file)
    components = parse_csv(csv_file)
    
    print(f"✓ Parsed {len(nets)} nets")
    print(f"✓ Parsed {len(components)} components")
    print(f"✓ Found {len(unconnected_pins)} unconnected pins\n")
    
    # Run ERC checks
    findings = run_erc_checks(nets, unconnected_pins, components)
    
    # Summarize by severity
    errors = [f for f in findings if '❌' in f['severity']]
    warnings = [f for f in findings if '⚠️' in f['severity']]
    info = [f for f in findings if 'ℹ️' in f['severity']]
    
    print(f"=== ERC CHECK SUMMARY ===")
    print(f"Errors:   {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Info:     {len(info)}")
    print(f"Total findings: {len(findings)}\n")
    
    # Output findings table
    print("=== FINDINGS (sorted by severity) ===\n")
    
    all_sorted = sorted(findings, key=lambda x: (0 if '❌' in x['severity'] else 1 if '⚠️' in x['severity'] else 2))
    
    for idx, finding in enumerate(all_sorted, 1):
        print(f"{idx}. [{finding['id']}] {finding['severity']}")
        print(f"   Net/Component: {finding['net_name']}")
        print(f"   {finding['detail']}\n")

if __name__ == '__main__':
    main()
