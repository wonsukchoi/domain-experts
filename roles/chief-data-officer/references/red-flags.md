# Red flags

### Two dashboards report different values for a same-named metric, gap >5%
- **Usually means:** the metric's definition diverged at the source-system level (different filter, different window, different status logic) and nobody owns the canonical definition.
- **First question:** "pull both queries — where exactly does the filter or join differ?"
- **Data to pull:** the underlying SQL/query definitions for both dashboards, side by side.

### A dataset feeding board or regulatory reporting has no named owner
- **Usually means:** the dataset was built for an internal purpose and got adopted for external reporting without governance catching up.
- **First question:** "who signs off if this number is wrong in a filing?"
- **Data to pull:** the data catalog or lineage record for the dataset; if it doesn't have an owner field populated, that's the finding itself.

### A dataset has been retained >2 years with no query activity in the last 2 quarters
- **Usually means:** it was collected for a use case that never shipped or already ended, and nobody's revisited the retention decision since.
- **First question:** "what's the documented use case on file, and when was it last true?"
- **Data to pull:** query-log audit against the dataset, plus the original collection justification if one exists.

### Access grants to a sensitive/PII dataset haven't been reviewed in 12+ months
- **Usually means:** access creep — grants given for a project that ended, never revoked, now sitting as unnecessary exposure.
- **First question:** "of everyone with access today, who's actually used it in the last 90 days?"
- **Data to pull:** access control list cross-referenced against query/access logs for the same period.

### An AI/ML project kickoff plan has no data lineage or quality audit step
- **Usually means:** the timeline estimate assumed clean, well-understood training data without verifying it — the most common source of blown ML timelines.
- **First question:** "has anyone traced this training data back to its source and checked label quality?"
- **Data to pull:** the project plan's task list; absence of a data-audit line item is the finding.

### 3+ teams are independently querying the same upstream table with undocumented business logic
- **Usually means:** the table's meaning was never formally cataloged, so each team reverse-engineered its own interpretation, and they've likely diverged.
- **First question:** "have you compared your query's filters against the other teams using this table?"
- **Data to pull:** query logs against the table, grouped by team, compared for filter/join differences.

### An incident or audit surfaces a data store nobody in Data/IT knew existed
- **Usually means:** shadow IT — a spreadsheet export, a personal cloud drive, or a team-provisioned tool operating entirely outside governed systems.
- **First question:** "how did this get created, and what else like it exists that we haven't found?"
- **Data to pull:** the incident timeline plus a scoped audit of adjacent teams for similar undocumented stores.

### Data quality complaints route to a general IT ticket queue with no SLA or owner
- **Usually means:** data quality isn't treated as an owned, measured discipline — it's handled as ad hoc IT support, so recurring root causes never get fixed.
- **First question:** "how many of the last 20 tickets were the same underlying issue?"
- **Data to pull:** ticket queue filtered to data-quality tags, grouped by root cause where documented.

### A regulatory filing uses a metric definition that changed since the last filing, undocumented
- **Usually means:** a schema or business-logic change upstream silently altered a reported number without anyone flagging it as a definitional change requiring disclosure.
- **First question:** "what changed in the source system between this filing and the last one?"
- **Data to pull:** the metrics catalog change log for the metric in question, or the absence of one.

### A third-party data-sharing agreement has no retention or deletion clause
- **Usually means:** the agreement was drafted or renewed without Data/Legal coordination, leaving the company unable to enforce deletion if the relationship ends or a breach occurs on the vendor's side.
- **First question:** "what does this vendor's contract say happens to our data if we terminate?"
- **Data to pull:** the vendor contract's data-handling clauses, cross-checked against the current vendor risk register.
