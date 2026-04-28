# Review Checklist — {{project}} — {{phase}}

> Use this before a formal review meeting or when generating a sign-off package.
> Work through each section top to bottom. Do not skip sections.

---

## Test coverage

- [ ] All test cases in VERIFICATION.md have a result (Pass / Fail / Deferred)
- [ ] Every deferred test case has a written justification and owner
- [ ] Coverage matrix is up to date — no blank Status cells
- [ ] Every must-have requirement is covered by at least one test case

## Failures and issues

- [ ] Every Fail result has an open issue in `ISSUES/`
- [ ] Every issue has a disposition: Accepted / Waived / Re-test required
- [ ] Waived issues have documented rationale (recorded in DECISIONS.md)
- [ ] Re-test items have been re-tested and result recorded

## Evidence

- [ ] Each test session log references actual evidence files (screenshots, logs, data)
- [ ] Evidence files are stored in `TEST_RESULTS/assets/` or `ASSETS/`
- [ ] No test case is marked Pass without linked evidence

## DUT status

- [ ] DUT_LOG.md reflects the final state of all DUTs
- [ ] No DUT is left in "In Test" state
- [ ] Any damaged or abnormal DUT is noted

## Documentation

- [ ] STATUS.md is current
- [ ] DECISIONS.md captures all scope or criteria changes
- [ ] Any open QUESTIONS.md items have been resolved or deferred with owner

---

## Review outcome

**Date:**
**Reviewer(s):**
**Outcome:** Approved / Approved with conditions / Not approved

**Conditions / open actions:**
- [ ]

**Sign-off note (copy to DECISIONS.md):**
> Decision: Phase sign-off approved — {{phase}}
> Date: {{date}}
> Rationale:
> Impact:
> Follow-up:
