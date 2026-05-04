---
project: ESH10000535
revision: R3
updated: 2026-05-04 (session 5)
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
- [x] R2 fixes confirmed in R3 (100pF PWM/TACH_VCCO cap; R96/R76 mounted)
- [ ] Assign R3 DUT serial numbers
- [ ] Execute verification tests; record in DUT_LOG.md

---

## Latest Confirmed State

- **Design:** Complete
- **Schematic ERC:** ✅ Signed off 2026-05-04 (MJ) — 8/8 open items closed
- **Layout review:** In progress — 6 pass, 4 info items open (LR-P01, LR-P02, LR-V01, LR-G01)
- **Specification:** ✅ Approved v0.3 — 30 requirements
- **Verification plan:** ✅ Created — 43 tests, 0 executed
- **Verification results:** Not started — awaiting DUT serial numbers

---

## Open Issues / Blockers

- Layout review info items (LR-P01, LR-P02, LR-V01, LR-G01) — pending engineer disposition
- DUT serial numbers not yet assigned

---

## Next 3 Actions

1. **Assign R3 DUT serial numbers** — update DUT register in Verification/DUT_LOG.md
2. **Execute M and P tests** — mechanical and power rails first; record in DUT_LOG.md
3. **Disposition layout review info items** (LR-P01/P02/V01/G01) when ready

---

## Notes for Verification Stage

- **SPI_ENn (D26):** Verify in functional test that SPI_ENn is at the correct logic level before the first SPI transaction. Flagged during schematic ERC 2026-05-04.
