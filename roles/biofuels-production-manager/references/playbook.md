# Production playbook

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Daily spread tracking

| Date | Corn cost (blended) | Ethanol price | DDGS price | Revenue/bu | Cost/bu | Margin/bu |
|---|---|---|---|---|---|---|
| Day 1 (pre-spike) | $4.50 | $2.10/gal | $180/ton | $7.41 | $5.85 | $1.56 |
| Day 8 (spike, unhedged case) | $5.80 | $2.10/gal | $180/ton | $7.41 | $7.15 | $0.26 |
| Day 8 (spike, 40% hedged actual) | $5.32 blended | $2.10/gal | $180/ton | $7.41 | $6.67 | $0.74 |

Revenue/bu = (2.80 gal × ethanol price) + (0.0085 ton × DDGS price). Cost/bu = corn cost + $1.35/bu other variable (energy, enzyme, chemicals).

## 2. Throughput decision worksheet (filled — see Worked example in SKILL.md for full narrative)

| Throughput | Yield (gal/bu) | Variable cost/bu | Blended corn cost/bu | Margin/bu | Daily volume | Daily margin |
|---|---|---|---|---|---|---|
| Current: 300,000 bu/day | 2.80 | $1.35 | $5.32 | $0.74 | 300,000 bu | +$222,000 |
| Proposed +8%: 324,000 bu/day | 2.75 | $1.62 | $5.39 | −$0.10 | 324,000 bu | −$32,400 |

**Decision rule applied:** reject a throughput increase when it flips per-unit margin negative, regardless of the volume gain — a negative margin at higher volume is a larger loss, not a smaller one.

## 3. Feedstock quality response matrix

| Measured characteristic | Out-of-spec threshold | Process adjustment |
|---|---|---|
| Moisture | >16% (vs. 14% target) | Increase dryer residence time; reduce grind rate 3-5% until moisture normalizes |
| Oil/starch content | <58% starch (vs. 60% target) | Increase enzyme dosing by ~8-10%; re-test yield after 2 batches |
| Contaminant (foreign material) | >3% by weight | Route lot to secondary cleaning before intake; do not blend into main feedstock stream undiluted |
| Storage-related spoilage indicators | Any detected mycotoxin above regulatory threshold | Reject lot for food/feed-grade co-product stream; route to alternate use or reject entirely per protocol |

## 4. Co-product management scorecard

| Co-product | Quality spec tracked | Target buyer segment | Realized price vs. best-available market price |
|---|---|---|---|
| DDGS (distillers grains) | Protein %, fat %, moisture | Dairy/feedlot premium buyers (higher protein spec) | $180/ton realized vs. $185/ton best-available — $5/ton gap flagged for next contract renewal |
| CO2 (captured) | Purity % | Beverage-grade CO2 buyers (if purity meets spec) vs. industrial-grade | Currently sold industrial-grade at $28/ton; beverage-grade spec would command ~$45/ton — capital case for purification under review |

## 5. Hedge ratio and policy-dependency tracker

| Exposure | Current hedge ratio | Instrument | Residual unhedged exposure |
|---|---|---|---|
| Feedstock (corn) | 40% | Forward contract at $4.60/bu | 60% (180,000 bu/day) exposed to spot |
| Product (ethanol) | 0% | — | 100% exposed to spot ethanol price |
| Fuel credit value (RIN/LCFS) | 0% | — | 100% exposed to credit market and policy risk |

**Policy scenario check (for any capital decision with a payback period >3 years):** model the project's payback under (a) current incentive levels, and (b) a stated downside scenario (e.g., 25% reduction in credit value) — proceed only if the decision still clears an acceptable return threshold under the downside case, not only the current-policy case.
