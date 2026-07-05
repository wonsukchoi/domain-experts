# PM Artifacts — Templates With Example Content

Real work products, filled in with plausible examples. Copy the structure, replace the content. The example product throughout is "Relay," a fictional B2B workflow tool (~4,000 weekly active accounts, $14M ARR).

---

## 1. One-page PRD

A PRD longer than a page and a half means the thinking isn't done yet. The build details live in tickets; the PRD exists so anyone can answer "why are we building this and how will we know it worked" in 90 seconds.

```
# PRD: Native Slack Notifications
Owner: J. Park (PM) · Eng lead: M. Osei · Status: Approved · Last updated: 2026-07-02

## Problem
1,400 of our 3,900 weekly active accounts pay for a Zapier workaround to pipe
Relay events into Slack. Support logs 30-40 tickets/quarter about workaround
breakage. Users are telling us with their wallets that they want to live in
Slack, not in our notification center (11% weekly open rate).

Evidence: Zapier integration telemetry, support tag `slack-workaround`,
6 discovery interviews (May 2026).

## Who
Team leads and ops managers on Growth and Scale plans. NOT individual
contributors (interviews showed ICs mute channel noise; leads triage from it).

## Success metric (written before build, not after)
Primary: ≥35% of workaround accounts switch to native within 60 days of GA.
Guardrail: notification-driven session starts don't cannibalize weekly digest
email opens by more than 10%.

## Solution outline (the "what," not the "how")
- Per-project Slack channel mapping, event-type filters
- Actionable messages: approve/reject inline for approval events
- Out of scope v1: DM notifications, Teams, custom message templates
  (each cut has a reason — see appendix — not just "later")

## Risks & open questions
- Slack app review adds 2-3 wks calendar time — start submission week 1
- Rate limits at our largest account's volume (~9k events/day): eng to spike

## Kill criteria
If <15% of workaround accounts switch by day 60, we misread the demand:
run 5 interviews with non-switchers before investing further.
```

What makes this work: the problem cites behavioral evidence (paid workarounds), the success metric has a number and a deadline, "who" excludes a segment explicitly, and there's a kill criterion — most PRDs omit the last two.

---

## 2. RICE prioritization table

| Candidate | Reach (accts/qtr) | Impact (0.25–3) | Confidence | Effort (eng-wks) | RICE |
|---|---|---|---|---|---|
| Native Slack notifications | 1,400 | 2 | 80% | 5 | 448 |
| Bulk-edit for workflows | 900 | 1 | 80% | 3 | 240 |
| SSO/SAML (blocks 4 enterprise deals) | 60 | 3 | 90% | 6 | 27 |
| Custom report builder | 40 | 3 | 50% | 12 | 5 |
| Dark mode | 2,000 | 0.25 | 50% | 4 | 62 |

**Honest caveats — read before trusting any of the numbers:**

- **Garbage in, garbage out.** Reach for Slack is measured (Zapier telemetry). Reach for report builder is a guess dressed as a number. Annotate which cells are measured vs. estimated; argue about the estimated ones.
- **Scores within ~2x of each other are noise.** Bulk-edit at 240 vs. dark mode at 62 is a real gap; 240 vs. 448 is worth a strategy conversation, not blind ranking.
- **RICE structurally punishes strategic bets.** SSO scores 27 but unblocks $700k of pipeline and is table stakes for moving upmarket. If strategy says "win enterprise," SSO jumps the queue and the table just documents the cost of that choice. That's the table doing its job.
- **Impact is the most-gamed cell.** Whoever wants the feature scores it 3. Fix: define what each level means in advance (3 = moves the primary metric >5%, 2 = 1-5%, 1 = <1%, 0.25 = polish).
- **Confidence should reflect evidence type:** 90%+ = shipped experiment or direct telemetry; 80% = strong behavioral signal; 50% = interviews only; below 50% = someone's opinion, go do discovery instead of scoring.

---

## 3. Product strategy one-pager

```
# Relay Product Strategy — H2 2026

## Where we play
Mid-market ops teams (50-500 employees) drowning in approval workflows
spread across email and spreadsheets. NOT enterprise (yet), NOT solo users.

## How we win
Fastest time-to-first-automated-workflow in the category: 12 minutes
median today vs. competitor onboarding measured in days. Every H2 bet
either widens this gap or removes a reason mid-market buyers churn.

## Current belief about the biggest problem
Retention cliff at week 3: accounts that build a 2nd workflow retain at
84%/6mo; accounts that don't, 31%. H2 is organized around getting
accounts to workflow #2.

## The 3 bets (now/next/later, not dated commitments)
NOW:    Templates gallery + Slack notifications (drive workflow #2)
NEXT:   Workflow analytics (leads ask "is this even working?")
LATER:  API/webhooks platform (pull, don't push — waiting on demand signal:
        trigger is 25+ accounts requesting within a quarter)

## What we are explicitly not doing in H2
Enterprise SSO/compliance work, native mobile app, AI workflow generation.
Each was considered; each loses to the week-3 cliff on opportunity cost.

## How we'll know the strategy is working (check monthly)
% of new accounts reaching 2nd workflow by day 21: 34% → target 50%.
```

The "not doing" section is the point of the document. A strategy that excludes nothing is a wish list.

---

## 4. Launch checklist

Scaled for a medium feature (Slack notifications tier). Cut ruthlessly for small ones; a copy change needs none of this.

```
T-2 weeks
[ ] Success metric + guardrail instrumented and VERIFIED firing in staging
    (the #1 postmortem finding is "we couldn't measure it after all")
[ ] Kill criteria and revisit date in the decision doc
[ ] Feature flag + rollout plan: internal → 5% → 25% → 100%, with owner
[ ] Support briefed; macros drafted for top 3 predicted questions
[ ] Pricing/packaging call made (which plans get it?) — in writing

T-1 week
[ ] Dogfood period done; sev-1 papercuts fixed or consciously accepted
[ ] Docs page drafted; in-app announcement copy reviewed
[ ] Sales enablement: one-paragraph "what changed, who cares" (not a deck)
[ ] Load/abuse check at largest-account volume

Launch day
[ ] Flag to 5%; watch error rates + guardrail metric for 24h
[ ] Announce internally BEFORE customers can (support finds out from
    tickets = process failure)

T+1 week / T+60 days
[ ] 25% → 100% per rollout plan
[ ] T+60: post-launch review against the pre-registered success metric.
    Outcome is one of: scale / iterate / kill. "We shipped it" is not an outcome.
```

---

## 5. Decision-doc formats

### Two-way door (reversible) — keep it to 10 lines, decide within a day

```
DECISION (2026-07-02): Default new workflow notifications to ON.
Type: Two-way door — one config flip to revert.
Context: 62% of users who miss their first approval never return that week.
Options considered: default on / default off + nudge / ask during onboarding.
Call: Default on. Evidence is thin but reversal is free.
Watch: unsubscribe rate. Revert trigger: >8% notification opt-out in 14 days.
Owner: J. Park. Revisit: 2026-07-16.
```

The discipline is the revert trigger — a number, decided now, so nobody relitigates from vibes later.

### One-way door (irreversible) — full doc, circulated 1 week, named approver

```
# Decision: Deprecate the Legacy API (v1)

Status: PROPOSED — comment by 2026-07-14 · Approver: VP Product
Type: One-way door. Once partners migrate, there is no going back;
      trust cost of reversal exceeds cost of not doing this.

## Decision proposed
Sunset API v1 on 2027-01-31. 6-month migration window, v2 parity by 2026-09.

## Why now
v1 serves 210 accounts (5%) but consumes ~20% of platform-eng maintenance
and blocks the queueing rework every H2 bet depends on.

## Options considered (with the one we're NOT picking argued honestly)
1. Sunset with 6-mo window (proposed)
2. Maintain both indefinitely — costs ~1.5 engineers/yr forever; rejected
   on opportunity cost, not on feasibility. It IS feasible. It's just worse.
3. Sunset in 3 months — saves 2 quarters, but 4 of the 210 accounts are
   >$100k ACV with annual IT change-windows; rejected on churn risk.

## Cost of being wrong
Churn exposure: 210 accounts / $1.1M ARR. Mitigation: white-glove migration
for top 12; measured checkpoint at T-3mo (if <50% migrated, extend window
rather than force).

## Dissent recorded
Sales leadership prefers option 2. Documented, heard, overruled — rationale
above. (Recording dissent beats pretending consensus existed.)
```

The difference between the two formats is deliberate: matching decision-process weight to reversibility is the whole point. Writing a 3-page doc for a default-toggle is as much a failure as Slack-messaging your way through an API deprecation.
