# Red Flags & Diagnostics

### Badge-out logged with no matching badge-in within the same shift
- **Usually means:** a tailgating event (someone held the door for an unbadged follower) or a badge malfunction; second-most-likely is a legitimate but unlogged exit (fire stairwell, dock door).
- **First question:** was this door's camera footage pulled for the timestamp, and does it show a second person?
- **Data to pull:** badge-access log for that door +/- 5 minutes, CCTV footage for the same window.

### Guard-force cost per post >1.5x local market rate with no capability upgrade
- **Usually means:** the contract hasn't been rebid in several years, or the incumbent is billing for a specialization (armed, K9) the site doesn't actually use.
- **First question:** when was this contract last competitively rebid, and does the post require the premium capability being billed?
- **Data to pull:** current contract terms, post orders, 3 comparable-market bids.

### Workplace-violence report where security hardens access before HR/legal/EAP convenes
- **Usually means:** the process is being treated as security-only, missing the personnel-signal intervention window and creating legal exposure if the individual is later disciplined without documented multidisciplinary review.
- **First question:** has the multidisciplinary threat-assessment team been convened, and within what timeframe from the initial report?
- **Data to pull:** intake timestamp, team-convene timestamp, HR employment history for the individual.

### Executive protection tier hasn't been reassessed in >12 months
- **Usually means:** the detail was sized once (often by title) and never re-scored against current exposure — either overspending on a now-lower-risk executive or under-covering one who's since become a public target.
- **First question:** has this executive been publicly tied to a controversial decision (layoffs, litigation, activist target) since the last assessment?
- **Data to pull:** last threat-assessment date, recent press/social mentions of the executive, travel itinerary for the next quarter.

### A single facility asset scores >20 on CARVER but shares its access tier with low-scoring spaces
- **Usually means:** the badge-tiering schema was built by convenience or seniority rather than consequence, and the highest-value asset on site has no better protection than a supply closet.
- **First question:** what access tier does this asset currently sit in, and when was that tier last reviewed against a CARVER score?
- **Data to pull:** current access-tier assignment, CARVER worksheet, badge-holder list for that tier.

### Guard-force headcount request follows within 60 days of an incident
- **Usually means:** the program is being sized reactively to the last event rather than to a documented, recurring risk assessment — a pattern that inflates cost and doesn't necessarily close the actual gap.
- **First question:** does the proposed headcount increase address the specific control failure in the incident, or is it a general increase?
- **Data to pull:** incident report root cause, proposed post orders for the new headcount.

### Terminated employee's badge still shows active access >24 hours post-termination
- **Usually means:** offboarding process gap between HR notification and security/IT badge deactivation — one of the most common and cheapest-to-fix insider-threat exposures.
- **First question:** what's the current SLA between termination notice and badge deactivation, and was it met here?
- **Data to pull:** termination timestamp from HR, badge-deactivation timestamp from access-control system.

### Vendor or contractor credential count exceeds 10% of total active badges
- **Usually means:** vendor access provisioning has outpaced de-provisioning — a common insider-adjacent exposure since vendor offboarding rarely has the same HR trigger as employee termination.
- **First question:** what fraction of active vendor badges belong to contracts that have already ended?
- **Data to pull:** active badge list filtered by vendor/contractor flag, cross-referenced against current vendor contract end dates.

### Physical penetration test hasn't been run in >12 months
- **Usually means:** access-control policy is untested against a real tailgating/social-engineering attempt, so its actual failure rate is unknown.
- **First question:** what was the result and date of the last unannounced penetration test?
- **Data to pull:** most recent pen-test report, corrective actions taken (or not) from its findings.
