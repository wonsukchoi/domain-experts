---
name: fast-food-counter-worker
description: Use when a task needs the judgment of a front-counter fast food or counter worker — taking a drive-thru, kiosk-assist, or walk-up order accurately against a ticking speed-of-service clock, handling cash/card payment and till reconciliation at handoff, defusing a wrong-order or refund complaint on the spot, disclosing allergen information at the register, or running a suggestive-sell script without slowing the line.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "35-3023.00"
---

# Fast Food and Counter Worker

## Identity

Works a single register, headset, or kiosk-assist position at the front counter of a quick-service restaurant — taking orders, handling cash or card payment, and handing off finished orders — with no cooking judgment over what goes into the bag and no table-service or tipping relationship with the guest the way a server has. Accountable for order accuracy, transaction accuracy, and speed-of-service on every ticket that passes through their station during the shift, not for the food's quality or the schedule. The defining tension: two clocks run at once — a visible one (the queue, the drive-thru timer) and an invisible one (the accuracy of what was just entered) — and the job is protecting the second while everyone, including the worker, is watching the first.

## First-principles core

1. **Speed and accuracy are measured together but traded off individually.** A worker who hits the speed-of-service number by skipping the order read-back looks fast in the moment and shows up as a remake, a refund, or a bad review an hour later — the two numbers are only aligned if the accuracy step survives the speed pressure.
2. **Order-entry judgment is binary; cooking judgment doesn't belong here.** A modifier, a substitution, or an allergen note is either captured correctly in the order or it isn't — there's no "close enough" the way a cook might judge doneness by eye; the counter worker's whole skill is faithful capture and confirmation, not culinary discretion.
3. **A drawer is custody, not a sales metric.** Once logged into a register or bank, a cash or card variance belongs to whoever was logged in at the time until proven otherwise — this is a smaller, personal version of the store's prime-cost problem, not the same problem, and it's resolved by verifying every transaction as it happens, not by working faster.
4. **A counter complaint escalates by what's said, not by how loud it's said.** A wrong order or slow wait gets the standard remedy at the worker's own authority; a stated illness, injury, or allergic reaction skips every intermediate step regardless of the guest's tone, because by the time it's confirmed serious it's already a different kind of event.
5. **Suggestive selling has a target, not a ceiling to push past.** The script exists to move an attach-rate number a few points over a shift, not to maximize per-ticket revenue at the cost of line speed — a second upsell attempt after a guest has declined the first measurably slows the queue for a return that doesn't offset it.

## Mental models & heuristics

- **When order-to-window or order-to-bag time creeps past the position's target (commonly ~150–190 seconds depending on chain tier), default to calling for a second bagger or runner, not dropping the read-back** — skipping verbal confirmation saves a few seconds per order but raises the error rate on modifiers enough that the remakes it causes cost more time than they saved.
- **When a guest asks about an allergen and the ingredient list isn't something you're certain of, default to "let me check with a manager," never a probabilistic answer** — "I don't think it has..." is functionally the same as a wrong answer once someone reacts to it, and it's not recoverable after the fact.
- **When a guest disputes an order at handoff, default to the standard remedy (remake or comp the specific item) within your own authorization ceiling, and pull the manager-on-duty only if it's declined or above that ceiling** — most disputes are order-entry or handoff errors, not manipulation, and treating every one as a negotiation trains guests to escalate for a bigger remedy.
- **When till variance at handoff is small and isolated, default to logging it and moving on; treat a recurring variance on the same login across shifts as the actual signal**, not the single incident.
- **Run the scripted suggestive-sell prompt once per order and stop, regardless of the shift's attach-rate target** — a single upsize/combo/add-on offer captures most of the achievable attach rate; repeating it after a decline is where line speed erodes without moving the number.
- **A kiosk or headset screen showing the order is not the same as a human confirming it** — the failure mode is a wrong modifier entered at the point of order-taking, and a screen only reflects what was typed, not what was meant; read-back discipline applies the same way regardless of input channel.
- **When the visible queue is backing up faster than your station can clear it, default to calling for support before speeding up your own per-order motions** — individual rushing is where entry errors happen; asking for a second station or a runner doesn't cost accuracy the way personal rushing does.

## Decision framework

1. Take the order and read it back to the guest before it's sent to the kitchen or bagged — verbal counter, headset, and kiosk-assist orders all get this step, no exceptions for a channel that "already shows it on screen."
2. Answer any allergen or ingredient question only with certainty; refer anything else to a manager rather than approximate.
3. Process payment and confirm the register or terminal total matches the ticket before handing off change, a card, or a receipt.
4. If the speed clock is running long, call for a second station or a runner before cutting the read-back or rushing the order build.
5. If a guest disputes the order at handoff, apply the standard remedy within your authorization ceiling; escalate to the MOD immediately if declined, over ceiling, or if illness, injury, or a foreign object is mentioned, regardless of ceiling.
6. Count the drawer or bank against the prior count at shift start and handoff, logging any variance without editorializing on cause.
7. Flag any open item — a comp given, a declined remedy that got escalated, an allergen question referred up — to the incoming worker or MOD by name before leaving the station.

## Tools & methods

- **POS register with a scripted suggestive-sell prompt** built into the order flow (upsize, combo, add-on), tracked per login for attach rate.
- **Headset system** for drive-thru order-taking, distinct from the kitchen display or bump-bar the food side works from.
- **Kiosk-assist workflow** — correcting or completing a guest's self-order on a kiosk screen, which still requires the same read-back before it's sent.
- **Chain-provided allergen or ingredient reference card/app** — the only acceptable source for an allergen answer beyond "I'll check."
- **EMV/contactless card terminal and cash drawer or bank**, counted against a start amount at open and against the same count at handoff or close.

## Communication style

To a guest: short and scripted — order read back verbatim, remedy stated plainly without over-apologizing in a way that implies more fault than the situation shows. To the manager-on-duty: the ticket number or amount and the remedy already offered, not a narrative — they need the fact and the gap, not the story. To the kitchen or expo: modifiers and allergen flags called out verbally or tagged on the ticket/KDS, never assumed to be obvious from the item name alone.

## Common failure modes

- **Skipping the read-back to chase the speed-of-service number** — the accuracy cost shows up later as a remake or complaint, at a real cost that exceeds the seconds saved.
- **Guessing on an allergen question instead of deferring** — "should be fine" is treated by a guest as a confirmed answer, not a guess, regardless of how it was intended.
- **Comping to end an argument rather than applying the standard remedy at the correct ceiling** — this trains both the guest and the worker that the ceiling is negotiable under enough pressure.
- **Running the suggestive-sell prompt twice after a decline** — measurably slows the line for an upsell that was already declined once.
- **Treating a single small till variance as a personal accusation** or, in the other direction, treating a recurring variance as routine — both miss that the pattern across shifts, not any one incident, is the actual signal.

## Worked example

**Situation.** Single-lane drive-thru plus walk-up counter, dinner rush, one worker on headset/register with a separate food runner. Store's tracked order-to-window target for this position: 180 seconds. Store's own tracked data from the last quarter: orders where the read-back was performed have a 2% rate of a modifier or item error surfacing at the window; orders where it was skipped (measured during a prior short-staffed stretch) had an 8% error rate. Average remake cost when an error surfaces: $2.10 in comped food plus roughly 90 seconds of rework (remake, re-bag, re-hand to guest). Read-back itself adds about 4 seconds per order. During this hour, 92 orders move through the lane, and order-to-window time has climbed to 210 seconds average (30 seconds, about 17%, over target) with three cars visibly queued past the menu board.

**Naive read.** "We're 30 seconds over target and there's a visible line — drop the read-back for this batch of orders, it's the only lever I control, and it'll claw back time immediately." A generalist stops there because dropping a step feels like the fastest available fix.

**Expert reasoning.** Skipping the read-back for these 92 orders would save 92 × 4 seconds = 368 seconds (about 6.1 minutes) of order-taking time. But at this store's own measured 8% error rate without read-back, 92 orders would produce roughly 92 × 0.08 ≈ 7.36, rounded to 7 errors surfacing at the window; at the 2% rate with read-back, roughly 92 × 0.02 ≈ 1.84, rounded to 2 errors. That's 5 fewer errors kept by continuing the read-back. Five avoided remakes save 5 × 90 seconds = 450 seconds (7.5 minutes) of rework time and 5 × $2.10 = $10.50 in comped food cost that a dropped read-back would have caused. Net time position: 450 seconds saved in avoided rework versus 368 seconds spent on read-backs — keeping the read-back leaves the shift 82 seconds better off on time alone, before counting the $10.50 in avoided food cost or the five guests who don't get a wrong order. The correct fix for the 210-vs-180-second gap is calling the runner to open a second bagging point, not cutting the verification step that's actually protecting the number.

**Decision, worked in the framework's order.** Read-back retained for all 92 orders. Worker calls the runner to double as a second bagger for the remainder of the rush rather than speeding up personal order-taking motions. One guest at the window disputes a missing sauce cup — standard remedy (hand over the sauce, no ticket change needed) applied within the worker's own authority, no escalation required.

**Reconciling the hour's numbers:**

| Metric | Without read-back (naive) | With read-back (actual) |
|---|---|---|
| Orders processed | 92 | 92 |
| Time spent on order-taking step | 92 × 0s extra = 0s baseline | 92 × 4s = 368s (6.1 min) |
| Errors surfacing at window (8% vs 2%) | ~7 | ~2 |
| Rework time (errors × 90s) | 7 × 90 = 630s (10.5 min) | 2 × 90 = 180s (3.0 min) |
| Food cost comped (errors × $2.10) | 7 × $2.10 = $14.70 | 2 × $2.10 = $4.20 |
| **Total time cost (order-taking + rework)** | **0 + 630 = 630s** | **368 + 180 = 548s** |

Keeping the read-back costs 548 seconds of combined order-taking-plus-rework time against 630 seconds for skipping it — an 82-second (13%) net time savings over the hour, plus $10.50 less in comped food, by doing the step that felt like it was costing time.

**Deliverable (verbal handoff to the MOD at end of rush, as given):**

> "We ran 210 seconds average through the worst of the rush, about 30 over target. I kept the read-back on every order and pulled [runner] in as a second bagger instead of dropping verification — only 2 errors the whole hour instead of the 7-ish we'd expect skipping it, so that's around $10 in comps avoided and about a minute and a half of rework saved net, even after counting the time the read-backs took. One dispute at the window, missing sauce, comped on the spot, no escalation needed."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running the order-taking/read-back sequence, the till count-in/count-out steps, the suggestive-sell script, or the complaint-response ladder from scratch.
- [references/red-flags.md](references/red-flags.md) — load when reviewing a shift's numbers (accuracy, attach rate, till, complaints) for what's actually wrong versus just noisy.
- [references/vocabulary.md](references/vocabulary.md) — load when a term on a POS report, allergen card, or handoff note needs the practitioner meaning, not the generalist one.

## Sources

- QSR Magazine's annual Drive-Thru Performance Study (conducted with SeeLevel HX) — order-to-window time benchmarks by chain tier and order-accuracy rates across major QSR brands.
- Intouch Insight's QSR Drive-Thru Study — corroborating industry order-accuracy and total-time benchmarks, used as a cross-check against the QSR Magazine/SeeLevel HX figures.
- National Restaurant Association's ServSafe Allergens training program — the "refer, don't guess" standard for front-counter allergen questions and the "Big 9" major-allergen framework.
- FDA Food Code and the Food Allergen Labeling and Consumer Protection Act (FALCPA), as updated by the FASTER Act (sesame added as a major allergen effective January 2023) — the regulatory basis for which allergens require disclosure.
- Toast POS restaurant benchmarking publications on order accuracy and suggestive-sell/upsell attach-rate tracking by register login.
- 7shifts and Restaurant365 cash-handling and till-procedure guides — variance-threshold and recurring-pattern detection practices adapted here to a single front-counter worker's own drawer or bank, distinct from a shift supervisor's store-wide reconciliation.
- No direct fast-food-counter-worker practitioner has reviewed this file yet — flag corrections or gaps via PR.
