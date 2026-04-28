# DUT Tracking Workflow

## Purpose
Maintain a reliable record of every Device Under Test (DUT) — its identity, current state, and history across test sessions.

---

## DUT states

| State | Meaning |
|---|---|
| Incoming | DUT received, not yet characterized |
| Available | Ready for testing |
| In Test | Currently assigned to an active test session |
| On Hold | Reserved — waiting for equipment, parts, or decision |
| Passed | All assigned test cases passed |
| Failed | One or more test cases failed — pending disposition |
| Scrapped | No longer usable |
| Returned | Returned to supplier, customer, or production |

---

## DUT intake

When a new DUT arrives:
1. Assign a DUT ID — use a short local identifier (e.g. `DUT-01`, `DUT-02`)
2. Record in `DUT_LOG.md`:
   - DUT ID
   - Description (part number, variant, hardware revision)
   - Serial number (if available)
   - Date received
   - Initial condition (as-received notes)
   - State: **Incoming**
3. Note any pre-existing damage or deviations from expected condition
4. Update state to **Available** once the DUT is confirmed ready

---

## During test sessions

- Update DUT state to **In Test** at the start of the session
- Record in the history section which test session the DUT was used in
- Note any changes to the DUT: modifications, damage, configuration changes
- Return to **Available** (or **Passed** / **Failed**) at the end of the session

---

## After a failure

- Set state to **Failed**
- Reference the ISSUE number from `ISSUES/`
- Record the failure condition and date
- Do not reuse the DUT until the failure is understood and a disposition decision is made

---

## AI usage in this workflow
- AI can help maintain and update DUT_LOG.md from session notes
- AI must not infer DUT state from test results — state must be explicitly set
- AI can generate a DUT status summary table on request
