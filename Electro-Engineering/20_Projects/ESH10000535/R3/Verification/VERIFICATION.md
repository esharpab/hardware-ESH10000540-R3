---
project: ESH10000535
revision: R3
document: Verification Plan
status: Draft
created: 2026-05-04
---

# Verification Plan — Sparrow N-Top R3

## Overview

Derived from R2 manual verification plan (DOCS/Verification_Sparrow_N-TOP.xlsx).
All acceptance criteria marked **[R2]** are carried from R2 and must be confirmed by the engineer before R3 sign-off.

---

## Equipment Required

- DMM (calibrated)
- Oscilloscope
- I2C scanner / host PC with test software
- SPI host
- UART programmer
- Fixture Electronics PCBA (for MPIO / analog IO tests)
- N-Top connector breakout / Agent board

---

## DUT Coverage Matrix

| Req ID | Test ID(s) | Status |
|--------|-----------|--------|
| REQ-M01 | M.00 | ⏳ Pending |
| REQ-M02 | M.01 | ⏳ Pending |
| REQ-M03 | M.02 | ⏳ Pending |
| REQ-P01 | P.00 | ⏳ Pending |
| REQ-P02 | P.01 | ⏳ Pending |
| REQ-P03 | P.02 | ⏳ Pending |
| REQ-P04 | P.03 | ⏳ Pending |
| REQ-P05 | P.04 | ⏳ Pending |
| REQ-P06 | P.05 | ⏳ Pending |
| REQ-P07 | P.06 | ⏳ Pending |
| REQ-P08 | P.07–P.10 | ⏳ Pending |
| REQ-P09 | P.11–P.14 | ⏳ Pending |
| REQ-P10 | P.15–P.16 | ⏳ Pending |
| REQ-P11 | P.17–P.18 | ⏳ Pending |
| REQ-P12 | P.19 | ⏳ Pending |
| REQ-P13 | P.20 | ⏳ Pending |
| REQ-P14 | P.21 | ⏳ Pending |
| REQ-P15 | P.22 | ⏳ Pending |
| REQ-CIO01 | CIO.00 | ⏳ Pending |
| REQ-CIO02 | CIO.02 | ⏳ Pending |
| REQ-CIO03 | CIO.03 | ⏳ Pending |
| REQ-CIO04 | CIO.04 | ⏳ Pending |
| REQ-CIO05 | CIO.05 | ⏳ Pending |
| REQ-CIO06 | CIO.06 | ⏳ Pending |
| REQ-CIO07 | CIO.07 | ⏳ Pending |
| REQ-CIO08 | CIO.08 | ⏳ Pending |
| REQ-CIO09 | CIO.09 | ⏳ Pending |
| REQ-CIO10 | CIO.10 | ⏳ Pending |
| REQ-UIO01 | UIO.00 | ⏳ Pending |
| REQ-UIO02 | UIO.01 | ⏳ Pending |
| REQ-UIO03 | UIO.02 | ⏳ Pending |
| REQ-UIO04 | UIO.03 | ⏳ Pending |
| REQ-C01 | C.00 | ⏳ Pending |
| REQ-C02 | C.01 | ⏳ Pending |

---

## M — Mechanical

| Test ID | Step | Description | Signals | Pass Criteria | R2 Notes |
|---------|------|-------------|---------|---------------|----------|
| M.00 | No Mounts | Verify all NM components absent; confirm R3-specific population | N/A | All NM designators absent; R3 BOM population correct | R2: R96 and R76 were missing — R96 caused wrong LED driver address; R76 caused missing UART to ATmega |
| M.01 | Spacers | Verify M1/M2 spacers fit mechanically | N/A | M1/M2 install without interference | — |
| M.02 | LSHM | Verify LSHM connector and cable fit in top cover | N/A | LSHM + cable installs without interference | — |

---

## P — Power

Apply 12V supply. Measure all rails with DMM. Record to DUT_LOG.md.

> **Note:** Tolerances are relative (e.g. ±5% of nominal). All measurements in volts.

| Test ID | Step | Description | Signal | Nominal | Tolerance | Pass Criteria | R2 Notes |
|---------|------|-------------|--------|---------|-----------|---------------|----------|
| P.00 | 12V power | Measure 12V rail | 12V | 12.0 V | ±5% | 11.40–12.60 V | — |
| P.01 | 5V power | Measure 5V rail | 5V | 5.0 V | ±5% | 4.75–5.25 V | — |
| P.02 | 5VA power | Measure 5VA rail | 5VA | 5.0 V | ±1% | 4.95–5.05 V | — |
| P.03 | 3V3 power | Measure 3V3 rail | 3V3 | 3.3 V | ±2.5% | 3.218–3.383 V | — |
| P.04 | VID power | Measure VID rail | VID | 3.3 V | ±2.5% | 3.218–3.383 V | — |
| P.05 | VREF power | Measure VREF_BUF rail | VREF_BUF | 2.5 V | ±0.14% | 2.497–2.504 V | — |
| P.06 | LED power | Measure VCAP at LED driver | VCAP | 1.8 V | ±2.5% | 1.755–1.845 V | — |
| P.07 | PWM_VCCO @1.5V | Set PWM_VCCO to 1.5V via DAC; measure with DMM | PWM_VCCO | 1.5 V | ±1% | 1.485–1.515 V | R2: 100pF feedback cap added to OP to suppress ripple |
| P.08 | PWM_VCCO @1.8V | Set PWM_VCCO to 1.8V via DAC; measure with DMM | PWM_VCCO | 1.8 V | ±1% | 1.782–1.818 V | R2: 100pF feedback cap added |
| P.09 | PWM_VCCO @2.5V | Set PWM_VCCO to 2.5V via DAC; measure with DMM | PWM_VCCO | 2.5 V | ±1% | 2.475–2.525 V | R2: 100pF feedback cap added |
| P.10 | PWM_VCCO @3.3V | Set PWM_VCCO to 3.3V via DAC; measure with DMM | PWM_VCCO | 3.3 V | ±1% | 3.267–3.333 V | R2: 100pF feedback cap added |
| P.11 | TACH_VCCO @1.5V | Set TACH_VCCO to 1.5V via DAC; measure with DMM | TACH_VCCO | 1.5 V | ±1% | 1.485–1.515 V | R2: 100pF feedback cap added |
| P.12 | TACH_VCCO @1.8V | Set TACH_VCCO to 1.8V via DAC; measure with DMM | TACH_VCCO | 1.8 V | ±1% | 1.782–1.818 V | R2: 100pF feedback cap added |
| P.13 | TACH_VCCO @2.5V | Set TACH_VCCO to 2.5V via DAC; measure with DMM | TACH_VCCO | 2.5 V | ±1% | 2.475–2.525 V | R2: 100pF feedback cap added |
| P.14 | TACH_VCCO @3.3V | Set TACH_VCCO to 3.3V via DAC; measure with DMM | TACH_VCCO | 3.3 V | ±1% | 3.267–3.333 V | R2: 100pF feedback cap added |
| P.15 | ADJ+ | Measure ADJ+ rail (LTC3265) | ADJ+ | 1.2 V | ±1% | 1.188–1.212 V | — |
| P.16 | ADJ- | Measure ADJ- rail (LTC3265) | ADJ- | −1.2 V | ±1% | −1.188– −1.212 V | — |
| P.17 | BYP+ | Measure BYP+ rail (LTC3265) | BYP+ | 1.2 V | ±1% | 1.188–1.212 V | — |
| P.18 | BYP- | Measure BYP- rail (LTC3265) | BYP- | −1.2 V | ±1% | −1.188– −1.212 V | — |
| P.19 | VOUT+ | Measure VOUT+ charge pump rail | VOUT+ | ≈24 V | informational | Present and > 20 V | — |
| P.20 | VOUT- | Measure VOUT- charge pump rail | VOUT- | ≈−24 V | informational | Present and < −20 V | — |
| P.21 | +18V | Measure +18V rail | +18V | 18.0 V | ±1% | 17.82–18.18 V | — |
| P.22 | -18V | Measure -18V rail | -18V | −18.0 V | ±1% | −17.82– −18.18 V | — |

---

## CIO — Control IO

| Test ID | Step | Description | Signals | Pass Criteria | R2 Notes |
|---------|------|-------------|---------|---------------|----------|
| CIO.00 | I2C scan | Find all I2C devices; program IDPROM | SDA, SCL | LED driver at 0x14 and 0x0C; I2C expander at 0x20; IDPROM at 0x50; IDPROM write succeeds | R2: R96 missing caused wrong LED driver address |
| CIO.01 | UART loopback | Loopback UART at ATmega pins | UART_ENn, DRTS, DTXD, UCTS, URXD, UPDI_PGM, UPDI | Loopback data received correctly | R2: Question — sometimes needed to toggle PROG_EN; investigate PROG_EN / EN switch behaviour |
| CIO.02 | ATmega UART program | Program ATmega over UART | UART_ENn, DRTS, DTXD, UCTS, URXD, UPDI_PGM, UPDI | Firmware loads without error | — |
| CIO.03 | ATmega I2C | Find ATmega over I2C | SDA, SCL | ATmega responds at 0x30 | — |
| CIO.04 | ATmega reset | Test ATmega RESETn pin | RESETn | MCU restarts correctly on RESETn assertion | — |
| CIO.05 | ADC SPI access | Access both AD5592R (U10, U22) over SPI | SPI_ENn, DSCLK, SMOSI, SCS0n, SDO, DCS1n, SCK, SDI | Read/write both devices without error | — |
| CIO.06 | ADC reset | Test AD5592R RESETn pin | RESETn | Both devices restart correctly | — |
| CIO.07 | LED driver | Control LEDs via LP5012 | LED* | All LED channels respond to register writes | — |
| CIO.08 | PWM OE | Test PWM output enable | PWM_OEn | PWM_OEn enables/disables PWM output correctly | — |
| CIO.09 | Tach OE | Test tachometer input enable | TACH_OEn | TACH_OEn enables/disables tach input correctly | — |
| CIO.10 | IREF | Test LED driver IREF | IREF | IREF setting correctly controls LED current | — |

---

## UIO — User IO

| Test ID | Step | Description | Signals | Pass Criteria | R2 Notes |
|---------|------|-------------|---------|---------------|----------|
| UIO.00 | PWM functional | Test PWM output at all VCCO voltages; static low, high, tri-state, and dynamic | PWM* | PWM signal correct at all setpoints; no unexpected tri-state behaviour | R2: FAIL on 1 DUT — investigate on R3 |
| UIO.01 | Tach functional | Test tach input at all VCCO voltages and frequencies | TACH* | Tach signal received correctly at all setpoints and frequencies | — |
| UIO.02 | MPIO | Test MPIO (with Fixture Electronics) | MPIO_0 | MPIO_0 operates correctly | — |
| UIO.03 | Differential analog IO | Set DAC to 2.5V (VREF); compare to DMM | MPIO_1 | DAC setpoint matches DMM ±acceptance; ADC reads back correctly | Tested via Fixture Electronics |

---

## C — Connectors

| Test ID | Step | Description | Signals | Pass Criteria | R2 Notes |
|---------|------|-------------|---------|---------------|----------|
| C.00 | LSHM mapping | Verify LSHM connector pin mapping | All | All signals at correct LSHM pins per connector map | — |
| C.01 | N-Top mapping | Verify N-Top to Agent connector mapping | All | All signals correct per N-Top to Agent mapping | — |

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Test Engineer | — | — | — |
| Design Engineer | — | — | — |
