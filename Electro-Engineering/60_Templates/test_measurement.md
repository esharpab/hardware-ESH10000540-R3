---
session_id: "TS-{{date}}-001"
date: "{{date}}"
engineer: "{{engineer}}"
dut_id: "DUT-01"
dut_serial: "{{serial}}"
categories_tested:
  - "{{category_id}}"
---

# Test Session — {{date}} — {{category}} — {{dut_id}}

## Pre-session checks

- [ ] DUT state confirmed (DUT_LOG.md updated to "In Test")
- [ ] Equipment ready and calibrated
- [ ] Safety conditions checked

## Measurements

| ID | Measured DMM | Measured ADC Min | Measured ADC Max | Pass/Fail | Comment |
|----|-------------|-----------------|-----------------|-----------|---------|
| {{id}} | | | | | |

## Observations

_Notes on anomalies, edge cases, or items to monitor._

## Evidence

_Links to waveform captures, photos, or data files in ASSETS/._

## Session summary

**Completed:** {{list of test IDs}}
**Failures:** None
**DUT state after session:** Available

## Next actions

- [ ] _follow-up items_

---

> Results are immutable once written. Add correction notes rather than editing.
