# Red flags — what a senior engineer notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### An architecture change justified by "scalability" with no actual load or bottleneck number cited
- **Usually means:** the proposed fix may be solving an imagined problem while the real pain (deploy coupling, team ownership, a different bottleneck entirely) goes unaddressed.
- **First question:** "What's the actual current load/CPU/latency number, and what specifically is failing to scale today?"
- **Data to pull:** current resource utilization for the component in question, any concrete incident or metric showing an actual scaling limit being hit.

### A deploy shipped with no described rollback plan
- **Usually means:** the change is only tested going forward, and if it needs to be undone under production pressure, the undo path is untested or nonexistent.
- **First question:** "How do we undo this specific deploy if it goes wrong, and has that path actually been tested?"
- **Data to pull:** the rollback plan (or its absence), whether a comparable rollback has been exercised before.

### An exception caught with an empty or no-op handler
- **Usually means:** a loud failure is being silently swallowed, which can turn a visible bug into silent data corruption discovered much later and with less context.
- **First question:** "What happens to the system state if this specific exception occurs, and is silently continuing actually safe here?"
- **Data to pull:** the specific catch block and what it does (or doesn't do), downstream effects if the underlying error condition is real.

### A new abstraction introduced for a pattern with only one or two concrete instances
- **Usually means:** premature abstraction based on an assumed pattern that may turn out to be a coincidence rather than a real recurring shape — the "rule of three" threshold hasn't been met.
- **First question:** "How many concrete instances of this pattern actually exist right now, not projected forward?"
- **Data to pull:** the actual current instances the abstraction is meant to unify, versus hypothetical future ones.

### A code review approved without evidence the reviewer actually understood the change (no substantive comments, fast turnaround on a complex diff)
- **Usually means:** review may be functioning as a formality/rubber stamp rather than actually catching what the author is blind to.
- **First question:** "Did this review surface any disagreement or question, or was it approved without engagement?"
- **Data to pull:** review comment history and turnaround time relative to the diff's complexity.

### A postmortem whose action items are process language ("communicate better," "be more careful") rather than concrete, owned changes
- **Usually means:** the review likely didn't reach an actual systemic fix, and the same failure mode is likely to recur.
- **First question:** "What specific, owned, dated action item would have actually caught or prevented this?"
- **Data to pull:** the postmortem's action items, whether each has a named owner and a concrete mechanism (not just an exhortation).

### A production incident investigated by immediately theorizing about causes without first checking what changed (recent deploys, config changes)
- **Usually means:** correlation-then-causation debugging is being skipped — the deploy or change that immediately preceded the incident is the natural first suspect and should be checked before broader theorizing.
- **First question:** "What deployed or changed right before this started, and has that been ruled in or out first?"
- **Data to pull:** deploy/config change log around the incident's onset time.

### Instrumentation (logging, metrics, tracing) added only after an incident revealed its absence, rather than shipped with the original feature
- **Usually means:** the team is repeatedly discovering observability gaps reactively, during incidents, rather than closing them proactively as features ship.
- **First question:** "Was instrumentation for this feature added at ship time, or only after we needed it and didn't have it?"
- **Data to pull:** the feature's original PR/instrumentation coverage, any subsequent incident where missing observability was cited as a contributing factor.
