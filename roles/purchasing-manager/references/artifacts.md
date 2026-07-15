# Sourcing decision artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Single-vs-multi-source risk analysis (filled — see Worked example in SKILL.md for full narrative)

| Option | Annual cost | Premium vs. single-source | Expected residual disruption cost | Total annual cost |
|---|---|---|---|---|
| Single-source only | $9,000,000 | — | $460,000 (5% × $9.2M) | $9,460,000 |
| Full dual-source (70/30) | $9,945,000 | $945,000 | ~$0 (backup fully independent) | $9,945,000 |
| Hybrid (90/10) | $9,250,000 | $250,000 | $100,000 (5% × $2M, faster backup scale-up) | $9,350,000 |

**Reading it:** the hybrid option has the lowest total annual cost once both the guaranteed premium and the expected residual risk are counted — full dual-sourcing over-corrects (paying more than the risk is worth), while pure single-sourcing under-protects.

## 2. Total cost of ownership model (filled example)

| Factor | Supplier A | Supplier B |
|---|---|---|
| Unit price | $18.00 | $19.50 |
| Defect rate | 2.1% | 0.7% |
| Rework cost per defect | $45 | $45 |
| Rework cost per unit (defect rate × cost) | $0.95 | $0.32 |
| On-time delivery rate | 91% | 98% |
| Estimated cost of late delivery (expediting, line stoppage) per unit | $0.60 (9% × avg cost) | $0.12 (2% × avg cost) |
| **Effective TCO per unit** | **$18.00 + $0.95 + $0.60 = $19.55** | **$19.50 + $0.32 + $0.12 = $19.94** |

**Reading it:** Supplier A's TCO ($19.55) is actually lower than Supplier B's ($19.94) despite B's better quality/delivery metrics, once the actual defect and delivery cost impact is quantified rather than assumed — the numbers, not the qualitative reputation, should decide it.

## 3. Supplier risk monitoring log (filled example)

| Supplier | Last full risk assessment | Financial health check | Geographic exposure | Trigger for reassessment |
|---|---|---|---|---|
| Primary sensor supplier | 8 months ago | Stable, no flags | Single-region (moderate geopolitical exposure) | Ownership change, credit rating change, or 12-month elapsed |
| Secondary sensor supplier (newly qualified) | At qualification, 2 months ago | Stable | Different region (diversifies geographic exposure) | 12-month elapsed or capacity change |

**Rule applied:** reassessment is triggered by specific events (ownership change, credit rating shift) or a fixed time elapsed, not left open-ended until a disruption forces an unplanned review.

## 4. Category segmentation (Kraljic-style, filled example)

| Category | Criticality | Supply market complexity | Sourcing strategy |
|---|---|---|---|
| Critical sensor component | High | High (few qualified suppliers) | Strategic — hybrid sourcing, deep relationship management, ongoing risk monitoring |
| Standard packaging materials | Low | Low (many suppliers) | Non-critical — competitive bidding, minimal relationship overhead |
| Specialized software license | High | Low (single vendor, but low disruption consequence) | Bottleneck — negotiate strong contract terms, monitor vendor health |
| Office supplies | Low | Low | Non-critical — standard procurement, no special treatment |

**Rule applied:** sourcing strategy differs by quadrant — the critical sensor component gets the most relationship investment and risk monitoring, while office supplies get a minimal, standardized approach.
