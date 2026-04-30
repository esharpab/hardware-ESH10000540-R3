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
| Component data coverage | ⏳ 17/19 types in COMPONENT_DATA.md — ERC-C08/P06/D pending for 17 types; 2 missing datasheet (SN74LVC1G125DBVR, G20N06D52) |
| Findings dispositioned | ⏳ In progress |
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
| 1 | 24AA025UIDT-I/OT | U1 | ✅ (24AA02UID — same family) | — | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 2 | PS509LEX | U2, U3, U12, U25 | ✅ | ✅ PS508-509.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 3 | SN74LVC126APW | U4, U5 | ✅ | ✅ sn74lvc126a.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 4 | SN74LVC125APW | U6, U7 | ✅ | ✅ sn74lvc125a.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 5 | LTC3265EDHC | U8 | ✅ | ✅ 3265fa.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 6 | PI4IOE5V6416ZDEX | U9 | ✅ | — | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 7 | AD5592R | U10, U22 | ✅ | ✅ ad5592r.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 8 | PGA849 | U11, U16 | ✅ | ✅ pga849.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 9 | 74LVC1G19DBV | U13 | ✅ | ✅ 74LVC1G19.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 10 | AMS1117-ADJ | U14 | ✅ (AMS1117) | — | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 11 | OPA192 | U15 | ✅ | ✅ opa192.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 12 | LP5012RUKR | U17 | ✅ | ✅ lp5012.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 13 | ATmega4809 | U18 | ✅ | ✅ ATmega4808-4809-Data-Sheet-DS40002173A.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 14 | SN74AVC4T774RGYR | U19, U20 | ✅ | ✅ sn74avc4t774.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 15 | TLV9102IDR | U21 | ✅ | ✅ tlv9102.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 16 | SN74LVC1G125DBVR | U23 | ❌ | ❌ Missing | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 17 | SN74LVC1G126DBVR | U24 | ✅ | ✅ sn74lvc1g126.pdf | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 18 | SN74LVC2G06DBVR | U26 | ✅ | — | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| 19 | G20N06D52 | Q1 | ❌ | ❌ Missing | ⏳ Pending | ⏳ Pending | ⏳ Pending |

**Coverage summary:** 17/19 types in COMPONENT_DATA.md. 2 types still missing: SN74LVC1G125DBVR (U23, no datasheet) and G20N06D52 (Q1, no datasheet).

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

*(To be completed per device type as datasheet data is added to COMPONENT_DATA.md.)*

---

## ERC-P06: Power Pin Voltage Range

*(To be completed per device type as datasheet data is added to COMPONENT_DATA.md.)*

---

## ERC-D: Device Constraints

*(To be completed per device type as datasheet data is added to COMPONENT_DATA.md.)*

---

## Open Items

| # | ID | Description | Status |
|---|----|-------------|--------|
| 1 | OI-01 | Component data: 13 entries added 2026-04-30; 17/19 types now in COMPONENT_DATA.md | ✅ Closed |
| 2 | OI-02 | Missing datasheets: SN74LVC1G125DBVR (U23), G20N06D52 (Q1) — not in 70_Assets | ⏳ Open |
| 3 | OI-03 | VOUT+/VOUT− caps C2/C3 are NM — verify this is intentional in schematic | ⏳ Pending engineer confirmation |
| 4 | OI-04 | ATmega4809 (U18): 26/48 pins in netlist — verify unconnected I/O pins are intentional NCs | ⏳ Pending engineer confirmation |

---

## Sign-off

| Role | Name | Date | Signature / Initials |
|------|------|------|----------------------|
| **Design Engineer / Review Lead** | — | — | ⏳ Pending |
| **Quality** | — | — | ⏳ Pending |
