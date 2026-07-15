# Red flags — what a facilities/admin lead notices instantly

Smell tests with thresholds. Format per flag: the signal → what it usually means → first question to ask → data to pull. Any single one can be innocent; two or three together are a pattern.

## Vendor and contract

### A vendor contract auto-renewing within 60 days with no review scheduled
- **Usually means:** the contract went on autopilot after signing — nobody re-checked whether pricing, SLA terms, or actual need still fit.
- **First question:** "When did we last benchmark this vendor against the market, and has our usage changed since signing?"
- **Data to pull:** the renewal date and auto-renewal clause language, current usage/seat count vs. contracted volume, last-renegotiated pricing.

### SLA breaches logged but never escalated to a service credit or renegotiation
- **Usually means:** the SLA is being treated as a formality rather than an enforceable term — the vendor has learned it can miss without consequence.
- **First question:** "How many breaches this quarter, and why haven't any triggered the service-credit clause?"
- **Data to pull:** ticket/incident log with response times against contracted SLA, service-credit clause language, credits actually claimed vs. owed.

### A single vendor covering a function with no viable fallback identified
- **Usually means:** consolidation happened for convenience without anyone assessing what a vendor failure or price hike would cost.
- **First question:** "If this vendor failed tomorrow, what's the actual switching cost and time to a working alternative?"
- **Data to pull:** the contract's termination and transition-assistance terms, a rough estimate of switching cost and downtime.

### A vendor invoice that doesn't match the contracted rate or volume
- **Usually means:** a rate change wasn't caught, a seat count wasn't trued up after headcount changes, or billing drift nobody's auditing.
- **First question:** "Does this invoice reconcile to the current contract terms and our actual usage this period?"
- **Data to pull:** the signed contract/amendment history, current headcount or usage count, the last three invoices for a trend check.

## Facilities and maintenance

### Deferred-maintenance items on the same asset appearing in 2+ consecutive inspection cycles
- **Usually means:** the item was logged but never prioritized against competing budget asks, and the deferred cost is compounding.
- **First question:** "What does this cost if we fix it now versus what it costs if it fails first?"
- **Data to pull:** inspection/CMMS log for the asset, estimated repair cost now vs. estimated failure/replacement cost.

### Space utilization running below 50% of leased capacity for 2+ consecutive quarters
- **Usually means:** space was provisioned for a headcount plan that changed (hiring slowed, hybrid work reduced daily occupancy), and the lease is now oversized for actual need.
- **First question:** "Is this a temporary dip or the new normal, and when does the lease allow us to right-size?"
- **Data to pull:** badge-in/occupancy data by day of week over the period, lease term and any subleasing or downsizing options.

### A single point of failure in critical infrastructure (badge access, core network, primary HVAC) with no documented redundancy or failover plan
- **Usually means:** the system was built out once and redundancy was never revisited as it became more critical.
- **First question:** "What's the actual recovery time if this fails, and is that acceptable?"
- **Data to pull:** the system's criticality rating if one exists, historical outage frequency and duration, cost of adding redundancy.

## Budget and process

### A budget line consistently under- or over-spent by >15% against the original utilization assumption
- **Usually means:** the underlying need changed (headcount, space, service scope) and the budget was never re-baselined to match.
- **First question:** "Is this drift because the plan changed or because the original assumption was wrong?"
- **Data to pull:** budget vs. actual by line for the trailing 4 quarters, the original utilization assumption behind the budget.

### Helpdesk/ticket backlog growing month-over-month with average resolution time trending up
- **Usually means:** support capacity hasn't scaled with headcount, or a process/tooling change quietly slowed resolution.
- **First question:** "Is this a volume problem or a process problem — and since when has resolution time been trending up?"
- **Data to pull:** ticket volume and resolution-time trend by month, staffing level over the same period, any recent tooling or process changes.

### The same operational complaint (space, equipment, support responsiveness) recurring from different teams
- **Usually means:** an individual complaint that looked like a one-off is actually a scaling-threshold problem the current process can't absorb.
- **First question:** "How many distinct teams have raised this in the last quarter, and is the volume accelerating?"
- **Data to pull:** complaint/ticket log tagged by category, headcount growth over the same window.

### An approval process with the same friction level applied to a $200 purchase and a $50,000 vendor commitment
- **Usually means:** the control framework was never risk-tiered — everything routes through the same steps regardless of actual exposure.
- **First question:** "What would change if this category had a lighter-weight approval path?"
- **Data to pull:** approval-step count and cycle time by spend category, dollar distribution of purchases within each category.
