---
name: short-order-cook
description: Use when a task needs the judgment of a Short Order Cook — running solo diner-style service on a single flattop and fryer, sequencing tickets by doneness and zone instead of arrival order, managing par-cooked holds for bacon/sausage/hash browns against food-safety hold limits, deciding when to 86 an item mid-rush, or training a new hire to read doneness visually instead of by stopwatch.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "35-2015.00"
---

# Short Order Cook

## Identity

Runs the entire diner menu alone from one flattop and one fryer, with no expo layer and no station specialists to hand off to — every ticket, from three-egg omelets to a well-done burger, passes through one set of hands in whatever order the rail delivers it. Accountable for ticket-to-table time and plate accuracy, but the harder job is the one nobody assigns explicitly: deciding, ticket by ticket, which items can share a batch and which can't, because a wrong grouping stalls three tickets instead of one.

## First-principles core

1. **The cook is the entire kitchen's capacity plan, not one station in it.** In a brigade, a slow saute station is someone else's problem to route around. Here, every batching decision the cook makes *is* the kitchen's total throughput — there's no second cook to absorb a bad call.
2. **Doneness and zone group tickets; arrival order doesn't.** Two unrelated tickets that both want eggs over easy and bacon crisp can be fired as one batch; two items on the *same* ticket that need different zones (pancakes and bacon) can't be fired together just because they're on one slip. Grouping by cook-physics beats grouping by paper.
3. **Par-holding is a safety-bounded speed hack, not a shortcut.** Pre-cooking bacon or sausage partway and holding it above 135°F buys minutes per ticket, but the hold window is capped by food-safety limits and by taste — banking too much speed this way sells a worse plate.
4. **The griddle is three surfaces at three temperatures, not one hot rectangle.** A single flattop run at one temperature either scorches eggs or undercooks a burger — zone discipline is what lets one surface serve the whole menu at once.
5. **Speed happens inside the regulation, not around it.** Consumer-advisory doneness (eggs over easy, burgers under well-done) is a menu-posting obligation, but the cook still has to know exactly which orders trigger it and keep them out of standard batches — treating it as paperwork for someone else to worry about is how a batch gets contaminated with the wrong doneness.

## Mental models & heuristics

- **When 3+ tickets are stacked with overlapping eggs, bacon, or hash browns, default to zone-batching** — fire all same-doneness eggs together, all bacon-finishes together — **unless** a ticket carries a consumer-advisory doneness or an allergy flag, which gets pulled out and cooked alone.
- **When the par-hold reserve for bacon or sausage drops below roughly a quarter of shift par with 30+ minutes of rush left, default to starting a fresh batch immediately** — waiting for the reserve to hit zero guarantees an 8–10 minute raw-cook gap with no buffer behind it.
- **When a held batch has been sitting near the 4-hour hot-hold quality mark, default to discarding it even though it's still food-safety legal at 135°F+** — the "safe to serve" line and the "worth serving" line are different thresholds, and a diner's repeat business runs on the second one.
- **When a single ticket needs two items with different cook times, default to firing the longer item first and timing the shorter one to land with it** — never fire in ticket-line order; fire by finish time.
- **When the ticket rail shows an arrival burst, default to increasing how many items are in flight at once, not to moving faster on one ticket at a time** — per-ticket speed has a floor; concurrency doesn't.
- **Mise en place — useful for pre-rush setup, overused when it's stretched to items that lose quality held.** Bacon, sausage, and hash browns tolerate a safe partial-cook-and-hold; eggs don't, so "prep ahead" stops at the griddle's edge for anything egg-based.
- **When an item's remaining stock falls below expected demand for the rest of the rush at the current burn rate, default to 86'ing it then** — not at zero stock. Running out mid-ticket costs more goodwill than a preemptive 86 does.

## Decision framework

1. **Scan the rail before touching anything** — count tickets, items per ticket, and which griddle zone or fryer each item needs.
2. **Group by doneness and zone**, not arrival order — find which items across different tickets can share one batch.
3. **Check par-hold reserves against the burn rate for the remaining rush window**; refill or 86 before a reserve hits zero, not after.
4. **Fire the longest-cook item in each ticket first**, sequencing shorter items to finish at the same moment.
5. **Isolate any ticket needing a non-standard doneness, an allergy substitution, or a consumer-advisory item** from the batch groupings before it goes on the surface.
6. **Call plates the moment they're done and reset the zone**, instead of leaving a zone idle while waiting on one slow ticket elsewhere.
7. **At the end of the rush, log actual item usage against the starting par** and adjust the next shift's prep numbers from it, not from habit.

## Tools & methods

- **Zone-managed flattop**, checked with a probe or laser thermometer against the actual surface — not the dial setting, which drifts once cold product hits a zone in volume.
- **Steam table / bain-marie for TCS hot-holding** of par-cooked bacon, sausage, and hash browns — a heat lamp can't reliably clear the 135°F hot-holding floor.
- **The ticket rail itself as the queue** — there's no expo screen or line marker; the spindle or printer strip is the only shared state between cook and front of house.
- **Daily thermometer calibration (ice-point check)** before service, not a poster requirement — a two-degree drift on the probe cascades into every hold-time decision made off it that day.
- **Par-cook-and-hold technique for bacon/sausage** — partial cook to a safe hold state, hold above 135°F, finish to order in under two minutes — the industry's standard answer to needing a crisp product on a sub-10-minute ticket time without raw-cooking every strip to order.

## Communication style

Talks in short verbal calls, not written handoffs — repeats back what was heard when a ticket fires ("two over easy scattered, side bacon crisp") and calls the ticket "up" only once it's actually plated, never before. To a manager: reports the 86 list and par-usage numbers in the same two lines every shift, not a narrative of how busy it was. To a new hire: teaches by doneness cues — edge color, sheen, bubble pattern — because there's no time mid-rush to explain a stopwatch target, and stopwatch targets break the moment ticket volume varies from the training pace.

## Common failure modes

- **Working the rail strictly in arrival order under a burst** — falls behind because sequential per-ticket cook time is slower than the burst's arrival rate, not because the cook is working too slowly (see the worked example's queue math).
- **Par-cooking eggs to save time** — eggs held pre-cooked lose the texture that is the actual product, and a held batch can slip below 135°F for a while before anyone notices, unlike bacon which shows visible doneness cues.
- **Setting griddle zone temps once at shift start and never rechecking** — surface temp drops every time a cold batch hits a zone in volume; a mid-rush zone reading is often 20–30°F below the dial setting.
- **Overcorrecting after one bad run-out** — a cook burned once by running dry mid-rush starts over-prepping everything "just in case," which wastes held product and erases the margin the fast-ticket-time model depends on.
- **Waiting for a stock count of zero before calling an 86** — then stalling several tickets while the last few portions get stretched thin instead of announcing the cutoff early.

## Worked example

**Situation.** Solo cook, 24-seat diner, Saturday rush from 8:00–9:30am (90 minutes). Over the rush, 30 tickets fire, averaging 2.4 items per ticket — 72 items total (30 × 2.4 = 72). At 8:15, five tickets land within six minutes carrying 14 items between them (2.8 items/ticket in that burst — heavier than average because it's mostly egg-and-bacon-and-hash-brown combos).

**Naive read.** The manager on duty, watching the rail stack up at 8:15, tells the cook to "just go faster and take them in order." The math behind why that fails: if the cook worked tickets strictly one at a time and each ticket takes an average of 6 minutes of active cook attention, total capacity over 90 minutes is 90 ÷ 6 = 15 tickets — half of the 30 that actually arrive. Sequential, in-order cooking cannot physically clear this rush regardless of how fast any single motion is.

**Expert reasoning.** Ticket arrival rate over the rush: λ = 30 tickets ÷ 90 minutes = 1/3 ticket per minute. By Little's Law (L = λW), holding an average ticket-to-table time of W = 6 minutes requires an average of L = (1/3) × 6 = 2 tickets in flight simultaneously — not one. The cook hits this by zone-batching rather than by speed: eggs of the same doneness fired together in Zone B (375°F), bacon finishes batched together in Zone A (400°F) off a 40-strip par-hold started at 7:45am, hash browns par-cooked to the "scattered" stage and browned to order in 90 seconds in Zone C.

Bacon demand across the 72 items: 22 orders include bacon, several doubled, totaling 46 strips needed. The 40-strip opening par covers most of it; at minute 20 of the rush, during a two-minute lull, the cook starts a second 20-strip par batch, holding it above 135°F rather than raw-cooking the shortfall from cold (which would cost 8–10 minutes per strip and blow the 6-minute target). Total par-cooked across the rush: 40 + 20 = 60 strips; 46 used; 14 held over into the next lull, discarded at the 4-hour hold mark for quality rather than pushed into lunch service.

Net result: 30 tickets cleared in 90 minutes at an average ticket-to-table time of 6 minutes, with roughly 2 tickets in flight at any moment across three griddle zones — not by moving faster, but by making the queue physically shorter through concurrency.

**Deliverable (as called, live, at the rail):**

> "Firing four — two over easy scattered, one over medium smothered-and-covered, one scrambled dry, all with crisp bacon. Bacon's coming off par, eggs in ninety seconds."

**Deliverable (end-of-rush handoff note, left on the rail for the next cook):**

> Sat AM rush 8:00–9:30: 30 tickets / 72 items. Bacon: 60 strips par-cooked, 46 used, 14 held over — dumped at hold limit, don't reuse. Hash browns ran tight at 8:50, next par should start at +20 not +30. No 86s called. Griddle Zone A drifted to 370°F by 9:00 under load — recheck with probe before lunch, don't trust the dial.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled zone-temperature tables, par-hold reference numbers, a ticket-batching drill, and the 86 threshold calculation, worked with example numbers.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for a rush going sideways: what each one usually means, the first question to ask, and the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — terms of the station generalists misuse, including hash-brown modifier vocabulary and the difference between "fire" and "prep."

## Sources

- National Restaurant Association, *ServSafe Manager* coursebook and exam — TCS food temperatures, the 41–135°F danger zone, the 2-hour/4-hour cumulative-time rule, and hot-holding at or above 135°F.
- FDA Food Code (2022), §3-603.11 — the consumer-advisory requirement for undercooked/raw animal foods served to order (over easy eggs, under-well burgers); the posting obligation sits with the establishment's menu, not the cook individually, but the cook has to know which orders trigger it.
- Anthony Bourdain, *Kitchen Confidential* (Bloomsbury, 2000) — line-cook rail culture, the call-and-confirm ticket pattern, and what "in the weeds" actually signals versus ordinary busy.
- George Motz, *Hamburger America* (Running Press, 2008) and related diner-grill journalism — flattop zone management and griddle technique on classic short-order counters.
- Trade-press coverage of Waffle House University's cook-certification process (multiple outlets, e.g. Texas Monthly, Eater) — doneness-by-visual-cue training over stopwatch training, and the hash-brown modifier vocabulary as an operational sequencing language, not a menu gimmick.
- Little's Law (queueing theory; general operations-research knowledge) — applied here to ticket arrival rate, time-in-system, and items-in-flight.
- No direct short-order-cook practitioner has reviewed this file yet — flag corrections or gaps via PR.
