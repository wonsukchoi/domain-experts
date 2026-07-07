# Economist — Artifacts

## Elasticity memo (filled)

**Question:** Revenue impact of a proposed 10% price increase ($20 → $22/month, 100,000 active users).

| Input | Value |
|---|---|
| Baseline users | 100,000 |
| Baseline price | $20.00 |
| Baseline revenue | $2,000,000/mo |
| Proposed price | $22.00 (+10%) |
| Estimated elasticity | -1.2 (95% CI: -1.5 to -0.9) |
| Method | Difference-in-differences, 42 treated metros vs. matched controls, 6-month pre-trend confirmed parallel |

| Scenario | %ΔQ | New users | New revenue | Δ Revenue |
|---|---|---|---|---|
| Lower bound (elasticity -0.9) | -9.0% | 91,000 | $2,002,000 | +0.1% |
| Point estimate (elasticity -1.2) | -12.0% | 88,000 | $1,936,000 | -3.2% |
| Upper bound (elasticity -1.5) | -15.0% | 85,000 | $1,870,000 | -6.5% |

**Segment decomposition:** bottom price-sensitivity quartile (elasticity -2.1) vs. remaining 75% (elasticity -0.85, re-estimated excluding that quartile).

| Segment | Users | Elasticity | %ΔQ | New revenue | Δ vs. baseline share |
|---|---|---|---|---|---|
| Bottom quartile (excluded from increase) | 25,000 | -2.1 | — (price held) | $500,000 | 0.0% |
| Remaining 75% (price increased) | 75,000 | -0.85 | -8.5% | $1,509,000 (68,625 × $22) | +0.6% |
| **Segmented total** | 100,000 | — | — | **$2,009,000** | **+0.4%** vs. blended -3.2% |

## Difference-in-differences specification table (filled)

| Check | Result | Pass/fail |
|---|---|---|
| Pre-period parallel trends (6 mo, treated vs. control) | Slope difference 0.03pp/mo, not significant (p=0.71) | Pass |
| Placebo test (fake treatment date, 6 mo before actual) | Estimated effect -0.4%, not significant (p=0.62) | Pass |
| Alternate control group (next-tier metros instead of matched) | Elasticity -1.15 (within CI of primary -1.2) | Pass — robust |
| First-stage strength (if IV used) | N/A — DiD, no instrument | — |
| Clustered SE (by metro, 42 clusters) | Used; naive OLS SE would understate by ~35% | Applied |

## Cost-benefit worksheet (skeleton, filled with the pricing case)

| Line item | Value | Basis |
|---|---|---|
| Expected revenue Δ (blended) | -$64,000/mo | Point estimate scenario |
| Expected revenue Δ (segmented) | +$9,000/mo | Segmented scenario |
| Estimated churn-driven support cost avoided (segmented vs. blended) | +$3,200/mo | Historical churn-ticket cost ($40/churned user × ~80 fewer churns) |
| Implementation cost (segmentation logic, one-time) | -$18,000 | Engineering estimate, amortized over 12 mo = -$1,500/mo |
| **Net monthly benefit, segmented vs. blended increase** | **+$74,700/mo** | Sum of above |
