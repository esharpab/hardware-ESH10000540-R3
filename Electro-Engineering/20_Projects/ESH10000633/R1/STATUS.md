---
project: ESH10000633
revision: R1
updated: 2026-05-15 (session 18)
---

# Status: Sparrow Complete Product R1

## Current Phase

**Production Test + Production Readiness** (R1). Gate 1 design release substantially complete (2026-05-11/12 audit); critical-path procurement and ESH10000182 build still open. Delivery target 2026-07-13 — **scope expanded 2026-05-12** to include standalone items (10× 636, 20× 614, 20× 637, 20× EPN1000786) in addition to 20 systems.

---

## Current Focus

- [x] SPECIFICATION.md ✅
- [x] PRODUCTION_TEST_PLAN.md ✅ (38/44 req covered; 6 deferred)
- [x] PRODUCTION_TEST_PROCEDURE.md ✅ (74 steps; 6 TBD items)
- [x] PRODUCTION_READINESS.md ✅ (full BOM hierarchy, 6 gates, weekly check-ins)
- [x] Gate 1 MES audit ✅ 2026-05-11/12 — 9 promotions, 2 hard-rule violations closed, single-Mfg discipline applied
- [x] ESH10000539 R2 created in MES ✅; 60 incoming R1 pcs decided to be mounted as R2 spec
- [x] USB PD PSU sub-system R1.0 rollout ✅ (582, 579, 580, 581)
- [x] ESH10000158 / ESH10000183 / 522 / 544 / 572 / 615 reclassified as externally built (no MES BOM expected)
- [ ] **Resolve 6 TBD items in PRODUCTION_TEST_PROCEDURE.md** (Accordion API, AIN cal, FIXED_LOAD delta, PWM readback, MIC_IN values, serial format)
- [ ] **Place ESH10000182 build order** (qty ≥ 19) — critical path
- [ ] **Place ESH10000637 cable procurement order** (qty ≥ 40 — doubled by scope expansion)
- [x] **ESH10000539 R1 → EOL** ✅ 2026-05-15 (single-Mfg clean; ISSUE-002 closed)
- [x] ESH10000544 R3 created in MES + R1 → EOL ✅ 2026-05-15 (75 pcs R3 on order; single-Mfg clean)
- [x] ESH10000572 R3 created in MES + R1 → EOL ✅ 2026-05-15 (75 pcs R3 on order; single-Mfg clean)
- [x] **ESH10000522 R5 created in MES** + R0+R1 → EOL ✅ 2026-05-15 (single-Mfg clean)
- [x] **ESH10000182 R0 promoted to Manufacturing** ✅ 2026-05-15 (last Gate 1 Block A promotion)
- [x] ESH10000538 R1 — externally built ✅ 2026-05-15 (no MES BOM needed; 100 pcs on order ETA 2026-05-29)
- [x] ESH10000062 R1 — externally built ✅ 2026-05-15 (no MES BOM needed; 265 R0 pcs on hand — disposition TBC)
- [x] Testing-location stock released for production ✅ 2026-05-15 — ESH10000535 (24), 540 (50), 536 (31 — ⚠️ +1 margin still tight)
- [ ] Track ESH10000634 R3 + ESH10000534 R4 PCBA internal assembly (ETA 2026-05-22)
- [ ] Resolve ESH10000654 R0 4 open interface items (PSU connector, PoE routing, PWR_EN, PD load) — unblocks PT procedure

---

## Latest Confirmed State

- **SPECIFICATION.md:** ✅ 44 requirements (8 formally deferred)
- **PRODUCTION_TEST_PLAN.md:** ✅ Coverage reviewed; ESH10000634 added to PT-M.00
- **PRODUCTION_TEST_PROCEDURE.md:** ✅ Draft (74 steps, 6 TBD items flagged)
- **PRODUCTION_READINESS.md:** ✅ Updated continuously — see its §revision history for full ledger. Most recent: 2026-05-12 — ESH10000634/534 R4 PCBA assembly status, ESH10000536 Testing-location flag (+1 margin), delivery scope expansion
- **Gate 1 Block A (promotions):** ✅ **COMPLETE** — all 10 sub-assemblies at Manufacturing (182 promoted 2026-05-15)
- **Gate 1 Block B (single-Mfg rule):** ✅ **COMPLETE** — zero remaining violations (539/544/572 R1 all → EOL 2026-05-15)
- **Gate 1 Block C (NotApproved + rev jumps):** ✅ all rev creates done (522 R5, 544 R3, 572 R3 in MES; 579/580/581 R1.0 promoted; 538/062 R1 Mfg — BOM TBC remaining)
- **Gate 1 Block D (BOM-missing on Mfg revs):** ✅ closed (all externally-built items reclassified N/A; 634 R3 BOM added)
- **ESH10000634 R3:** Manufacturing + BOM 21 items ✅; PCB in-house (98 pcs); PCBA in internal assembly — ETA 2026-05-22
- **ESH10000534 R4:** Manufacturing ✅; PCBA in internal assembly (24 pcs in process) — ETA 2026-05-22
- **ESH10000539:** ✅ R2 sole Manufacturing rev (R0+R1 EOL 2026-05-15); 60 incoming boards mounted as R2; 7 R1 in *Testing* kept as-is (not for this build); ISSUE-002 closed
- **ESH10000654 R0 (Test Adapter):** VERIFICATION.md created 2026-05-15 (33 test cases, 22/22 SPEC req covered); DUT_LOG.md created — DUT-01 = S/N P0 with 2 rail patches + R48 fitted; verification execution not yet started
- **DUT (Sparrow system):** ⏳ none assembled yet

---

## Open Issues / Blockers

1. **ESH10000182 (Accordion A2 Bare)** — only 1 in stock, need 19 fresh builds; **build order still not placed** — critical path
1a. **ESH10000158 R5 procurement — DECISION DUE 2026-05-27** (G-13) — no order in MES yet; need 19 pcs; if R6 sidetrack slips, this blocks the entire ESH10000182 build
2. **ESH10000637 cable** — need 40 (system + standalone), 0 on hand — order doubled by scope expansion
3. ~~ESH10000182 R0 promotion~~ ✅ DONE 2026-05-15 (Gate 1 Block A complete)
4. ~~ESH10000539 R1 retirement~~ ✅ DONE 2026-05-15 (R1 → EOL; ISSUE-002 closed)
5. ~~ESH10000522 R5 / 544 R3 / 572 R3 rev jumps~~ ✅ ALL DONE 2026-05-15 (single-Mfg clean for all three)
6. **Six TBD items in PRODUCTION_TEST_PROCEDURE.md** — Accordion API, AIN cal, FIXED_LOAD delta, PWM readback, MIC_IN values, serial format
7. **ESH10000654 R0** — 4 open interface items (PSU connector, PoE routing, PWR_EN, PD load) block production test procedure finalisation
8. **ESH10000536 Active Load** — only +1 spare (31 released from Testing 2026-05-15 vs need 30 incl. standalone); margin remains tight
9. **ISSUE-001** — ESH10000538 R0 SPI/loopback intermittency. Open question whether the new ESH10000538 R1 design addresses it. See `ISSUES/ISSUE-001_M2base_loopback_SPI_intermittent.md`
10. ~~ISSUE-002~~ ✅ **CLOSED 2026-05-15** — ESH10000539 R2 BOM change fully done (R2 at Mfg, R1 EOL, 60 incoming mounted as R2, 7 R1 in *Testing* set aside). See `ISSUES/ISSUE-002_ESH10000539_R2_BOM_change.md`

---

## Next 3 Actions

1. **ESH10000158 R5 procurement decision — DUE 2026-05-27** (G-13): order ≥19 pcs OR confirm R6 sidetrack timing
2. **Place ESH10000182 build order** (qty ≥ 19) — critical path, longest lead time
3. **Place ESH10000637 cable procurement order** (qty ≥ 40 — doubled by scope expansion)

---

## Risks

- ESH10000158 R5 procurement decision is a hard 2026-05-27 deadline — slipping it risks blocking the ESH10000182 build outright
- ESH10000182 build lead time is the longest critical-path item — order immediately
- ESH10000536 stock is tight (+1 margin) — if any unit committed to verification, build shortfalls
- ESH10000634 R3 / ESH10000534 R4 PCBA delivery 2026-05-22 — monitor; coordinated milestone
- ESH10000654 R0 verification must complete before production test procedure can be finalised (4 open interface items still pending)
- ISSUE-001 SPI intermittency unresolved — may surface in production test if the new R1 design doesn't address it
