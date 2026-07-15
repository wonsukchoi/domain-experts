# Vendor & budget artifacts

Filled templates a facilities/admin lead actually produces. Real structures with plausible numbers, not descriptions of what to include.

## Vendor TCO comparison worksheet

Scenario: IT helpdesk support renewal at 240 seats (see SKILL.md worked example for the full walkthrough).

| Cost component | Vendor A | Vendor B |
|---|---|---|
| Contract price ($/seat/month × 240 seats × 12) | $18 → $51,840/yr | $24 → $69,120/yr |
| SLA response time | 4 hours | 1 hour |
| Downtime cost (15 incidents/mo × SLA hrs × $65/hr loaded × 12) | $46,800/yr | $11,700/yr |
| Internal escalation overhead (hrs/wk × 52 × $50/hr loaded) | $7,800/yr (3 hrs/wk) | $1,300/yr (0.5 hrs/wk) |
| **Total cost of ownership** | **$106,440/yr** | **$82,120/yr** |
| Termination notice | 90 days | 30 days |

Decision rule applied: TCO governs unless the cheaper-TCO option fails a hard requirement (e.g., no viable fallback, unacceptable termination lock-in) — here Vendor B wins on both TCO and flexibility, so the comparison is decisive.

## Space utilization tracker (quarterly)

| Quarter | Leased sq ft | Avg daily occupancy (badge-in) | Utilization % | Provisioned for headcount | Actual headcount |
|---|---|---|---|---|---|
| Q1 | 42,000 | 168 desks used | 40% | 300 (at signing) | 240 |
| Q2 | 42,000 | 176 desks used | 42% | 300 | 248 |
| Q3 | 42,000 | 182 desks used | 43% | 300 | 255 |

Threshold applied: utilization sustained below 50% for 2+ consecutive quarters triggers a formal right-sizing review at the next lease break option — here Q1–Q3 all sit under that threshold, so the review is scheduled regardless of the modest upward trend, since the trend alone (43% by Q3) doesn't project past 50% before the next break date.

## Preventive maintenance decision table

| Asset | Age vs. expected life | Deferred repair cost now | Estimated failure cost if deferred | Decision |
|---|---|---|---|---|
| Rooftop HVAC unit 2 | 6 yrs of 15 | $2,400 (compressor service) | $18,000+ (full unit replacement + downtime) | Schedule now — early in life, deferral cost ratio is 7.5x |
| Lobby carpet | 9 yrs of 10 | $6,000 (partial replace) | $6,500 (full replace, ~1 yr out) | Defer to planned full replacement next year — near end of life, minimal deferral premium |
| Backup generator | 4 yrs of 20 | $900 (annual service) | $40,000+ (failure during an outage, plus liability exposure) | Schedule now — critical single point of failure, deferral cost is severe and asset is early in life |

Decision rule applied: schedule preventive work when the asset has >20% of expected useful life remaining AND the deferred-failure cost meaningfully exceeds the current repair cost; defer to planned replacement only when both the remaining-life and cost-delta conditions argue against further investment.

## Budget-to-utilization review (annual, by line)

| Budget line | Budgeted | Actual spend | Original utilization assumption | Current utilization | Action |
|---|---|---|---|---|---|
| Office space lease | $1,260,000 | $1,260,000 | 300 employees | 255 employees (85%) | Flag for right-sizing at next break |
| Software licenses (design tools) | $86,400 | $86,400 | 240 seats provisioned | 149 seats active (62%) | Reduce seat count at renewal |
| Cleaning/janitorial | $144,000 | $151,200 | 5x/week service | 5x/week, rate increase not caught | True up contract, recover overpayment if possible |
| Helpdesk support (post-upgrade) | $69,120 | $69,120 | 240 seats, 1-hr SLA | 255 seats, SLA holding | On track, seat count needs a contract amendment |

Review cadence applied: every line gets checked against its original utilization assumption at least annually, with any line drifting >15% from assumption (space, licenses here) flagged for action at the next natural decision point (lease break, contract renewal) rather than immediately renegotiated mid-term unless the drift is a compliance or overpayment issue (cleaning line, caught immediately).
