---
project: ESH10000540
revision: R3
created: 2026-05-04
type: Verification Plan
source: Derived from R2 Verification_Sparrow_FE.xlsx (DUT sheet)
---

# Verification Plan: Sparrow Fixture Electronics PCBA R3

## Overview

This document lists all test cases for ESH10000540 R3 verification.
Test cases are ported from the R2 Excel plan. R2 results are included for reference only —
they do not constitute R3 evidence. All R3 results must be recorded in DUT_LOG.md.

---

## Column Definitions

| Column | Meaning |
|--------|---------|
| Test ID | Unique test case identifier (matches R2 Excel DUT sheet) |
| Req | Linked requirement from SPECIFICATION.md |
| Group | Functional group / sub-group |
| Description | Test procedure summary |
| Signal(s) | Primary signal(s) under test |
| Nominal | Target value |
| Unit | Measurement unit |
| Tol. | Acceptance tolerance |
| R2 | R2 outcome (Pass / Fail / see note) — reference only |
| R3 Status | R3 result — Pending until tested |

---

## Test Equipment

| Equipment | Model / Spec | Purpose |
|-----------|-------------|---------|
| DMM | Siglent SDM3055 (calibrated) | Voltage and current reference |
| Isolated supply | TBD | Isolated stimulus for audio and AIN channels |
| Electronic load | TBD | Current load for power switch PG tests |
| Oscilloscope | TBD | PWM and I2C timing verification |

---

## DUT Information

| Attribute | Value |
|-----------|-------|
| DUT Part Number | ESH10000540 |
| Revision | R3 |
| Serial Number | TBD |
| Location | TBD |
| Status | Pending |

---

## M — Mechanical

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| M.00 | SR-M01 | Mechanical / No Mounts | Verify all no-mount components are absent | NA | — | — | — | Pass | Pending |
| M.01 | SR-M02 | Mechanical / Spacers | Verify N-Top spacers M1, M2 fit mechanically | NA | — | — | — | Pass | Pending |
| M.02 | SR-M02 | Mechanical / Spacers | Verify M.2 Active Load spacers M3, M4 fit mechanically | NA | — | — | — | Pass | Pending |
| M.03 | SR-M02 | Mechanical / Spacers | Verify M.2 PSU spacers M5, M6 fit mechanically | NA | — | — | — | Pass | Pending |

---

## P — Power

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| P.00 | SR-P01 | Power / VDD | Measure VDD rail with DMM | VDD | 20.000 | V | ±5.0% | Pass | Pending |
| P.01 | SR-P02 | Power / 12V | Measure 12V DC/DC rail with DMM | 12V | 12.000 | V | ±5.0% | Pass | Pending |
| P.02 | SR-P02 | Power / 12V | Enable 12V_EXT switch; measure 12V_EXT rail with DMM | 12V_EXT | 12.000 | V | ±5.0% | Pass | Pending |
| P.03 | SR-P02 | Power / 12V | Verify 12V is present at all IDC connectors | — | — | — | — | Pass | Pending |
| P.04 | SR-P02 | Power / 12V | Measure VMON_12V_EXT with ADC; compare to DMM reading | VMON_12V_EXT | DMM vs ADC | V | ±2.4% | Pass | Pending |
| P.05 | SR-P02 | Power / 12V | Increase load on 12V_EXT; verify PG trips at ~500 mA | 12V_EXT | 500.000 | mA | ±5.0% | Pass | Pending |
| P.06 | SR-P02 | Power / 12V | Measure maximum EN current for 12V_EXT switch | 12V_EXT | — | mA | — | Pass | Pending |
| P.07 | SR-P02 | Power / 12V | Measure IMON_12V_EXT_R with ADC at 300 mA; compare to DMM. Nominal gain: 1.21 V/A | IMON_12V_EXT_R | DMM vs ADC | mA | ±10.0% | Pass | Pending |
| P.08 | SR-P03 | Power / 6V5/VADJ | Measure 6V5 DC/DC rail with DMM | 6V5 | 6.500 | V | ±2.5% | Pass | Pending |
| P.09 | SR-P03 | Power / 6V5/VADJ | Enable 6V5_LIM (VADJ_EN) switch; measure 6V5_LIM rail with DMM | 6V5_LIM | 6.500 | V | ±2.5% | Pass | Pending |
| P.10 | SR-P03 | Power / 6V5/VADJ | Measure VADJ_EXT at 1.5 V set-point with DMM at IDC | VADJ_EXT | 1.500 | V | ±2.5% | Pass | Pending |
| P.11 | SR-P03 | Power / 6V5/VADJ | Measure VADJ_EXT at 1.8 V set-point with DMM at IDC | VADJ_EXT | 1.800 | V | ±2.5% | Pass | Pending |
| P.12 | SR-P03 | Power / 6V5/VADJ | Measure VADJ_EXT at 2.5 V set-point with DMM at IDC | VADJ_EXT | 2.500 | V | ±2.5% | Pass | Pending |
| P.13 | SR-P03 | Power / 6V5/VADJ | Measure VADJ_EXT at 3.3 V set-point with DMM at IDC | VADJ_EXT | 3.300 | V | ±2.5% | Pass | Pending |
| P.14 | SR-P03 | Power / 6V5/VADJ | Measure VADJ_EXT at 5 V set-point with DMM at IDC | VADJ_EXT | 5.000 | V | ±2.5% | Pass | Pending |
| P.15 | SR-P03 | Power / 6V5/VADJ | Measure VADJ_EXT at 6 V set-point with DMM at IDC | VADJ_EXT | 6.000 | V | ±2.5% | Pass | Pending |
| P.16 | SR-P03 | Power / 6V5/VADJ | Measure VMON_VADJ_EXT at 6 V with ADC; compare to DMM | VMON_VADJ_EXT | DMM vs ADC | V | ±2.0% | Pass | Pending |
| P.17 | SR-P03 | Power / 6V5/VADJ | Increase load on VADJ_EXT; verify PG trips at ~500 mA | VADJ_EXT | 500.000 | mA | ±5.0% | Pass | Pending |
| P.18 | SR-P03 | Power / 6V5/VADJ | Measure maximum EN current for VADJ_EXT switch | VADJ_EXT | — | mA | — | Pass | Pending |
| P.19 | SR-P03 | Power / 6V5/VADJ | Measure IMON_VADJ_EXT with ADC at 300 mA; compare to DMM | IMON_VADJ_EXT | DMM vs ADC | mA | ±10.0% | Pass | Pending |
| P.20 | SR-P04 | Power / 5V/VIO | Measure 5V DC/DC rail with DMM | 5V | 5.000 | V | ±2.5% | Pass | Pending |
| P.21 | SR-P04 | Power / 5V/VIO | Enable 5V_LIM (VIO_EN) switch; measure 5V_LIM rail with DMM | 5V_LIM | 5.000 | V | ±2.5% | Pass | Pending |
| P.22 | SR-P04 | Power / 5V/VIO | Verify 5V is present at all IDC connectors | — | — | — | — | Pass | Pending |
| P.23 | SR-P04 | Power / 5V/VIO | Measure VIO_EXT at 1.5 V set-point with DMM at IDC | VIO_EXT | 1.500 | V | ±2.5% | Pass | Pending |
| P.24 | SR-P04 | Power / 5V/VIO | Measure VIO_EXT at 1.8 V set-point with DMM at IDC | VIO_EXT | 1.800 | V | ±2.5% | Pass | Pending |
| P.25 | SR-P04 | Power / 5V/VIO | Measure VIO_EXT at 2.5 V set-point with DMM at IDC | VIO_EXT | 2.500 | V | ±2.5% | Pass | Pending |
| P.26 | SR-P04 | Power / 5V/VIO | Measure VIO_EXT at 3.3 V set-point with DMM at IDC | VIO_EXT | 3.300 | V | ±2.5% | Pass | Pending |
| P.27 | SR-P04 | Power / 5V/VIO | Measure VMON_VIO_EXT with ADC; compare to DMM | VMON_VIO_EXT | DMM vs ADC | V | ±1.1% | Pass | Pending |
| P.28 | SR-P04 | Power / 5V/VIO | Increase load on VIO_EXT; verify PG trips at ~500 mA | VIO_EXT | 500.000 | mA | ±5.0% | Pass | Pending |
| P.29 | SR-P04 | Power / 5V/VIO | Measure maximum EN current for VIO_EXT switch | VIO_EXT | — | mA | — | Pass | Pending |
| P.30 | SR-P04 | Power / 5V/VIO | Measure IMON_VIO_EXT with ADC at 300 mA; compare to DMM | IMON_VIO_EXT | DMM vs ADC | mA | ±10.0% | Pass | Pending |
| P.31 | SR-P05 | Power / 3V3 | Measure 3V3 LDO rail with DMM | 3V3 | 3.300 | V | ±2.5% | Pass | Pending |
| P.32 | SR-P05 | Power / 3V3 | Enable 3V3_EXT switch; measure 3V3_EXT rail with DMM at IDC | 3V3_EXT | 3.300 | V | ±2.5% | Pass | Pending |
| P.33 | SR-P05 | Power / 3V3 | Measure VMON_3V3_EXT with ADC; compare to DMM | VMON_3V3_EXT | DMM vs ADC | V | ±1.8% | Pass | Pending |
| P.34 | SR-P05 | Power / 3V3 | Increase load on 3V3_EXT; verify PG trips at ~500 mA | 3V3_EXT | 500.000 | mA | ±5.0% | Pass | Pending |
| P.35 | SR-P05 | Power / 3V3 | Measure maximum EN current for 3V3_EXT switch | 3V3_EXT | — | mA | — | Pass | Pending |
| P.36 | SR-P05 | Power / 3V3 | Measure IMON_3V3_EXT_R with ADC at 300 mA; compare to DMM | IMON_3V3_EXT_R | DMM vs ADC | mA | ±10.0% | Pass | Pending |
| P.37 | SR-P06 | Power / 3V3/1V8 | Enable 3V3_LIM (EXT_1V8_EN) switch; measure 3V3_LIM rail with DMM | 3V3_LIM | 3.300 | V | ±2.5% | Pass | Pending |
| P.38 | SR-P06 | Power / 3V3/1V8 | Enable 3V3_LIM switch; measure 1V8_EXT rail with DMM at IDC | 1V8_EXT | 1.800 | V | ±2.5% | Pass | Pending |
| P.39 | SR-P06 | Power / 3V3/1V8 | Measure VMON_1V8_EXT with ADC; compare to DMM | VMON_1V8_EXT | DMM vs ADC | V | ±1.0% | Pass | Pending |
| P.40 | SR-P06 | Power / 3V3/1V8 | Increase load on 1V8_EXT; verify PG trips at ~500 mA | 1V8_EXT | 500.000 | mA | ±5.0% | Pass | Pending |
| P.41 | SR-P06 | Power / 3V3/1V8 | Measure maximum EN current for 1V8_EXT switch | 1V8_EXT | — | mA | — | Pass | Pending |
| P.42 | SR-P06 | Power / 3V3/1V8 | Measure IMON_1V8_EXT with ADC at 300 mA; compare to DMM | IMON_1V8_EXT | DMM vs ADC | mA | ±10.0% | Pass | Pending |
| P.43 | SR-P07 | Power / VREF | Measure VREF rail with DMM | VREF | 2.500 | V | ±0.14% | Pass | Pending |
| P.44 | SR-P08 | Power / RS485 PSU | Measure voltage over C1+/C1- capacitor with DMM | C1+/- | — | V | — | Pass | Pending |
| P.45 | SR-P08 | Power / RS485 PSU | Measure voltage over C2+/C2- capacitor with DMM | C2+/- | — | V | — | Pass | Pending |
| P.46 | SR-P08 | Power / RS485 PSU | Measure voltage over VS+ capacitor with DMM | VS+ | — | V | — | Pass | Pending |
| P.47 | SR-P08 | Power / RS485 PSU | Measure voltage over VS- capacitor with DMM | VS- | — | V | — | Pass | Pending |
| P.48 | SR-P09 | Power / LED | Verify power LED goes green when Fixture Link is active | LED_GREEN | — | — | — | Pass | Pending |
| P.49 | SR-P10 | Power / Audio Load | Activate MIC_BIAS_LOAD_L; measure load current at 5 V | MIC_IN_L | 2.273 | mA | ±2.3% | Pass | Pending |
| P.50 | SR-P10 | Power / Audio Load | Activate MIC_BIAS_LOAD_Ln; measure load current at 5 V | MIC_IN_Ln | 2.273 | mA | ±2.3% | Pass | Pending |
| P.51 | SR-P10 | Power / Audio Load | Activate MIC_BIAS_LOAD_R; measure load current at 5 V | MIC_IN_R | 2.273 | mA | ±2.3% | Pass | Pending |
| P.52 | SR-P10 | Power / Audio Load | Activate MIC_BIAS_LOAD_Rn; measure load current at 5 V | MIC_IN_Rn | 2.273 | mA | ±2.3% | Pass | Pending |
| P.53 | SR-P10 | Power / Audio Load | Activate PHANTOM_LOAD_L; measure load current at 5 V | MIC_IN_L | 7.353 | mA | ±5.4% | Pass | Pending |
| P.54 | SR-P10 | Power / Audio Load | Activate PHANTOM_LOAD_Ln; measure load current at 5 V | MIC_IN_Ln | 7.353 | mA | ±5.4% | Pass | Pending |
| P.55 | SR-P10 | Power / Audio Load | Activate PHANTOM_LOAD_R; measure load current at 5 V | MIC_IN_R | 7.353 | mA | ±5.4% | Pass | Pending |
| P.56 | SR-P10 | Power / Audio Load | Activate PHANTOM_LOAD_Rn; measure load current at 5 V | MIC_IN_Rn | 7.353 | mA | ±5.4% | Pass | Pending |
| P.57 | SR-P11 | Power / Fixed Load | Activate GND_SW0; measure load current at 5 V | GND_SW0_OUT | 2.273 | mA | ±2.0% | Pass | Pending |
| P.58 | SR-P11 | Power / Fixed Load | Activate GND_SW1; measure load current at 5 V | GND_SW1_OUT | 2.273 | mA | ±2.0% | Pass | Pending |
| P.59 | SR-P11 | Power / Fixed Load | Activate GND_SW2; measure load current at 5 V | GND_SW2_OUT | 2.273 | mA | ±2.0% | Pass | Pending |
| P.60 | SR-P11 | Power / Fixed Load | Activate GND_SW3; measure load current at 5 V | GND_SW3_OUT | 2.273 | mA | ±2.0% | Pass | Pending |

---

## UIO — User IO

### Audio ADC (MIC_IN channels)

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.00 | SR-U01 | UIO / Audio / ADC | Apply 15 V (isolated) at MIC_IN_L; measure bias voltage from ADC | MIC_IN_L | 15.000 | V | ±2.4% | Pass | Pending |
| UIO.01 | SR-U01 | UIO / Audio / ADC | Apply 15 V (isolated) at MIC_IN_Ln; measure bias voltage from ADC | MIC_IN_Ln | 15.000 | V | ±2.4% | Pass | Pending |
| UIO.02 | SR-U01 | UIO / Audio / ADC | Apply 15 V (isolated) at MIC_IN_R; measure bias voltage from ADC | MIC_IN_R | 15.000 | V | ±2.4% | Pass | Pending |
| UIO.03 | SR-U01 | UIO / Audio / ADC | Apply 15 V (isolated) at MIC_IN_Rn; measure bias voltage from ADC | MIC_IN_Rn | 15.000 | V | ±2.4% | Pass | Pending |
| UIO.04 | SR-U01 | UIO / Audio / ADC | Apply 0.1 V (isolated) at MIC_IN_L; measure bias voltage from ADC | MIC_IN_L | 0.100 | V | ±7.1% | Pass | Pending |
| UIO.05 | SR-U01 | UIO / Audio / ADC | Apply 0.1 V (isolated) at MIC_IN_Ln; measure bias voltage from ADC | MIC_IN_Ln | 0.100 | V | ±7.1% | Pass | Pending |
| UIO.06 | SR-U01 | UIO / Audio / ADC | Apply 0.1 V (isolated) at MIC_IN_R; measure bias voltage from ADC | MIC_IN_R | 0.100 | V | ±7.1% | Pass | Pending |
| UIO.07 | SR-U01 | UIO / Audio / ADC | Apply 0.1 V (isolated) at MIC_IN_Rn; measure bias voltage from ADC | MIC_IN_Rn | 0.100 | V | ±7.1% | Pass | Pending |

### RS485 ADC

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.08 | SR-U02 | UIO / RS485 / ADC | Apply logic '1' on buffer to drive RS485_TX*; measure voltage from ADC | RS485_TX* | >0.200 | V | ±2.5% | Pass | Pending |
| UIO.09 | SR-U02 | UIO / RS485 / ADC | Apply 2.5 V across RS485_RX*; measure voltage from ADC | RS485_RX* | 2.500 | V | ±1.9% | Pass | Pending |
| UIO.10 | SR-U02 | UIO / RS485 / ADC | Apply 0.1 V across RS485_RX*; measure voltage from ADC | RS485_RX* | 0.100 | V | ±7.1% | Pass | Pending |

### Fixed Load ADC (GND_SW outputs)

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.11 | SR-U03 | UIO / Fixed Load / ADC | Apply 5 V across GND_SW0_OUT; measure voltage from ADC | GND_SW0_OUT | 5.000 | V | — | Pass | Pending |
| UIO.12 | SR-U03 | UIO / Fixed Load / ADC | Apply 5 V across GND_SW1_OUT; measure voltage from ADC | GND_SW1_OUT | 5.000 | V | — | Pass | Pending |
| UIO.13 | SR-U03 | UIO / Fixed Load / ADC | Apply 5 V across GND_SW2_OUT; measure voltage from ADC | GND_SW2_OUT | 5.000 | V | — | Pass | Pending |
| UIO.14 | SR-U03 | UIO / Fixed Load / ADC | Apply 5 V across GND_SW3_OUT; measure voltage from ADC | GND_SW3_OUT | 5.000 | V | — | Pass | Pending |
| UIO.15 | SR-U03 | UIO / Fixed Load / ADC | Apply 0.1 V across GND_SW0_OUT; measure voltage from ADC | GND_SW0_OUT | 0.100 | V | ±6.4% | Pass | Pending |
| UIO.16 | SR-U03 | UIO / Fixed Load / ADC | Apply 0.1 V across GND_SW1_OUT; measure voltage from ADC | GND_SW1_OUT | 0.100 | V | ±6.4% | Pass | Pending |
| UIO.17 | SR-U03 | UIO / Fixed Load / ADC | Apply 0.1 V across GND_SW2_OUT; measure voltage from ADC | GND_SW2_OUT | 0.100 | V | ±6.4% | Pass | Pending |
| UIO.18 | SR-U03 | UIO / Fixed Load / ADC | Apply 0.1 V across GND_SW3_OUT; measure voltage from ADC | GND_SW3_OUT | 0.100 | V | ±6.4% | Pass | Pending |

### MPIO ADC and DAC (MPIO_0–3)

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.19 | SR-U04 | UIO / MPIO / ADC | Apply 0.1 V across MPIO_0; measure voltage from ADC | MPIO_0 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.20 | SR-U04 | UIO / MPIO / ADC | Apply 0.1 V across MPIO_1; measure voltage from ADC | MPIO_1 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.21 | SR-U04 | UIO / MPIO / ADC | Apply 0.1 V across MPIO_2; measure voltage from ADC | MPIO_2 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.22 | SR-U04 | UIO / MPIO / ADC | Apply 0.1 V across MPIO_3; measure voltage from ADC | MPIO_3 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.23 | SR-U04 | UIO / MPIO / ADC | Apply 4 V across MPIO_0; measure voltage from ADC | MPIO_0 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.24 | SR-U04 | UIO / MPIO / ADC | Apply 4 V across MPIO_1; measure voltage from ADC | MPIO_1 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.25 | SR-U04 | UIO / MPIO / ADC | Apply 4 V across MPIO_2; measure voltage from ADC | MPIO_2 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.26 | SR-U04 | UIO / MPIO / ADC | Apply 4 V across MPIO_3; measure voltage from ADC | MPIO_3 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.27 | SR-U04 | UIO / MPIO / DAC | Output 0.1 V on MPIO_0; measure with DMM | MPIO_0 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.28 | SR-U04 | UIO / MPIO / DAC | Output 0.1 V on MPIO_1; measure with DMM | MPIO_1 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.29 | SR-U04 | UIO / MPIO / DAC | Output 0.1 V on MPIO_2; measure with DMM | MPIO_2 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.30 | SR-U04 | UIO / MPIO / DAC | Output 0.1 V on MPIO_3; measure with DMM | MPIO_3 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.31 | SR-U04 | UIO / MPIO / DAC | Output 4 V on MPIO_0; measure with DMM | MPIO_0 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.32 | SR-U04 | UIO / MPIO / DAC | Output 4 V on MPIO_1; measure with DMM | MPIO_1 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.33 | SR-U04 | UIO / MPIO / DAC | Output 4 V on MPIO_2; measure with DMM | MPIO_2 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.34 | SR-U04 | UIO / MPIO / DAC | Output 4 V on MPIO_3; measure with DMM | MPIO_3 | 4.000 | V | ±0.55% | Pass | Pending |

### FE_MPIO ADC and DAC (FE_MPIO_0–11)

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.35 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_0; measure from ADC | FE_MPIO_0 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.36 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_1; measure from ADC | FE_MPIO_1 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.37 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_2; measure from ADC | FE_MPIO_2 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.38 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_3; measure from ADC | FE_MPIO_3 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.39 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_4; measure from ADC | FE_MPIO_4 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.40 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_5; measure from ADC | FE_MPIO_5 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.41 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_6; measure from ADC | FE_MPIO_6 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.42 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_7; measure from ADC | FE_MPIO_7 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.43 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_8; measure from ADC | FE_MPIO_8 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.44 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_9; measure from ADC | FE_MPIO_9 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.45 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_10; measure from ADC | FE_MPIO_10 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.46 | SR-U05 | UIO / FE_MPIO / ADC | Apply 0.1 V across FE_MPIO_11; measure from ADC | FE_MPIO_11 | 0.100 | V | ±9.0% | Pass | Pending |
| UIO.47 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_0; measure from ADC | FE_MPIO_0 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.48 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_1; measure from ADC | FE_MPIO_1 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.49 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_2; measure from ADC | FE_MPIO_2 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.50 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_3; measure from ADC | FE_MPIO_3 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.51 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_4; measure from ADC | FE_MPIO_4 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.52 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_5; measure from ADC | FE_MPIO_5 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.53 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_6; measure from ADC | FE_MPIO_6 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.54 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_7; measure from ADC | FE_MPIO_7 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.55 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_8; measure from ADC | FE_MPIO_8 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.56 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_9; measure from ADC | FE_MPIO_9 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.57 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_10; measure from ADC | FE_MPIO_10 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.58 | SR-U05 | UIO / FE_MPIO / ADC | Apply 4 V across FE_MPIO_11; measure from ADC | FE_MPIO_11 | 4.000 | V | ±0.7% | Pass | Pending |
| UIO.59 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_0; measure with DMM | FE_MPIO_0 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.60 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_1; measure with DMM | FE_MPIO_1 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.61 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_2; measure with DMM | FE_MPIO_2 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.62 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_3; measure with DMM | FE_MPIO_3 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.63 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_4; measure with DMM | FE_MPIO_4 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.64 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_5; measure with DMM | FE_MPIO_5 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.65 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_6; measure with DMM | FE_MPIO_6 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.66 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_7; measure with DMM | FE_MPIO_7 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.67 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_8; measure with DMM | FE_MPIO_8 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.68 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_9; measure with DMM | FE_MPIO_9 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.69 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_10; measure with DMM | FE_MPIO_10 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.70 | SR-U05 | UIO / FE_MPIO / DAC | Output 0.1 V on FE_MPIO_11; measure with DMM | FE_MPIO_11 | 0.100 | V | ±6.9% | Pass | Pending |
| UIO.71 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_0; measure with DMM | FE_MPIO_0 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.72 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_1; measure with DMM | FE_MPIO_1 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.73 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_2; measure with DMM | FE_MPIO_2 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.74 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_3; measure with DMM | FE_MPIO_3 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.75 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_4; measure with DMM | FE_MPIO_4 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.76 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_5; measure with DMM | FE_MPIO_5 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.77 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_6; measure with DMM | FE_MPIO_6 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.78 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_7; measure with DMM | FE_MPIO_7 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.79 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_8; measure with DMM | FE_MPIO_8 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.80 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_9; measure with DMM | FE_MPIO_9 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.81 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_10; measure with DMM | FE_MPIO_10 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.82 | SR-U05 | UIO / FE_MPIO / DAC | Output 4 V on FE_MPIO_11; measure with DMM | FE_MPIO_11 | 4.000 | V | ±0.55% | Pass | Pending |
| UIO.83 | SR-U05 | UIO / FE_MPIO / Digital | Set FE_MPIO_* as pseudo digital input (threshold 4.5 V / 0.5 V); test at 5 V and 0 V | FE_MPIO_* | — | — | — | Pass | Pending |

### GPIO (USR_GPIO_1–4)

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.84 | SR-U06 | UIO / GPIO / Input | Set USR_GPIO_1 as input; VIL <0.8 V → LOW, VIH >2.0 V → HIGH | USR_GPIO_1 | — | — | — | Pass | Pending |
| UIO.85 | SR-U06 | UIO / GPIO / Input | Set USR_GPIO_2 as input; VIL <0.8 V → LOW, VIH >2.0 V → HIGH | USR_GPIO_2 | — | — | — | Pass | Pending |
| UIO.86 | SR-U06 | UIO / GPIO / Input | Set USR_GPIO_3 as input; VIL <0.8 V → LOW, VIH >2.0 V → HIGH | USR_GPIO_3 | — | — | — | Pass | Pending |
| UIO.87 | SR-U06 | UIO / GPIO / Input | Set USR_GPIO_4 as input; VIL <0.8 V → LOW, VIH >2.0 V → HIGH | USR_GPIO_4 | — | — | — | Pass | Pending |
| UIO.88 | SR-U06 | UIO / GPIO / Output | Set USR_GPIO_1 as output; VOL <0.5 V, VOH >2.3 V | USR_GPIO_1 | — | — | — | Pass | Pending |
| UIO.89 | SR-U06 | UIO / GPIO / Output | Set USR_GPIO_2 as output; VOL <0.5 V, VOH >2.3 V | USR_GPIO_2 | — | — | — | Pass | Pending |
| UIO.90 | SR-U06 | UIO / GPIO / Output | Set USR_GPIO_3 as output; VOL <0.5 V, VOH >2.3 V | USR_GPIO_3 | — | — | — | Pass | Pending |
| UIO.91 | SR-U06 | UIO / GPIO / Output | Set USR_GPIO_4 as output; VOL <0.5 V, VOH >2.3 V | USR_GPIO_4 | — | — | — | Pass | Pending |

### Analog High-Range Channels (AIN_P/N, CH1–8)

> **Note:** UIO.92 (calibration) must be performed before any measurement in UIO.93–UIO.220.
> R2 watch items: UIO.197–204 (AIN_N, G0.25, −16 V) failed on one R2 board; UIO.205–220 (G0.125, ±30 V) failed — test voltage reduced to ±24 V for R3.

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.92 | SR-U07 | UIO / AIN / Calibrate | Calibrate all AIN_*_CH[1:8] channels before measurement | AIN_*_CH[1:8] | — | — | — | Pass | Pending |
| UIO.93 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.94 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.95 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.96 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.97 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.98 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.99 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.100 | SR-U07 | UIO / AIN / G16 | Apply +0.05 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 0.050 | V | ±4.9% | Pass | Pending |
| UIO.101 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH1; measure from ADC | AIN_N_CH1 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.102 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH2; measure from ADC | AIN_N_CH2 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.103 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH3; measure from ADC | AIN_N_CH3 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.104 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH4; measure from ADC | AIN_N_CH4 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.105 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH5; measure from ADC | AIN_N_CH5 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.106 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH6; measure from ADC | AIN_N_CH6 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.107 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH7; measure from ADC | AIN_N_CH7 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.108 | SR-U07 | UIO / AIN / G16 | Apply −0.05 V on AIN_N_CH8; measure from ADC | AIN_N_CH8 | −0.050 | V | ±4.9% | Pass | Pending |
| UIO.109 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.110 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.111 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.112 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.113 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.114 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.115 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.116 | SR-U07 | UIO / AIN / G8 | Apply +0.1 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 0.100 | V | ±2.5% | Pass | Pending |
| UIO.117 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH1; measure from ADC | AIN_N_CH1 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.118 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH2; measure from ADC | AIN_N_CH2 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.119 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH3; measure from ADC | AIN_N_CH3 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.120 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH4; measure from ADC | AIN_N_CH4 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.121 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH5; measure from ADC | AIN_N_CH5 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.122 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH6; measure from ADC | AIN_N_CH6 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.123 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH7; measure from ADC | AIN_N_CH7 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.124 | SR-U07 | UIO / AIN / G8 | Apply −0.1 V on AIN_N_CH8; measure from ADC | AIN_N_CH8 | −0.100 | V | ±2.5% | Pass | Pending |
| UIO.125 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.126 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.127 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.128 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.129 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.130 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.131 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.132 | SR-U07 | UIO / AIN / G4 | Apply +0.5 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 0.500 | V | ±0.58% | Pass | Pending |
| UIO.133 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH1; measure from ADC | AIN_N_CH1 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.134 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH2; measure from ADC | AIN_N_CH2 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.135 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH3; measure from ADC | AIN_N_CH3 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.136 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH4; measure from ADC | AIN_N_CH4 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.137 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH5; measure from ADC | AIN_N_CH5 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.138 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH6; measure from ADC | AIN_N_CH6 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.139 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH7; measure from ADC | AIN_N_CH7 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.140 | SR-U07 | UIO / AIN / G4 | Apply −0.5 V on AIN_N_CH8; measure from ADC | AIN_N_CH8 | −0.500 | V | ±0.58% | Pass | Pending |
| UIO.141 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.142 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.143 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.144 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.145 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.146 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.147 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.148 | SR-U07 | UIO / AIN / G2 | Apply +1 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 1.000 | V | ±0.34% | Pass | Pending |
| UIO.149 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH1; measure from ADC | AIN_N_CH1 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.150 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH2; measure from ADC | AIN_N_CH2 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.151 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH3; measure from ADC | AIN_N_CH3 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.152 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH4; measure from ADC | AIN_N_CH4 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.153 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH5; measure from ADC | AIN_N_CH5 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.154 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH6; measure from ADC | AIN_N_CH6 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.155 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH7; measure from ADC | AIN_N_CH7 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.156 | SR-U07 | UIO / AIN / G2 | Apply −1 V on AIN_N_CH8; measure from ADC | AIN_N_CH8 | −1.000 | V | ±0.34% | Pass | Pending |
| UIO.157 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.158 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.159 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.160 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.161 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.162 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.163 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.164 | SR-U07 | UIO / AIN / G1 | Apply +2 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 2.000 | V | ±0.22% | Pass | Pending |
| UIO.165 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH1; measure from ADC | AIN_N_CH1 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.166 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH2; measure from ADC | AIN_N_CH2 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.167 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH3; measure from ADC | AIN_N_CH3 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.168 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH4; measure from ADC | AIN_N_CH4 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.169 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH5; measure from ADC | AIN_N_CH5 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.170 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH6; measure from ADC | AIN_N_CH6 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.171 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH7; measure from ADC | AIN_N_CH7 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.172 | SR-U07 | UIO / AIN / G1 | Apply −2 V on AIN_N_CH8; measure from ADC | AIN_N_CH8 | −2.000 | V | ±0.22% | Pass | Pending |
| UIO.173 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.174 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.175 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.176 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.177 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.178 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.179 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.180 | SR-U07 | UIO / AIN / G0.5 | Apply +8 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 8.000 | V | ±0.13% | Pass | Pending |
| UIO.181 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH1; measure from ADC | AIN_N_CH1 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.182 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH2; measure from ADC | AIN_N_CH2 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.183 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH3; measure from ADC | AIN_N_CH3 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.184 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH4; measure from ADC | AIN_N_CH4 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.185 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH5; measure from ADC | AIN_N_CH5 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.186 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH6; measure from ADC | AIN_N_CH6 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.187 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH7; measure from ADC | AIN_N_CH7 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.188 | SR-U07 | UIO / AIN / G0.5 | Apply −8 V on AIN_N_CH8; measure from ADC | AIN_N_CH8 | −8.000 | V | ±0.13% | Pass | Pending |
| UIO.189 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH1; measure from ADC | AIN_P_CH1 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.190 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH2; measure from ADC | AIN_P_CH2 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.191 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH3; measure from ADC | AIN_P_CH3 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.192 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH4; measure from ADC | AIN_P_CH4 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.193 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH5; measure from ADC | AIN_P_CH5 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.194 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH6; measure from ADC | AIN_P_CH6 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.195 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH7; measure from ADC | AIN_P_CH7 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.196 | SR-U07 | UIO / AIN / G0.25 | Apply +16 V on AIN_P_CH8; measure from ADC | AIN_P_CH8 | 16.000 | V | ±0.115% | Pass | Pending |
| UIO.197 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH1; measure from ADC ⚠ R2 fail on one board | AIN_N_CH1 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.198 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH2; measure from ADC ⚠ R2 fail on one board | AIN_N_CH2 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.199 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH3; measure from ADC ⚠ R2 fail on one board | AIN_N_CH3 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.200 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH4; measure from ADC ⚠ R2 fail on one board | AIN_N_CH4 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.201 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH5; measure from ADC ⚠ R2 fail on one board | AIN_N_CH5 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.202 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH6; measure from ADC ⚠ R2 fail on one board | AIN_N_CH6 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.203 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH7; measure from ADC ⚠ R2 fail on one board | AIN_N_CH7 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.204 | SR-U07 | UIO / AIN / G0.25 | Apply −16 V on AIN_N_CH8; measure from ADC ⚠ R2 fail on one board | AIN_N_CH8 | −16.000 | V | ±0.115% | Fail (1 board) | Pending |
| UIO.205 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH1; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH1 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.206 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH2; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH2 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.207 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH3; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH3 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.208 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH4; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH4 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.209 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH5; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH5 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.210 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH6; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH6 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.211 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH7; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH7 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.212 | SR-U07 | UIO / AIN / G0.125 | Apply +24 V on AIN_P_CH8; measure from ADC (R2: 30 V failed; reduced to 24 V) | AIN_P_CH8 | 24.000 | V | ±0.11% | 30V fail / 24V pass | Pending |
| UIO.213 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH1; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH1 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.214 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH2; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH2 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.215 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH3; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH3 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.216 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH4; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH4 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.217 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH5; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH5 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.218 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH6; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH6 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.219 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH7; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH7 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |
| UIO.220 | SR-U07 | UIO / AIN / G0.125 | Apply −24 V on AIN_N_CH8; measure from ADC ⚠ R2 −30 V fail; −24 V fail on one board | AIN_N_CH8 | −24.000 | V | ±0.11% | −30V fail / −24V fail (1 board) | Pending |

### Latch

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.221 | SR-U08 | UIO / Latch | Set LATCH*_POL=0, LATCH*_PULL=1; toggle RESETn; verify VALUE=1; drive LATCH* low then float; verify VALUE=0 | LATCH_* | — | — | — | Pass | Pending |
| UIO.222 | SR-U08 | UIO / Latch | Set LATCH*_POL=1, LATCH*_PULL=0; toggle RESETn; verify VALUE=0; drive LATCH* high then float; verify VALUE=1 | LATCH_* | — | — | — | Pass | Pending |

### I2C Transceivers (I2C_4 / I2C26)

> **Note:** UIO.232–235 (t_low) failed in R2 at all voltage levels. Root cause must be identified before R3 sign-off.

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.223 | SR-U09 | UIO / I2C / Functional | Connect I2C device to I2C_4 (I2C26) IDC pins; set I2C_EN high; verify functional I2C at multiple voltage levels (use VIO <2.4 V → I2C_V_SEL=0) | SDA_4, SCL_4 | — | — | — | Pass | Pending |
| UIO.224 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from controller side at 1.5 V supply | SDA_4, SCL_4 | 0.450 | V | — | Pass | Pending |
| UIO.225 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from device side at 1.5 V supply | SDA_4, SCL_4 | 0.450 | V | — | Pass | Pending |
| UIO.226 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from controller side at 1.8 V supply | SDA_4, SCL_4 | 0.540 | V | — | Pass | Pending |
| UIO.227 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from device side at 1.8 V supply | SDA_4, SCL_4 | 0.540 | V | — | Pass | Pending |
| UIO.228 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from controller side at 2.5 V supply | SDA_4, SCL_4 | 0.750 | V | — | Pass | Pending |
| UIO.229 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from device side at 2.5 V supply | SDA_4, SCL_4 | 0.750 | V | — | Pass | Pending |
| UIO.230 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from controller side at 3.3 V supply | SDA_4, SCL_4 | 0.990 | V | — | Pass | Pending |
| UIO.231 | SR-U09 | UIO / I2C / VIL | Measure VIL_max driven from device side at 3.3 V supply | SDA_4, SCL_4 | 0.990 | V | — | Pass | Pending |
| UIO.232 | SR-U09 | UIO / I2C / t_low | Measure t_low min per UM10204 at 1.5 V supply ⚠ R2 Fail | SDA_4, SCL_4 | 1.300 | µs | — | Fail | Pending |
| UIO.233 | SR-U09 | UIO / I2C / t_low | Measure t_low min per UM10204 at 1.8 V supply ⚠ R2 Fail | SDA_4, SCL_4 | 1.300 | µs | — | Fail | Pending |
| UIO.234 | SR-U09 | UIO / I2C / t_low | Measure t_low min per UM10204 at 2.5 V supply ⚠ R2 Fail | SDA_4, SCL_4 | 1.300 | µs | — | Fail | Pending |
| UIO.235 | SR-U09 | UIO / I2C / t_low | Measure t_low min per UM10204 at 3.3 V supply ⚠ R2 Fail | SDA_4, SCL_4 | 1.300 | µs | — | Fail | Pending |
| UIO.236 | SR-U09 | UIO / I2C / t_high | Measure t_high min per UM10204 at 1.5 V supply | SDA_4, SCL_4 | 0.600 | µs | — | Pass | Pending |
| UIO.237 | SR-U09 | UIO / I2C / t_high | Measure t_high min per UM10204 at 1.8 V supply | SDA_4, SCL_4 | 0.600 | µs | — | Pass | Pending |
| UIO.238 | SR-U09 | UIO / I2C / t_high | Measure t_high min per UM10204 at 2.5 V supply | SDA_4, SCL_4 | 0.600 | µs | — | Pass | Pending |
| UIO.239 | SR-U09 | UIO / I2C / t_high | Measure t_high min per UM10204 at 3.3 V supply | SDA_4, SCL_4 | 0.600 | µs | — | Pass | Pending |
| UIO.240 | SR-U09 | UIO / I2C / t_rise | Measure t_rise max per UM10204 at 1.5 V supply | SDA_4, SCL_4 | 0.300 | µs | — | Pass | Pending |
| UIO.241 | SR-U09 | UIO / I2C / t_rise | Measure t_rise max per UM10204 at 1.8 V supply | SDA_4, SCL_4 | 0.300 | µs | — | Pass | Pending |
| UIO.242 | SR-U09 | UIO / I2C / t_rise | Measure t_rise max per UM10204 at 2.5 V supply | SDA_4, SCL_4 | 0.300 | µs | — | Pass | Pending |
| UIO.243 | SR-U09 | UIO / I2C / t_rise | Measure t_rise max per UM10204 at 3.3 V supply | SDA_4, SCL_4 | 0.300 | µs | — | Pass | Pending |

### UART-RS485

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.244 | SR-U10 | UIO / UART-RS485 | Loop back RS485_TX to RS485_RX; send frames; verify received frames match; test up to 1 Mbps | RS485_TX*, RS485_RX*, RS485_EN, UART_* | — | — | — | Pass | Pending |

### PWM

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.245 | SR-U11 | UIO / PWM | Set frequency and duty cycle; verify on oscilloscope at multiple voltage ranges | — | — | — | — | Pass | Pending |

### Active Load (CH0 and CH1)

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| UIO.246 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 0.5 A (PSU 5 V, 2 A); measure current from DMM and ADC | — | 0.500 | A | — | Pass | Pending |
| UIO.247 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 0.5 A; measure local voltage | — | 5.000 | V | — | Pass | Pending |
| UIO.248 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 0.5 A; measure remote voltage from DMM and ADC | — | 5.000 | V | — | Pass | Pending |
| UIO.249 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 1 A (PSU 5 V, 2 A); measure current from DMM and ADC | — | 1.000 | A | — | Pass | Pending |
| UIO.250 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 1 A; measure local voltage | — | 5.000 | V | — | Pass | Pending |
| UIO.251 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 1 A; measure remote voltage from DMM and ADC | — | 5.000 | V | — | Pass | Pending |
| UIO.252 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 2 A (PSU 5 V, 2 A); measure current from DMM and ADC | — | 2.000 | A | — | Pass | Pending |
| UIO.253 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 2 A; measure local voltage | — | 5.000 | V | — | Pass | Pending |
| UIO.254 | SR-U12 | UIO / Active Load / CH0 | CH0: set load 2 A; measure remote voltage from DMM and ADC | — | 5.000 | V | — | Pass | Pending |
| UIO.255 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 0.5 A (PSU 5 V, 2 A); measure current from DMM and ADC | — | 0.500 | A | — | Pass | Pending |
| UIO.256 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 0.5 A; measure local voltage | — | 5.000 | V | — | Pass | Pending |
| UIO.257 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 0.5 A; measure remote voltage from DMM and ADC | — | 5.000 | V | — | Pass | Pending |
| UIO.258 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 1 A (PSU 5 V, 2 A); measure current from DMM and ADC | — | 1.000 | A | — | Pass | Pending |
| UIO.259 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 1 A; measure local voltage | — | 5.000 | V | — | Pass | Pending |
| UIO.260 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 1 A; measure remote voltage from DMM and ADC | — | 5.000 | V | — | Pass | Pending |
| UIO.261 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 2 A (PSU 5 V, 2 A); measure current from DMM and ADC | — | 2.000 | A | — | Pass | Pending |
| UIO.262 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 2 A; measure local voltage | — | 5.000 | V | — | Pass | Pending |
| UIO.263 | SR-U12 | UIO / Active Load / CH1 | CH1: set load 2 A; measure remote voltage from DMM and ADC | — | 5.000 | V | — | Pass | Pending |

---

## CIO — Controller IO

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| CIO.00 | SR-C01 | CIO / I2C | Scan I2C_1 (I2C23); find ADC/DAC @0x10/11/48/49/4A, GPIO expander @0x20, IDPROM @0x50–57, LED driver @0x28/3C | SDA_1, SCL_1 | — | — | — | Pass | Pending |
| CIO.01 | SR-C01 | CIO / I2C | Scan I2C_2 (I2C24); find M.2 Active Load devices @0x0C/10/14/48/49/50–57 | SDA_2, SCL_2 | — | — | — | Pass | Pending |
| CIO.02 | SR-C01 | CIO / I2C | Scan I2C_3 (I2C25); find M.2 PSU devices @0x48/4D/50–57 | SDA_3, SCL_3 | — | — | — | Pass | Pending |
| CIO.03 | SR-C02 | CIO / IO Expander | Verify IO expander RESET_N pin behavior at power-up | RESET_N | — | — | — | Pass | Pending |
| CIO.04 | SR-C03 | CIO / ADC/DAC | Verify ADC/DAC RESETn pin behavior | RESETn | — | — | — | Pass | Pending |
| CIO.05 | SR-C04 | CIO / LSHM | Verify LSHM PRESENCEn pin behavior for connected / disconnected states | PRESENCEn | — | — | — | Pass | Pending |

---

## C — Connectors

| Test ID | Req | Group | Description | Signal(s) | Nominal | Unit | Tol. | R2 | R3 Status |
|---------|-----|-------|-------------|-----------|---------|------|------|----|-----------|
| C.00 | SR-CN01 | Connectors / LSHM | Verify LSHM connector signal mapping is correct | * | — | — | — | Pass | Pending |
| C.01 | SR-CN01 | Connectors / N-Top | Verify N-Top connector signal mapping is correct | * | — | — | — | Pass | Pending |
| C.02 | SR-CN01 | Connectors / M.2 AL | Verify M.2 Active Load connector signal mapping is correct | * | — | — | — | Pass | Pending |
| C.03 | SR-CN01 | Connectors / M.2 PSU | Verify M.2 PSU connector signal mapping is correct | * | — | — | — | Pass | Pending |
| C.04 | SR-CN01 | Connectors / FL | Verify Fixture Link connector signal mapping is correct | * | — | — | — | Pass | Pending |
| C.05 | SR-CN01 | Connectors / Audio | Verify Audio Load connector signal mapping is correct | * | — | — | — | Pass | Pending |

---

## Test Results Summary

| Group | Total | Pass | Fail | Blocked | Pending |
|-------|-------|------|------|---------|---------|
| M — Mechanical | 4 | 0 | 0 | 0 | 4 |
| P — Power | 61 | 0 | 0 | 0 | 61 |
| UIO — User IO | 264 | 0 | 0 | 0 | 264 |
| CIO — Controller IO | 6 | 0 | 0 | 0 | 6 |
| C — Connectors | 6 | 0 | 0 | 0 | 6 |
| **Total** | **341** | **0** | **0** | **0** | **341** |

---

## Notes

- All test results are immutable once recorded in DUT_LOG.md. Add correction notes, do not edit logged results.
- Calibrate all AIN channels (UIO.92) before executing UIO.93–UIO.220.
- R2 watch items requiring attention in R3:
  - **UIO.197–204**: AIN_N at G0.25 (−16 V) — failed on one R2 board. Investigate before testing.
  - **UIO.205–220**: G0.125 test voltage reduced to ±24 V (±30 V failed in R2). AIN_N at −24 V failed on one board.
  - **UIO.232–235**: I2C t_low at all voltages — failed in R2. Root cause required before R3 pass/fail can be assessed.
- See Verification/DUT_LOG.md for per-DUT measurements.
- See DECISIONS.md for any test plan changes made during R3.
