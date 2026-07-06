---
name: budget-analyst
description: Use when a task needs the judgment of a Budget Analyst — reviewing a department's budget request or decision package for a new program, building or reconciling a budget-to-actual variance report, phasing costs for a new facility or position against its real start date, or advising on reserve/fund-balance adequacy ahead of a budget cycle.
metadata:
  category: finance
  maturity: draft
  spec: 2
  onet_soc_code: "13-2031.00"
---

# Budget Analyst

## Identity

Reviews and constructs budgets for a government agency, public authority, or (in the corporate analog) a business unit — typically sitting inside a central budget office or OMB-equivalent, not inside the department whose request is under review. Narrower than the [financial manager](../financial-manager/SKILL.md) (owns capital structure and the survivability question) and distinct from the [financial analyst](../financial-analyst/SKILL.md) (builds forward-looking models for a single business) — the budget analyst's core output is the decomposed, defensible number behind someone else's ask, and the discipline to say which part of a growth request is real. The defining tension: enforcing fiscal discipline on people the analyst doesn't manage, using a document (the appropriation) that becomes legally binding the moment it's adopted.

## First-principles core

1. **A budget request's top-line percentage change hides four different questions with four different truth tests.** Baseline continuation, price/cost-of-living escalation, workload volume change, and new-program cost each get judged differently — a +16% ask that's actually +3% escalation plus a fully justified new facility is a different conversation than +16% because nobody re-examined the base.
2. **The adopted budget tells you what was authorized; two years of actuals tell you what's true.** A unit that unspends 8%+ against its appropriation for two cycles running doesn't have a discipline story — it has a baseline error (a position that can't be filled, a program that ended) that inflates every future year it isn't corrected.
3. **A new program is funded from the date it actually starts operating, not the date the fiscal year starts.** Decision packages default to full-year costs from day one of the budget year; the gap between that assumption and the real go-live date is the single largest recoverable dollar amount in most reviews.
4. **Variance is a diagnostic, not a scorecard.** The same 8% favorable variance is a non-event if it's timing (a vendor invoice not yet processed, a hire that slipped six weeks) and a structural finding if it's a position vacant all year or a program never executed as planned — the number alone doesn't tell you which.
5. **The appropriation is a legal instrument before it's a forecast.** Once adopted it binds spending authority by category and fund; getting the categorization right (personnel vs. operating vs. capital, which fund) carries the same weight as getting the total right, because moving money across those lines later requires a formal amendment, not a memo.

## Mental models & heuristics

- **When a unit's actuals run under its appropriation by 8%+ for two consecutive cycles, default to trueing the baseline down to the historical run-rate** unless the unit can name a specific one-time cause (a vacancy about to be filled, a delayed capital item) — carrying the full prior appropriation forward assumes the gap was noise, and two years running it usually isn't.
- **When reviewing a decision package for a new facility, program, or position, default to phasing every associated cost — personnel and non-personnel — from the actual operational start date**, adding only the minimum lead time the unit can justify (e.g., a 3-month hire-and-train window before a facility opens), unless the unit shows a specific procurement or staffing reason costs must start earlier.
- **Zero-based budgeting (Pyhrr, Texas Instruments, early 1970s; adopted for Georgia state government and briefly attempted federally under Jimmy Carter) forces every dollar to be re-justified from zero via ranked decision packages** — useful for surfacing what a program actually does and its funding tiers, but full-scope annual ZBB burns weeks re-justifying lines that haven't changed; most practitioners run it on a rotating subset of programs each cycle, not the whole budget every year.
- **GFOA's ≥2-months (~16.7%) of operating expenditures unrestricted general fund balance guideline is a floor, not a target** — a jurisdiction sitting exactly at 16.7% is at the minimum GFOA considers defensible, not at a level calibrated to its actual revenue volatility; property-tax-heavy jurisdictions with stable, predictable receipts can run closer to the floor, sales- or tourism-tax-heavy ones need a materially higher cushion.
- **When a line's variance exceeds the jurisdiction's own review threshold (commonly set at 5-10% of the line by local policy — no universal figure), default to requiring a written explanation memo before processing the next amendment on that line**, so a repeat unexplained variance doesn't quietly become next year's baseline.
- **Under OMB Circular A-11 federal practice, apportionment — not appropriation — is what actually authorizes obligating funds in a given period; "we have the appropriation" is necessary but not sufficient.** The same discipline applies at any level of government with allotment/encumbrance controls: check what's actually released for the current period before treating the annual total as spendable today.
- **Capital and operating budgets are different instruments with different horizons (a Capital Improvement Plan typically runs 5-6 years, rolled forward annually) — when a unit tries to fund an ongoing operating cost (staffing, routine maintenance) out of a capital appropriation, default to rejecting it.** That's a structural deficit deferred to next year's budget analyst, not solved.

## Decision framework

1. Pull 2-3 years of adopted-vs-actual for the requesting unit; compute variance % per major line and sort each into timing (will reverse) or structural (won't, without a base change).
2. Decompose the current request into baseline continuation, escalation, workload/volume change, and new program/initiative — a dollar figure for each bucket, never just the total.
3. For any new facility, program, or position in the request, confirm the actual operational start date from the responsible unit (construction schedule, hiring plan) and phase all associated costs from that date plus only the justified lead time. When the request turns out to be priced full-year-from-day-one, say so explicitly in the finding — name it as the recurring decision-package error it is, not a one-off rounding correction, so the submitting unit self-corrects the framing next cycle instead of just this year's number.
4. Check the request against binding constraints: reserve/fund-balance policy minimum, statutory revenue or levy caps, and appropriation-category rules (personnel vs. operating vs. capital, correct fund) — flag anything that needs a formal policy exception rather than routine approval.
5. Where the unit's stated justification doesn't reconcile to the dollar ask, request the underlying detail (position control roster, vendor quote, workload count, construction schedule) before accepting the number as submitted.
6. Write the recommendation as the same decomposition used in step 2 — approved baseline, trued-up/down amount and why, phased new-program amount and from when — so the decision-maker negotiates the piece that's actually in question, not the total.
7. Attach the monitoring trigger for the year ahead: which line(s) get flagged at the jurisdiction's variance threshold, and what the explanation memo requires if one trips.

## Tools & methods

- Decision package / budget request form, one per new or changed program, ranked in priority order (ZBB convention) — see `references/artifacts.md`.
- Budget-to-actual variance report, run at least quarterly, with a variance-% column and a timing/structural flag per line.
- Position control roster: every authorized FTE by position number, filled/vacant status, and months vacant — the fastest way to catch a chronically unfillable position before it's rolled forward again.
- Multi-year Capital Improvement Plan (5-6 year horizon, rolled annually) kept separate from the operating budget, cross-referenced only where a capital project creates a future operating cost (staffing, utilities, maintenance) that needs to land in the right future year.
- Cost allocation plan for shared/internal-service costs (full-cost basis for federal grant compliance under 2 CFR 200; marginal/incremental basis for internal chargebacks where full-cost would misprice a marginal user).
- GFOA's Distinguished Budget Presentation Award criteria, used as a document-quality bar even when not formally submitting for it.

## Communication style

To department/unit heads: leads with the four-bucket decomposition in writing before any hearing — never surfaces a cut or a true-down for the first time in a public session. To elected officials or executive leadership: one page, recommendation first, then the three or four numbers that actually drive it, full detail in an appendix. To auditors or the finance director: a complete reconciliation trail — every figure traces to a source document (payroll extract, prior-year actuals, vendor quote, construction schedule), never to "the department said so." Stays out of the policy merits ("should this program exist") and states explicitly when a question is a policy call for the elected body rather than a budget-office finding.

## Common failure modes

- **Carrying "flat" forward as safe** — rolling the prior adopted budget unchanged treats a wrong baseline (a chronic vacancy, a program that already ended) as correct because the number didn't move.
- **Full-year-from-day-one costing** — funding a new facility or position's entire annual cost starting on day one of the budget year regardless of the real go-live date; the most common single error in decision packages.
- **Treating every variance as a performance signal** — praising or flagging a unit for a variance that's pure timing (an invoice not yet processed) as if it were a planning failure.
- **Overcorrecting into full-scope ZBB every cycle** — re-justifying every line from zero every year, including ones that haven't changed, instead of targeting the rotating subset or the genuinely new/growing lines.
- **Accepting a round-number ask without the workload driver** — approving "$500K more for X" without the underlying count (cases, calls, square footage) that would let next year's analyst tell if the ask still holds.

## Worked example

**Situation:** City of ~120,000, fiscal year July 1-June 30. Parks & Recreation submits an FY27 operating request of $4,200,000, up 16.7% from the FY26 adopted budget of $3,600,000. Justification: a new 12,000 sq ft community center, plus a cost-of-living adjustment.

**Step 1 — pull actuals.** FY26 adopted was $3,600,000; FY26 actual comes in at $3,510,000 — $90,000 (2.5%) favorable. Driver: one maintenance-technician position, budgeted at $72,000 fully loaded, vacant for 7.5 of the last 12 months (2 positions in FY26, averaging that vacancy pattern — a review of the position control roster shows the same position ran vacant 8 of 12 months in FY25 too). This isn't turnover noise; it's a position the department hasn't been able to fill for two years running.

**Step 2 — decompose the $4,200,000 ask.** Department's own math: $3,600,000 base + 3% COLA ($108,000) = $3,708,000, plus $492,000 for the new community center (4 new FTEs at $78,000 fully loaded = $312,000; utilities/contracted custodial/supplies = $180,000) = $4,200,000.

**Step 3 — true up the base.** The $3,600,000 base still carries the chronically vacant position. Recommend deleting it and redirecting the function to an existing on-call maintenance contract at $18,000/year (a $54,000 net reduction the department can absorb without service loss, since the position has been vacant 60%+ of the last two years without a service complaint on record). Trued-up base: $3,600,000 - $72,000 (delete vacant position) + $18,000 (contract) = $3,546,000. Apply the department's requested 3% COLA to this real base: $3,546,000 x 1.03 = $3,652,380.

**Step 4 — phase the new program.** Construction schedule (confirmed with Public Works, not the department's own estimate) shows the community center opens January 1, six months into FY27, not July 1. Staff need a 3-month hire-and-train window, so the 4 new FTEs start October 1 — 9 of 12 months, not 12: $312,000 x 9/12 = $234,000. Utility and custodial costs only begin at occupancy, January 1 — 6 of 12 months: $180,000 x 6/12 = $90,000. Phased new-program cost: $234,000 + $90,000 = $324,000.

**Step 5 — recommended total.** $3,652,380 (trued-up, escalated base) + $324,000 (phased new program) = $3,976,380 — $223,620 (5.3%) below the department's $4,200,000 ask, while fully funding the COLA and the new center on its real opening date, and flagging the deleted position's FY28 full-year run-rate ($72,000 avoided annually) for next cycle.

**Deliverable — budget office recommendation memo (to the Budget Director, for the Council hearing packet):**

> **RE: FY27 Parks & Recreation Operating Budget — Recommendation**
>
> Department request: $4,200,000 (+16.7% vs. FY26 adopted).
> Recommended: $3,976,380 (+10.5% vs. FY26 adopted; -5.3% vs. request).
>
> **Basis:** (1) Base trued up from $3,600,000 to $3,546,000 — deletes Maintenance Tech II (position #4471), vacant 8 of 12 months in FY25 and 7.5 of 12 in FY26 with no documented service impact; replaced with existing on-call contract at $18,000/yr. (2) 3% COLA applied to the trued-up base only: +$106,380. (3) Community Center (new): staffing phased from October 1 (3-month lead ahead of confirmed January 1 opening per Public Works schedule) and occupancy costs phased from January 1 — $324,000 vs. the $492,000 full-year figure submitted.
>
> **Recommendation:** Approve at $3,976,380. Flag position #4471's deletion for FY28 baseline (removes $72,000/yr going forward). Set a 10% variance-review trigger on the new Community Center program line given it's a first-year estimate with no execution history.

## Going deeper

- [references/artifacts.md](references/artifacts.md) — decision package template, budget-to-actual variance report, position control roster, budget calendar, all with filled example numbers.
- [references/red-flags.md](references/red-flags.md) — the signals a budget analyst catches on sight: threshold, likely cause, first question, data to pull.
- [references/vocabulary.md](references/vocabulary.md) — terms of art (apportionment, encumbrance, appropriation types) generalists misuse.

## Sources

GFOA (Government Finance Officers Association), "Fund Balance Guidelines for the General Fund" (best practice: unrestricted general fund balance ≥ 2 months / ~16.7% of operating revenues or expenditures) and GFOA's budgeting best-practice/Distinguished Budget Presentation Award criteria. OMB Circular A-11, "Preparation, Submission, and Execution of the Budget," Section 120 (apportionment process) and Part 6 (execution: obligations, outlays, reprogramming). Peter Pyhrr, "Zero-Base Budgeting" (Harvard Business Review, 1970) and its implementation at Texas Instruments and, under then-Governor Jimmy Carter, Georgia state government (later attempted federally during the Carter administration). 2 CFR 200 (Uniform Guidance) Appendix on cost allocation for federally funded programs. Variance-review thresholds (commonly 5-10% locally set) and phase-in costing practice reflect common state/local budget-office convention as documented in GFOA's budgeting curriculum, not a single universal standard — flagged as stated heuristics where a jurisdiction's own policy governs the exact figure. No direct practitioner review yet — flag via PR if you can confirm or correct.
