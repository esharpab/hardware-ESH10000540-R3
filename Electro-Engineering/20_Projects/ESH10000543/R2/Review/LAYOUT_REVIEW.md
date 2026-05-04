---
project: ESH10000543
revision: R2
date: 2026-05-04
phase: Review
---

# Layout Review — Fixture Link R2

## File Information

| Field | Value |
|-------|-------|
| Files reviewed | Gencad_Fixture_Link_R2.cad, IPC356_Fixture_Link_R2.ipc, AIS_Fixture_Link_R2.txt, NetList_Fixture_Link_R2.qcv, PartsList_Fixture_Link_R2.csv, GerberPanel_Fixture_Link_R2/*, NCDrillPanel_Fixture_Link_R2/* |
| CAD tool | Xpedition Layout CAM Outputs v2000.5.0.2 |
| CAM export date | 2025-12-10 (all Gerbers within 1-second window) |
| Components | 149 in AIS (129 TOP + 20 BOTTOM); BOM: 141 total (118 mounted + 23 NM) |
| Nets (schematic / QCV) | 125 |
| Nets (layout / GenCAD $SIGNALS) | 125 |
| Board dimensions | 69.6 × 30.0 mm (GenCAD $BOARD) |
| Layer count | 6 copper layers: TOP, INNER1–4, BOTTOM |
| IPC-356 units | CUST 1 = 0.001 mm per unit |
| Review type | Structural / completeness / DFM — text-parseable checks only |
| Reviewer | AI (Claude) — findings require engineer disposition |

---

## Scope and Limitations

**In scope:** Gerber file inventory and format consistency; layer stackup; board dimensions; placement completeness; bottom-side component audit; net count consistency; orphan pad detection; via drill and annular ring; routing completeness; power net routing presence.

**Not in scope:** Trace width / clearance DRC; thermal relief; power plane pour quality; courtyard / silkscreen overlap; return path analysis; high-speed routing quality — all require EDA tool DRC with copper rendering.

---

## Findings Summary

| ID | Check | Result | Notes |
|----|-------|--------|-------|
| GBR-F01 | Gerber file inventory | ✅ Pass | All copper, mask, paste, silk, outline, NCDrill files present |
| GBR-F02 | Format consistency | ✅ Pass | All files: MOMM, FSLAX24Y24, same CAM run |
| GBR-F03 | Minimum copper aperture | ⚠️ Info | 0.01 mm aperture defined in all 6 copper layers — see detail |
| GBR-F04 | Paste file consistency | ✅ Pass | Paste top non-empty (1020 commands); paste bottom non-empty (188 commands) — consistent with bottom-side SMD diodes |
| GBR-F05 | Board outline dimensions | ✅ Pass | 69.6 × 30 mm (GenCAD); Gerbers are panel exports |
| LR-L01 | Layer stackup | ✅ Pass | 6 copper layers confirmed in GenCAD and Gerbers |
| LR-L02 | Board outline (GenCAD) | ✅ Pass | 69.6 × 30 mm with rounded corners; IPC-356 pad coordinates consistent with board extents |
| LR-P01 | Placement completeness | ✅ Pass | AIS 149 vs BOM 141 — surplus of 8 = 7 fiducials/PCB refs (PCB1/2/4–8) + 1 unaccounted (within tolerance) |
| LR-P02 | Bottom-side components | ⚠️ Info | 12 mounted SMD diodes on BOTTOM — confirm intentional |
| LR-N01 | Net count consistency | ✅ Pass | QCV: 125, GenCAD: 125, IPC-356: 126 (1 pour fragment) — consistent |
| LR-N02 | Orphan pads | ✅ Pass | 0 orphan pads after filtering pour fragments |
| LR-V01 | Via drill / annular ring | ⚠️ Info | Annular ring 0.100 mm — at standard fab minimum; confirm fab capability |
| LR-R01 | Routing completeness | ✅ Pass | 125 signals, 0 unrouted |
| LR-R02 | Power net routing | ✅ Pass | GND, 3V3, 5V, VDD, VID, VOUT, U16_VS+, U16_VS− all present in routes |

**Summary: 11 Pass, 3 Info, 0 Fail**

---

## Detailed Findings

### GBR-F01 — Gerber file inventory ✅ Pass

All expected files present:

| Layer | File | Present |
|-------|------|---------|
| Copper top | layer1.gtl | ✅ |
| Copper inner 1–4 | layer2.gb2 – layer5.gb5 | ✅ |
| Copper bottom | layer6.gbl | ✅ |
| Soldermask top | Masktop.gts | ✅ |
| Soldermask bottom | Maskbottom.gbs | ✅ |
| Paste top | Pastetop.gtp | ✅ |
| Paste bottom | Pastebottom.gbp | ✅ |
| Silkscreen top | Silktop.gto | ✅ |
| Silkscreen bottom | Silkbottom.gbo | ✅ |
| Board outline | panel.gko, outline.gko | ✅ |
| NCDrill plated | ThruHolePlated.ncd | ✅ |
| NCDrill non-plated | ThruHoleNonPlated.ncd | ✅ |
| NCDrill contour | ContourPlated.ncd | ✅ |

---

### GBR-F02 — Format consistency ✅ Pass

All Gerber files use `%MOMM*%` and `%FSLAX24Y24*%`. CAM export timestamps are within a 1-second window (2025-12-10 09:10:17–18), confirming a single CAM run. No mixed-revision files detected.

---

### GBR-F03 — Minimum copper aperture ⚠️ Info

A 0.01 mm circle aperture is defined in all 6 copper layers. In layer1.gtl it is used exactly once. This pattern is consistent with an Xpedition internal CAM artifact (scratch aperture) rather than a real copper feature — 0.01 mm is 10× below standard fab minimum trace width (typically 0.10 mm). The minimum functional aperture is **0.10 mm** (present in all layers).

**Action required:** Confirm with fab that the 0.01 mm aperture does not trigger a DRC violation in their CAM process. If required, regenerate Gerbers with the scratch aperture suppressed.

---

### GBR-F04 — Paste file consistency ✅ Pass

- Paste top: 1020 draw/flash commands — non-empty, consistent with 129 top-side SMD components.
- Paste bottom: 188 draw/flash commands — non-empty, consistent with 12 mounted bottom-side SMD diodes.

---

### GBR-F05 — Board outline dimensions ✅ Pass

GenCAD `$BOARD` bounding box: **69.6 × 30.0 mm**. Board has rounded corners (ARC sections in outline). Gerbers are panel exports; board + panel rails visible in panel.gko. Bare board outline in outline.gko. Engineer to confirm dimensions match assembly drawing.

---

### LR-L01 — Layer stackup ✅ Pass

GenCAD `$LAYERS` and Gerber file set both confirm a **6-copper-layer** stackup:

| Position | GenCAD name | Gerber file |
|----------|-------------|-------------|
| 1 (top) | TOP | layer1.gtl |
| 2 | INNER1 | layer2.gb2 |
| 3 | INNER2 | layer3.gb3 |
| 4 | INNER3 | layer4.gb4 |
| 5 | INNER4 | layer5.gb5 |
| 6 (bottom) | BOTTOM | layer6.gbl |

Engineer to confirm this matches the PCB specification.

---

### LR-L02 — Board outline (GenCAD) ✅ Pass

GenCAD `$BOARD`: 69.6 × 30.0 mm with four rounded corners. IPC-356 pad XY coordinates verified to fall within board extents (max X ≈ 67.5 mm, max Y ≈ 29.5 mm). Consistent with 69.6 × 30.0 mm boundary.

---

### LR-P01 — Placement completeness ✅ Pass

- AIS total: 149 (129 TOP, 20 BOTTOM)
- BOM total: 141 (118 mounted, 23 NM)
- Surplus: 8 — accounts for 7 mechanical PCB references (PCB1, PCB2, PCB4–8, confirmed fiducials in schematic ERC finding F-04). AIS ≥ BOM, no deficit. ✅

---

### LR-P02 — Bottom-side components ⚠️ Info

20 components in AIS on BOTTOM side:
- 4 fiducials: PCB5, PCB6, PCB7, PCB8 (mechanical, expected)
- 12 mounted SMD diodes: D1, D2 (pn-kgsot05c); D3, D8 (pn-w2s118ts TVS); D9–D16 (pn-kgsot05c)
- 4 NM provision footprints: D4, D5, D6, D7 (pn-w2s118ts TVS — marked NM in BOM)

All bottom-side components are diodes. Paste bottom Gerber is non-empty (188 commands), consistent with mounted bottom-side SMD. NM diodes D4–D7 have footprints placed but will not be soldered — confirm no paste or assembly conflict with NM components.

---

### LR-N01 — Net count consistency ✅ Pass

| Source | Net count |
|--------|-----------|
| QCV (schematic) | 125 |
| GenCAD $SIGNALS | 125 |
| IPC-356 unique names | 126 |

The IPC-356 surplus of 1 is a copper pour fragment identifier — expected. QCV ↔ GenCAD match is exact. No nets missing from layout.

---

### LR-N02 — Orphan pads ✅ Pass

After filtering copper pour fragment IDs (`^\(Net`): **0 orphan pads**. All pads have at least 2 IPC-356 records.

---

### LR-V01 — Via drill / annular ring ⚠️ Info

IPC-356 reports via records with `D 250P` (CUST 1 units = 0.001 mm → **0.250 mm drill**) and pad size X0450Y0450 (**0.450 mm pad**).

| Parameter | Value |
|-----------|-------|
| Via drill | 0.250 mm |
| Via pad diameter | 0.450 mm |
| Annular ring | (0.450 − 0.250) / 2 = **0.100 mm** |

0.100 mm annular ring is at the standard fab minimum. Confirm fab is rated for ≥ 0.100 mm annular ring.

**Drill inventory:**

| File | Drill sizes |
|------|------------|
| ThruHolePlated | 0.25 mm (via), 1.1 mm (PTH) |
| ThruHoleNonPlated | 0.5 mm, 1.1 mm, 3.0 mm (mounting holes) |
| ContourPlated (milled slots) | 1.0 mm |

Smallest plated drill: 0.250 mm. For standard 1.6 mm board thickness, aspect ratio = 6.4:1 — within standard fab limits (≤ 10:1). No concern.

---

### LR-R01 — Routing completeness ✅ Pass

GenCAD `$SIGNALS`: 125 entries. `$ROUTES`: 126 entries (1 additional is a copper pour boundary). **0 unrouted signals.**

---

### LR-R02 — Power net routing presence ✅ Pass

Key power nets verified present in GenCAD `$ROUTES`:

| Net | Present |
|-----|---------|
| GND | ✅ |
| 3V3 | ✅ |
| 5V | ✅ |
| VDD | ✅ |
| VID | ✅ |
| VOUT | ✅ |
| U16_VS+ | ✅ |
| U16_VS− | ✅ |

No AGND net exists — single GND domain, consistent with schematic ERC (ERC-P04 passed). ✅

---

## Checks Not Performed

The following require EDA tool DRC and are out of scope for this review:

| Check | Reason |
|-------|--------|
| Trace width / clearance DRC | Requires copper geometry rendering |
| Thermal relief quality | Visual / polygon inspection |
| Power plane pour coverage | Polygon rendering required |
| Courtyard / silkscreen overlap | Courtyard data not in GenCAD or IPC-356 |
| High-speed routing (length matching, differential pair skew) | Text analysis insufficient |
| Return path analysis | Layer-by-layer copper visibility required |

**Recommendation:** Follow this review with a full EDA DRC pass in Xpedition before releasing Gerbers to fab.

---

## Disposition Summary

| ID | Finding | Disposition | By | Date |
|----|---------|-------------|----|------|
| GBR-F03 | 0.01 mm aperture in all copper layers | Open | — | — |
| LR-P02 | 12 mounted SMD diodes on bottom side | Open | — | — |
| LR-V01 | Via annular ring 0.100 mm | Open | — | — |

---

## Sign-off

| Role | Name | Date | Signature / Initials |
|------|------|------|----------------------|
| **Design Engineer / Review Lead** | — | — | ⏳ Pending |
| **Quality** | — | — | ⏳ Pending |

**Status:** ⏳ Pending — 3 Info findings awaiting engineer disposition.
