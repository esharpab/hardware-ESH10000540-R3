# Review and Sign-off Workflow

## Purpose
Define how verification results are reviewed, issues are dispositioned, and a project phase is formally closed.

---

## Review gates

A review is triggered when:
- All test cases for a phase or scope area are complete (or explicitly deferred)
- A milestone requires a verification sign-off
- A design change affects previously verified test cases

---

## Pre-review checklist

Before calling a review meeting or generating a review package:

- [ ] All test cases have a result: Pass / Fail / Deferred with justification
- [ ] All failures have an open issue in `ISSUES/`
- [ ] Each issue has a disposition: Accepted, Waived, or Requires re-test
- [ ] Coverage matrix is up to date in VERIFICATION.md
- [ ] DUT_LOG.md reflects the final state of all DUTs
- [ ] Evidence files are referenced in test session logs

---

## Issue disposition

For each open issue from `ISSUES/`, record a disposition decision:

| Disposition | Meaning |
|---|---|
| Accepted | Failure accepted as-is — within acceptable risk |
| Waived | Requirement waived or scope changed — record in DECISIONS.md |
| Re-test required | Issue resolved or root cause corrected — re-run affected test case |

---

## Review package

A review package typically contains:
- Executive summary (verification scope, result overview, open items)
- Coverage matrix with final results
- Summary of failures and dispositions
- DUT status summary
- Evidence appendix (links/paths to session logs and assets)

Use `40_Tools/report_builder.py` to generate a structured Markdown report from session data.

---

## Sign-off

Sign-off conditions:
- All must-have requirements covered and passed (or waived with documented rationale)
- No open Fail dispositions without accepted or waived status
- Review package approved by responsible engineer

Record sign-off in DECISIONS.md:
```
Decision: Phase sign-off approved
Date: YYYY-MM-DD
Rationale: All REQ-xxx through REQ-xxx verified. Open items: [list]
Impact: Product is cleared for [next phase]
Follow-up: [any open actions, re-tests, or post-sign-off work]
```

---

## AI usage in this workflow
- AI can generate a coverage summary and open issue list on request
- AI can draft the review package from pasted session logs and VERIFICATION.md
- AI must not mark any requirement as "passed" or "signed off" — only the responsible engineer does that
