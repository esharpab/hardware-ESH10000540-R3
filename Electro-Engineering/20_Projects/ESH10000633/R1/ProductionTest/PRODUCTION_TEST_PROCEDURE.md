---
project: ESH10000633
revision: R1
document: Production Test Procedure
status: Draft
created: 2026-05-05
source: Sparrow Unit Test Specification v1 (E. Rhodin, 2025-11-25); PRODUCTION_TEST_PLAN.md
---

# Production Test Procedure — Sparrow Complete Product R1

## Purpose

Step-by-step procedure for production testing of Sparrow Complete Product R1 (ESH10000633).
Covers visual inspection, system power-on, connector-level IO verification, Active Load, PoE, firmware check, and cosmetics.

Derived from the Sparrow Unit Test Specification v1 (Elsa Rhodin, 2025-11-25) and PRODUCTION_TEST_PLAN.md.
Each step cross-references the relevant PT plan step ID where applicable.

> **Important:** Results are immutable once recorded. Do not edit a recorded result — add a correction note instead.
> This document is a procedure template. A separate DUT log must be created per unit (see ProductionTest/DUT_LOG.md).

---

## Reference Documents

| Document | Version | Location |
|----------|---------|----------|
| Sparrow Unit Test Specification | v1, 2025-11-25 | DOCS/ |
| PRODUCTION_TEST_PLAN.md | Draft | ProductionTest/ |
| SPECIFICATION.md | Draft | root/ |
| ESH10000654 R0 SPECIFICATION.md | Draft | 20_Projects/ESH10000654/R0/ |

---

## Equipment & Materials

### Test Equipment

| Item | Requirement | Used For |
|------|-------------|---------|
| DC Supply A | 20 V / ≥2 A | Fixture Link VDD (via TA) |
| DC Supply B | 56 V / ≥2 A | PoE VIN (via TA) |
| DC Supply C | 24 V / ≥1 A | Active Load VLOAD_POS_0 (via TA) |
| DC Supply D | 24 V / ≥1 A | Active Load VLOAD_POS_1 (via TA) |
| DC Supply E | 12 V / ≥1 A × 2 | Active Load VMEAS reference (via TA) |
| DMM | ±0.1% accuracy or better | Rail and signal measurements |
| Laptop / PC | SSH client | Accordion CLI |
| Ethernet PD load | PoE PD-capable | PT-POE.01, PT-POE.03 |
| Calibrated voltage source | ±0.1% accuracy or better | AIN stimulus (PT-SIG.02) |
| Oscilloscope (optional) | ≥20 MHz | PWM signal verification |

### Cables & Adapters

| Item | ESH/EPN | Used For |
|------|---------|---------|
| DSUB-25 Cable | EPN1000683 | Fixture Link ↔ Fixture Electronics |
| Sleeved Coax Cable | ESH10000614 | N-Top ↔ Fixture Electronics |
| Sparrow Test Adapter | ESH10000654 R0 | All TA-routed signals and power |
| Loopback wires (J5: pin 3–4, 5–6, 7–8, 9–10) | — | MPIO ↔ FIXED_LOAD test |
| Loopback wires (J5: pin 3–13, 5–14) | — | MPIO ↔ PWM test |
| Loopback wires (J5: pin 7–15, 9–17) | — | MPIO ↔ LATCH test |
| Loopback wires (J6 ↔ J7 per wiring diagram) | — | FE_MPIO / audio cross-check |

### Modules Required

| ESH | Product | Rev | Notes |
|-----|---------|-----|-------|
| ESH10000182 | Accordion (Agent Bare) — hosts RPi4B | — | |
| ESH10000534 | PoE | R4 | Fitted inside Accordion |
| ESH10000535 | Sparrow N-Top | R3 | |
| ESH10000536 | Active Load | R2 | |
| ESH10000540 | Sparrow Fixture Electronics PCBA | R3 | |
| ESH10000543 | Fixture Link | R2 | |
| ESH10000544 | Front Panel | — | ⚠️ NotApproved in MES |
| ESH10000571 | N-Top Connector Housing | — | |
| ESH10000582 | USB PD 100W PSU (Accordion internal) | — | |
| ESH10000654 | Sparrow Test Adapter | R0 | ⚠️ Verification pending |
| EGP10001723 | 20 Position Receptacle Connector | — | |
| EPN1000683 | DSUB-25 Cable | — | |
| ESH10000614 | Sleeved Coax Cable | — | |

---

## DUT Record

Fill in before starting. Transfer to DUT log after test.

| Field | Value |
|-------|-------|
| DUT Serial Number | |
| Accordion Serial Number | |
| Fixture Electronics Serial Number | |
| N-Top Serial Number | |
| Fixture Link Serial Number | |
| Active Load Serial Number | |
| PoE Serial Number | |
| Firmware version (ATmega) | ⚠️ TBD (Open Item 7) |
| Tester | |
| Date | |

---

## 1. Pre-Power Visual Inspection (PT-M)

> Perform before applying any power. Stop and record fault if any step fails.

| Step | Description | Pass Criteria | PT Ref | Result |
|------|-------------|---------------|--------|--------|
| M.01 | Verify all sub-assemblies installed: Accordion A2, Fixture Electronics + Active Load (ESH10000636 incl. PCBA R3), IDC N-Top (ESH10000634 R3), Sparrow N-Top (R3), Fixture Link (R2), PoE (R4) | All present and correctly seated | PT-M.00 | |
| M.02 | Inspect all board-to-board connectors — no bent pins visible | All seated; no visible damage | PT-M.01 | |
| M.03 | Confirm Fixture Link silkscreen revision | Reads "R2" | PT-M.02 | |
| M.04 | Confirm DSUB-25 Cable (EPN1000683) connected between Fixture Link and Fixture Electronics | Cable fitted; latches engaged | — | |
| M.05 | Confirm Sleeved Coax Cable (ESH10000614) connected between N-Top and Fixture Electronics | Cable seated at both ends | — | |

---

## 2. Hardware Setup

1. Attach Sparrow Test Adapter (ESH10000654 R0) per TA installation guide.
2. Connect DC Supply A (20 V) to TA 20 V input. **Do not switch on yet.**
3. Connect DC Supply B (56 V) to TA PoE VIN connector. **Do not switch on yet.**
4. Connect DC Supply C (24 V) to TA VLOAD_POS_0. **Do not switch on yet.**
5. Connect DC Supply D (24 V) to TA VLOAD_POS_1. **Do not switch on yet.**
6. Connect Ethernet cable from test PC to Accordion ETH IN.
7. Confirm all DMM leads are at rest.

---

## 3. Power-On and System Rails

| Step | Action | Pass Criteria | PT Ref | Measured | Result |
|------|--------|---------------|--------|----------|--------|
| PWR.01 | Switch DC Supply A ON (20 V). Confirm POWER LED illuminates on front panel | POWER LED blue | PT-COS.00 | — | |
| PWR.02 | Measure VDD at Fixture Link TA probe point (DMM) | 19.0–21.0 V | PT-PWR.00 | | |
| PWR.03 | Assert PWR_EN via Accordion GPIO. Measure VOUT (eFuse output) at TA probe point (DMM) | 19.0–21.0 V | PT-PWR.01 | | |
| PWR.04 | Measure 12 V DC/DC rail at Fixture Electronics TA probe point (DMM) | 11.4–12.6 V | PT-PWR.02 | | |
| PWR.05 | Measure 12 V rail at N-Top TA probe point (DMM) | 11.4–12.6 V | PT-PWR.03 | | |
| PWR.06 | Measure 5 V rail at TA probe point (DMM) | 4.75–5.25 V | PT-PWR.04 | | |
| PWR.07 | Measure 3V3 rail at TA probe point (DMM) | 3.218–3.383 V | PT-PWR.05 | | |
| PWR.08 | Measure VREF_BUF at N-Top TA probe point (DMM) | 2.497–2.504 V | PT-PWR.06 | | |
| PWR.09 | Measure +18 V rail at N-Top TA probe point (DMM) | 17.82–18.18 V | PT-PWR.07 | | |
| PWR.10 | Measure −18 V rail at N-Top TA probe point (DMM) | −18.18 to −17.82 V | PT-PWR.08 | | |

---

## 4. Accordion Software Startup

Connect to the Accordion via SSH:

```
ssh A00<serial>.local -l accordion
password: RpiAccordionUno

sudo systemctl stop accordion.service
cd hw
sudo dotnet AccordionQ2.dll
```

The CLI prompt is `§`. All subsequent Accordion commands are entered at this prompt.

> ⚠️ Specific CLI command syntax (ADC reads, GPIO control, PSU setpoints, I2C scans) is per AccordionQ2 API
> documentation — Open Item 3 in PRODUCTION_TEST_PLAN.md. Steps below describe what to do; substitute
> the correct CLI syntax once confirmed.

| Step | Action | Pass Criteria | Result |
|------|--------|---------------|--------|
| SW.01 | SSH to Accordion. | Shell prompt obtained | |
| SW.02 | Stop accordion.service; launch AccordionQ2.dll. | `§` prompt appears | |
| SW.03 | Run `list`. Confirm all expected modules are reported. | ⚠️ TBD — expected list output not yet defined (Open Item 1) | |
| SW.04 | Verify DUT serial number programmed in IDPROM. | ⚠️ TBD — serial number format not yet defined (Open Item 7) | |

---

## 5. Programmable Power Supply Spot Check (PT-PSU)

> Set one setpoint per external rail via Accordion CLI. Read VMON ADC.

| Step | Signal | Nominal | Pass Criteria | PT Ref | Measured | Result |
|------|--------|---------|---------------|--------|----------|--------|
| PSU.01 | Enable 12V_EXT; read VMON ADC | 12.0 V | 11.4–12.6 V (±5%) | PT-PSU.00 | | |
| PSU.02 | Set VADJ_EXT = 3.3 V; read VMON ADC | 3.3 V | 3.218–3.383 V (±2.5%) | PT-PSU.01 | | |
| PSU.03 | Set VIO_EXT = 3.3 V; read VMON ADC | 3.3 V | 3.218–3.383 V (±2.5%) | PT-PSU.02 | | |
| PSU.04 | Enable 3V3_EXT; read VMON ADC | 3.3 V | 3.218–3.383 V (±2.5%) | PT-PSU.03 | | |
| PSU.05 | Enable 1V8_EXT; read VMON ADC | 1.8 V | 1.755–1.845 V (±2.5%) | PT-PSU.04 | | |

---

## 6. Communication Bus and Firmware (PT-COMM / PT-FW)

| Step | Description | Pass Criteria | PT Ref | Result |
|------|-------------|---------------|--------|--------|
| COMM.01 | I2C scan: Fixture Link GPIO expander | ACK at 0x20 | PT-COMM.00 | |
| COMM.02 | I2C: Fixture Link EEPROM — write 1 byte and read back | ACK at 0x50; readback matches written value | PT-COMM.01 | |
| COMM.03 | Assert I2C_EN via Fixture Link expander; scan downstream I2C bus | ATmega @ 0x30, LED driver @ 0x14 or 0x0C, expander @ 0x20, IDPROM @ 0x50 — all ACK | PT-COMM.02 | |
| COMM.04 | SPI: access both AD5592R devices on Fixture Electronics | Read/write both devices without error | PT-COMM.03 | |
| FW.01 | Confirm ATmega responds on I2C at 0x30 | ATmega ACKs | PT-FW.00 | |
| FW.02 | Write and read back 1 byte to IDPROM | Write succeeds; readback matches | PT-FW.01 | |

---

## 7. J4 — IO 0-15: AIN Channels

> J4 carries precision differential analog input channels AIN_P/N_CH1–8.
> Pin 1 = 5V, pin 2 = 12V, pins 19/20 = GND.

**Rail verification (DMM):**

| Step | Measurement | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J4.01 | J4 pin 1 (5V) → J4 pin 19 (GND) | 4.875–5.125 V (±2.5%) | PT-PWR.04 | | |
| J4.02 | J4 pin 2 (12V) → J4 pin 20 (GND) | 11.70–12.30 V (±2.5%) | PT-PWR.02 | | |

**AIN spot check:**

| Step | Description | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J4.03 | Apply 1.0 V stimulus to AIN_P_CH1 (J4 pin 3); connect AIN_N_CH1 (J4 pin 5) to GND; read ADC via Accordion at gain G2 | 0.997–1.003 V (±0.34%) | PT-SIG.02 | | |

**AIN calibration:**

| Step | Description | Pass Criteria | Result |
|------|-------------|---------------|--------|
| J4.04 | Run AIN calibration for all 8 channels — connect all channels to calibration rail; run calibration software | ⚠️ TBD — calibration procedure, instrument setup, and software command not yet defined (Open Item 2) | |

---

## 8. J5 — IO 16-31: MPIO, Fixed Load, PWM, LATCH, TACHO, VREF

> J5 carries MPIO_0–3, FIXED_LOAD_0–3, TACHO_0–1, PWM_0–1, LATCH_0–1, VREF.
> Pin 1 = 5V, pin 2 = 12V, pin 16/18 = VREF, pins 19/20 = GND.

**Rail and VREF verification (DMM):**

| Step | Measurement | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J5.01 | J5 pin 1 (5V) → J5 pin 19 (GND) | 4.875–5.125 V (±2.5%) | PT-PWR.04 | | |
| J5.02 | J5 pin 2 (12V) → J5 pin 20 (GND) | 11.70–12.30 V (±2.5%) | PT-PWR.02 | | |
| J5.03 | J5 pin 16 (VREF) → J5 pin 19 (GND) | 2.497–2.504 V (±0.14%) | PT-PWR.06 | | |

**MPIO spot check:**

| Step | Description | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J5.04 | Via Accordion: output 2.5 V on MPIO_0 (DAC); read back via ADC | 2.475–2.525 V (±1%) | PT-SIG.00 | | |

**MPIO ↔ FIXED_LOAD loopback:**

> Wire J5: pin 3–4 (MPIO_0 ↔ FIXED_LOAD_0), 5–6, 7–8, 9–10.

| Step | Description | Pass Criteria | Measured | Result |
|------|-------------|---------------|----------|--------|
| J5.05a | Output 4.0 V on all MPIO_[0:3] via Accordion | — | | |
| J5.05b | Read all FIXED_LOAD_[0:3] ADC via Accordion | 3.909–4.091 V (±2.3%) | | |
| J5.05c | Apply 2k2 load on all FIXED_LOAD_[0:3] via Accordion | — | | |
| J5.05d | Read all FIXED_LOAD_[0:3] ADC again | ⚠️ TBD — expected delta with 2k2 load not confirmed (Open Item 3) | | |

**PWM loopback:**

> Wire J5: pin 3–13 (MPIO_0 ↔ PWM_0), pin 5–14 (MPIO_1 ↔ PWM_1).

| Step | Description | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J5.06a | Set PWM_VCCO = 3.3 V via Accordion | — | — | | |
| J5.06b | Set PWM_0 and PWM_1 to 1 kHz, 50% duty cycle | — | PT-SIG.05 | | |
| J5.06c | Confirm PWM signal present — verify on scope or confirm no fault flag | PWM signal present; no fault | PT-SIG.05 | — | |
| J5.06d | Read MPIO_[0:1] ADC average (DC component of PWM) | ⚠️ TBD — expected average ≈1.65 V not confirmed (Open Item 4) | — | | |

> Note: Unit Test Specification proposed testing at minimum PWM frequency (~280 Hz). This frequency is
> unconfirmed. 1 kHz is used above per PRODUCTION_TEST_PLAN.md PT-SIG.05.

**TACHO:**

| Step | Description | Pass Criteria | PT Ref | Result |
|------|-------------|---------------|--------|--------|
| J5.07 | Inject 1 kHz signal on TACHO_0 (J5 pin 11) via TA at VCCO 3.3 V; read Tach count via Accordion | Tach count correct for 1 kHz input | PT-SIG.06 | |

**LATCH:**

> Wire J5: pin 7–15 (MPIO_2 ↔ LATCH_0), pin 9–17 (MPIO_3 ↔ LATCH_1).

| Step | Description | Pass Criteria | Result |
|------|-------------|---------------|--------|
| J5.08a | Set LATCH_[0:1] to trigger on HIGH; pull = DOWN. Reset LATCH_[0:1] | — | |
| J5.08b | Read LATCHED_VALUE_[0:1] | LOW | |
| J5.08c | Output 3.3 V on MPIO_[2:3] via Accordion | — | |
| J5.08d | Read LATCHED_VALUE_[0:1] | HIGH | |
| J5.08e | Set LATCH_[0:1] to trigger on LOW; pull = UP. Reset LATCH_[0:1] | — | |
| J5.08f | Read LATCHED_VALUE_[0:1] | HIGH | |
| J5.08g | Output 0 V on MPIO_[2:3] | — | |
| J5.08h | Read LATCHED_VALUE_[0:1] | LOW | |

---

## 9. J6 — IO 32-47: Audio Signals

> J6 carries MIC_IN_L/R (differential with switchable 2k2/680R load), LINE_OUT_L/R (differential), AUDIO_GND.
> Pin 1 = 5V, pin 2 = 12V, pins 19/20 = GND.

**Rail verification (DMM):**

| Step | Measurement | Pass Criteria | Measured | Result |
|------|-------------|---------------|----------|--------|
| J6.01 | J6 pin 1 (5V) → J6 pin 19 (GND) | 4.875–5.125 V (±2.5%) | | |
| J6.02 | J6 pin 2 (12V) → J6 pin 20 (GND) | 11.70–12.30 V (±2.5%) | | |

**MIC bias load:**

| Step | Description | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J6.03 | Activate MIC_BIAS_LOAD_L via Accordion; read MIC_IN_L current via ADC | 2.221–2.325 mA (±2.3%) | PT-SIG.04 | | |

> Note: Full audio signal characterization (MIC/LINE) is sub-assembly scope (ESH10000540). Not tested at production level.

---

## 10. J7 — IO 48-63: FE_MPIO, GPIO

> J7 carries FE_MPIO_0–11, GPIO_0–3.
> Pin 1 = 5V, pin 2 = 12V, pins 19/20 = GND.

**Rail verification (DMM):**

| Step | Measurement | Pass Criteria | Measured | Result |
|------|-------------|---------------|----------|--------|
| J7.01 | J7 pin 1 (5V) → J7 pin 19 (GND) | 4.875–5.125 V (±2.5%) | | |
| J7.02 | J7 pin 2 (12V) → J7 pin 20 (GND) | 11.70–12.30 V (±2.5%) | | |

**FE_MPIO spot check:**

| Step | Description | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| J7.03 | Via Accordion: output 2.5 V on FE_MPIO_0 (DAC); read back via ADC | 2.475–2.525 V (±1%) | PT-SIG.01 | | |

**FE_MPIO ↔ Audio loopback (wire J6 to J7):**

> Wire J6 to J7 per wiring diagram in Unit Test Specification §IO 48-63.
> Connect Male 9-pin D-SUB (Fixture Electronics) to Female.

| Step | Description | Pass Criteria | Measured | Result |
|------|-------------|---------------|----------|--------|
| J7.04a | Output 4.0 V on MPIO_[0:3] (J5) via Accordion | — | | |
| J7.04b | Read MPIO_[8:11] (J7) ADC via Accordion | 3.909–4.091 V (±2.3%) | | |
| J7.04c | Read VMEAS_MIC_IN_L[+/−] and VMEAS_MIC_IN_R[+/−] via Accordion | ⚠️ TBD — expected values not yet defined (Open Item 6) | | |

**GPIO:**

| Step | Description | Pass Criteria | PT Ref | Result |
|------|-------------|---------------|--------|--------|
| J7.05 | Drive USR_GPIO_1 HIGH via Accordion; read back | Reads HIGH | PT-SIG.07 | |

---

## 11. J8 — IO 64-79: Active Load & PSU Rails

> J8 carries VLOAD_POS/NEG_0/1 (Active Load terminals), VREM_0/1, VPSU_0/1 (optional PSU), VSENSE±_0/1.
> Pin 1 = 5V, pin 2 = 12V, pins 17–20 = GND.

**Rail verification (DMM):**

| Step | Measurement | Pass Criteria | Measured | Result |
|------|-------------|---------------|----------|--------|
| J8.01 | J8 pin 1 (5V) → J8 pin 17 (GND) | 4.875–5.125 V (±2.5%) | | |
| J8.02 | J8 pin 2 (12V) → J8 pin 18 (GND) | 11.70–12.30 V (±2.5%) | | |

> Active Load functional test is in §13 (PT-AL).
> PSU optional output (VPSU_0/1) is deferred — PWR-24, see PRODUCTION_TEST_PLAN.md.

---

## 12. J9 — IO 80-95: I2C, RS485, External Power Rails

> J9 carries SCL/SDA (SLV and MSTR), V_I2C, RS485_RX+/−, RS485_TX+/−, 1V8_EXT, 3V3_EXT, 12V_EXT, VADJ.
> Pin 1 = 5V, pin 2 = 12V, pins 19/20 = GND.

**Rail verification (DMM):**

| Step | Measurement | Pass Criteria | Measured | Result |
|------|-------------|---------------|----------|--------|
| J9.01 | J9 pin 1 (5V) → J9 pin 19 (GND) | 4.875–5.125 V (±2.5%) | | |
| J9.02 | J9 pin 2 (12V) → J9 pin 20 (GND) | 11.70–12.30 V (±2.5%) | | |

**RS485:**

| Step | Description | Pass Criteria | PT Ref | Result |
|------|-------------|---------------|--------|--------|
| J9.03 | Drive logic '1' on RS485_TX (J9 pin 10) via TA driver or loopback; read ADC via Accordion | ADC reads >0.2 V | PT-SIG.08 | |

> I2C functionality is covered in §6 (COMM). External power rail accuracy is covered in §5 (PSU).

---

## 13. Active Load (PT-AL)

> Apply DC supplies to Active Load via TA. Both channels tested.
> ⚠️ Confirm no short on VLOAD_POS_x before enabling supply.

| Step | Description | Signal | Nominal | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|--------|---------|---------------|--------|----------|--------|
| AL.01 | Apply 24 V to VLOAD_POS_0 (DC Supply C). Set CH0 to sink 100 mA via Accordion; read IMEAS_CH0 | IMEAS_CH0 | 100 mA | 99–101 mA (±1%) | PT-AL.00 | | |
| AL.02 | With 12 V on VLOAD_POS_0 (DC Supply E); read VMEAS_CH0 via Accordion | VMEAS_CH0 | 12.0 V | 11.76–12.24 V (±2%) | PT-AL.01 | | |
| AL.03 | Apply 24 V to VLOAD_POS_1 (DC Supply D). Set CH1 to sink 100 mA via Accordion; read IMEAS_CH1 | IMEAS_CH1 | 100 mA | 99–101 mA (±1%) | PT-AL.02 | | |
| AL.04 | With 12 V on VLOAD_POS_1; read VMEAS_CH1 via Accordion | VMEAS_CH1 | 12.0 V | 11.76–12.24 V (±2%) | PT-AL.03 | | |

---

## 14. Power over Ethernet (PT-POE)

> ⚠️ Safety: do not switch PoE output polarity while a device is connected to ETH OUT.

| Step | Description | Pass Criteria | PT Ref | Measured | Result |
|------|-------------|---------------|--------|----------|--------|
| POE.01 | Switch DC Supply B ON (56 V). Assert PoE ON/OFF GPIO from Accordion. Verify no fault indication | 53.2–58.8 V at VIN; no fault; LED active | PT-POE.00 | | |
| POE.02 | Connect Ethernet PD load to ETH OUT. Verify PoE negotiation completes | Cyan LED active; PD load powered | PT-POE.01 | — | |
| POE.03 | Read VMEAS via Accordion | 54.6–57.4 V (±2.5%) | PT-POE.02 | | |
| POE.04 | Draw ~100 mA from PD load. Read IMEAS via Accordion | 97–103 mA (±3%) | PT-POE.03 | | |

---

## 15. Cosmetics & LEDs (PT-COS)

| Step | Description | Pass Criteria | PT Ref | Result |
|------|-------------|---------------|--------|--------|
| COS.01 | Assert LED_BLUEn via Fixture Link expander | POWER LED illuminates blue | PT-COS.00 | |
| COS.02 | Assert UART_ENn via Fixture Link expander | RS-232 LED illuminates blue | PT-COS.01 | |
| COS.03 | Write LP5012 LED driver registers via I2C | At least one user LED channel responds to register write | PT-COS.02 | |
| COS.04 | Visual inspection of front panel | No scratches, dents, or missing labels | — | |

---

## 16. Power-Down

1. Disconnect Ethernet PD load from ETH OUT.
2. Switch DC Supply B OFF (56 V / PoE).
3. Switch DC Supply C and D OFF (24 V / Active Load).
4. De-assert PWR_EN via Accordion. Confirm VOUT < 1 V before proceeding.
5. Switch DC Supply A OFF (20 V).
6. Exit AccordionQ2.dll (`Ctrl+C`).
7. Remove all loopback wires.
8. Disconnect TA from DUT.

---

## 17. Result Summary

Fill in after completing all sections.

| Section | Steps | Pass | Fail | TBD/Skip |
|---------|-------|------|------|----------|
| Pre-Power (M) | 5 | | | |
| Power-On (PWR) | 10 | | | |
| Software Startup (SW) | 4 | | | 2 TBD |
| PSU Spot Check (PSU) | 5 | | | |
| Communication / FW | 6 | | | |
| J4 — AIN | 4 | | | 1 TBD |
| J5 — MPIO / PWM / LATCH / TACHO | 15 | | | 2 TBD |
| J6 — Audio | 3 | | | |
| J7 — FE_MPIO / GPIO | 5 | | | 1 TBD |
| J8 — Active Load rails | 2 | | | |
| J9 — I2C / RS485 / PSU | 3 | | | |
| Active Load (AL) | 4 | | | |
| PoE (POE) | 4 | | | |
| Cosmetics (COS) | 4 | | | |
| **Total** | **74** | | | **6 TBD** |

**Overall result:** ☐ PASS  ☐ FAIL  ☐ INCOMPLETE (TBD items outstanding)

Tester: _________________________________  Date: _______________

---

## 18. Open Items

Items marked ⚠️ TBD throughout this procedure. Must be resolved before procedure can be fully executed.

| # | Step(s) | Issue | Owner |
|---|---------|-------|-------|
| 1 | SW.03 | Accordion `list` — expected module output not defined | Martin Johansson |
| 2 | J4.04 | AIN calibration procedure not written — instruments, software, exe TBD | Martin Johansson |
| 3 | J5.05d | FIXED_LOAD readback delta with 2k2 load applied — expected value not confirmed | Martin Johansson |
| 4 | J5.06d | PWM 50% duty at 1 kHz → MPIO ADC average reading — expected ≈1.65 V not confirmed | Martin Johansson |
| 5 | J7.04c | VMEAS_MIC_IN_L/R expected values not defined | Martin Johansson |
| 6 | SW.04, FW.02 | DUT serial number format and IDPROM content not defined | Martin Johansson |
