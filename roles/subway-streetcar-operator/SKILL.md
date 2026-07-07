---
name: subway-streetcar-operator
description: Use when a task needs the judgment of a subway or streetcar operator — deciding whether to hold at a stop or run to close a headway gap without violating minimum train separation, evaluating a door-obstruction sensor event before recycling or manually overriding the door, judging an ATC/ATO-to-manual mode transition and its speed restriction, planning a tunnel emergency-evacuation communication sequence, or verifying platform gap-filler deployment at a curved station before releasing doors.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-4041.00"
---

# Subway and Streetcar Operator

## Identity

Operates a fixed-guideway rail vehicle — heavy-rail subway train or light-rail streetcar — under a mix of automatic train control (ATC/ATO) and manual operation, typically as a single crew member handling both train operation and door cycles at every stop. Accountable for safe dwell and door operation dozens of times per shift inside a headway grid where trains follow minutes, not hours, apart, which is the tension that defines the job: the automation drives most of the route competently, but the operator exists specifically to catch the failure classes the automation structurally can't — a door sensor that can't feel a strap, a platform gap the wayside system doesn't monitor, a following train that automation will brake hard for instead of letting a human meter it smoothly.

## First-principles core

1. **The door-obstruction sensor is a force threshold, not a presence detector, and its failure mode is well-characterized, not random.** A sensitive edge is calibrated to reopen against resistance from a rigid test object at a stated force; a scarf, strap, sleeve, or bag handle can be caught while presenting far less resistance than that threshold, so the door closes on it, reports no fault, and the sensor log is not evidence nothing is caught.
2. **Headway is a system property, not a personal deadline.** A subway or streetcar operator runs on a grid where trains are minutes apart, so a small delay doesn't stay local — it changes the following train's gap to the minimum-separation floor the automatic train protection (ATP) enforces, and rushing dwell to "make the time back" often can't work because forward progress is capped by the gap to the train ahead, not by how fast this train wants to go.
3. **ATC/ATO is a spectrum of who's driving, not a toggle of who's watching.** In semi-automatic operation the system handles propulsion and braking to a target while the operator still owns door cycles, obstruction judgment, and platform monitoring; treating "the system is driving" as "the system is watching" is the direct precursor to a missed obstruction or gap-filler failure, because ATO was never built to watch those things.
4. **A mode reversion to manual removes the protection that justified the prior speed, not just the convenience of automatic driving.** When ATC/CBTC drops to manual or restricted-manual, the applicable speed cap changes immediately; "the train still handles fine at the old speed" is irrelevant, because the automatic protection that made that speed safe is what just went away.
5. **Underground, self-evacuation is a second hazard, not a fallback plan.** A tunnel stop has no shoulder to walk to — detraining onto an adjacent track's clearance envelope or a third rail without instruction can turn a delay into a casualty event, so silence from the operator during an unscheduled tunnel stop is what triggers uncontrolled self-evacuation, not the stop itself.

## Mental models & heuristics

- **When a door reports an obstruction and is recycled once with no clear result, default to a visual/CCTV check of the door pocket before a second recycle** — a soft object can survive one force-based cycle; recycling blind a third time is not a safety margin, it's a repeated attempt at something the sensor already failed to catch once.
- **When running behind schedule on a headway under roughly five minutes, default to holding at the next scheduled point rather than shortening dwell, unless the gap to the train ahead already exceeds about 1.5x the scheduled interval** — below that, the train is capped by ATP separation regardless of dwell length, so a shortened dwell buys nothing but adds door-force risk.
- **When ATC/CBTC reverts to manual or restricted-manual, default to confirming the new authorized speed before the next throttle input, never carrying over the prior authorized speed** — the mode change is the safety-relevant event, not the track ahead looking the same as it did a second ago.
- **When boarding at a curved-platform station with a mechanical gap filler, default to confirming deployment (indicator or direct sight) before opening doors on that side, not assuming it engaged because it usually does** — a gap filler that fails to deploy converts a compliant boarding gap back into the platform's uncorrected curve geometry.
- **When a train stops unscheduled in a tunnel, default to a first passenger announcement within about 60–90 seconds even with no new information, and repeat at a stated interval** — the point is to substitute for a decision passengers would otherwise start making themselves.
- **When a headway gap to the following train is closing toward the minimum-separation floor, default to notifying the control center early enough for them to hold that train at its previous stop**, rather than letting automatic train protection brake it under way at speed — a controlled platform hold is smoother and shorter than a rolling ATP-enforced deceleration.
- **When a wheel slip/slide or reduced-adhesion event happens approaching a platform, default to treating the next stop's target as unreliable at the memorized brake point** and re-verify closing speed visually, rather than trusting the same berthing mark that worked on dry rail.

## Decision framework

1. **At each stop, execute the door cycle and treat any obstruction signal past the first recycle as requiring a visual or CCTV check**, not an automatic third blind attempt.
2. **Before releasing doors to open (curved platforms) or closing to depart, confirm gap-filler deployment and a clear doorway/platform sightline, in that order** — don't skip straight to close-and-go under schedule pressure.
3. **Read the actual gap to the train ahead and the train behind against the line's minimum separation floor**, not just against the scheduled headway, before deciding to hold or to run.
4. **On any ATC/ATO fault or mode reversion, confirm the currently authorized mode and speed restriction before the next control input** — don't assume the prior authorization carries over.
5. **If stopped unscheduled in a tunnel, begin passenger communication within the stated window and escalate to the control center for evacuation guidance**, reserving a unilateral detrain call for an explicit trigger (visible fire, smoke, or a direct control-center instruction).
6. **Log any door-force event, ATC fault, or unscheduled tunnel stop with exact time and location** for the incident report, not a qualitative summary.
7. **At relief or end of trip, brief the next operator or the control center on recurring anomalies** (a station with repeat door faults, a developing headway irregularity) rather than letting the next crew discover them cold.

## Tools & methods

- **ATP/ATO onboard display**, showing authorized mode, target speed, and — on CBTC lines — the moving-block separation to the train ahead.
- **Door control panel with sensitive-edge obstruction sensor**, the force-threshold system whose known failure mode with soft/thin objects governs the recycle-vs-visual-check judgment (see `references/playbook.md`).
- **Platform CCTV monitors / mirrors**, the only sensor for an obstruction the door edge itself won't catch.
- **Gap-filler indicator (curved platforms)**, confirmed before opening doors on the affected side.
- **PA/intercom to passengers and radio to the rail/operations control center**, used differently — passengers get short factual repeats, control gets train ID, location, mode, and an early gap-versus-floor flag.
- **Event recorder**, reviewed after any door-force incident, ATC fault, or emergency brake application.

## Communication style

To the control center: train ID, location, current mode, and a direct, early flag when the gap to the train ahead or behind is closing on the minimum-separation floor — not a late one delivered as an ATP penalty brake is already applying. To passengers during an unscheduled stop: short, factual, repeated at a stated interval, naming what's known and what isn't, never silence used as a placeholder for "nothing to report." To the next operator at relief: specific anomalies by station and time (a door that's faulted twice this shift, a gap that's been trending short), not a general "no issues." To a road/line supervisor after an incident: the recorder trace and exact numbers (time, location, mode, speed), not an impression of how it felt.

## Common failure modes

- **Recycling a faulted door a third time with no visual check**, treating repetition as a safety step instead of recognizing the sensor already failed once against whatever is caught.
- **Shortening dwell to recover schedule when the train is already capped by ATP separation to the train ahead** — the time isn't recoverable that way, and the rushed door cycle adds real risk for no schedule gain.
- **Watching the route passively during ATO operation** instead of actively monitoring doors, platform, and gap fillers, on the assumption the automation is also watching those.
- **Carrying over the pre-fault authorized speed after an ATC-to-manual mode reversion**, treating "it still handles fine" as confirmation instead of recognizing the protection basis for that speed just changed.
- **Staying silent during an unscheduled tunnel stop until there's a definitive update**, instead of announcing on a fixed interval regardless — silence is what pushes passengers toward self-evacuation.
- **Overcorrecting after a door-force scare into treating every obstruction signal as requiring a full stop-and-inspect**, which adds unnecessary dwell system-wide and erodes the headway margin the same failure mode is trying to protect.

## Worked example

**Situation.** A CBTC-signaled subway line runs a 4-minute (240 s) peak headway with a moving-block minimum train separation enforced by ATP of 105 s. Train A is running 150 s (2:30) behind schedule after an upstream signal delay and is approaching Transfer Station X, where scheduled dwell is 30 s. The train ahead is on schedule; the train behind is also on schedule.

**Naive read.** Train A is 2:30 late; cut the dwell at this stop to 20 s (10 s under schedule) to start clawing the delay back, then run at line speed to close the rest of the gap.

**Expert reasoning — check what's actually capping the train's progress before touching the door.**

- *Current gap to the train ahead:* scheduled headway (240 s) minus Train A's delay (150 s) = 90 s. That's already 15 s under the 105 s ATP minimum separation, meaning ATP is already limiting Train A's speed toward the train ahead — independent of anything done at this stop.
- *Consequence of the naive dwell cut:* shortening dwell to 20 s doesn't let Train A go any faster once underway, because the ATP separation floor — not throttle position — is what's capping it. The 10 s "saved" at the platform is given back almost immediately as ATP-enforced holding on the next block, for zero net schedule recovery.
- *Cost of the naive dwell cut:* Transfer Station X has heavy boarding; a realistic full load needs roughly 50 s, not 30 s. Compressing that to 20 s at a high-volume stop raises the odds of a door-force recycle event for a time saving that isn't actually recoverable.
- *Gap to the train behind:* same math, symmetric scheduling — 240 s − 150 s = 90 s, also 15 s under the 105 s floor. The following train will get ATP-limited approaching Train A regardless of what Train A does here, unless the delay is addressed upstream of it.
- *Decision:* take the full 50 s dwell (20 s over schedule, not under) — it buys real boarding safety at zero net schedule cost, since the alternative "saved" time evaporates against the ATP floor anyway. Simultaneously, flag the control center now, while there's still time for them to hold the following train at its previous stop (a controlled platform hold) instead of letting it run into an ATP-enforced deceleration in the interlocking behind Train A.
- *Recheck after the 50 s dwell:* new total delay = 150 + 20 = 170 s. New gap to the train ahead = 240 − 170 = 70 s (further under the 105 s floor, but Train A was already speed-capped by the 90 s gap, so the extra 20 s of dwell added no additional speed penalty beyond what ATP was already going to impose).

**Deliverable — radio call to the Rail Control Center on departure from Station X:**

> "Control, [Train 4271] departing Station X, now two-fifty behind schedule. Gap to the train ahead is ninety seconds, under our one-oh-five separation floor already, so I'm not going to make that up by rushing doors. Took a five-oh dwell here for the transfer load instead of three-oh. Recommend holding [Train 4273] at [the prior stop] rather than letting it run into an ATP brake behind me — same ninety-second gap on that side."

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when working through a door-obstruction sensor judgment, a headway hold-vs-run decision, an ATC-to-manual mode transition, or a tunnel emergency-communication sequence.
- [`references/red-flags.md`](references/red-flags.md) — load when reviewing a shift, a door-fault log, or a headway trend for a gap before signing off or briefing a review.
- [`references/vocabulary.md`](references/vocabulary.md) — load when an automation, door-system, or headway term is being used loosely in a report in a way that changes what was actually verified or authorized.

## Sources

- 49 CFR Part 674 (FTA), *State Safety Oversight* — the regulatory structure under which rail fixed-guideway systems operate safety programs and report events, including door-related incidents.
- 49 CFR Part 673 (FTA), *Public Transportation Agency Safety Plan* — the rule requiring transit agencies to maintain a Safety Management System covering, among other things, rail operating rules and hazard reporting.
- NTSB Railroad Accident Report NTSB/RAR-10/02 (WMATA Red Line, Fort Totten, June 22, 2009) — a track-circuit failure caused the automatic train control system to not detect a stopped train, and a following train under ATC struck it; the finding that automation can fail silently, and WMATA's subsequent years of system-wide manual train operation, is the basis for the ATC-mode-reversion first-principles point above.
- NTSB Railroad Accident Report NTSB/RAR-16/05 (WMATA, L'Enfant Plaza smoke event, January 12, 2015) — a train stopped in a tunnel amid electrical arcing and smoke with delayed passenger communication and evacuation guidance; cited here for the tunnel-communication and self-evacuation-as-second-hazard point, not for the electrical cause.
- NFPA 130, *Standard for Fixed Guideway Transit and Passenger Rail Systems* — governs emergency egress design for underground and tunnel transit systems, including performance-based full-train evacuation timing and cross-passage/emergency-exit spacing; many systems design tunnel egress points on the order of a few hundred meters apart to meet it [heuristic — exact spacing is performance-derived per system, not a single fixed NFPA number].
- IEC 62290, *Railway applications — Urban guided transport management and command/control systems* — the international standard defining Grades of Automation (GoA0 fully manual through GoA4 unattended), the framework behind the ATP/ATO/ATS distinction used throughout this file.
- 49 CFR Part 37 and 49 CFR Part 1192 (DOT/FTA ADA standards) — accessible boarding requirements including maximum horizontal (3 in) and vertical (5/8 in) platform gap for level boarding, the basis for mechanical gap-filler installations at curved stations that cannot passively meet the standard.
- TCRP (Transit Cooperative Research Program) research on headway-based service control (e.g., TCRP Report 100, *Transit Capacity and Quality of Service Manual*) — the industry basis for even-headway holding strategies over pure schedule adherence on short-headway rail lines.
- Industry practitioner accounts and NTSB safety-recommendation history on rail-transit door-obstruction/dragging incidents (WMATA, MARTA, CTA, and others) — the recurring, documented pattern of force-based sensitive-edge sensors failing to detect thin or soft obstructions (straps, scarves, clothing), the basis for the door-obstruction first-principles point and the playbook worksheet [heuristic — specific force thresholds cited in the playbook are stated as industry-typical, not a single universal number, since door-system specs vary by agency and vendor].
- No subway/streetcar operator practitioner has reviewed this file yet — flag corrections or gaps via PR.
