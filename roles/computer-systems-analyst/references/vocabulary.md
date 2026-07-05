# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Requirement vs. specification

- **Definition:** a requirement states *what* the business needs and why (a capability, a constraint); a specification states *how* the system will provide it (a field, a workflow, an API contract).
- **In use:** "The requirement is 'approval required above the authority limit' — the spec is the SuiteScript workflow that enforces $10K/single-signer, $50K/dual-signer once finance confirms those are the actual limits."
- **Common misuse:** writing specs and calling them requirements — "the system shall have a dropdown with these five values" is a spec masquerading as a requirement, and it locks in an implementation choice before anyone checked whether it's the right one.

## Feasibility vs. desirability

- **Definition:** feasibility asks whether something *can* be done within technical, operational, economic, and schedule constraints (TELOS); desirability asks whether it *should* be done given competing priorities.
- **In use:** "Technically and economically feasible, yes — but it's not desirable this quarter given the ERP replatform already consuming the same integration team's capacity."
- **Common misuse:** conflating "we proved it's feasible" with "we should build it now." A feasibility study that doesn't separate the two lets a technically sound project jump the queue on the wrong basis.

## Gap analysis

- **Definition:** the structured comparison of current-state capability against target-state capability, producing a sized, classified list of what's missing — not a vague sense that "some things are different."
- **In use:** "The gap analysis puts 12% of requirements in custom-integration territory, concentrated in warehouse tracking — that's where the budget and risk actually sit, not spread evenly across the project."
- **Common misuse:** treating gap analysis as a one-time document instead of a matrix that gets revisited at each checkpoint; gaps discovered after the "analysis" is filed still count and still need an owner.

## Requirements traceability matrix (RTM)

- **Definition:** a live document mapping every requirement to its source, its classification, its design element, and its owner — the mechanism that prevents a requirement from being written down once and forgotten.
- **In use:** "Pull the RTM before design freeze — anything without an owner in the design-element column is orphaned and blocks freeze."
- **Common misuse:** building the RTM once during elicitation and never updating it as design decisions get made, so it becomes a historical artifact instead of the live source of truth it's meant to be.

## Point-to-point integration vs. middleware/ESB vs. API-led

- **Definition:** point-to-point connects each system pair directly (n systems → up to n(n-1)/2 connections); an ESB routes all traffic through a central bus; API-led builds reusable System/Process/Experience API layers that any consumer can call.
- **In use:** "At 14 point-to-point links we're past the point where direct connections make sense — consolidating to 6 canonical process APIs cuts both the connection count and the blast radius when one system changes its schema."
- **Common misuse:** picking a pattern based on vendor marketing rather than connection count and change frequency; an ESB is overkill for 3 systems, and point-to-point is a liability past roughly 8-10.

## Strangler fig (phased replacement)

- **Definition:** a migration pattern where the new system incrementally takes over functionality from the old one, module by module, until the old system can be retired — named for the plant that grows around a host tree and eventually replaces it.
- **In use:** "Finance/GL migrates first — lowest integration count, cleanest data — then order-to-cash, then warehouse last, so a bad first phase is recoverable before the highest-risk module."
- **Common misuse:** calling any phased rollout "strangler fig" even when phases aren't ordered by risk or reversibility — the pattern's value is specifically in sequencing low-risk-first so early failure is cheap to absorb, not just "doing it in pieces."

## Build vs. buy vs. customize

- **Definition:** three distinct maintenance-liability bets — build (full ongoing engineering ownership), buy/configure (vendor owns the roadmap, org adapts process), customize (vendor package plus org-owned code that must survive every vendor upgrade).
- **In use:** "Buy and configure for GL and AP — no differentiation there. Customize for license-plate tracking, because that process is a genuine warehouse-efficiency edge, not a legacy habit."
- **Common misuse:** defaulting to "customize" for every gap because it feels like the safest way to avoid business disruption, without pricing the ongoing cost of re-testing every customization against every future vendor upgrade.

## TELOS feasibility

- **Definition:** Technical, Economic, Legal/schedule (commonly split as Schedule and Operational), and Operational feasibility — four independent dimensions a project must clear, in the version used here: Technical, Economic, Operational, Schedule.
- **In use:** "Technical and economic pass. Operational fails at big-bang — training throughput can't cover 220 staff in one weekend. Schedule fails as requested. Two of four block approval as-is."
- **Common misuse:** treating feasibility as a single composite score (e.g., averaging four dimensions) instead of four independent gates — a strong economic case doesn't offset a genuine operational failure.

## Data profiling vs. data cleansing

- **Definition:** profiling measures the current state of the data (completeness, duplication, conflict rate) without changing anything; cleansing is the remediation work that follows once profiling has sized the problem.
- **In use:** "Profiling found 22% of the customer master flagged duplicate or conflicting — that's the number that sizes the cleansing gate, five weeks at one FTE."
- **Common misuse:** starting cleansing before profiling is complete, which means remediation effort gets estimated on a guess instead of a measured rate, and the "we're almost done" status is unverifiable.

## Interface control document (ICD)

- **Definition:** a specification of the data contract between two systems — fields, types, triggering events, and explicitly the error-handling and reconciliation behavior — not just a statement of which systems are connected.
- **In use:** "The ICD for the order-creation interface specifies that a tax ID not found in the cleaned customer master routes to a manual queue instead of auto-creating a new record — that's the rule that prevents the next duplicate-rate problem."
- **Common misuse:** writing an ICD that covers only the happy path, leaving error handling to be improvised in production by whoever is on call.

## Cutover vs. go-live vs. hypercare

- **Definition:** cutover is the technical act of switching systems; go-live is the point the business starts operating on the new system; hypercare is the defined, resourced period immediately after go-live with elevated support before returning to normal operations.
- **In use:** "Hypercare is two weeks with the integration team on standby and daily reconciliation checks — after that we step down to standard support, but not before."
- **Common misuse:** treating go-live as the finish line and under-resourcing hypercare, so the first real-world data-quality or integration issue lands on a skeleton crew.

## Reconciliation

- **Definition:** the check that confirms two systems agree on record count and value after an integration or migration event — a control, not a nice-to-have report.
- **In use:** "Nightly reconciliation compares closed-won opportunity count and value in CRM against created-order count and value in ERP; a variance over 0.5% triggers same-day investigation."
- **Common misuse:** treating reconciliation as an end-of-project report instead of an ongoing control with a defined variance threshold and response time.
