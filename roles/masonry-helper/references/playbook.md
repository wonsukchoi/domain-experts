# Masonry Helper Playbook

Filled templates for take-off, batching, and site conditions. Populate with the day's real numbers — don't work from the blank column headers.

## Unit take-off and coverage rates

| Unit | Nominal size | Coverage rate | Notes |
|---|---|---|---|
| Standard modular brick | 3 5/8" x 2 1/4" x 8" | 6.75 units/sq ft | 3/8" joints, running bond |
| Standard CMU | 8" x 8" x 16" | 1.125 units/sq ft | 8"x16" face module, 3/8" joints |
| Half-high CMU | 4" x 8" x 16" | 2.25 units/sq ft | Common for veneer/screen walls |
| Norman brick | 3 5/8" x 2 1/4" x 12" | 4.5 units/sq ft | Longer unit, same joint width |

**Take-off formula:** wall area (sq ft) × coverage rate = net units. Add 5% waste for straight runs, 8–10% for walls with corners, openings, or cut courses. Round up to whole units for ordering.

Example: 90 lf × 2 ft height = 180 sq ft × 1.125 = 202.5 net CMU → × 1.05 waste = 212.6 → order 213.

## Mortar bag-yield table (full-bed coverage, 80-lb bags)

| Unit | Units per bag | Bags for 1,000 units |
|---|---|---|
| Standard modular brick | 36 | 27.8 → 28 bags |
| Standard 8"x8"x16" CMU (full bed) | 15 | 66.7 → 67 bags |
| Standard 8"x8"x16" CMU (face-shell only) | 27 | 37.1 → 38 bags |
| Norman brick | 30 | 33.3 → 34 bags |

Full bedding is required below grade and on structural/reinforced CMU cells per most specs; face-shell bedding is standard for above-grade non-structural block — confirm which the spec calls for before batching, the yield nearly doubles between the two.

## Batch-scheduling template (staggered)

1. Compute combined mason course rate (units/hr) from the day's target ÷ effective laying-window hours.
2. Compute one batch's placement time: (units per batch ÷ course rate) × 60 = minutes.
3. Set next-batch trigger = current batch start + (placement time − 20 min buffer).
4. Repeat until total bags for the day are scheduled.
5. Log actual mix time for every batch — this is the retemper/discard clock, not a formality.

| Batch | Bags | Mix start (min from shift start) | Placement time (min) | Done (min) |
|---|---|---|---|---|
| 1 | 3 | 60 | 76 | 136 |
| 2 | 3 | 116 | 76 | 192 |
| 3 | 3 | 172 | 76 | 248 |
| 4 | 3 | 228 | 76 | 304 |
| 5 | 3 | 284 | 76 | 360 |

If a stoppage occurs mid-window, shift every subsequent batch's start by the stoppage length — don't recompute from the original plan, the delay is additive, not compounding, as long as no batch was already past its 150-min working-life window when the stoppage began.

## Retemper / discard decision table

| Batch age at check | Workability | Action |
|---|---|---|
| < 90 min | Stiff but workable | Place as-is |
| 90–150 min | Stiffened, won't spread | Retemper once — add water, re-mix on board |
| 150 min, already retempered once | Stiff again | Discard — do not retemper twice |
| > 150 min, never retempered | Any | Discard — window closed regardless of retemper history |

## Scaffold duty-rating reference (OSHA 1926.451)

| Duty class | Load capacity | Typical use |
|---|---|---|
| Light duty | 25 psf | Material staging, mason working with hand tools only |
| Medium duty | 50 psf | Mason plus mortar/board stock on the platform |
| Heavy duty | 75 psf | Block/stone stockpiled directly on planks |

Default to light-duty assumption when the rating isn't posted on the scaffold tag — confirm with the erecting crew before loading beyond it.

## Cold-weather protocol (below 40°F trending)

1. Heat mix water to 70–120°F (never above 160°F — flash-sets the mortar) before batching.
2. Cover sand stockpiles to keep them frost-free; thaw before batching if frozen.
3. Cover completed courses with insulating blankets at the end of each work period, not just overnight.
4. Extend the working-life check — cold mortar stiffens slower but gains strength slower too; don't read "still workable" as "cured enough" for early bracing removal.

## Silica control quick-reference (OSHA Table 1)

| Task | Control |
|---|---|
| Walk-behind masonry saw | Continuous water at the blade, or vacuum with ≥25 cfm/blade dust collector |
| Handheld grinder (no water) | Vacuum dust collection + HEPA filter, or full-face respirator + wet method |
| Mortar removal/tuckpointing | Dust collection shroud + HEPA vacuum, or wet method |

Never dry-cut unshrouded, even for a single cut — the exposure standard applies per task, not per duration.
