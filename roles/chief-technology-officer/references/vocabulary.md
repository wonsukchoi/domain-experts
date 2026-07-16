# Vocabulary

### One-way door / two-way door
A framing (Bezos) for decision reversibility: two-way doors are cheap to reverse and should be decided fast by whoever's closest; one-way doors are expensive or impossible to reverse and deserve slow, wide-input review.
**In use:** "This vendor contract is a one-way door — 3-year lock-in — so I want Legal and Finance in the room, not just Eng."
**Common misuse:** Labeling any decision that feels scary as one-way to justify slow-walking it, when the actual reversal cost is a sprint of work, not a quarter.

### Technical debt
The gap between the fastest-to-ship implementation and the "correct" one, framed as a financing decision with an interest rate (how fast it compounds) rather than a binary good/bad.
**In use:** "That shortcut has a low interest rate — it's isolated to one service — so it can sit for two more quarters."
**Common misuse:** Using it as a catch-all complaint for "code I don't like," disconnected from any measurable compounding cost.

### Bus factor
The number of people who, if unavailable, would leave a system without anyone who understands it well enough to operate or modify it safely.
**In use:** "Auth service is bus factor 1 — that's the risk I called out to the board this quarter."
**Common misuse:** Treating it as solved by documentation alone; bus factor requires a second person who has actually operated the system under pressure, not just read about it.

### Error budget
The allowed amount of unreliability (1 minus the SLO) treated as a spendable resource — when it's exhausted, feature work pauses for reliability work, by prior agreement.
**In use:** "We've burned 80% of this month's error budget in the first two weeks — new deploys are gated on Eng leadership sign-off until it resets."
**Common misuse:** Setting an error budget and never actually gating anything on it, which makes it a vanity metric instead of a governance tool.

### Conway's Law
Systems end up structured to mirror the communication structure of the organizations that build them, whether or not anyone designed it that way.
**In use:** "We keep getting a messy API boundary between these two services — that's because it's two teams, not one, drawing that line."
**Common misuse:** Citing it as an excuse for bad architecture rather than as a lever — the fix is often reorganizing the teams, not just refactoring the code.

### Change failure rate
One of the four DORA metrics: the percentage of deployments that cause a failure in production requiring remediation (rollback, hotfix, patch).
**In use:** "Change failure rate is at 4%, down from 9% — the new staging environment is catching more before prod."
**Common misuse:** Confusing it with incident count; a single bad deploy that triggers three cascading pages is one change failure, not three.

### MTTR (mean time to recovery)
Average time from an incident starting to service being restored, one of the four DORA metrics; a measure of operational resilience, not of how good the original code was.
**In use:** "MTTR dropped from 95 to 38 minutes once we added the auto-rollback trigger."
**Common misuse:** Optimizing MTTR by silently auto-restarting failing services without alerting anyone, which hides recurring problems instead of fixing them.

### RFC (request for comments)
A written proposal circulated for structured feedback before a cross-team technical decision is finalized, distinct from an ADR which records a decision already made.
**In use:** "Send the sharding RFC to Platform and Payments before Friday's review — I want objections in writing, not in the meeting."
**Common misuse:** Treating an RFC as optional theater after the decision's already been made informally; it stops being useful the moment feedback can't actually change the outcome.

### ADR (architecture decision record)
A short, permanent document recording a specific technical decision, the alternatives considered, why they lost, and the conditions under which it should be revisited.
**In use:** "That tradeoff is in ADR-014 — read it before reopening the Temporal-vs-build-it-ourselves argument."
**Common misuse:** Writing ADRs only for decisions that already have consensus, so the "alternatives considered" section is a formality rather than real analysis.

### Blameless postmortem
An incident review discipline that treats failures as a property of the system (design, process, incentives) rather than of the individual who happened to trigger them.
**In use:** "The postmortem found three separate systems that should've caught this before it reached the engineer who deployed it — that's where the fixes go."
**Common misuse:** Using "blameless" to avoid identifying that the same component or team keeps recurring across incidents — blameless applies to people, not to letting patterns go unaddressed.

### Platform team
In Team Topologies' vocabulary, a team that builds internal tools/infrastructure consumed by other engineering teams as a self-service product, distinct from a stream-aligned team that ships customer-facing value directly.
**In use:** "That's platform work — three product teams have hit the same auth-integration problem, it's time to fund a team to own it."
**Common misuse:** Standing up a platform team before 3+ consuming teams exist, which produces infrastructure built for a hypothetical future user instead of a real one.

### SLA vs. SLO vs. SLI
SLI (indicator) is the measured metric (e.g. request success rate); SLO (objective) is the internal target for that metric; SLA (agreement) is the external, often contractual, commitment with consequences for missing it — always looser than the internal SLO.
**In use:** "Our SLO is 99.95%, but the SLA we sign with customers is 99.9% — that gap is our safety margin."
**Common misuse:** Setting the external SLA equal to the internal SLO, leaving zero margin for the inevitable gap between target and reality.

### Blast radius
The scope of systems, users, or data affected if a given component fails or a given change goes wrong.
**In use:** "Before we roll this out globally, what's the blast radius if the migration script has a bug — all customers, or just the ones on the new schema?"
**Common misuse:** Estimating blast radius only for the intended failure mode, missing that a shared dependency (e.g. a common auth library) can turn a small change into a company-wide one.

### Vendor lock-in
The cost, in time or money, of switching away from a vendor after adopting their product deeply enough that switching requires significant rework.
**In use:** "The lock-in risk here is bounded — the SDK's isolated to 40 call sites, migration's a 3-week job if the vendor ever fails us."
**Common misuse:** Treating all lock-in as equally disqualifying, rather than quantifying the actual switching cost and weighing it against the switching cost of building the alternative yourself.
