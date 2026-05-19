# Project Index

Overview of all projects — active and otherwise.

| Project | Product / Document | Revision | Phase | Status | Notes |
|---|---|---|---|---|---|
| ESH10000540 | Sparrow Fixture Electronics PCBA | R3 | Verification | 🟢 Active | Verification plan complete (351 tests, 29 req) — awaiting DUT serial numbers; R132 gain gap open |
| ESH10000535 | Sparrow N-Top | R3 | Verification | 🟢 Active | Verification plan complete incl. R3-CHG tests — awaiting R3 DUT serials |
| ESH10000543 | Fixture Link | R2 | Verification | 🟢 Active | Verification plan complete (24 tests); F-02 CM32 pull-ups confirmed — awaiting R2 DUT |
| ESH10000536 | Active Load | R2 | — | 🔵 Planned | Project created — phase and requirements TBD; assembled with Fixture Electronics (ESH10000540) |
| ESH10000654 | Sparrow Test Adapter | R0 | Verification | 🟢 Active | VERIFICATION.md created 2026-05-15 (33 test cases, 22/22 req covered); DUT_LOG.md created — DUT-01 S/N P0 with 2 rail patches (10 kΩ→2.5 V) and R48 populated (R0 BOM defect). Pending: schematic/layout review, 4 open interface items, test execution |
| ESH10000633 | Sparrow Complete Product | R1 | Production Test | 🟢 Active | Major Gate 1 MES audit 2026-05-12: 9 promotions, ESH10000539 R2 created (60 incoming to be mounted as R2), USB PD R1.0 rollout, scope expanded (10× 636 / 20× 614 / 20× 637 / 20× EPN1000786 standalone). Open: ESH10000182 build order, 522/544/572 rev creates, R1 retirement, 538 ISSUE-001 |
| ESH10000634 | Sparrow FE N-Top | R3 | Design | 🔵 Planned | Project created — requirements definition next |
| ESH10000534 | PoE | R4 | Design | 🟢 Active | Project created — requirements definition next |

---

## Column definitions

| Column | Meaning |
|---|---|
| Project | Short name linking to `20_Projects/Project-<Name>/` |
| Product / Document | Product name, part number, or requirements document reference |
| Revision | Hardware or document revision under design or test |
| Phase | e.g. Requirements, Schematic, Layout, Release, Prototype, DVT, Compliance, Sign-off |
| Status | See legend below |
| Notes | Free-text: blockers, DUT location, etc. |

---

## Status legend

| Symbol | Meaning |
|---|---|
| 🟢 Active | Ongoing work |
| 🟡 Paused | On hold, may resume |
| ✅ Done | Project complete and signed off |
| 🔵 Planned | Scope defined, not yet started |
| 🔴 Blocked | Waiting on DUT, requirements, or external input |
