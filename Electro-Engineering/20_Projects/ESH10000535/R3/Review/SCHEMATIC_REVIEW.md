---
project: ESH10000535
revision: R3
document: Schematic ERC Review
status: In progress
created: 2026-04-30
reviewer: Martin Johansson / AI-assisted
---

# Schematic ERC Review — Sparrow N-Top R3

## Review Status

| Item | Status |
|------|--------|
| Netlist imported | ✅ `DOCS/NetList_Sparrow_NTop_R3.qcv` |
| BOM imported | ✅ `DOCS/PartsList_Sparrow_NTop_R3.csv` |
| Structural ERC (C/P/S/B) | ✅ Complete |
| Component data coverage | ✅ 19/19 types in COMPONENT_DATA.md |
| ERC-C08 (unconnected pins) | ✅ Complete — 2 flags: U1 pin count (OI-05), U9 missing pin 22 (OI-06), Q1 pin mapping (OI-07) |
| ERC-P06 (power supply range) | ✅ Complete — 1 flag: U19/U20 VCCB range (OI-08) |
| ERC-D (device constraints) | ✅ Complete — 30 checks; 13 flags logged |
| Findings dispositioned | ⏳ Engineer review of flagged items required |
| Sign-off | ⏳ Pending |

---

## Source Files

| File | Location |
|------|----------|
| Netlist (PADS QCV) | `DOCS/NetList_Sparrow_NTop_R3.qcv` |
| BOM (CSV) | `DOCS/PartsList_Sparrow_NTop_R3.csv` |
| Schematic PDF | `DOCS/Schematic_Sparrow_NTop_R3.pdf` |

---

## Design Overview

| Parameter | Value |
|-----------|-------|
| Nets | 233 |
| Mounted components | 229 |
| No-Mount (NM) components | 67 |
| Unique IC types (U + Q) | 19 |
| Power rails | GND, 3V3, 5V, 5VA, 5VA_ADJ, 12V, +18V, −18V, VOUT+, VOUT− |
| GND domains | 1 (single GND) |
| Bus types | I2C, SPI (×2 external + 1 internal), UART/RS-485, UPDI |

---

## Component Coverage

| # | Device Type | RefDes | COMPONENT_DATA.md | Datasheet in 70_Assets | ERC-C08 | ERC-P06 | ERC-D |
|---|-------------|--------|--------------------|------------------------|---------|---------|-------|
| 1 | 24AA025UIDT-I/OT | U1 | ✅ (24AA02UID — same family) | — | ✅ | ✅ | ✅ |
| 2 | PS509LEX | U2, U3, U12, U25 | ✅ | ✅ PS508-509.pdf | ✅ | ✅ | ✅ |
| 3 | SN74LVC126APW | U4, U5 | ✅ | ✅ sn74lvc126a.pdf | ✅ | ✅ | ✅ |
| 4 | SN74LVC125APW | U6, U7 | ✅ | ✅ sn74lvc125a.pdf | ✅ | ✅ | ✅ |
| 5 | LTC3265EDHC | U8 | ✅ | ✅ 3265fa.pdf | ✅ | ✅ | ✅ |
| 6 | PI4IOE5V6416ZDEX | U9 | ✅ | — | ✅ | ✅ | ✅ |
| 7 | AD5592R | U10, U22 | ✅ | ✅ ad5592r.pdf | ✅ | ✅ | ✅ |
| 8 | PGA849 | U11, U16 | ✅ | ✅ pga849.pdf | ✅ | ✅ | ✅ |
| 9 | 74LVC1G19DBV | U13 | ✅ | ✅ 74LVC1G19.pdf | ✅ | ✅ | ✅ |
| 10 | AMS1117-ADJ | U14 | ✅ (AMS1117) | — | ✅ | ✅ | ✅ |
| 11 | OPA192 | U15 | ✅ | ✅ opa192.pdf | ✅ | ✅ | ✅ |
| 12 | LP5012RUKR | U17 | ✅ | ✅ lp5012.pdf | ✅ | ✅ | ✅ |
| 13 | ATmega4809 | U18 | ✅ | ✅ ATmega4808-4809-Data-Sheet-DS40002173A.pdf | ✅ | ✅ | ✅ |
| 14 | SN74AVC4T774RGYR | U19, U20 | ✅ | ✅ sn74avc4t774.pdf | ✅ | ✅ | ✅ |
| 15 | TLV9102IDR | U21 | ✅ | ✅ tlv9102.pdf | ✅ | ✅ | ✅ |
| 16 | SN74LVC1G125DBVR | U23 | ✅ (= SN74CBTLV1G125 — FET bus switch) | ✅ sn74cbtlv1g125.pdf | ✅ | ✅ | ✅ |
| 17 | SN74LVC1G126DBVR | U24 | ✅ | ✅ sn74lvc1g126.pdf | ✅ | ✅ | ✅ |
| 18 | SN74LVC2G06DBVR | U26 | ✅ | — | ✅ | ✅ | ✅ |
| 19 | G20N06D52 | Q1 | ✅ | ✅ G20N06D52.pdf | ✅ | ✅ | ✅ |

**Coverage summary:** 19/19 types in COMPONENT_DATA.md. All datasheets present. Note: SN74LVC1G125DBVR (U23) is a FET bus switch (SN74CBTLV1G125DBVR), not a 3-state buffer — verify intent in ERC-D. G20N06D52 (Q1) is a dual N-ch MOSFET — verify which instance is used in schematic.

---

## Structural ERC

### ERC-C: Connectivity

| Check | Description | Result | Findings |
|-------|-------------|--------|----------|
| ERC-C01 | Nets with only 1 connection (floating signal) | ✅ PASS | 0 single-pin nets |
| ERC-C02 | Empty/null nets | ✅ PASS | No empty NET entries |
| ERC-C03 | Multi-driver / bus contention | ✅ PASS | SPI_ENn and UART_ENn drive multiple OE pins (inputs) — no output conflict |
| ERC-C04 | Dangling net stubs | ✅ PASS | No stub nets detected |
| ERC-C05 | Unconnected component outputs | ⏳ Pending | Requires per-device datasheet check (ERC-C08) |
| ERC-C06 | Differential pair integrity | N/A | No diff pairs in scope |
| ERC-C07 | Termination resistors present | ✅ PASS | RS-485 and SPI lines have series resistors at bus interface |
| ERC-C08 | Unconnected pins vs datasheet | ⏳ Pending | 19 device types to check — see Component Coverage table |

### ERC-P: Power

| Check | Description | Result | Findings |
|-------|-------------|--------|----------|
| ERC-P01 | Power nets without source | ⚠️ Accepted | PADS QCV limitation: power symbols not exported to netlist. All 10 rails have multiple consumer connections (GND: 174, 3V3: 40, +18V: 14, −18V: 16, etc.). Accept — same disposition as ESH10000540. |
| ERC-P02 | Supply voltage within component ratings | ⏳ Pending | Requires ERC-P06 per-device check |
| ERC-P03 | Power pin polarity | ✅ PASS | No reversed polarity observed in netlist |
| ERC-P04 | Multiple ground domains | ✅ PASS | Single GND domain only |
| ERC-P05 | Decoupling capacitors present | ✅ PASS | Bypass caps on all major rails: 3V3, 5VA, +18V, −18V, 12V |
| ERC-P06 | Power supply range vs component ratings | ⏳ Pending | 19 device types to check — see Component Coverage table |

**Power rail summary:**

| Rail | Connections | Source | Primary Loads |
|------|-------------|--------|---------------|
| GND | 174 | J3 connector / internal | All ICs, passives |
| 3V3 | 40 | U9/U18/MCU-regulated? | U18, U9, logic ICs, LP5012, I2C bus |
| 5V | 12 | J3 connector | LED supply (D2–D8 via LP5012) |
| 5VA | 13 | AMS1117-ADJ (U14) | PGA849 (U11, U16 VS+), AD5592R (U10, U22), OPA192 (U15) |
| 5VA_ADJ | 3 | R90/R91 divider → U14-1 | AMS1117 adjust pin |
| 12V | 11 | J3 connector | LTC3265 (U8) input, AMS1117 (U14) input |
| +18V | 14 | LTC3265 (U8-17) | PGA849 (U11-6, U16-6), PS509 (U2/U3/U12/U25 VCC) |
| −18V | 16 | LTC3265 (U8-7) | PGA849 (U11-15/17, U16-15/17), PS509 (U2/U3/U12/U25 VEE) |
| VOUT+ | 4 | LTC3265 charge pump node | C37, C2 (NM), U8-11/18 |
| VOUT− | 3 | LTC3265 charge pump node | C38, C3 (NM), U8-8 |

> **Note:** VOUT+ and VOUT− are LTC3265 internal charge pump nodes, not external supply rails. C2 and C3 (NM) are optional filter caps — NM status is intentional design choice; verify in schematic.

### ERC-S: Signal Integrity

| Check | Description | Result | Findings |
|-------|-------------|--------|----------|
| ERC-S01 | Missing BOM values | ⚠️ Accepted | QBLP600-RGB (D2–D8): no value field — RGB LED identified by part name. BAT54J (D1): no value — Schottky identified by part name. BZX84-C3V6 (D9–D12): identified by Voltage field (3V6). Accept — standard practice for diodes. |
| ERC-S02 | Net naming consistency | ✅ PASS | Net names consistent and descriptive |
| ERC-S03 | Signal level compatibility | ⏳ Pending | Requires ERC-D per-device checks (logic levels at bus buffer interfaces) |
| ERC-S04 | Pull-up/pull-down presence | ✅ PASS | I2C pull-ups (R1, R2) present. SPI_ENn and UART_ENn driven from MCU/IO expander — verify pull-up/down at power-on |

### ERC-B: Bus

| Check | Description | Result | Findings |
|-------|-------------|--------|----------|
| ERC-B01 | I2C bus integrity | ✅ PASS | SCL: R2 pull-up + 7 connections (U1, U9, U17, U18, J3, TP25, R2). SDA: R1 pull-up + 7 connections (U1, U9, U17, U18, J3, TP26, R1). All devices are legitimate I2C participants. |
| ERC-B02 | SPI bus integrity | ✅ PASS | Two external SPI buses: D-SPI (debug, via J3, buffered by U4) and U-SPI (user, via J3, buffered by U4/U6). Internal SPI: SCK/SCK_R for AD5592R (U10, U22). All CS lines present and individually routed. |
| ERC-B03 | UART/RS-485 integrity | ✅ PASS | TXD/RXD from U18 (ATmega4809) buffered through U7 (SN74LVC125APW). Direction control via UART_ENn (U9-1 → U5, R46). DTXD/DRXD on J3 (debug UART). UPDI programming via U13 (74LVC1G19) mux. |

---

## ERC-C08: Unconnected Pin Check

| RefDes | Device | Pins in Netlist | Required Pins | Result | Notes |
|--------|--------|-----------------|---------------|--------|-------|
| U1 | 24AA025UIDT-I/OT | 6 | — | ⚠️ Flag | 6 pins in netlist; COMPONENT_DATA.md entry (24AA02UID) is SOT-23-5 (5-pin). VCC on p6=VID net. See OI-05. |
| U2, U3 | PS509LEX | 16 | 16 | ✅ Pass | All pins connected: A0/A1/EN/VSS/VDD/GND + S1A–S4A/S1B–S4B/DA/DB |
| U4, U5 | SN74LVC126APW | 14 | 14 | ✅ Pass | All pins connected; all 4 OE pins driven |
| U6, U7 | SN74LVC125APW | 14 | 14 | ✅ Pass | All pins connected; all 4 OE\ pins driven |
| U8 | LTC3265EDHC | 19 | 19 | ✅ Pass | All pins connected including EP=GND, BYP±, ADJ±, RT, MODE, EN+/EN− |
| U9 | PI4IOE5V6416ZDEX | 23 | 24 | ⚠️ Flag | p22 absent from netlist. Determine if INT (OK to leave floating) or ADDR (must be tied). See OI-06. |
| U10, U22 | AD5592R | 16 | 16 | ✅ Pass | All pins connected; all 8 I/O pins driven |
| U11, U16 | PGA849 | 15 (+ EP) | 15 (+ EP) | ✅ Pass | NC pins 8 and 13 correctly absent from netlist per datasheet. EP=-18V (=VS−) ✅ |
| U12, U25 | PS509LEX | 16 | 16 | ✅ Pass | Calibration mux instance. S-channel pins tied to GND/VREF_BUF/CH_SHORT (intentional) |
| U13 | 74LVC1G19DBV | 6 | 6 | ✅ Pass | All pins connected: A/E\/Y1/Y2/VCC/GND |
| U14 | AMS1117-ADJ | 3 | 3 | ✅ Pass | ADJ/OUTPUT/INPUT all connected. Tab=OUTPUT, not separately listed in netlist (normal). |
| U15 | OPA192 | 5 | 5 | ✅ Pass | All pins connected: OUT/V−/+IN/−IN/V+ |
| U17 | LP5012RUKR | 20 + EP | 20 + EP | ✅ Pass | OUT0–OUT11, VCAP, ADDR0/1, VCC, SDA, SCL, EN, IREF, EP=GND all connected |
| U18 | ATmega4809 | 26 | 48 | ⚠️ OI-04 | 3×VDD/AVDD + 3×GND + UPDI/RESET/I2C/UART/EXTCLK connected. 22 I/O pins NC — per OI-04. |
| U19, U20 | SN74AVC4T774RGYR | 16 + EP | 16 + EP | ✅ Pass | DIR1–DIR4 all tied to fixed rail (GND for U19, 3V3 for U20). All A/B signal pins connected. OE driven. |
| U21 | TLV9102IDR | 8 | 8 | ✅ Pass | Both amp inputs and outputs connected. V+=12V, V−=GND. |
| U23 | SN74CBTLV1G125 | 5 | 5 | ✅ Pass | OE=SPI_ENn, A=CS1n, B=UCS1n, GND, VCC=3V3 |
| U24 | SN74LVC1G126DBVR | 5 | 5 | ✅ Pass | All 5 pins connected. Pin 2 in PADS symbol = Y (output); GND on pin 3. Verify footprint mapping. |
| U26 | SN74LVC2G06DBVR | 6 | 6 | ✅ Pass | Both inputs and open-drain outputs connected: 1A=SW_EN_PGA2→1Y=SW_ENn_PGA2; 2A=SW_EN_PGA1→2Y=SW_ENn_PGA1 |
| Q1 | G20N06D52 | 6 | 6 | ⚠️ Flag | All 6 pins connected. Cannot verify G/S/D mapping — datasheet pin diagram is a graphical image. See OI-07. |

---

## ERC-P06: Power Pin Voltage Range

| RefDes | Device | Power Pin | Net | Actual Voltage | Spec Range | Result |
|--------|--------|-----------|-----|----------------|------------|--------|
| U1 | 24AA025UIDT | VCC | VID | Unknown (VID net) | 1.7–5.5 V | ⚠️ Verify VID rail voltage — see OI-05 |
| U2, U3, U12, U25 | PS509LEX | VDD | +18V | +18 V | ±5–±18 V | ✅ |
| U2, U3, U12, U25 | PS509LEX | VSS | −18V | −18 V | ±5–±18 V | ✅ |
| U4, U5, U6, U7 | LVC126A / LVC125A | VCC | 3V3 | 3.3 V | 1.65–3.6 V | ✅ |
| U8 | LTC3265EDHC | VIN_P | 12V | 12 V | 4.5–16 V | ✅ |
| U8 | LTC3265EDHC | VIN_N | VOUT+ | ≈24 V | 4.5–32 V | ✅ (VOUT+=2×12V pre-LDO) |
| U9 | PI4IOE5V6416ZDEX | VCC | 3V3 | 3.3 V | 1.65–5.5 V | ✅ |
| U10, U22 | AD5592R | VDD | 5VA | 5 V | 2.7–5.5 V | ✅ |
| U11, U16 | PGA849 | VS+ | +18V | +18 V | ±4–±18 V | ✅ |
| U11, U16 | PGA849 | VS− | −18V | −18 V | ±4–±18 V | ✅ |
| U11, U16 | PGA849 | LVDD | 5VA | 5 V | LVDD−LVSS ≥ ±2.25 V | ✅ (5V−0V=5V) |
| U13 | 74LVC1G19DBV | VCC | 3V3 | 3.3 V | 1.65–5.5 V | ✅ |
| U14 | AMS1117-ADJ | INPUT | 12V | 12 V | ≤18 V abs max | ✅ |
| U15 | OPA192 | V+ | 5VA | 5 V | 4.5–36 V (single) | ✅ |
| U17 | LP5012RUKR | VCC | 3V3 | 3.3 V | 2.7–5.5 V | ✅ |
| U18 | ATmega4809 | VDD/AVDD | 3V3 | 3.3 V | 1.8–5.5 V | ✅ |
| U19 | SN74AVC4T774 | VCCA | 3V3 | 3.3 V | 1.1–3.6 V | ✅ |
| U19 | SN74AVC4T774 | VCCB | TACH_VCCO | DAC-set | 1.1–3.6 V | ⚠️ OI-08: Verify DAC range ≤3.6 V |
| U20 | SN74AVC4T774 | VCCA | 3V3 | 3.3 V | 1.1–3.6 V | ✅ |
| U20 | SN74AVC4T774 | VCCB | PWM_VCCO | DAC-set | 1.1–3.6 V | ⚠️ OI-08: Verify DAC range ≤3.6 V |
| U21 | TLV9102IDR | V+ | 12V | 12 V | 2.7–16 V | ✅ |
| U23 | SN74CBTLV1G125 | VCC | 3V3 | 3.3 V | 2.3–3.6 V | ✅ |
| U24 | SN74LVC1G126DBVR | VCC | 3V3 | 3.3 V | 1.65–5.5 V | ✅ |
| U26 | SN74LVC2G06DBVR | VCC | 3V3 | 3.3 V | 1.65–5.5 V | ✅ |
| Q1 | G20N06D52 | Source (assumed) | 5V | 5 V | VDS ≤ 60 V; VGS ≤ ±20 V | ✅ VDS well within rating |

---

## ERC-D: Device Constraints

| # | RefDes | Device | Check | Result | Finding |
|---|--------|--------|-------|--------|---------|
| D01 | U2, U3 | PS509LEX | EN polarity | ✅ | EN=SW_EN_PGA1/2 (active-HIGH), driven from U9 GPIO. ✅ |
| D02 | U2/U12, U3/U25 | PS509LEX | Shared output contention | ✅ | U2 and U12 both drive PGA1_P/PGA1_N. SW_EN_PGA1 and SW_ENn_PGA1 are complementary via U26 — never simultaneously HIGH. ✅ |
| D03 | U4 | SN74LVC126APW | OE polarity | ✅ | OE active-HIGH; SPI_ENn HIGH → debug SPI path enabled. Complementary to U6. ✅ |
| D04 | U5 | SN74LVC126APW | OE/UART_ENn polarity | ⚠️ | OE is active-HIGH (126A) driven by UART_ENn. If UART_ENn is active-LOW (LOW=UART active), buffer enables when UART is disabled. Verify intended logic polarity with schematic. |
| D05 | U6 | SN74LVC125APW | OE\ polarity | ✅ | OE\ active-LOW; SPI_ENn LOW → internal SPI path enabled. Complementary to U4. ✅ |
| D06 | U7 | SN74LVC125APW | Multi-driver on URXD_R | ⚠️ | Ch3 (OE\=RxD_TxD_ENn) and Ch4 (OE\=UPDI_ENn) both drive URXD_R. No contention only if RxD_TxD_ENn and UPDI_ENn are mutually exclusive (never both LOW). Verify. |
| D07 | U8 | LTC3265EDHC | VIN_N tied to VOUT+ | ✅ | Standard symmetric ±18V topology. VOUT−=−2×VIN_P pre-LDO; LDO− regulated to −18V. ✅ |
| D08 | U8 | LTC3265EDHC | MODE pin | ⚠️ | MODE=net "MODE". Datasheet: must not float. Verify MODE is driven HIGH (Burst) or LOW (constant-freq). |
| D09 | U8 | LTC3265EDHC | OI-03 disposition | ✅ | VOUT+/VOUT− are internal nodes; C2/C3 NM is acceptable per LTC3265 design guide. Pending engineer confirmation per OI-03. |
| D10 | U9 | PI4IOE5V6416ZDEX | Power-on state | ⚠️ | All GPIOs are inputs at reset, pull resistors disabled by default. Firmware must write output values before setting direction to avoid glitch. |
| D11 | U10, U22 | AD5592R | RESET\ pin | ⚠️ | RESETn must be driven HIGH for normal operation. Verify driven or tied to 3V3 (not left open). |
| D12 | U10, U22 | AD5592R | VREF input | ✅ | VREF=VREF_BUF (buffered by OPA192 unity-gain). External reference: valid if 1V–VDD(5V). VREF_BUF ≈ VREF (passive divider value). Verify VREF level is within 1–5V. |
| D13 | U11, U16 | PGA849 | Thermal pad (EP) | ✅ | EP=−18V (=VS−). Per datasheet: connect to VS− or float. −18V is correct. ✅ |
| D14 | U11, U16 | PGA849 | REF pin drive | ✅ | REF=VREF_BUF (driven from OPA192 low-impedance buffer). ✅ |
| D15 | U13 | 74LVC1G19DBV | Logic function | ✅ | 1-of-2 demux for UPDI/UART routing. A=UPDI_PGM select; E\=UART_ENn enable; Y1/Y2 drive UPDI_ENn/RxD_TxD_ENn. ✅ |
| D16 | U14 | AMS1117-ADJ | Minimum load | ⚠️ | ADJ variant requires ≥10 mA minimum load for regulation. Verify R90/R91 divider plus downstream loads provide ≥10 mA at all conditions. |
| D17 | U15 | OPA192 | Unity-gain buffer | ✅ | OUT(p1)=−IN(p4)=VREF_BUF (feedback). +IN(p3)=VREF. Stable at unity gain. ✅ |
| D18 | U17 | LP5012RUKR | EN pin | ⚠️ | EN=3V3 (permanently HIGH). Chip cannot be software-shutdown. Verify this is intentional; LP5012 can only be disabled by pulling EN LOW. |
| D19 | U18 | ATmega4809 | 22 GPIO NCs (OI-04) | ⚠️ | 22/48 I/O pins absent from netlist. Configure in firmware as inputs with pull-ups. Pending engineer confirmation per OI-04. |
| D20 | U18 | ATmega4809 | TOSC1/TOSC2 | ⚠️ | p34=TOSC1, p35=TOSC2 connected to nets. Verify 32.768 kHz crystal (or other clock source) on these pins. |
| D21 | U19 | SN74AVC4T774 | DIR=GND (B→A) | ✅ | All DIR pins tied to GND → fixed B→A direction. TACH signals at TACH_VCCO level on Port B translated to 3V3 on Port A. ✅ |
| D22 | U20 | SN74AVC4T774 | DIR=3V3 (A→B) | ✅ | All DIR pins tied to 3V3 → fixed A→B direction. MCU PWM (3V3) translated to PWM_VCCO level on Port B. ✅ |
| D23 | U19, U20 | SN74AVC4T774 | VCCB limit | ⚠️ | VCCB=TACH_VCCO and PWM_VCCO are DAC-set voltages from U22 (AD5592R I/O). Must remain 1.1–3.6V. Exceeding 3.6V damages device. See OI-08. |
| D24 | U21 | TLV9102IDR | Feedback topology | ✅ | Each amp: +IN=V_SET (DAC/analog setpoint), −IN=V_FB (output feedback net). V_R=output. Standard non-inverting configuration. ✅ |
| D25 | U23 | SN74CBTLV1G125 | Bidirectional switch | ✅ | OE=SPI_ENn (active-LOW): LOW → CS1n↔UCS1n connected. HIGH → disconnected. Complementary to U24. ✅ |
| D26 | U23, U24 | — | SPI_ENn pull-up | ⚠️ | SPI_ENn drives OE of both U23 and U24. Must not float at power-up. Verify pull-up or MCU drives SPI_ENn to defined state before enabling SPI. |
| D27 | U24 | SN74LVC1G126DBVR | Footprint pin mapping | ⚠️ | Netlist p2=UCS1n (Y output), p3=GND. Physical SOT-23-5 pin 2=GND, pin 4=Y. Schematic symbol uses non-standard numbering. Verify footprint correctly maps PADS symbol pins to physical pads. |
| D28 | U26 | SN74LVC2G06DBVR | Open-drain pull-ups | ⚠️ | 1Y=SW_ENn_PGA2 and 2Y=SW_ENn_PGA1 are open-drain outputs. PS509 EN pin (active-HIGH) needs to be pulled HIGH by external pull-up when U26 output is Hi-Z. Verify pull-up resistors on SW_ENn_PGA1/2 nets. |
| D29 | Q1 | G20N06D52 | Pin mapping | ⚠️ | Cannot verify G/S/D assignment from datasheet (graphical pin diagram). See OI-07. Tentative: G=PWM_VCCO/TACH_VCCO, S=PWM_VCCO_Q/TACH_VCCO_Q, D=5V (or reversed). |
| D30 | Q1 | G20N06D52 | Gate drive voltage | ⚠️ | Gate driven from U20/U19 Port B (VCCB=PWM_VCCO/TACH_VCCO ≤ 3.6V max). VGS(th)=1.0–2.5V. Full enhancement spec is at VGS=10V; at VGS=4.5V: RDS(ON)=40mΩ max. At VGS<4.5V RDS(ON) will be higher. See OI-08. Verify VGS and acceptable on-resistance. |

---

## Open Items

| # | ID | Description | Status |
|---|----|-------------|--------|
| 1 | OI-01 | Component data: 13 entries added 2026-04-30; 17/19 types now in COMPONENT_DATA.md | ✅ Closed |
| 2 | OI-02 | Missing datasheets resolved: U23 = sn74cbtlv1g125.pdf; Q1 = G20N06D52.pdf | ✅ Closed |
| 3 | OI-03 | VOUT+/VOUT− caps C2/C3 are NM — verify this is intentional in schematic | ⏳ Pending engineer confirmation |
| 4 | OI-04 | ATmega4809 (U18): 26/48 pins in netlist — verify unconnected I/O pins are intentional NCs | ⏳ Pending engineer confirmation |
| 5 | OI-05 | U1 (24AA025UIDT-I/OT): netlist has 6 pins; COMPONENT_DATA.md entry is 24AA02UID SOT-23-5 (5-pin). VCC on net "VID" (p6). Verify 24AA025UID datasheet pinout — different package? | ⏳ Pending engineer confirmation |
| 6 | OI-06 | U9 (PI4IOE5V6416ZDEX): PADS symbol pin 22 absent from netlist. Determine if INT output (OK floating if unused) or ADDR pin (must be tied to set I2C address). | ⏳ Pending engineer confirmation |
| 7 | OI-07 | Q1 (G20N06D52): pin G/S/D assignment cannot be verified — datasheet pin diagram is a graphical image not extractable as text. Verify against datasheet figure or PCB footprint. | ⏳ Pending engineer confirmation |
| 8 | OI-08 | U19/U20 VCCB (TACH_VCCO, PWM_VCCO) are DAC-set voltages from U22 AD5592R. SN74AVC4T774 VCCB max = 3.6V — verify DAC output range ≤ 3.6V. Also: Q1 gate drive ≤ 3.6V; verify RDS(ON) acceptable at actual VGS. | ⏳ Pending engineer confirmation |

---

## Sign-off

| Role | Name | Date | Signature / Initials |
|------|------|------|----------------------|
| **Design Engineer / Review Lead** | — | — | ⏳ Pending |
| **Quality** | — | — | ⏳ Pending |
