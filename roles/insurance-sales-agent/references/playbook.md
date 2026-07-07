# Insurance Sales Agent — Playbook

## Needs-analysis worksheet (life insurance, income-replacement + DIME components)

| Line item | Formula | Example value |
|---|---|---|
| Income replacement | Annual income × 8-12 (years-of-support multiplier, longer for younger dependents) | $85,000 × 10 = $850,000 |
| Debt payoff | Sum of mortgage + other outstanding debt | $310,000 + $28,000 = $338,000 |
| Education/future obligations | Per-child estimate × number of children | $60,000 × 2 = $120,000 |
| **Gross need** | Sum of above | $1,308,000 |
| Less: liquid assets | Savings, existing coverage, other liquid investments | −$40,000 |
| **Net coverage need** | Gross need − liquid assets | $1,268,000 |

Multiplier selection: 8x for dependents near independence (college-age or older), 10x for mid-range (elementary/middle-school-age dependents), 12x for very young dependents where the replacement horizon is longest. State the multiplier chosen and why — it is the single most consequential assumption in the calc and the one most worth defending to the client.

## Matched-terms carrier comparison table

| Comparison axis | Carrier A | Carrier B | Carrier C |
|---|---|---|---|
| Coverage amount | $1,250,000 | $1,250,000 | $1,250,000 |
| Term length | 20 years | 20 years | 20 years |
| Monthly premium (quoted) | $89.40 | $84.15 | $97.20 |
| Required riders for client profile | None | Aviation rider, +$6.00/mo | None |
| **True comparable premium** | **$89.40** | **$90.15** | **$97.20** |
| Notable exclusions | Standard | Aviation excluded without rider | None additional |
| Included riders | None | None | Accelerated death benefit |

Rule: never rank carriers on the quoted-premium column alone. Add required riders to reach the "true comparable premium" row before ranking.

## Replacement-cost comparison (when a client wants to swap an in-force policy)

| Factor | Existing policy | New policy | Client impact |
|---|---|---|---|
| Cash value accumulated | $14,200 | $0 (day one) | Immediate loss if surrendered |
| Surrender charge if cancelled now | $3,100 (year 4 of 7-year schedule) | N/A | Direct cost of switching |
| Contestability clock | Cleared (year 4, past 2-year mark) | Resets to day one | 2 years of claim-contest risk re-opens |
| Premium | $145/mo | $89/mo | $56/mo savings |
| Breakeven on premium savings vs. switching cost | ($3,100 + $14,200) / $56 ≈ 309 months (25.8 years) | — | Switching cost not recovered within any realistic policy horizon |

This is the standard trap: a lower monthly premium on paper almost never clears the combined surrender-charge-plus-forfeited-cash-value hurdle within a useful time horizon. Run this table before recommending any replacement, and put the breakeven number in front of the client explicitly.

## Objection-handling script fragments (filled, not templated)

**"Why is this quote higher than the online calculator said?"**
"The online number is a rate-table estimate before underwriting looks at your specific health history and driving record. Once we submit the application, the carrier's underwriter assigns you a risk class — Preferred, Standard, or a rated class — based on your exam results. I quoted you at Standard, which is the middle of the range; if your exam comes back better than that, the premium can come down, and if it comes back worse, it can go up. I'll flag it immediately either way so there's no surprise at binding."

**"Can't I just get the cheapest policy?"**
"I can quote you the cheapest policy at whatever coverage amount you want — but let's separate two things: how much coverage you need, and how cheap we can make it. Based on your income and debts, the number that actually replaces what your family would lose is about $1.27 million. If you want to cap the premium at a specific dollar amount instead, tell me the number and I'll show you exactly how much coverage that buys and what gap it leaves — that's a real tradeoff you're choosing with full information, not a guess."
