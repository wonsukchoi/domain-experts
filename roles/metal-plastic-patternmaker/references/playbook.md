# Playbook

## Shrink-rule application worksheet (CNC pattern programming)

Fill before programming any pattern dimension for machining.

| Field | Value |
|---|---|
| Casting | Bronze Bushing, target bore 2.000" |
| Metal shrink rule | 3/16"/ft (~1.6%) |
| Target dimension in feet | 2.000"/12 = 0.1667 ft |
| Shrinkage allowance | 0.1667 × 0.1875 = 0.031" |
| Programmed pattern dimension | 2.000" + 0.031" = 2.031" |
| First-casting trial result | 1.998"-2.002" across 5-casting sample |
| Within tolerance? | Y (±0.005" spec) |

**Rule:** never program a pattern dimension as the literal target casting dimension — CNC precision applies to hitting whatever dimension is programmed, not to whether that dimension already includes the necessary shrinkage allowance.

## Matchplate coordination checklist

1. Confirm each individual pattern's own dimensional accuracy per its shrink-rule-compensated target.
2. Measure and verify spacing/center-to-center distance between all patterns on the plate against the layout specification.
3. Verify consistent orientation across all patterns (no unintended rotation or mirroring).
4. Check gating/runner alignment relative to each pattern's position on the plate.
5. Document coordinated spacing tolerance results separately from individual pattern dimensional results.
6. If any pattern requires rework, re-verify coordination across the full plate afterward, not just the reworked pattern alone.

## Pattern material/volume matching guide (illustrative — always confirm with foundry engineering)

| Anticipated production volume | Typical pattern material/construction |
|---|---|
| Under 500 units | Wood, or 3D-printed pattern |
| 500-5,000 units | Reinforced wood, or basic plastic/resin pattern |
| 5,000-50,000 units | Machined aluminum or plastic (durable, matchplate-compatible) |
| Over 50,000 units | Machined steel or hardened aluminum, matchplate, with periodic re-verification schedule |

**Rule:** always confirm with foundry engineering what pattern material/construction actually suits the specific volume and casting requirements — this table is illustrative, not a substitute for a project-specific tooling investment decision.
