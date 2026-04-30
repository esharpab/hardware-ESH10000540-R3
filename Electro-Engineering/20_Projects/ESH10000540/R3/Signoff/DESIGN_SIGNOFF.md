---
project: ESH10000540
revision: R3
document: Design Sign-off
date: 2026-04-30
status: Signed
---

# Design Sign-off — Sparrow Fixture Electronics PCBA R3

## Scope of This Sign-off

This document records approval of the **Schematic ERC Review** for ESH10000540 R3.

| Item | In Scope | Notes |
|------|----------|-------|
| Schematic ERC — structural and connectivity | ✅ Yes | Netlist-based review against PADS QCV export |
| Bus signal integrity (I2C, UART/RS-485) | ✅ Yes | All bus pin assignments verified against datasheets |
| Power pin validation (ERC-P06) | ✅ Yes | All 17 device types verified |
| Unconnected pin validation (ERC-C08) | ✅ Yes | All 17 device types verified |
| Device constraint checks (ERC-D) | ✅ Yes | All 17 device types verified; all findings closed |
| Layout review (DFM, clearance, routing) | ❌ Not in scope | Separate review required before PCB release |
| Compliance / regulatory review | ❌ Not in scope | Separate process |

---

## Review Summary

**Review file:** [Review/SCHEMATIC_REVIEW.md](../Review/SCHEMATIC_REVIEW.md)  
**Netlist source:** `DOCS/NetList_Sparrow_FE_R3.qcv`  
**BOM source:** `DOCS/PartsList_Sparrow_FE_R3.csv`  
**Schematic source:** `DOCS/Schematic_Sparrow_FE_R3.pdf`  
**Review completed:** 2026-04-30

### Findings Dispositioned

| Category | Count | Disposition |
|----------|-------|-------------|
| ERC-P01 — Power nets without source | 24 | Accepted — known PADS netlist limitation; power symbols not exported |
| ERC-P04 — Multiple ground domains | 1 | Accepted — intentional (AGND, GND, GND_SWx) |
| ERC-S01 — Missing BOM values | 18 | Accepted — diodes identified by part name; value field N/A |
| **Total findings** | **43** | **All dispositioned** |

### Checks Passed

ERC-C01–C07, ERC-P02–P05, ERC-S02–S04, ERC-B01 (I2C), ERC-B02 (SPI N/A), ERC-B03 (UART/RS-485) — all clean.

### Component Data Coverage

17 / 17 unique IC types verified against COMPONENT_DATA.md. All ERC-C08, ERC-P06, ERC-D01/D02/D03 checks complete with no open findings.

### Key Engineer Confirmations (recorded 2026-04-30)

| Item | Confirmation |
|------|-------------|
| U39 (ADS7828) pin 11 mode | COM = AGND via R180 (0Ω); single-ended mode, intentional |
| U4 (PCA9616) VDD(A) = VIO_EXT | VDDA_SEL=1; VIO_EXT within 2.2–5.5 V |
| U29 (24AA02UID) VDD = VIO_EXT | VIO_EXT = 1.8–3.3 V; within 1.7–5.5 V requirement |
| U5, U6 (AD5593R) VLOGIC | Confirmed 3V3 |
| U15–U17 (TPS54302) VIN | Confirmed VDD = 20 V; within 4.5–28 V range |

---

## Open Items at Sign-off

| # | Item | Risk | Owner |
|---|------|------|-------|
| 1 | Layout review not performed | Medium — clearance, DFM, return paths not verified | Design engineer |
| 2 | ERC-P01 — Power net sources not visible in PADS QCV netlist | Low — accepted false positive; verify visually in schematic | Design engineer |

---

## Sign-off

| Role | Name | Date | Signature / Initials |
|------|------|------|----------------------|
| **Design Engineer / Review Lead** | Martin Johansson | 2026-04-30 | MJ |
| **Quality** | — | — | ⏳ Pending |

**Decision:** ✅ **Approved** — Schematic ERC review complete. Design may proceed to layout review and verification planning.

> **Note:** Layout review must be completed and signed off before PCB release to fabrication.

---

## Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2026-04-30 | Martin Johansson | Initial sign-off — schematic ERC review complete |
