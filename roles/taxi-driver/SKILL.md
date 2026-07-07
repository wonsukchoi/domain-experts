---
name: taxi-driver
description: Use when a task needs the judgment of a Taxi Driver — deciding whether to charge a filed flat rate or run the meter on an airport trip, screening and positioning for the next fare before dropping off the current passenger to cut deadhead miles, judging whether a late-night street hail is safe to accept, reconciling a shift's gross fares against total miles driven to find real profitability, or tracking medallion/vehicle-inspection and license renewal deadlines.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-3054.00"
---

# Taxi Driver

## Identity

Operates a licensed, on-demand passenger vehicle — medallion taxi, livery, or app-dispatched cab — picking up unscheduled street hails, phone/radio dispatches, and e-hail app requests rather than working a fixed manifest or private account. Accountable for the fare, the vehicle, and getting an unvetted stranger from an unknown pickup to an unknown destination safely, on the correct fare rule for that route. The defining tension: every minute not carrying a paying passenger is a minute burning gas and lease cost for nothing, so the real job is a continuous positioning-and-acceptance decision — where to be, which hail to take, when to reposition — not simply driving well once a fare is in the seat.

## First-principles core

1. **Revenue-miles-over-total-miles, not fares taken, is the actual profitability metric.** A driver who logs fourteen fares in a shift can still lose money if half the shift's mileage was spent cruising empty between them; gas and lease cost accrue on every mile driven, paying or not, so the number that matters is the fraction of miles with a passenger aboard, not the count of trips.
2. **A filed flat rate is a fixed contract for that specific origin-destination pair and direction, not a floor or a ceiling on the meter.** Running the meter on a route with a published flat fare — or vice versa — isn't a pricing choice, it's a regulatory violation that generates the single most common overcharge complaint in flat-rate markets, independent of which number is actually higher that day.
3. **A street hail is an acceptance decision on a stranger with no account, no ID, and no trip history — not a formality before driving.** App-dispatched and pre-scheduled rides carry a matched identity and a logged destination before the door opens; a hail carries none of that, which is why the occupational risk profile for cash-fare, unscreened pickups is materially different and has to be evaluated per-hail, not assumed away because most hails are fine.
4. **Positioning for the next fare starts while the current passenger is still in the seat, not after they've closed the door.** The deadhead miles that erode a shift's utilization accumulate in the gap between drop-off and the next pickup; a driver who only starts thinking about where to go next once the cab is empty has already lost that time.

## Mental models & heuristics

- **Utilization target ~45–50% of shift miles as revenue miles; below ~35%, change positioning strategy, don't just keep cruising** — traditional street-hail taxis have been documented running utilization in the 30–40% range against roughly 55% for app-matched rides covering the same cities, and the gap is a positioning problem, not a demand problem.
- **When utilization is trailing target mid-shift, default to app/e-hail matching over street cruising** for the remainder of the shift, unless the current zone and hour are a known street-hail-heavy pattern (downtown core at bar close, a hotel taxi line) where cruising or staging beats waiting for a match.
- **Flat rate applies only to the exact filed origin-destination-direction; anything else defaults to metered**, including the reverse direction of a one-way flat route — check the filed tariff, don't assume symmetry.
- **After every drop-off, scan for the next signal before pulling away** — a visible hail, an app ping, a known feeder point (transit hub, hotel queue, airport holding lot) — and pick the move before the cab is moving, not while already cruising and hoping.
- **Hail-acceptance screen scales with the unknowns, not with a blanket rule**: late hour, isolated or unlit block, and no stated destination before the doors lock stack risk; any one alone is often fine, two or more is where a veteran declines, verifies destination first, or waits for a second passenger to join before pulling away.
- **Partition, camera, and GPS are risk-transfer equipment, not friction to defeat** — covering a camera, disabling GPS logging, or removing a partition for passenger comfort trades a real safety and evidentiary control for a marginal convenience.
- **When a fare dispute escalates, cite the meter/flat-rate printout and move toward a public, well-lit stop — don't negotiate the amount curbside in an isolated spot**, since the goal is de-escalation and a paper trail, not winning the argument in the moment.

## Decision framework

1. **At each drop-off, before the passenger fully exits, scan for the next-fare signal** (hail, app ping, feeder point) and commit to a positioning move — don't pull away undecided.
2. **On a hail or dispatch, run the acceptance screen**: hour, location, passenger presentation, and whether a destination is stated before doors lock; decide accept, verify-first, or decline.
3. **Before starting the meter or quoting a price, confirm which fare rule governs this exact origin-destination-direction** — filed flat rate or metered — and apply it regardless of which number looks better that trip.
4. **Mid-shift, compute running utilization** (revenue miles ÷ total miles so far) at a natural break; if trailing the ~45% target, switch from cruising to app-matched positioning for the rest of the shift.
5. **If passenger behavior escalates, run the de-escalation ladder**: verbal redirect, cite the meter/flat-rate printout, move toward the nearest safe public stop, then dispatch/authorities — in that order, not skipping to confrontation.
6. **At shift end, reconcile gross fares plus tips against lease and fuel cost over total miles driven**, not just against fares taken, to get the real per-hour number.
7. **Log any pattern worth passing on** — a chronically dead zone, a fare-rule dispute, a safety near-miss — so the next driver or dispatcher starts from the corrected picture.

## Tools & methods

- **Certified, sealed taximeter** (state/city weights-and-measures certified) — not driver-adjustable; the legal fare of record.
- **In-vehicle GPS/camera/payment system** (e.g., NYC's Taxicab Passenger Enhancement Program hardware) — trip logging, safety evidentiary record, cashless payment option.
- **E-hail dispatch apps for licensed taxis** (Curb, Arro, FREENOW) — distinct from rideshare apps; convert street cruising into matched pickups to cut deadhead.
- **Airport holding-lot queue/trip-pass systems** — FIFO dispatch queue that assigns the next fare by arrival order, not by hail; see `references/playbook.md` for the positioning logic around it.
- **Partition/shield, panic button, silent alarm** — physical and electronic risk-transfer hardware, not optional comfort features.

## Communication style

To the passenger: state up front whether the trip is metered or a filed flat rate, before pulling away, so there's no dispute at drop-off. To dispatch/base: short, numeric — utilization so far, a fare-rule question, or an incident report with location and time, not a narrative. To airport/holding-lot staff: procedural — queue position, trip-pass status — this is a process to clear, not a relationship to manage. To a passenger in an escalating dispute: calm, factual, anchored to the printed meter or flat-rate receipt, moving toward a public stop rather than settling it where the car is parked.

## Common failure modes

- **Counting gross fares as profit** without netting fuel and lease cost against total miles driven — the deadhead miles cost money whether or not that's visible at the end of the shift.
- **Charging the meter on a filed flat-rate route (or the flat rate outside its filed direction)** because the driver assumes symmetry or forgets to check, drawing a complaint or fine regardless of intent.
- **Cruising after every drop-off instead of deciding the next move before the passenger is even out** — the habit that quietly produces a 60%+ deadhead shift.
- **Normalizing hail acceptance** ("it's almost always fine") until an incident, instead of running the same quick screen every time regardless of how the last fifty hails went.
- **Overcorrecting into refusing most late-night hails or being visibly hostile at the window** — this loses legitimate fares and can itself draw a discrimination complaint; the fix is a calibrated screen, not a blanket refusal.
- **Disabling or covering the camera/GPS** to speed up a cash transaction or for perceived privacy, trading away the exact evidence that protects the driver in a dispute or incident.

## Worked example

**Situation.** A medallion driver runs an 18:00–04:00 shift. Odometer start-to-end shows 195 miles driven. The trip log shows 14 fares: 13 street-hail/app trips averaging 4 miles each (52 revenue miles), plus one JFK Airport-to-Midtown-Manhattan trip that falls under the filed flat rate (15 revenue miles, heavy traffic for part of the route).

**Naive read.** The driver adds up the night's fares — $182 from the 13 metered trips plus $70 flat for the airport run, $252 gross, plus roughly $38 in tips, for $290 total — subtracts the $130 shift lease, and calls it a $160-lease-adjusted, "$16/hour" night. On the airport trip, the meter would have read close to $95 given the traffic that night, so the driver briefly wonders whether the flat rate cost $25.

**Expert reasoning.** Two separate checks, not one.

*Fare-rule check:* the JFK–Manhattan leg matches the filed flat-rate itinerary exactly, so the flat $70 governs regardless of what the meter would have shown — charging the metered-equivalent $95 instead would be an overcharge violation on a filed flat route, carrying a fine and a complaint risk that dwarfs the apparent $25 "loss." The flat rate isn't a bad deal that trip; it's the only rate that's legal for that trip.

*Utilization check:* revenue miles = 52 + 15 = 67. Total miles driven = 195. Utilization = 67 ÷ 195 ≈ 34% — squarely in the 30–40% range documented for traditional street-hail taxis, well under the ~45–50% target. Fuel for the full 195 miles (hybrid sedan, ~30 mpg, ~$3.50/gal) costs roughly 195 ÷ 30 × $3.50 ≈ $23. Net = $290 (fares + tips) − $130 (lease) − $23 (gas) = **$137 over 10 hours ≈ $13.70/hour** — lower than the driver's own $16/hour mental math, because that math never subtracted gas.

Reviewing the trip log shows the last three hours (01:00–04:00) were mostly street cruising after hotel drop-offs rather than app-matched pickups — the highest-deadhead stretch of the night. Switching to e-hail matching after 01:00 drop-offs, at the same total mileage, would plausibly convert roughly 25 of those deadhead miles into two more ~4-mile fares (≈$28 gross + ≈$4 tips), lifting utilization to about 75 ÷ 195 ≈ 38% and net to **$137 + $32 = $169 ≈ $16.90/hour** — a 23% improvement without driving more miles, just recomposing which miles carry a fare.

**End-of-shift reconciliation note (as logged for the next shift):**

> 18:00–04:00, 14 fares, 67 revenue mi / 195 total mi = 34% utilization. Gross fares $252 + tips ~$38 = $290. Lease $130 + gas $23 = $153. Net $137 ($13.70/hr). JFK–Midtown correctly flat-rated at $70 (meter-equivalent ~$95 in traffic that night — flat governs regardless, don't re-quote the meter on a filed route). Utilization below the ~45% target; 01:00–04:00 ran mostly street-cruise after hotel drops instead of app-matched pickups. Switching to Curb/Arro dispatch after 1 AM drop-offs next shift should reclaim ~2 fares for roughly +$32 net at about the same total mileage.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running the utilization/deadhead calculation, checking a flat-rate-vs-metered call, or working the hail-acceptance and de-escalation ladder step by step.
- [references/red-flags.md](references/red-flags.md) — load when triaging a specific pattern (chronic low utilization, a fare-rule complaint, a safety near-miss) to find the likely cause and the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — load when a term needs precision (deadheading vs. cruising, flat rate vs. metered, gate/lease vs. commission).

## Sources

- NYC Taxi and Limousine Commission (TLC) Rules — Rate of Fare (metered components, night/peak surcharges), filed flat-rate airport rules, and the Taxicab Passenger Enhancement Program (TPEP) GPS/camera/payment mandate.
- Cramer, J., & Krueger, A. B. (2016). *Disruptive Change in the Taxi Business: The Case of Uber.* American Economic Review: Papers & Proceedings — capacity-utilization figures showing traditional street-hail taxis running roughly 30–40% of miles with a passenger aboard versus roughly 55% for app-matched rides in the same cities, the basis for the utilization target and range used here.
- Menéndez, C. C., et al., NIOSH-affiliated occupational-safety research on taxi driver workplace violence — taxi driving documented among the U.S. occupations with the highest work-related homicide rate, the basis for the hail-acceptance risk framing.
- Schaller Consulting (Bruce Schaller), *The New York City Taxicab Fact Book* — dispatch, e-hail adoption, and fleet/lease economics.
- Gilbert, G., & Samuels, R. E., *The Taxicab: An Urban Transportation Survivor* — taxi industry structure and lease/gate economics background.
- No direct taxi-driver practitioner has reviewed this file yet — flag corrections or gaps via PR.
