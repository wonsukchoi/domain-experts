# Financial planning artifacts — templates with real structure

Filled templates for a hypothetical household: married couple, both 58, retiring at 62, $1.4M portfolio, $90,000/yr target spending (see SKILL.md worked example for the full reasoning). All figures in today's real dollars unless noted.

## 1. Probability-of-success table (Monte Carlo output)

Run at the planning meeting and at every annual review. Compares the current plan against two candidate changes, holding everything else constant.

| Scenario | Retirement age | Annual spending | Success probability (30-yr horizon) | Median ending balance | 10th-percentile ending balance |
|---|---|---|---|---|---|
| Current plan (SS at 62, straight 4% draw) | 62 | $90,000 | 78% | $1.6M | $0 (depleted ~year 24) |
| Delay SS to 70, bridge from portfolio | 62 | $90,000 | 91% | $2.1M | $310,000 |
| Delay SS to 70 + guardrail spending rule | 62 | $90,000 (adjustable ±10%) | 96% | $2.3M | $540,000 |
| Retire at 64 instead | 64 | $90,000 | 95% | $2.4M | $480,000 |

**Reading it like an advisor:** success probability alone doesn't rank the options — the 10th-percentile ending balance shows how bad the bad case actually is, and the "retire at 64" option buys a similar improvement to "delay SS + guardrail" without giving up two working years being the only lever considered. Present the client with the ranked list of levers (spending flexibility, delay, work longer) and let them choose which one they'd rather pull, don't default to the retirement-age answer because it's the easiest to model.

## 2. Investment Policy Statement (excerpt, filled)

**Household:** [Client names]. **Purpose:** fund retirement income beginning age 62, target $90,000/yr real spending, with a secondary goal of leaving a residual estate to two adult children.

**Target allocation (post-retirement, blended across all accounts):**

| Asset class | Target % | Rebalance band | Vehicle / location |
|---|---|---|---|
| U.S. total market equity | 35% | ±5% | Taxable + Roth IRA (tax-efficient, low turnover) |
| International developed/emerging equity | 15% | ±5% | Taxable (foreign tax credit eligible) |
| Investment-grade taxable bonds | 20% | ±5% | Traditional 401(k)/IRA (tax-inefficient interest shielded) |
| Municipal bonds | 15% | ±3% | Taxable (tax-exempt interest justifies the location) |
| Cash / short-term (bridge reserve) | 15% | ±5%, minimum 2 years of essential spending | Money market / T-bill ladder |
| Real estate (paid-off home, excluded from investable total) | — | — | Not rebalanced; illiquid |

**Withdrawal rule:** initial rate 4.0% of investable assets at retirement start, adjusted per Guyton-Klinger guardrails — cut planned spending 10% if the trailing withdrawal rate exceeds 4.8% (20% above target) at an annual review; raise spending 10% if it falls below 3.2% (20% below target). No adjustment applied for single-year market moves alone.

**Rebalancing trigger:** any asset class outside its band at a quarterly check, or annually regardless. Rebalance using new contributions/withdrawals first before selling appreciated positions, to minimize realized gains.

**Review cadence:** annual, plus immediately upon: job loss, inheritance or windfall exceeding 10% of net worth, a market move beyond ±15% from the prior review, a change in tax law affecting bracket thresholds or RMD rules, or a health diagnosis materially affecting life expectancy for either spouse.

## 3. Social Security claiming comparison

| Claim age | Husband PIA-adjusted (mo/yr) | Wife PIA-adjusted (mo/yr) | Combined annual | Notes |
|---|---|---|---|---|
| 62 (both) | $1,820 / $21,840 | $980 / $11,760 | $33,600 | 30% reduction each (60 months early at FRA 67); survivor benefit locked at reduced level |
| 67 (FRA, both) | $2,600 / $31,200 | $1,400 / $16,800 | $48,000 | No reduction, no credit |
| 70 (both) | $3,224 / $38,688 | $1,736 / $20,832 | $59,520 | 24% delayed credit (8%/yr × 3 years past FRA) |
| **70 (husband only, wife at 67)** | $3,224 / $38,688 | $1,400 / $16,800 | $55,488 | Middle path if bridge funding is tight — still locks in the higher survivor benefit |

**Recommendation logic:** rank by (a) survivor-benefit floor secured, then (b) combined lifetime guaranteed income, then (c) bridge-funding feasibility from the portfolio. The husband's claim is prioritized for delay in every scenario here because it sets the survivor floor; the wife's claim age is the flexible lever if bridge funding is tight.

## 4. Retirement income "bucket" schedule

Three buckets, funded at the retirement date, each with a distinct role and risk-taking permitted:

| Bucket | Time horizon | Funded amount | Holdings | Refill rule |
|---|---|---|---|---|
| 1 — Bridge/near-term | Years 1–2 of retirement | $180,000 (2 × $90,000) | Cash, T-bills, short-term bonds | Refilled from Bucket 2 at each annual review, only if Bucket 2 is above its target band |
| 2 — Intermediate | Years 3–10 | $450,000 (5 × $90,000, less overlap with guaranteed income phase-in) | Intermediate bonds, dividend equity, 40/60 mix | Refilled from Bucket 3 gains during up years; never sold down during a >10% equity drawdown |
| 3 — Growth | Years 10+ | Remainder (~$1.17M at retirement) | 80/20 equity-tilted, global diversified | Source of refills for Buckets 1–2; rebalanced on the standard IPS bands |

**Rule that matters most:** Bucket 1 is drawn down first and refilled only from gains, never by selling Bucket 3 during a drawdown. This is the mechanical version of "don't sell equities in a down market to fund this year's spending" — stated as a rule the client can verify was followed, not a promise to remember it under pressure.

## 5. Tax-loss harvesting log entry (example)

| Date | Account | Security sold | Loss realized | Replacement bought | Wash-sale check | Offset applied |
|---|---|---|---|---|---|---|
| 2024-11-14 | Taxable brokerage | Total International Stock Index Fund | ($8,200) | Different international index fund (not "substantially identical") tracking a different benchmark | Checked: no purchase of the sold fund or a substantially identical one in this account, the spouse's account, or either party's IRA/401(k) within 30 days before or after | Applied first against $5,100 in realized gains from a separate rebalancing trade; remaining ($3,100) carried to offset up to $3,000 of ordinary income this year, $100 carried forward |

**Process note:** the wash-sale check must cover every account the household owns, including a spouse's IRA and workplace 401(k) — Revenue Ruling 2008-5 disallows the loss if the taxpayer repurchases inside their own IRA within the window, even though it's a different account than the one where the loss was realized.
