# ESH10000540 R3 Project Rules

**Project:** Sparrow Fixture Electronics PCBA  
**Revision:** R3 (Verification and Production Test)

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** — authoritative requirements and test scope
2. **VERIFICATION.md** — test plan, coverage matrix, and pass/fail criteria
3. **STATUS.md** — current focus and blockers
4. **DUT_LOG.md** — chronological DUT state and test results
5. **DECISIONS.md** — rationale for key choices
6. **Daily logs** (`10_Daily/`) — session-by-session work record

---

## Key Rules

- **Test results are immutable:** Once logged in DUT_LOG.md, never edit a result. Add a correction note instead.
- **Traceability is mandatory:** Every test must link to a requirement ID (from SPECIFICATION.md).
- **No assumptions:** If DUT status or measurement values are unclear, ask before proceeding.
- **Decisions are documented:** If you make a test plan change, update DECISIONS.md with the rationale.

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Skim **DUT_LOG.md** (latest DUT state and test results).
3. Check **DECISIONS.md** for any recent plan changes.

Do not read other files unless specifically referenced.

---

## Session End

- Append to **DUT_LOG.md** (if test results were logged).
- Update **STATUS.md** (current focus, next actions, blockers).
- Optionally update **DECISIONS.md** if new decisions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
