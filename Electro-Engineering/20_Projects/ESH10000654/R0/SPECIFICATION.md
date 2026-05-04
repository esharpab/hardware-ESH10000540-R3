---
project: ESH10000654
product: Sparrow Test Adapter
revision: R0
type: Design
created: 2026-05-04
last_updated: 2026-05-04
---

# Specification: Sparrow Test Adapter (R0)

## Scope

This document defines the functional requirements and acceptance criteria for the Sparrow Test Adapter R0
(ESH10000654). The adapter is a passive/active PCB that physically interfaces the Accordion A2 test
controller to the Sparrow DUT sub-assemblies during production test (ESH10000633 R1 Production Test Plan).

Requirements are derived from:
- The schematic ESH10000654 R0 (designed by Martin Trobäck, 2026-02-20)
- ESH10000633 R1 PRODUCTION_TEST_PLAN.md — Test Adapter Requirements Summary

---

## Requirements

### Category definitions

| Category | Description |
|----------|-------------|
| MECH | PCB form factor, mounting, and connector mechanical fit |
| INT | Connector types, pinout compatibility, and external instrument connections |
| EL | Signal routing, power distribution, switching, and protection |
| FN | Adapter-level functional behaviour during production test |

---

### Requirements table

| Req ID | Category | Requirement | Acceptance Criteria | Test Case(s) | Status |
|--------|----------|-------------|---------------------|--------------|--------|
| MECH.00 | MECH | PCB shall interface Accordion A2 to Sparrow sub-assemblies without mechanical modification to either | All connectors engage; no mechanical interference | Visual inspection | Draft |
| MECH.01 | MECH | Sparrow interface headers J4–J9 (6× 20-pin, 2.54 mm pitch SMD female socket) shall mate with corresponding male headers on Sparrow sub-assemblies with pin-1–to–pin-1 alignment | All 6 connectors mate and seat; no bent pins; correct pin-1 orientation per schematic note | Visual inspection | Draft |
| MECH.02 | MECH | Accordion interface connectors J10–J13 (4× Samtec HTST-110-01-L-DV, 20-pin spring-loaded) shall mate with Accordion A2 mating connectors | All 4 connectors mate; spring-contact engagement confirmed | Visual inspection | Draft |
| INT.00 | INT | TA shall route Accordion A2 GPIO, I2C, relay-control, and power signals via J10–J13 to the correct Sparrow sub-assembly connectors (J4–J9) per schematic net list | Signal continuity verified on all Accordion ↔ Sparrow nets | EL.02-VER, FN.02-VER, FN.03-VER | Draft |
| INT.01 | INT | TA shall route all Sparrow sub-assembly signals accessible at J4–J9 per connector pinout defined in the schematic | Net continuity verified between J4–J9 and corresponding Accordion/instrument nets | Functional test | Draft |
| INT.02 | INT | TA shall provide 2× CT3151SP-2 (3-pin) connectors (P1, P3) for external DC supply (PSU) connections | PSU positive, negative, and sense/GND pins wired per schematic; mechanical mate confirmed | Visual inspection | Draft |
| INT.03 | INT | TA shall provide 2× CT3151SP-0 connectors (P2, P4) for external DMM connections | DMM +/− pins wired per schematic; mechanical mate confirmed | Visual inspection | Draft |
| EL.00 | EL | TA shall generate a 2.5 V regulated reference from the 5 V rail using AMS1117-ADJ LDO (U3); Vout = 1.25 × (1 + R2/R1); with R1 = R2 = 100 Ω → Vout = 2.5 V | Vout measured 2.5 V ± 2% (2.45–2.55 V) at rated load with 5 V input | EL.00-VER | Draft |
| EL.01 | EL | Relay coil supply (5V_SOLENOID) shall be separated from digital 5 V by ferrite bead FB1 (BLM18AG331SN1D, 330 Ω @ 100 MHz) to prevent relay switching transients from coupling into logic | 5V_SOLENOID present; digital 5 V waveform remains within spec during relay switching events | EL.01-VER | Draft |
| EL.02 | EL | Seven DPST relays Re1–Re7 (IME03GR) shall be individually selectable via 74HC238 3-to-8 decoder (U1) driving TBD62083 Darlington array (U2); control inputs: 3-bit address Relay_A0/A1/A2 + Relay_En from Accordion GPIO | Each address (0–6) activates exactly one relay; no relay activates when Relay_En is deasserted; verified by continuity on relay contact | EL.02-VER | Draft |
| EL.03 | EL | AIN_P/N switching: relay circuit shall connect J4 AIN_P/N to either the PSU (stimulus) or DMM (measurement) path; a DPDT relay shall provide polarity inversion enabling both positive and negative AIN stimulus without external rewiring | Both PSU→AIN and DMM→AIN paths functional; polarity-inverted path functional; no cross-connection between paths when relay deactivated | PT-SIG.02 | Draft |
| EL.04 | EL | Active Load supply: TA shall route external PSU output to VLOAD_POS_0 and VLOAD_POS_1 independently (2 channels); series sense resistors in line with each channel provide a VREMOTE measurement point | PSU voltage present at VLOAD_POS_0 and VLOAD_POS_1; VREMOTE sense point measurable via Accordion ADC | PT-AL.00–.03 | Draft |
| EL.05 | EL | Power rail monitoring: resistive voltage dividers (approx. ratio 1:11, upper R = 100 kΩ, lower R = 10 kΩ) on 12 V and 5 V rails at connectors J4–J9 shall provide ADC-readable divided voltages accessible to Accordion | Divided voltages present and readable; 12 V → ~1.09 V, 5 V → ~0.45 V at divider output | PT-PWR.02–.08 | Draft |
| EL.06 | EL | ESD protection: BAT54C dual Schottky clamp (D1) shall protect AIN stimulus lines against overvoltage on J4 AIN_P/N | Clamp diodes present per schematic; no damage to TA after AIN stimulus applied at rated PSU voltage | Design review | Draft |
| EL.07 | EL | Fixed loads: resistors on J5 FIXED_LOAD_0–3 shall establish a midpoint voltage of approximately 2.5 V (5 V / 2) measurable by Fixture Electronics MPIO ADC | MPIO reads 2.5 V ± 5% on all four FIXED_LOAD nets with 5 V applied | FN.05-VER | Draft |
| EL.08 | EL | MPIO routing: MPIO_0–3 signals shall be interconnected between Sparrow connectors via 0 Ω jumpers (R68–R79) to allow Fixture Electronics to exercise and detect pin-to-pin short circuits across all connected MPIO nets | Continuity present on all populated MPIO jumper paths; isolation confirmed between unpopulated paths | EL.08-VER | Draft |
| FN.00 | FN | AIN stimulus: TA shall provide switchable PSU stimulus and DMM readback on AIN_P/N via relay; relay shall also invert polarity; this enables testing all PGA gain settings at both positive and negative input values without rewiring | AIN stimulus applied; DMM reads applied voltage ± instrument uncertainty; polarity-inverted test value confirmed | PT-SIG.02 | Draft |
| FN.01 | FN | Active Load supply: TA shall route external DC supply to VLOAD_POS_0 and VLOAD_POS_1 to support Active Load sink current tests on both channels | PSU supply present at VLOAD_POS_0 and VLOAD_POS_1 during PT-AL steps; VLOAD_GND return connected | PT-AL.00–.03 | Draft |
| FN.02 | FN | RS485 loopback: TA shall short RS485_TX_POS/NEG to RS485_RX_POS/NEG to enable RS485 loopback self-test from Accordion | RS485 TX data echoed on RX; loopback round-trip passes Accordion communication test | PT-SIG.08 | Draft |
| FN.03 | FN | I2C loopback: TA shall connect I2C HOST SDA/SCL to DEV SDA/SCL to enable I2C loopback self-test | I2C transaction from host received on device side; loopback round-trip passes | PT-COMM | Draft |
| FN.04 | FN | PWM/TACH access: TA shall route PWM_0/1 and TACHO_0/1 signals to accessible test points or connector pins for probe connection or signal injection | PWM output present at designated TA access point; TACH signal injectable via TA connection | PT-SIG.05, PT-SIG.06 | Draft |
| FN.05 | FN | MPIO self-test: TA shall connect MPIO signals between J4–J9 connectors such that Fixture Electronics can drive each MPIO output and detect short-circuit faults to adjacent nets | All MPIO routing paths exercised; short-circuit faults detectable at Accordion ADC level | PT-SIG.00, PT-SIG.01 | Draft |

---

## Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Confirm which PSU connector (P1 or P3) routes 20 V to Fixture Link VDD vs. Active Load supply vs. PoE 56 V | Martin Johansson | Open |
| 2 | Confirm PoE 56 V routing — is this via TA connector or routed externally? No ETH connector visible in schematic | Martin Johansson | Open |
| 3 | Confirm PWR_EN signal routing — is it via TA from Accordion GPIO, or is it a direct connection not through TA? | Martin Johansson | Open |
| 4 | Confirm Ethernet PD load interface — is a passive PD load fitted on the TA or connected externally for PT-POE.01/.03? | Martin Johansson | Open |
| 5 | Assign formal verification test case IDs (EL.00-VER etc.) when Verification/VERIFICATION.md is created | Martin Johansson | Open |

---

## Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| R0 | 2026-05-04 | Martin Johansson | Initial requirements derived from schematic R0 (Trobäck, 2026-02-20) and ESH10000633 PT plan |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Design Engineer | | | |
| Quality | | | |
