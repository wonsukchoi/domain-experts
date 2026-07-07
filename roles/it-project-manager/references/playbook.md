# IT Project Manager — Playbook

## RAID log (filled example)

| ID | Type | Description | Owner | Trigger/Review Date | Impact | Status |
|---|---|---|---|---|---|---|
| R-04 | Risk | Vendor hardware ship date has no penalty clause; same vendor missed equivalent milestone on prior contract | J. Alvarez (Procurement) | 2026-08-15 (30 days before ship date) | 3-week schedule slip if missed | Open |
| A-02 | Assumption | Test environment has production-equivalent data volume for load testing | M. Chen (QA Lead) | 2026-07-30 | Load test results invalid if false | Open |
| I-07 | Issue | Two data-mapping defects found in integration testing, not in original test plan | R. Osei (Dev Lead) | Resolved 2026-07-10 | 4-week critical path slip | Closed — see CR-03 |
| D-11 | Decision | Descope legacy archive migration to phase 2 rather than add headcount | Steering Committee | Decided 2026-07-18 | Recovers 4-week slip at $0 net cost | Closed |

Review cadence: risks and assumptions re-scored every status cycle; a risk with no review in 2+ cycles is stale — either re-score it or close it, never let it sit unowned.

## EVM tracking table (filled example, week 20 of 40)

| Work package | Baseline budget | % planned by wk 20 | PV | Objective milestone met? | EV | AC |
|---|---|---|---|---|---|---|
| Requirements | $80,000 | 100% | $80,000 | Signed-off spec, yes | $80,000 | $82,000 |
| Data migration (critical path) | $160,000 | 62.5% | $100,000 | 2 of 5 sub-tasks passed integration test | $64,000 | $95,000 |
| Integration build | $200,000 | 40% | $80,000 | Build compiles, unit tests pass | $80,000 | $88,000 |
| UAT | $120,000 | 0% | $0 | Not started | $0 | $0 |
| ... (8 more packages) | $400,000 | — | $220,000 | — | $216,000 | $245,000 |
| **Total** | **$960,000** | — | **$480,000** | — | **$440,000** | **$510,000** |

CPI = 440,000 / 510,000 = 0.86. SPI = 440,000 / 480,000 = 0.92. Forecast at completion (EAC) = Budget at Completion / CPI = 960,000 / 0.86 = $1,116,279 — an $156,279 overrun at current performance if uncorrected.

## Change-request memo (filled template)

> **Change Request CR-03**
> **Project:** ERP Integration | **Date:** 2026-07-18 | **Requested by:** IT Project Manager
> **Change:** Remove legacy-system archive migration from Phase 1 scope; defer to Phase 2 (separately funded, no committed date).
> **Reason:** Data migration work package (critical path) re-forecast to slip 4 weeks (wk 22 to wk 26) due to 2 data-mapping defects found in integration testing. Removing archive migration (lowest business priority, no active users depend on it pre-go-live) frees $40,000 and 3 FTE-weeks, fully absorbing the slip.
> **Cost impact:** -$40,000 from Phase 1 budget (returned to contingency). **Schedule impact:** recovers go-live date to original baseline (wk 40).
> **Approval required from:** Steering Committee sponsor (budget authority >$25,000).
> **Decision:** Approved 2026-07-18. Rebaseline effective this date.

## Escalation threshold table

| Cumulative approved change value (% of original budget) | Action |
|---|---|
| 0-5% | Log in RAID, note in routine status, no formal re-baseline |
| 5-10% | Flag to sponsor in next scheduled steering meeting |
| >10% | Formal re-baseline conversation required before next status cycle |

## Recovery-option fallback order (when critical path slips)

1. Resequence non-critical work to free resources for the critical-path task (zero cost, use first if float exists elsewhere).
2. Fast-track: run normally-sequential tasks in parallel, accepting rework risk.
3. Crash: add resources to the critical-path task at incremental cost (diminishing returns past ~2 added resources on most software tasks — coordination overhead eats the gain).
4. Descope: remove lowest-priority scope to recover the date at reduced/zero cost — preferred over crashing when a genuinely low-priority package exists, since it doesn't introduce crashing's rework risk.
5. Re-baseline the date: only after 1-4 are exhausted or rejected by the sponsor as not viable.
