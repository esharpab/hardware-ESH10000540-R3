---
product: "{{product}}"
revision: "{{revision}}"
date_created: "{{date}}"
engineer: "{{engineer}}"
status: "Draft"
---

# Requirements Specification — {{project}} {{revision}}

> AI instruction: This is the authoritative requirements document for this project.
> Never mark a requirement as Approved, Changed, or Deleted without explicit instruction from the engineer.
> Never invent Req IDs. When the engineer adds a requirement, assign the next sequential ID.

---

## Scope

**Product / Document:** {{product}}
**Hardware revision:** {{revision}}
**Date created:** {{date}}
**Engineer:** {{engineer}}

**In scope:**
{{describe what is being specified}}

**Out of scope:**
{{explicitly list exclusions}}

**Reference documents:**
- {{customer spec, standards, datasheets, etc.}}

---

## Column definitions

| Column | Description |
|--------|-------------|
| **Req ID** | Unique identifier (REQ-001, REQ-002...) |
| **Requirement** | Concise statement of what the design shall do |
| **Type** | Functional / Performance / Mechanical / Interface / Environmental / Safety |
| **Source** | Where this requirement comes from (customer spec, standard, internal) |
| **Priority** | Must / Should / Nice |
| **Acceptance Criterion** | Measurable condition that proves compliance |
| **Status** | Draft / Approved / Changed / Deleted |
| **Trace** | Link to verification step (e.g. P.03, A.01) — filled when VERIFICATION.md exists |

---

## Requirements

| Req ID | Requirement | Type | Source | Priority | Acceptance Criterion | Status | Trace |
|--------|-------------|------|--------|----------|---------------------|--------|-------|
| REQ-001 | | | | | | Draft | |

---

## Traceability

> When a VERIFICATION.md exists for this project, populate the **Trace** column with the test step IDs that verify each requirement.
> Use the verification-planning workflow to build a coverage matrix and ensure every "Must" requirement has at least one test case.

---

## Revision history

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | {{date}} | {{engineer}} | Initial draft |

---

## Sign-off

| Milestone | Condition | Signed off | Date |
|-----------|-----------|------------|------|
| Requirements approved | All requirements reviewed and baselined | | |
