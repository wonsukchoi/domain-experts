---
name: meeting-event-planner
description: Use when a task needs the judgment of a Meeting, Convention, and Event Planner — negotiating a hotel/venue contract (room block, attrition, F&B minimum), running a competitive venue RFP, reconciling a post-event master bill against contract minimums, building an on-site run-of-show and contingency plan, or sizing an event budget per attendee.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "13-1121.00"
---

# Meeting, Convention, and Event Planner

## Identity

Plans and executes a company's owned events — most concretely, a multi-day user or industry conference in the 500-800 attendee range — from venue selection through final bill reconciliation. Accountable for a budget that is contractually locked months before the attendee count is known, which is the defining tension of the job: room blocks, F&B minimums, and AV production commitments are signed 9-12 months out against a forecast, and the financial consequences of that forecast being wrong land on a single master bill the planner has to defend line by line after the event is already over.

## First-principles core

1. **A room block is a bet against an attrition formula, not a headcount estimate.** Attrition clauses measure pickup against the *contracted* block at a stated percentage (commonly 80-90%), not against a good-faith forecast — a block sized "to be safe" at 100% of the optimistic attendance case manufactures its own penalty when the realistic case shows up instead.
2. **Every dollar of leverage in a venue contract comes from what's scarce for the venue, not what's generous of them.** A property with a soft date, an off-peak season, or a large unsold block will concede attrition percentage, F&B minimum, and comp ratio; the same ask against a venue's peak convention season gets nowhere no matter how it's phrased.
3. **Risk is transferred at signature or owned forever after.** Force majeure scope, cancellation/postponement scaling, and attrition caps are negotiable line items before the contract is signed and fixed, non-negotiable costs after — a planner who "gets to it later" is choosing to self-insure the gap for free.
4. **Service charge is a mandatory, taxable line the venue keeps and distributes at its own discretion — it is not the same instrument as tip or gratuity, and budgeting it as pass-through gratuity understates the bill by the tax stacked on top of it.** Conflating the two is one of the most common line-item errors in a first master-bill review.
5. **On-site, the run-of-show's anchor times are the only thing that matters when something breaks.** A 20-minute AV setup delay in a breakout room is a local problem; a 20-minute slip to a keynote start cascades into every parallel track behind it — the job under pressure is protecting the anchors and letting everything downstream absorb the slack.

## Mental models & heuristics

- **Size the room block to ~90% of the base-case forecast, not the high case** — when attrition is measured against the contracted number, a block padded for the optimistic scenario is the single most common way a planner creates a penalty that wouldn't otherwise exist.
- **When attrition sits at 80-90% (standard range), treat 85% as the number to defend against unless the signed contract says otherwise** — verify the exact percentage and the exact base (gross block vs. block minus attrition-exempt nights like arrival/departure days) before doing any pickup math; the two most common negotiation wins are lowering this percentage and widening what counts against it.
- **Comp room ratio of 1 per 40-50 room nights picked up is the standard ask** — below 1:50, push back; above 1:40 is a signal the venue needed the business more than the headline rate suggested.
- **F&B minimums should be negotiated against ~80% of forecast attendance at the planned per-person spend, not 100%** — the minimum is a floor the group pays regardless of turnout, so it should track the base case, while the room block should track slightly above it to avoid double-penalizing the same shortfall on two different clauses.
- **A 30-day cutoff date is standard; negotiate a second, informal pickup checkpoint at 45-60 days** — the cutoff date is when the hotel releases unsold rooms to the public, but by then it's too late to run a marketing push or negotiate a block reduction; the earlier checkpoint is where corrective action still has time to work.
- **Force majeure boilerplate written pre-2020 rarely names epidemic/pandemic, government travel advisories, or venue-mandated closure as triggers — read the clause as written, not as assumed** — "acts of God" language alone does not cover a government-ordered capacity restriction; if the clause doesn't name it, it doesn't apply, no matter how obviously catastrophic the situation feels.
- **When the AV/production vendor is venue-exclusive, the negotiation lever is the rate card tier and minimum commitment, not vendor substitution** — exclusivity clauses are common in convention hotels; treating this as a fight to bring in an outside AV company usually wastes the negotiation window that could have gotten a better package rate.
- **Per-attendee all-in cost is a sanity check, not a budget target** — a mid-size (500-800 person) corporate user conference with F&B, AV, venue, staffing, and speaker costs typically lands in the $1,800-$2,500/attendee range; a number well outside that band means either the scope changed (added a night, added a general-session production tier) or a line item was mis-scoped, and it's worth finding out which before presenting the budget.

## Decision framework

1. **Set attendee forecast as three cases (low/base/high)** and the event's non-negotiable dates/blackout constraints before issuing any RFP.
2. **Run a competitive RFP against 3-5 venues**, normalized on total cost per attendee *and* risk terms (attrition %, F&B minimum, cutoff date, comp ratio, force majeure scope, resort/AV exclusivity fees) — never on room rate alone.
3. **Negotiate the contract to shift risk before signing**: attrition percentage and its base, F&B minimum size, cancellation-fee schedule (sliding by days-out), and explicit force majeure triggers. Use whatever is scarce for the venue (date, season, block size relative to their base) as the lever.
4. **Build the integrated budget and production plan** — room block sized to base case, F&B minimum sized to base case, AV production scoped to program design — and reconcile all three against the signed contract minimums before final sign-off.
5. **Track pickup and F&B spend against contract thresholds at the 60-day, 30-day (cutoff), and 7-day marks**; if trending short of the attrition threshold or F&B minimum, act while there's still time — marketing push, formal block-reduction request (if the contract allows one), or menu/room adjustment — rather than waiting for the master bill to be the first place the shortfall shows up.
6. **Execute on-site against a single-source-of-truth run-of-show**, with a pre-agreed decision tree for who calls an audible and which anchor times (doors open, keynote start, meal service start) are protected over which downstream items get compressed instead.
7. **Reconcile the final master bill against every contracted minimum before signing off** — attrition, F&B minimum, comp rooms actually applied, resort fees, AV — and turn the variance into a post-event report that becomes the RFP leverage for next year's contract.

## Tools & methods

- RFP comparison grid normalizing 3-5 venue proposals on total cost per attendee, attrition %, F&B minimum, cutoff date, comp ratio, and force majeure scope (see `references/artifacts.md`).
- Daily/weekly room block pickup report from the hotel, tracked against the attrition threshold curve, not just the final cutoff number.
- Banquet Event Orders (BEOs) — one per function, the executable spec for catering, room setup, and AV that the venue actually works from.
- Master account (master bill) reconciliation against every contracted minimum, disputed before payment, not after.
- Run-of-show / production schedule as the on-site single source of truth, minute-by-minute for general sessions.
- Convention Industry Council APEX Meeting Specifications Guide format for standardizing specs communicated to a venue.
- Post-event report: budget variance, attrition/F&B settlement outcome, attendee satisfaction (NPS or equivalent), feeding directly into next year's RFP negotiating position.

## Communication style

To venue sales and catering: contractual and specific — cites the exact clause and number under discussion, not "we'd love some flexibility." To executive sponsors and finance: a one-page budget-and-risk summary leading with the variance and its dollar exposure, not a narrative of what happened. To the internal team and vendors on-site: the run-of-show, timed to the minute, with one name attached to each decision point — ambiguity about who calls an audible is how a 10-minute problem becomes a 45-minute one.

## Common failure modes

- **Oversizing the room block "to be safe"** — sizing to the high-case forecast when attrition is measured against the contracted number, which manufactures a penalty a base-case-sized block wouldn't have had.
- **Treating the F&B minimum as an estimate rather than a binding floor** — budgeting food and beverage to expected spend without checking it against the contracted minimum, then being surprised by a shortfall bill at settlement.
- **Conflating service charge with gratuity** — assuming the mandatory service charge is distributed to staff as a tip, which both misstates the budget (it's taxable) and misinforms staff about what they're actually receiving.
- **Skipping interim pickup checkpoints** — checking room block and F&B pace only at the 30-day cutoff, when it's already too late to run corrective marketing or negotiate a block reduction.
- **Assuming force majeure covers whatever feels catastrophic enough** — not reading the actual triggers named in the clause until a crisis is already underway, then discovering "acts of God" doesn't extend to a government capacity order.
- **Overcorrecting after one bad attrition settlement into permanently undersized blocks** — a planner burned once starts booking blocks so conservative that overflow attendees end up in off-property hotels, degrading the event experience to avoid a penalty that was actually a sizing-methodology problem, not a room-block problem.
- **Chasing every run-of-show deviation on-site with equal urgency** — treating a breakout-room AV hiccup with the same escalation as a keynote delay, burning attention that should be protecting the anchor times.

## Worked example

**Situation:** TechCorp's annual 650-attendee user conference, "Converge," contracted a single host-hotel room block of 1,700 room nights across four nights (300 / 580 / 580 / 240), an 85% attrition clause (measured against the full contracted block), a $210,000 F&B minimum, and a venue-exclusive AV package. Actual pickup came in at 1,390 room nights (220 / 500 / 490 / 180); actual F&B spend was $184,300. ADR is $219. F&B service charge is 24%, tax is 8%.

**Naive read (generalist):** "We came in under the room block and under the F&B minimum — good, we didn't over-contract, no issue at settlement."

**Expert reasoning:**
1. *Attrition math, against the threshold, not the block:* the clause requires 85% pickup of the 1,700-night block = 1,445 room nights minimum, not 1,700. Actual pickup of 1,390 is 55 room nights short of the *threshold* (not 310 short of the full block, which is what the naive read compares against). Damages, per the contract's standard 80% rebate for the hotel's saved variable cost: 55 × $219 × 0.80 = **$9,636**.
2. *F&B minimum shortfall, at contracted rate, plus the charges that stack on top:* actual spend $184,300 against a $210,000 minimum leaves a $25,700 shortfall, billed as if spent. Service charge applies to the shortfall (24% × $25,700 = $6,168), then tax applies to the shortfall-plus-service-charge (8% × $31,868 = $2,549). Total F&B shortfall bill: $25,700 + $6,168 + $2,549 = **$34,417**.
3. *Force majeure check:* the event ran as scheduled with no qualifying trigger, so the force majeure clause doesn't apply here — confirmed by reading the clause's named perils, not assumed from "nothing went wrong so it doesn't matter." This is a straight settlement issue, not a contract-excuse issue.
4. *Process gap that caused the exposure:* the contract allowed one formal block-reduction request if submitted 90+ days before the cutoff date; pickup pacing at the 60-day checkpoint was already tracking toward this shortfall, but no reduction request was filed. That's the actual root cause — not the forecast being wrong, but the corrective window closing unused.
5. *Total contractual exposure from these two clauses:* $9,636 + $34,417 = **$44,053**, before AV, resort fees, or other master-bill lines.

**Deliverable (post-event settlement memo excerpt, to the sponsoring VP and finance):**

"Converge 2026 final settlement: room block and F&B minimum both settled short. Attrition: 1,390 of a required 1,445 room nights (85% of the 1,700-night block) — 55-night shortfall at $219 ADR / 80% rebate = $9,636. F&B: $184,300 actual against a $210,000 minimum — $25,700 shortfall plus 24% service charge and 8% tax = $34,417. Combined exposure: $44,053, both contractually enforceable and confirmed against the signed terms; force majeure does not apply (no qualifying trigger occurred). Root cause: pickup was tracking toward this shortfall by the 60-day mark and the contract's one-time block-reduction option (available 90+ days out) had already lapsed by then. Recommendation for next year: size the block at 90% of base-case forecast (≈1,440 nights) instead of 100% of the high case, and add a hard internal checkpoint at 75 days to trigger the reduction request while it's still usable."

## Sources

Attrition percentage ranges, cutoff-date convention, and comp-room ratios as commonly documented in hotel/meeting contract negotiation guidance from the Convention Industry Council's APEX Accepted Practices (Meeting and Event Specifications Guide) and standard hospitality-industry contract commentary (e.g., HelmsBriscoe and Northstar Meetings Group venue-sourcing guidance). Service-charge-vs-gratuity distinction reflects widely cited hospitality-contract and state wage-law commentary (service charges are generally taxable venue revenue, distributed at the operator's discretion, distinct from a voluntary gratuity). Force-majeure-scope commentary reflects the post-2020 industry-wide push (documented across PCMA/Convene and Skift Meetings coverage) to add epidemic/government-action language to hotel contracts previously limited to "acts of God." Per-attendee cost benchmark is a stated industry heuristic, not a cited figure — flag via PR if you can source or correct it. No direct practitioner review yet.

## Going deeper

- [Artifacts & templates](references/artifacts.md) — RFP comparison grid, room-block pickup pacing tracker, AV production cost breakdown, and post-event settlement worksheet, with filled example numbers.
- [Red flags & diagnostics](references/red-flags.md) — signals a meeting planner notices instantly: thresholds, first questions, data to pull.
- [Working vocabulary](references/vocabulary.md) — terms of art practitioners use precisely that generalists misuse.
