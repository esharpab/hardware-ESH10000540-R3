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

**Target:** 20 units by 2026-07-13 (10 weeks)
**Source:** MES BOM extracted 2026-05-04. All inventory levels as of that date.

---

## 1. BOM Hierarchy (from MES)

```
ESH10000633 R1 — Sparrow Complete Product (Manufacturing)
│
├── ESH10000631 R1 — Sparrow Accordion A2 (Manufacturing)                    ×1/unit
│   ├── ESH10000182 R0 — Accordion A2 Bare (Prototype) ⚠️                   ×1
│   │   ├── ESH10000158 R5 — Accordion A2 Base PCBA (Manufacturing)          ×1
│   │   ├── ESH10000183 R6 — Accordion A2 Top PCBA (Manufacturing)           ×1
│   │   ├── ESH10000539 R1 — Control Module 32ch A2 (Manufacturing)          ×1
│   │   ├── ESH10000031 R0 — Raspberry Pi 4B 8GB (Manufacturing)             ×1
│   │   ├── ESH10000538 R0 — M2base loopback (NotApproved) 🔴                ×1
│   │   ├── ESH10000062 R0 — PCIe16 riser for AGENT base (NotApproved) 🔴   ×2
│   │   ├── EPN1000012     — Agent Fan 25×10mm 5V (purchased)                ×1
│   │   ├── EPN1000068     — RPI Fan 30×10mm 5V (purchased)                  ×1
│   │   ├── EPN1000072     — SD card 32GB (purchased)                        ×1
│   │   └── (fasteners, Hammond enclosure, misc)
│   ├── ESH10000535 R3 — Sparrow N-Top (Prototype) ⚠️                        ×1
│   ├── ESH10000543 R2 — Fixture Link (Prototype) ⚠️                         ×1
│   ├── ESH10000534 R4 — M2Top PoE (Prototype) ⚠️                            ×1
│   ├── ESH10000544 R0 — A2 Front Panel DSub Fixturelink (NotApproved) 🔴    ×1
│   ├── ESH10000522 R0 — A2 Back Panel (Prototype) ⚠️                        ×1
│   ├── ESH10000572 R0 — Accordion Sparrow Top (NotApproved) 🔴               ×1
│   ├── ESH10000024 R0 — Accordion Loopback R2 (Manufacturing)               ×5
│   └── (fasteners, LED fibres, misc)
│
├── ESH10000636 R1 — Sparrow ASSY FE with Active Load (Manufacturing)         ×1/unit
│   ├── ESH10000540 R3 — Sparrow Fixture Electronics (Prototype) ⚠️           ×1
│   ├── ESH10000634 R3 — Sparrow IDC N-Top (PCB ordered, ETA w/c 2026-05-04; PCBA ETA w/c 2026-05-11) ⚠️ ×1
│   ├── ESH10000536 R2 — M2Top Active Load (Prototype) ⚠️                     ×1
│   └── (connector, fasteners)
│
├── ESH10000582 R0.1 — USB PD 100W PSU (Manufacturing)                        ×1/unit
│   ├── ESH10000579 R0.2 — USB PD 100W PSU PCBA (NotApproved) 🔴              ×1
│   ├── ESH10000580 R0.1 — USB PD 100W PSU Front Panel (NotApproved) 🔴       ×1
│   └── ESH10000581 R0.1 — USB PD 100W Rear Panel (NotApproved) 🔴            ×1
│
├── ESH10000614 R0 — Sleeved Coax Cable HLCD-20-40.00 (Prototype) ⚠️          ×1/unit
│   ├── EPN1000718     — CABLE HLCD-20-40.00-TRS-TLS-4 (purchased)           ×1
│   ├── ESH10000615 R0 — Kontakthuvud HLCD-20-40.00 (Prototype) ⚠️            ×2
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
| ESH10000582 | USB PD 100W PSU | R0.1 | Manufacturing | ✅ | ✅ |
| ESH10000024 | Accordion Loopback R2 | R0 | Manufacturing | — | ✅ |
| ESH10000634 | Sparrow IDC N-Top | R3 | Not in MES | — | ⚠️ PCB ordered, ETA w/c 2026-05-04; PCBA ETA w/c 2026-05-11 — promote to Manufacturing and update ESH10000636 BOM once received |
| ESH10000540 | Sparrow Fixture Electronics | R3 | **Prototype** | ✅ | 🔴 Must be promoted to Manufacturing |
| ESH10000535 | Sparrow N-Top | R3 | **Prototype** | ✅ | 🔴 Must be promoted to Manufacturing |
| ESH10000543 | Fixture Link | R2 | **Prototype** | ✅ | 🔴 Must be promoted to Manufacturing |
| ESH10000534 | M2Top PoE | R4 | **Prototype** | ✅ | 🔴 Must be promoted to Manufacturing |
| ESH10000536 | M2Top Active Load | R2 | **Prototype** | ✅ | 🔴 Must be promoted to Manufacturing |
| ESH10000182 | Accordion A2 Bare | R0 | **Prototype** | ✅ | 🔴 Must be promoted to Manufacturing |
| ESH10000544 | A2 Front Panel DSub | R0 | **NotApproved** | ❌ No BOM | 🔴 Not approved; no BOM defined |
| ESH10000572 | Accordion Sparrow Top | R0 | **NotApproved** | ❌ No BOM | 🔴 Not approved; no BOM defined |
| ESH10000522 | A2 Back Panel | R0 | Prototype | ❌ No BOM | ⚠️ No BOM defined |
| ESH10000614 | Sleeved Coax Cable | R0 | Prototype | ✅ | ⚠️ Must be promoted to Manufacturing |

**Summary: 6 sub-assemblies at Prototype, 2 at NotApproved (no BOM). All must reach Manufacturing status before production start.**

---

## 3. Inventory vs. Requirement (20 units)

> Quantities marked **On Hand** are physically in stock. **Available** = On Hand + Pending (on order).
> Items with no inventory record are assumed to be built-to-order or not yet stocked.

### 3.1 Top-Level BOM Items

| Part | Name | Qty/Unit | Need ×20 | On Hand | Available | Gap | Status |
|------|------|----------|----------|---------|-----------|-----|--------|
| ESH10000631 | Sparrow Accordion A2 | 1 | 20 | — | — | — | Built to order |
| ESH10000636 | Sparrow ASSY FE with Active Load | 1 | 20 | — | — | — | Built to order |
| ESH10000582 | USB PD 100W PSU | 1 | 20 | 32 | 32 | +12 | ✅ |
| ESH10000614 | Sleeved Coax Cable | 1 | 20 | 51 | 51 | +31 | ✅ |
| ESH10000637 | Sparrow PSU Power Cable 1m | 1 | 20 | 0 | 0 | **−20** | 🔴 Order required |
| EPN1000677 | 5-port USB wall charger | 1 | 20 | 18 | 18 | **−2** | 🔴 Order 2+ |
| EPN1000678 | 100W USB-C cable | 1 | 20 | 84 | 84 | +64 | ✅ |
| EPN1000786 | D-Sub cable 1m | 1 | 20 | 50 | 50 | +30 | ✅ |
| EPN1000752 | M3 standoffs 8.6mm | 5 | 100 | 213 | 213 | +113 | ✅ |

### 3.2 ESH10000631 — Sparrow Accordion A2 (contents, ×1 per unit)

| Part | Name | Qty/Unit | Need ×20 | On Hand | Available | Gap | Status |
|------|------|----------|----------|---------|-----------|-----|--------|
| ESH10000182 | Accordion A2 Bare | 1 | 20 | 1 | 1 | **−19** | 🔴 Critical shortage |
| ESH10000535 | Sparrow N-Top R3 | 1 | 20 | 24 | 24 | +4 | ⚠️ In Testing — confirm cleared for production |
| ESH10000543 | Fixture Link R2 | 1 | 20 | 48 | 48 | +28 | ✅ |
| ESH10000534 | M2Top PoE R4 | 1 | 20 | 15 | 39 | +19 | ✅ (24 on order) |
| ESH10000544 | A2 Front Panel DSub | 1 | 20 | 6 | 6 | **−14** | 🔴 Critical shortage |
| ESH10000522 | A2 Back Panel | 1 | 20 | 26 | 26 | +6 | ✅ |
| ESH10000572 | Accordion Sparrow Top | 1 | 20 | 7 | 7 | **−13** | 🔴 Critical shortage |
| ESH10000024 | Accordion Loopback R2 | 5 | 100 | 751 | 751 | +651 | ✅ |

### 3.3 ESH10000636 — Sparrow ASSY FE with Active Load (contents, ×1 per unit)

| Part | Name | Qty/Unit | Need ×20 | On Hand | Available | Gap | Status |
|------|------|----------|----------|---------|-----------|-----|--------|
| ESH10000540 | Sparrow Fixture Electronics R3 | 1 | 20 | 50 | 50 | +30 | ⚠️ In Testing — confirm cleared for production |
| ESH10000634 | Sparrow IDC N-Top R3 | 1 | 20 | 0 | 98 | +78 | ⏳ 98 pcs on order, ETA w/c 2026-05-11 |
| ESH10000536 | M2Top Active Load R2 | 1 | 20 | 31 | 31 | +11 | ✅ |

---

## 4. Critical Gaps Summary

| # | Gap | Type | Impact | Action Required |
|---|-----|------|--------|-----------------|
| G-01 | ESH10000182 (Accordion A2 Bare): need 20, have 1 | Inventory | Blocks all 19 remaining units | Initiate build order immediately; check RPi4B stock |
| G-02 | ESH10000634 R3 (Sparrow IDC N-Top): need 20, have 0 at R3 | Design + Inventory | Blocks all 20 units of ESH10000636 | ⏳ In progress — PCB ordered ETA w/c 2026-05-04; 98 pcs PCBA ordered ETA w/c 2026-05-11; promote to Manufacturing and update ESH10000636 BOM on receipt |
| G-03 | ESH10000544 (A2 Front Panel DSub): need 20, have 6 | Inventory | Blocks 14 units of ESH10000631 | PCB order + assembly; currently NotApproved |
| G-04 | ESH10000572 (Accordion Sparrow Top): need 20, have 7 | Inventory | Blocks 13 units of ESH10000631 | PCB order + assembly; currently NotApproved |
| G-05 | ESH10000637 (PSU Power Cable): need 20, have 0 | Inventory | Blocks final assembly of all 20 units | Order cables |
| G-06 | EPN1000677 (USB wall charger): need 20, have 18 | Inventory | 2 units short | Order ≥2 |
| G-07 | ESH10000540, 535, 543, 534, 536, 182 at Prototype status | Design | Cannot formally release to production | Promote all 6 to Manufacturing in MES |
| G-08 | ESH10000544 and ESH10000572 at NotApproved, no BOM | Design | Cannot build Accordion A2 at production standard | Define BOM and approve in MES |
| G-09 | ESH10000634 revision not pinned in ESH10000636 BOM | Design | Ambiguous build spec (R1 or R2?) | Pin revision in MES BOM |
| G-10 | ESH10000535 (24 units) and ESH10000540 (50 units) are in "Testing" location | Inventory | May be committed to R3 verification | Confirm units are cleared for production build |

---

## 5. Production Readiness Checklist

### Gate 1 — Design Release *(target: Week 1–2)*

- [ ] ESH10000540 R3 (Sparrow Fixture Electronics) promoted to Manufacturing in MES
- [ ] ESH10000535 R3 (Sparrow N-Top) promoted to Manufacturing in MES
- [ ] ESH10000543 R2 (Fixture Link) promoted to Manufacturing in MES
- [ ] ESH10000534 R4 (M2Top PoE) promoted to Manufacturing in MES
- [ ] ESH10000536 R2 (M2Top Active Load) promoted to Manufacturing in MES
- [ ] ESH10000182 R0 (Accordion A2 Bare) promoted to Manufacturing in MES
- [ ] ESH10000538 R0 (M2base loopback) approved and promoted to Manufacturing in MES
- [ ] ESH10000062 R0 (PCIe16 riser for AGENT base) approved and promoted to Manufacturing in MES
- [ ] ESH10000544 R0 (A2 Front Panel DSub Fixturelink) BOM defined, approved, promoted to Manufacturing
- [ ] ESH10000572 R0 (Accordion Sparrow Top) BOM defined, approved, promoted to Manufacturing
- [ ] ESH10000579 R0.2 (USB PD 100W PSU PCBA) approved and promoted to Manufacturing in MES
- [ ] ESH10000580 R0.1 (USB PD 100W PSU Front Panel) approved and promoted to Manufacturing in MES
- [ ] ESH10000581 R0.1 (USB PD 100W Rear Panel) approved and promoted to Manufacturing in MES
- [ ] ESH10000614 R0 (Sleeved Coax Cable HLCD-20-40.00) promoted to Manufacturing in MES
- [ ] ESH10000615 R0 (Kontakthuvud HLCD-20-40.00) promoted to Manufacturing in MES
- [x] ESH10000634 R3 (Sparrow IDC N-Top): PCB ordered — ETA w/c 2026-05-04
- [ ] ESH10000634 R3: PCBA assembled — ETA w/c 2026-05-11
- [ ] ESH10000634 R3: create R3 in MES, verify, promote to Manufacturing
- [ ] ESH10000634 R3: update ESH10000636 BOM to reference R3

### Sidetrack — New Sub-Assembly Revisions *(parallel track, not on critical path)*

> **Strategy:** New revisions of ESH10000158 and ESH10000539 are planned to run in parallel with the 10-week production programme. If the new revisions are ready in time, they will be incorporated into the ESH10000182 (Accordion A2 Bare) build. If not, the current approved revisions (ESH10000158 R5 / ESH10000539 R1 — **verify**) will be used. Do not hold production start or ESH10000182 build orders pending these revisions.

- [ ] **⚠️ VERIFY:** Confirm current production revision of ESH10000539 (Control Module 32ch A2) — MES shows R1; is this correct?
- [ ] ESH10000158 R6 (Accordion A2 Base PCBA): schematic/layout complete
- [ ] ESH10000158 R6: PCB fab ordered
- [ ] ESH10000158 R6: PCBA assembled and verified
- [ ] ESH10000158 R6: promoted to Manufacturing in MES and BOM in ESH10000182 updated
- [ ] ESH10000539 new rev (Accordion A2 Base PCBA — Control Module 32ch A2): revision confirmed and design started
- [ ] ESH10000539 new rev: PCB fab ordered
- [ ] ESH10000539 new rev: PCBA assembled and verified
- [ ] ESH10000539 new rev: promoted to Manufacturing in MES and BOM in ESH10000182 updated
- [ ] If either new revision is **not** ready by Week 4: decision recorded — fall back to ESH10000158 R5 and ESH10000539 R1 for this production run

### Gate 2 — Inventory Procurement *(target: Week 1–4)*

- [ ] ESH10000182 (Accordion A2 Bare) build order placed (qty ≥ 19); confirm RPi4B 8GB stock for 20 units
- [x] ESH10000634 R3 (Sparrow IDC N-Top) PCB ordered (ETA w/c 2026-05-04); 98 pcs PCBA ordered, ETA w/c 2026-05-11
- [ ] ESH10000544 (A2 Front Panel DSub Fixturelink) PCB order placed (qty ≥ 14) — pending design approval
- [ ] ESH10000572 (Accordion Sparrow Top) PCB order placed (qty ≥ 13) — pending design approval
- [ ] ESH10000637 (Sparrow PSU Power Cable 1m) cable procurement order placed (qty ≥ 20)
- [ ] EPN1000677 (5-port USB wall charger) order placed (qty ≥ 2)
- [ ] ESH10000535 (Sparrow N-Top R3) units in Testing confirmed available for production (24 available, need 20)
- [ ] ESH10000540 (Sparrow Fixture Electronics R3) units in Testing confirmed available for production (50 available, need 20)

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

- [ ] All 20 units assembled
- [ ] All 20 units passed production test
- [ ] DUT log (serial numbers, test results, dates) complete
- [ ] All non-conformances dispositioned

### Gate 6 — Delivery *(target: Week 10, by 2026-07-13)*

- [ ] Final QC inspection passed for all 20 units
- [ ] Packaging and labelling complete
- [ ] Delivery documentation complete
- [ ] MES serial number records updated

---

## 6. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| ESH10000182 (Accordion A2 Bare) build lead time > 4 weeks | High | Critical — gates all 19 units | Order immediately; escalate if RPi4B supply constrained |
| ESH10000634 R3 (Sparrow IDC N-Top) PCBA delayed beyond w/c 2026-05-11 | Low | Blocks all 20 units of ESH10000636 | PCB already ordered; PCBA ETA w/c 2026-05-11 — monitor delivery |
| ESH10000544 (A2 Front Panel DSub) / ESH10000572 (Accordion Sparrow Top) design not approved in time | Medium | Blocks Accordion A2 build | Expedite design review; check if existing stock can be reworked |
| Testing units ESH10000535 (Sparrow N-Top) / ESH10000540 (Sparrow Fixture Electronics) not released for production | Medium | Blocks sub-assembly supply | Confirm with test team; 4 N-Top spare margin is tight |
| ESH10000654 (Sparrow Test Adapter) verification not complete in time | Medium | Blocks production test execution | TA assembled and in-house; 4 open interface items remain (see ESH10000654 R0 SPECIFICATION.md); verification in progress — monitor weekly |
| Multiple sub-assemblies at Prototype — late MES promotion delays WO creation | Medium | Delays work order release | Assign MES promotion as Week 1 priority |
| ESH10000158 R6 / ESH10000539 new rev not ready in time | Low–Medium | Minor — fallback to R5/R1 is available; no production stop | Treat as sidetrack; decide at Week 4 gate; do not delay ESH10000182 build order pending these |
| ESH10000539 revision unclear — may not be R1 | Medium | Wrong revision built into ESH10000182 if unverified | Verify immediately (Gate 1 sidetrack action) |

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
| 6 | Gate 5 — Production Run | All 20 units assembled and tested | 2026-07-06 | NOT STARTED |
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
