---
project: ESH10000543
revision: R2
created: 2026-05-04
type: Verification Plan
basis: R1 verification plan (Verification_FixtureLink.xlsx) — confirmed valid for R2 2026-05-04
---

# Verification Plan: Fixture Link R2

## Overview

Functional verification of Fixture Link R2 against the requirements defined in SPECIFICATION.md. Test cases are carried forward from the R1 manual verification plan with no scope changes.

---

## Test Scope

### In Scope
- Mechanical: no-mount population check, panel fit
- Power: all supply rails (VDD, 5V, 3V3, VID, VOUT), eFuse parametrics (PG, ILM, OVLO, slew rate, ITIMER)
- Control IO: I2C expander, EEPROM, status LEDs, I2C transceivers, UART loopback
- R2-specific: verify U7 open-drain output levels on SRQn, INTERRUPTn, SRQ1–4n_BUF nets (schematic review finding F-02)

### Out of Scope
- Production test (separate procedure)
- Compliance / regulatory testing
- Thermal / environmental stress

---

## Test Environment

| Equipment / Tool | Purpose |
|-----------------|---------|
| DMM | Rail voltage measurements (P.00–P.04) |
| Adjustable DC supply | VDD source (set to 20 V) |
| Oscilloscope | Slew rate measurements (P.08–P.10), ITIMER (P.11) |
| DC electronic load | VOUT load tests (P.06, P.09, P.10, P.11) |
| I2C host (Accordion or bench controller) | I2C expander, EEPROM, transceiver tests (C.00–C.05) |
| UART loopback cable / host | UART test (C.06) |
| Sparrow FE PCB | I2C transceiver test with real downstream devices (C.03–C.04) |

---

## Test Cases

### Mechanical

| ID | Step | Function | Test Procedure | Signals | Nominal | Unit | Tol | Pass Criteria | Req ID |
|----|------|----------|---------------|---------|---------|------|-----|---------------|--------|
| M.00 | No Mounts | No Mounts | Verify all NM components are not populated per BOM | — | — | — | — | No NM component mounted | FL-M01 |
| M.01 | Mechanical Fit | Panel Fit | Confirm board fits mechanically with Sparrow front panel; no interference | — | — | — | — | No mechanical interference | FL-M02 |
| M.02 | DSUB Solder Paste | DSUB Oblong Hole | Inspect DSUB connector oblong hole; confirm no solder paste present (R2 change #1) | — | — | — | — | No solder paste in oblong hole | FL-M03 |
| M.03 | DSUB Position | DSUB 1.1 mm Shift | Verify DSUB connector seats correctly in panel cutout after 1.1 mm position change; no interference (R2 change #5) | — | — | — | — | DSUB correctly positioned; no interference | FL-M04 |
| M.04 | Rev Marking | Silkscreen | Inspect PCB silkscreen; confirm revision marking reads R2 (R2 change #4) | — | — | — | — | Silkscreen reads R2 | FL-M05 |

### Power

| ID | Step | Function | Test Procedure | Signals | Nominal | Unit | Tol | Pass Criteria | Req ID |
|----|------|----------|---------------|---------|---------|------|-----|---------------|--------|
| P.00 | VDD power | VDD Supply | Measure VDD rail with DMM | VDD | 20.000 | V | ±5% | 19.00–21.00 V | FL-P01 |
| P.01 | 5V power | 5V Supply | Measure 5V rail with DMM | 5V | 5.000 | V | ±5% | 4.75–5.25 V | FL-P02 |
| P.02 | 3V3 power | 3V3 Supply | Measure 3V3 rail with DMM | 3V3 | 3.300 | V | ±2.5% | 3.218–3.383 V | FL-P03 |
| P.03 | VID power | VID Supply | Measure VID rail with DMM | VID | 3.300 | V | ±2.5% | 3.218–3.383 V | FL-P04 |
| P.04 | VOUT power | eFuse output | Assert PWR_EN; measure VOUT with DMM | PWR_EN, VOUT | 20.000 | V | ±5% | 19.00–21.00 V | FL-P05 |
| P.05 | VOUT power | eFuse PG | Assert PWR_EN; ramp VDD up from 0 V; measure VDD level when PG asserts | PG | 18.300 | V | ±2.5% | 17.84–18.76 V | FL-P06 |
| P.06 | VOUT power | eFuse ILM | Assert PWR_EN at 20 V; increase load on VOUT until PG de-asserts; record current | ILM | 2.220 | A | ±2.5% | 2.165–2.276 A | FL-P07 |
| P.07 | VOUT power | eFuse OVLO | Assert PWR_EN; ramp VDD above 20 V; measure VDD level when VOUT shuts off | OVLO | 22.600 | V | ±2.5% | 22.04–23.17 V | FL-P08 |
| P.08 | VOUT power | Slew @ no load | Assert PWR_EN at no load; measure VOUT slew rate (0 V → 20 V) with oscilloscope | DVDT | 0.090 | V/ms | — | ≥0.090 V/ms | FL-P09 |
| P.09 | VOUT power | Slew @ 430 mA | Assert PWR_EN with 430 mA load; measure VOUT slew rate (0 V → 20 V) | DVDT | 0.090 | V/ms | — | ≥0.090 V/ms | FL-P10 |
| P.10 | VOUT power | Slew @ 500 mA | Assert PWR_EN with 500 mA load; observe if VOUT starts | DVDT | — | — | — | **Known R1 result: eFuse does not start at 500 mA preload. Record observed behaviour.** | FL-P11 |
| P.11 | VOUT power | eFuse ITIMER | Assert PWR_EN; apply step load 0 → 2.2 A; measure time before VOUT shuts off | ITIMER | 18.500 | ms | — | ≥18.5 ms | FL-P12 |

### Control IO

| ID | Step | Function | Test Procedure | Signals | Pass Criteria | Req ID |
|----|------|----------|---------------|---------|---------------|--------|
| C.00 | IO Expander | I2C Expander + EEPROM | Scan I2C bus; confirm expander at 0x20 and EEPROM at 0x50; write and read back EEPROM | SDA, SCL | Devices ACK at 0x20 and 0x50; EEPROM write/read-back passes | FL-C01, FL-C02 |
| C.01 | IO Expander | LED (Power) | Assert LED_BLUEn via I2C expander; confirm Power LED illuminates blue | LED_BLUEn | LED follows signal | FL-C03 |
| C.02 | IO Expander | LED (RS-232) | Assert UART_ENn via I2C expander; confirm RS-232 LED illuminates blue | UART_ENn | LED follows signal | FL-C04 |
| C.03 | IO Expander | I2C Transceivers | Connect Sparrow FE to J1; observe READY and PIDET states | READY, PIDET | READY low when I2C_EN low; PIDET low (known R1 behaviour: signals not functionally used) | FL-C05 |
| C.04 | IO Expander | I2C Transceivers | Assert I2C_EN; scan I2C bus; confirm all Sparrow FE devices visible | I2C_EN*, SDA*, SCL* | All expected Sparrow FE I2C devices ACK | FL-C06 |
| C.05 | IO Expander | SRQ Interrupts | Assert SRQ signals from Sparrow FE; observe SRQn, INTERRUPTn, SRQ1–4n_BUF at J1 | SRQn, INTERRUPTn, SRQ1–4n_BUF | **R2 addition (F-02):** Verify open-drain output levels are valid logic levels. Pull-ups confirmed on Accordion CM32 module (MJ, 2026-05-04) — bench measurement confirms design intent. Note R1 result: signals were observed but not functionally used. | FL-C07 |
| C.06 | UART | UART Loopback | Connect UART loopback; test RXD, TXD, RTS, CTS | RXD, TXD, RTS, CTS | All four signals loopback correctly | FL-C08 |
| C.07 | UART Pull-ups | R6, R39 Population | Inspect PCB: confirm R6 and R39 are mounted. Measure voltage on UTXD and DRXD with no driver active (R2 changes #2 & #3) | UTXD, DRXD | ≥2 V (pull-up active) | V | — | R6 and R39 mounted; UTXD and DRXD measure ≥2 V | FL-C09 |

---

## Test Coverage Matrix

| Req ID | Requirement | Test Case(s) | Status |
|--------|-------------|--------------|--------|
| FL-M01 | NM components not populated | M.00 | Pending |
| FL-M02 | Panel fit | M.01 | Pending |
| FL-P01 | VDD 20 V ±5% | P.00 | Pending |
| FL-P02 | 5V ±5% | P.01 | Pending |
| FL-P03 | 3V3 ±2.5% | P.02 | Pending |
| FL-P04 | VID ±2.5% | P.03 | Pending |
| FL-P05 | VOUT 20 V ±5% when PWR_EN | P.04 | Pending |
| FL-P06 | PG threshold 18.3 V ±2.5% | P.05 | Pending |
| FL-P07 | ILM current limit 2.22 A ±2.5% | P.06 | Pending |
| FL-P08 | OVLO 22.6 V ±2.5% | P.07 | Pending |
| FL-P09 | Slew rate ≥0.09 V/ms @ no load | P.08 | Pending |
| FL-P10 | Slew rate ≥0.09 V/ms @ 430 mA | P.09 | Pending |
| FL-P11 | eFuse behaviour @ 500 mA preload (characterisation) | P.10 | Pending |
| FL-P12 | ITIMER ≥18.5 ms @ step load 0→2.2 A | P.11 | Pending |
| FL-C01 | I2C expander accessible at 0x20 | C.00 | Pending |
| FL-C02 | EEPROM accessible at 0x50, programmable | C.00 | Pending |
| FL-C03 | Power LED responds to LED_BLUEn | C.01 | Pending |
| FL-C04 | RS-232 LED responds to UART_ENn | C.02 | Pending |
| FL-C05 | READY and PIDET correct with Sparrow FE | C.03 | Pending |
| FL-C06 | I2C transceivers pass traffic when I2C_EN | C.04 | Pending |
| FL-C07 | U7 open-drain output levels valid (pull-ups on Accordion) | C.05 | Pending |
| FL-C08 | UART loopback passes | C.06 | Pending |
| FL-M03 | DSUB oblong hole has no solder paste | M.02 | Pending |
| FL-M04 | DSUB position correct after 1.1 mm shift | M.03 | Pending |
| FL-M05 | PCB silkscreen reads R2 | M.04 | Pending |
| FL-C09 | UART pull-ups R6/R39 populated; UTXD and DRXD ≥2 V | C.07 | Pending |

---

## R1 Reference Results

Three DUTs tested in R1: A002708, A002709, A002712. All passed except:

| ID | R1 Result | Notes |
|----|-----------|-------|
| P.10 | Fail (accepted) | eFuse does not start with 500 mA preload — known limitation |
| C.05 | Pass (N/A) | SRQ interrupt signals observed but noted "not used" across all 3 DUTs |

See `DOCS/Verification_FixtureLink.xlsx` for full R1 measurements.

---

## Notes

- All test results are logged in **DUT_LOG.md** — immutable once written.
- C.05 is a required test for R2 to close schematic review finding F-02 (U7 pull-ups on Accordion).
- P.10 expected result is "does not start" — record actual behaviour for characterisation.
- M.02, M.03, M.04, C.07 are R2-specific additions derived from DesignLog_FixttureLink.xlsx Rev 1 tab (changes #1–#5). All must pass before R2 verification can be signed off.
