# Backend engineering working vocabulary

Terms a senior engineer uses precisely. Format: definition → how a practitioner says it → common misuse.

**p50/p99 latency** — Percentile latency measures: p50 is the median request latency, p99 is the latency below which 99% of requests fall — used together because they answer different questions (typical experience vs. worst-case tail).
In use: "p50 is fine at 40ms, but p99 is 800ms — that tail is what's actually causing the timeout complaints, not the median."
Misuse: reporting only average or p50 latency when investigating a performance complaint, missing that tail latency (p99, p999) is often what users and downstream timeouts actually experience as "slow."

**Rule of three (abstraction)** — The heuristic that an abstraction shouldn't be introduced until at least three concrete instances of the pattern exist, since two instances often look like a pattern but are frequently coincidental.
In use: "We have two places doing this — that's not three yet. Duplicate it again for now rather than abstracting on a guess."
Misuse: abstracting after seeing only one or two instances of a apparent pattern, producing a generalized structure that doesn't actually fit the third real instance when it appears, requiring a costly re-abstraction.

**YAGNI (You Aren't Gonna Need It)** — The extreme programming principle against building speculative functionality or abstraction for a need that hasn't materialized yet, applied to interfaces and infrastructure, not to keeping contracts stable.
In use: "We're not building a generic rules engine for hypothetical future promotion types — YAGNI. Ship the configuration schema for what Sales actually runs today."
Misuse: applying YAGNI to argue against keeping stable, well-designed API contracts or interfaces, when the principle is about not building unneeded implementation complexity, not about avoiding good interface design.

**Blast radius (software context)** — The scope of a system or user base affected if a specific change or component fails, a key factor in choosing deploy strategy (canary, feature flag) and failure-mode design.
In use: "Extracting this into a separate service increases blast radius — if it goes down, it takes the whole request path with it, versus today's contained, in-process failure."
Misuse: evaluating an architecture change purely on its benefits (scalability, separation of concerns) without considering how it changes the blast radius of a failure in that component.

**Reversibility (of a technical decision)** — How cheap and fast it is to undo a decision if it turns out wrong (feature flags, additive schema changes, small deploys), used as a design principle since predicting which decisions will be wrong is much harder than making wrong decisions cheap to reverse.
In use: "Ship this behind a feature flag — that makes the decision reversible in minutes if it's wrong, instead of betting on getting it right up front."
Misuse: treating all technical decisions as equally hard to reverse and applying the same heavy review/caution to a reversible change (a flagged rollout) as to a genuinely hard-to-reverse one (a breaking schema migration).

**Boring technology** — Deliberately choosing the well-understood, operationally battle-tested tool over a newer, more novel one, unless the novel tool solves a problem the team actually has today — treating novelty as something that has to earn its place, not a default preference.
In use: "We're using Postgres for this, not the new graph database — boring technology wins unless we have a graph-shaped problem we actually can't solve otherwise."
Misuse: choosing a new or trendy technology because it's interesting to work with (resume-driven architecture) rather than because the actual problem at hand requires capabilities the boring, well-understood option lacks.

**Observability triad (logs, metrics, traces)** — Three complementary signal types: logs (discrete events, what happened), metrics (aggregated counts/rates, how often/how much), and traces (request-scoped timing across services, where time went) — used together, not as substitutes for each other.
In use: "The trace showed where the 800ms went; the metric confirmed it's not a one-off; the log gave us the specific request's error detail — we needed all three."
Misuse: relying on only one signal type (commonly logs alone) to diagnose a production issue, missing what a metric's aggregate trend or a trace's cross-service timing would have shown.

**Canary rollout** — Releasing a change to a small subset of traffic or instances first, monitored against defined signals, before progressively expanding — a way of bounding blast radius on a risky deploy rather than releasing to 100% at once.
In use: "This ships to 5% of traffic first with automatic rollback on error-rate spike, not a full release."
Misuse: calling a staged rollout a "canary" without an actual monitored signal and rollback trigger — without that, it's just a slow full release, not a genuine bounded-risk canary.

**Correlation-then-causation debugging** — The practice of checking what changed (recent deploys, config changes) immediately before investigating other theories when something breaks, since a recent change is the most likely and checkable first suspect.
In use: "It broke 10 minutes after the deploy went out — the deploy is guilty until proven innocent, check that before theorizing about anything else."
Misuse: immediately theorizing about complex causes for a production incident without first checking the deploy/change log for what happened right before the incident started.

**Architecture decision record (ADR)** — A documented record of a significant technical decision, including the alternatives considered, the actual constraint/requirement driving the choice, and the reasoning — as distinct from an undocumented decision that later has to be reverse-engineered from the code.
In use: "The ADR for the auth module change documents why we chose an internal module boundary over a microservice, with the actual deploy-coupling numbers behind it."
Misuse: making a significant architecture decision without documenting the reasoning and alternatives considered, leaving future engineers to guess at why the current structure exists.
