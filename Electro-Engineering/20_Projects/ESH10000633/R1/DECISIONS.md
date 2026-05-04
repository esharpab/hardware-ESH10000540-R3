---
project: ESH10000633
revision: R1
---

# Decisions: Sparrow Complete Product R1

---

## D.01 — Production test scope: system-level only, not sub-assembly re-test

**Date:** 2026-05-04
**Decision:** The production test for ESH10000633 R1 covers system-level integration and key functional checks only. It does not repeat sub-assembly characterization already covered by ESH10000535 R3, ESH10000540 R3, and ESH10000543 R2 verification plans.
**Rationale:** Sub-assembly verification provides full parametric characterization. Production test must be fast and focus on assembly integrity, bus connectivity, and end-to-end signal paths.
**Impact:** Production test will be shorter than sub-assembly verification. Defects in individual PCBA performance (e.g. gain accuracy) are caught at sub-assembly level, not here.
**Follow-up:** Define clear boundary between what is tested at sub-assembly level vs. production test level.

---
