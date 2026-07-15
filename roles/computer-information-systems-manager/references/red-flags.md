# Red flags — what an IT manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A vendor/platform decision justified by implementation quote alone, with no migration, retraining, or exit-cost estimate attached
- **Usually means:** the real total cost of ownership hasn't been priced — the decision may look cheaper than it actually is once switching and future exit costs are included.
- **First question:** "What's the one-time migration/retraining cost, and what would it cost to leave this new platform in three years?"
- **Data to pull:** vendor implementation quote, estimated migration effort (hours, contractor cost), historical retraining cost for comparable past migrations.

### A known security vulnerability sitting unremediated for 90+ days with no documented risk-acceptance decision
- **Usually means:** the risk is being deferred by default inaction rather than a deliberate, business-informed decision by someone with the authority to accept it.
- **First question:** "Who explicitly accepted this risk, in business-impact terms, and when does it get re-reviewed?"
- **Data to pull:** vulnerability age and severity, risk register entry (or absence of one), name of the accountable risk-acceptance owner.

### A technical-debt backlog with no estimated remediation cost or dedicated capacity allocation
- **Usually means:** debt is being tracked as a list, not managed as a quantified liability — it will keep compounding until a forced, more expensive reckoning.
- **First question:** "What percentage of this quarter's engineering capacity is allocated to debt paydown, and what's the estimated cost if this specific item is deferred another year?"
- **Data to pull:** technical debt backlog with age and estimated remediation cost per item, capacity allocation by initiative type for the current planning cycle.

### Disaster recovery / backup testing that hasn't actually been executed (only documented) in the last 12 months
- **Usually means:** the recovery plan's real effectiveness is unverified — a plan that's never been tested often fails at the exact moment it's needed.
- **First question:** "When was the last full recovery test actually run, and what was the measured recovery time versus the target?"
- **Data to pull:** DR test execution log and results, stated recovery time objective (RTO) per critical system versus what was actually measured.

### Resilience/DR investment that's uniform across systems regardless of actual downtime cost
- **Usually means:** budget may be misallocated — over-invested in low-stakes systems, under-invested in genuinely critical ones.
- **First question:** "What's the actual quantified cost of an hour of downtime for this specific system, and does the DR investment level match it?"
- **Data to pull:** business-impact-of-downtime estimate per system, current DR/redundancy spend per system.

### Custom-built internal tooling for a capability that has multiple mature commercial products available
- **Usually means:** engineering capacity may be going toward undifferentiated, commodity work instead of what's actually core to the business's competitive differentiation.
- **First question:** "What does this custom system do that a standard commercial tool doesn't, and is that difference actually differentiating for our business?"
- **Data to pull:** ongoing maintenance cost/headcount for the custom system, feature comparison against available commercial alternatives.

### A major system decision made without input from whoever ultimately owns the business capability it serves
- **Usually means:** the technology choice risks being optimized for technical elegance or IT convenience rather than the actual business need it's meant to serve.
- **First question:** "What specific business capability was this decision meant to enable, and did the business owner sign off on this approach?"
- **Data to pull:** the original business requirement/ask, decision documentation and stakeholder sign-off.

### IT budget where technology-refresh or new-initiative spend has grown for several consecutive cycles while technical-debt-paydown allocation has stayed flat or shrunk
- **Usually means:** debt paydown is being systematically deprioritized against new visible work, setting up a larger forced reckoning later.
- **First question:** "What's the trend in debt-paydown allocation over the last 4-6 budget cycles, and is the debt backlog growing faster than it's shrinking?"
- **Data to pull:** budget allocation trend by category, technical debt backlog size/age trend over the same period.
