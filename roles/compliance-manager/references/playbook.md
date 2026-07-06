# Compliance program resourcing playbook

Filled worksheets for the three recurring resourcing decisions: coverage-ratio sizing, build-vs-buy TCO, and staffing-model choice.

## 1. Risk-tiered coverage worksheet

Score each business line/product on likelihood (1–5) × impact (1–5) = risk score, then allocate analyst headcount proportional to score, not headcount-per-unit.

| Business line | Likelihood | Impact | Risk score | Accounts/relationships | Target ratio | FTE needed | FTE assigned | Gap |
|---|---|---|---|---|---|---|---|---|
| Consumer lending (top-risk-tier) | 4 | 5 | 20 | 28,000 | 1:175 | 2.9 | 2.0 | -0.9 |
| Small-business lending | 3 | 4 | 12 | 9,500 | 1:200 | 1.6 | 1.5 | -0.1 |
| Deposit/payments | 2 | 3 | 6 | 41,000 | 1:250 | 1.3 | 1.5 | +0.2 |
| Marketing/affiliate | 2 | 2 | 4 | n/a (activity-based) | n/a | 0.5 | 1.0 | +0.5 |

Reading the gap column: consumer lending is under-resourced relative to its risk score despite having the most analysts in absolute terms — the ratio, not the headcount, is what defends a reallocation ask. Anything under-target by more than 0.5 FTE is the reallocation to propose before requesting net-new headcount.

## 2. Build-vs-buy total cost of ownership comparison

Run this side-by-side before any monitoring/case-management technology decision. Include the paired headcount line — a tooling-only comparison understates the buy path's real cost and overstates its savings.

| Line item | Build (18-month in-house dev) | Buy (licensed platform) |
|---|---|---|
| One-time development/implementation | $310,000 (2 engineers × 9 months loaded) | $22,000 (implementation/config fee) |
| Annual licensing | $0 | $37,800 (175 req/mo × $18 × 12) |
| Annual maintenance/on-call | $85,000 (0.5 FTE eng loaded) | included in license |
| Paired analyst FTE (exception handling) | 0.5 FTE, $47,500/year | 0.5 FTE, $47,500/year |
| Time to first coverage | 9–12 months | 6–8 weeks |
| Year 1 total | $442,500 | $107,300 |
| Year 3 total (build amortized) | $612,500 | $220,900 |

Decision rule: buy wins unless the 3-year build total is lower **and** the regulatory deadline allows a 9–12 month implementation runway. Here it isn't and it doesn't — buy is correct on both cost and time-to-coverage.

## 3. Staffing-model decision matrix

| Factor | Favors centralized | Favors embedded |
|---|---|---|
| Regulatory consistency across business units required | Yes | — |
| Business-unit-specific product knowledge needed for effective review | — | Yes |
| Business unit volume large enough to justify dedicated headcount (>1.5 FTE by coverage worksheet) | — | Yes |
| Independence risk (unit has history of pushing back on findings) | Yes | — |
| Speed-to-decision on routine, low-risk approvals is the bottleneck | — | Yes |

Once picked, document explicitly:
- **Reporting line:** embedded analyst's performance review and compensation stay with compliance (solid-line); business-unit head gets a dotted-line input to review, not sign-off.
- **Escalation path:** embedded analyst escalates directly to the compliance manager on any finding the business-unit head disagrees with — never routed through the business unit first.
- **Review cadence:** centralized team audits a sample of embedded analysts' decisions quarterly to confirm consistency with the risk-tiered coverage standard.

## 4. Budget ask template

```
Obligation: <regulation/requirement>, effective <date>
Volume impact: <current> → <projected>, benchmarked against <named source>
Cost — manual/hire path: <FTE count> × <loaded cost> = $<total>, <hiring lag> lead time
Cost — tooled path: $<licensing> + <FTE count> × <loaded cost> = $<total>, <implementation lead time>
Recommendation: <path>, $<amount>/year
Coverage instrumentation: <specific metric>, reported <cadence> to <audience>
If unfunded: <explicit named tradeoff — what gap remains or what existing coverage gets pulled>
```
