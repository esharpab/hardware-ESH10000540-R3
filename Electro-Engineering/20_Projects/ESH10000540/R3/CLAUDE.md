# ESH10000540 R3 Project Rules

**Project:** Sparrow Fixture Electronics PCBA  
**Revision:** R3 (Verification and Production Test)

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** (root) — Authoritative requirements and test scope
2. **VERIFICATION.md** (Verification/) — Test plan, coverage matrix, and pass/fail criteria
3. **STATUS.md** (root) — Current focus and blockers
4. **Verification/DUT_LOG.md** — Chronological DUT state and test results
5. **DECISIONS.md** (root) — Rationale for key choices
6. **Daily logs** (`10_Daily/`) — Session-by-session work record

---

## Folder Structure & File Organization

```
ESH10000540/R3/
├── CLAUDE.md                 (this file)
├── SPECIFICATION.md          (requirements)
├── STATUS.md                 (current state)
├── DECISIONS.md              (design decisions)
├── DESIGN_LOG.md             (chronological design work)
│
├── Design/
│   ├── README.md             (index)
│   └── DESIGN_PROGRESS.md    (milestones & progress)
│
├── Review/
│   ├── README.md             (index & workflow)
│   ├── SCHEMATIC_REVIEW.md   (schematic findings)
│   └── LAYOUT_REVIEW.md      (layout findings)
│
├── Verification/
│   ├── README.md             (index & workflow)
│   ├── VERIFICATION.md       (test plan)
│   └── DUT_LOG.md            (immutable test results)
│
├── Signoff/
│   ├── README.md             (index & workflow)
│   ├── DESIGN_SIGNOFF.md     (design approval & release)
│   └── VERIFICATION_SIGNOFF.md (test sign-off & release)
│
├── ProductionTest/
│   ├── README.md             (placeholder)
│   └── (future test docs)
│
├── ASSETS/
├── DOCS/
└── ISSUES/
```

---

## Key Rules

- **Test results are immutable:** Once logged in Verification/DUT_LOG.md, never edit a result. Add a correction note instead.
- **Traceability is mandatory:** Every test must link to a requirement ID (from SPECIFICATION.md).
- **No assumptions:** If DUT status or measurement values are unclear, ask before proceeding.
- **Decisions are documented:** If you make a test plan change, update DECISIONS.md (root) with the rationale.

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Skim **Verification/DUT_LOG.md** (latest DUT state and test results).
3. Check **DECISIONS.md** for any recent plan changes.

Do not read other files unless specifically referenced.

---

## Session End

- Append to **Verification/DUT_LOG.md** (if test results were logged).
- Update **STATUS.md** (current focus, next actions, blockers).
- Optionally update **DECISIONS.md** if new decisions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
