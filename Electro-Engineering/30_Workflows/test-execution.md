# Test Execution Workflow

## Purpose
Run test cases systematically, document results with evidence, and log everything in a way that supports traceability and review.

---

## Before a test session

1. **Check STATUS.md** — confirm which test cases are open and prioritized
2. **Check DUT_LOG.md** — confirm the DUT is available and in the expected state
3. **Create a session log** from `60_Templates/test_session.md` in `TEST_RESULTS/`
   - Name: `YYYY-MM-DD_<session-description>.md` (e.g. `2026-04-01_TC003-power-on-sequence.md`)
4. **Set up equipment** — note calibration status if relevant

---

## During a test session

- Execute the test procedure steps in order
- Record results immediately — do not rely on memory at the end of the session
- Log pass/fail for each step, not just the overall test case
- Capture evidence: measurements, waveform screenshots, photos, log files
  - Store in `TEST_RESULTS/assets/` or `ASSETS/`
  - Reference file paths in the session log
- If a step fails: stop, note the failure conditions, and decide whether to continue or abort

---

## Result classification

| Result | Meaning |
|---|---|
| ✅ Pass | All steps met acceptance criteria |
| ❌ Fail | One or more steps did not meet criteria |
| ⚠️ Inconclusive | Test could not be completed (DUT issue, setup problem) |
| ⏭ Deferred | Skipped intentionally — document reason |

---

## After a test session

1. **Finalize the session log** — results are immutable once written; add correction notes rather than editing
2. **Update VERIFICATION.md** — mark the test case status in the coverage matrix
3. **If a test failed** — open an issue in `ISSUES/` using the naming `ISSUE-NNN_short-description.md`
4. **Update DUT_LOG.md** — record the test session and any change in DUT state
5. **Update STATUS.md** — reflect current coverage and next test cases

---

## AI usage in this workflow
- AI can help draft test session logs from pasted notes
- AI must not fill in pass/fail results from inference — only record explicitly stated outcomes
- AI can help analyze patterns across multiple test sessions (e.g. which test cases have been failing)
- On failure analysis: AI may suggest potential root causes but must label them as hypotheses
