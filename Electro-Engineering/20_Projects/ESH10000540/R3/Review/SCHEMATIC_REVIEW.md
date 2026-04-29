---
project: ESH10000540
revision: R3
date: 2026-04-29
phase: Review
---

# Schematic Review — Sparrow Fixture Electronics PCBA R3

## File Information

| Field | Value |
|-------|-------|
| **File** | NetList_Sparrow_FE_R3.qcv + PartsList_Sparrow_FE_R3.csv |
| **Format** | PADS QCV netlist + BOM CSV |
| **Date** | 2026-04-29 |
| **Components** | 445 |
| **Nets** | 335 |
| **Review Type** | Electrical Rule Check (ERC) — structural and connectivity |

---

## ERC Findings Summary

| Category | Count | Status |
|----------|-------|--------|
| **Errors** | 24 | Requires disposition |
| **Warnings** | 19 | Requires disposition |
| **Info** | 0 | — |
| **Total** | 43 | — |

---

## Detailed Findings

### ❌ Errors (24)

| # | Check ID | Detail | Disposition |
|---|----------|--------|-------------|
| 1 | ERC-P01 | Power net `3V3_EXT_PG` has 3 consumer pins but no identified power source | — |
| 2 | ERC-P01 | Power net `6V5` has 8 consumer pins but no identified power source | — |
| 3 | ERC-P01 | Power net `12V_EXT` has 5 consumer pins but no identified power source | — |
| 4 | ERC-P01 | Power net `3V3_LIM` has 4 consumer pins but no identified power source | — |
| 5 | ERC-P01 | Power net `5V` has 30 consumer pins but no identified power source | — |
| 6 | ERC-P01 | Power net `12V_EXT_EN` has 3 consumer pins but no identified power source | — |
| 7 | ERC-P01 | Power net `3V3_EXT_EN` has 3 consumer pins but no identified power source | — |
| 8 | ERC-P01 | Power net `12V_EXT_DIV` has 3 consumer pins but no identified power source | — |
| 9 | ERC-P01 | Power net `3V3_LIM_PG` has 3 consumer pins but no identified power source | — |
| 10 | ERC-P01 | Power net `1V8_EXT` has 5 consumer pins but no identified power source | — |
| 11 | ERC-P01 | Power net `5V_LIM_EN` has 3 consumer pins but no identified power source | — |
| 12 | ERC-P01 | Power net `5V_LIM_PG` has 3 consumer pins but no identified power source | — |
| 13 | ERC-P01 | Power net `VDD` has 28 consumer pins but no identified power source | — |
| 14 | ERC-P01 | Power net `12V_EXT_PG` has 3 consumer pins but no identified power source | — |
| 15 | ERC-P01 | Power net `3V3_EXT_DIV` has 3 consumer pins but no identified power source | — |
| 16 | ERC-P01 | Power net `6V5_LIM_EN` has 3 consumer pins but no identified power source | — |
| 17 | ERC-P01 | Power net `6V5_LIM_PG` has 3 consumer pins but no identified power source | — |
| 18 | ERC-P01 | Power net `AGND` has 27 consumer pins but no identified power source | — |
| 19 | ERC-P01 | Power net `3V3_LIM_EN` has 3 consumer pins but no identified power source | — |
| 20 | ERC-P01 | Power net `5V_LIM` has 4 consumer pins but no identified power source | — |
| 21 | ERC-P01 | Power net `6V5_LIM` has 4 consumer pins but no identified power source | — |
| 22 | ERC-P01 | Power net `3V3` has 84 consumer pins but no identified power source | — |
| 23 | ERC-P01 | Power net `12V` has 9 consumer pins but no identified power source | — |
| 24 | ERC-P01 | Power net `3V3_EXT` has 6 consumer pins but no identified power source | — |

### ⚠️ Warnings (19)

| # | Check ID | Detail | Disposition |
|---|----------|--------|-------------|
| 25 | ERC-P04 | Design has **18 ground domains** (AGND, GND, GND_SW0, GND_SW0_DIV, GND_SW0_OUT, GND_SW0_OUT_R, GND_SW1, GND_SW1_DIV, GND_SW1_OUT, GND_SW1_OUT_R, GND_SW2, GND_SW2_DIV, GND_SW2_OUT, GND_SW2_OUT_R, GND_SW3, GND_SW3_DIV, GND_SW3_OUT, GND_SW3_OUT_R) | — |
| 26 | ERC-S01 | Component `D1` (W2S118TS-A41) has no value in BOM | — |
| 27 | ERC-S01 | Component `D2` (KGSOT05C) has no value in BOM | — |
| 28 | ERC-S01 | Component `D3` (KGSOT05C) has no value in BOM | — |
| 29 | ERC-S01 | Component `D4` (KGSOT05C) has no value in BOM | — |
| 30 | ERC-S01 | Component `D5` (KGSOT05C) has no value in BOM | — |
| 31 | ERC-S01 | Component `D6` (KGSOT05C) has no value in BOM | — |
| 32 | ERC-S01 | Component `D7` (KGSOT05C) has no value in BOM | — |
| 33 | ERC-S01 | Component `D8` (KGSOT05C) has no value in BOM | — |
| 34 | ERC-S01 | Component `D9` (KGSOT05C) has no value in BOM | — |
| 35 | ERC-S01 | Component `D16` (KGSOT05C) has no value in BOM | — |
| 36 | ERC-S01 | Component `D17` (KGSOT05C) has no value in BOM | — |
| 37 | ERC-S01 | Component `D10` (ESD652) has no value in BOM | — |
| 38 | ERC-S01 | Component `D11` (ESD652) has no value in BOM | — |
| 39 | ERC-S01 | Component `D12` (ESD562) has no value in BOM | — |
| 40 | ERC-S01 | Component `D13` (ESD562) has no value in BOM | — |
| 41 | ERC-S01 | Component `D14` (BZX84-C3V6) has no value in BOM | — |
| 42 | ERC-S01 | Component `D15` (BZX84-C3V6) has no value in BOM | — |
| 43 | ERC-S01 | Component `D18` (ESD652) has no value in BOM | — |

---

## Analysis & Notes

### ERC-P01 (Power nets without source)

**Observation:** The netlist parser detected 24 power nets with consumer pins but no identified power source component. This is a **known limitation** of the ERC-P01 check when dealing with netlists exported from PADS:

- **Root cause:** Power symbols (e.g., `+3V3`, `+12V`) in PADS do not have reference designators, so they do not appear in the netlist as components with pins. The parser cannot identify them as "sources."
- **Validity:** The design likely **does have power sources** connected to these nets in the schematic. This is a **false positive** in the automated check — the absence of a regulator IC does not mean the net is undriven; it may be:
  - Connected to a power symbol (invisible to the netlist)
  - Connected to a connector pin or external supply
  - Connected via a power plane

**Recommendation:** 
- [ ] **Accept as known issue** — Power connectivity should be verified visually in the schematic or layout, not via netlist ERC alone.
- [ ] Or: **Re-export netlist** with full component data to include power symbols.

### ERC-P04 (Multiple ground domains)

**Observation:** Design uses **18 distinct ground net names**, including `GND`, `AGND` (analog), `GND_SW0/1/2/3` (switched grounds), and variants.

**Validity:** This is **intentional**. The presence of multiple ground domains suggests:
- Analog/digital ground separation (AGND vs. GND)
- Switched/isolated grounds for load switching (GND_SW0, GND_SW1, etc.)
- Planned layout partitioning

**Recommendation:**
- [ ] **Accept** — Multiple ground domains are intentional per design. Confirm layout routing enforces proper star-point connections and return paths.

### ERC-S01 (Component values missing)

**Observation:** 18 diode components (D1–D18) have part names but **no value field** in the BOM CSV. Examples:
- `D1` → Part Name: `W2S118TS-A41` (Schottky diode)
- `D2–D9, D16–D17` → Part Name: `KGSOT05C` (transient suppression diode)
- `D10–D11` → Part Name: `ESD652` (ESD suppressor)
- `D12–D13` → Part Name: `ESD562` (ESD suppressor)
- `D14–D15` → Part Name: `BZX84-C3V6` (Zener, 3.6V)

**Validity:** The **part name is sufficient** to identify the component; the "Value" field typically stores numerical ratings (e.g., "10μ" for capacitors, "1k" for resistors) which are **not applicable to discrete diodes**. The part name contains all necessary info (device type, voltage/current rating).

**Recommendation:**
- [ ] **Accept** — Diode components have part names but no "value" in the BOM. This is normal for discrete semiconductors. No action needed.

---

## Checks Passed (No Issues Found)

✅ **ERC-C01** — No floating nets (single-node nets)  
✅ **ERC-C02** — No unconnected pins without flags  
✅ **ERC-C03** — No contradictory no-connect flags  
✅ **ERC-C04** — No orphan net labels  
✅ **ERC-C05** — No duplicate net names  
✅ **ERC-C06** — No suspicious all-GND connectors  
✅ **ERC-C07** — No pins on `<NO NET>`  
✅ **ERC-P02** — No shorted power rails  
✅ **ERC-P03** — No missing ground connections  
✅ **ERC-P05** — No power pin conflicts  
✅ **ERC-S02** — No duplicate reference designators  
✅ **ERC-S03** — N/A (hierarchical sheets)  
✅ **ERC-S04** — N/A (SPICE subcircuits)  

---

## Recommended Actions

- [ ] **Review power net sources** — Verify in the schematic that all identified power nets (`3V3`, `5V`, `12V`, etc.) have proper supply connections via power symbols or regulators
- [ ] **Confirm ground domain separation** — Review layout to ensure analog/digital/switched grounds are routed correctly with proper star-point connections
- [ ] **Update BOM if needed** — If diode values should be captured for traceability, add them to the "Value" column (e.g., `D1 Value = "Schottky"` or `D14 Value = "3.6V Zener"`) — but this is optional

---

## Disposition Status

**Current:** Pending engineer review and disposition.

| Check | Status | Engineer Notes |
|-------|--------|-----------------|
| ERC-P01 × 24 | Pending | — |
| ERC-P04 × 1 | Pending | — |
| ERC-S01 × 18 | Pending | — |

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| **Review Lead** | — | — | ⏳ Pending |
| **Design Engineer** | — | — | ⏳ Pending |
| **Quality** | — | — | ⏳ Pending |

---

## Workflow Notes

- Review type: Structural & connectivity (ERC)
- Layout-level checks (DFM, signal integrity, clearance) are out of scope for this review
- Power net source detection relies on netlist component data; power symbols are not always exported from PADS
- Findings are based on automated checks; engineer disposition required
