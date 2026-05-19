---
project: ESH10000654
product: Sparrow Test Adapter
revision: R0
type: Verification Plan
created: 2026-05-15
engineer: Martin Johansson
basis: SPECIFICATION.md R0 (22 requirements across MECH/INT/EL/FN)
---

# Verification Plan: Sparrow Test Adapter R0

> **AI instruction:** This document is the authoritative source for verification scope and test coverage.
> Never mark a test step as **PASS** unless explicitly stated by the engineer. When a measurement is reported,
> fill in the **Measured** column and evaluate against **Nominal ± Tol**. Only the engineer sets **Result** and **Accepted**.

---

## Overview

Functional verification of the Sparrow Test Adapter R0 against the 22 requirements in SPECIFICATION.md. The TA is a passive/active PCB that interfaces the Accordion A2 test controller to Sparrow sub-assemblies during production test (ESH10000633 R1).

Results are logged in [DUT_LOG.md](DUT_LOG.md) per DUT serial number and test session.

---

## Scope

### In Scope

- **Mechanical:** PCB form factor, connector mate/pin-1 alignment for J4–J9, J10–J13, P1–P4
- **Connectors:** Signal-pin wiring of P1/P3 (PSU) and P2/P4 (DMM)
- **Power:** 2.5 V reference (U3 LDO), 5V_SOLENOID separation (FB1), VLOAD_POS_0/1 routing, voltage-divider readback (12 V / 5 V on J4–J9)
- **Analog:** AIN stimulus / measurement / polarity inversion path, FIXED_LOAD midpoints, ESD clamp presence
- **Digital:** 74HC238 + TBD62083 relay control (Re1–Re7), RS485/I2C loopback, PWM/TACH access
- **Routing:** Accordion ↔ Sparrow signal continuity J10–J13 ↔ J4–J9, MPIO 0 Ω jumpers (R68–R79), MPIO short-circuit detection paths
- **System:** End-to-end functional with Accordion + Sparrow DUT, plus validation of patches on DUT-01 (P0)

### Out of Scope

- Production test of the Sparrow product itself (covered by ESH10000633 R1 PT plan/procedure)
- Schematic/layout review (separate: Review/SCHEMATIC_REVIEW.md, Review/LAYOUT_REVIEW.md)
- Compliance / EMC / environmental stress
- Long-term reliability

### Dependencies / blockers

| # | Item | Affected tests | Status |
|---|------|----------------|--------|
| 1 | PSU connector assignment (P1 vs P3) for 20 V vs Active-Load vs 56 V PoE | C.01, P.04, P.05 | Open (SPECIFICATION Open Item 1) |
| 2 | PoE 56 V routing — no ETH connector visible in schematic | PoE-related tests | Open (SPECIFICATION Open Item 2) |
| 3 | PWR_EN routing — via TA or direct? | R.00 partial | Open (SPECIFICATION Open Item 3) |
| 4 | Ethernet PD load — on TA or external? | n/a here (covered by 633 PT) | Open (SPECIFICATION Open Item 4) |

Tests dependent on these items are marked **⏭ DEFERRED** until each item is resolved.

---

## Test Environment

| Equipment / Tool | Purpose |
|------------------|---------|
| Bench DMM (≥ 5½ digit) | Voltage measurements (P.00–P.06, A.03), continuity (C.*, R.*) |
| Bench DC supply (adjustable) | Stimulus on PSU connectors (P.04, P.05, A.00–A.02) |
| Oscilloscope (≥ 200 MHz) | 5V_SOLENOID transient observation (P.01), waveform checks |
| Accordion A2 + control software | Drive relay address / Relay_En, MPIO drive, I2C/RS485/PWM/TACH testing |
| Sparrow FE sub-assembly (ESH10000540) | Required for end-to-end S.* tests (otherwise S.* deferred) |
| Continuity tester (or DMM continuity mode) | Connector pin-out verification (C.01, C.02) |
| Pinout reference (schematic PDF in DOCS/) | Cross-check for all C.* and R.* tests |

---

## Column definitions

| Column | Description |
|--------|-------------|
| **ID** | Test step identifier (category prefix + number) |
| **Step** | Short label for the test |
| **Function** | Circuit / subsystem under test |
| **Test Procedure** | What is applied and what is observed |
| **Signals** | Nets / test points involved |
| **Nominal** | Expected value from SPECIFICATION / schematic / datasheet |
| **Unit** | Unit of measurement |
| **Tol** | Acceptable tolerance |
| **Measured** | Actual recorded value (filled in by engineer) |
| **Result** | ✅ PASS / ❌ FAIL / ⏭ DEFERRED / ⚠️ OPEN |
| **Req ID** | Cross-reference to SPECIFICATION requirement IDs |

> **Status legend:** ⚠️ OPEN (not yet tested) · 🔄 in progress · ✅ PASS · ❌ FAIL · ⏭ DEFERRED (blocked by dependency).

---

## Test Cases

### Mechanical

| ID | Step | Function | Test Procedure | Signals | Nominal | Unit | Tol | Measured | Result | Req ID |
|----|------|----------|---------------|---------|---------|------|-----|----------|--------|--------|
| M.00 | Form factor | PCB outline | Verify TA PCB physical outline matches mechanical assembly drawing; no interference with Accordion or Sparrow when mated | — | — | — | — | | ⚠️ | MECH.00 |
| M.01 | J4–J9 mate | Sparrow interface | Mate TA J4–J9 (20-pin 2.54 mm SMD female) to Sparrow male headers; verify full seating, no bent pins, pin-1 alignment per schematic | — | — | — | — | | ⚠️ | MECH.01 |
| M.02 | J10–J13 mate | Accordion interface | Mate TA J10–J13 (Samtec HTST-110-01-L-DV spring-loaded) to Accordion A2 mating connectors; verify spring-contact engagement | — | — | — | — | | ⚠️ | MECH.02 |
| M.03 | P1, P3 mate | PSU connectors | Verify P1, P3 (CT3151SP-2) mate with PSU mating connectors; mechanical only | — | — | — | — | | ⚠️ | INT.02 (mech) |
| M.04 | P2, P4 mate | DMM connectors | Verify P2, P4 (CT3151SP-0) mate with DMM mating connectors; mechanical only | — | — | — | — | | ⚠️ | INT.03 (mech) |
| M.05 | R48 populated | BOM/assembly check | Visually verify **R48** is populated on the DUT. **Known defect:** R48 is missing on as-assembled R0 (present in schematic, not fitted at assembly). On DUT-01 (P0), R48 has been patched on 2026-05-15 — confirm patch is present and well-soldered. For any unpatched DUT, record as FAIL. | R48 | populated per schematic | — | — | | ⚠️ | R0 assembly defect |

### Connectors

| ID | Step | Function | Test Procedure | Signals | Pass Criteria | Result | Req ID |
|----|------|----------|---------------|---------|---------------|--------|--------|
| C.00 | J4–J9 pin-1 | Pin-1 orientation | Visually inspect silkscreen pin-1 markers on J4–J9; cross-check against schematic | — | All 6 pin-1 markers present and aligned per schematic | ⚠️ | MECH.01 |
| C.01 | P1, P3 wiring | PSU pin wiring | DMM continuity between P1/P3 pins and schematic-defined nets (PSU+, PSU−, sense/GND) | per schematic | All defined pin-to-net continuities pass; no shorts | ⏭ (blocked by Open Item 1) | INT.02 |
| C.02 | P2, P4 wiring | DMM pin wiring | DMM continuity between P2/P4 pins and DMM±/GND nets per schematic | per schematic | All defined pin-to-net continuities pass | ⚠️ | INT.03 |

### Power

| ID | Step | Function | Test Procedure | Signals | Nominal | Unit | Tol | Measured | Result | Req ID |
|----|------|----------|---------------|---------|---------|------|-----|----------|--------|--------|
| P.00 | 2.5 V ref | U3 LDO output | Apply 5 V to U3 Vin; measure U3 Vout (AMS1117-ADJ, R1=R2=100 Ω → Vout = 1.25 × 2 = 2.5 V) | 2V5_REF | 2.500 | V | ±2% (2.45–2.55) | | ⚠️ | EL.00 |
| P.01 | 5V_SOLENOID isolation | FB1 ferrite separation | With 5 V applied and relays cycling at addresses 0..6 via Accordion, observe digital 5 V on scope; confirm transients are attenuated downstream of FB1 (BLM18AG331SN1D, 330 Ω @ 100 MHz) | 5V, 5V_SOLENOID | digital 5 V transient < (TBD — engineer to define) | mV | TBD | | ⚠️ | EL.01 |
| P.02 | 12 V divider @ J4 | ADC-readable 12 V | Apply 12.000 V to a J-connector 12 V net; measure divided output at Accordion ADC node (R_top = 100 kΩ, R_bot = 10 kΩ → ratio 1:11) | 12V_DIV | 1.091 | V | ±5% | | ⚠️ | EL.05 |
| P.03 | 5 V divider @ J4 | ADC-readable 5 V | Apply 5.000 V to a J-connector 5 V net; measure divided output (same divider) | 5V_DIV | 0.455 | V | ±5% | | ⚠️ | EL.05 |
| P.04 | VLOAD_POS_0 | Active Load supply ch 0 | Apply PSU output via assigned connector; measure VLOAD_POS_0 on Sparrow-side connector | VLOAD_POS_0 | matches PSU output | V | ±2% | | ⏭ (blocked by Open Item 1) | EL.04 / FN.01 |
| P.05 | VLOAD_POS_1 | Active Load supply ch 1 | Same as P.04 for channel 1 | VLOAD_POS_1 | matches PSU output | V | ±2% | | ⏭ (blocked by Open Item 1) | EL.04 / FN.01 |
| P.06 | VREMOTE | Sense voltage | Confirm VREMOTE node is accessible via Accordion ADC and reflects PSU voltage minus voltage drop across sense resistor | VREMOTE | TBD | V | TBD | | ⚠️ | EL.04 |

### Analog

| ID | Step | Function | Test Procedure | Signals | Nominal | Unit | Tol | Measured | Result | Req ID |
|----|------|----------|---------------|---------|---------|------|-----|----------|--------|--------|
| A.00 | AIN PSU path | PSU → AIN stimulus | With AIN relay in stimulus position, apply PSU output to AIN; measure on J4 AIN_P/N | AIN_P, AIN_N | matches PSU | V | ±instrument unc. | | ⚠️ | EL.03 / FN.00 |
| A.01 | AIN DMM path | AIN → DMM measurement | With AIN relay in measurement position, apply known AIN_P/N stimulus; read on DMM via P2/P4 | AIN_P, AIN_N | matches applied | V | ±instrument unc. | | ⚠️ | EL.03 / FN.00 |
| A.02 | AIN polarity invert | DPDT polarity swap | Activate polarity-inversion relay; confirm AIN_P/N polarity is swapped relative to A.00 | AIN_P, AIN_N | inverted polarity | — | — | | ⚠️ | EL.03 / FN.00 |
| A.03 | FIXED_LOAD midpoints | Voltage divider on J5 | With 5 V applied, measure each FIXED_LOAD_0..3 at Sparrow MPIO ADC | FIXED_LOAD_0..3 | 2.500 | V | ±5% | | ⚠️ | EL.07 |
| A.04 | ESD clamp (BAT54C) | D1 Schottky present | Visually verify D1 (BAT54C) is populated; confirm via continuity that AIN lines clamp to rails (V_F drop characteristic) | AIN_P, AIN_N | clamp present | — | — | | ⚠️ | EL.06 |

### Digital

| ID | Step | Function | Test Procedure | Signals | Nominal | Unit | Tol | Measured | Result | Req ID |
|----|------|----------|---------------|---------|---------|------|-----|----------|--------|--------|
| D.00 | Relay select Re1 | 74HC238 + TBD62083 → Re1 | Set Relay_A2/A1/A0 = 000, assert Relay_En; verify Re1 closes via continuity on its contacts | Relay_A0..2, Relay_En, Re1 | Re1 closed | — | — | | ⚠️ | EL.02 |
| D.01 | Relay select Re2..Re7 | Sequential decode | Cycle Relay address 001..110; verify each Re2..Re7 closes exactly | Relay_A0..2, Relay_En, Re2..Re7 | Each addressed relay closed; others open | — | — | | ⚠️ | EL.02 |
| D.02 | Relay_En deassert | Disable all | Set Relay_En = 0 with any address; verify no relays close | Relay_En, Re1..Re7 | All relays open | — | — | | ⚠️ | EL.02 |
| D.03 | RS485 loopback | TX/RX short on TA | Drive RS485 TX from Accordion; verify RX echoes TX (loopback) | RS485_TX_POS/NEG, RS485_RX_POS/NEG | TX data = RX data | — | — | | ⚠️ | FN.02 |
| D.04 | I2C loopback | HOST ↔ DEV bridge | From Accordion, drive I2C HOST SDA/SCL; verify I2C DEV side mirrors transaction | I2C HOST/DEV SDA/SCL | bus traffic mirrored | — | — | | ⚠️ | FN.03 |
| D.05 | PWM_0/1 access | TA test access | Drive PWM_0 then PWM_1 from Accordion; verify accessible at TA test point | PWM_0, PWM_1 | square wave at expected freq/duty | — | — | | ⚠️ | FN.04 |
| D.06 | TACHO_0/1 inject | Signal injection | Inject TACH stimulus via TA; verify Accordion reads expected frequency | TACHO_0, TACHO_1 | matches injected freq | — | — | | ⚠️ | FN.04 |

### Routing

| ID | Step | Function | Test Procedure | Signals | Pass Criteria | Result | Req ID |
|----|------|----------|---------------|---------|---------------|--------|--------|
| R.00 | Accordion ↔ Sparrow continuity | Full J10–J13 → J4–J9 net continuity | Using continuity tester, verify each Accordion-side pin connects to the correct Sparrow-side pin per schematic netlist | all | All defined Accordion↔Sparrow nets pass; no extras / no missing | ⚠️ | INT.00, INT.01 |
| R.01 | MPIO 0 Ω jumpers | R68–R79 populated | Verify R68–R79 are populated (0 Ω) per schematic; continuity across each | MPIO_0..3 paths | All populated jumpers continuous | ⚠️ | EL.08 |
| R.02 | MPIO short-circuit detect | Pin-to-pin via TA | From Fixture Electronics, drive each MPIO; observe propagation to connected neighbour MPIO nets per schematic routing | MPIO_0..3 | Detected at every routed neighbour | ⚠️ | FN.05 |

### System (end-to-end + patch validation)

| ID | Step | Function | Test Procedure | Signals | Pass Criteria | Result | Req ID |
|----|------|----------|---------------|---------|---------------|--------|--------|
| S.00 | E2E with Sparrow FE | Full integration | Mate TA to Accordion A2 and to Sparrow FE; run Accordion auto-sequence covering AIN, FIXED_LOAD, relay control, MPIO, I2C/RS485 loopback | many | All Accordion checks pass | ⚠️ | FN.00–FN.05 |
| S.01 | Patch P0 — Rail A readback | DUT-01 P0 patch | Drive RELAY1 on Sparrow FE; read FE_MPIO_8 and FE_MPIO_10 via Accordion. Repeat with RELAY3. Both relays should drive the same Rail A low. | FE_MPIO_8, FE_MPIO_10, RELAY1, RELAY3 | Rail A = 2.5 V when both relays OFF; Rail A ≈ 0 V when RELAY1 OR RELAY3 ON | ⚠️ | Carry-forward (DESIGN_LOG 2026-05-12) |
| S.02 | Patch P0 — Rail B readback | DUT-01 P0 patch | Same as S.01 for RELAY2, RELAY4 → FE_MPIO_9, FE_MPIO_11 | FE_MPIO_9, FE_MPIO_11, RELAY2, RELAY4 | Rail B = 2.5 V when both relays OFF; Rail B ≈ 0 V when RELAY2 OR RELAY4 ON | ⚠️ | Carry-forward (DESIGN_LOG 2026-05-12) |
| S.03 | Patch P0 — pull-up behaviour | 10 kΩ pull-up to 2.5 V | With all four relays OFF, measure Rail A and Rail B static voltage | Rail A, Rail B | Both 2.5 V ± 2% (2.45–2.55 V) | ⚠️ | Carry-forward |

---

## Coverage Matrix

| SPECIFICATION Req ID | Test Case(s) | Status |
|----------------------|--------------|--------|
| MECH.00 | M.00 | ⚠️ Open |
| MECH.01 | M.01, C.00 | ⚠️ Open |
| MECH.02 | M.02 | ⚠️ Open |
| INT.00 | R.00 | ⚠️ Open |
| INT.01 | R.00 | ⚠️ Open |
| INT.02 | M.03, C.01 | ⏭ Partially deferred (Open Item 1) |
| INT.03 | M.04, C.02 | ⚠️ Open |
| EL.00 | P.00 | ⚠️ Open |
| EL.01 | P.01 | ⚠️ Open |
| EL.02 | D.00, D.01, D.02 | ⚠️ Open |
| EL.03 | A.00, A.01, A.02 | ⚠️ Open |
| EL.04 | P.04, P.05, P.06 | ⏭ Partially deferred (Open Item 1) |
| EL.05 | P.02, P.03 | ⚠️ Open |
| EL.06 | A.04 | ⚠️ Open |
| EL.07 | A.03 | ⚠️ Open |
| EL.08 | R.01 | ⚠️ Open |
| FN.00 | A.00–A.02, S.00 | ⚠️ Open |
| FN.01 | P.04, P.05 | ⏭ Partially deferred (Open Item 1) |
| FN.02 | D.03 | ⚠️ Open |
| FN.03 | D.04 | ⚠️ Open |
| FN.04 | D.05, D.06 | ⚠️ Open |
| FN.05 | R.02, S.00 | ⚠️ Open |
| *(Carry-forward 2026-05-12)* | S.01, S.02, S.03 | ⚠️ Open |

**Coverage:** 22 / 22 SPECIFICATION requirements mapped to test cases. 4 partially blocked by SPECIFICATION Open Items 1–4.

---

## DUT references

| DUT ID | Serial # | State | Notes |
|--------|----------|-------|-------|
| DUT-01 | P0 | Available (patched) | In-house assembled board; 2× rail patches for prototype relay-driver readback (see DUT_LOG.md) |

---

## Open Items (verification-side)

1. **Pull-up resistor value for next revision** — 10 kΩ used on P0 patch. Validate S.01/S.02/S.03 results before committing this value in DESIGN_LOG.md carry-forward. (Resistor-value question still flagged TBD in DESIGN_LOG.)
2. **Tolerances for several tests are TBD** (P.01 transient amplitude, P.06 VREMOTE nominal, A.04 clamp characterization, S.03 tolerance window). Engineer to set before measurement.
3. **Patch granularity question** — S.01 and S.02 cannot distinguish RELAY1 vs RELAY3 (or RELAY2 vs RELAY4) since they share rails. If individual-relay readback is needed for production test, next-revision design must use 4 channels (see DESIGN_LOG carry-forward).
4. **R0 assembly defect — R48 missing** — R48 is in the schematic but was not fitted at assembly. Patched on DUT-01 (P0) 2026-05-15. New test M.05 checks population on each DUT. **Function of R48 to be recorded** from schematic (currently unknown to this plan). For next revision: ensure R48 is correctly flagged for mount in BOM/PnP files.

---

## Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| R0 | 2026-05-15 | Martin Johansson | Initial verification plan derived from SPECIFICATION.md R0 (22 req); 32 test cases across 7 categories; coverage matrix; 4 cases deferred pending SPECIFICATION Open Items 1–4 |
| R0 | 2026-05-15 | Martin Johansson | Added **M.05 R48 population check** — R48 missing on as-assembled R0 board (BOM/assembly defect); patched on DUT-01 (P0). Function of R48 still to be recorded. Verification doc now has 33 test cases. |

---

## Sign-off

| Milestone | Condition | Signed off | Date |
|-----------|-----------|------------|------|
| Verification plan reviewed | Plan reviewed and approved by design engineer | | |
| Verification complete | All non-deferred test cases pass or have approved waiver | | |
