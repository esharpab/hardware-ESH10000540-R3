# Verification Planning Workflow

## Purpose
Define what needs to be verified, how it will be tested, and what counts as pass.
This workflow results in a completed `VERIFICATION.md` for a project.

## When to use this workflow
- At the start of a new verification effort
- When requirements change and test coverage must be reassessed
- When the scope of a prototype/DVT phase is being defined

---

## Step 1 — Gather inputs
Before writing the plan, collect:
- Requirements document (or list of requirements to cover)
- Hardware revision and configuration under test
- Any existing test procedures or legacy test cases
- Known constraints (lab availability, DUT count, regulatory deadlines)

## Step 2 — Define verification scope
Write a one-paragraph scope statement:
- What is being verified (product, subsystem, revision)
- What is explicitly OUT of scope
- What standard or requirement set is the reference

## Step 3 — List requirements
Create a requirements table. For each requirement:

| Req ID | Requirement | Source | Priority | Verification Method |
|---|---|---|---|---|
| REQ-001 | Description | Spec section X | Must | Test / Inspection / Analysis |

**Verification methods:**
- **Test** — apply stimulus, measure output
- **Inspection** — visual check or document review
- **Analysis** — calculation or simulation

## Step 4 — Define test cases
For each requirement (or group of related requirements), define at least one test case.
Use `60_Templates/test_case.md` as the base.

Each test case must include:
- Unique ID (TC-001)
- Linked requirement(s)
- Pass/fail criterion — specific, measurable
- Required setup (equipment, DUT state, environment)
- Test procedure steps

## Step 5 — Build the coverage matrix
Verify that every requirement has at least one test case linked to it.
Flag any requirement without coverage as OPEN.

| Req ID | Test Case(s) | Coverage |
|---|---|---|
| REQ-001 | TC-001, TC-002 | ✅ Covered |
| REQ-002 | — | ⚠️ Open |

## Step 6 — Review and approve the plan
- Walk through the plan for completeness and feasibility
- Identify test cases that are blocked (missing equipment, undefined acceptance criteria)
- Record any scope decisions in DECISIONS.md

---

## AI usage in this workflow
- AI can help draft the requirements table and test cases from a pasted requirements document
- AI must not assign pass/fail status to any test case — only the engineer can do that
- AI must flag any requirement that has no test case coverage
