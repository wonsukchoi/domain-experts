# Modeling artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Sensitivity table (filled — see Worked example in SKILL.md, sales channel investment)

| Close rate | CAC $1,800 | CAC $2,200 (base) | CAC $2,600 |
|---|---|---|---|
| 18% (downside) | 22 months | 27 months | 34 months |
| 24% (base) | 15 months | 18 months | 22 months |
| 30% (upside) | 11 months | 13 months | 16 months |

**Reading it:** payback swings from 11 to 34 months across plausible ranges of just two assumptions — this is why the pitch's single "18 months" number needs the range attached, and why close rate and CAC (not the assumptions that were easiest to source) get the most diligence.

## 2. Downside case derivation (filled example)

| Metric | Pitch assumption | Company's actual historical range (comparable channel) | Downside case used |
|---|---|---|---|
| CAC | $2,200 | $1,900-$2,600 over trailing 8 quarters | $2,600 (worst actual, not an arbitrary -20%) |
| Close rate | 24% | 16%-27% over trailing 8 quarters | 18% (near worst actual, not an arbitrary haircut) |
| Average deal size | $8,400 | $7,100-$9,200 over trailing 8 quarters | $7,400 |

**Rule applied:** the downside case is derived from the worst actual historical performance in a comparable channel, not an arbitrary uniform percentage discount applied to the base case.

## 3. Variance decomposition (filled example)

| Component | Amount | Direction | Explanation |
|---|---|---|---|
| Volume | +$120,000 favorable | Units sold above budget | Strong Q3 demand, not a pricing/mix issue |
| Price | −$340,000 unfavorable | Realized price below budget | Competitive discounting in the enterprise segment |
| Mix | −$80,000 unfavorable | More low-margin SKUs sold | Shift toward entry-tier product |
| One-time | −$100,000 unfavorable | Warranty provision | Non-recurring, excluded from run-rate trend |
| **Total variance** | **−$400,000 unfavorable** | | |

**Rule applied:** the corrective action differs by driver — price erosion (largest component) triggers a pricing/discounting policy review, while the one-time warranty item is excluded from any run-rate corrective action since it won't recur.

## 4. Cash vs. profit reconciliation (filled — see Worked example in SKILL.md, SaaS quarter)

| Line | Amount |
|---|---|
| GAAP net income | +$400,000 |
| Less: AR growth (customers invoiced, not yet collected) | −$650,000 |
| Less: capitalized sales commissions (cash paid, expensed over time) | −$220,000 |
| Less: deferred implementation costs (cash paid, recognized over time) | −$130,000 |
| Plus: non-cash items (depreciation, stock comp) | +$0 (not material this quarter) |
| **Operating cash flow** | **−$600,000** |

**Rule applied:** the reconciliation traces the full gap between net income and cash flow to specific line items (AR growth, capitalized costs) rather than treating the divergence as unexplained or as evidence one number is "wrong."
