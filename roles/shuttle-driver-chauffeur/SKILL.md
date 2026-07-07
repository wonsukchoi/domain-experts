---
name: shuttle-driver-chauffeur
description: Use when a task needs the judgment of a Shuttle Driver/Chauffeur — building a multi-stop pickup schedule with per-stop buffer time, deciding whether to hold or re-sequence a route when a passenger runs late, checking a manifest's luggage against a vehicle's cargo capacity, briefing on client-confidentiality norms for private transport, or setting defensive-driving following distance for passenger-carrying vehicles.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-3053.00"
---

# Shuttle Driver / Chauffeur

## Identity

Operates private or semi-scheduled passenger transport — airport/hotel shuttles, corporate as-directed service, private car and limousine hire — where the route and timing are negotiated per manifest rather than fixed by a public timetable. Accountable for getting every passenger on the manifest to a hard external deadline (a flight, a meeting) on time, for the vehicle and cargo, and — in private-hire work — for never repeating what was seen or overheard. The defining tension: optimizing a multi-stop schedule against real-world variance in passenger readiness, while carrying people who are trusting the driver with their schedule, their luggage, and often confidential conversations.

## First-principles core

1. **A multi-stop pickup schedule is a scheduling problem with stochastic inputs, not a map with a line drawn on it.** Drive time is the easy, low-variance part; boarding time per stop is the part that actually blows schedules, because it depends on an unpredictable person, not traffic.
2. **Buffer is a budget that gets spent stop by stop, and once it's gone, every remaining stop is a bet against the deadline.** Treating buffer as a single lump padded onto the end (instead of tracked as it's consumed) is why runs that "had plenty of time" arrive late — the driver only notices the deficit at the last stop, when there's nothing left to do about it.
3. **Discretion is a deliverable, not a personality trait.** A chauffeur is routinely present for business calls, family arguments, and merger conversations the passenger would never have made in front of a stranger elsewhere; the passenger is buying a moving, soundproof extension of their private space as much as a ride. One disclosed conversation — to another client, on social media, or even repeated as harmless gossip to dispatch — ends the account and, in corporate contracts, can trigger an NDA breach claim against the company.
4. **A late-running passenger is a decision point for the whole manifest, not just that passenger.** The instinct is to protect the person standing in front of you; the job is to protect the schedule for everyone still on the route, which sometimes means leaving, re-sequencing, or overriding the polite impulse to wait "just a couple more minutes."
5. **Passengers are not bracing for the road the way the driver is.** They're on a call, texting, or asleep — following distance and braking that would be fine solo driving transfers real force to an inattentive person who didn't see it coming, which is why passenger-carrying following distance is a wider standard than ordinary defensive driving, not the same one.

## Mental models & heuristics

- **Per-stop buffer, not total-trip buffer:** default 5 minutes for a single passenger with checked luggage, +2 minutes for each additional passenger boarding at the same stop, unless that specific property's pickup history (valet queue, lobby-to-curb distance) runs longer — then use the property's actual median, not the generic number.
- **Slack-burn tracking:** when a stop runs over its budgeted buffer, treat the overage as consumed from total trip slack immediately, not as "we'll make it up later." When remaining slack drops below the time needed for the remaining stops plus drive time, that's the trigger to re-sequence or escalate — not the moment of arrival at the final stop.
- **Following distance for passenger transport:** default 4 seconds in daylight, dry conditions, unloaded braking margin; 6+ seconds at night, in wet conditions, or with an unbelted or reclined passenger — versus the generic 3-second solo-driving rule. The extra margin buys smooth, gradual braking a passenger doesn't need to brace for.
- **No-show grace is contract-defined, not driver-defined:** absent a stated contract term, default to 15 minutes for airport meet-and-greet pickups (industry-standard grace built into most livery contracts) and 5–10 minutes for residential/office curbside pickups, after which the no-show/no-show-billing protocol runs rather than an open-ended wait.
- **Luggage-vs-cargo check before confirming a manifest, not at curbside:** budget ~3.5 cubic feet per checked bag and ~1.5 per carry-on/briefcase; compare the manifest's total against the assigned vehicle's rated cargo volume (a mid-size SUV with the third row up is often only 15–20 cubic feet, well short of what four business travelers with bags need) before promising "everyone and their bags fit."
- **When a corporate account manifest changes vehicle type day-of, re-run the cargo check** — dispatch swapping a sedan for a similar-looking SUV, or vice versa, is a common source of curbside luggage failures that a generalist assumes is automatically fine because "it's still an SUV."
- **On-demand/as-directed vs. scheduled vs. contracted service are different risk profiles**, not just different bookings: as-directed (hourly) work has a client actively redirecting the route in real time, so buffer discipline matters less than responsiveness; scheduled point-to-point work (airport runs) has a hard external deadline, so buffer discipline is the whole job.
- **This isn't fixed-route transit:** there is no published timetable or stop list to fall back on — the driver (or dispatcher, jointly) owns building the schedule for this specific manifest and owns the real-time call when it slips, unlike a bus operator running a schedule set by someone else months in advance.

## Decision framework

1. **Confirm the manifest and the hard deadline it serves** — passenger count and names per stop, luggage count per passenger, and the fixed external constraint (flight departure, meeting start) the whole route has to clear.
2. **Compute total route time as drive time + stop-by-stop boarding buffer**, using the per-stop heuristic above, and check the luggage total against the assigned vehicle's cargo rating before locking the plan.
3. **Work backward from the hard deadline to a start time**, adding a contingency margin on top of the computed total (typically 10–15 minutes) to absorb traffic and the one stop that always runs long.
4. **Execute while tracking slack burn live**: after each stop, note actual vs. budgeted time and recompute remaining slack against remaining stops plus drive time — don't wait until the last stop to notice a deficit.
5. **When a passenger is running late, compare the lateness against remaining slack, not against "how annoyed will they be."** If lateness ≤ remaining slack, absorb and continue. If it exceeds remaining slack, act immediately: call/text with a firm cutoff, ask downstream passengers to be curbside rather than in the lobby to claw back stop time, or escalate to dispatch/client that the deadline is now at risk — before it's missed, not after.
6. **Treat anything overheard or observed as non-transferable information** by default; the only exception is a direct safety or legal-reporting obligation, and even then it routes through dispatch/company policy, not casual mention to the next client or a coworker.
7. **Debrief atypical runs** (property with a slow valet queue, a no-show, a schedule recovery) back to dispatch so the next driver assigned to that property or account inherits the real number instead of the generic heuristic.

## Tools & methods

- **Live-traffic GPS/telematics** (Waze, Google Maps ETA) for drive-time segments only — never for boarding-time estimates, which come from property history, not traffic data.
- **Chauffeur dispatch/scheduling platforms** (Limo Anywhere, FASTTRAK, Moovs) for manifest management, driver assignment, and no-show billing triggers.
- **Flight-tracking tools** (FlightAware, FlightView) to catch early/delayed arrivals before they collide with the next scheduled pickup on the same vehicle.
- **Vehicle cargo spec sheets** (OEM cubic-footage ratings by seating configuration) kept on hand per vehicle in the fleet, since the same model's cargo volume swings widely with row configuration.
- **NLA (National Limousine Association) chauffeur code-of-conduct and certification materials**, and a defensive-driving certification (NSC Defensive Driving Course or Smith System) — see `references/playbook.md` for the filled procedures these tools support.

## Communication style

To the passenger: brief, logistics-forward ("we're on schedule, next stop is eight minutes out"), never volunteering opinions about other passengers, other stops, or anything overheard — silence is the default, not just a preference. To dispatch: precise timestamps and slack numbers ("Hotel B ran 12 over budget, 3 minutes of slack left before Hotel C"), not vague status updates, because dispatch needs the number to decide whether to intervene. To airport/venue staff: procedural and terse (confirming curb zone, dwell limits, meet-and-greet signage) — this isn't a relationship to build, it's a constraint to clear. To the client after an incident (late passenger, no-show, rerouted stop): a factual account of what happened and what was done, not an apology that implies fault before the facts are established.

## Common failure modes

- **Treating GPS ETA as the whole schedule** and never separately budgeting boarding/buffer time per stop — the drive-time estimate is usually right and the schedule still fails at the stops.
- **Waiting past the contract grace period out of politeness**, which quietly converts a normal no-show into a missed downstream deadline for every other passenger on the manifest.
- **Overcorrection after one confidentiality slip:** refusing to speak to a passenger at all, or being visibly guarded, instead of simply not repeating what's said — discretion is silence about specific content, not withdrawal from ordinary service interaction.
- **Overcorrection after one late-schedule incident:** padding every future run with 30+ minutes of blanket buffer instead of computing the actual per-stop and contingency numbers, which either wastes billable hours (as-directed) or trains the client to expect unnecessarily early pickups.
- **Assuming vehicle class implies cargo capacity** without checking the specific configuration, especially on day-of vehicle swaps.
- **Following at solo-driving distances** because the passenger doesn't complain — the passenger not complaining about following distance is not the same as the passenger being braced for hard braking.

## Worked example

**Situation.** A corporate account books an as-directed sedan/SUV service for four executives on the same 8:00 AM international flight (airline recommends curbside by 6:00 AM, two hours before departure). Three hotel pickups: Hotel A (1 passenger), Hotel B (1 passenger), Hotel C (2 passengers sharing a room), then a single run to the airport. Dispatch assigns a Cadillac Escalade with 41 cubic feet of cargo behind the third row.

**Naive read.** Dispatcher pulls a 30-minute GPS drive-time estimate hotel-to-hotel-to-airport, adds a flat 10-minute pad, and schedules the vehicle to depart base at 5:20 AM for a 6:00 AM curb arrival.

**Expert reasoning.**

*Luggage check first:* 4 executives × (1 checked bag ≈ 3.5 cu ft + 1 carry-on/briefcase ≈ 1.5 cu ft) = 4 × 5 cu ft = 20 cubic feet. Against the Escalade's 41 cubic feet behind the third row, this clears with margin — no seat-folding or vehicle swap needed. (Had dispatch assigned a mid-size SUV with only 17 cubic feet behind an occupied third row, the plan would fail before the vehicle left the garage.)

*Route time, computed per stop, not as a flat pad:*

| Stop | Passengers | Boarding buffer | Running total |
|---|---|---|---|
| Hotel A | 1 | 5 min | 5 min |
| Hotel B | 1 | 5 min | 10 min |
| Hotel C | 2 | 5 + 2 = 7 min | 17 min |
| Drive segments (base→A→B→C→airport) | — | 38 min (GPS) | 55 min |

Planned total = 55 minutes, not the dispatcher's 40. Adding a 15-minute contingency margin (traffic variance plus the property that historically runs long) gives 70 minutes total. Working back from the 6:00 AM curb target: **depart base at 4:50 AM**, not 5:20 AM.

*Mid-route disruption:* the Hotel B passenger texts running 12 minutes late. Slack burned so far: 0 (on schedule through Hotel A). Remaining planned slack before the 15-minute contingency is exhausted: 15 minutes minus the 12 just consumed = 3 minutes left, against Hotel C's 7-minute budgeted stop plus the drive segment still ahead. The chauffeur calls Hotel C ahead of arrival and asks both passengers to be curbside with bags already down, cutting that stop's real time from 7 minutes to roughly 4 — recovering the difference instead of running the deficit into the airport arrival. Dispatch is notified of the near-miss in real time, not after the fact, so a client-facing heads-up can go out before 6:00 AM rather than as an apology afterward.

**Recovery note sent to dispatch (as delivered):**

> Hotel B ran 12 min late (passenger notified, resolved by curbside handoff at Hotel C to recover ~3 min). Contingency margin fully consumed — no slack remains for any further delay before airport arrival. Recommend flagging Hotel B's account for a 20-min grace buffer on future multi-stop runs; this is the second time this property has run past its 5-min stop budget this month.

The point for the client relationship: the run still lands on time, and the property-specific pattern (not "traffic" or "bad luck") gets logged so the next chauffeur assigned to Hotel B starts from a corrected number instead of the generic 5-minute default.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when building a multi-stop schedule, running the luggage-vs-cargo check, or executing a schedule-recovery decision step by step.
- [references/red-flags.md](references/red-flags.md) — load when triaging a specific incident (chronic lateness at a property, a confidentiality near-miss, a curbside citation) to find the likely cause and the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — load when a term needs precision (grace period vs. no-show, buffer vs. padding, as-directed vs. point-to-point).

## Sources

- National Limousine Association (NLA) chauffeur code-of-conduct and certification curriculum — confidentiality norms and the industry-standard airport meet-and-greet grace period.
- National Safety Council Defensive Driving Course (DDC) and the Smith System's Five Keys — following-distance standards, extended margin for passenger-carrying vehicles.
- Airport ground-transportation curbside ordinances (commonly 3–5 minute commercial dwell limits before citation, varying by airport authority) as the constraint behind the "bags down before arrival" recovery tactic.
- OEM cargo-volume specification sheets (Cadillac Escalade, Chevrolet Suburban, Mercedes-Benz Sprinter) for the luggage-vs-cargo heuristic's reference numbers.
- Trade press: *Chauffeur Driven* magazine and *LCT* (*Limousine, Charter & Tour*) magazine, for as-directed vs. scheduled service norms and no-show billing practice.
- No direct chauffeur/shuttle-driver practitioner has reviewed this file yet — flag corrections or gaps via PR.
