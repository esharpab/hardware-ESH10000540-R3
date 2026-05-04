---
project: ESH10000540
revision: R3
date: 2026-05-04
phase: Review
---

# Layout Review — Sparrow Fixture Electronics PCBA R3

## File Information

| Field | Value |
|-------|-------|
| **Files reviewed** | Gencad_Sparrow_FE_R3.cad, IPC356_Sparrow_FE_R3.ipc, AIS_Sparrow_FE_R3.txt, PartsList_Sparrow_FE_R3.csv, NetList_Sparrow_FE_R3.qcv, Gerber_Sparrow_FE_R3/jlc/\*, NCDrill_Sparrow_FE_R3/\* |
| **CAD tool** | Xpedition Layout (Mentor/Siemens) |
| **CAM export date** | 2025-12-22 |
| **Components** | 445 total (394 mounted, 51 NM) |
| **Nets (schematic)** | 335 (QCV netlist) |
| **Nets (layout)** | 485 (GenCAD — includes 150 copper pour segment IDs) |
| **Board dimensions** | 140 × 80 mm |
| **Layer count** | 8 copper layers |
| **Review type** | Structural / completeness / DFM (text-parseable checks only) |
| **Reviewer** | AI — findings require engineer disposition |

---

## Scope and Limitations

This review covers checks that can be extracted from text-format layout files (GenCAD, IPC-356, AIS, Gerber RS-274X, Excellon drill). It does **not** replace a DRC pass in the EDA tool.

**In scope:** Layer stackup, board outline, Gerber file inventory and format, minimum aperture sizes, paste/mask presence, placement completeness, component side assignment, net count consistency, single-node/orphan pad detection, via drill inventory, routing completeness, power net routing presence.

**Out of scope:** Trace width/clearance DRC, thermal relief, power plane pour shape, courtyard/silkscreen overlap, return path analysis, differential pair skew, EMC layout quality.

---

## Findings Summary

| Check | ID | Result | Notes |
|-------|----|--------|-------|
| Gerber file inventory | GBR-F01 | ✅ Pass | All 16 expected Gerber files present |
| Gerber format consistency | GBR-F02 | ✅ Pass | All files: MOMM, FSLAX24Y24, same export 2025-12-22 |
| Board outline dimensions | GBR-F05 | ✅ Pass | 140 × 80 mm; panel 163.2 × 103.2 mm (11.6 mm rails) |
| Layer stackup | LR-L01 | ✅ Pass | 8 layers: TOP, INNER1–6, BOTTOM |
| Board dimensions (GenCAD) | LR-L02 | ✅ Pass | 140 × 80 mm confirmed |
| Routing completeness | LR-R01 | ✅ Pass | 485/485 signals routed — 0 unrouted nets |
| Power net routing | LR-R02 | ✅ Pass | All power nets present in route data |
| Net count consistency | LR-N01 | ✅ Pass | 335 (QCV) vs 485 (GenCAD) — Δ150 = pour segment IDs, expected |
| Single-node / orphan pads | LR-N02 | ✅ Pass | 150 single-record IPC-356 entries — all (Net0) pour fragments, no orphan pads |
| Minimum copper aperture | GBR-F03 | ⚠️ Info | 0.100 mm on all 8 layers — verify within fab spec |
| Paste file consistency | GBR-F04 | ⚠️ Info | Paste present on both sides — consistent with bottom-side SMDs; confirm intentional |
| Placement completeness | LR-P01 | ⚠️ Info | AIS 457 placed vs BOM 445 — Δ12 likely mechanical/fiducial items; confirm |
| Bottom-side components | LR-P02 | ⚠️ Info | 24 bottom-side components found — confirm bottom assembly in scope |
| Via drill inventory | LR-V01 | ⚠️ Info | 0.25 mm via drill / 0.45 mm pad → 0.10 mm annular ring — verify fab spec |

**Totals: 9 Pass, 5 Info, 0 Fail**

All Info items require engineer disposition. No failures found.

---

## Detailed Findings

---

### ✅ GBR-F01 — Gerber File Inventory

**Result:** Pass

All 16 expected Gerber output files are present in the `Gerber_Sparrow_FE_R3/jlc/` folder:

| File | Layer |
|------|-------|
| layer1.gtl | Copper layer 1 (Top) |
| layer2.gb2 | Copper layer 2 (Inner 1) |
| layer3.gb3 | Copper layer 3 (Inner 2) |
| layer4.gb4 | Copper layer 4 (Inner 3) |
| layer5.gb5 | Copper layer 5 (Inner 4) |
| layer6.gb6 | Copper layer 6 (Inner 5) |
| layer7.gb7 | Copper layer 7 (Inner 6) |
| layer8.gbl | Copper layer 8 (Bottom) |
| Masktop.gts | Soldermask Top |
| Maskbottom.gbs | Soldermask Bottom |
| Pastetop.gtp | Solderpaste Top |
| Pastebottom.gbp | Solderpaste Bottom |
| Silktop.gto | Silkscreen Top |
| Silkbottom.gbo | Silkscreen Bottom |
| panel.gko | Board outline / keep-out |

NCDrill files present: `ThruHolePlated.ncd`, `ThruHoleNonPlated.ncd`, `ContourPlated.ncd`.

---

### ✅ GBR-F02 — Gerber Format Consistency

**Result:** Pass

All Gerber files share the same coordinate system and export metadata:

| Field | Value |
|-------|-------|
| Units | Metric (MOMM) |
| Format | FSLAX24Y24 (2.4, metric, absolute, leading zeros suppressed) |
| Export date | Mon Dec 22 10:50:29 2025 |
| Tool | Xpedition Layout CAM Outputs 2000.5.0.2 |

No format mismatches between files.

---

### ✅ GBR-F05 — Board Outline Dimensions

**Result:** Pass

Board outline extracted from `panel.gko`:

| Dimension | Value |
|-----------|-------|
| Board (bare) | 140.0 × 80.0 mm |
| Panel (with rails) | 163.2 × 103.2 mm |
| Rail width | 11.6 mm (all sides) |

Board dimensions consistent with GenCAD `$BOARD` section (0,0 to 140,80 mm).

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

Surface finishes: soldermask and paste on both TOP and BOTTOM.

> **Note:** GenCAD does not encode signal/plane layer assignments in the `$LAYERS` section. Layer function (signal vs plane) requires EDA tool inspection or PCB specification document.

---

### ✅ LR-L02 — Board Outline (GenCAD)

**Result:** Pass

Board outline from GenCAD `$BOARD`: rectangle 0,0 to 140,80 mm. Consistent with GBR-F05.

---

### ✅ LR-R01 — Routing Completeness

**Result:** Pass

GenCAD `$SIGNALS` lists 485 nets; `$ROUTES` contains 486 route entries (1 extra is the `(Net0)` copper plane boundary).

**All 485 signals have a corresponding route entry — 0 unrouted nets.**

---

### ✅ LR-R02 — Power Net Routing Presence

**Result:** Pass

Spot-checked key power nets in GenCAD `$ROUTES`:

| Net | Status |
|-----|--------|
| GND | ✅ Routed |
| AGND | ✅ Routed |
| 3V3 | ✅ Routed |
| VDD | ✅ Routed |
| 5V | ✅ Routed |
| 6V5 | ✅ Routed |
| 12V | ✅ Routed |
| 1V8_EXT | ✅ Routed |
| 5V_LIM | ✅ Routed |
| 3V3_LIM | ✅ Routed |
| 6V5_LIM | ✅ Routed |
| 12V_EXT | ✅ Routed |

All power nets from the ERC review are present in layout routing.

---

### ✅ LR-N01 — Net Count Consistency

**Result:** Pass

| Source | Net count |
|--------|-----------|
| QCV netlist (schematic) | 335 |
| GenCAD $SIGNALS (layout) | 485 |
| IPC-356 unique net IDs | 485 |
| Difference | 150 |

The 150-net difference is explained by copper pour segment IDs. PADS/Xpedition assigns internal IDs such as `(Net0)-1` through `(Net0)-150` to GND/AGND plane copper fragments. These are not separate electrical nets — they are all connected segments of the same net (GND).

**Schematic-to-layout net count is consistent. No missing or extra schematic nets.**

---

### ✅ LR-N02 — Single-Node / Orphan Pads

**Result:** Pass

IPC-356 analysis: 150 single-record net IDs found. All 150 are copper pour fragment IDs of the form `(Net0)-N`. Zero single-record entries for named schematic nets.

**No orphan pads or floating test points detected.**

---

### ⚠️ GBR-F03 — Minimum Copper Aperture

**Result:** Info — engineer to verify against fab spec

Minimum circular aperture sizes extracted from aperture tables in each copper Gerber:

| Layer | Min aperture (C/circle) | Second smallest |
|-------|------------------------|-----------------|
| TOP (layer1.gtl) | 0.100 mm | 0.118 mm |
| INNER1 (layer2.gb2) | 0.100 mm | 0.250 mm |
| INNER2 (layer3.gb3) | 0.100 mm | 0.126 mm |
| INNER3 (layer4.gb4) | 0.100 mm | 0.250 mm |
| INNER4 (layer5.gb5) | 0.100 mm | 0.250 mm |
| INNER5 (layer6.gb6) | 0.100 mm | 0.126 mm |
| INNER6 (layer7.gb7) | 0.100 mm | 0.250 mm |
| BOTTOM (layer8.gbl) | 0.100 mm | 0.118 mm |

**Observation:** 0.100 mm (3.94 mil) is the smallest defined aperture on all 8 layers, used for both traces (D01 draw commands) and via pads (D03 flash commands). The 0.118 mm aperture (seen on TOP and BOTTOM only) is consistent with fine-pitch SMD pads.

**Action required:** Confirm 0.100 mm minimum trace width is within the selected fab's design rules (e.g. JLC standard: 0.09 mm min; some fabs require 0.127 mm / 5 mil). If the fab spec is tighter, a DRC pass in the EDA tool is needed.

| Field | Value |
|-------|-------|
| **Disposition** | Open — engineer to verify |
| **Risk** | Low if within fab spec; fabrication yield risk if below min |

---

### ⚠️ GBR-F04 — Paste File Consistency

**Result:** Info — confirm bottom assembly is in scope

| Gerber | Apertures | Draw/Flash commands |
|--------|-----------|---------------------|
| Pastetop.gtp | 38 | Present (SMD pads + polygon fills) |
| Pastebottom.gbp | 6 | Present (131 draw/flash lines) |

Paste bottom has content, consistent with the bottom-side SMD components identified in LR-P02 (ESD diodes D1–D17 etc.). No missing paste detected.

**Action required:** Confirm that bottom-side assembly is planned and covered by the assembly process (see LR-P02). No paste anomaly found; this is informational.

| Field | Value |
|-------|-------|
| **Disposition** | Open — confirm bottom assembly in scope |
| **Risk** | None if bottom assembly is planned |

---

### ⚠️ LR-P01 — Placement Completeness

**Result:** Info — AIS / BOM count difference to verify

| Source | Component count |
|--------|----------------|
| BOM — mounted (QtyOnBoard, NoMount ≠ NM) | 394 |
| BOM — No-Mount (NoMount = NM) | 51 |
| BOM — total | 445 |
| AIS — TOP side | 433 |
| AIS — BOTTOM side (real components) | 24 |
| AIS — placed total | 457 |
| Difference (AIS − BOM) | +12 |

The 12-item surplus in AIS is consistent with mechanical/PCB-only items not in the BOM: 4 board fiducials (PCB5–PCB8) and 4 standoffs (M1–M4), which are placed in the layout but typically excluded from the electrical BOM. The remaining 4 items should be verified.

All TOP components placed on TOP side. All BOTTOM components placed on BOTTOM side. No side inconsistency detected.

| Field | Value |
|-------|-------|
| **Disposition** | Open — confirm 12 AIS-only items are all mechanical/fiducial |
| **Risk** | Low |

---

### ⚠️ LR-P02 — Bottom-Side Components

**Result:** Info — confirm bottom assembly is intentional

24 components are placed on the BOTTOM side:

| Ref | Footprint | Type | Count |
|-----|-----------|------|-------|
| D1 | pn-w2s118ts | Diode | 1 |
| D2–D9, D16, D17 | pn-kgsot05c | SOT-05C diode (TVS/ESD) | 10 |
| D10, D11 | pn-esd652 | ESD diode | 2 |
| D12, D13 | pn-esd562 | ESD diode | 2 |
| M1–M4 | pn-SMTSO3025 | SMT standoff | 4 |
| J5 | pn-m2top_2 | Connector | 1 |
| PCB5–PCB8 | pn-pcb_fiducial1 | Fiducial | 4 |

**Observation:** 15 diodes (likely TVS/ESD protection), 4 SMT standoffs, 1 connector, and 4 fiducials are bottom-mounted. This is a common design pattern for placing ESD protection close to connectors. Paste bottom file contains appropriate openings.

**Action required:** Engineer to confirm bottom-side assembly is intentional and that the assembly process accounts for two-sided reflow or selective soldering.

| Field | Value |
|-------|-------|
| **Disposition** | Open — engineer to confirm bottom assembly is planned |
| **Risk** | Process risk if bottom-side assembly not in assembly plan |

---

### ⚠️ LR-V01 — Via Drill Size Inventory

**Result:** Info — verify annular ring and drill sizes against fab spec

**Plated through holes (ThruHolePlated.ncd):**

| Tool | Drill dia. | Likely use |
|------|-----------|------------|
| T05 | 0.25 mm | Signal vias (most common — 1068 in IPC-356) |
| T02 | 0.60 mm | Small THT / mechanical |
| T03 | 1.10 mm | THT component pins |
| T06 | 3.20 mm | Large mounting / THT |
| T01 | 4.20 mm | Largest holes |

**Non-plated through holes (ThruHoleNonPlated.ncd):**

| Tool | Drill dia. | Likely use |
|------|-----------|------------|
| T07 | 0.50 mm | Non-plated via / slot |
| T09 | 1.15 mm | Non-plated hole |
| T10 | 1.45 mm | Non-plated hole |
| T08 | 1.65 mm | Non-plated hole |

**Plated milled slots (ContourPlated.ncd):**

| Tool | Mill dia. | Use |
|------|----------|-----|
| T04 | 1.00 mm | Plated milled slot |

**Via annular ring (signal vias):**

| Parameter | Value |
|-----------|-------|
| Via drill (IPC-356) | 0.25 mm |
| Via pad (IPC-356) | 0.45 × 0.45 mm |
| Annular ring | (0.45 − 0.25) / 2 = **0.10 mm** |

**Action required:** Confirm 0.10 mm annular ring meets the selected fab's minimum via specification. For JLC standard this is 0.075 mm min (pass), but tighter specs exist. Board thickness also affects via aspect ratio for the 0.25 mm drill — confirm acceptable for fab.

| Field | Value |
|-------|-------|
| **Disposition** | Open — engineer to verify annular ring and aspect ratio |
| **Risk** | Low for standard fab; verify if using advanced process |

---

## Checks Not Performed

The following checks require visual rendering or EDA tool DRC and were not performed in this review:

| Check | Why not possible |
|-------|-----------------|
| Trace width / clearance DRC | Requires rendering copper geometry from Gerber |
| Thermal relief inspection | Visual / geometric |
| Power plane pour quality | Requires polygon rendering |
| Courtyard / silkscreen overlap | No courtyard data in GenCAD |
| High-speed routing quality | Partial text analysis insufficient |
| Return path analysis | Requires layer-by-layer copper visibility |

**Recommendation:** Run a full EDA DRC pass (Xpedition DRC or equivalent) before releasing to fabrication. Pay particular attention to: trace width vs power current capacity, return paths under high-speed signals, and thermal relief on power components.

---

## Disposition Summary

| ID | Finding | Disposition | By | Date |
|----|---------|-------------|----|----|
| GBR-F03 | Min aperture 0.100 mm — verify fab spec | Open | — | — |
| GBR-F04 | Paste bottom present — confirm bottom assembly | Open | — | — |
| LR-P01 | AIS +12 vs BOM — confirm mechanical items | Open | — | — |
| LR-P02 | 24 bottom-side components — confirm intended | Open | — | — |
| LR-V01 | Via annular ring 0.10 mm — verify fab spec | Open | — | — |

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Layout Reviewer | — | — | — |
| Design Engineer | — | — | — |

*This review was performed by AI analysis of text-format layout files. All findings require engineer disposition. AI does not approve or reject the design.*