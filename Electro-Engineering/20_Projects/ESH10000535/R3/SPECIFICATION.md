---
project: ESH10000535
revision: R3
document: Specification
status: Approved
created: 2026-04-30
updated: 2026-05-04
---

# Specification — Sparrow N-Top R3

## Scope

The Sparrow N-Top (ESH10000535) is a signal-conditioning and interface PCB that provides:
- Regulated power rails (12V, 5V, 5VA, 3.3V, ±18V, programmable VCCO)
- I2C bus with LED driver, GPIO expander, and IDPROM
- ATmega4809 MCU with UART and UPDI programming interface
- Dual AD5592R DAC/ADC accessible over SPI
- Programmable PWM output voltage rail (PWM_VCCO) and tachometer input voltage rail (TACH_VCCO)
- User IO: PWM output, tachometer input, MPIO, differential analog IO
- LSHM and N-Top connectors to the Agent board

Requirements below are derived from the R2 verification plan (Verification_Sparrow_N-TOP.xlsx). Acceptance criteria marked **[R2]** are carried from R2 and must be confirmed by the engineer for R3 before sign-off.

---

## Requirements

### Mechanical

| Req ID | Type | Description | Acceptance Criteria | Status | Notes |
|--------|------|-------------|---------------------|--------|-------|
| REQ-M01 | Functional | All NM components absent; required substitutions mounted | Visual inspection confirms all NM designators absent; R3-specific NM list verified | Approved | R96 and R76 confirmed mounted in R3 (2026-05-04 MJ) |
| REQ-M02 | Interface | Spacers M1/M2 fit mechanically | M1/M2 can be installed without interference | Approved | [R2] |
| REQ-M03 | Interface | LSHM connector and cable fit in top cover | LSHM + cable installs without mechanical interference with cover | Approved | [R2] |

### Power

| Req ID | Type | Description | Acceptance Criteria | Status | Notes |
|--------|------|-------------|---------------------|--------|-------|
| REQ-P01 | Performance | 12V supply rail within tolerance | 12.0V ±5% (11.40–12.60V) measured with DMM | Approved | [R2] |
| REQ-P02 | Performance | 5V supply rail within tolerance | 5.0V ±5% (4.75–5.25V) measured with DMM | Approved | [R2] |
| REQ-P03 | Performance | 5VA supply rail within tolerance | 5.0V ±1% (4.95–5.05V) measured with DMM | Approved | [R2] |
| REQ-P04 | Performance | 3V3 supply rail within tolerance | 3.3V ±2.5% (3.218–3.383V) measured with DMM | Approved | [R2] |
| REQ-P05 | Performance | VID supply rail within tolerance | 3.3V ±2.5% (3.218–3.383V) measured with DMM | Approved | [R2] |
| REQ-P06 | Performance | VREF_BUF reference within tolerance | 2.5V ±0.14% (2.497–2.504V) measured with DMM | Approved | [R2] — tight spec; confirm for R3 |
| REQ-P07 | Performance | VCAP (LED driver internal supply) within tolerance | 1.8V ±2.5% (1.755–1.845V) measured with DMM | Approved | [R2] |
| REQ-P08 | Performance | PWM_VCCO programmable voltage correct at 4 setpoints | 1.5V, 1.8V, 2.5V, 3.3V each ±1% measured with DMM | Approved | [R2] — R2 note: 100pF feedback cap required to suppress ripple |
| REQ-P09 | Performance | TACH_VCCO programmable voltage correct at 4 setpoints | 1.5V, 1.8V, 2.5V, 3.3V each ±1% measured with DMM | Approved | [R2] — R2 note: 100pF feedback cap required to suppress ripple |
| REQ-P10 | Performance | ADJ+ / BYP+ LTC3265 reference pins within tolerance | 1.2V ±1% (1.188–1.212V) measured with DMM | Approved | [R2] |
| REQ-P11 | Performance | ADJ- / BYP- LTC3265 reference pins within tolerance | −1.2V ±1% (−1.188– −1.212V) measured with DMM | Approved | [R2] |
| REQ-P12 | Performance | VOUT+ charge pump rail present | ≈24V (informational — within 30V abs max) | Approved | [R2] |
| REQ-P13 | Performance | VOUT− charge pump rail present | ≈−24V (informational — within −30V abs max) | Approved | [R2] |
| REQ-P14 | Performance | +18V supply rail within tolerance | 18.0V ±1% (17.82–18.18V) measured with DMM | Approved | [R2] |
| REQ-P15 | Performance | −18V supply rail within tolerance | −18.0V ±1% (−17.82– −18.18V) measured with DMM | Approved | [R2] |

### Control IO

| Req ID | Type | Description | Acceptance Criteria | Status | Notes |
|--------|------|-------------|---------------------|--------|-------|
| REQ-CIO01 | Functional | I2C bus operational; all devices discoverable | LED driver at 0x14 and 0x0C, I2C expander at 0x20, IDPROM at 0x50 found on I2C scan; IDPROM programmable | Approved | R96 confirmed mounted in R3 — address issue resolved |
| REQ-CIO02 | Functional | ATmega4809 programmable over UART | Firmware loadable via UART without error | Approved | [R2] — R2: UART toggle issue observed; check PROG_EN / EN switch behaviour |
| REQ-CIO03 | Functional | ATmega4809 discoverable over I2C | ATmega responds at I2C address 0x30 | Approved | [R2] |
| REQ-CIO04 | Functional | ATmega4809 reset functional | Reset pin (RESETn) restarts MCU correctly | Approved | [R2] |
| REQ-CIO05 | Functional | AD5592R DACs/ADCs accessible over SPI | Read/write to both U10 and U22 over SPI without error | Approved | [R2] |
| REQ-CIO06 | Functional | AD5592R reset functional | RESETn pin restarts devices correctly | Approved | [R2] |
| REQ-CIO07 | Functional | LED driver controls LEDs as expected | All LED channels respond to LP5012 register writes | Approved | [R2] |
| REQ-CIO08 | Functional | PWM output enable pin functional | PWM_OEn enables/disables PWM output correctly | Approved | [R2] |
| REQ-CIO09 | Functional | Tachometer input enable pin functional | TACH_OEn enables/disables tach input correctly | Approved | [R2] |
| REQ-CIO10 | Functional | LED driver IREF setting functional | IREF pin correctly sets LED current reference | Approved | [R2] |

### User IO

| Req ID | Type | Description | Acceptance Criteria | Status | Notes |
|--------|------|-------------|---------------------|--------|-------|
| REQ-UIO01 | Functional | PWM output functional at all VCCO voltages | PWM signal correct at all setpoints (static low/high and dynamic); no unexpected tri-state | Approved | [R2] — R2: FAIL on 1 DUT; check R3 |
| REQ-UIO02 | Functional | Tachometer input functional at all VCCO voltages and frequencies | Tach signal received correctly at all setpoints and frequencies | Approved | [R2] |
| REQ-UIO03 | Functional | MPIO functional | MPIO_0 operates correctly (tested with Fixture Electronics) | Approved | [R2] |
| REQ-UIO04 | Functional | Differential analog IO functional | DAC/ADC signals correct; 2.5V (VREF) setpoint matches DMM reading | Approved | [R2] — tested via Fixture Electronics |

### Connectors

| Req ID | Type | Description | Acceptance Criteria | Status | Notes |
|--------|------|-------------|---------------------|--------|-------|
| REQ-C01 | Interface | LSHM connector pin mapping correct | All signals at LSHM verified against connector mapping | Approved | [R2] |
| REQ-C02 | Interface | N-Top to Agent connector mapping correct | All signals verified against N-Top to Agent mapping | Approved | [R2] |

---

## Column Definitions

| Column | Meaning |
|--------|---------|
| Req ID | Unique identifier |
| Type | Functional / Performance / Interface / Safety / Regulatory |
| Description | What the system must do |
| Acceptance Criteria | Measurable condition that proves the requirement is met |
| Status | Draft / Approved / Verified / Waived |
| Notes | Rationale, source, or open questions |

---

## Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 0.1 | 2026-04-30 | Martin Johansson | Initial blank template |
| 0.2 | 2026-05-04 | Martin Johansson / AI | Requirements derived from R2 verification plan (Verification_Sparrow_N-TOP.xlsx) |
| 0.3 | 2026-05-04 | Martin Johansson | Approved — R2 fixes confirmed in R3: 100pF PWM/TACH_VCCO feedback cap, R96 and R76 mounted |
