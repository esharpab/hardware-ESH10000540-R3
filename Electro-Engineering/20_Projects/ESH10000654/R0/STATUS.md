---
project: ESH10000654
revision: R0
updated: 2026-05-04 (session 2)
---

# Status: Sparrow Test Adapter R0

## Current Phase

**Verification pending** — Assembled board is in-house. Requirements defined. Schematic and layout review not yet done.

---

## Current Focus

- [ ] Resolve 4 open interface questions (PoE routing, PWR_EN, PD load, PSU connector assignment)
- [ ] Schedule schematic review (Review/SCHEMATIC_REVIEW.md)
- [ ] Schedule layout review (Review/LAYOUT_REVIEW.md)
- [ ] Create Verification/VERIFICATION.md with functional verification plan

---

## Latest Confirmed State

| Item | Status | Notes |
|------|--------|-------|
| Requirements | ✅ Defined | 21 req (MECH/INT/EL/FN); 5 open items |
| Schematic | ✅ Complete | Rev 0, Martin Trobäck, 2026-02-20; PDF in DOCS/ |
| Layout | ✅ Complete | Gerbers in DOCS/Sparrow_TA_R0_Gerber_Drill/ |
| PCB fabricated | ✅ Done | — |
| PCBA assembled | ✅ In-house | Available for verification |
| Schematic review | ⏳ Not started | — |
| Layout review | ⏳ Not started | — |
| Verification | ⏳ Not started | Plan not yet created |
| Design sign-off | ⏳ Not started | Pending reviews |

---

## Open Issues / Blockers

| # | Issue | Impact |
|---|-------|--------|
| 1 | PoE 56 V routing unclear — no ETH connector visible in schematic | May affect PT-POE requirement coverage |
| 2 | PSU connector assignment (P1 vs P3) not confirmed for each supply voltage | Required before writing PT procedure |
| 3 | PWR_EN routing — via TA or direct? | Affects PT-PWR.01 procedure |
| 4 | Ethernet PD load — on TA or external? | Affects PT-POE.01/.03 setup |

---

## Next 3 Actions

1. **Resolve open items 1–4** — confirm with Martin Trobäck or review schematic in detail
2. **Schematic review** — open Review/SCHEMATIC_REVIEW.md, perform structured ERC review against SPECIFICATION.md
3. **Create Verification/VERIFICATION.md** — derive verification test cases from SPECIFICATION.md requirements

---

## Risks

- *Open interface questions* — items 1–4 must be resolved before the production test procedure (ESH10000633) can be completed
- *No schematic/layout review on record* — assembled board was built prior to formal review; review should be done before verification sign-off
