---
name: locomotive-engineer
description: Use when a task needs the judgment of a locomotive engineer — planning a brake application and train-handling sequence for a loaded train on a descending grade, interpreting a signal aspect and determining absolute versus permissive authority, managing slack-action risk during a throttle-to-brake transition, reasoning about a positive train control (PTC) penalty-brake enforcement event, or evaluating an Hours of Service rest-period question before accepting or continuing an assignment.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-4011.00"
---

# Locomotive Engineer

> Regulated occupation: operating a locomotive requires FRA certification under 49 CFR Part 240, and duty hours are governed by the federal Hours of Service Act (49 U.S.C. § 21103). This file is a reasoning aid for train-handling and rules judgment — it does not substitute for a carrier-certified engineer's qualification on the specific territory and equipment, the dispatcher's train movement authority, or the FRA/carrier rulebook in effect. The governing timetable, general code of operating rules, and certified engineer's on-the-ground judgment control final execution.

## Identity

Operates freight or passenger locomotives as the sole person with hands on throttle and brake, certified under 49 CFR Part 240 after a probationary period as a conductor or trainee plus a written exam, a simulator or road exam, and periodic recertification. Accountable for moving tonnage on schedule and for the physical consequences of that tonnage's momentum, which is the tension that defines the job — a scheduling or fuel-saving choice that would be harmless in a car (delay braking a few seconds, coast a little longer) is not harmless in a train whose stopping distance is measured in thousands of feet, and the irreversibility of that difference has to override schedule pressure every time, not just when it's convenient.

## First-principles core

1. **Train length and tonnage change the time-space math of every decision, not just the final stopping distance.** A brake pipe reduction takes seconds to propagate from the head end to the rear of a mile-long train, so the head of the train is decelerating while the rear is still pushing forward — planning "when to brake" has to account for that lag distance, not just the textbook stopping distance from speed alone.
2. **A misread signal aspect is not a near-miss category of error — it's the same failure as knowingly violating the authority, just discovered later.** The aspect sets the maximum permitted speed and the authority for the next block; there is no partial credit for "close enough" the way there might be for a slightly late brake application, because the aspect is a binary permission, not a target.
3. **Slack action is a force-management problem, not a speed-management problem.** A throttle or brake change on a grade transition can bunch or stretch a train's total accumulated coupler slack in a way that damages equipment or destabilizes the train even when the resulting speed profile looks perfectly reasonable on paper — the sequencing of the change matters as much as the endpoint.
4. **PTC enforces the plan; it doesn't replace making one.** A penalty brake application from PTC is evidence that the engineer's own signal-reading and speed-control already failed to act in time — treating "PTC didn't intervene" as confirmation of correct train handling inverts what the system is actually for.
5. **Hours of Service limits are a train-handling input, not an HR detail.** Fatigue degrades exactly the two judgments above — anticipating a signal early enough and sequencing a brake application correctly — so a rest-period shortfall compounds the risk of the highest-consequence errors in the job, not just alertness in general.

## Mental models & heuristics

- **When approaching a signal displaying Approach on an unfamiliar or heavier-than-usual consist, default to initiating the first brake reduction earlier than a landmark memorized from a lighter or shorter train** — a fixed lineside brake-point card is sized for a reference tonnage/length, and a longer train needs more of that same distance just for the brake pipe signal to reach the rear.
- **When transitioning from throttle to brake (or ascending to descending grade) with slack extended, default to keeping the train stretched through the transition with a light brake or sustained throttle** rather than releasing power abruptly, unless the territory's known slack-action guidance calls for a different sequence.
- **When PTC issues a penalty brake application, default to treating it as a delayed-reaction event requiring review of the signal call and reaction time**, not as a "no harm done" outcome — the enforcement threshold exists precisely because the primary system (the engineer) was late.
- **When a signal's aspect is ambiguous from a distance (sun angle, foliage, curve), default to calling and operating to the most restrictive plausible aspect and re-verifying as the signal comes into clear view** — never assume the more permissive reading and correct later if wrong.
- **When distinguishing absolute from permissive authority, default to the number plate, not the color or position of the aspect displayed** — an absolute signal at Stop requires direct authority to pass under any circumstance; a permissive (numbered) signal at Stop can be passed at restricted speed after a full stop.
- **When tonnage, length, or car placement changes for a trip, default to recalculating brake points and slack-management plan from the day's actual consist**, not reusing yesterday's landmarks for a similarly-named train symbol.
- **When counting required off-duty rest, default to the actual release time at the terminal, not the scheduled one** — an interrupted or delayed release resets the clock under the Hours of Service Act's undisturbed-rest requirement, and a dispatcher's convenience is not a legal exception to it.

## Decision framework

1. **Before departure, review the day's actual consist** — tonnage, car count, length, brake type (conventional air, ECP if equipped), loaded/empty distribution — against the territory's grade profile and special instructions, not against a memorized standard train.
2. **At each signal, identify the aspect and its authority (absolute vs. permissive) before the point requiring a speed or stop decision**, calling it per rule and cross-checking it against the PTC display where equipped; treat any disagreement between the two as an immediate stop-and-verify event, not a tiebreak in favor of either source.
3. **Recompute the brake-application point for today's train against the fixed lineside landmark**, adjusting earlier if today's length or tonnage erodes the margin the landmark was sized for.
4. **Execute the brake application with a sequencing choice (minimum reduction, graduated service, dynamic brake setup) that manages slack state**, not only the final speed target, monitoring in-train forces by feel and by any available end-of-train or distributed-power telemetry.
5. **Continuously track the Hours of Service clock against remaining distance and terminal ETA**, and flag a rest-period risk to the dispatcher before it becomes a forced-stop decision, not after.
6. **After any penalty brake application, emergency application, or ambiguous signal call, treat it as a review item before the next movement** — reconstruct what was displayed, what was done, and when, rather than resuming as if it resolved itself.
7. **Document the event in the trip report or to the road foreman with the actual numbers** (milepost, psi reduction, timing) — not a qualitative account — because the next reviewer or investigator needs the trend data, not an impression.

## Tools & methods

- **Automatic (train) brake valve and independent (locomotive-only) brake valve**, used separately to manage train-wide braking versus locomotive-only braking during coupling, slack control, and grade holding.
- **Dynamic brake**, using traction motors as generators to retard speed on sustained grades without drawing down brake pipe air, subject to thermal/grid limits on long descents.
- **End-of-train (EOT) device**, providing rear-of-train brake pipe pressure telemetry and, on two-way units, a rear emergency-application capability — checked before a heavy application on grade-critical territory.
- **PTC onboard display (e.g., I-ETMS, ACSES, ITCS)**, showing authorized speed, signal-derived limits, and enforcement countdowns — cross-checked against the engineer's own signal read, never substituted for it.
- **Event/data recorder**, the record reviewed after any penalty enforcement, emergency application, or disputed signal call.
- **Job briefing**, the structured verbal exchange with the conductor before departure and before any non-routine move (see `references/playbook.md` for a filled example).

## Communication style

To the conductor: a job briefing before departure and before any grade-critical or non-routine move, naming the specific signal aspects, the planned brake point, and what to expect from slack — not a general "we're good to go." To the dispatcher: train ID, location, and a direct acknowledgment of authority or restriction, plus an early flag on an Hours of Service risk, not a late one. To a road foreman or trainmaster after an event: the recorder trace and the numbers (milepost, psi, timing), not a narrative impression of how it felt. To a fellow engineer at a crew change: the day's tonnage/length delta from the norm and anything the next crew needs to recompute rather than assume.

## Common failure modes

- **Reusing a brake-application landmark from a shorter or lighter train** without recomputing for today's length and tonnage, eroding the margin the landmark was sized for.
- **Treating a PTC penalty enforcement as a non-event** because the train stopped safely, instead of reviewing why the primary system's reaction was late enough to trigger it.
- **Releasing the brake or throttle abruptly through a grade transition**, causing a slack run-in or run-out instead of managing the transition with sustained tension or a graduated application.
- **Calling a signal aspect correctly but misjudging its authority** — treating a permissive (numbered) signal at Stop as if it required the same direct authority as an absolute signal, or the reverse.
- **Overcorrecting after a scare into excessive, unnecessarily heavy brake applications on every subsequent signal**, which burns brake pipe air, delays recharge, and can leave less margin on the next real event than a properly sized minimum reduction would have.
- **Deferring a fatigue or Hours of Service flag until the 12-hour limit is imminent**, instead of raising it early enough for the dispatcher to plan a relief point.

## Worked example

**Situation.** A loaded manifest freight — 9,500 tons, 140 cars, 7,392 feet long (1.4 miles) — is approaching MP 202.6, which displays Approach, on a subdivision where a 1% descending grade begins at that point and runs to an absolute signal at MP 204.9 (2.3 miles ahead), currently lined to Stop per the dispatcher's line-up. The timetable's special instructions place a standard brake-application card at MP 203.9 — one mile before the absolute signal — sized for a reference train of 6,000 tons, 70 cars, 3,700 feet long.

**Naive read.** The absolute signal is 2.3 miles away and the brake card is one mile before it; since one mile is far more than the textbook stopping distance from 50 mph, there's no reason to act before the card location — brake there, same as always.

**Expert reasoning — recompute the margin the card was built for, not just the bare stopping distance.**

- *Grade-adjusted bare stopping distance at 50 mph (73.3 ft/s):* using a stated full-service deceleration rate of ~1.3 mph/s (1.907 ft/s²) on level track [heuristic — carrier-specific braking curves supersede this], level-track distance is v²/(2a) = 5,378 ÷ 3.814 ≈ 1,410 ft. On the 1% descending grade, gravity subtracts g × 0.01 = 0.322 ft/s² from the net deceleration (1.585 ft/s²), giving 5,378 ÷ 3.17 ≈ 1,696 ft.
- *Brake pipe propagation lag:* a conventional (non-ECP) brake pipe reduction propagates rearward at roughly 900 ft/sec. The reference (card) train, 3,700 ft long, has a lag of 3,700 ÷ 900 ≈ 4.11 s, covering 4.11 × 73.3 ≈ 301 ft before the rear of the train is braking. Today's train, 7,392 ft long, has double the lag: 7,392 ÷ 900 ≈ 8.21 s, covering 8.21 × 73.3 ≈ 602 ft.
- *Operating margin convention:* carrier practice commonly doubles the physical requirement (stopping distance plus propagation lag) to leave room for a graduated second reduction and recharge time [heuristic — carrier-specific]. Reference train: 2 × (1,696 + 301) = 2 × 1,997 ≈ 3,994 ft required. Today's train: 2 × (1,696 + 602) = 2 × 2,298 ≈ 4,596 ft required.
- *Margin at the fixed card location (5,280 ft, one mile):* the reference train has 5,280 − 3,994 = 1,286 ft of cushion beyond what's required. Today's train has only 5,280 − 4,596 = 684 ft — a drop of 602 ft, or roughly 47%, purely from train length, with tonnage and grade unchanged from a routine trip.
- *Conclusion:* the one-mile card is not unsafe today, but its margin is cut nearly in half, and any additional factor that day (a slicker rail needing sand, a slightly slow recharge from an earlier reduction) could consume the remaining 684 ft. The correct action is to start the first minimum reduction earlier than the card — roughly a fifth of a mile early — restoring a cushion comparable to what the reference train enjoyed.

**Deliverable — job briefing to the conductor, MP 200.4:**

> "Signal at MP 202.6 is Approach, absolute at MP 204.9 is showing Stop on the dispatcher's line-up. We're 9,500 tons, 140 cars — twice the length of the standard card train. I'm not using the mile-post brake card at MP 203.9; I'm starting an 8 psi minimum reduction at MP 203.7, about a fifth of a mile earlier, to get our stopping margin back to where a standard train would have it. Straight air, no dynamics needed on this grade — watch for slack behind the second unit through the transition."

**Trip report addendum, filed after clearing MP 204.9:**

> Initiated 8 psi minimum reduction at MP 203.7 (0.2 mi ahead of the MP 203.9 timetable card) — train length (7,392 ft vs. the 3,700 ft reference the card is sized for) reduced the propagation-adjusted stopping margin at the card location from ~1,286 ft to ~684 ft. Train stopped clear of the absolute signal at MP 204.9 with margin restored to standard. No PTC penalty enforcement triggered.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when building a brake-point plan for a non-standard consist, working through a slack-action sequencing decision, or scheduling around an Hours of Service limit.
- [`references/red-flags.md`](references/red-flags.md) — load when reviewing a trip, an event recorder trace, or a PTC enforcement log for a gap before signing off or briefing a review.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a rules or train-handling term is being used loosely in a report in a way that changes what was actually authorized or verified.

## Sources

- 49 CFR Part 240 (FRA), *Qualification and Certification of Locomotive Engineers* — §240.117 (revocation for serious operational occurrences on an escalating basis: 30 days minimum for a first occurrence, 1 year for a second within a 3-year lookback, 3 years or permanent for a third), §240.201–.211 (recurrent certification, operational monitoring, and unannounced compliance/efficiency testing on a 3-year cycle).
- 49 U.S.C. § 21103, the Hours of Service Act as amended by the Rail Safety Improvement Act of 2008 — 12-hour maximum on-duty limit for train employees, minimum 10 consecutive hours of undisturbed off-duty rest afterward, and the "limbo time"/interrupted-rest provisions governing interim releases at away-from-home terminals.
- 49 CFR Part 236, Subpart I (FRA) — Positive Train Control system requirements (I-ETMS, ACSES, ITCS), including PTC's role enforcing authorized speed and signal compliance via penalty brake application.
- 49 CFR Part 232 (FRA), *Brake System Safety Standards for Freight and Other Non-Passenger Trains* — train brake and end-of-train device requirements, including Subpart F provisions for electronically controlled pneumatic (ECP) brake systems.
- GCOR (General Code of Operating Rules) and NORAC Operating Rules — signal aspect definitions, the number-plate distinction between absolute and permissive (intermediate) signals, and the definition of restricted speed (not exceeding 20 mph, prepared to stop within half the range of vision).
- Al Krug, "Train Handling" and related railroad physics articles — widely cited practitioner-level treatment of brake pipe propagation speed, slack action (buff/draft forces), and grade/tonnage effects on stopping distance; the 900 ft/sec propagation figure and the double-the-requirement operating margin convention are drawn from this and general carrier practice and are flagged as heuristics above.
- NTSB Railroad Accident Report RAR-16/02 (Amtrak Train 188, Philadelphia, 2015) — overspeed entering a curve where PTC was not yet in service on that segment, cited here for the PTC-as-backstop-not-primary-system point in the first-principles core.
- No locomotive-engineer practitioner has reviewed this file yet — flag corrections or gaps via PR.
