---
project: ESH10000633
revision: R1
document: Production Readiness Checklist
status: Draft
created: 2026-05-04
target_qty: 20
target_deadline: 2026-07-13 (10 weeks from 2026-05-04)
---

# Production Readiness Checklist — Sparrow Complete Product R1

**Target:** 20 units by 2026-07-13 (10 weeks) — **scope expanded 2026-05-12** with additional standalone deliverables (see below)
**Source:** MES BOM extracted 2026-05-04. All inventory levels as of that date.

## Delivery Scope (updated 2026-05-12)

| Item | Qty | Note |
|------|-----|------|
| ESH10000633 R1 (Sparrow Complete Product — full system) | 20 | Original scope |
| ESH10000636 R1 (Sparrow ASSY FE with Active Load) | 10 | **New** — standalone (in addition to the 20 inside systems) |
| ESH10000614 R0 (Sleeved Coax Cable HLCD-20-40.00) | 20 | **New** — standalone (in addition to the 20 inside systems) |
| ESH10000637 R0 (Sparrow PSU Power Cable 1m) | 20 | **New** — standalone (in addition to the 20 inside systems) |
| EPN1000786 (D-Sub cable 1m) | 20 | **New** — standalone (in addition to the 20 inside systems) |

**Combined totals** (used for §3 inventory calculations):
- ESH10000636: 30 (20 in systems + 10 standalone)
- ESH10000614: 40 (20 + 20)
- ESH10000637: 40 (20 + 20)
- EPN1000786: 40 (20 + 20)
- Children of ESH10000636 (ESH10000540, 634, 536): 30 each (10 more than original)

---

## 1. BOM Hierarchy (from MES)

> **⚠️ MES limitation — this document is the authoritative revision pin.**
> MES does not currently support revision-specific parent-BOM references: when a parent BOM lists a sub-assembly, it points to the part number but not to a specific revision. The hierarchy below is therefore the **authoritative record** of which revision of each sub-assembly is targeted for this production run. When work orders are released, the operator/scheduler must use this document to select the correct revision of each child item. Any change to a target revision must be reflected here.
>
> **The only MES-side control:**
> - **Hard rule** — for each part, **at most one revision at Manufacturing status**. This is what MES uses to resolve a single live revision when a parent BOM points to a part number.
> - **Soft rule** — older revisions retired to **EndOfLife**, **Obsolete**, or **NotApproved** (any of those is acceptable; the choice has no functional difference for revision resolution).
> Maintaining the hard rule is part of Gate 1; the soft rule is good hygiene.

```
ESH10000633 R1 — Sparrow Complete Product (Manufacturing)
│
├── ESH10000631 R1 — Sparrow Accordion A2 (Manufacturing)                    ×1/unit
│   ├── ESH10000182 R0 — Accordion A2 Bare (Manufacturing ✅ 2026-05-15)     ×1
│   │   ├── ESH10000158 R5 — Accordion A2 Base PCBA (Manufacturing; PCBA externally built — no MES BOM needed) ✅ ×1
│   │   ├── ESH10000183 R6 — Accordion A2 Top PCBA (Manufacturing; PCBA externally built — no MES BOM needed) ✅ ×1
│   │   ├── ESH10000539 R2 — Control Module 32ch A2 (Manufacturing ✅; BOM 33 items; R0+R1 EOL ✅) ×1
│   │   ├── ESH10000031 R0 — Raspberry Pi 4B 8GB (Manufacturing)             ×1
│   │   ├── ESH10000538 R1 — M2base loopback (Manufacturing ✅; externally built — no MES BOM needed; 100 pcs on order ETA 2026-05-29; R0 NotApproved) ×1
│   │   ├── ESH10000062 R1 — PCIe16 riser for AGENT base (Manufacturing ✅; externally built — no MES BOM needed; R0 NotApproved) ×2
│   │   ├── EPN1000012     — Agent Fan 25×10mm 5V (purchased)                ×1
│   │   ├── EPN1000068     — RPI Fan 30×10mm 5V (purchased)                  ×1
│   │   ├── EPN1000072     — SD card 32GB (purchased)                        ×1
│   │   └── (fasteners, Hammond enclosure, misc)
│   ├── ESH10000535 R3 — Sparrow N-Top (Manufacturing) ✅                     ×1
│   ├── ESH10000543 R2 — Fixture Link (Manufacturing) ✅                      ×1
│   ├── ESH10000534 R4 — M2Top PoE (Manufacturing ✅; PCBA in internal assembly — ETA 2026-05-22) ⏳ ×1
│   ├── ESH10000544 R3 — A2 Front Panel DSub Fixturelink (Manufacturing ✅; externally built — no MES BOM; 75 pcs on order; R0 Obsolete, R1 EOL ✅) ×1
│   ├── ESH10000522 R5 — A2 Back Panel (Manufacturing ✅; externally built — no MES BOM; R0+R1 EOL ✅) ×1
│   ├── ESH10000572 R3 — Accordion Sparrow Top (Manufacturing ✅; externally built — no MES BOM; 75 pcs on order; R0 Obsolete, R1 EOL ✅) ×1
│   ├── ESH10000024 R0 — Accordion Loopback R2 (Manufacturing)               ×5
│   └── (fasteners, LED fibres, misc)
│
├── ESH10000636 R1 — Sparrow ASSY FE with Active Load (Manufacturing)         ×1/unit
│   ├── ESH10000540 R3 — Sparrow Fixture Electronics (Manufacturing) ✅        ×1
│   ├── ESH10000634 R3 — Sparrow IDC N-Top (Manufacturing, BOM 21 items; PCB in-house; PCBA in internal assembly — ETA 2026-05-22) ⏳ ×1
│   ├── ESH10000536 R2 — M2Top Active Load (Manufacturing) ✅                  ×1
│   └── (connector, fasteners)
│
├── ESH10000582 R1.0 — USB PD 100W PSU (Manufacturing ✅ 2026-05-12; BOM 6 items; R0.1 → EOL ✅) ×1/unit
│   ├── ESH10000579 R1.0 — USB PD 100W PSU PCBA (Manufacturing ✅ 2026-05-12; BOM TBC; R0.1+R0.2 NotApproved) ×1
│   ├── ESH10000580 R1.0 — USB PD 100W PSU Front Panel (Manufacturing ✅ 2026-05-12; BOM TBC; R0.1 NotApproved) ×1
│   └── ESH10000581 R1.0 — USB PD 100W Rear Panel (Manufacturing ✅ 2026-05-12; BOM TBC; R0.1 NotApproved) ×1
│
├── ESH10000614 R0 — Sleeved Coax Cable HLCD-20-40.00 (Manufacturing) ✅       ×1/unit
│   ├── EPN1000718     — CABLE HLCD-20-40.00-TRS-TLS-4 (purchased)           ×1
│   ├── ESH10000615 R0 — Kontakthuvud HLCD-20-40.00 (Manufacturing; externally built — no MES BOM needed) ✅ ×2
│   └── (fasteners)
│
├── ESH10000637 R0 — Sparrow PSU Power Cable 1m (Manufacturing)               ×1/unit
│   ├── EPN1000249     — Terminal block plug 2pos 5.08mm (purchased)          ×1
│   └── EPN1000703     — 15EDGK-3.81-02P connector (purchased)               ×1
│
├── EPN1000677    — 5-port USB wall charger 1.5m (purchased)                  ×1/unit
├── EPN1000678    — 100W USB-C charging cable 1m (purchased)                  ×1/unit
├── EPN1000786    — D-Sub cable 1m                                 ×1/unit
└── EPN1000752    — M3 standoffs 8.6mm (3D-printed)                ×5/unit
```

---

## 2. Design Readiness

> **Gate:** All sub-assemblies used in production must be at **Manufacturing** status in MES before production start.

| ESH | Name | Rev | MES Status | BOM | Design Gate |
|-----|------|-----|-----------|-----|-------------|
| ESH10000633 | Sparrow Complete Product | R1 | Manufacturing | ✅ | ✅ |
| ESH10000631 | Sparrow Accordion A2 | R1 | Manufacturing | ✅ | ✅ |
| ESH10000636 | Sparrow ASSY FE with Active Load | R1 | Manufacturing | ✅ | ✅ |
| ESH10000582 | USB PD 100W PSU | R1.0 | Manufacturing | ✅ (6 items) | ✅ R1.0 sole Mfg rev (R0.1 → EOL ✅ 2026-05-12) — clean |
| ESH10000024 | Accordion Loopback R2 | R0 | Manufacturing | — | ✅ |
| ESH10000634 | Sparrow IDC N-Top | R3 | Manufacturing | ✅ (21 items) | ⏳ R3 BOM in MES ✅ 2026-05-11; PCB in-house (98 pcs); PCBA assembly to be scheduled. R1+R2 at NotApproved — clean (only R3 at Manufacturing). **Revision target pinned to R3 in §1 of this doc** (MES BOMs are not revision-specific) |
| ESH10000540 | Sparrow Fixture Electronics | R3 | Manufacturing | ✅ | ✅ Promoted 2026-05-11; R1+R2 at NotApproved — clean (only one at Manufacturing) |
| ESH10000535 | Sparrow N-Top | R3 | Manufacturing | ✅ | ✅ Promoted 2026-05-11; R1+R2 at NotApproved — clean |
| ESH10000543 | Fixture Link | R2 | Manufacturing | ✅ | ✅ Promoted 2026-05-11; R0+R1 at NotApproved — clean |
| ESH10000534 | M2Top PoE | R4 | Manufacturing | ✅ | ✅ Promoted 2026-05-11; R1+R2+R3 at NotApproved — clean |
| ESH10000536 | M2Top Active Load | R2 | Manufacturing | ✅ | ✅ Promoted 2026-05-11; R0 Obsolete, R1 EOL — clean |
| ESH10000182 | Accordion A2 Bare | R0 | Manufacturing | ✅ | ✅ Promoted 2026-05-15 |
| ESH10000522 | A2 Back Panel | R5 | Manufacturing | N/A — externally built | ✅ Single-Mfg clean: R5 active, R0+R1 EOL (2026-05-15). No MES BOM expected |
| ESH10000158 | Accordion A2 Base PCBA | R5 | Manufacturing | N/A — externally built | ✅ R5 sole Manufacturing rev (R3+R4 → EOL 2026-05-11); R6 in design (sidetrack). Procurement closes the −19 shortfall |
| ESH10000183 | Accordion A2 Top PCBA | R6 | Manufacturing | N/A — externally built | ✅ R6 sole Manufacturing rev (R5 → EOL 2026-05-11); 20 pcs in stock — not blocking |
| ESH10000539 | Control Module 32ch A2 | R2 | Manufacturing | ✅ (33 items) | ✅ Single-Mfg clean: R2 active, R0+R1 EOL (2026-05-15). BOM 33 items (R61, R67 mount toggled from DNP) |
| ESH10000544 | A2 Front Panel DSub | R3 | Manufacturing | N/A — externally built | ✅ Single-Mfg clean: R3 active, R0 Obsolete, R1 EOL (2026-05-15). 75 pcs R3 on order |
| ESH10000572 | Accordion Sparrow Top | R3 | Manufacturing | N/A — externally built | ✅ Single-Mfg clean: R3 active, R0 Obsolete, R1 EOL (2026-05-15). 75 pcs R3 on order |
| ESH10000614 | Sleeved Coax Cable | R0 | Manufacturing | ✅ | ✅ Promoted 2026-05-11; 51 pcs in stock — adequate for 20-unit run |
| ESH10000615 | Kontakthuvud HLCD-20-40.00 | R0 | Manufacturing | N/A — externally built | ✅ Promoted 2026-05-11; externally built (no MES BOM expected). 51 pcs of parent ESH10000614 already in stock |

**Summary: 6 sub-assemblies at Prototype, 2 at NotApproved (no BOM). All must reach Manufacturing status before production start.**

---

## 3. Inventory vs. Requirement (20 units)

> Quantities marked **On Hand** are physically in stock. **Available** = On Hand + Pending (on order).
> Items with no inventory record are assumed to be built-to-order or not yet stocked.

### 3.1 Top-Level BOM Items

> **Need column updated 2026-05-12** to reflect expanded delivery scope (see "Delivery Scope" callout above).

| Part | Name | Qty/Unit | Need | On Hand | Available | Gap | Status |
|------|------|----------|------|---------|-----------|-----|--------|
| ESH10000631 | Sparrow Accordion A2 | 1 | 20 | — | — | — | Built to order (only inside systems) |
| ESH10000636 | Sparrow ASSY FE with Active Load | 1 | **30** (20 + 10 standalone) | — | — | — | Built to order |
| ESH10000582 | USB PD 100W PSU | 1 | 20 | 32 | 32 | +12 | ✅ stock adequate. R1.0 sole Mfg rev ✅ 2026-05-12 (R0.1 → EOL). Existing 32 pcs are R0.1 — confirm usability for R1.0 production |
| ESH10000614 | Sleeved Coax Cable | 1 | **40** (20 + 20 standalone) | 51 | 51 | +11 | ✅ still adequate after scope expansion |
| ESH10000637 | Sparrow PSU Power Cable 1m | 1 | **40** (20 + 20 standalone) | 0 | 0 | **−40** | 🔴 Order required — doubled by scope expansion |
| EPN1000677 | 5-port USB wall charger | 1 | 20 | 18 | 18 | **−2** | 🔴 Order 2+ |
| EPN1000678 | 100W USB-C cable | 1 | 20 | 84 | 84 | +64 | ✅ |
| EPN1000786 | D-Sub cable 1m | 1 | **40** (20 + 20 standalone) | 50 | 50 | +10 | ✅ still adequate after scope expansion |
| EPN1000752 | M3 standoffs 8.6mm | 5 | 100 | 213 | 213 | +113 | ✅ |

### 3.2 ESH10000631 — Sparrow Accordion A2 (contents, ×1 per unit)

| Part | Name | Qty/Unit | Need ×20 | On Hand | Available | Gap | Status |
|------|------|----------|----------|---------|-----------|-----|--------|
| ESH10000182 | Accordion A2 Bare | 1 | 20 | 1 | 1 | **−19** | 🔴 Critical shortage |
| ESH10000535 | Sparrow N-Top R3 | 1 | 20 | 24 | 24 | +4 | ✅ 24 pcs in Testing — released for production (2026-05-15) |
| ESH10000543 | Fixture Link R2 | 1 | 20 | 48 | 48 | +28 | ✅ |
| ESH10000534 | M2Top PoE R4 | 1 | 20 | 15 | 39 | +19 | ✅ 15 on hand + 24 in internal PCBA assembly (ETA 2026-05-22) |
| ESH10000544 | A2 Front Panel DSub | 1 | 20 | 6 (R0 Obs) | 81 | **+61** | ✅ R3 in MES; **75 pcs R3 on order ✅ 2026-05-15**. 6 pcs on hand are R0 (Obsolete — not for production). Comfortable margin after delivery |
| ESH10000522 | A2 Back Panel | 1 | 20 | 26 | 26 | +6 | ⚠️ 26 pcs on hand are R1 (now EOL); target rev R5 — confirm whether R1 stock is usable as-is or must be replaced/reworked |
| ESH10000572 | Accordion Sparrow Top | 1 | 20 | 7 (R0 Obs) | 82 | **+62** | ✅ R3 in MES; **75 pcs R3 on order ✅ 2026-05-15**. 7 pcs on hand are R0 (Obsolete — not for production). Comfortable margin after delivery |
| ESH10000024 | Accordion Loopback R2 | 5 | 100 | 751 | 751 | +651 | ✅ |

### 3.3 ESH10000636 — Sparrow ASSY FE with Active Load (contents, ×1 per unit)

> **Need recomputed 2026-05-12** to ×30 (20 in systems + 10 standalone).

| Part | Name | Qty/Unit | Need ×30 | On Hand | Available | Gap | Status |
|------|------|----------|----------|---------|-----------|-----|--------|
| ESH10000540 | Sparrow Fixture Electronics R3 | 1 | 30 | 50 | 50 | +20 | ✅ 50 pcs in Testing — released for production (2026-05-15) |
| ESH10000634 | Sparrow IDC N-Top R3 | 1 | 30 | 0 | 98 | +68 | ⏳ PCB in-house (98 pcs); **PCBA in internal assembly — ETA 2026-05-22** |
| ESH10000536 | M2Top Active Load R2 | 1 | 30 | 31 | 31 | +1 | ⚠️ Very tight margin (1 spare after scope expansion). All 31 pcs in *Testing* — released for production (2026-05-15) |

### 3.4 ESH10000182 — Accordion A2 Bare (contents, ×1 per Accordion A2)

> 1 ESH10000182 is already on hand; **19 new builds** are required to cover 20 production units.
> Need column shows components required for those 19 builds. Inventory snapshot 2026-05-05.

| Part | Name | Qty/Build | Need ×19 | On Hand | Available | Gap | Status |
|------|------|-----------|----------|---------|-----------|-----|--------|
| ESH10000158 | Accordion A2 Base PCBA (R5) | 1 | 19 | 0 | 0 | **−19** | 🔴 **CRITICAL — decision by 2026-05-27** on whether to order more R5 (vs. wait for R6 sidetrack). Externally built; no internal WO/BOM. R5 is sole Mfg rev. **No order in MES.** |
| ESH10000183 | Accordion A2 Top PCBA (R6) | 1 | 19 | 20 | 20 | +1 | ⚠️ Very tight margin (1 spare) |
| ESH10000539 | Control Module 32ch A2 (R2) | 1 | 19 | 0 (usable) | 60 | +41 | ✅ Single-Mfg clean (R2 Mfg; R0+R1 EOL 2026-05-15). 60 incoming boards mounted as R2 spec. 7 R1 pcs in *Testing* kept as-is (not for this build) |
| ESH10000031 | Raspberry Pi 4B 8GB | 1 | 19 | 39 | 39 | +20 | ✅ |
| ESH10000062 | PCIe16 riser for AGENT base | 2 | 38 | 265 | 265 | +227 | ✅ R1 at Manufacturing; **externally built — no MES BOM needed** (confirmed 2026-05-15). 265 pcs on hand are R0 — confirm reuse vs scrap |
| ESH10000538 | M2base loopback | 1 | 19 | 0 (usable) | 100 | +81 | ✅ R1 at Manufacturing; **externally built — no MES BOM needed**. **100 pcs R1 on order — ETA 2026-05-29**. 15 R0 pcs on hand → **scrap** (decided 2026-05-15). ⚠️ ISSUE-001 (SPI/loopback intermittency) — confirm whether R1 design addresses this |
| EPN1000012 | Agent Fan 25×10mm 5V | 1 | 19 | 22 | 22 | +3 | ⚠️ Tight margin (3 spare) |
| EPN1000068 | RPI Fan 30×10mm 5V | 1 | 19 | 15 | 15 | **−4** | 🔴 Order ≥4 |
| EPN1000072 | SD card 32GB | 1 | 19 | 106 | 106 | +87 | ✅ |
| EGP10001249 | Connector 6-173977-3 (3p fan housing) | 2 | 38 | 163 | 163 | +125 | ✅ |
| EPN1000439 | Hammond enclosure (blue, AGENT A2) | 1 | 19 | 20 | 20 | +1 | ⚠️ Very tight margin (1 spare) |
| EPN1000704 | CAP pushbutton square black | 1 | 19 | 142 | 142 | +123 | ✅ |
| EPN1000676 | Jumper 2.54 mm 2-pos black | 1 | 19 | 45 | 45 | +26 | ✅ |
| EPN1000152 | Skruv M2.5 × 16 mm | 6 | 114 | 326 | 326 | +212 | ✅ |
| EPN1000182 | Mutter M2.5 | 6 | 114 | 221 | 221 | +107 | ✅ |
| EPN1000154 | Skruv M3 × 8 mm | 1 | 19 | 750 | 750 | +731 | ✅ |
| EPN1000213 | Skruv M3 × 4 mm | 1 | 19 | 454 | 454 | +435 | ✅ |
| EPN1000186 | Mutter M3 | 1 | 19 | 994 | 984 | +965 | ✅ |

**Summary — ESH10000182 build of 19:**
- 🔴 2 critical shortages remaining: **ESH10000158 (−19, decision due 2026-05-27 — see G-13)**, **EPN1000068 (−4)**
- ✅ Resolved 2026-05-08 by procurement orders: **ESH10000538 (+96 after 100 pcs on order)**, **ESH10000539 (+48 after 60 pcs on order)**
- ⚠️ 3 tight margins (≤3 spare): **ESH10000183 (+1), EPN1000439 (+1), EPN1000012 (+3)**
- **ESH10000538:** R1 at Mfg ✅; **externally built — no MES BOM needed** (confirmed 2026-05-15); 100 pcs R1 on order ETA 2026-05-29. 15 R0 pcs on hand → **scrap** (decided 2026-05-15). **ESH10000062:** R1 at Mfg ✅; **externally built — no MES BOM needed** (confirmed 2026-05-15); 265 pcs R0 on hand — disposition TBC.
- ⚠️ **ESH10000538 R0 — open quality concern (ISSUE-001):** intermittent Sparrow N-Top startup faults suspected to be linked to loopback PCB thickness or SPI startup sequencing. **Not a gate** — flagged for investigation in parallel with build planning. **Open question:** does the R1 design address this? See `ISSUES/ISSUE-001_M2base_loopback_SPI_intermittent.md`.
- ✅ **ESH10000539 R1 → R2 BOM change (ISSUE-002):** mount R67 (10 kΩ) for DRxD; mount R61 (10 kΩ) for DCTS. **R2 in MES ✅ 2026-05-12**. **Decisions 2026-05-12:** 60 incoming boards mounted as R2 spec ✅; 7 R1 pcs in *Testing* kept as-is, **not usable for this build** ✅. Open: R1 retirement in MES. See `ISSUES/ISSUE-002_ESH10000539_R2_BOM_change.md`.
- ESH10000539 stock is in *Testing* location — confirm released for production. ✅ **Revision resolved 2026-05-08:** current rev is **R1**; the "R4" seen on the silkscreen is the legacy `ESH10000023 R4` part number from before the renumber to ESH10000539 — silkscreen artwork was never updated. MES BOM (R1) is correct.

---

## 4. Critical Gaps Summary

| # | Gap | Type | Impact | Action Required |
|---|-----|------|--------|-----------------|
| G-01 | ESH10000182 (Accordion A2 Bare): need 20, have 1 | Inventory | Blocks all 19 remaining units | Initiate build order immediately; check RPi4B stock |
| G-02 | ESH10000634 R3 (Sparrow IDC N-Top): need 20 (system) + 10 (standalone via 636) = 30 assembled | Inventory | Blocks 30 units of ESH10000636 | ⏳ R3 BOM in MES ✅; PCB in-house (98 pcs); **PCBA in internal assembly — ETA 2026-05-22** ✅. Revision pinned to R3 in §1 |
| G-03 | ~~ESH10000544 R3~~ ✅ **CLOSED 2026-05-15** — R3 at Mfg; R1 → EOL; R0 Obsolete; 75 pcs on order | Closed | n/a | Existing 6 R0 pcs Obsolete (not for production) |
| G-04 | ~~ESH10000572 R3~~ ✅ **CLOSED 2026-05-15** — R3 at Mfg; R1 → EOL; R0 Obsolete; 75 pcs on order | Closed | n/a | Existing 7 R0 pcs Obsolete (not for production) |
| G-05 | ESH10000637 (PSU Power Cable): need **40** (20 systems + 20 standalone), have 0 | Inventory | Blocks final assembly + standalone deliverables | Order ≥40 cables (was 20 — doubled by scope expansion 2026-05-12) |
| G-06 | EPN1000677 (USB wall charger): need 20, have 18 | Inventory | 2 units short | Order ≥2 |
| G-07 | ~~Sub-assemblies at Prototype~~ ✅ **CLOSED 2026-05-15** — all promoted to Manufacturing: 540, 535, 543, 536, 534 (2026-05-11), 182 (2026-05-15) | Closed | n/a | — |
| G-08 | ~~ESH10000544 R1 and ESH10000572 R1 — no BOM in MES~~ ✅ **CLOSED 2026-05-11** — both externally built; no MES BOM expected. Supply via procurement | Closed | Procurement orders (see G-03, G-04). R2 may follow — track separately when triggered |
| G-09 | ~~ESH10000634 revision not pinned in ESH10000636 BOM~~ ✅ **CLOSED 2026-05-11** — MES does not store revision pins; revision **R3** is now pinned in §1 of this doc (the authoritative source). Work-order releases must consult §1 to select the correct child revision. | Closed | No MES action — pin maintained here |
| G-10 | ~~ESH10000535 (24), 540 (50), 536 (31) in "Testing" location~~ ✅ **CLOSED 2026-05-15** — all released for production use. ⚠️ 536 margin remains tight (+1 against 30-unit need) — monitor | Closed | n/a | — |
| G-11 | ~~Multiple revisions at Manufacturing~~ ✅ **FULLY CLOSED 2026-05-15** — all single-Mfg violations resolved. **2026-05-15:** ESH10000539 R1 → EOL ✅, ESH10000544 R1 → EOL ✅, ESH10000572 R1 → EOL ✅. **Previously:** ESH10000582 R0.1 → EOL; ESH10000158 R3+R4 → EOL; ESH10000183 R5 → EOL; ESH10000579 rev resolved as R1.0. | Closed | No remaining violations | — |
| G-12 | ~~BOM missing on active Manufacturing revisions~~ ✅ **CLOSED 2026-05-12** — all externally-built items reclassified N/A: **ESH10000158 R5**, **ESH10000183 R6**, **ESH10000522 R5** (target; not yet in MES), **ESH10000544 R3** (target; not yet in MES), **ESH10000572 R3** (target; not yet in MES), **ESH10000615 R0**. **ESH10000634 R3** — ✅ BOM added 2026-05-11. No remaining items | Closed | No MES BOMs expected for any externally-built items |
| G-13 | ESH10000158 R5 procurement — **decision required by 2026-05-27** | Inventory / Decision | If no order placed and R6 sidetrack slips, the 19-piece shortfall blocks the entire ESH10000182 build | **Decide by 2026-05-27:** order ≥19 pcs R5 (externally built) **OR** confirm R6 will be ready in time (sidetrack — Week 4 gate). No order currently in MES |

---

## 5. Production Readiness Checklist

### Gate 1 — Design Release *(target: Week 1–2)*

**Sub-task block A — Promote target revisions to Manufacturing in MES**

- [x] ESH10000540 R3 (Sparrow Fixture Electronics) promoted to Manufacturing in MES ✅ 2026-05-11
- [x] ESH10000535 R3 (Sparrow N-Top) promoted to Manufacturing in MES ✅ 2026-05-11
- [x] ESH10000543 R2 (Fixture Link) promoted to Manufacturing in MES ✅ 2026-05-11
- [x] ESH10000534 R4 (M2Top PoE) promoted to Manufacturing in MES ✅ 2026-05-11 (R1-R3 retired to NotApproved)
- [x] ESH10000536 R2 (M2Top Active Load) promoted to Manufacturing in MES ✅ 2026-05-11
- [x] ESH10000182 R0 (Accordion A2 Bare) promoted to Manufacturing in MES ✅ 2026-05-15 (last Gate 1 Block A promotion)
- [x] ESH10000522 R5 (A2 Back Panel) — R5 created in MES at Manufacturing ✅ 2026-05-15; R0+R1 → EOL ✅. Externally built — no MES BOM expected. Single-Mfg clean.

**Sub-task block B — Single-Manufacturing-revision discipline** *(hard rule: at most one revision per part at Manufacturing; see §1 callout)*

**🔴 Hard-rule violations — must fix:**

- [x] ~~ESH10000158: R3+R4+R5 all at Manufacturing~~ ✅ **RESOLVED 2026-05-11** — R3 and R4 retired to EOL; R5 sole Manufacturing rev.
- [x] ~~ESH10000183: R5+R6 both at Manufacturing~~ ✅ **RESOLVED 2026-05-11** — R5 retired to EOL; R6 confirmed as target and sole Manufacturing rev.
- [x] ~~ESH10000582: R0.1 + R1.0 both at Manufacturing~~ ✅ **RESOLVED 2026-05-12** — R0.1 → EOL; R1.0 sole Manufacturing rev.
- [x] ~~ESH10000539: R1 + R2 both at Manufacturing~~ ✅ **RESOLVED 2026-05-15** — R1 → EOL; R2 sole Manufacturing rev.
- [x] ~~ESH10000544: R1 + R3 both at Manufacturing~~ ✅ **RESOLVED 2026-05-15** — R1 → EOL; R3 sole Manufacturing rev.
- [x] ~~ESH10000572: R1 + R3 both at Manufacturing~~ ✅ **RESOLVED 2026-05-15** — R1 → EOL; R3 sole Manufacturing rev.

**Soft-cleanup items** *(not blocking — informational hygiene)*

- [x] ~~ESH10000579 revision verification~~ ✅ **RESOLVED 2026-05-12** — target rev is **R1.0** (not the suspected R0.3); R1.0 created at Manufacturing in MES. R0.1+R0.2 stay at NotApproved.

**Sub-task block C — Other Gate 1 items**
- [x] ESH10000538 R1 (M2base loopback) — R1 at Manufacturing ✅; **externally built — no MES BOM needed** (2026-05-15); 100 pcs R1 on order ETA 2026-05-29; **15 R0 pcs on hand → scrap** (decided 2026-05-15). Open: does R1 design address ISSUE-001?
- [x] ESH10000062 R1 (PCIe16 riser for AGENT base) — R1 at Manufacturing ✅; **externally built — no MES BOM needed** (confirmed 2026-05-15). 265 R0 pcs on hand — disposition TBC.
- [x] ESH10000544 R3 (A2 Front Panel DSub Fixturelink) — R3 created in MES at Manufacturing ✅ 2026-05-15. R0 → Obsolete. **R1 still at Mfg — retire** (single-Mfg, see block B). Externally built — no MES BOM expected.
- [x] ESH10000572 R3 (Accordion Sparrow Top) — R3 created in MES at Manufacturing ✅ 2026-05-15. R0 → Obsolete. **R1 still at Mfg — retire** (single-Mfg, see block B). Externally built — no MES BOM expected.
- [x] ESH10000579 R1.0 (USB PD 100W PSU PCBA) — created in MES at Manufacturing ✅ 2026-05-12 (target was R1.0, not the suspected R0.3). BOM TBC — confirm in-house vs externally built.
- [x] ESH10000580 R1.0 (USB PD 100W PSU Front Panel) promoted to Manufacturing in MES ✅ 2026-05-12. BOM TBC — externally built likely (panel).
- [x] ESH10000581 R1.0 (USB PD 100W Rear Panel) promoted to Manufacturing in MES ✅ 2026-05-12. BOM TBC — externally built likely (panel).
- [x] ESH10000614 R0 (Sleeved Coax Cable HLCD-20-40.00) promoted to Manufacturing in MES ✅ 2026-05-11
- [x] ESH10000615 R0 (Kontakthuvud HLCD-20-40.00) promoted to Manufacturing in MES ✅ 2026-05-11 — externally built; no MES BOM expected.
- [x] ESH10000634 R3 (Sparrow IDC N-Top): PCB ordered — ETA w/c 2026-05-04
- [x] ESH10000634 R3: PCB in-house ✅ (2026-05-11)
- [x] ESH10000634 R3: created in MES at Manufacturing status ✅ (R1 and R2 now Obsolete)
- [x] ESH10000634 R3: BOM defined in MES ✅ (21 items, 2026-05-11)
- [x] ESH10000634 R3: revision pinned to R3 in §1 of this doc ✅ 2026-05-11 *(MES does not store revision pins; no MES action available)*

**Sub-task block D — Define BOM in MES for active Manufacturing revisions** *(without a BOM, work orders cannot release)*

- [x] ~~ESH10000158 R5~~ — N/A: PCBA built externally, no MES BOM expected. (Procurement of finished PCBA closes the −19 shortfall.)
- [x] ~~ESH10000183 R6~~ — N/A: PCBA built externally, no MES BOM expected. (Still need to decide R5-vs-R6 target and retire the other — see block B.)
- [x] ~~ESH10000522 R5~~ — N/A: externally built, no MES BOM expected. (Still need to create R5 in MES + retire R1 — see block C.)
- [x] ~~ESH10000544 R1, ESH10000572 R1~~ — N/A: externally built, no MES BOM expected (see Gate 1 block C).
- [x] ~~ESH10000615 R0~~ — N/A: externally built, no MES BOM expected.

### Sidetrack — New Sub-Assembly Revisions *(parallel track, not on critical path)*

> **Strategy:** ESH10000158 R6 may run in parallel with the 10-week production programme as a sidetrack. **ESH10000539 R2 is now in MES at Manufacturing** (2026-05-15) — no fallback needed for 539. For 158: if R6 is ready in time it will be incorporated into the ESH10000182 build; if not, R5 (current Manufacturing) will be used. Do not hold production start or ESH10000182 build orders pending R6.

- [x] ✅ **VERIFIED 2026-05-08:** Current revision is **ESH10000539 R1** (MES BOM is correct). The "R4" observed on MJsAgent is the legacy `ESH10000023 R4` part number still printed on the silkscreen — the board was renumbered to ESH10000539 R1 but the silkscreen artwork was never updated. No revision change needed.
- [ ] Confirm what revision the 7 pcs in *Testing* location are (should all be ESH10000539 R1) and whether they are released for production use.
- [ ] ESH10000158 R6 (Accordion A2 Base PCBA): schematic/layout complete
- [ ] ESH10000158 R6: PCB fab ordered
- [ ] ESH10000158 R6: PCBA assembled and verified
- [ ] ESH10000158 R6: promoted to Manufacturing in MES and BOM in ESH10000182 updated
- [x] ESH10000539 R2 (Control Module 32ch A2) — BOM change corrected 2026-05-12 (ISSUE-002): mount R67 (10 kΩ) for DRxD; mount R61 (10 kΩ) for DCTS ✅
- [x] ESH10000539 R2: schematic/BOM updated and approved in MES ✅ 2026-05-12 (BOM 33 items)
- [x] ESH10000539 R2: created in MES at Manufacturing ✅ 2026-05-12 — **retire R1 from Manufacturing** (single-Mfg rule)
- [x] ESH10000539 R2: stock-supply decision ✅ 2026-05-12 — **60 incoming boards mounted as R2 spec** (mount R61, R67); enter stock as R2. *(No new PCB fab needed.)*
- [ ] ESH10000539 R2: PCBA assembled and verified
- [ ] **Decision needed:** rework strategy for the 60 incoming R1 boards (R1 as-is vs. rework to R2 spec) — see ISSUE-002
- [ ] If either new revision is **not** ready by Week 4: decision recorded — fall back to ESH10000158 R5 and ESH10000539 R1 for this production run

### Gate 2 — Inventory Procurement *(target: Week 1–4)*

- [ ] ESH10000182 (Accordion A2 Bare) build order placed (qty ≥ 19); confirm RPi4B 8GB stock for 20 units
- [x] ESH10000634 R3 (Sparrow IDC N-Top) PCB ordered and **received** (98 pcs in-house ✅ 2026-05-11); PCBA assembly to be scheduled
- [ ] ESH10000634 R3 PCBA in internal assembly ✅ 2026-05-12 — **ETA 2026-05-22**
- [ ] ESH10000534 R4 (M2Top PoE) PCBA in internal assembly ✅ 2026-05-12 — **ETA 2026-05-22**
- [ ] ESH10000538 R1 (M2base loopback) — 100 pcs R1 on order (externally built); **ETA 2026-05-29**
- [ ] **ESH10000158 R5 procurement decision — DUE 2026-05-27** (G-13): place order ≥19 pcs **OR** confirm R6 sidetrack will land in time
- [x] ESH10000544 R3 (A2 Front Panel DSub Fixturelink) **procurement order placed ✅ 2026-05-15** — 75 pcs R3 on order (externally built; against R3 spec)
- [x] ESH10000572 R3 (Accordion Sparrow Top) **procurement order placed ✅ 2026-05-15** — 75 pcs R3 on order (externally built; against R3 spec)
- [ ] ESH10000637 (Sparrow PSU Power Cable 1m) cable procurement order placed (qty **≥ 40** — 20 systems + 20 standalone)
- [ ] EPN1000677 (5-port USB wall charger) order placed (qty ≥ 2)
- [x] ESH10000535 (Sparrow N-Top R3) units in Testing released for production ✅ 2026-05-15 (24 pcs, need 20)
- [x] ESH10000540 (Sparrow Fixture Electronics R3) units in Testing released for production ✅ 2026-05-15 (50 pcs, need 20)
- [x] ESH10000536 (Active Load R2) units in Testing released for production ✅ 2026-05-15 (31 pcs, need 30 — ⚠️ +1 margin still tight)

### Gate 3 — Test & Production Infrastructure *(target: Week 2–4)*

- [ ] Production test plan approved (PRODUCTION_TEST_PLAN.md)
- [ ] PRODUCTION_TEST_PROCEDURE.md written and reviewed
- [x] ESH10000654 R0 (Sparrow Test Adapter) assembled and in-house
- [ ] ESH10000654 R0: 4 open interface items resolved (PSU connector, PoE routing — see ESH10000654 R0 SPECIFICATION.md)
- [ ] ESH10000654 R0: verification complete
- [ ] Test software (Accordion automation scripts) ready
- [ ] 20 V DC supply available for Fixture Link eFuse test
- [ ] 56 V DC supply available for PoE test
- [ ] DUT serial number format defined; IDPROM content specified
- [ ] ATmega production firmware version defined and flashed

### Gate 4 — First Article *(target: Week 4–5)*

- [ ] First unit assembled (S/N 001)
- [ ] Full production test executed on S/N 001
- [ ] All PT steps pass or deviations formally recorded
- [ ] First article sign-off by Design Engineer and Quality

### Gate 5 — Production Run *(target: Week 5–9)*

- [ ] All 20 systems assembled (ESH10000633 R1)
- [ ] All 20 systems passed production test
- [ ] Standalone deliverables built/sourced: 10 × ESH10000636, 20 × ESH10000614, 20 × ESH10000637, 20 × EPN1000786 *(scope added 2026-05-12)*
- [ ] DUT log (serial numbers, test results, dates) complete
- [ ] All non-conformances dispositioned

### Gate 6 — Delivery *(target: Week 10, by 2026-07-13)*

- [ ] Final QC inspection passed for all 20 systems and standalone deliverables (10 × 636, 20 × 614, 20 × 637, 20 × EPN1000786)
- [ ] Packaging and labelling complete
- [ ] Delivery documentation complete
- [ ] MES serial number records updated

---

## 6. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| ESH10000182 (Accordion A2 Bare) build lead time > 4 weeks | High | Critical — gates all 19 units | Order immediately; escalate if RPi4B supply constrained |
| ESH10000158 R5 — no procurement order yet placed | High | Critical — without order or R6 falling in on time, ESH10000182 build cannot start | **Decision required by 2026-05-27 (G-13):** place order ≥19 pcs R5 OR confirm R6 sidetrack timing. Externally built — no MES BOM needed. *(Previously closed 2026-05-11 as a BOM-missing concern; re-opened 2026-05-15 because the procurement order itself is still outstanding.)* |
| ESH10000634 R3 (Sparrow IDC N-Top) PCBA assembly delayed | Low | Blocks 30 units of ESH10000636 | PCB in-house (98 pcs); R3 BOM in MES ✅; PCBA in internal assembly ETA 2026-05-22 — monitor delivery |
| ~~ESH10000544 R3 / ESH10000572 R3 procurement~~ ✅ **CLOSED 2026-05-15** — both R3 created in MES; 75 pcs each on order; existing R0 stock confirmed Obsolete (not for production) | Closed | n/a | Outstanding: retire R1 of both in MES (single-Mfg) |
| Testing units ESH10000535 (Sparrow N-Top) / ESH10000540 (Sparrow Fixture Electronics) not released for production | Medium | Blocks sub-assembly supply | Confirm with test team; 4 N-Top spare margin is tight |
| ESH10000654 (Sparrow Test Adapter) verification not complete in time | Medium | Blocks production test execution | TA assembled and in-house; 4 open interface items remain (see ESH10000654 R0 SPECIFICATION.md); verification in progress — monitor weekly |
| Multiple sub-assemblies at Prototype — late MES promotion delays WO creation | Medium | Delays work order release | Assign MES promotion as Week 1 priority |
| ESH10000158 R6 not ready in time | Low–Medium | Minor — fallback to R5 (current Mfg) is available; no production stop | Treat as sidetrack; decide at Week 4 gate; do not delay ESH10000182 build order pending it. *(ESH10000539 R2 closed 2026-05-15 — R2 at Mfg, R1 EOL.)* |
| ~~ESH10000539 revision unclear~~ ✅ **RESOLVED 2026-05-08** — current rev is R1; "R4" on silkscreen is legacy ESH10000023 R4 designator from before the renumber | Closed | No action — MES BOM (R1) is correct | Outstanding: confirm release of 7 pcs in *Testing* location |

---

## Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| R1 | 2026-05-04 | Martin Johansson | Initial document; BOM and inventory extracted from MES 2026-05-04 |
| R1 | 2026-05-04 | Martin Johansson | BOM hierarchy updated with full revision numbers from MES; additional NotApproved sub-components flagged (ESH10000538, 062, 579, 580, 581) |
| R1 | 2026-05-04 | Martin Johansson | Sidetrack section added: ESH10000158 R6 and ESH10000539 new rev planned as parallel track; fallback to R5/R1 if not ready by Week 4 |
| R1 | 2026-05-04 | Martin Johansson | ESH10000634 updated to R3 (hard requirement); R3 not yet in MES — added to critical path in Gate 1 and Gate 2 |
| R1 | 2026-05-04 | Martin Johansson | ESH10000634 R3 status updated: PCB ordered ETA w/c 2026-05-04, PCBA ETA w/c 2026-05-11; risk downgraded to Low |
| R1 | 2026-05-04 | Martin Johansson | Weekly check-in section added |
| R1 | 2026-05-08 | Martin Johansson | Procurement update: 100 pcs ESH10000538 and 60 pcs ESH10000539 R1 on order — both removed from critical-shortage list. ESH10000539 R1→R2 BOM change scoped (4 components: R5, C37, R14, mount C32) — see ISSUE-002. ESH10000538 R0 quality concern logged (ISSUE-001). |
| R1 | 2026-05-11 | Martin Johansson | Gate 1 MES audit: **ESH10000544 R0 and ESH10000572 R0 retired (Obsolete)**; production target rev for both is **R1** (already at Manufacturing in MES, BOM pending — design in progress). §1, §2, §3.2, §4 G-03/G-04/G-08, §5 Gate 1+2, §6 risk register updated. Parent ESH10000631 BOM still references R0 for both — must be updated to R1. |
| R1 | 2026-05-11 | Martin Johansson | ESH10000634 R3 progress: R3 now exists in MES at Manufacturing status (R1, R2 → Obsolete); PCB in-house (98 pcs); **R3 BOM added in MES (21 items)** ✅. **Open:** PCBA assembly to be scheduled; ESH10000636 BOM update to reference R3. §1, §2, §3.3, §4 G-02/G-09, §5 Gate 1+2, §6 risk register updated. |
| R1 | 2026-05-11 | Martin Johansson | ESH10000614 and ESH10000615 promoted to Manufacturing in MES ✅. ESH10000615 BOM still missing — flagged as non-blocker for this run (51 pcs of finished parent 614 in stock); resolve before next 614 build. §1, §2, §5 Gate 1 updated. |
| R1 | 2026-05-11 | Martin Johansson | **MES limitation captured**: MES does not store revision-specific parent-BOM references. Callout added to §1 — this document is now the authoritative revision pin. G-09 closed (no MES action available). All "update parent BOM in MES" tasks reframed accordingly across §2, §4 G-02/G-03/G-04/G-08, §5 Gate 1, §6 risk register. |
| R1 | 2026-05-11 | Martin Johansson | **Single-live-revision discipline** captured in §1 callout as the only MES-side control. Re-audit found 5 parts with multiple active revisions: ESH10000540, 535, 543, 534 (each have 2–3 stale Prototype revisions to retire) and ESH10000579 (R0.1/R0.2 both NotApproved). New gap G-11 added, and Gate 1 split into sub-blocks A (promote target revs), B (retire old revs to EOL), C (other items). |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000579 revision verification flagged**: MES only has R0.1 + R0.2 (both NotApproved); R0.3 suspected to exist outside MES. §1 hierarchy, §4 G-11, §5 Gate 1 blocks B + C updated to capture verification need; cannot decide retire/promote until current rev is confirmed. |
| R1 | 2026-05-11 | Martin Johansson | **Full MES sweep — significant progress + new findings**: Promotions to Manufacturing ✅ — ESH10000540 R3, 535 R3, 543 R2, 536 R2, 522 R1. Older revs of 540/535/543 moved Prototype → NotApproved (acceptable retired state). **🔴 New critical finding:** ESH10000158 R5 has no BOM in MES, and R3+R4+R5 all at Manufacturing — blocks the 19 ESH10000182 builds (CRITICAL PATH). **🔴 New finding:** ESH10000183 R5+R6 both Manufacturing, no BOM (not blocking; 20 pcs stock). New gap G-12 added for BOM-missing on active revs; new risk row; Gate 1 sub-block D added; §1, §2, §3.4, §4 G-07/G-11 updated. |
| R1 | 2026-05-11 | Martin Johansson | **Single-revision rule corrected**: Hard rule is "at most one revision at **Manufacturing** status" (not "exactly one active revision"). Older revisions may be EOL / Obsolete / **NotApproved** — any retired state is acceptable. §1 callout rewritten; G-11 reduced from 6 items to 2 hard violations (ESH10000158, ESH10000183); Gate 1 block B split into hard-rule fixes (158, 183) and soft cleanup (534 future, 579 verify); §2 status notes updated; ESH10000634 R1/R2 "regression" reclassified as non-issue (NotApproved is fine since only R3 is at Manufacturing). |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000534 R4 promoted to Manufacturing** ✅; R1+R2+R3 retired to NotApproved — clean by hard rule. G-07 now only lists ESH10000182; Gate 1 block A and B updated; soft-cleanup line for 534 removed. |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000158 BOM-missing reclassified as N/A**: PCBA is built externally, so no MES BOM is expected — supply is procurement-based, not internal build. §1, §2, §3.4, §4 G-12, §5 Gate 1 block D, §6 risk register updated. The hard-rule violation (R3+R4+R5 all Manufacturing) still stands and is unchanged. |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000183 same as 158** — also externally built PCBA, no MES BOM expected. §1, §2, §4 G-12, §5 Gate 1 block D updated. Hard-rule violation (R5+R6 both Manufacturing) still stands — decide target rev and retire the other. |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000522, ESH10000544, ESH10000572 all externally built — no MES BOM expected.** Each may bump to R2; when R2 lands, retire R1 (single-Mfg rule). §1, §2, §3.2, §4 G-03/G-04/G-08 (closed)/G-12, §5 Gate 1 block C (544/572 closed), block D, Gate 2 (procurement re-framing), §6 risk register updated. |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000544 production target is R3, not R1.** R3 not yet in MES — must be created at Manufacturing status; R1 then retired (single-Mfg rule). R2 apparently skipped. §1, §2, §3.2, §4 G-03, §5 Gate 1 block C (re-opened for 544), Gate 2 (R3 spec), §6 risk register updated. |
| R1 | 2026-05-11 | Martin Johansson | **ESH10000522 production target is R5, not R1.** R5 not yet in MES — must be created at Manufacturing status; R1 then retired (single-Mfg rule). R2–R4 apparently skipped. §1, §2 (removed stale R0 row), §3.2 (R1 stock flagged for R5 usability check), §4 G-12, §5 Gate 1 block C (re-opened for 522), block D updated. |
| R1 | 2026-05-11 | Martin Johansson | **G-11 closed — both hard-rule violations resolved**: ESH10000158 R3+R4 → EOL (R5 sole Mfg ✅); ESH10000183 R5 → EOL (R6 sole Mfg ✅, target confirmed). §1, §2, §3.4, §4 G-11, §5 Gate 1 block B updated. |
| R1 | 2026-05-11 | Martin Johansson | §9 weekly check-in added for 2026-05-12 — captures the week's MES Gate 1 work (9 promotions, 2 hard-rule fixes, 544/522 rev-jump pins, externally-built reclassification, ISSUE-001/002 logged). 6 action points for steering committee with 2026-05-15/05-22 deadlines. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000572 production target is R3, not R1.** R3 not yet in MES — must be created at Manufacturing status; R1 then retired (single-Mfg rule). R2 apparently skipped. §1, §2, §3.2, §4 G-04/G-12, §5 Gate 1 block C (re-opened for 572), Gate 2 (R3 spec), §6 risk register updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000615 reclassified as externally built — no MES BOM expected.** Last remaining BOM-missing item closed; **G-12 closed**. §1, §2, §4 G-12 (closed), §5 Gate 1 block A and D updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000538 and ESH10000062 production target is R1, not R0.** Both in-house builds — R1 must be created in MES at Manufacturing, BOM defined, R0 retired. Existing 538 stock (15 + 100 on order) and 062 stock (265 pcs) are R0 — rev usability needs confirmation. ISSUE-001 ↔ R1 open question: does R1 design address the R0 SPI/loopback intermittency? §1, §3.4 (rows + summary), §5 Gate 1 block C, §9 check-in action point updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000538 R1 and ESH10000062 R1 created in MES at Manufacturing** ✅; R0 stays at NotApproved (single-Mfg rule satisfied for both). BOMs not yet defined — open: confirm in-house vs externally built (drives whether BOMs are required). §1, §3.4 rows + summary, §5 Gate 1 block C updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000582 R1.0 promoted to Manufacturing** ✅ (BOM 6 items). ⚠️ R0.1 still also at Manufacturing — **G-11 re-opened**: retire R0.1 to satisfy single-Mfg rule. §1, §2, §3.1, §4 G-11, §5 Gate 1 block B updated. |
| R1 | 2026-05-12 | Martin Johansson | **USB PD 100W PSU sub-system coordinated R1.0 promotion** ✅: ESH10000582 R0.1 → EOL (G-11 re-closed ✅); ESH10000579 R1.0 created at Manufacturing (target was R1.0 not R0.3 — rev question **resolved**); ESH10000580 R1.0 and ESH10000581 R1.0 promoted to Manufacturing. §1, §2, §3.1, §4 G-11 (closed), §5 Gate 1 blocks B + C updated. BOMs TBC for 579/580/581 — confirm in-house vs externally built. |
| R1 | 2026-05-12 | Martin Johansson | **Delivery scope expanded**: in addition to the original 20 systems, the delivery now also includes 10× ESH10000636, 20× ESH10000614, 20× ESH10000637, 20× EPN1000786 as standalone items. New "Delivery Scope" callout added at top. §3.1 (Need column ×30/40 for affected items), §3.3 (ESH10000636 contents now need ×30 — 536 margin tight at +1), §4 G-05 (cable need doubled to 40), §5 Gate 2 + Gate 5 + Gate 6 + gate-overview table updated. |
| R1 | 2026-05-12 | Martin Johansson | **ISSUE-002 BOM-change spec corrected.** Original 2026-05-08 entry (R5 → 0 Ω; C37 → 330 pF; R14 → 680 Ω; C32 mount) was wrong. Actual R1 → R2 change: mount **R67 (10 kΩ)** for DRxD; mount **R61 (10 kΩ)** for DCTS. Rework path simplified (two SMT components only). §3.4 row + summary, §5 Sidetrack task, STATUS.md Open Issue 8, ISSUE-002 file updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000539 R2 created in MES at Manufacturing** ✅ (BOM 33 items — R61, R67 mount toggled from DNP). ⚠️ R1 still at Manufacturing — **G-11 re-opened** for R1 retirement. §1, §2, §3.4, §4 G-11, §5 Gate 1 block B + Sidetrack section, STATUS.md, ISSUE-002 updated. |
| R1 | 2026-05-12 | Martin Johansson | **Stock-supply decision for ESH10000539** ✅: the 60 incoming boards (on order since 2026-05-08) will be **mounted as R2 spec** — receive directly as R2 stock, no internal rework needed. ISSUE-002 Option B partially closed. Still open: disposition of 7 R1 pcs on hand in *Testing*. §3.4 row + summary, §5 Sidetrack, STATUS.md, ISSUE-002 updated. |
| R1 | 2026-05-12 | Martin Johansson | **7 R1 pcs in *Testing* — kept as-is, NOT usable for this build** ✅ (decision 2026-05-12). Inventory math updated: usable for 19 builds = 60 incoming R2 (gap +41). §3.4 row + summary, STATUS.md, ISSUE-002 updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000634 R3 PCBA now in internal assembly — ETA 2026-05-22**. Gate 1 PCBA-assembly task removed (was duplicate); Gate 2 procurement row updated with assembly status. §1, §3.3, §4 G-02, §5 Gate 1 + Gate 2, §6 risk register updated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000536 Testing-location release added to Gate 2.** MES inventory query: all 31 pcs in *Testing* location (none in regular stock). Very tight against need 30 (only +1 margin). G-10 expanded to include 536; §3.3 row annotated. |
| R1 | 2026-05-12 | Martin Johansson | **ESH10000534 R4 PCBA in internal assembly — ETA 2026-05-22**. §1 hierarchy, §3.2 inventory row, §5 Gate 2 updated. |
| R1 | 2026-05-15 | Martin Johansson | **ESH10000544 R3 created in MES at Manufacturing** ✅; R0 → Obsolete; **75 pcs R3 on order** ✅. Inventory gap closed (+61 spare against need 20). ⚠️ R1 still at Mfg — **G-11 expanded with 544** (R1+R3 both Mfg). §1, §2, §3.2, §4 G-03/G-11, §5 Gate 1 block B + C, Gate 2, §6 risk register updated. |
| R1 | 2026-05-15 | Martin Johansson | **ESH10000572 R3 created in MES at Manufacturing** ✅; R0 → Obsolete; **75 pcs R3 on order** ✅. Inventory gap closed (+62 spare against need 20). ⚠️ R1 still at Mfg — **G-11 expanded with 572** (R1+R3 both Mfg). §1, §2, §3.2, §4 G-04/G-11, §5 Gate 1 block B + C, Gate 2, §6 risk register updated. |
| R1 | 2026-05-15 | Martin Johansson | **ESH10000544 R1 + ESH10000572 R1 → EndOfLife** ✅. Single-Mfg rule now clean for both (R3 sole Manufacturing rev). G-03 and G-04 closed; G-11 reduced to a single remaining violation (ESH10000539 R1). §1, §2, §4 G-03/G-04/G-11, §5 Gate 1 block B updated. |
| R1 | 2026-05-15 | Martin Johansson | **Major Gate 1 milestone — three key closures**: (1) **ESH10000182 R0 promoted to Manufacturing** ✅ — last Gate 1 Block A promotion (G-07 closed). (2) **ESH10000539 R1 → EOL** ✅ — single-Mfg rule violation closed; R2 sole Mfg. (3) **ESH10000522 R5 created at Manufacturing** ✅, R0+R1 → EOL — rev jump complete. **G-11 now FULLY CLOSED** (zero violations). §1, §2, §3.2/§3.4, §4 G-07/G-11, §5 Gate 1 blocks A/B/C, Sidetrack, §6 risk register updated. |
| R1 | 2026-05-15 | Martin Johansson | **ESH10000538 R1 reclassified as externally built — no MES BOM needed**. 100 pcs R1 on order — **ETA 2026-05-29**. Testing-location inventory confirmed 2026-05-15: ESH10000535 (24 pcs), 540 (50 pcs), 536 (31 pcs) — release-for-production confirmation still pending for all three. §1, §3.2, §3.4, §5 Gate 1 block C, Gate 2 updated. |
| R1 | 2026-05-15 | Martin Johansson | **Three quick decisions:** (1) **ESH10000062 R1 reclassified as externally built** — no MES BOM needed. (2) **Testing-location stock released for production** — ESH10000535 (24), 540 (50), 536 (31) all cleared — **G-10 closed**. (3) **15 R0 pcs of ESH10000538 → scrap** (usable supply now = 100 on order only; gap +81 against need 19). §1, §3.2, §3.3, §3.4, §4 G-10, §5 Gate 1 block C + Gate 2 updated. |
| R1 | 2026-05-15 | Martin Johansson | **ESH10000158 R5 procurement decision flagged — DUE 2026-05-27** (G-13 added). No order in MES yet; need 19 pcs; if R6 sidetrack slips, the 19-piece shortfall blocks the entire ESH10000182 build. §3.4 row + summary, new §4 G-13, §5 Gate 2 task, §6 risk register re-opened. |

---

## 8. Weekly Project Check-Ins

> One entry per week. Add a new `### Check-in — YYYY-MM-DD` block each week. Do not edit prior entries.

**Project responsible:** Martin Johansson
**Steering committee:** Daniel Rhodin, Daniel Hansson
**Project:** ESH10000633 R1 — Sparrow Complete Product (20 units, deadline 2026-07-13)

---

### Delivery Plan

| # | Milestone | Description | Deadline | Status |
|---|-----------|-------------|----------|--------|
| 1 | Project start | Production readiness analysis initiated | 2026-05-04 | DONE |
| 2 | Gate 1 — Design Release | All sub-assemblies at Manufacturing in MES; ESH10000634 R3 approved | 2026-05-15 | IN PROGRESS |
| 3 | Gate 2 — Inventory Procurement | All shortfalls resolved; ESH10000182 build order confirmed | 2026-06-05 | NOT STARTED |
| 4 | Gate 3 — Test & Production Infrastructure | Test adapter (ESH10000654) built; test procedure complete; DUT serials defined | 2026-06-05 | NOT STARTED |
| 5 | Gate 4 — First Article | S/N 001 assembled and passed production test | 2026-06-12 | NOT STARTED |
| 6 | Gate 5 — Production Run | All 20 systems assembled and tested + standalone deliverables (10×636, 20×614, 20×637, 20×EPN1000786) built/sourced | 2026-07-06 | NOT STARTED |
| 7 | Gate 6 — Delivery | Final QC, packaging, and delivery documentation complete | 2026-07-13 | NOT STARTED |

---

### Check-in — 2026-05-04

| Last Week | Next Week | Risks & Dependencies |
|-----------|-----------|----------------------|
| Production readiness analysis completed | ESH10000634 R3 PCBA expected (ETA w/c 2026-05-11) | **DEPENDENCY** ESH10000182 (Accordion A2 Bare) — only 1 in stock, need 20; build order not yet placed |
| Full MES BOM extracted (all levels); inventory vs 20-unit need assessed | Verify current revision of ESH10000539 (Control Module 32ch A2) — should it be R1? | **DEPENDENCY** ESH10000654 (Sparrow Test Adapter) — assembled in-house; 4 open interface items remain; verification pending |
| ESH10000634 R3 PCB ordered (ETA this week) | Initiate Gate 1: promote Prototype sub-assemblies to Manufacturing in MES | **RISK** ESH10000544 / ESH10000572 at NotApproved with no BOM — blocks Accordion A2 build |
| PRODUCTION_READINESS.md created with full BOM hierarchy, 6 production gates, and risk register | Confirm ESH10000535 / ESH10000540 units in Testing are cleared for production build | **RISK** I2C issue on PoE / FE N-Top — pending resolution (noted in check-in 2026-04-28) |

**Jira:** *(link TBD)*
**Clockify:** Time estimate: — h / Tracked: — h / Remaining: — h

**Action points for steering committee:**

| Description | Responsible | Deadline |
|-------------|-------------|----------|
| Approve build order for ESH10000182 (Accordion A2 Bare) — qty 19 minimum | Martin Johansson | 2026-05-08 |
| Confirm ESH10000544 / ESH10000572 design approval path and ETA | Martin Johansson | 2026-05-08 |
| Resolve ESH10000654 R0 (Sparrow Test Adapter) open interface items (PSU connector, PoE routing) to unblock PT procedure | Martin Johansson | 2026-05-11 |

**General notes:**
- Overall status: **IN PROGRESS** — production readiness analysis complete; Gate 1 design release actions to begin this week
- I2C issue carried from previous check-in (2026-04-28) — needs resolution before production test can be finalised

---

### Check-in — 2026-05-12

| Last Week | Next Week | Risks & Dependencies |
|-----------|-----------|----------------------|
| PRODUCTION_TEST_PROCEDURE.md draft created (74 steps, 6 TBD); §3.4 ESH10000182 BOM unfolded (4 critical shortages identified) | Promote ESH10000182 R0 to Manufacturing in MES | **DEPENDENCY** ESH10000182 build order still not placed — critical path |
| 100 pcs ESH10000538 + 60 pcs ESH10000539 R1 on order — both removed from critical shortage list | Create **ESH10000544 R3**, **ESH10000572 R3**, **ESH10000522 R5** in MES at Manufacturing; retire R1s | **DEPENDENCY** ESH10000654 R0 (Test Adapter) — 4 open interface items still block PT procedure finalisation |
| Gate 1 MES audit completed; promotions ✅: ESH10000540 R3, 535 R3, 543 R2, 536 R2, 534 R4, 522 R1, 614 R0, 615 R0, 634 R3 | Schedule ESH10000634 R3 PCBA assembly (98 pcs PCB in-house, BOM ✅ 21 items) | **RISK** ISSUE-001 (ESH10000538 R0 / SPI startup intermittency) — investigation pending |
| ESH10000634 R3 PCB in-house (98 pcs); R3 BOM added in MES (21 items); R1+R2 retired | Create ESH10000538 R1 + ESH10000062 R1 in MES, define BOMs; promote ESH10000580 + ESH10000581 in MES; verify ESH10000579 (R0.3 outside MES?) | **RISK** ISSUE-002 (ESH10000539 R1→R2 BOM change) — 60 R1 pcs on order; decision pending on rework vs. as-is |
| ESH10000158 R3+R4 → EOL (R5 sole Mfg); ESH10000183 R5 → EOL (R6 sole Mfg) — hard-rule violations closed | Resolve PRODUCTION_TEST_PROCEDURE.md 6 TBD items (Accordion API, AIN cal, FIXED_LOAD delta, PWM readback, MIC_IN values, serial format) | **RISK** ESH10000544 R3 / ESH10000522 R5 / ESH10000572 R3 — target revs not yet in MES; existing stock may be at wrong rev |
| ESH10000544 R3 / ESH10000522 R5 / ESH10000572 R3 pinned as production targets in §1 (jumping past intermediate revs) | Place procurement orders: ESH10000637 cables (qty ≥20), EPN1000677 USB chargers (qty ≥2), ESH10000158 R5 PCBAs (qty ≥19) | **DEPENDENCY** ESH10000539 *Testing*-location stock release confirmation (7 pcs) |
| MES limitation captured in doc + memory: no BOM revision pins; control = single-Manufacturing-revision discipline | Continue ESH10000582 (USB PD PSU) sub-assembly approval path | |
| Externally-built parts reclassified N/A for MES BOM: 158, 183, 522, 544, 572 | | |

**Jira:** *(link TBD)*
**Clockify:** Time estimate: — h / Tracked: — h / Remaining: — h

**Action points for steering committee:**

| Description | Responsible | Deadline |
|-------------|-------------|----------|
| Place ESH10000182 (Accordion A2 Bare) build order — qty ≥19 | Martin Johansson | 2026-05-15 |
| Decide ESH10000539 R1 stock disposition (use as-is / rework to R2 / hybrid) — see ISSUE-002 | Design lead | 2026-05-15 |
| Resolve ESH10000654 R0 open interface items (PSU connector, PoE routing) | Martin Johansson | 2026-05-15 |
| Create ESH10000544 R3, ESH10000572 R3, ESH10000522 R5, ESH10000538 R1, ESH10000062 R1 in MES (Manufacturing status); define R1 BOMs for 538 and 062 (in-house builds); retire older revs | Martin Johansson | 2026-05-15 |
| Confirm ESH10000539 *Testing*-location stock (7 pcs) is released for production | Martin Johansson | 2026-05-15 |
| Investigate ISSUE-001 (ESH10000538 R0 SPI/loopback intermittency) — measure PCB thickness; document Enable startup sequence | Martin Johansson | 2026-05-22 |

**General notes:**
- Overall status: **IN PROGRESS** — major Gate 1 hygiene progress on 2026-05-11; 9 promotions + 2 hard-rule fixes
- **G-11 (multiple Manufacturing revisions) closed** ✅; **G-08 (544/572 BOM not finalised) closed** ✅; **G-09 (ESH10000634 BOM rev pin) closed** ✅
- ISSUE-001 (loopback/SPI) and ISSUE-002 (ESH10000539 R2 BOM change) logged this week — neither is a Gate 1 blocker
- ESH10000158 R5 BOM-missing risk **closed** — externally built (no MES BOM expected); supply via procurement
- I2C issue carried from 2026-04-28 — still needs resolution before PT can be finalised
