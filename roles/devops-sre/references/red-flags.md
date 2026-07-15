# Red flags — what an SRE notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A risky deploy proposed while the error budget is already 70-80%+ consumed for the period
- **Usually means:** the team is treating error budget as a formality rather than a decision rule — the math likely says stop shipping risk, not proceed.
- **First question:** "What's the remaining budget in minutes, and does this change's historical failure rate fit inside it even in the failure case, not just on average?"
- **Data to pull:** current error budget consumption and remaining allowance, historical failure rate and impact for this class of change.

### A deploy decision based on expected-value downtime math alone, with no check of the tail (failure-case) scenario
- **Usually means:** averaging hides the risk that actually determines SLO compliance — a low-probability, high-impact failure can single-handedly breach the budget even when the expected value looks safe.
- **First question:** "If this specific change fails (not on average, but this one time), does that single event blow the remaining budget?"
- **Data to pull:** historical failure rate and impact-when-failed for comparable changes, remaining error budget.

### A large, infrequent release bundling many changes together
- **Usually means:** if something breaks, isolating which specific change caused it will be slow, extending MTTR — the batch itself is a reliability risk independent of any single change's quality.
- **First question:** "If this release causes an incident, how long would it take to identify which of the bundled changes caused it?"
- **Data to pull:** number of distinct changes in the release, rollback granularity (can we roll back one change or only the whole batch?).

### A runbook that hasn't been executed (tested, not just read) in 6+ months
- **Usually means:** the runbook may no longer match the current system, and its first real test may happen during an actual incident — the worst time to discover it's wrong.
- **First question:** "When was this runbook last actually run, and does the current system architecture still match what it assumes?"
- **Data to pull:** runbook last-tested date, recent architecture changes to the systems it covers.

### An alert that has fired repeatedly with no action taken, or a page that's routinely acknowledged and dismissed without investigation
- **Usually means:** alert fatigue is setting in — real signals are at risk of being lost in noise, and responders are learning to ignore pages.
- **First question:** "What percentage of pages for this alert in the last month required real action versus were dismissed as noise?"
- **Data to pull:** alert firing frequency and resolution/dismissal rate over the trailing month.

### A postmortem document that names an individual as the cause rather than the systemic/process gap that allowed the failure
- **Usually means:** the review is heading toward blame rather than root cause, which teaches people to hide problems rather than surface them early — and the same failure mode will likely recur.
- **First question:** "What would have caught or contained this regardless of who was involved?"
- **Data to pull:** the postmortem draft, whether action items target systemic fixes (better tests, better alerts, better rollout gates) versus individual behavior.

### Production configuration that differs from what's defined in infrastructure-as-code, discovered via a manual "quick fix" not reflected back into code
- **Usually means:** configuration drift — the system's actual running state is no longer fully reproducible, reviewable, or recoverable from the code that's supposed to define it.
- **First question:** "Is this manual change reflected in the IaC repo, or does production now silently differ from what the code says?"
- **Data to pull:** diff between actual running configuration and the IaC definition, log of recent manual console/CLI changes.

### A service missing one or more of the four golden signals (latency, traffic, errors, saturation) in its dashboard
- **Usually means:** there's a real observability gap — the team can't fully diagnose this service's failure modes within minutes, and will discover this specifically during an incident.
- **First question:** "Which of the four golden signals are we missing for this service, and what would it take to add them?"
- **Data to pull:** current dashboard/metrics coverage per service, incident history where a missing signal slowed diagnosis.
