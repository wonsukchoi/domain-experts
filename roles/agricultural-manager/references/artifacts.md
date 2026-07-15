# Farm planning artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Enterprise budget (per acre)

| Line item | Corn | Soybeans |
|---|---|---|
| Expected yield | 180 bu/acre | 50 bu/acre |
| Forecast price | $5.20/bu | $12.00/bu |
| Gross revenue | $936 | $600 |
| Seed | $130 | $75 |
| Fertilizer | $220 | $60 |
| Chemicals | $70 | $55 |
| Fuel/machinery | $115 | $105 |
| Land (cash rent) | $250 | $250 |
| Insurance/other | $50 | $40 |
| **Total cost** | **$835** | **$585** |
| **Margin per acre** | **$101** | **$15** |

Note: this is the fully-loaded (including land) budget, distinct from the variable-cost-only margin used in the diversification stress test — used for the "is this ground worth farming at all this year" question rather than the marginal planting-mix question.

## 2. Break-even worksheet

**Corn, 2,000-acre operation, variable + fixed cost of $650/acre (excludes land):**

| Scenario | Yield | Price | Revenue/acre | Cost/acre | Margin/acre |
|---|---|---|---|---|---|
| Forecast case | 180 bu | $5.20 | $936 | $650 | $286 |
| Conservative case | 165 bu | $4.60 | $759 | $650 | $109 |
| Break-even price at forecast yield | 180 bu | $3.61 | $650 | $650 | $0 |
| Bad-corn stress case | 120 bu | $4.00 | $480 | $650 | −$170 |

**Reading it:** the operation clears a profit down to $3.61/bu at forecast yield — a meaningful cushion versus the current $5.20 futures price, but the bad-yield stress case shows that a simultaneous yield and price miss (not just one or the other) is what actually produces a loss.

## 3. Diversification stress-test (filled — see Worked example in SKILL.md for full narrative)

| Mix (corn/soy acres) | Forecast-case total margin | Bad-corn-scenario total margin | % of $550,000 cushion consumed in bad scenario |
|---|---|---|---|
| 1,200 / 800 (current) | $487,200 | −$60,000 | 11% |
| 1,500 / 500 (compromise) | $519,000 | −$165,000 | 30% |
| 1,800 / 200 (proposed) | $550,800 | −$270,000 | 49% |

**Decision rule applied:** reject the mix whose downside exceeds ~35-40% of total cushion unless the upside gap over the next-best option is large enough to justify it. Here the upside gap between compromise and proposed ($31,800) doesn't justify the downside gap (19 additional points of cushion exposure) — compromise wins.

## 4. Hedging/marketing plan template (filled)

| Marketing step | % of expected production | Instrument | Price/terms locked |
|---|---|---|---|
| Pre-plant | 40% | Forward contract | $5.00/bu |
| Pre-plant | 20% | Put option (floor) | $4.75/bu floor, premium $0.18/bu |
| Growing season, if price rallies | up to 20% more | Forward contract, opportunistic | Target $5.25+/bu |
| Unpriced at harvest (residual) | remaining ~20% | Cash sale or storage | Priced at harvest based on basis/carry |

**Rule applied:** never leave 100% unpriced going into harvest on a crop where the operation is a price-taker; the specific split (60/40, 70/30, etc.) is sized to the operation's break-even and cushion, not a fixed rule.

## 5. Input marginal-return check (filled example)

| Nitrogen rate | Yield | Marginal yield vs. prior rate | Marginal revenue (@ $5.20/bu) | Marginal N cost | Marginal return |
|---|---|---|---|---|---|
| 140 lb/acre | 165 bu | — | — | — | — |
| 160 lb/acre | 172 bu | +7 bu | +$36.40 | $9.00 | +$27.40 |
| 180 lb/acre | 176 bu | +4 bu | +$20.80 | $9.00 | +$11.80 |
| 200 lb/acre | 178 bu | +2 bu | +$10.40 | $9.00 | +$1.40 |
| 220 lb/acre | 179 bu | +1 bu | +$5.20 | $9.00 | **−$3.80** |

**Reading it:** the 220 lb/acre rate produces the single highest total yield in the table, but it's the wrong choice — marginal return goes negative between 200 and 220 lb/acre. The profit-maximizing rate is around 200 lb/acre, where marginal return is still positive but thin, not the yield-maximizing 220 lb/acre.
