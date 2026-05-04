---
project: ESH10000543
revision: R2
created: 2026-05-04
---

# DUT Log: Fixture Link R2

Chronological record of DUT state, test runs, and results. **Immutable once logged** — corrections are added as notes, never edits.

---

## DUT State

| Date | Serial # | Condition | Notes |
|------|----------|-----------|-------|
| 2026-05-04 | — | — | Verification plan created; no R2 DUT assigned yet |

---

## Test Runs

*(No runs logged yet — awaiting R2 DUT)*

---

## Issues & Corrections

None yet.

---

## Appendix: Template for New Test Run

```
### Session N: <Descriptive Title>

**Date:**
**Operator:**
**DUT Serial #:**
**Environment:** VDD = 20 V, ambient temperature

| ID | Test | Result | Measured | Unit | Notes |
|----|------|--------|----------|------|-------|
| M.00 | No Mounts | | | | |
| M.01 | Panel Fit | | | | |
| P.00 | VDD Supply | | | V | |
| P.01 | 5V Supply | | | V | |
| P.02 | 3V3 Supply | | | V | |
| P.03 | VID Supply | | | V | |
| P.04 | VOUT (eFuse output) | | | V | |
| P.05 | PG threshold | | | V | |
| P.06 | ILM current limit | | | A | |
| P.07 | OVLO trip level | | | V | |
| P.08 | Slew @ no load | | | V/ms | |
| P.09 | Slew @ 430 mA | | | V/ms | |
| P.10 | Slew @ 500 mA | | | | Expected: does not start |
| P.11 | ITIMER | | | ms | |
| C.00 | I2C expander + EEPROM | | | | |
| C.01 | Power LED | | | | |
| C.02 | RS-232 LED | | | | |
| C.03 | READY / PIDET | | | | |
| C.04 | I2C transceivers | | | | |
| C.05 | SRQ / U7 output levels | | | | Closes F-02 |
| C.06 | UART loopback | | | | |
```

When logging results:
- **Result:** PASS, FAIL, BLOCKED, or N/A
- **Measured:** raw value where applicable
- **Notes:** any anomalies, waveform references, or context
