---
issue_id: ISSUE-002
project: ESH10000633 R1
component: ESH10000539 — Control Module 32ch A2
status: Open — R2 created in MES 2026-05-12; 60 incoming → R2 spec (decided 2026-05-12); 7 R1 pcs in Testing kept as-is, not for this build (decided 2026-05-12); R1 retirement in MES pending
opened: 2026-05-08
type: BOM change / revision bump R1 → R2
---

# ISSUE-002 — ESH10000539 R1 → R2 BOM change

## Summary

ESH10000539 R1 (Control Module 32ch A2) must be updated to **R2** with two component-mount changes to the BOM. Logged 2026-05-08; **spec corrected 2026-05-12** (previously-recorded component list was wrong — see "Correction" note below).

## BOM changes (R1 → R2)

| Reference | Change | Function |
|-----------|--------|----------|
| **R67** | **mount** 10 kΩ | Pull-up/-down for **DRxD** |
| **R61** | **mount** 10 kΩ | Pull-up/-down for **DCTS** |

Both resistors were previously DNP (Do-Not-Populate) on R1. R2 adds them to the BOM and they must be mounted in build.

## Correction note (2026-05-12)

The original 2026-05-08 entry incorrectly listed the BOM changes as: R5 → 0 Ω; C37 → 330 pF; R14 → 680 Ω; C32 → mount EGP10001337 (22 µF 100 V). That list was wrong. The correct R1 → R2 change is the two pull-up mounts on R61 and R67 above. The earlier procurement entries that referenced the wrong components have been updated in PRODUCTION_READINESS.md and STATUS.md.

## Current procurement state

- **60 pcs ESH10000539 R1 on order** (PO placed 2026-05-08).
- 7 pcs R1 on hand in *Testing* location (release-for-production confirmation pending).
- Total available R1 = 67 pcs against 19-build need for ESH10000182 (gap +48).

## Stock-disposition decision (2026-05-12)

✅ **DECISION:** The **60 incoming boards will be mounted to R2 spec** (mount R61 10 kΩ + R67 10 kΩ). They will enter stock as ESH10000539 R2, not R1.

- [x] ~~Option A — Use R1 as-is.~~ Not selected for the 60 incoming.
- [x] ✅ **Option B (partial — 60 incoming)** — The 60 boards in the incoming PO will be mounted as R2 spec.
- [x] ✅ **7 R1 pcs in *Testing*** — kept as R1 as-is, **not usable for this build** (decided 2026-05-12). Retained for other purposes (re-work / dev / spares).

### Net impact on production supply

With the 7 R1 boards excluded from this build, usable stock for the 19 builds of ESH10000182 comes from the 60 incoming R2 pcs: **60 vs need 19 → +41 spare** ✅ still comfortable.

## Implementation tasks

- [x] Schematic and BOM updated (mount R61 10 kΩ, mount R67 10 kΩ) and reviewed ✅
- [x] R2 created in MES with new BOM (33 items); old R1 BOM preserved ✅ 2026-05-12
- [x] R2 promoted to Manufacturing in MES ✅ 2026-05-12
- [ ] **Retire R1 from Manufacturing in MES** (single-Mfg rule — currently both R1 and R2 at Mfg)
- [x] Decision recorded for the 60 pcs on order ✅ 2026-05-12 — mount as R2 spec
- [ ] Confirm with supplier/assembly that the 60 pcs are mounted with R61 + R67 (10 kΩ each) before PCBA completion; receive as R2 stock
- [x] Disposition decision for the 7 R1 pcs on hand in *Testing* location ✅ 2026-05-12 — kept as-is, not for this build
- [ ] *(Rework instructions not needed for this build — no internal rework planned.)*
- [ ] If new fab needed: PCB fab order placed and tracked
- [ ] *(MES BOM in ESH10000182 — no action: MES doesn't store revision pins; target rev R2 pinned in PRODUCTION_READINESS.md §1)*

## Linked artifacts

- `PRODUCTION_READINESS.md` §3.4 — inventory row
- `PRODUCTION_READINESS.md` §5 Sidetrack — task list
- `STATUS.md` — open item

## Notes

- R1 is the verified baseline (silkscreen-vs-MES discrepancy resolved 2026-05-08 — see project history); the R2 changes are deliberate component-value updates, not a renumber.
- Sub-assembly verification of R2 belongs in an ESH10000539 sub-project. This issue tracks the project-level impact only (BOM rollup, build planning, stock disposition).
