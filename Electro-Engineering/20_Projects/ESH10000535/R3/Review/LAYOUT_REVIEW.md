---
project: ESH10000535
revision: R3
date: 2026-05-04
phase: Review
status: In progress
---

# Layout Review — Sparrow N-Top R3

## File Information

| Field | Value |
|-------|-------|
| **Files reviewed** | Gencad_Sparrow_NTop_R3.cad, IPC356_Sparrow_NTop_R3.ipc, AIS_Sparrow_NTop_R3.txt, PartsList_Sparrow_NTop_R3.csv, NetList_Sparrow_NTop_R3.qcv |
| **CAD tool** | Xpedition Layout 2000.5.0.2 |
| **CAD revision date** | 2026-01-23 |
| **Components (BOM)** | 229 mounted, 67 NM (296 total) |
| **Components (layout)** | 304 (TOP: 291, BOTTOM: 13) |
| **Nets (schematic / QCV)** | 233 |
| **Nets (layout / GenCAD)** | 380 (233 named + 147 pour segments) |
| **Board dimensions** | 78 × 53 mm |
| **Layer count** | 8 copper layers |
| **Review type** | Structural / completeness / DFM (text-parseable checks only) |
| **Reviewer** | AI — findings require engineer disposition |

---

## Scope and Limitations

This review covers checks extractable from text-format layout files (GenCAD, IPC-356, AIS, QCV, BOM CSV). It does **not** replace a DRC pass in the EDA tool.

**In scope:** Board outline, layer stackup, routing completeness, power net routing, net count consistency, single-node/orphan pad detection, placement completeness, component side assignment, via drill inventory.

**Out of scope:** Trace width/clearance DRC, thermal relief, power plane pour shape, courtyard/silkscreen overlap, return path analysis, high-speed routing quality — all require EDA tool DRC with copper rendering.

**Note — no Gerber files:** Only an ODB++ panel (`ODBPanel_Sparrow_NTop_R3.tgz`) is present; it is a binary/compressed archive not parseable as text. Gerber-specific checks (file inventory, aperture sizes, paste file consistency) cannot be performed. Run Gerber export and verify against fab spec before release.

---

## Findings Summary

| # | Check | ID | Result | Notes |
|---|-------|----|--------|-------|
| 1 | Layer stackup | LR-L01 | ✅ Pass | 8 copper layers: TOP, INNER1–6, BOTTOM |
| 2 | Board outline | LR-L02 | ✅ Pass | 78 × 53 mm confirmed in GenCAD |
| 3 | Routing completeness | LR-R01 | ✅ Pass | 233/233 named nets routed — 0 unrouted |
| 4 | Power net routing | LR-R02 | ✅ Pass | All 11 power rails present in route data |
| 5 | Net count consistency | LR-N01 | ✅ Pass | QCV 233 = GenCAD named routes 233 |
| 6 | Single-node / orphan pads | LR-N02 | ✅ Pass | 0 orphan pads detected |
| 7 | Placement completeness | LR-P01 | ⚠️ Info | Layout 304 vs BOM 296 — Δ8; 6 accounted (PCB5–8 fiducials + M1–M2 standoffs); 2 unaccounted |
| 8 | Bottom-side components | LR-P02 | ⚠️ Info | 13 bottom-side items including 4 ICs (U2, U3, U12, U25) — confirm bottom assembly planned |
| 9 | Via drill inventory | LR-V01 | ⚠️ Info | 0.25 mm drill / 0.45 mm pad → 0.10 mm annular ring — verify fab spec |
| 10 | Gerber files | LR-G01 | ⚠️ Info | No Gerber files present — ODB++ only; Gerber checks not performed |

**Totals: 6 Pass, 4 Info, 0 Fail**

All Info items require engineer disposition. No failures found.

---

## Detailed Findings

---

### ✅ LR-L01 — Layer Stackup

**Result:** Pass

8-layer copper stackup confirmed from GenCAD `$LAYERS`:

| Layer | Name | Type |
|-------|------|------|
| 1 | TOP | Signal / component side |
| 2 | INNER1 | Signal / plane |
| 3 | INNER2 | Signal / plane |
| 4 | INNER3 | Signal / plane |
| 5 | INNER4 | Signal / plane |
| 6 | INNER5 | Signal / plane |
| 7 | INNER6 | Signal / plane |
| 8 | BOTTOM | Signal / component side |

Surface finishes: soldermask and paste on both TOP and BOTTOM (confirmed from GenCAD `$BOARD` ARTWORK entries).

> **Note:** GenCAD does not encode signal/plane layer assignments in the `$LAYERS` section. Layer function (signal vs plane) requires EDA tool inspection or PCB specification document.

---

### ✅ LR-L02 — Board Outline

**Result:** Pass

Board outline from GenCAD `$BOARD`: rectangle 0,0 to 78,53 mm.

| Dimension | Value |
|-----------|-------|
| Width | 78.0 mm |
| Height | 53.0 mm |

---

### ✅ LR-R01 — Routing Completeness

**Result:** Pass

GenCAD `$SIGNALS` lists 380 entries (233 named nets + 147 pour segment IDs). `$ROUTES` contains 381 route entries (233 named + 148 pour segments; 1 extra is the `(Net0)` copper plane boundary).

**All 233 schematic nets have a corresponding named route entry — 0 unrouted nets.**

---

### ✅ LR-R02 — Power Net Routing Presence

**Result:** Pass

All power rails from the schematic ERC review are present in GenCAD `$ROUTES`:

| Net | Status |
|-----|--------|
| GND | ✅ Routed |
| 3V3 | ✅ Routed |
| 5V | ✅ Routed |
| 5VA | ✅ Routed |
| 12V | ✅ Routed |
| +18V | ✅ Routed |
| -18V | ✅ Routed |
| VOUT+ | ✅ Routed |
| VOUT- | ✅ Routed |
| TACH_VCCO | ✅ Routed |
| PWM_VCCO | ✅ Routed |

---

### ✅ LR-N01 — Net Count Consistency

**Result:** Pass

| Source | Net count |
|--------|-----------|
| QCV netlist (schematic) | 233 |
| GenCAD $SIGNALS named nets | 233 |
| GenCAD $SIGNALS pour segments | 147 |
| GenCAD $SIGNALS total | 380 |
| IPC-356 unique nets | 380 |

Schematic net count matches layout named net count exactly. The 147 pour segment IDs are internal copper fragment identifiers (all part of the GND/power planes), not additional electrical nets.

**No missing or extra schematic nets.**

---

### ✅ LR-N02 — Single-Node / Orphan Pads

**Result:** Pass

IPC-356 analysis: 0 single-record entries for named schematic nets detected.

**No orphan pads or floating test points detected.**

---

### ⚠️ LR-P01 — Placement Completeness

**Result:** Info — 2 unaccounted items in layout vs BOM

| Source | Count |
|--------|-------|
| BOM — mounted components | 229 |
| BOM — NM components | 67 |
| BOM — total | 296 |
| GenCAD / AIS — total placed | 304 |
| Difference | +8 |

6 of the 8 extra items are accounted for: PCB5–PCB8 (4 fiducials) and M1–M2 (2 SMT standoffs) — these are mechanical/PCB-only items typically excluded from the electrical BOM. The remaining 2 items are unaccounted for.

**Action required:** Confirm the 2 unaccounted layout items are mechanical or fiducial items not in the BOM.

| Field | Value |
|-------|-------|
| **Disposition** | ⏳ Open — confirm identity of 2 unaccounted items |
| **Risk** | Low |

---

### ⚠️ LR-P02 — Bottom-Side Components

**Result:** Info — confirm bottom assembly planned

13 components are placed on the BOTTOM side:

| Ref | Type | Category |
|-----|------|----------|
| PCB5, PCB6, PCB7, PCB8 | Fiducial | Mechanical |
| M1, M2 | SMT standoff | Mechanical |
| J1, J2, J3 | Connector | Electrical |
| U2, U3, U12, U25 | PS509LEX (analog mux) | IC — electrical |

**Observation:** 4 PS509LEX analog mux ICs are bottom-mounted. These are likely placed bottom-side for space or routing reasons. Confirm the assembly process accounts for two-sided reflow or selective soldering.

**Action required:** Engineer to confirm bottom-side assembly is intentional and planned in the assembly process.

| Field | Value |
|-------|-------|
| **Disposition** | ⏳ Open — confirm bottom assembly is planned |
| **Risk** | Process risk if not in assembly plan |

---

### ⚠️ LR-V01 — Via Drill Size Inventory

**Result:** Info — verify annular ring against fab spec

From IPC-356:

| Parameter | Value |
|-----------|-------|
| Via drill diameter | 0.25 mm |
| Via pad size | 0.45 × 0.45 mm |
| Annular ring | (0.45 − 0.25) / 2 = **0.10 mm** |

**Action required:** Confirm 0.10 mm annular ring meets the selected fab's minimum via specification (e.g. JLC standard: 0.075 mm min — pass; other fabs may differ).

| Field | Value |
|-------|-------|
| **Disposition** | ⏳ Open — engineer to verify against fab spec |
| **Risk** | Low for standard fab; verify if using advanced process |

---

### ⚠️ LR-G01 — Gerber Files Not Present

**Result:** Info — ODB++ only; Gerber checks not performed

No RS-274X Gerber files are present in the DOCS folder. Only an ODB++ panel export (`ODBPanel_Sparrow_NTop_R3.tgz`) is available, which is a compressed binary archive not parseable as text.

The following Gerber-based checks were **not** performed:
- Gerber file inventory and completeness
- Gerber format consistency
- Minimum copper aperture sizes
- Paste file consistency (paste layers, SMD openings)
- Board outline verification from Gerbers

**Action required:** Before release to fabrication, either:
1. Export Gerber RS-274X files and run a Gerber viewer / fab DFM check, or
2. Submit the ODB++ directly to the fab and confirm they accept ODB++ format.

| Field | Value |
|-------|-------|
| **Disposition** | ⏳ Open — Gerber export and fab DFM check required before release |
| **Risk** | Medium — manufacturing data not verified in text-parseable format |

---

## Checks Not Performed

| Check | Reason |
|-------|--------|
| Minimum copper aperture / trace width | No Gerber files; ODB++ not text-parseable |
| Paste file consistency | No Gerber files |
| Courtyard / silkscreen overlap | No courtyard data in GenCAD |
| Trace width / clearance DRC | Requires EDA tool |
| Thermal relief inspection | Requires EDA tool |
| Power plane pour quality | Requires EDA tool |
| High-speed routing quality | Requires EDA tool |

**Recommendation:** Run a full EDA DRC pass (Xpedition DRC or equivalent) and a Gerber DFM check before releasing to fabrication.

---

## Disposition Summary

| # | ID | Finding | Disposition | By | Date |
|---|----|---------|-------------|----|----|
| 1 | LR-P01 | Layout +8 vs BOM — 2 items unaccounted | ⏳ Open | — | — |
| 2 | LR-P02 | 13 bottom-side items incl. 4 ICs — confirm assembly | ⏳ Open | — | — |
| 3 | LR-V01 | Via annular ring 0.10 mm — verify fab spec | ⏳ Open | — | — |
| 4 | LR-G01 | No Gerber files — ODB++ only | ⏳ Open | — | — |

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Layout Reviewer | — | — | — |
| Design Engineer | — | — | — |

*This review was performed by AI analysis of text-format layout files. All findings require engineer disposition. AI does not approve or reject the design.*
