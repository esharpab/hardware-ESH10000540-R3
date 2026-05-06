---
project: ESH10000633
revision: R1
updated: 2026-05-06 (session 15)
---

# Status: Sparrow Complete Product R1

## Current Phase

**Production Test + Production Readiness** (R1) — Production readiness checklist created; 20-unit delivery target 2026-07-13.

---

## Current Focus

- [x] Define system-level requirements in SPECIFICATION.md ✅
- [x] Build PRODUCTION_TEST_PLAN.md ✅ — 38/44 req covered; 6 deferred with rationale
- [x] Production readiness checklist created ✅ — full MES BOM hierarchy, inventory gaps, 6 gates, weekly check-in
- [x] ESH10000182 BOM unfolded in PRODUCTION_READINESS.md §3.4 ✅ (2026-05-06) — 18 sub-components vs need ×19; 4 critical shortages identified
- [x] Build PRODUCTION_TEST_PROCEDURE.md ✅ — Draft created 2026-05-05; 74 steps across 16 sections; 6 TBD items flagged
- [ ] Resolve 6 TBD items in PRODUCTION_TEST_PROCEDURE.md (Accordion API, AIN cal, FIXED_LOAD delta, PWM readback, MIC_IN values, serial format)
- [ ] Resolve Gate 1: promote Prototype sub-assemblies to Manufacturing in MES
- [ ] Resolve Gate 2: ESH10000182 build order; ESH10000544/572 PCB orders
- [ ] Verify ESH10000654 R0 (Test Adapter) — assembled, 4 open interface items remain

---

## Latest Confirmed State

- **SPECIFICATION.md:** ✅ 44 requirements; sub-assembly table updated with two-level MES BOM hierarchy; ESH10000634 added
- **PRODUCTION_TEST_PLAN.md:** ✅ Coverage reviewed; ESH10000634 added to PT-M.00; 8 requirements formally deferred
- **PRODUCTION_TEST_PROCEDURE.md:** ✅ Draft created 2026-05-05 — 74 steps, connector-level structure (J4–J9), Accordion CLI, Active Load, PoE, cosmetics; 6 TBD items flagged
- **ProductionReadiness/PRODUCTION_READINESS.md:** ✅ Created — full BOM hierarchy (all levels), inventory vs 20-unit need, 10 gaps identified, 6-gate checklist, weekly check-in section; **§3.4 added 2026-05-06** — ESH10000182 sub-component inventory (18 rows) showing 4 critical shortages: ESH10000158 (−19), ESH10000539 (−12), ESH10000538 (−4), EPN1000068 (−4)
- **Test Adapter (ESH10000654):** ⚠️ Assembled in-house; 4 open interface items; verification pending
- **ESH10000634 R3:** ⚠️ PCB ordered ETA w/c 2026-05-04; 98 pcs PCBA ordered ETA w/c 2026-05-11
- **DUT:** ⏳ No DUT available yet

---

## Open Issues / Blockers

1. **ESH10000182 (Accordion A2 Bare)** — only 1 in stock, need 20; build order not yet placed — critical path
2. **ESH10000544 / ESH10000572** — NotApproved, no BOM; blocks Accordion A2 build
3. **6 sub-assemblies at Prototype** — ESH10000540, 535, 543, 534, 536, 182 must be promoted to Manufacturing before WOs can be released
4. **ESH10000634 R3** — not yet in MES; must be created, approved, and ESH10000636 BOM updated
5. **ESH10000654 R0** — 4 open interface items (PSU connector, PoE routing) block PRODUCTION_TEST_PROCEDURE.md
6. **ESH10000539 revision** — unverified; confirm R1 is correct before sidetrack planning proceeds

---

## Next 3 Actions

1. **Resolve PRODUCTION_TEST_PROCEDURE.md TBD items** — Accordion API (Open Item 1/3), AIN cal (2), FIXED_LOAD delta (3), PWM readback (4), MIC_IN values (5), serial format (6)
2. **Place build order for ESH10000182** (Accordion A2 Bare) — qty ≥ 19; confirm RPi4B stock
3. **Promote Prototype sub-assemblies to Manufacturing** in MES (Gate 1)

---

## Risks

- ESH10000182 build lead time is the longest critical-path item — order immediately
- ESH10000544 and ESH10000572 at NotApproved with no BOM — design approval path needed
- ESH10000654 R0 verification must complete before production test procedure can be written
