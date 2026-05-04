---
project: ESH10000535
revision: R3
updated: 2026-05-04 (session 6)
---

# Status: Sparrow N-Top R3

## Current Phase

**Verification** (R3) — In progress

---

## Current Focus

- [x] Schematic ERC review signed off 2026-05-04 (MJ)
- [x] Layout review created — 6 pass, 4 info items pending disposition
- [x] SPECIFICATION.md approved (v0.3) — 30 requirements, all Approved 2026-05-04 (MJ)
- [x] VERIFICATION.md created — 43 tests across M / P / CIO / UIO / C sections
- [x] VERIFICATION.md augmented — [R3-CHG] steps added to CIO.01, UIO.00, UIO.01 for R3 design changes
- [x] R2 fixes confirmed in R3 (100pF PWM/TACH_VCCO cap; R96/R76 mounted)
- [ ] Assign R3 DUT serial numbers
- [ ] Execute verification tests; record in DUT_LOG.md

---

## Latest Confirmed State

- **Design:** Complete
- **Schematic ERC:** ✅ Signed off 2026-05-04 (MJ) — 8/8 open items closed
- **Layout review:** In progress — 6 pass, 4 info items open (LR-P01, LR-P02, LR-V01, LR-G01)
- **Specification:** ✅ Approved v0.3 — 30 requirements
- **Verification plan:** ✅ Created and augmented for R3 changes — 43 tests + [R3-CHG] steps, 0 executed
- **Verification results:** Not started — awaiting DUT serial numbers

---

## Open Issues / Blockers

- Layout review info items (LR-P01, LR-P02, LR-V01, LR-G01) — pending engineer disposition
- DUT serial numbers not yet assigned

---

## Next 3 Actions

1. **Assign R3 DUT serial numbers** — update DUT register in Verification/DUT_LOG.md
2. **Calculate expected TACH idle level** — fill in UIO.01 pass criterion from schematic before execution
3. **Execute M and P tests** — mechanical and power rails first; record in DUT_LOG.md

---

## Notes for Verification Stage

- **SPI_ENn (D26):** Verify in functional test that SPI_ENn is at the correct logic level before the first SPI transaction. Flagged during schematic ERC 2026-05-04.
