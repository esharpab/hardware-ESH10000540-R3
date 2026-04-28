---
product: "{{product}}"
revision: "{{revision}}"
phase: "{{phase}}"
date_created: "{{date}}"
engineer: "{{engineer}}"
dut_slots: 4

categories:
  - id: M
    name: Mechanical
    color: "#A6A6A6"
    slots: 4
  - id: P
    name: Power
    color: "#F4B084"
    slots: 4
  - id: A
    name: Analog
    color: "#A9D18E"
    slots: 4
  - id: D
    name: Digital
    color: "#BDD7EE"
    slots: 4
  - id: C
    name: Connectors
    color: "#FFFF00"
    slots: 4
  - id: S
    name: System
    color: "#C5B0D5"
    slots: 4
  - id: R
    name: Routing
    color: "#D5A6E6"
    slots: 4
  - id: O
    name: Other
    color: "#A5A5A5"
    slots: 4
---

# Verification Plan — {{project}}

> AI instruction: This is the authoritative document for verification scope and test coverage.
> Never mark a test step as passed unless explicitly stated by the engineer.
> When the engineer reports a measurement, fill in the Measured column and evaluate
> against Nominal ± Tolerance. Only the engineer may set the Result or update Accepted.

---

## Scope

**Product / Document:** {{product}}
**Hardware revision:** {{revision}}
**Verification phase:** {{phase}}
**Date created:** {{date}}
**Engineer:** {{engineer}}

**In scope:**
{{describe what is being verified}}

**Out of scope:**
{{explicitly list exclusions}}

**Reference documents:**
- {{requirements document, schematics, etc.}}

---

## Column definitions

| Column | Description |
|--------|-------------|
| **ID** | Unique step identifier (category prefix + number) |
| **Step** | Short name for the test step |
| **Function** | What circuit / subsystem is under test |
| **Test** | Description of what is applied and what is observed |
| **Conditions** | Stimulus details — voltage, current, load, duration, temperature, etc. |
| **Signals** | Net names / test points involved |
| **Nominal** | Expected value from design / datasheet |
| **Unit** | Unit of measurement |
| **Tol** | Acceptable tolerance (±value, ±%, or min–max range) |
| **Measured** | Actual value recorded during DUT test |
| **Result** | ✅ PASS / ❌ FAIL / ⏭ DEFERRED / ⚠️ OPEN |
| **Accepted** | Engineer-approved acceptance value (if different from Nominal ± Tol) |
| **Notes** | Observations, justifications for acceptance, anomalies |

---

## Test Steps

### Mechanical

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| M.00 | | | | | | | | | | ⚠️ | | |
| M.01 | | | | | | | | | | ⚠️ | | |
| M.02 | | | | | | | | | | ⚠️ | | |
| M.03 | | | | | | | | | | ⚠️ | | |

### Power

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| P.00 | | | | | | | | | | ⚠️ | | |
| P.01 | | | | | | | | | | ⚠️ | | |
| P.02 | | | | | | | | | | ⚠️ | | |
| P.03 | | | | | | | | | | ⚠️ | | |

### Analog

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| A.00 | | | | | | | | | | ⚠️ | | |
| A.01 | | | | | | | | | | ⚠️ | | |
| A.02 | | | | | | | | | | ⚠️ | | |
| A.03 | | | | | | | | | | ⚠️ | | |

### Digital

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| D.00 | | | | | | | | | | ⚠️ | | |
| D.01 | | | | | | | | | | ⚠️ | | |
| D.02 | | | | | | | | | | ⚠️ | | |
| D.03 | | | | | | | | | | ⚠️ | | |

### Connectors

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| C.00 | | | | | | | | | | ⚠️ | | |
| C.01 | | | | | | | | | | ⚠️ | | |
| C.02 | | | | | | | | | | ⚠️ | | |
| C.03 | | | | | | | | | | ⚠️ | | |

### System

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| S.00 | | | | | | | | | | ⚠️ | | |
| S.01 | | | | | | | | | | ⚠️ | | |
| S.02 | | | | | | | | | | ⚠️ | | |
| S.03 | | | | | | | | | | ⚠️ | | |

### Routing

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| R.00 | | | | | | | | | | ⚠️ | | |
| R.01 | | | | | | | | | | ⚠️ | | |
| R.02 | | | | | | | | | | ⚠️ | | |
| R.03 | | | | | | | | | | ⚠️ | | |

### Other

| ID | Step | Function | Test | Conditions | Signals | Nominal | Unit | Tol | Measured | Result | Accepted | Notes |
|----|------|----------|------|------------|---------|---------|------|-----|----------|--------|----------|-------|
| O.00 | | | | | | | | | | ⚠️ | | |
| O.01 | | | | | | | | | | ⚠️ | | |
| O.02 | | | | | | | | | | ⚠️ | | |
| O.03 | | | | | | | | | | ⚠️ | | |

---

## Coverage Summary

| Category | Defined | Tested | Passed | Failed | Deferred | Open |
|----------|---------|--------|--------|--------|----------|------|
| Mechanical | 0 | 0 | 0 | 0 | 0 | 0 |
| Power | 0 | 0 | 0 | 0 | 0 | 0 |
| Analog | 0 | 0 | 0 | 0 | 0 | 0 |
| Digital | 0 | 0 | 0 | 0 | 0 | 0 |
| Connectors | 0 | 0 | 0 | 0 | 0 | 0 |
| System | 0 | 0 | 0 | 0 | 0 | 0 |
| Routing | 0 | 0 | 0 | 0 | 0 | 0 |
| Other | 0 | 0 | 0 | 0 | 0 | 0 |

**Status:** ⚠️ Open / 🔄 In Progress / ✅ Pass / ❌ Fail / ⏭ Deferred

---

## Appendixes

> Reference from the Notes column as "See Appendix A", "See Appendix B", etc.
> Label each appendix with the test step ID and name.

### Appendix A

{{Graph, image, or data here}}

---

## Sign-off

| Milestone | Condition | Signed off | Date |
|-----------|-----------|------------|------|
| Phase complete | All defined test steps pass or have approved waiver | | |
