---
project: ESH10000535
revision: R3
document: DUT Log
created: 2026-05-04
---

# DUT Log — Sparrow N-Top R3

## Rules

- Results are **immutable** once logged. Never edit a recorded result.
- To correct an error: add a correction note below the original entry.
- Record actual measured values, not just Pass/Fail.
- One section per DUT. One entry per test session.

---

## DUT Register

| DUT # | Serial Number | HW Rev | FW Rev | Location | Status |
|-------|--------------|--------|--------|----------|--------|
| DUT-1 | — | R3 | — | — | ⏳ Not started |
| DUT-2 | — | R3 | — | — | ⏳ Not started |
| DUT-3 | — | R3 | — | — | ⏳ Not started |

---

## DUT-1

*Serial: TBD*

*(No entries yet)*

---

## DUT-2

*Serial: TBD*

*(No entries yet)*

---

## DUT-3

*Serial: TBD*

*(No entries yet)*

---

## Reference — R2 Results Summary

Carried from DOCS/Verification_Sparrow_N-TOP.xlsx for traceability.

| Test ID | DUT A002757 | DUT A002758 | DUT A002759 | Notes |
|---------|------------|------------|------------|-------|
| M.00 | Pass | Pass | Pass | R96 and R76 were missing in earlier build |
| M.01 | Pass | Pass | Pass | |
| M.02 | Pass | Pass | Pass | |
| P.00–P.06 | Pass | Pass | Pass | All power rails within tolerance |
| P.07–P.14 | Pass | Pass | Pass | 100pF feedback cap added to suppress PWM/TACH_VCCO ripple |
| P.15–P.22 | Pass | Pass | Pass (partial) | Some R2 DUT-3 measurements not recorded (−1 in log) |
| CIO.00 | Pass | Pass | Pass | R96 missing caused wrong address in earlier build |
| CIO.01 | Question | Question | Question | PROG_EN toggle sometimes required; behaviour not fully resolved |
| CIO.02–CIO.10 | Pass | Pass | Pass | |
| UIO.00 | Fail (1 unit) | Pass | Fail | PWM issue on some units — investigate on R3 |
| UIO.01 | — | — | — | Not recorded in R2 log |
| UIO.02 | Pass | Pass | Pass | |
| UIO.03 | See FE | See FE | See FE | Tested via Fixture Electronics |
| C.00–C.01 | Pass | Pass | Pass | |
