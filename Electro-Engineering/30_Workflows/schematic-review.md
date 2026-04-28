# Schematic & Netlist Review Workflow

## Purpose
Structured process for AI-assisted electrical rule checking (ERC) of schematics and netlists.
The engineer provides design files (or pastes relevant sections); the AI performs deterministic checks and reports findings.

## Scope (v1)
- **Review type:** Electrical rule checks — connectivity, floating pins, power net integrity
- **Not in scope (yet):** Design best-practices, component rating checks, requirement traceability

---

## Supported formats

| Format | Extension / type | Notes |
|--------|-----------------|-------|
| KiCad schematic | `.kicad_sch` | S-expression text; full symbol, wire, label, and power-flag data |
| KiCad netlist | `.kicad_net` (or `.net`) | S-expression; component list + net list with pin mappings |
| SPICE2G6 netlist | `.cir`, `.sp`, `.net` | Line-oriented; `.SUBCKT` blocks, node names, component instances |
| PADS QCV netlist + BOM CSV | `.qcv` + `.csv` | **Preferred PADS input.** QCV: clean net→pin list + explicit unconnected-pin section. BOM CSV: component values and part numbers to supplement QCV. |
| PADS Professional export (legacy) | ASCII / XML | Fallback if QCV unavailable. PADS SPICE2G6 also supported (see section below). |

### Format-specific parsing guidance

#### KiCad schematic (.kicad_sch)
- Top-level list: `(kicad_sch ...)`
- Key elements to extract:
  - `(symbol ...)` — component instances; look at `(pin ...)` and `(property "Reference" ...)` 
  - `(wire ...)` — copper connections between points
  - `(label ...)` / `(global_label ...)` / `(hierarchical_label ...)` — net names
  - `(no_connect ...)` — explicit no-connect markers (X flags)
  - `(power_port ...)` or symbols with `power` property — power rail sources
  - `(junction ...)` — T-junction dots (absence may indicate unintended crossing)
- Hierarchical sheets: `(sheet ...)` blocks reference child sheets; check pin ↔ hierarchical_label consistency

#### KiCad netlist (.kicad_net)
- Top-level: `(export ...)`
- `(components ...)` — list of `(comp ...)` with ref, value, footprint, fields, sheetpath
- `(nets ...)` — list of `(net (code N) (name "NET_NAME") (node (ref XX) (pin YY)) ...)`
- Single-node nets = floating; zero-node nets = orphan net name

**Parser caveats (validated 2026-04-16):**
- `(pintype ...)` is **optional** on `(node ...)` entries — many IC pins omit it. The parser must not require this field or it will silently drop nodes, leading to false floating-net errors.
- `(pinfunction ...)` is also optional and appears inconsistently.
- Net names starting with `unconnected-` (e.g. `unconnected-(U3-NC-Pad4)`) are **intentional no-connect markers** placed by KiCad ERC. Classify these as ℹ️ Info for digital/power/passive pins. **Exception:** Analog input pins (ADC channels, op-amp inputs, comparator inputs) marked `unconnected-` should be flagged as ⚠️ Warning — floating analog inputs cause noise coupling and increased power consumption. Most datasheets recommend tying unused analog inputs to GND or COM.
- Power symbols (`+3V3`, `GND`, etc.) create nets but do not appear in `(components ...)`; their pins often lack `pintype`. Power net identification should rely on net name conventions (`+*`, `VCC*`, `VDD*`, `GND`, `VSS`, `VBUS`, etc.) rather than `power_out` pin type alone.
- **`<NO NET>` handling (critical):** KiCad exports pins that have no net assignment under a net literally named `<NO NET>`. **Every pin on `<NO NET>` is unconnected/floating and must be flagged as an ERC violation (❌ Error).** This includes pins that the designer may have *intended* to connect to GND via a power symbol — if they appear on `<NO NET>`, the connection was not made in the schematic. Common categories found on `<NO NET>`:
  1. **Capacitor GND pins** — pin 2 of decoupling caps that should be tied to GND but aren't.
  2. **IC GND/supply pins** — ground pins on ICs that are not connected.
  3. **Connector shield/GND pins** — connector pins expected to be grounded.
  4. **Signal/RF pins** — pins that should have explicit routing.
  All of these are schematic errors requiring correction. Do not assume `<NO NET>` is a valid ground plane.

#### SPICE2G6 netlist
- Components: lines starting with device letter (R, C, L, D, Q, M, X, V, I, ...)
  - Format: `<name> <node1> <node2> [<node3> ...] <value/model>`
  - Node `0` or `GND` = ground reference
- `.SUBCKT name node1 node2 ...` defines a subcircuit
- Build a node → pin-count map; nodes with count = 1 are floating

**PADS SPICE2G6 export specifics (validated 2026-04-16):**
- Exported by Mentor Graphics / PADS Professional using `wspice.cfg` configuration.
- Format: `<RefDes> <node1> <node2> ... CELL NAME` — the `CELL NAME` suffix is a placeholder and should be stripped before parsing.
- Auto-generated node names follow pattern `NxNyyy` (e.g. `N2N922`, `N4N2302`). Named/meaningful nets use readable names (e.g. `SDA1`, `SCL0`, `UART_EN`).
- A `* Dictionary` section at the end maps power net aliases: e.g. `* 3V3=N3V3`, `* GND = 0`. Use this to identify power nets.
- **No pin types, pin names, or component values** are included — only ref-des and node connections. This limits power-conflict checks (ERC-P05) and makes intent harder to determine for floating nodes.
- **Floating node classification:** Distinguish between auto-named single-pin nodes (likely unused connector/IC pins — lower severity) and named single-pin nodes (likely real missing connections — higher severity).

#### PADS QCV netlist (.qcv) — preferred PADS format

Net list lines:
```
NET : 'NetName' RefDes-Pin RefDes-Pin ...
```
- One net per line; net name in single quotes; no escaping.
- Single-node nets (one `RefDes-Pin` after the name) = floating → ERC-C01 ❌

Unconnected pins section:
```
# begin un-connected pins list
PIN : '/RefDesPath' RefDes-Pin (by TERM)
```
- `(by TERM)` = pin explicitly terminated/no-connected in PADS.
- Treat as intentional NC — equivalent to a KiCad no-connect marker. Classify as ℹ️ Info unless the pin function (from BOM) suggests it should be connected.

**Parser notes:**
- Lines starting with `#` are section markers or comments — skip.
- The `# begin one pin nets list` header may precede single-node entries; parse them the same as multi-node nets (apply ERC-C01).
- Net names are case-sensitive; `GND` and `gnd` would be different nets (flag as ERC-P04 if both appear).

#### PADS BOM CSV (companion to QCV)

Typical columns (PADS default export): `Ref Des`, `Part Number`, `Value`, `Description`, `Footprint`

Usage during review:
- Join on `Ref Des` to resolve component type for every pin in the QCV net list.
- Use `Value` / `Description` to determine pin function (e.g. identify passives for ERC-S01, power ICs for ERC-P01).
- If a BOM row has no `Part Number` or `Value`, flag as ERC-S01 ⚠️.

If no BOM is provided: component type and value checks (ERC-S01, ERC-P05 confirmation) are limited — note this in the review header.

#### PADS ASCII / XML export (legacy fallback)
- ASCII: section-based (`*NET*`, `*PART*`, `*CONNECTION*`, `*SIGNAL*`)
- XML: typically `<netlist>` with `<net>` and `<node>` child elements
- Extract the net → component.pin mapping and apply the same checks as for KiCad netlists
- Prefer QCV + BOM CSV over this format where possible.

---

## ERC checks

Perform each check below when reviewing a schematic or netlist. Mark each as ✅ Pass, ⚠️ Warning, or ❌ Fail with specifics.

### Connectivity checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| ERC-C01 | Floating nets | ❌ Error | Net connected to only one pin (single-node net). Likely unfinished routing. For PADS SPICE exports: auto-named single-pin nodes (`NxNyyy`) are downgraded to ⚠️ Warning (likely unused connector/IC pins); named single-pin nodes remain ❌ Error. |
| ERC-C02 | Unconnected pins | ⚠️ Warning | Component pin not on any net and no no-connect flag. May be intentional (NC pin) or an error. |
| ERC-C03 | No-connect markers | ⚠️ Warning | No-connect flag placed on a pin that IS connected to a net. Contradictory. |
| ERC-C04 | Net label orphans | ❌ Error | A net label that appears only once in the design — the other end is missing. For KiCad: nets named `unconnected-*` are **intentional NC markers** and should be classified as ℹ️ Info, not errors — **except** analog input pins (ADC channels, op-amp inputs), which should be ⚠️ Warning (floating analog inputs cause noise; tie unused to GND/COM per datasheet). |
| ERC-C05 | Duplicate net names | ⚠️ Warning | Different nets assigned the same name (possible unintended short). Context-dependent. |
| ERC-C06 | All-GND connector | ⚠️ Warning | Connector with every pin tied to GND. Likely a shield/mechanical connector or placeholder. Flag for engineer confirmation. |
| ERC-C07 | `<NO NET>` audit | ❌ Error | (KiCad) Pins on the `<NO NET>` net have no net assignment — they are floating/unconnected. **Every pin on `<NO NET>` is an error**, regardless of expected function (GND, signal, RF). If a pin should be grounded, the GND connection is missing in the schematic. |

### Power net checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| ERC-P01 | Power net without source | ❌ Error | A power net (VCC, 3V3, etc.) with consumer pins but no power source (regulator output, power flag, supply symbol). |
| ERC-P02 | Shorted power rails | ❌ Error | Two distinct power nets (e.g. 3V3 and 5V) directly connected. May indicate a wiring error. |
| ERC-P03 | Missing ground connection | ❌ Error | Component with a ground pin (GND, VSS, AGND) that is not connected to any ground net. |
| ERC-P04 | Multiple ground domains | ⚠️ Warning | Design has multiple ground net names (GND, AGND, DGND, etc.). Flag for the engineer to confirm intentional separation. |
| ERC-P05 | Power pin conflict | ❌ Error | Two output-type power pins driving the same net (e.g. two regulator outputs shorted). |

### Structural checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| ERC-S01 | Missing component value | ⚠️ Warning | Passive component (R, C, L) with no value or placeholder value ("?", "DNP" without flag). |
| ERC-S02 | Duplicate reference designator | ❌ Error | Two or more components sharing the same reference (e.g. two R1). |
| ERC-S03 | Hierarchical pin mismatch | ❌ Error | (KiCad) Sheet pin has no matching hierarchical_label in child sheet, or vice versa. |
| ERC-S04 | Empty subcircuit | ⚠️ Warning | (SPICE) `.SUBCKT` with no internal components or only passthrough. |

---

## Review procedure

### 1. Receive the design file
The engineer provides the file by one of:
- Pointing to a file path in the workbook or project folder
- Pasting the file content (or relevant sections) into the chat
- Attaching an export

> ⚠️ **Large file warning:** The `view` tool truncates files at 50 KB. KiCad netlists for real designs are typically 100–250 KB and will be silently truncated, causing the parser to stall or produce false results.
>
> **Do not use `view` to read netlist files directly.** Instead, run a Python parser via `powershell` and capture its structured output. If the project already has a `parse_netlist.py`, run it first to get the net and component data. If not, write a minimal parser script to a temp file and execute it. This bypasses the 50 KB limit entirely.

### 2. Identify format
Determine the file format from extension, content structure, or engineer's statement.

### 3. Parse and extract
Build an internal model:
- **Component list:** Reference, value, footprint (if available), pins
- **Net list:** Net name → list of (component.pin) connections
- **Power nets:** Identify nets that are power rails by name convention (VCC, VDD, 3V3, 5V, GND, VSS, AGND, etc.) or by symbol type
- **No-connect markers:** Pins explicitly marked NC

### 4. Run ERC checks
Execute each check from the table above. For each finding:
- Record the check ID
- State the specific net(s) / component(s) / pin(s) involved
- Classify severity

### 5. Report findings

Use this output format:

```markdown
## ERC Review — <design name>

**File:** <filename or "pasted content">
**Format:** <format>
**Date:** <YYYY-MM-DD>
**Components:** <count>
**Nets:** <count>

### Findings

| # | Check | Severity | Detail |
|---|-------|----------|--------|
| 1 | ERC-C01 | ❌ Error | Net `SPI_MISO` has only 1 connection (U3.pin12) — missing endpoint |
| 2 | ERC-P01 | ❌ Error | Net `VCC_3V3` has 5 consumers but no power source |
| 3 | ERC-C02 | ⚠️ Warning | U1.pin14 (NC) not connected, no no-connect flag |
| ... | ... | ... | ... |

### Summary
- Errors: N
- Warnings: M
- Clean: Y checks passed

### Recommended actions
- [ ] ...
```

### 6. Engineer disposition
The engineer reviews findings and dispositions each:
- **Fix** — update the design
- **Accept** — intentional, no change needed (engineer notes reason)
- **False positive** — check doesn't apply in this context

---

## Limitations and caveats

- **AI cannot see binary files.** PADS native schematics must be exported first. Preferred: QCV netlist + BOM CSV. Fallback: ASCII/XML or SPICE2G6.
- **Pin type data may be incomplete.** If the netlist doesn't carry pin direction (input/output/power/passive), some power-conflict checks (ERC-P05) rely on naming conventions and heuristics — the AI will flag these as "needs engineer confirmation."
- **No layout awareness.** These checks are purely schematic/netlist-level. Physical DRC (clearance, copper pours, vias) is out of scope.
- **No simulation.** The AI does not simulate circuits. It checks structural/connectivity rules only.
- **Large files.** For very large designs (>50KB), the engineer should provide the netlist rather than the full schematic, or split into manageable sections.

---

## AI usage rules (same principles as other workflows)
- AI performs checks and reports findings — **it does not approve or reject a design.**
- AI must not claim a design is "correct" or "clean" — only that no findings were detected in the checks performed.
- If the file is incomplete, ambiguous, or a format is unrecognized, AI stops and asks for clarification.
- Findings are always presented to the engineer for disposition.

---

## Validation log

This workflow was validated against real designs on 2026-04-16:

| Design | Format | Components | Nets | Errors | Warnings | Notes |
|--------|--------|-----------|------|--------|----------|-------|
| ESH10000671 R0 (Accordion Beacon) | KiCad netlist | 79 | 114 | 80 | 7 | 1 orphan, 13 floating signals, 66 unconnected pins on `<NO NET>`, 7 floating ADC analog inputs, 41 intentional NCs |
| ESH10000560 R1 (Tone Audio) | PADS SPICE2G6 | 86 | 239 | 2 named + 127 auto | 1 | 2 floating named nets, 127 floating auto-named (connector/IC pins), J2 all-GND |

**Parser issues found and resolved:**
1. **KiCad `(pintype)` optional** — initial parser required `(pintype ...)` on every node, silently dropping IC pin connections. Fixed: pintype is now parsed as optional. Without this fix, GND showed 0 connections instead of 26.
2. **KiCad `unconnected-*` classification** — initial parser flagged 48 intentional NC markers as errors. Fixed: nets matching `unconnected-*` are classified as informational.
3. **PADS auto-named vs named net severity** — initial parser treated all single-pin nodes equally. Fixed: auto-named (`NxNyyy`) single-pin nodes are downgraded to warnings; named single-pin nodes remain errors.
4. **KiCad `<NO NET>` misclassified** — initial parser treated `<NO NET>` as an implicit GND plane and only flagged non-GND pins as errors. Corrected: `<NO NET>` means "no net assignment" — every pin on it is floating/unconnected and must be flagged as ❌ Error. Pins that should be grounded have a missing GND connection in the schematic.
