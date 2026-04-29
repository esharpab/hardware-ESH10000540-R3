# Review Phase Documentation

This folder contains design reviews (schematic, layout, etc.) and review findings for ESH10000540 R3.

## Contents

| File | Purpose |
|------|---------|
| **SCHEMATIC_REVIEW.md** | ERC and design review findings for schematic |
| **LAYOUT_REVIEW.md** | Layout review findings (DFM, signal integrity, etc.) |
| (future) | Review checklists, findings disposition, and approval records |

## Workflow

1. **Import artifact** (schematic, netlist, or layout)
2. **Run review** using workflow from [30_Workflows/schematic-review.md](../../30_Workflows/schematic-review.md)
3. **Log findings** in SCHEMATIC_REVIEW.md or LAYOUT_REVIEW.md
4. **Disposition findings** — link to DECISIONS.md (root) for design changes
5. **Obtain sign-off** — record approval in review document

## Related Files

- Root: [DECISIONS.md](../DECISIONS.md)
- Workflow: [30_Workflows/schematic-review.md](../../30_Workflows/schematic-review.md)
- Workflow: [30_Workflows/review-and-signoff.md](../../30_Workflows/review-and-signoff.md)
