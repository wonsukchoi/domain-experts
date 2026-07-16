# Artifacts

Filled templates for the three documents a CTO produces most: the architecture decision record, the board technology update, and the build-vs-buy scorecard.

## Architecture Decision Record (ADR)

```markdown
# ADR-014: Payment retry queue — build on existing message bus vs. adopt Temporal

Status: Accepted
Date: 2026-03-02
Owner: CTO (final call), input from Payments lead + Platform lead
Reversibility: One-way door — migrating a workflow engine after adoption costs ~2 quarters

## Context
Payment retries currently live as ad-hoc cron jobs + manual DB flags. Two P1 incidents
in the last quarter traced to retries firing twice (duplicate charge, refunded) and not
firing at all (silent revenue loss, ~$14K over 9 days before detection).

## Options considered
1. Build retry/orchestration logic on the existing Kafka-based message bus.
   Cost: ~5 weeks, 2 engineers. Risk: reinvents workflow state machine semantics
   the team has already gotten wrong twice.
2. Adopt Temporal (workflow orchestration engine) for this and future stateful workflows.
   Cost: ~7 weeks, 2 engineers (incl. 1.5 weeks infra + on-call runbook), plus new
   operational surface to run in production.
3. Buy a managed retry/dunning vendor (e.g. embedded in payments processor).
   Cost: ~2 weeks integration, ~$1,800/mo. Risk: vendor's retry logic is opaque,
   can't customize dunning cadence per contract tier (a stated product requirement).

## Decision
Option 2 — adopt Temporal. The failure mode (double-fire, silent-drop) is a workflow
state machine bug, exactly the class of bug orchestration engines exist to eliminate,
and the team will need this primitive again for the subscription-proration workflow
already on next quarter's roadmap. Option 1 saves 2 weeks now and reintroduces the same
bug class next quarter. Option 3 fails the customization requirement.

## Consequences
New operational dependency: Temporal server, on-call runbook needed before launch.
Revisit trigger: if Temporal ops burden (pages/month) exceeds 2/month after Q2, escalate
whether a managed Temporal Cloud offering is worth the cost delta.
```

## Board technology update (excerpt, quarterly)

```markdown
## Engineering — Q1 2026

**Headline:** Shipped SOC 2 Type II (in progress, on track for May) and payment
reliability fix; deployment frequency up 40% QoQ after CI pipeline rework.

**Metrics** (DORA four keys, trailing 90 days):
- Deploy frequency: 3.2/day (was 2.3/day last quarter)
- Lead time for changes: 6 hours (was 11 hours)
- Change failure rate: 4% (was 9%)
- MTTR: 38 min (was 95 min)

**Risk called out this quarter:** Auth service has bus factor of 1 (single owner,
on PTO for 3 weeks in Q2). Mitigation: pairing rotation started, target bus factor 2
by end of Q2.

**Spend:** Infra spend up 12% QoQ ($38K -> $42.5K/mo), driven by Temporal adoption
(ADR-014) and increased staging environment count. Within budget.

**Asks of the board:** none this quarter.
```

## Build-vs-buy scorecard (filled example)

Decision: customer-facing feature-flag system.

| Criterion | Weight | Build (internal) | Buy (LaunchDarkly-class vendor) |
|---|---|---|---|
| Core differentiator? | — | No — flags are infra, not product | No |
| Time to first use | 30% | 6 weeks (1 eng) | 3 days (integration only) |
| Ongoing eng cost | 25% | ~0.2 FTE indefinitely (on-call, feature parity) | ~0 FTE, vendor-maintained |
| Cost at current scale | 20% | ~$0 direct, opportunity cost above | ~$450/mo at current MAU tier |
| Lock-in risk | 15% | None | Medium — SDK embedded in 40+ call sites; migration cost estimated 3 weeks if vendor fails |
| Feature completeness | 10% | Matches only what's built | Includes targeting, experimentation, audit log out of the box |
| **Verdict** | | | **Buy** — not a differentiator, 0.2 FTE ongoing cost alone exceeds vendor price within 4 months, lock-in risk is bounded and known upfront |

Rule of thumb applied: buy when (a) not the differentiator and (b) a vendor has multi-year
runway and a real SLA — both true here. Re-evaluate only if MAU growth pushes vendor cost
past the fully-loaded internal build cost (~$4,500/mo equivalent at 0.2 FTE), not before.
