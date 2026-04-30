# ESH10000535 R3 Project Rules

**Project:** Sparrow N-Top
**Revision:** R3 (Design Review)

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** (root) — Authoritative requirements and design scope
2. **Review/SCHEMATIC_REVIEW.md** — Schematic ERC findings and disposition
3. **STATUS.md** (root) — Current focus and blockers
4. **DECISIONS.md** (root) — Rationale for key choices
5. **DESIGN_LOG.md** (root) — Chronological design work record
6. **Daily logs** (`10_Daily/`) — Session-by-session work record

---

## Folder Structure & File Organization

```
ESH10000535/R3/
├── CLAUDE.md                 (this file)
├── SPECIFICATION.md          (requirements)
├── STATUS.md                 (current state)
├── DECISIONS.md              (design decisions)
├── DESIGN_LOG.md             (chronological design work)
│
├── Review/
│   ├── README.md             (index & workflow)
│   └── SCHEMATIC_REVIEW.md   (schematic ERC findings)
│
├── Signoff/
│   └── DESIGN_SIGNOFF.md     (design approval)
│
├── ASSETS/
├── DOCS/
└── ISSUES/
```

---

## Key Rules

- **No assumptions:** If a finding is ambiguous, ask for the schematic or datasheet section before dispositioning.
- **Decisions are documented:** Log any accepted/waived finding in DECISIONS.md with rationale.
- **Review findings are append-only:** Once logged in SCHEMATIC_REVIEW.md, never delete a row — add a disposition note instead.
- **Sign-off is engineer-only:** Only the engineer may mark a review as Approved.

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Read **Review/SCHEMATIC_REVIEW.md** (open findings).
3. Check **DECISIONS.md** for any recent dispositions.

Do not read other files unless specifically referenced.

---

## Session End

- Update **Review/SCHEMATIC_REVIEW.md** with new findings or dispositions.
- Update **STATUS.md** (current focus, next actions, blockers).
- Optionally update **DECISIONS.md** if new dispositions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
