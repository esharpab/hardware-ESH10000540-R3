# Verification — Fixture Link R2

| File | Purpose |
|------|---------|
| [VERIFICATION.md](VERIFICATION.md) | Test plan, test cases, and pass/fail criteria |
| [DUT_LOG.md](DUT_LOG.md) | Chronological DUT state and test results (immutable once logged) |

## Workflow

1. Assign DUT serial numbers in DUT_LOG.md before testing begins.
2. Execute test cases in sequence order from VERIFICATION.md.
3. Log all results — measured values, pass/fail, and comments — in DUT_LOG.md.
4. Results are immutable once written; add a correction note rather than editing.
5. Update VERIFICATION.md test coverage status as test cases complete.

## Related Files

- Requirements: [SPECIFICATION.md](../SPECIFICATION.md)
- Schematic review: [Review/SCHEMATIC_REVIEW.md](../Review/SCHEMATIC_REVIEW.md)
- Workflow: [30_Workflows/](../../../../30_Workflows/)
