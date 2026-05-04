---
project: ESH10000543
product: Fixture Link
revision: R2
type: Design + Verification
created: 2026-05-04
last_updated: 2026-05-04
---

# Specification: Fixture Link R2

## Scope

Fixture Link is an interface board between Accordion and Fixture Electronics. This document defines the functional requirements and acceptance criteria for revision R2. Requirements are derived from the R1 functional verification plan.

---

## Requirements

| Req ID | Category | Requirement | Acceptance Criteria | Test Case(s) | Status |
|--------|----------|-------------|---------------------|--------------|--------|
| FL-M01 | Mechanical | All NM components shall not be populated | No NM component mounted per BOM | M.00 | Pending |
| FL-M02 | Mechanical | Board shall fit mechanically with Sparrow front panel | No mechanical interference | M.01 | Pending |
| FL-P01 | Power | VDD rail shall be 20 V ±5% | 19.00–21.00 V measured at VDD | P.00 | Pending |
| FL-P02 | Power | 5V rail shall be 5 V ±5% | 4.75–5.25 V measured at 5V | P.01 | Pending |
| FL-P03 | Power | 3V3 rail shall be 3.3 V ±2.5% | 3.218–3.383 V measured at 3V3 | P.02 | Pending |
| FL-P04 | Power | VID rail shall be 3.3 V ±2.5% | 3.218–3.383 V measured at VID | P.03 | Pending |
| FL-P05 | Power | VOUT shall be 20 V ±5% when PWR_EN asserted | 19.00–21.00 V measured at VOUT | P.04 | Pending |
| FL-P06 | Power | eFuse PG shall assert when VOUT ≥ 18.3 V ±2.5% | PG asserts at 17.84–18.76 V | P.05 | Pending |
| FL-P07 | Power | eFuse current limit (ILM) shall be 2.22 A ±2.5% | PG de-asserts at 2.165–2.276 A | P.06 | Pending |
| FL-P08 | Power | eFuse OVLO shall trip at 22.6 V ±2.5% | VOUT shuts off at 22.04–23.17 V | P.07 | Pending |
| FL-P09 | Power | VOUT slew rate shall be ≥0.090 V/ms at no load | Measured slew ≥ 0.090 V/ms | P.08 | Pending |
| FL-P10 | Power | VOUT slew rate shall be ≥0.090 V/ms at 430 mA load | Measured slew ≥ 0.090 V/ms | P.09 | Pending |
| FL-P11 | Power | VOUT start behaviour at 500 mA preload (characterisation) | Record observed behaviour; R1 result: does not start | P.10 | Pending |
| FL-P12 | Power | ITIMER shall maintain VOUT for ≥18.5 ms at step load 0→2.2 A | Measured ITIMER ≥ 18.5 ms | P.11 | Pending |
| FL-C01 | Control IO | I2C expander shall be accessible at address 0x20 | Device ACKs at 0x20 on I2C bus | C.00 | Pending |
| FL-C02 | Control IO | EEPROM shall be accessible at address 0x50 and programmable | Device ACKs at 0x50; write/read-back verified | C.00 | Pending |
| FL-C03 | Control IO | Power LED shall respond to LED_BLUEn | LED state follows LED_BLUEn signal | C.01 | Pending |
| FL-C04 | Control IO | RS-232 LED shall respond to UART_ENn | LED state follows UART_ENn signal | C.02 | Pending |
| FL-C05 | Control IO | READY and PIDET shall exhibit correct states with Sparrow FE connected | READY low when I2C_EN low; PIDET low | C.03 | Pending |
| FL-C06 | Control IO | I2C transceivers shall pass traffic to Sparrow FE when I2C_EN asserted | All expected Sparrow FE I2C devices visible on bus | C.04 | Pending |
| FL-C07 | Control IO | U7 open-drain outputs shall present valid logic levels at J1 | SRQn, INTERRUPTn, SRQ1–4n_BUF show valid levels — confirms Accordion pull-ups (closes schematic review F-02) | C.05 | Pending |
| FL-C08 | Control IO | UART interface shall pass loopback test | RXD, TXD, RTS, CTS all loopback correctly | C.06 | Pending |
| FL-M03 | Mechanical | DSUB oblong hole shall have no solder paste (R2 change #1) | Visual: no solder paste visible in DSUB oblong hole | M.02 | Pending |
| FL-M04 | Mechanical | DSUB connector shall be correctly positioned after 1.1 mm shift (R2 change #5) | DSUB seats correctly in panel cutout; no interference | M.03 | Pending |
| FL-C09 | Control IO | UART pull-up resistors R6 and R39 shall be populated; pull-up voltage present on UTXD and DRXD (R2 change #2/#3) | R6 and R39 mounted; ≥2 V measured on UTXD and DRXD with no driver active | C.07 | Pending |
| FL-M05 | Mechanical | PCB silkscreen revision marking shall read R2 (R2 change #4) | "R2" visible on PCB silkscreen | M.04 | Pending |

---

## Design Scope

**In Scope:**
- Power supply distribution and eFuse (U3) parametrics
- UART buffering (U1, U2) and RS-232 interface (U16)
- I2C differential repeaters (U8–U11, 4 channels)
- I2C I/O expander (U14) and EEPROM (U15)
- Open-drain output buffer (U7)
- Status LED indication

**Out of Scope:**
- Production test (separate procedure)
- Compliance / regulatory testing
- Thermal / environmental stress testing

---

## Acceptance Criteria

- All requirements marked "Pass" in the traceability table above.
- No open schematic or layout review findings without disposition.
- DUT log complete and traceable.

---

## Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| R2 | 2026-05-04 | MJ | Populated requirements from R1 verification plan; expanded scope to include verification |
| R2 | 2026-05-04 | MJ | Added FL-M03, FL-M04, FL-M05, FL-C09 to cover R2 design changes from DesignLog Rev 1 tab |

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Design Engineer | | | |
| Reviewer | | | |
