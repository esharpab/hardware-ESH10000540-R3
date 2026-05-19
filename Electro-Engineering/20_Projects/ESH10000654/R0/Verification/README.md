# Verification — ESH10000654 R0

Files in this folder:

- **[VERIFICATION.md](VERIFICATION.md)** — Test plan, coverage matrix, pass/fail criteria. Derived from `../SPECIFICATION.md` (22 requirements → 32 test cases).
- **[DUT_LOG.md](DUT_LOG.md)** — Immutable per-DUT log of state, patches/modifications, and test results.

Per the workbook conventions (see [`30_Workflows/dut-tracking.md`](../../../../30_Workflows/dut-tracking.md)):

- Results in DUT_LOG.md are **immutable once recorded** — corrections are added as notes, never edits.
- Each test result links back to a SPECIFICATION Req ID via the VERIFICATION coverage matrix.
- Physical changes to a DUT (bodges, fly wires, component swaps) go in the **Patches / Modifications** section of DUT_LOG.md.
