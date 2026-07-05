# Red flags & diagnostics

Signals an experienced postmaster/mail superintendent notices instantly. Load this when triaging a performance, routing, or security question — not for general reasoning (that's `SKILL.md`).

### On-time performance drops and the proposed response is a general carrier efficiency initiative
- **Usually means:** the actual failing stage (collection, processing, transportation, delivery) hasn't been identified, and the response may target a stage that isn't the actual problem
- **First question:** "What does stage-by-stage timing data show — is the delay actually at the delivery/carrier stage, or upstream?"
- **Data to pull:** stage-level timing comparison against the prior baseline period

### A route hasn't been rebalanced despite a documented double-digit change in delivery points or volume-per-point
- **Usually means:** the route's original design assumptions no longer match current reality, producing either carrier overload or hidden inefficiency
- **First question:** "When was this route last rebalanced, and what's changed in delivery-point count and volume-per-point since then?"
- **Data to pull:** route rebalancing worksheet with current vs. last-rebalance delivery-point and volume data

### Peak-season planning is described as "the standard plan, scaled up"
- **Usually means:** the plan may not account for the peak's different volume mix (more packages relative to letters), which changes the actual bottleneck from the standard-day one
- **First question:** "What's the peak period's volume mix compared to standard-day, and does the capacity plan address the resulting bottleneck specifically?"
- **Data to pull:** historical peak-season volume mix by mail class vs. standard-day mix

### A lost or delayed registered/certified item is being handled only through customer service recovery
- **Usually means:** the chain-of-custody break isn't being treated as the security incident it is, missing the investigation and reporting process it requires
- **First question:** "Has this been logged and routed as a chain-of-custody security incident, separate from the customer service response?"
- **Data to pull:** the chain-of-custody incident report and whether the security investigation protocol was triggered

### Access control for high-value mail handling areas is designed only around external threat
- **Usually means:** insider risk isn't being addressed, missing a real category of custody-failure incidents
- **First question:** "Does the current access control and audit logging address who inside the facility had access during the relevant window, not just external security?"
- **Data to pull:** access logs and dual-custody handling protocol documentation for high-value/tracked mail

### Delivery-point growth and volume-per-point trend are reported as a single combined metric
- **Usually means:** the two trends may be moving in different directions, and combining them obscures which route-planning response is actually needed
- **First question:** "Are delivery points growing, volume-per-point growing, both, or diverging — and does the route plan account for the specific combination?"
- **Data to pull:** delivery-point count and volume-per-point tracked as separate trend lines over the relevant period
