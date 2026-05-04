# ESH10000536 R2 Project Rules

**Project:** Active Load  
**Revision:** R2

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** (root) — Authoritative requirements and design scope
2. **Design/DESIGN_PROGRESS.md** — Design milestones and open items (when populated)
3. **Verification/VERIFICATION.md** — Test scope and coverage (when populated)
4. **STATUS.md** (root) — Current focus and blockers
5. **DECISIONS.md** (root) — Rationale for key choices
6. **DESIGN_LOG.md** (root) — Chronological design work record
7. **Daily logs** (`10_Daily/`) — Session-by-session work record

---

## Folder Structure & File Organization

```
ESH10000536/R2/
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
│   ├── SCHEMATIC_REVIEW.md   (schematic ERC findings)
│   └── LAYOUT_REVIEW.md      (layout review findings)
│
├── Verification/
│   └── README.md             (placeholder — populated when DV starts)
│
├── ProductionTest/
│   └── README.md             (placeholder — populated when PT is defined)
│
├── Signoff/
│   └── README.md             (placeholder)
│
├── ASSETS/
├── DOCS/
└── ISSUES/
```

---

## Key Rules

- **Traceability is mandatory:** Every design decision must link to a requirement or rationale.
- **No assumptions:** If interface requirements or connector pinouts are unclear, ask before proceeding.
- **Decisions are documented:** Any change to design scope or approach → update DECISIONS.md.
- **Test results are immutable:** Once logged in Verification/DUT_LOG.md (when populated), never edit a result.

---

## Context

Active Load PCBA (internal name: `m2top_2xload`) used in the Sparrow product family, assembled together with Fixture Electronics (ESH10000540).
Phase is TBD — update this file when design or verification work begins.

When design activities start, create `Design/DESIGN_PROGRESS.md`.
When verification activities start, create `Verification/VERIFICATION.md` and `Verification/DUT_LOG.md`.

---

## Available Documentation (DOCS/)

| File | Type | Description |
|------|------|-------------|
| `m2top_2xload_R2.pdf` | Schematic | Full schematic — read when planning test coverage or reviewing circuits |
| `m2top_2xload_R2_BOM.csv` | BOM | Full bill of materials — use for component-level test planning |
| `vb_ais.txt` | Placement | PADS AIS component placement file — use for assembly verification |

### Board architecture summary (from BOM/placement)

| Block | Component(s) | Function |
|-------|-------------|----------|
| Load channels (×2) | Q1, Q2 (70N06 N-MOSFET) | Active load pass elements |
| Current sense | U1 (INA2181A1) | Current measurement per channel |
| Load control | U2 (OPA2192), U4 (AD5593R ADC/DAC) | Current setpoint via DAC; voltage/current readback via ADC |
| Voltage reference | U3 (REF3425) | 2.5 V reference for ADC/DAC |
| Digital isolator | U5 (ISOW7741) | Isolates load side from controller bus |
| Board ID EEPROM | U6 (24AA02UID) | Unique board identification |
| Fan control | U7 (MAX6650) | Fan speed control for thermal management |
| Temperature | U8 (TMP116) | Board temperature monitoring |
| LED driver | U9 (LP5012) | 12-ch LED driver (status indicators) |
| Load connectors | J3, J4 (4-pin terminal blocks) | Load outputs, one per channel |
| Platform connector | J1 (Accordion M.2 module) | Interface to Sparrow/Accordion platform |
| Power connector | J5 (TE 2-292173-3) | Board power input |
| Status LEDs | D2–D5 (W2S118TS) | White status LEDs |

### Key production test targets (to expand when PT is planned)

- EEPROM UID readable and unique (U6)
- Both load channels functional and calibrated (Q1/Q2, U1, U2, U4)
- Temperature sensor readable (U8)
- Fan control responsive (U7)
- LED driver and status LEDs functional (U9, D2–D5)
- Platform interface communicates correctly via J1

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Check **DECISIONS.md** for any recent plan changes.
3. If in design phase: skim **Design/DESIGN_PROGRESS.md**.
4. If in verification phase: skim **Verification/VERIFICATION.md**.

Do not read other files unless specifically referenced.

---

## Session End

- Append to **DESIGN_LOG.md** (if design work was done).
- Update **STATUS.md** (current focus, next actions, blockers).
- Optionally update **DECISIONS.md** if new decisions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
