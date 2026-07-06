# Red flags — what a project management specialist notices instantly

Any one of these can be innocent. Two or three together, especially clustered around one work package or one status cycle, is a pattern.

### "90% complete" reported for 3+ consecutive status cycles
- **Usually means:** % complete is being estimated from time elapsed or effort spent, not from objective, pre-defined completion criteria — the classic "90% done" syndrome where the last 10% is actually the hardest, least-defined part of the task.
- **First question:** "What are the specific, named remaining deliverables for this task, and what % of BAC do they represent?"
- **Data to pull:** task-level completion criteria from the WBS dictionary, EV calculation method used for this task (0/100, 50/50, or % complete self-reported), prior 3 status reports for the same task.

### CPI or SPI below 0.90 for 2+ consecutive reporting periods
- **Usually means:** a real, structural variance — vendor rate change, scope creep absorbed silently, or a resourcing gap — not statistical noise. Below this threshold twice in a row rules out "it's just a blip."
- **First question:** "Which specific work package is driving this, and does the RAID log already have it logged as a risk or issue?"
- **Data to pull:** work-package-level EVM breakdown (not the project roll-up), RAID log entries dated before the variance appeared.

### Contingency reserve drawn down >50% while project is <30% complete (by EV/BAC)
- **Usually means:** the original estimate under-scoped known risks, and the "well-managed risk" story is actually an estimating error surfacing early — or a PM is quietly using contingency to cover scope creep instead of routing it through change control.
- **First question:** "Walk me through each draw — which ones map to a specific, previously scored risk, and which don't?"
- **Data to pull:** contingency drawdown log with risk-ID cross-references, change control log for the same period (checking for undisclosed scope changes funded from contingency).

### A risk score unchanged for 3+ consecutive status cycles
- **Usually means:** either the risk actually resolved and nobody updated the register, or nobody is re-assessing it and the register has become theater.
- **First question:** "When did anyone last actually re-evaluate probability and impact on this one, versus just copy the row forward?"
- **Data to pull:** RAID log version history / edit timestamps, owner's last comment or update on the item.

### Schedule shows 0 tasks with negative float and 0 tasks past due, but delivery dates keep slipping anyway
- **Usually means:** the schedule's logic is broken (missing predecessor/successor links, especially near the end of the plan) so the tool isn't actually computing a real critical path — it's reporting slack that doesn't exist in reality.
- **First question:** "When was the schedule logic last audited — missing links, leads, high-float outliers?"
- **Data to pull:** schedule health check (missing logic %, leads %, high-float task list), compare against DCMA 14-point-style thresholds (missing logic ≤5%, leads = 0%).
- Note: >20% of a project's tasks (or of remaining-duration critical/near-critical tasks) showing float above roughly 20% of remaining project duration is the specific numeric tell that logic is missing, not that slack is real.

### The baseline schedule or budget changed without an entry in the change control log
- **Usually means:** someone rebaselined informally to make an ugly variance disappear before the next report — every EVM number computed after that point is now comparing against a baseline nobody approved.
- **First question:** "Show me the change control entry, approver, and date for this baseline revision."
- **Data to pull:** baseline version history, change control log, prior vs. current PV curve overlay (a jump with no corresponding CR is the tell).

### A change request sized just under the delegated tolerance threshold
- **Usually means:** either a genuine coincidence, or scope is being deliberately split into pieces to avoid CCB review (e.g., three $40K requests instead of one $120K request against a $42K/±5% tolerance).
- **First question:** "Are any of these related — same root cause, same work package, same requester, filed within the same reporting period?"
- **Data to pull:** change control log filtered by requester and work package over the last 2–3 cycles, not just the single CR in question.

### Status report RAG color stays green while the underlying EVM numbers (CPI/SPI) have been below 0.95 for 2+ periods
- **Usually means:** the RAG assessment is running on gut feel or optics management rather than the pre-agreed numeric thresholds — the report is telling the sponsor what they want to hear, not what the data says.
- **First question:** "What are this project's actual pre-agreed RAG thresholds, and does this month's CPI/SPI clear amber or red under them?"
- **Data to pull:** the charter or kickoff document defining RAG thresholds, last 3 status reports' stated color vs. the underlying CPI/SPI/risk-score data for the same periods.

### Sponsor or PM proposes adding headcount to recover a slipping schedule with <20% of the schedule remaining
- **Usually means:** Brooks's Law territory — new people add ramp-up and coordination cost before they add throughput, and there often isn't enough remaining schedule to recoup that cost.
- **First question:** "What's the ramp-up time for a new person on this work, and does it fit inside the time we're trying to save?"
- **Data to pull:** remaining schedule duration on the affected path, historical onboarding/ramp time for this project's tech stack or domain, current team's actual float/utilization (adding people to a not-actually-bottlenecked path helps nothing).
