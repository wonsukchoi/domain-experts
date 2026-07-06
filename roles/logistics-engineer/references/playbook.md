# Logistics Engineer — Playbook

## Facility-count total cost comparison (filled example)

| Cost component | 1 DC (current) | 2 DC (proposed, East/West split) |
|---|---|---|
| Facility fixed cost | $2,200,000 | $4,000,000 (two facilities, duplicated overhead) |
| Outbound freight cost | $8,400,000 | $5,600,000 (33% reduction, closer to regional customers) |
| Inventory carrying cost | $1,800,000 (pooled) | $2,600,000 (44% increase, pooling-effect loss) |
| **Total** | **$12,400,000** | **$12,200,000** |
| **Net difference** | | **−$200,000/year (~1.6% savings)** |

**Use:** Always model all three cost components together — the freight savings alone ($2.8M) looks compelling, but the combined fixed-cost increase ($1.8M) and inventory carrying cost increase ($0.8M) offset most of it, leaving only a modest net benefit.

## Center-of-gravity model validation checklist

1. Calculate the demand-weighted centroid based on customer locations and volumes.
2. Identify the resulting search area (not a single point) accounting for model sensitivity to demand data assumptions.
3. Within that search area, identify actual candidate sites with available real estate.
4. Validate each candidate against: real road network distance (not straight-line), labor market depth, transportation infrastructure (highway/rail access), and zoning.
5. Only after this validation should a specific site be treated as a viable recommendation.

## ABC/velocity-based slotting plan (illustrative structure)

| Classification | Pick frequency | Slotting priority |
|---|---|---|
| A (fast-movers) | Top 20% of SKUs by pick volume, ~70-80% of total picks | Closest to pack/ship station, ground-level, easy-access locations |
| B (medium-movers) | Next 30% of SKUs, ~15-20% of total picks | Mid-distance, standard shelving |
| C (slow-movers) | Remaining 50% of SKUs, ~5-10% of total picks | Farthest locations, upper shelving/less accessible |

**Use:** Reslot based on actual current pick-velocity data, not the original layout assumptions — velocity rankings shift as product mix changes, and a slotting plan that's a year or more stale is likely misaligned with current demand patterns.

## Peak-demand capacity sizing worksheet (illustrative structure)

| Metric | Value |
|---|---|
| Average daily demand | 8,000 units |
| Historical peak daily demand (e.g., holiday season) | 11,000 units |
| Stated service-level buffer | 15% above historical peak |
| **Capacity sizing target** | 11,000 × 1.15 ≈ **12,650 units/day** |

**Use:** Size equipment, labor, and throughput capacity against this peak-plus-buffer figure, not average daily demand — sizing to the 8,000-unit average would leave the facility unable to handle the actual peak-season volume without costly overtime or missed service levels.

## Network design findings memo — filled example

> **Facility Count Analysis — 1 DC vs. 2 DC Network**
> 1 DC total cost: $12,400,000/year (fixed $2.2M + freight $8.4M + inventory carrying $1.8M).
> 2 DC total cost: $12,200,000/year (fixed $4.0M + freight $5.6M + inventory carrying $2.6M).
> **Net savings from adding a second DC: $200,000/year (~1.6%)** — a modest improvement once fixed cost duplication and inventory pooling-effect loss are included, not the larger gain the freight reduction alone would imply.
> **Recommendation: The 2-DC option is marginally favorable on cost; validate the proposed regional split's center-of-gravity search areas against real road distances, available real estate, and labor market conditions before committing, and reassess if freight rates or fixed cost estimates change materially.**
