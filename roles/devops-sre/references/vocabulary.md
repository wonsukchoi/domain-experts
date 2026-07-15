# SRE/DevOps working vocabulary

Terms an SRE uses precisely. Format: definition → how a practitioner says it → common misuse.

**SLI (Service Level Indicator)** — The specific metric being measured to assess service behavior (e.g., request latency, error rate, availability), the raw input the SLO is set against.
In use: "Our SLI here is the percentage of requests completing under 300ms — that's what the SLO target actually applies to."
Misuse: confusing the SLI (what's measured) with the SLO (the target for that measurement) — they're related but distinct concepts.

**SLO (Service Level Objective)** — The target value or range for an SLI over a period (e.g., "99.9% of requests succeed over a rolling 30 days"), set from actual user/business impact rather than from what's technically achievable.
In use: "The SLO is 99.9% monthly — that's 43.2 minutes of allowed downtime, not a vague aspiration."
Misuse: setting an SLO at the highest technically achievable number rather than the level actual users/business impact requires — over-shooting the right target wastes engineering effort that could go toward features.

**Error budget** — The allowed amount of unreliability implied by the SLO (100% minus the SLO, translated into actual time or request count), spendable on risk — when it's healthy, ship features and take risk; when it's exhausted, stop and fix reliability.
In use: "We've burned 80% of this month's error budget — 8.64 minutes left. That's the number driving the canary-only decision, not caution in the abstract."
Misuse: treating error budget as a slogan rather than an actual calculated number that gates specific go/no-go deploy decisions.

**Toil** — Manual, repetitive, automatable operational work with no enduring value, which scales with system growth until it consumes all available engineering time if not actively eliminated.
In use: "That's toil — we've done this same manual restart 40 times this quarter. It gets automated next sprint, not assigned to more people."
Misuse: labeling all operational work as toil, including work that requires genuine judgment or isn't actually repetitive/automatable — toil has a specific definition, not just "work I don't enjoy."

**MTTR (Mean Time to Recovery) vs. MTBF (Mean Time Between Failures)** — MTTR measures how fast a system recovers from failure; MTBF measures how often it fails. For user-perceived reliability, MTTR often matters more — frequent-but-fast-recovering systems can beat rare-but-slow-recovering ones on total user-affected time.
In use: "Our MTBF isn't great, but our MTTR is under 3 minutes — that's why user-perceived reliability is still solid."
Misuse: optimizing only for MTBF (fewer failures) while ignoring MTTR, missing that a system which fails rarely but takes hours to recover can have worse actual user impact than one that fails more often but recovers in seconds.

**Blast radius** — The scope of a system or user base affected if a specific change or failure goes wrong, the key variable canary/staged rollouts are designed to bound.
In use: "5% canary bounds the blast radius to a tenth of what a full fleet-wide deploy would risk if this fails."
Misuse: evaluating a change's risk only by its likelihood of failure without also considering how much of the system/user base would be affected if it does fail.

**Canary deployment** — Releasing a change to a small subset of traffic or instances first, observing it against defined signals and rollback triggers, before progressively expanding to the full fleet.
In use: "We're canarying this at 5% for 2 hours with an automatic rollback trigger before going to 25%."
Misuse: calling any staged process a "canary" without an actual automatic or clearly-defined rollback trigger — without that, it's just a slow rollout, not a true canary with a bounded-risk safety mechanism.

**Blameless postmortem** — An incident review process that treats the incident as a systemic/process failure rather than an individual's fault, on the premise that any complex system with humans in the loop will have incidents — the goal is honest reporting that surfaces the real cause, not assigning blame.
In use: "The postmortem action items target the missing alert and the ambiguous runbook step — not who was on call that night."
Misuse: running a "blameless" postmortem in name while the actual discussion or write-up still implicitly assigns fault to an individual, which teaches people to hide problems next time rather than report them early.

**Golden signals** — The four core metrics (latency, traffic, errors, saturation) considered the minimum observability baseline for any service; without visibility into all four, a service isn't considered properly observable regardless of how much logging exists.
In use: "We have logs but no saturation metric for this service — that's a golden-signals gap, not full observability."
Misuse: treating extensive logging as equivalent to observability; logs alone, without the four golden signals as structured metrics, don't give the fast, at-a-glance diagnostic view an incident requires.

**Infrastructure as code (IaC)** — Defining and managing infrastructure (servers, networking, configuration) through versioned, reviewable code (e.g., Terraform, Pulumi) rather than manual console changes, so production state is reproducible and recoverable.
In use: "That firewall rule change needs to go through the IaC repo and a PR, not a manual console click — otherwise it's drift the moment someone else touches this."
Misuse: making a "quick fix" manually in production and treating it as temporary, when in practice unreflected manual changes routinely become permanent, undocumented configuration drift.
