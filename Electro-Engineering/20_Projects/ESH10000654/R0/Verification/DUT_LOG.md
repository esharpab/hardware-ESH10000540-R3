---
project: ESH10000654
revision: R0
created: 2026-05-15
---

# DUT Log: ESH10000654 R0 — Sparrow Test Adapter

Chronological record of DUT state, test runs, modifications, and results. **Immutable once logged** — corrections are added as notes, never edits.

See [`30_Workflows/dut-tracking.md`](../../../../30_Workflows/dut-tracking.md) for the tracking workflow.

---

## DUT State

| Date | DUT ID | Serial # | Condition | Notes |
|------|--------|----------|-----------|-------|
| 2026-05-15 | DUT-01 | **P0** | Available (patched — see Patches/Modifications) | In-house assembled board. S/N P0 assigned 2026-05-15. Carries 2× rail patches for prototype relay-driver readback (see DESIGN_LOG.md carry-forward 2026-05-12). |

States: Incoming · Available · In Test · On Hold · Passed · Failed · Scrapped · Returned (per `30_Workflows/dut-tracking.md`).

---

## Patches / Modifications

Immutable, additive log of any physical changes made to a DUT (bodges, fly wires, component swaps, rework). One row per modification — never edit; if a patch is reverted, add a new row.

| Date | DUT ID | Ref des / Net | Change | Reason | Issue link | By | Evidence |
|------|--------|---------------|--------|--------|------------|----|----------|
| 2026-05-15 | DUT-01 (P0) | **Rail A** — nets `FE_MPIO_8`, `FE_MPIO_10`, `RELAY1`, `RELAY3` | Tied these 4 nets together; added **10 kΩ** pull-up to **2.5 V** on the rail | Prototype implementation of relay-driver readback (carry-forward 2026-05-12 in DESIGN_LOG.md). 2-rail ganged version (odd relays + odd MPIOs) — coarser than the 4-channel intent in carry-forward. | — | Martin | TBD (photo / scope capture) |
| 2026-05-15 | DUT-01 (P0) | **Rail B** — nets `FE_MPIO_9`, `FE_MPIO_11`, `RELAY2`, `RELAY4` | Tied these 4 nets together; added **10 kΩ** pull-up to **2.5 V** on the rail | Prototype implementation of relay-driver readback (carry-forward 2026-05-12 in DESIGN_LOG.md). 2-rail ganged version (even relays + even MPIOs) — coarser than the 4-channel intent in carry-forward. | — | Martin | TBD (photo / scope capture) |
| 2026-05-15 | DUT-01 (P0) | **R48** | **Populated** R48 (missing on as-assembled R0 board — present in schematic but not fitted at assembly) | Restore intended schematic functionality. R0 assembly/BOM defect — function of R48 TBD (record from schematic) | — | Martin | TBD (photo) |

### Field meanings

- **Ref des / Net** — Affected component (e.g. `R12`), net (`PWR_EN`), or pin (`J7 pin 12`)
- **Change** — Concrete action ("Replaced R12 with 4.7 kΩ", "Added fly wire from J7-12 to J3-3", "Removed C8")
- **Reason** — Why the patch was made (debug, fix for ISSUE-NNN, design change carry-forward verification, etc.)
- **Issue link** — `ISSUES/ISSUE-NNN.md` if applicable
- **Evidence** — Photo filename in `ASSETS/`, scope capture reference, or test-result ref

> Patches that should drive a next-revision design change must also be reflected in `DESIGN_LOG.md` → "Carry-forward to next revision".

---

## Test Runs

### Session 1: (TBD)

**Date:** (TBD)
**Operator:** (TBD)
**DUT ID:** DUT-01
**DUT Serial #:** (TBD)
**Environment:** (TBD)

| Test Case | Result | Measurement / Evidence | Notes |
|-----------|--------|------------------------|-------|
| | | | |

---

## Issues & Corrections

None yet.

---

## Appendix: Template for New Test Run

```
### Session N: (Descriptive Title)

**Date:**
**Operator:**
**DUT ID:**
**DUT Serial #:**
**Environment:**

| Test Case | Result | Measurement / Evidence | Notes |
|-----------|--------|------------------------|-------|
| | | | |
```

When logging results:
- **Result:** PASS, FAIL, BLOCKED, or N/A
- **Measurement / Evidence:** Raw data, screenshots, or reference to external log
- **Notes:** Any anomalies or context

## Appendix: Template for Patches / Modifications row

```
| YYYY-MM-DD | DUT-NN | Refdes / net | What was changed | Reason / issue link | Operator | Evidence ref |
```
