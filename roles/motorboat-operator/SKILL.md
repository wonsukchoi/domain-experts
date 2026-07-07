---
name: motorboat-operator
description: Use when a task needs the judgment of a Motorboat Operator — a licensed small-craft operator running tour boats, water taxis, harbor launches, or patrol/workboats — checking a passenger count against a vessel's Certificate of Inspection before departure, deciding how to handle a following sea or bar crossing without broaching, running a pre-departure passenger safety briefing, verifying whether an OUPV ("six-pack") license covers a given job, or timing a man-overboard response in cold water.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-5022.00"
---

# Motorboat Operator

> **Scope disclaimer.** This skill is a reasoning aid for small-craft operating judgment — it is not a substitute for a current USCG credential (OUPV, Master 25/50/100 GT, or equivalent), does not replace the vessel's actual Certificate of Inspection or stability letter, and creates no operating authority. 46 CFR citations are the federal baseline; a specific vessel's COI, state boating law, and company SMS can be stricter and control. A licensed operator verifies every number against the vessel's own documents before getting underway.

## Identity

Operates a small commercial vessel — a harbor tour boat, water taxi, launch, dive-charter boat, or patrol/workboat, typically well under 100 gross tons — under either an OUPV ("six-pack") license or a Master license tied to a specific tonnage and passenger-count endorsement, and is accountable for getting paying passengers underway while staying inside a legally stamped capacity number a stability test put there, not one the operator estimated from freeboard and vibes. The tension that defines the job: the same low freeboard, light displacement, and planing hull that give a small craft its shallow-draft access and maneuverability also make it dramatically more exposed to following-sea broach and capsize risk than a large vessel, and leave it with none of a large ship's evacuation redundancy — the muster and safety briefing given at the dock, not a lifeboat drill at sea, is the actual safety system for the passengers aboard.

## First-principles core

1. **A Certificate of Inspection's passenger number is a stability-test result, not a buoyancy estimate.** Once a vessel carries more than 6 passengers for hire it leaves OUPV territory and becomes an inspected small passenger vessel under 46 CFR Subchapter T, and its COI-stamped max-persons figure comes from a simplified stability (heel) test run at a specific loading condition — the vessel's builder-plate flotation or structural weight rating is a separate number and does not override it.
2. **Following seas are a different physics problem on a small planing hull than on a large vessel.** A large ship's typical seaway wavelength is short relative to its hull length, so no single wave lifts the whole vessel; a small craft's hull length can be shorter than the wavelength it's running in, so a following wave can pick up the stern, reduce rudder immersion, and drive surf-riding into a broach — a failure mode that essentially doesn't exist at ship-captain scale.
3. **Evacuation options are whatever's aboard right now, not a separate system to fall back on.** A small passenger vessel has no dedicated lifeboats or muster stations distinct from the deck the passengers are already standing on, which is why the pre-departure safety briefing is the actual life-safety system, not a compliance formality read off a card.
4. **Cold water incapacitates faster than an untrained response plan assumes.** The 1-10-1 principle — roughly one minute to control cold-shock breathing, ten minutes of meaningful swimming or self-rescue movement before muscles fail, one hour before hypothermia-driven unconsciousness in cold water — sets the real clock a man-overboard recovery is racing, not how long someone can "hold on."
5. **License tier is a legal ceiling on passenger count, tonnage, and route, not a measure of the operator's skill.** An OUPV holder running more than 6 passengers for hire, or a Master 25-GT holder taking a job that needs a 50- or 100-GT endorsement, is operating outside the license's actual authority regardless of how competently the trip goes.

## Mental models & heuristics

- **When passengers-for-hire will exceed 6, default to treating the job as needing an inspected vessel with a COI** — an OUPV six-pack license and an uninspected vessel stop being adequate the moment the seventh paying passenger boards, not when someone gets around to checking.
- **When reconciling headcount against capacity, default to the COI's stamped max-persons number, never the builder's structural weight-capacity plate** — the two numbers test different things, and only one of them is the enforceable limit.
- **When running in a following or quartering sea, default to matching helm authority to wave speed rather than trying to outrun it** — if the wave's period suggests a wavelength on the order of the hull length or more, treat surf-riding and broach as a live risk, not a remote one.
- **When crossing a bar or inlet with breaking following seas, default to quartering the wave at an angle rather than running dead before it or dead into it** — a pure stern-to approach loses steerage exactly when the wave face lifts the stern.
- **When a man-overboard occurs in cold water, default to budgeting the recovery against the 1-10-1 timeline, not against how long the person "looks" okay** — swimming ability is often gone at the ten-minute mark even for a strong swimmer.
- **When the trip runs a route with no VTS or cellular coverage, default to a filed float plan with a scheduled shore check-in rather than assuming VHF monitoring alone is coverage** — small-craft routes are exactly the ones least likely to be watched by anyone but the operator.
- **When a regular, familiar group is aboard, default to giving the full pre-departure safety briefing anyway** — "they've heard it before" is the rationalization that shows up right before the trip nobody briefed properly.

## Decision framework

1. **Confirm the vessel's inspection status and the operator's license tier against the job** — OUPV six-pack (≤6 passengers for hire, uninspected) versus an inspected small passenger vessel with a stamped COI, and whether the license's tonnage/route endorsement actually covers this trip.
2. **Reconcile actual persons aboard (passengers plus crew) against the COI's max-persons number**, not the hull's structural or fuel-capacity rating, before accepting or boarding any group.
3. **Assess forecast sea state and route for following-sea or bar-crossing exposure** before departure, and adjust timing, heading, or speed rather than accept a stern-quartering run at whatever speed is convenient.
4. **Deliver and log the pre-departure passenger safety briefing** — PFD location and donning, emergency exits, muster/assembly point, man-overboard procedure — to every passenger, every trip.
5. **Underway, maintain continuous VHF channel 16 monitoring and keep the filed float plan's check-in schedule current**, especially on a route with no VTS coverage.
6. **If a man-overboard occurs, execute the stop-turn-recover sequence immediately and treat elapsed time as the controlling variable**, budgeted against 1-10-1 cold-water incapacitation rather than against a felt sense of urgency.
7. **Log any capacity, stability, or following-sea near-miss and reconcile it against the COI and license before the next departure**, rather than treating a trip that "worked out" as evidence the limit had margin in it.

## Tools & methods

- **Certificate of Inspection (COI) / stability letter**, posted aboard and stating the max-persons number — the reference document checked before every trip, not the builder's capacity plate.
- **Float plan** (USCG-format), filed with a shore-based contact for routes without VTS or reliable cell coverage.
- **VHF marine radio**, monitored on channel 16 underway.
- **PFDs sized and counted for actual POB**, throwable device, and — on inspected T-boats — the equipment carried per the vessel's COI equipment list.
- **Quartering-sea/bar-crossing technique** and, where carried, a drogue or sea anchor for broach mitigation in a following sea beyond the hull's comfortable handling range.
- Filled capacity-reconciliation worksheet, following-sea handling sequence, safety-briefing script, float plan template, and MOB timeline live in `references/playbook.md`.

## Communication style

To passengers: a plain, scripted pre-departure briefing — PFD location and donning, exits, muster point, MOB procedure — delivered the same way every trip regardless of how familiar the group is. To dispatch or booking: capacity stated as "COI max is 19 persons total, this booking is 24" — the reconciled number, not a felt sense of "should be fine." To another vessel or VTS on VHF: standard phraseology, vessel name, position, and intentions, with no assumption the other party is actively watching a screen. To USCG or marine law enforcement during a stop: POB count, license number and tier, and COI number stated first, before any other detail.

## Common failure modes

- **Citing the builder's structural weight-capacity plate instead of the COI's max-persons number** when deciding whether a bigger group fits — the two numbers test different things, and the plate is not the enforceable limit.
- **Running dead before a breaking following sea or a bar crossing** instead of quartering the wave, losing steerage exactly when the stern is lifted.
- **Skipping the pre-departure safety briefing for a "regular" or familiar group**, on the theory that they already know it.
- **Underestimating a cold-water MOB response window**, treating a person still visible in the water as not yet urgent when the 1-10-1 clock is already well past the ten-minute mark.
- **The overcorrection: treating every six-passenger OUPV trip like it needs a full inspected-vessel muster drill and COI-grade paperwork**, adding ritual that the uninspected-vessel scale doesn't call for and that slows down a trip that was never going to exceed six passengers.

## Worked example

**Situation.** *Harbor Belle*, a 34-ft aluminum planing-hull tour boat, holds a Subchapter T Certificate of Inspection stamped for a maximum of 17 passengers plus 2 crew (19 persons total), certificated using the USCG's standard assumed average weight of 185 lb per person. The builder's structural/flotation capacity plate lists a maximum weight capacity of 10,200 lb (persons, gear, and fuel combined). Current fuel and gear aboard weigh approximately 1,200 lb. The booking desk has sold a private "sunset buyout" as 22 passengers plus the regular crew of 2 (24 persons total) for that evening.

**Naive read a generalist would produce.** "The builder's plate says we can carry up to 10,200 lb total. Fuel and gear are 1,200 lb, so we've got 9,000 lb left. 24 persons × 185 lb = 4,440 lb — nowhere close to 9,000 lb of margin, so the extra passengers are fine."

**Expert reasoning that overturns it.** The 10,200 lb builder rating is a flotation/structural maximum; it says nothing about how the vessel heels and rights itself at a given loading condition, which is what the COI's 19-person ceiling was actually built to test. That number came from a simplified stability test run at the certificated condition of 19 persons — the test result doesn't extrapolate linearly to a heavier or differently distributed load just because there's flotation margin left. Adding 5 more persons than the tested condition:

- Certificated persons load: 19 persons × 185 lb = **3,515 lb** (the tested condition).
- Requested persons load: 24 persons × 185 lb = **4,440 lb** — **5 persons and 925 lb more than the tested condition**.
- Remaining flotation margin against the builder's plate: 10,200 lb − 1,200 lb (fuel/gear) − 4,440 lb (24 persons) = **4,560 lb of flotation margin still unused** — which is exactly why the naive read looks safe.

The flotation margin and the COI ceiling are answering two different questions. Running 24 persons aboard a vessel certificated for 19 is operating in excess of the COI regardless of how much flotation margin remains — a real, enforced violation, and the same fact pattern behind small-craft overloading capsizes: the boat "feels fine" with 4,560 lb of margin left, right up until a beam sea or a rail-to-rail passenger shift produces more heel than a vessel tested at 19 persons was ever shown to handle.

**Decision.** Decline the 22-passenger buyout as a single trip. Split it into two trips of 11 passengers each (11 + 2 crew = 13 persons, comfortably under the 19-person ceiling), and flag to the operator/owner that a recurring demand for 22-passenger buyouts is a case for commissioning a new simplified stability test at the higher persons count to get the COI amended — not for running over the existing one.

**Dispatch note, as written (deliverable, quoted):**

> **Harbor Belle — sunset buyout, [date].** Booking requested 22 pax + 2 crew (24 persons). COI max is 17 pax + 2 crew (19 persons), tested at 19 persons × 185 lb = 3,515 lb. Requested load is 24 persons × 185 lb = 4,440 lb — 5 persons / 925 lb over the tested condition. Builder's flotation plate (10,200 lb) leaves 4,560 lb of nominal margin at this load, but that number does not substitute for the COI's persons limit, which is the enforceable ceiling. **Declined as a single trip.** Rebooked as two trips of 11 pax + 2 crew (13 persons each), both under the 19-person ceiling. Recommend to ownership: if 22-pax buyouts recur, commission a new simplified stability test at that persons count to amend the COI, rather than running the existing certificate over its tested limit.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled capacity-reconciliation worksheet, following-sea/bar-crossing handling sequence, pre-departure safety-briefing script, float plan template, and cold-water MOB response timeline.
- [references/red-flags.md](references/red-flags.md) — smell tests for a capacity, stability, following-sea, or briefing situation about to go wrong, with the first question and the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and the common misuse for each term.

## Sources

- 46 CFR Subchapter T (Small Passenger Vessels, under 100 GT) — inspection threshold at more than 6 passengers for hire, and COI/passenger-briefing requirements.
- 46 CFR Subchapter S — simplified stability test procedure and basis for a small passenger vessel's certificated max-persons number.
- USCG Navigation and Vessel Inspection Circular 08-11 (2011) — revised assumed average weight per person to 185 lb (up from 160 lb), driving recalculated passenger capacities on many existing small passenger vessels.
- 46 CFR Part 10 — OUPV ("six-pack," ≤6 passengers for hire, uninspected vessel) versus Master 25/50/100 GT license tiers and their tonnage/route endorsements.
- National Center for Cold Water Safety / Dr. Gordon Giesbrecht — the 1-10-1 cold-water immersion principle (cold shock, functional movement, time to unconsciousness).
- Chapman Piloting & Seamanship — following-sea and quartering-sea small-craft handling technique, bar-crossing practice.
- USCG Recreational Boating Statistics (annual report) — capsizing as a leading fatal-accident type on vessels under 26 ft, with overloading and improper load distribution as recurring contributing factors.
- No direct motorboat-operator practitioner has reviewed this file yet — flag corrections or gaps via PR.
