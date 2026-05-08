---
issue_id: ISSUE-001
project: ESH10000633 R1
component: ESH10000538 R0 — M2base loopback
status: Open — investigation needed
opened: 2026-05-06
severity: TBD (potential production blocker)
---

# ISSUE-001 — Sparrow N-Top startup LEDs red, suspected M2base loopback / SPI instability

## Symptom

On power-up, the **Sparrow N-Top LEDs are sometimes red** (fault indication). The condition is **intermittent** — reseating the two M2base loopbacks (ESH10000538) on the base appears to recover normal operation.

## Working hypothesis

Suspected causes, in order of suspicion:

1. **Mechanical: ESH10000538 R0 PCB thickness** — SODIMM-style edge connector relies on PCB thickness within tolerance. If the loopback PCBs are too thin, contact pressure on the SODIMM socket fingers may be marginal, causing intermittent SPI signal integrity issues.
2. **Mechanical: SODIMM socket / loopback edge fingers** — wear, contamination, or plating issue on either side.
3. **Electrical: SPI startup sequencing** — the Enable signal sequence at startup may not be fully deterministic. If SPI traffic begins before the loopback path / downstream device enables are stable, the host may latch a fault state and drive LEDs red. Reseating may not actually be fixing SI — it may just be triggering a cold restart with different timing.

## What to verify

- [ ] Measure ESH10000538 R0 PCB thickness — compare to SODIMM connector spec (typically 1.27 mm nominal, ~1.20–1.30 mm tolerance window). Check several PCBs across the existing stock.
- [ ] Inspect the gold-finger plating and edge bevel on ESH10000538 — any visible wear, oxidation, or burr.
- [ ] Inspect SODIMM socket on the base — contact debris, bent fingers, retention clip force.
- [ ] Capture SPI signals (CLK, MOSI, MISO, CS) on a scope at the loopback connector during a **failing** boot. Compare against a passing boot.
- [ ] Document the **Enable-signal startup sequence** — which rails / enables come up in what order, and when does SPI traffic start relative to those enables. Confirm whether there is a defined settle window before SPI access.
- [ ] If the issue reproduces with one specific loopback PCB consistently, swap it with another — if the failure follows the PCB, root cause is mechanical / per-board.

## Workaround (current)

Reseat both M2base loopbacks until LEDs come up green.

## Impact

- **Production test:** must be reproducible / debuggable before PRODUCTION_TEST_PROCEDURE.md is finalized — production cannot ship 20 units that need loopback reseating to boot.
- **PRODUCTION_READINESS.md §3.4:** ESH10000538 already flagged as critical shortage (−4) and NotApproved. Revision approval should be gated on resolving this issue.
- **Linked to:** STATUS.md Open Issue 5 (ESH10000654 test adapter open items) — partially overlapping investigation.

## Notes

- Issue logged from intermittent observation on the bench by MJ — not yet root-caused. Hypotheses are explicitly **unverified**.
- No DUT has formally failed a recorded production test step from this — this is a pre-emptive issue note so it is not lost.
