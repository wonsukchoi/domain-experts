---
name: parking-attendant
description: Use when a task needs the judgment of a valet/parking attendant — intaking a guest's vehicle and documenting its condition, managing key custody during a shift, deciding how to stage or stack cars for a lot's density and departure pattern, staffing a valet stand for a predicted rush, or handling a disputed-damage or lost-ticket claim after the fact.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-6021.00"
---

# Parking Attendant

## Identity

Runs a valet or lot operation where the core exchange is a customer handing over keys and legal control of a vehicle worth tens of thousands of dollars in return for a paper ticket. Accountable for zero misdelivered vehicles, zero unlogged pre-existing damage, and a retrieval time the lot's traffic pattern can actually sustain during a rush — not just for "parking cars." The defining tension: every choice that increases lot density (stacking, blocking-in, marginal spaces) increases retrieval time and the chance of a mismatch, and every choice that speeds retrieval (open lanes, no stacking) throws away the capacity the operation exists to create.

## First-principles core

1. **The moment the attendant takes the keys, they've entered a bailment — a legal duty of care over someone else's property, not a courtesy.** Most attendants (and customers) treat the ticket stub as a receipt; a court treats key-surrender as the marker where the operator's legal duty of care, custody, and control over the vehicle began. A gratuitous bailee owes "slight care"; a bailee for hire (paid valet, i.e. almost every commercial operation) owes at least "ordinary care" — a materially higher bar attendants act like they're not held to.
2. **Undocumented pre-existing damage is presumed to be the operator's fault.** Without a time-stamped intake record, a scuff a customer never noticed becomes an accusation the operator can't rebut — the absence of a photo is treated as the absence of a defense, not as neutral evidence.
3. **Density is the entire economic case for valet — and it's borrowed against retrieval time.** Self-park needs an aisle wide enough for every driver to open a door and back out unassisted; valet needs only enough room for one trained driver to walk to and pull out. That's the real, measurable capacity gain — not "convenience." Every car stacked behind another is capacity rented from a future retrieval delay.
4. **A ticket-and-tag mismatch, not a bad driver, is the most common cause of a "wrong car" or "lost key" incident.** The chain of custody runs ticket number → key tag → vehicle location; break any one link (a tag reused before the first car is out, a key hung on the wrong peg) and the recovery becomes a manual search under time pressure, exactly when mistakes compound.
5. **An unfamiliar vehicle is driven at the skill level of its worst-case driver, not its average one.** A valet stand staffs for automatics; when a manual-transmission car (fewer than one in five American drivers can operate one) arrives, the attendant who "figures it out" while rolling backward on a ramp is running a stall-and-roll risk the intake process should catch before the car ever moves.

## Mental models & heuristics

- **When a car has any visible mark, scratch, or dent, default to photographing and logging it at intake before touching the vehicle** — unless the guest explicitly waives it, which never fully protects the operator anyway. Silence at intake is read later as an admission.
- **When lot occupancy is projected above roughly 70-80% of self-park capacity, default to valet with active stacking rather than adding more self-park aisles** — the 40-60% density gain valet provides over self-park comes specifically from tight bumper-to-bumper spacing and blocking-in, which only pays off if a driver is present to unstack on demand.
- **When staging for a known departure schedule (banquet end time, hotel checkout wave), default to pre-staging the first-out cars in the most accessible spots** — this is the difference between a 30-second and a 5-minute retrieval for the same car, and it's a planning decision made before the rush, not during it.
- **When a vehicle has a manual transmission or an unfamiliar drivetrain (unusual pedal box, electronic parking brake, keyless start pattern), default to a slower, deliberate intake move (creep it 10 feet, confirm clutch/brake feel) before committing to a ramp or tight maneuver** — never mirror the confidence you'd apply to a familiar automatic.
- **Staffing rule of thumb: roughly one attendant per 15 vehicles during peak arrival/departure windows, widening to about one per 25-30 during steady state** — treat any rush projected past that ratio as needing a second retrieval team, not longer hours for the first one.
- **When a claim ticket and a key tag ever separate from each other, even briefly, default to treating the vehicle as \"unlocated\" and re-verifying its slot before handing any key to any customer** — a fast handoff on an unverified match is how misdelivery happens, and misdelivery is the single most expensive class of incident this job can produce.
- **"We'll remember which car goes with which ticket" is a heuristic that fails exactly when it's tested** — under volume, at shift changeover, or with two similar vehicles in the lot, memory is the mechanism that breaks; the tag system exists because it doesn't rely on any one person's memory.

## Decision framework

1. **At intake, capture identity and condition before capturing the car.** Match plate/make/model/color to the ticket number, walk the vehicle noting or photographing existing damage, and confirm mileage or fuel level if the lot's policy tracks it — this record is what everything downstream leans on.
2. **Attach the key tag to the ticket stub number, not to a description or a memory** — hang it in the numbered slot that corresponds, and never let a second key go on an unnumbered or reused hook while the first is still in play.
3. **Assess the vehicle before moving it**: transmission type, anything unfamiliar about the controls, any driver-assist quirks (auto-hold, unusual parking brake). If it's a manual or the attendant hasn't driven that model before, move it deliberately and confirm clutch bite before committing to any incline or tight space.
4. **Place it according to the lot's density plan for its expected dwell time** — short-dwell vehicles (restaurant guests, an hour or two) go where they can be pulled without unstacking others; long-dwell vehicles (overnight, event-length) can absorb the tightest, most-stacked spots since there's time to plan the unstack.
5. **On retrieval, re-verify the ticket-to-tag-to-vehicle match before pulling any car**, especially during a rush or after a shift change — a fast wrong-car handoff costs far more than the ten seconds the check takes.
6. **If a claimed pre-existing condition doesn't match the intake record, or the intake record is missing, escalate to a supervisor immediately rather than negotiating on the spot** — this is a documentation and liability question, not a courtesy question, and the wrong answer given informally becomes the operator's admitted position.
7. **After any incident (scrape, delay past a stated threshold, lost ticket), file the incident report the same shift**, while the guest, the vehicle, and the witnesses are still present — a report written the next day is worth a fraction of one written in the first ten minutes.

## Tools & methods

- **Numbered claim-ticket and key-tag system** — matching numbers on the guest stub, the key tag, and (where used) a chalk or chit mark on the windshield; the physical backbone of the chain of custody.
- **Intake damage log / walkaround photo set** — a consistent sequence (front-left corner around the car, close-ups of any existing marks, plate visible, odometer if policy requires) taken the same way every time so gaps are obvious.
- **Valet key box / pegboard with numbered slots**, sometimes an electronic key-tracking system on larger operations, so a key's location is never dependent on one attendant's memory.
- **Stand log / run sheet** tracking time in, time out, and which runner has which vehicle — the operational record a supervisor uses to diagnose a slow rush in real time rather than after the complaint.
- **Incident report form** — guest and employee statements, vehicle identifiers (VIN, plate, make/model/year/color), photos, timestamps, and contact information, filed the same shift.

## Communication style

Terse and procedural with guests — states the ticket number, points out anything noted at intake, gives an honest retrieval-time estimate during a rush rather than a reflexive "just a few minutes." Escalates to a supervisor immediately and factually on any damage dispute or lost ticket, without admitting fault or negotiating a settlement in the moment — that's a decision above the attendant's authority. With the rest of the stand, communication is almost entirely the ticket/tag system itself plus short verbal handoffs at shift change ("47 and 52 are stacked behind the pillar, 60 is a manual, be careful on the ramp").

## Common failure modes

- **Skipping the intake walkaround when the lot is busy** — the exact condition (volume, time pressure) that makes documentation matter most is when it gets skipped, so a busy stand needs the process to be faster, not optional.
- **Trusting memory over the tag system once the attendant feels experienced** — new attendants follow the ticket/tag protocol religiously; experienced ones start skipping the physical hang-and-match step because "I know where it is," which is exactly the overconfidence that produces a wrong-car handoff.
- **Treating a manual-transmission or unfamiliar vehicle like any other car** — an attendant who wants to look competent moves it at normal speed instead of the deliberate creep-and-confirm the situation calls for.
- **Overcorrection: refusing to stack or block in any vehicle "to be safe,"** which quietly gives back the density gain that is the entire point of running valet instead of self-park — the fix for stacking risk is a disciplined unstack process, not avoiding density altogether.
- **Answering a damage claim on the spot** with an apology or an offer, which functionally admits liability before anyone has compared the claim to the intake record.
- **Adding hours instead of a second retrieval team** when a rush is understaffed — a queue backing up past the sustainable retrieval rate is a headcount problem at that moment, not a motivation problem.

## Worked example

**Situation.** A hotel valet stand runs one team on a Friday night: 40 minutes of arrivals-and-departures work available per attendant per hour (after breaks, walking distance, and radio time), with 3 attendants on shift = 120 attendant-minutes/hour of retrieval-and-park capacity. A banquet lets out at 10:00 PM, and the stand's ticket log shows 84 vehicles parked in that section, average distance requiring 3.5 minutes of attendant time per car (walk to car, verify tag, drive to guest, hand off).

**Naive read.** "3 attendants, 84 cars, that's 28 cars each — should be done in under two hours, we're fine as staffed."

**Expert reasoning.** The relevant number isn't cars per attendant, it's attendant-minutes required versus attendant-minutes available in the window guests are actually waiting, which is the first 30-40 minutes after the banquet ends, not the full two hours. 84 cars × 3.5 minutes = 294 attendant-minutes of work. Against 120 attendant-minutes/hour of capacity, that's roughly 2.5 hours to clear the section at 3 attendants — guests queuing in the first half hour will wait far longer than that average implies, because demand is front-loaded and capacity is flat. Applying the roughly one-attendant-per-15-vehicles peak rule of thumb: 84 vehicles in a peak window calls for 84 ÷ 15 ≈ 5.6, round up to 6 attendants, not 3. Three additional attendants (6 total) add another 120 attendant-minutes/hour, bringing capacity to 240 attendant-minutes/hour and cutting the clearance window from ~2.5 hours to about 1 hour 15 minutes — inside the range where guest complaints and comped-parking concessions stay rare. The fix is staffing the known peak, not extending the shift length of an undersized team.

**Deliverable (shift-lead note to the GM, as written):**

> Friday banquet valet: 84 vehicles in Section C, 3.5 min/car average retrieval. At 3 attendants (120 attendant-min/hr) that's a ~2.5-hour clear — unacceptable for a 10:00 PM letout. Pulling 3 attendants from the self-park lot for the 9:45-11:00 PM window brings us to 6, cutting clear time to ~1 hour 15 minutes, in line with our 1-per-15 peak staffing rule. Recommend approving 3.75 attendant-hours of overtime (3 attendants × 1.25 hrs) — the alternative is a documented queue past 45 minutes, which is our comped-parking trigger.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when planning lot density/stacking, staffing a predicted rush, or filling out an intake or incident report.
- [`references/red-flags.md`](references/red-flags.md) — load when something about a shift, a claim, or a stand's numbers looks off and you need the first diagnostic question.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term (bailment, chain of custody, dwell time) needs its precise meaning and the way it gets misused.

## Sources

- Oklahoma Bar Association, *Civil Liability of Parking Valets* (Persaud, Oklahoma Bar Journal, Nov. 2018) — bailment framework, gratuitous-bailee "slight care" vs. bailee-for-hire "ordinary care" distinction.
- National Parking Association member insurance minimums ($1M legal liability / $5M general liability) as a stated industry baseline for valet operators.
- International Parking & Mobility Institute (IPI) — industry standards body for parking/valet operations cited as the professional-association reference point for staffing and safety practice.
- Industry operational sources on valet density and staffing: MB&L Parking Solutions and Open Door Valet operator blogs, cited for the 40-60% density-gain figure over self-park, the ~1-attendant-per-15-vehicles peak staffing rule, and key-tag/claim-ticket chain-of-custody practice — vendor-published, treated as industry-consensus heuristics rather than regulatory standards.
- Manual-transmission prevalence figure (under 18% of American drivers) — commonly cited industry/consumer-research statistic used here to size the unfamiliar-vehicle risk; treat as a stated heuristic, not a controlled study result.
- No direct parking-attendant/valet-manager practitioner has reviewed this file yet — flag corrections or gaps via PR.
