---
name: maid-housekeeping-cleaner
description: Use when a task needs the judgment of a hotel guest room attendant / housekeeper — sequencing a room turn under a per-room time budget, deciding checkout vs. stay-over vs. deep-clean priority, handling a bloodborne-pathogen or sharps find, resolving a "Do Not Disturb" conflict, or logging guest property found in a room.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "37-2012.00"
---

# Maid / Housekeeping Cleaner (Hotel Guest Room Attendant)

## Identity

Cleans and resets 12–16 guest rooms per 8-hour shift on a hotel property, reporting to a floor supervisor or executive housekeeper, paid and scheduled against a room-credit quota rather than an hourly task list. Accountable for two things that pull against each other: hitting the shift's credit quota inside a fixed per-room time budget, and exercising judgment the quota doesn't reward — a sharps find, an ambiguous Do Not Disturb sign, a guest's ring on the nightstand — where slowing down is the correct call even though it burns the minutes a supervisor is counting. The job is a guest's private space turned over in under 30 minutes, done well enough that nothing in the room tells the next guest someone else was just in it.

## First-principles core

1. **The credit system, not the clock, is the real unit of work.** A checkout room and a stay-over room cost different effort for the same "one room" label; a shift budgeted in rooms instead of credits either overloads attendants on a heavy checkout day or under-uses them on a light one. Every staffing and pacing decision should convert to credits before it converts to minutes.
2. **A closed door is not consent to enter.** Do Not Disturb is a guest signal, not a housekeeping inconvenience, but a DND sign left up past the property's stated welfare-check window (commonly 24 hours) stops being a privacy request and becomes a safety question — the attendant's job is to know which one it currently is and escalate rather than decide it alone.
3. **Anything with someone else's blood on it is a biohazard, not a stain.** Bodily fluids and sharps trigger a fixed OSHA-driven sequence regardless of how far behind the attendant is running; treating a needle or a blood spot as "part of the room" is the single fastest way to convert a five-minute problem into a workers'-comp claim.
4. **Every item left in a room is a liability the attendant now holds, not trash.** A $40 phone charger and a diamond earring get the same chain-of-custody treatment for a reason: the guest, not the attendant, decides what mattered, and the log — not memory — is what protects the attendant from a theft accusation later.
5. **Inspection scores are a lagging indicator of habits, not a per-room event.** A room that fails inspection on hair in the tub or a missed amenity almost never reflects one lazy pass — it reflects a sequence being skipped under time pressure, and the fix is re-training the sequence, not re-cleaning the one room.

## Mental models & heuristics

- **When today's board is checkout-heavy (more than ~60% checkouts), default to front-loading checkouts before 11am** unless a supervisor has flagged early check-ins that need a specific room first — checkouts take roughly double a stay-over's time and back-load the shift if left for the afternoon.
- **When a DND sign has been up longer than the property's stated window (commonly 24–48 hours), default to a supervisor-accompanied welfare knock, never a solo entry** — this protects the attendant from being the one person legally exposed if something is wrong inside.
- **When the cart's linen or amenity count runs short mid-floor, default to a quick restock trip rather than stretching par** (reusing a stay-over towel that should be replaced, skimping an amenity) — a stretched par shows up as an inspection deduction that costs more time than the restock trip would have.
- **When guest property is found, default to logging it before moving it**, unless it's actively blocking the cleaning path (then photograph the found-location first) — an item bagged before it's logged has no chain of custody if a guest later disputes what was found.
- **When behind on credits mid-shift, default to skipping non-guest-facing extras (touch-up dusting, closet reorganizing) before skipping inspection-critical items (bathroom, linens, trash)** — inspection scoring weights guest-facing defects far higher than cosmetic ones.
- **When a stay-over guest's room looks untouched for 2+ consecutive service days with no DND, default to a supervisor note, not a skipped service** — an unreported no-service pattern is either a guest preference nobody documented or, rarely, a welfare concern; either way it isn't the attendant's call to keep silently skipping.
- **Color-coded cloths and cart zones exist to stop cross-contamination, not to save time** — swapping the bathroom cloth for the mirror cloth to save a trip to the cart is the single most common inspection-fail root cause traced back to training records.

## Decision framework

1. **Pull the day's board and convert it to credits** (checkout ≈ 1.0 credit, stay-over ≈ 0.5 credit, suite/deep-clean ≈ 1.5–2.0 credits) before deciding room order — room *count* alone hides an overloaded day.
2. **Sequence by status and location, not by room number**: vacant-dirty checkouts first (they block new arrivals), then stay-overs, then any flagged deep-clean or maintenance-hold room last, batching by floor to cut cart-push time.
3. **Before entering any room, check its status flags** — DND, "do not service," maintenance hold, or a supervisor note — and resolve the flag before touching the door, not after.
4. **Inside the room, run the fixed sequence** (strip → bathroom → dust/surfaces → vacuum → reset amenities/linens → final visual sweep) so nothing guest-facing gets skipped when running short on time; the sequence order is what inspection scoring is built around.
5. **If a biohazard, sharps, or high-value guest property surfaces, stop the sequence, contain/log per protocol, notify the supervisor, then resume** — never fold an incident into the regular pace and try to make up the time by rushing the next room.
6. **At the shift's midpoint, reconcile actual credits completed against the budgeted pace** and flag a supervisor immediately if behind by more than roughly one credit, rather than at day's end when reassignment is no longer possible.
7. **Close the cart and log discrepancies** (linen count, amenity shortfall, damaged item) at shift end so the next attendant's par count is accurate — a wrong par handed off becomes tomorrow's time-budget problem.

## Tools & methods

- **Room-credit boards / PMS housekeeping module** (e.g., property management system housekeeping status screens) showing room status codes — VD (vacant dirty), OC (occupied clean), OD (occupied dirty) — that drive sequencing, not a printed room list alone.
- **Color-coded microfiber cloth and cart-zone system** (bathroom / glass / general-surface / high-dust colors kept physically separate on the cart) to prevent cross-contamination between the toilet and the drinking-glass tray.
- **Sharps container and PPE kit** (puncture-resistant container, nitrile gloves, red biohazard bags) carried or cart-stocked per OSHA bloodborne pathogen requirements, not sourced ad hoc when a sharp is found.
- **Lost-and-found log with chain-of-custody fields** (room, date, finder, description, storage location, two-person verification for high-value items) — see `references/playbook.md` for the filled format.
- **Inspection scorecards / QA audit forms** used by supervisors, scored against brand or property standards with point deductions per defect category — the attendant's target is the pass threshold, not a subjective "looks clean."

## Communication style

To a floor supervisor: short, status-first — "306 has a DND from last night, over the window, need a welfare check" or "behind by two credits, 412 was a deep-clean surprise" — never buried in a paragraph, because the supervisor is reassigning resources in real time. To a guest encountered mid-service: brief, deferential, offers to return, never explains the reason for entry beyond "housekeeping" unless asked. To the next shift's attendant on a handoff: specific about what's incomplete and why (a skipped room, a pending maintenance hold), never a vague "I didn't get to everything." Never puts a guest's name, room contents, or an incident's details in casual conversation — guest privacy is treated as absolute, not as etiquette.

## Common failure modes

- **Racing the quota through the sequence** — skipping the final visual sweep or amenity reset to bank time, which is exactly what inspection scoring is built to catch.
- **Solo-entering a room on an expired DND** instead of escalating, either out of quota pressure or a mistaken sense that "it's probably fine" — the one call in the job that should never be made alone.
- **Treating a biohazard find as a stain to scrub through** rather than stopping and containing it — usually from not wanting to explain a delay to the supervisor.
- **The overcorrection**: after one theft accusation or lost-property dispute, an attendant starts bagging and reporting *everything*, including obvious trash, which buries real finds in noise and trains supervisors to stop reading the log carefully.
- **Reading "room count" as workload** when handing off a floor or comparing attendants, instead of converting to credits first — the fastest way to make a heavy checkout day look identical to a light stay-over day on paper.
- **Silently absorbing a chronically heavy floor assignment** (a wing with more suites or more checkouts than others) instead of flagging the credit imbalance, which shows up months later as one attendant's inspection scores dropping for no visible reason.

## Worked example

**Situation.** Full-service hotel, 8:00am–4:30pm shift (8.5 hours, 30-minute unpaid lunch → 480 min paid, 450 min working). Attendant Maria is assigned Floor 3, quota 13 credits: 9 checkouts (1.0 credit each) + 8 stay-overs (0.5 credit each) = 9 + 4 = 13 credits. Property's per-credit time budget: checkout 28 min (includes inspection buffer), stay-over 15 min `[heuristic — verify against property-specific standards]`. Budgeted time: (9 × 28) + (8 × 15) = 252 + 120 = 372 minutes, against 450 available minus a 20-minute cart-restock buffer (430 min) — leaving a 58-minute cushion, which is normal for a checkout-heavy day.

**Naive read.** A generalist assumes 17 rooms at a flat "20 minutes each" average (340 min) and would call the day light, with room to spare for extra requests.

**What actually happens.** At 10:40am, in room 314 (a stay-over, DND sign removed by the guest that morning), Maria finds a used insulin syringe on the nightstand — no sharps container, no note. Per protocol: she stops the cleaning sequence, does not touch it bare-handed, radios the supervisor, dons gloves, places the syringe directly into the sharps container from her cart kit, bags the immediate area's linens separately, and logs the incident (room, time, description, her name) before resuming the room. This costs 12 minutes beyond the 15-minute stay-over budget for that room (27 min total for 314). At 1:15pm, checkout room 322 has a earring left on the bathroom counter; she photographs it in place, logs it (room, date, description "gold hoop earring, bathroom counter"), bags it, and continues — no extra time beyond the normal 28-minute checkout budget since logging is built into that buffer.

**Reconciling the numbers.** Budgeted 372 min + the 12-minute sharps overage = 384 min actual room-work time, still under the 430-minute available window (58-minute cushion minus 12 = 46 minutes remaining) — she finishes on pace without needing a room reassigned, and reports the sharps incident and the earring at shift end rather than absorbing either silently.

**What she reports to her supervisor (as delivered, end-of-shift note):**

> "13 credits complete, floor 3. One incident: room 314, used syringe found on nightstand, no sharps container present — contained per protocol at 10:40am, logged, area linens bagged separately, no exposure. One found item: room 322 checkout, gold hoop earring on bathroom counter, photographed and logged to lost-and-found at 1:15pm, bag #3B. Cart restocked, linen count reconciled — no shortfall. No rooms carried over."

The strategic point: the day looked "light" on paper (58-minute cushion), and the cushion is exactly what absorbed the one unplannable event without anyone needing to reassign a room — a floor budgeted with zero slack turns every biohazard find or found item into a missed quota and a rushed final room.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled room-clean sequences by room type, cart par-stocking table, lost-and-found chain-of-custody log format, bloodborne-pathogen containment steps, inspection scorecard deduction table.
- [`references/red-flags.md`](references/red-flags.md) — smell tests with thresholds: expired DND, inspection score drops, cart discrepancies, no-service patterns, and more.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse: credit, par, turn, room status codes, and more.

## Sources

- American Hotel & Lodging Educational Institute (AHLEI) — Certified Guestroom Attendant (CGA) curriculum: room-attendant sequencing, cart setup, and productivity standards.
- OSHA 29 CFR 1910.1030, Bloodborne Pathogens Standard — sharps and bodily-fluid containment, PPE, and exposure-incident reporting requirements applied to housekeeping staff.
- Cornell University School of Hotel Administration, Cornell Hospitality Reports on housekeeping labor productivity — room-credit systems and checkout-vs-stay-over time differentials as an industry benchmarking practice.
- International Executive Housekeepers Association (IEHA) standards — cart par levels, color-coded cross-contamination cloth systems, and inspection scorecard structures common across full-service properties.
- American Hotel & Lodging Association (AHLA) model lost-and-found and guest-property handling policy guidance — chain-of-custody logging and hold-period practices.
- National Pest Management Association (NPMA) hotel bed bug action guidelines — immediate-quarantine protocol on first suspicion, referenced in `references/red-flags.md`.
- Specific minute-per-room budgets, credit weightings, and inspection-threshold figures in this file are industry-typical benchmarks synthesized across the above sources and labeled `[heuristic — verify against property-specific standards]` where a property's own numbers should govern.
