---
project: ESH10000654
revision: R0
created: 2026-05-04
---

# Design Log: Sparrow Test Adapter R0

Chronological record of design work, decisions, and iterations.

---

## 2026-05-04 — Project created

- Project ESH10000654 / Sparrow Test Adapter / R0 created.
- Scope: test adapter for Sparrow verification and production test together with Accordion.
- Project structure established. Requirements definition is the next step.

---

## Carry-forward to next revision

Items to incorporate into the next revision of the Test Adapter.

### 2026-05-12 — J7 pins 12/14/16/18: relay-driver readback for Sparrow FE

**Change:** J7 pins **12, 14, 16, 18** are now relay drivers on the Sparrow FE side. The Test Adapter must let the Accordion read back the state of each driver.

**Circuit required (per pin, ×4):**
- Pull-up to **2.5 V**
- Connection to **FE_MPIO_[8:11]** (one MPIO per relay driver — pin 12 → FE_MPIO_8, 14 → MPIO_9, 16 → MPIO_10, 18 → MPIO_11 — *to be confirmed in schematic*)

**Expected readback behavior:**
- Relay driver **OFF** → FE_MPIO reads **2.5 V** (pull-up wins)
- Relay driver **ON** → FE_MPIO reads **0 V** (driver pulls the line low)

**Why:** Allows the production test to verify the FE relay-driver outputs via Accordion's MPIO inputs rather than needing a separate measurement probe.

**Open:**
- Confirm exact pin-to-MPIO mapping (above is assumed sequential 8→11)
- Pull-up resistor value (TBD — sized for FE_MPIO input bias / leakage)
- Add to next-revision SPECIFICATION as a new requirement (suggest INT or FN class)
