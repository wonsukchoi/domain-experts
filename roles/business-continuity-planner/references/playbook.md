# Business Continuity Planner — Playbook

## BIA cost-of-downtime curve and RTO derivation (filled example)

| Outage duration | Cost/hour | Cumulative cost |
|---|---|---|
| Hours 1-2 | $15,000 | $30,000 |
| Hours 3-4 | $25,000 | $80,000 |
| Hours 5-8 | $40,000 | $240,000 |
| Beyond 8 hours (MTD breach) | $40,000 + $250,000 flat penalty | Escalating |

| Metric | Value |
|---|---|
| MTD (contractual SLA ceiling) | 8 hours |
| Last-tested actual recovery capability | 10 hours |
| **Gap vs. MTD** | **2 hours over** |
| **Target RTO (with margin below MTD)** | **6 hours** |

**Use:** Always derive the RTO target from the cost curve and MTD together — the curve tells you how costly delay is at each interval, and the MTD tells you the hard ceiling the RTO must sit meaningfully below.

## Cost-benefit worksheet for a continuity investment (filled example)

| Component | Value |
|---|---|
| Proposed investment (hot-standby infrastructure) | $180,000/year |
| Historical MTD breaches (prior year) | 2 outages, combined 4 hours over MTD |
| Contractual penalty per breach | $250,000 × 2 = $500,000 |
| Escalated hourly loss for combined 4 extra hours | 4 × $40,000 = $160,000 |
| **Total historical annual exposure** | **$660,000** |
| **Investment vs. exposure** | $180,000 investment vs. $660,000 exposure — **justified** |

**Use:** Never present a continuity investment's cost in isolation — always pair it against quantified historical or projected exposure from the specific gap it closes.

## Dependency mapping and single-point-of-failure worksheet (illustrative structure)

| Critical process | System dependency | Vendor dependency | Personnel dependency |
|---|---|---|---|
| Order processing | Primary DB cluster | Payment gateway provider | On-call DBA (1 person, no backup identified) |
| Customer support | Ticketing platform | Same payment gateway provider | Support lead |
| Billing | Same primary DB cluster | — | Billing analyst |

**Use:** Read this table by column, not just by row — the payment gateway provider and the primary DB cluster each support multiple critical processes, making them the actual top-priority single points of failure, ahead of any individual process's own plan.

## Tabletop exercise design and after-action checklist

1. Design the scenario to be at least as severe as the worst outage this process has historically experienced, or a plausible worse case if no severe outage has occurred yet.
2. Include at least one deliberately unavailable resource (a key contact unreachable, a backup system also down) to test real decision-making under constraint, not just the ideal path.
3. Time each major step against the plan's assumed timeline.
4. If the exercise produces zero findings, treat that as a signal to increase scenario difficulty next cycle, not as confirmation of plan quality.
5. Document every finding with an owner and remediation deadline, and verify remediation before the next test cycle.

## BIA/RTO recommendation memo — filled example

> **Business Continuity Recommendation — Order Processing System**
> MTD: 8 hours (contractual SLA). Current tested recovery capability: 10 hours — **2-hour gap beyond MTD.**
> Recommended RTO: 6 hours (2-hour margin below MTD).
> Required investment: $180,000/year (hot-standby infrastructure).
> Historical annual exposure from MTD breaches: $500,000 (contractual penalties) + $160,000 (escalated hourly losses) = **$660,000/year**.
> **Recommendation: Approve the $180,000/year investment — it closes a demonstrated $660,000/year exposure and brings recovery capability within a defensible margin of MTD.**
