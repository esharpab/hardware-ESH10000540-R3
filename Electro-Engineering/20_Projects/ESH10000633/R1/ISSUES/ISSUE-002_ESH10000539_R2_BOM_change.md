---
issue_id: ISSUE-002
project: ESH10000633 R1
component: ESH10000539 — Control Module 32ch A2
status: Open — design change pending
opened: 2026-05-08
type: BOM change / revision bump R1 → R2
---

# ISSUE-002 — ESH10000539 R1 → R2 BOM change

## Summary

ESH10000539 R1 (Control Module 32ch A2) must be updated to **R2** with four component changes to the BOM. Logged 2026-05-08.

## BOM changes (R1 → R2)

| Reference | Change | Notes |
|-----------|--------|-------|
| **R5** | → 0 Ω | Resistor value change |
| **C37** | → 330 pF | Capacitor value change |
| **R14** | → 680 Ω | Resistor value change |
| **C32** | **mount** EGP10001337 (22 µF 100 V) | Previously DNP; now populated |

## Current procurement state

- **60 pcs ESH10000539 R1 on order** (PO placed 2026-05-08).
- 7 pcs R1 on hand in *Testing* location (release-for-production confirmation pending).
- Total available R1 = 67 pcs against 19-build need for ESH10000182 (gap +48).

## Open question — strategy for incoming R1 stock

The 60 pcs on order are R1, not R2. Before they arrive a decision is needed:

- [ ] **Option A — Use R1 as-is.** Build the current production run (20 units) on R1; introduce R2 for the next production run. Requires the design team to confirm R1 is functionally acceptable.
- [ ] **Option B — Rework R1 boards to R2 spec.** All 60 incoming pcs (and the 7 on hand) reworked: swap R5, C37, R14; mount C32. Estimate rework cost vs. new fab; document rework instructions.
- [ ] **Option C — Hybrid.** Use R1 as-is for early units, rework or new-fab R2 for later units. Define cutoff.

Decision owner: design lead. Required by: before incoming R1 stock arrives, otherwise the units will be put into stock as R1 by default.

## Implementation tasks

- [ ] Schematic and BOM updated (R5, C37, R14, C32) and reviewed
- [ ] R2 created in MES with new BOM; old R1 BOM preserved (immutable)
- [ ] Decision recorded for the 60 pcs R1 on order (Option A / B / C above)
- [ ] If Option B/C: rework instructions documented; rework executed and verified
- [ ] If new fab needed: PCB fab order placed and tracked
- [ ] R2 promoted to Manufacturing in MES
- [ ] BOM in ESH10000182 (Accordion A2 Bare) updated to reference R2

## Linked artifacts

- `PRODUCTION_READINESS.md` §3.4 — inventory row
- `PRODUCTION_READINESS.md` §5 Sidetrack — task list
- `STATUS.md` — open item

## Notes

- R1 is the verified baseline (silkscreen-vs-MES discrepancy resolved 2026-05-08 — see project history); the R2 changes are deliberate component-value updates, not a renumber.
- Sub-assembly verification of R2 belongs in an ESH10000539 sub-project. This issue tracks the project-level impact only (BOM rollup, build planning, stock disposition).
