---
project: ESH10000654
revision: R0
updated: 2026-05-04
---

# Design Progress: Sparrow Test Adapter R0

## Milestones

| Milestone | Status | Date | Notes |
|-----------|--------|------|-------|
| Requirements defined | ✅ Done | 2026-05-04 | 21 requirements (MECH/INT/EL/FN); 5 open items remain (PoE/PWR routing, PWR_EN, PD load) |
| Schematic started | ✅ Done | 2026-02-20 | Designed by Martin Trobäck |
| Schematic complete | ✅ Done | 2026-02-20 | Rev 0; PDF in DOCS/ |
| Schematic review | ⏳ Pending | | Not yet scheduled |
| Layout started | ✅ Done | — | Date not recorded |
| Layout complete | ✅ Done | — | Gerbers in DOCS/Sparrow_TA_R0_Gerber_Drill/ |
| Layout review | ⏳ Pending | | Not yet scheduled |
| PCB fabricated | ✅ Done | — | Date not recorded |
| PCBA assembled | ✅ Done | — | Assembled board in-house |
| Design sign-off | ⏳ Pending | | Pending schematic + layout review |
| Verification plan | ⏳ Pending | | Create Verification/VERIFICATION.md |
| Verification complete | ⏳ Pending | | |

---

## Open Design Items

| # | Item | Status |
|---|------|--------|
| 1 | Confirm which PSU connector (P1/P3) routes 20 V vs. Active Load supply vs. 56 V PoE | Open |
| 2 | Confirm PoE 56 V routing — no ETH connector visible in schematic; may be external | Open |
| 3 | Confirm PWR_EN routing — via TA or direct Accordion GPIO? | Open |
| 4 | Confirm Ethernet PD load interface — on TA or external? | Open |
| 5 | Schedule schematic review (Review/SCHEMATIC_REVIEW.md) | Open |
| 6 | Schedule layout review (Review/LAYOUT_REVIEW.md) | Open |
