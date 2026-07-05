# Red Flags

Smell tests for requirements work, feasibility studies, integration designs, and migration plans. Format per flag: what it usually means, the first question a veteran asks, the data to pull.

### Requirements sign-off happened in under a week with no dissent logged

- **Usually means:** the document was circulated for signature, not actually reviewed against real process — or the sessions excluded the people who'd disagree (front-line staff, not just their managers).
- **First question:** "Who was in the room, and what did they push back on?"
- **Data to pull:** JAD session attendee list against the org chart of who actually executes the process daily; count of change requests filed against "signed-off" requirements in the following 60 days as a proxy for how real the sign-off was.

### More than 10% of requirements have no assigned design element at gap-analysis checkpoint

- **Usually means:** elicitation surfaced the requirement but nobody translated it into a build decision — it will resurface as a UAT defect instead of a design-phase decision.
- **First question:** "Who owns closing this gap, and by when?"
- **Data to pull:** requirements traceability matrix, filtered to rows with a populated requirement ID but an empty design-element or owner column.

### Vendor demo drove the "meets requirement" checkbox

- **Usually means:** the demo was run on the vendor's curated dataset and workflow, not the org's actual process — edge cases the org hits weekly never appeared.
- **First question:** "Was this checked against our process with our data, or against the vendor's script?"
- **Data to pull:** the specific demo script or scenario list used, compared line-by-line against the org's documented as-is process for the same function.

### Data quality assessment deferred to UAT

- **Usually means:** remediation work is now competing with go-live schedule instead of having its own gate, and UAT will surface data problems that get misdiagnosed as system defects.
- **First question:** "What's the duplicate/conflict rate in the source system today, and when was it measured?"
- **Data to pull:** a profiling run against the actual production source table (not a stale export), duplicate/conflict rate by key entity (customer, item, vendor master).

### Point-to-point integration count is in the double digits and growing

- **Usually means:** the integration architecture wasn't designed, it accreted one urgent request at a time; maintenance cost is now tracking connection count (n(n-1)/2 growth), not system count.
- **First question:** "If we add one more system next year, how many new connections does that require under the current pattern?"
- **Data to pull:** current interface inventory with point-to-point vs. middleware-routed count, and incident/maintenance hours logged per interface over the last two quarters.

### Big-bang cutover proposed primarily because it's faster on paper

- **Usually means:** the schedule pressure is real but the blast radius of a failed cutover hasn't been priced against the schedule savings — reversibility was never on the table.
- **First question:** "If this cutover fails at hour 30 of the weekend, what's the rollback, and has it been tested?"
- **Data to pull:** rollback plan document (if one doesn't exist, that's the finding itself); training-throughput data for how many staff can be certified per week, compared against total staff needing training before go-live.

### Economic feasibility case was built entirely by IT with no finance sign-off

- **Usually means:** the discount rate, cost baseline, and what counts as a "benefit" were chosen by the people who want the project approved.
- **First question:** "Whose assumptions are the discount rate and the cost-avoidance figures, and has finance validated them independently?"
- **Data to pull:** the feasibility study's cited discount rate and cost-avoidance line items, cross-checked against finance's standard capital-project hurdle rate.

### Requested timeline is meaningfully shorter than benchmark data for comparable projects

- **Usually means:** the schedule was set by the sponsor's calendar (a fiscal year, an executive's tenure) rather than by the scope of the actual gap analysis and integration count.
- **First question:** "What comparable project — same system class, similar integration count — actually finished in this timeframe?"
- **Data to pull:** industry benchmark data for the platform/project type (e.g., Panorama Consulting's ERP report) and the project's own gap-analysis size (requirement count, customization count) as inputs to a bottom-up schedule estimate.

### A "customization" line item has no named business differentiator behind it

- **Usually means:** the org is paying ongoing upgrade-compatibility cost to preserve a process that isn't actually distinctive — often because nobody asked "would we lose anything real by conforming to the standard workflow."
- **First question:** "What does this customization protect that a competitor running the standard workflow can't do?"
- **Data to pull:** the customization backlog with a stated business justification per item, sorted by estimated ongoing maintenance cost.

### Interface control document says "System A syncs with System B" with no error-handling section

- **Usually means:** the design covers the happy path only; every mismatch (missing key, price discrepancy, duplicate record) will be handled ad hoc by whoever's on call when it first happens in production.
- **First question:** "What happens when the record this depends on doesn't exist yet on the other side?"
- **Data to pull:** the ICD's error-handling and reconciliation section — if absent, that absence is the finding; if present, the reconciliation job's actual run history and variance rate.
