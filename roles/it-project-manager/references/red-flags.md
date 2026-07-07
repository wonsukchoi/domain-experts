# IT Project Manager — Red Flags

### Task reported "90%+ complete" for 2+ consecutive status cycles
- **Usually means:** an undiscovered integration or dependency problem is hiding in the last portion of the work; second likeliest is the task owner rounding up to avoid an awkward status conversation.
- **First question:** "What's the specific remaining artifact — a passed test, a sign-off, a merged branch — and can I see it?"
- **Data to pull:** the task's linked build/test artifact or sign-off document, not the task tracker's percent field.

### CPI and SPI both below 0.90 at the same reporting period
- **Usually means:** the project is both over budget and behind schedule — a WBS decomposition that was too optimistic at baseline, or a risk that materialized without a contingency draw-down.
- **First question:** "Which work packages are driving both numbers down — is it one package or spread across many?"
- **Data to pull:** the EVM table broken out by work package, not just the rolled-up project total.

### Cumulative approved change requests exceed ~10% of original budget baseline
- **Usually means:** the original baseline is no longer a meaningful comparison point; continuing to report against it understates true cost/schedule reality.
- **First question:** "Has the sponsor formally re-baselined, or are we still measuring against a stale plan?"
- **Data to pull:** the change log with cumulative approved dollar value against original budget.

### A vendor deliverable is 1-2 weeks from its contractual milestone with zero interim artifact produced
- **Usually means:** the vendor is behind and hasn't disclosed it yet; second likeliest is a dependency on the client side (data, access, sign-off) that's blocking them silently.
- **First question:** "What have you actually delivered against this milestone so far, not what's the plan to deliver it?"
- **Data to pull:** the vendor's own internal status artifact if the contract entitles you to one, or a direct deliverable sample.

### Risk register entry with no owner name or no review/trigger date
- **Usually means:** the risk was logged once during a workshop and never revisited — it will surprise the team when it materializes because no one is watching for the trigger.
- **First question:** "Who checks this, and on what date?"
- **Data to pull:** the RAID log filtered for entries with blank owner or trigger-date fields.

### RAG status is green but the underlying CPI/SPI numbers weren't recomputed this cycle
- **Usually means:** the status color is being carried forward from last period rather than freshly derived — a common failure when the reporting cadence outpaces the team's willingness to recompute.
- **First question:** "When were these numbers last recalculated against actuals?"
- **Data to pull:** the timestamp on the EVM table or burn-rate chart versus the status report date.

### Scope change requests arriving informally (email, hallway ask) rather than through the change-control process
- **Usually means:** business users or sponsors have learned the formal process is slow or gets rejected, so they're routing around it — the scope is growing without a corresponding schedule/budget adjustment.
- **First question:** "Has this been logged as a change request, or is it 'just a small thing' someone asked for directly?"
- **Data to pull:** count of scope changes implemented in the last month with no matching change-request ticket.

### Critical path hasn't been recalculated since the last monthly review despite 2+ material task changes
- **Usually means:** the reported end date is stale and may no longer reflect reality — a delay on a near-critical task may have consumed all its float without anyone re-running the network.
- **First question:** "What's today's float on the tasks nearest the critical path?"
- **Data to pull:** the current CPM network diagram with float values, dated.

### Contingency reserve drawn down more than 50% before the project reaches its midpoint
- **Usually means:** risks are materializing faster than planned, or the contingency was undersized at baseline — either way the reserve won't cover the remaining project at the current burn rate.
- **First question:** "At this draw-down rate, does the remaining contingency last to project end?"
- **Data to pull:** contingency ledger with draw-down dates and remaining balance.

### Team members report status only in verbal standups, with no written artifact trail
- **Usually means:** there's no auditable record if a dispute arises later about what was known and when — a governance gap, not necessarily a performance one.
- **First question:** "Where is this written down?"
- **Data to pull:** the last four weeks of status reports or standup notes, checked for gaps.
