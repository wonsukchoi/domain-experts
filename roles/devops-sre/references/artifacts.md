# SRE operational artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Error budget worksheet (filled — see Worked example in SKILL.md for full narrative)

| Item | Value |
|---|---|
| SLO | 99.9% monthly availability |
| Total monthly budget | 43.2 minutes (30 days × 24 hr × 60 min × 0.001) |
| Consumed so far this month | 34.56 minutes (80%) |
| Remaining budget | 8.64 minutes |
| Proposed change's historical failure rate | 15% |
| Impact if it fails (fleet-wide) | 12 minutes |
| Expected value (fleet-wide) | 1.8 minutes (looks safe on average) |
| Tail risk (fleet-wide) | 12 minutes in the 15% failure case — exceeds remaining budget |
| Canary (5%) tail risk | ~0.5 minutes budget-equivalent — within remaining budget |
| **Decision** | Canary rollout, not direct fleet-wide deploy |

## 2. Canary rollout plan (filled example)

| Stage | Traffic % | Duration | Rollback trigger | Budget consumed if triggered |
|---|---|---|---|---|
| 1 | 5% | 2 hours | Error rate >0.5% sustained 5 min | ~0.5 min |
| 2 | 25% | 2 hours | Error rate >0.5% sustained 5 min, or Stage 1 budget consumption >1 min | ~2.5 min |
| 3 | 50% | 2 hours | Same trigger, or cumulative budget consumption >4 min | ~5 min |
| 4 | 100% | Ongoing | Same trigger | Full exposure if it fails post-rollout |

**Rule applied:** each stage only proceeds if the previous stage's actual budget consumption stayed under its pre-set sub-allocation — a stage that trips the trigger halts progression and initiates automatic rollback, not a manual judgment call under pressure.

## 3. Blameless postmortem template (filled example)

> **Incident:** Caching layer canary at 25% triggered automatic rollback after 6 minutes due to sustained error rate above 0.5%.
> **Timeline:** 14:02 canary expanded to 25%. 14:04 error rate crossed 0.5%. 14:09 sustained-5-minute threshold hit, automatic rollback fired. 14:11 error rate returned to baseline.
> **Impact:** ~2.1 minutes of budget-equivalent degraded availability (25% of traffic for ~6 min before rollback completed) — within the pre-approved Stage 2 sub-allocation of 2.5 minutes.
> **What went wrong:** New cache invalidation logic had a race condition under concurrent writes, not caught by staging tests (staging traffic pattern doesn't replicate this concurrency profile).
> **What caught it:** The automatic rollback trigger — worked as designed, contained the blast radius to 25% instead of 100%.
> **Action items (owner, date):** (1) Add a concurrency-pattern test to the staging suite matching production write patterns — Engineer A, next sprint. (2) Re-attempt canary with the race condition fixed, same staged plan — Engineer B, this week.
> **Not in this report:** who was on call, who wrote the original code — not relevant to what would have caught this sooner or contained it smaller.

## 4. Toil prioritization worksheet (filled example)

| Task | Frequency/month | Time cost per instance | Monthly time cost | Automation priority |
|---|---|---|---|---|
| Manual service restart after known memory leak | 40 | 5 min | 200 min | High — top of automation queue |
| Manual SSL cert renewal | 1 | 45 min | 45 min | Medium |
| Manual annual compliance report generation | 0.08 (once/year) | 60 min | ~5 min/month equivalent | Low — not worth automating relative to the above |

**Rule applied:** prioritize by frequency × time cost, not by which task feels most painful in the moment — the 40x/month, 5-minute task costs 4x more aggregate engineering time than the once-a-year hour-long task, even though the annual task feels bigger when it happens.
