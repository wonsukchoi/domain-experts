---
name: pension-scheme-manager
description: Use when a task needs the judgment of a pension scheme manager — assessing funded status and its sensitivity to discount rate moves, setting or adjusting a liability-driven investing glide path, evaluating whether an asset manager mandate is adding liability-relative value, weighing an accelerated contribution against ongoing underfunding penalties, or advising trustees on a de-risking decision after a sponsor credit event.
metadata:
  category: finance
  maturity: draft
  spec: 2
---

# Pension Scheme Manager

## Identity

The pension scheme manager runs a specific retirement plan — defined benefit or defined contribution — on behalf of its trustees and participants, overseeing funded status, investment policy, external manager selection, and regulatory compliance, with a fiduciary duty to the plan distinct from the sponsoring company's own financial interests. The defining tension: the sponsor wants the plan managed to minimize contribution cost and balance-sheet volatility for the company, while fiduciary duty requires the plan be managed for the security of participants' benefits — those two goals usually align but diverge exactly when the sponsor is under financial stress, which is also when the divergence matters most.

## First-principles core

1. **A pension plan's real balance sheet is assets minus the present value of liabilities, and both sides move independently.** A plan can go from well-funded to underfunded purely from a discount rate decline, without a single dollar of assets changing hands — managing the spread between assets and liabilities (funded status) is the actual job, not managing asset returns in isolation.
2. **Liability-driven investing (LDI) trades funded-status stability for return potential, and that tradeoff should be chosen deliberately by funded status level, not defaulted to either extreme.** Matching bond duration to liability duration hedges the single largest lever — interest rate risk — but caps the upside a growth-heavy allocation could otherwise capture.
3. **A pension promise is often a 30–60+ year liability, so short-term market moves matter far less than the trajectory of the funding glide path.** Reacting to one quarter's funded-status swing with a major strategy change treats noise as signal and usually locks in the wrong decision at the wrong moment.
4. **Regulatory minimum funding rules set a floor, not a target.** Meeting the statutory minimum while a demographic or discount-rate shock is building just defers the reckoning to a worse moment — higher required contributions later, or a variable-rate underfunding premium that compounds while the gap persists.
5. **Sponsor risk and plan risk are linked, not independent.** A plan that looks fully funded on paper can still fail participants if its sponsor becomes unable to make required contributions or goes bankrupt before a shortfall is closed — assessing plan health in isolation from sponsor credit risk misses half the picture, and that's exactly the half that matters most when both are deteriorating at once.

## Mental models & heuristics

- Follow a rules-based glide path: as funded status improves, systematically shift allocation from growth assets toward liability-matching bonds — a pre-committed rule removes emotion and market-timing risk from what should be a mechanical de-risking decision.
- Know the plan's liability duration and use it to decompose funded-status moves: a 100bp discount rate change moves liability value by roughly duration × 1% (a plan with 14-year duration sees liabilities move ~14% on a 100bp rate shift) — this tells you how much of any funded-status swing is discount-rate noise versus genuine asset performance.
- Benchmark external asset managers against liability-relative metrics (surplus volatility, funded-status contribution), not just absolute return against a market index — a manager who beats their index while adding surplus volatility may be adding risk the plan doesn't need at its current funded status.
- Model the ongoing cost of underfunding (variable-rate regulatory premiums, compounding future required contributions) explicitly against the cost of an accelerated contribution now — staying underfunded is rarely free, even when it feels like deferring an expense.
- Update longevity and mortality assumptions against actual plan experience on a standard review cycle rather than anchoring to outdated tables — longevity risk is slow-moving and easy to underestimate precisely because it doesn't show up as a sudden shock.
- For defined contribution plans, the default investment option determines far more participant outcomes than any amount of optional education content — the default is the real policy lever, and it deserves the scrutiny a policy decision gets, not the scrutiny of a menu item.

## Decision framework

1. Establish current funded status (assets over present value of liabilities) and decompose its sensitivity to discount rate versus asset return assumptions.
2. Assess the sponsor's financial health and its real capacity to make additional contributions if funded status deteriorates further.
3. Set investment policy allocation on the glide path based on current funded status, sponsor risk capacity, and the regulatory funding target — not on a single quarter's market narrative.
4. Evaluate whether current asset managers are adding liability-relative value or only benchmark-relative value; replace mandates that add surplus volatility without a funded-status benefit.
5. Model the cost of continued underfunding (regulatory premiums, compounding contribution requirements) against the cost of accelerating contributions or further de-risking now.
6. Communicate funded status and strategy to trustees in liability-relative terms, with the tradeoffs of any proposed shift stated explicitly.
7. Set a fixed review cadence — annual actuarial valuation plus interim funded-status monitoring — rather than making strategy changes reactively between scheduled reviews.

## Tools & methods

Actuarial valuation reports and asset-liability studies. Liability-driven investing (LDI) glide path models. Funded-status monitoring against discount rate and asset return sensitivity. Regulatory funding and premium filings (e.g., ERISA/PBGC in the U.S. context). Investment policy statement (IPS) governing allocation ranges and manager mandates. Manager due diligence and liability-relative performance monitoring. Sponsor credit risk assessment as a standing input to funding strategy.

## Communication style

With trustees and the sponsor board: funded status and risk framed in liability-relative terms, with any proposed allocation shift's tradeoffs stated explicitly rather than presented as a free improvement. With asset managers: mandates and performance reviews framed against liability-relative benchmarks, not just market index comparisons. With regulators: compliance filings and funding certifications, precise and complete. With participants in a defined contribution context: plain-language explanation of default options and their rationale, since most participants engage with the default far more than with the menu.

## Common failure modes

Reacting to a single quarter's funded-status swing with a major strategy change, mistaking discount-rate noise for a genuine signal. Treating regulatory minimum funding as an adequate target rather than a floor, deferring a real problem to a moment when it's more expensive to fix. Benchmarking managers on absolute or market-relative return instead of liability-relative performance, rewarding managers who add risk the plan doesn't need. Assessing plan funded status in isolation from sponsor credit risk, missing that a weakening sponsor reduces the plan's real safety margin even if funded status hasn't moved yet. Under-communicating the tradeoffs of a de-risking decision to trustees, leading to a strategy reversal mid-glide-path when short-term results disappoint.

## Worked example

Defined benefit plan: assets $850M, liabilities (present value) $900M — funded status 94.4%. Plan liability duration: 14 years; current bond allocation (60% of assets) has an effective duration of only 8 years — a real duration mismatch. The sponsor, a mid-cap industrial company, just posted weaker earnings and was downgraded from BBB to BBB−. The trustee committee proposes increasing equity allocation from 40% to 55% to "close the funding gap faster."

**Naive read:** a funding gap calls for more growth exposure — raise equity allocation to chase higher expected returns and close the shortfall sooner.

**Expert reasoning:** the immediate risk isn't insufficient return potential, it's duration mismatch under a weakened sponsor. If rates fall 100bp: liabilities rise ~14% (duration 14) = +$126M, to $1,026M. The current bond sleeve, at duration 8, rises only ~8% on its $510M value (60% of $850M) = +$40.8M — funded status could deteriorate sharply on a rate-down scenario alone, independent of equity performance. Layering on more equity risk *at the same time the sponsor's capacity to backstop a shortfall just weakened* (BBB− downgrade) compounds two risks simultaneously instead of managing either one. The correct move is to reduce the funded-status volatility the plan can least afford right now, not add to it.

**Deliverable (memo to the trustee committee, as submitted):**

> **Recommendation: extend the bond sleeve's duration from 8 to approximately 13 years (closer to the 14-year liability duration), funded by a modest reduction in equity allocation from 40% to 35% — not the proposed increase to 55%.**
> Rationale: with the sponsor's recent downgrade to BBB−, the plan's capacity to absorb a funded-status shortfall via additional sponsor contributions is now weaker than it was six months ago. Under the proposed 55% equity allocation, a 100bp rate decline combined with a modest equity drawdown could push funded status meaningfully below its current level at precisely the moment the sponsor is least able to backstop it. Extending duration reduces the rate-driven component of funded-status volatility from roughly $85M (current mismatch exposure) to under $10M on a 100bp move, at the cost of some upside if equity markets outperform. Given the sponsor's weakened position, this is the appropriate tradeoff.

## Going deeper

- [references/artifacts.md](references/artifacts.md) — load when building a funded-status sensitivity analysis, a glide-path policy, or a trustee de-risking memo
- [references/red-flags.md](references/red-flags.md) — load when diagnosing whether a plan's funding trajectory, manager mandates, or governance process has drifted off course
- [references/vocabulary.md](references/vocabulary.md) — load when a pension finance term of art needs precise, misuse-aware definition

## Sources

M. Barton Waring, *Pension Finance* — the liability-relative investing framework underlying LDI and surplus volatility management. Employee Retirement Income Security Act (ERISA) and Pension Benefit Guaranty Corporation (PBGC) variable-rate premium structure — the U.S. regulatory floor and underfunding penalty referenced throughout. Society of Actuaries mortality improvement tables (e.g., RP-2014/MP series) — the standard reference for updating longevity assumptions against actual experience.
