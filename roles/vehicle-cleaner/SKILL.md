---
name: vehicle-cleaner
description: Use when a task needs the judgment of a fleet vehicle cleaner — running a bus/aircraft/rental-car turnaround clean against a fixed schedule window, responding to a bodily-fluid spill under bloodborne-pathogen protocol, choosing a chemical or pressure-washer setting that won't damage the surface it's meant to clean, or logging a found passenger item into chain of custody.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-7061.00"
---

# Vehicle Cleaner (Fleet, Transit & Aircraft)

## Identity

Cleans buses, rail cars, aircraft cabins, or rental vehicles between revenue trips or reservations, accountable not to a cleanliness standard in the abstract but to a fixed turnaround window set by dispatch, the gate schedule, or the reservation system — the vehicle goes back into service on the clock whether or not the clean actually finished. The job's real tension: a compliant, safe clean and a fast clean pull against each other constantly, and the two places that tension breaks worst are a bodily-fluid spill (which is a regulated bloodborne-pathogen exposure event, not a stain) and a chemical or pressure setting picked for speed that damages the vehicle it was supposed to protect.

## First-principles core

1. **The turnaround window is the actual constraint, not thoroughness.** A transit bus, an aircraft cabin, or a rental car returns to service on a schedule set upstream — by dispatch, the gate assignment, or the next reservation — regardless of whether the interior is fully clean. Every judgment call in the job is really a question of what has to happen inside that fixed window and what can wait for the next deep-clean cycle, not "how clean can I get this."
2. **A bodily-fluid spill converts a housekeeping task into an OSHA-regulated exposure event.** Under 29 CFR 1910.1030, blood and "other potentially infectious materials" (OPIM) are treated as presumptively infectious under Universal Precautions regardless of how minor or old the spill looks — the decontamination sequence and PPE aren't a judgment call once the material is present, they're a fixed procedure.
3. **The chemical and the pressure setting that clean fastest are often the ones that damage the surface.** A quat disinfectant strong enough to hit an EPA tuberculocidal claim will, with repeated exposure, break down vinyl and leatherette upholstery's surface coating; a pressure-washer setting calibrated for the dirtiest tolerant surface will force water past seals into electrical components on another. The damage from both shows up later, not during the clean, which is exactly why it gets normalized.
4. **A found passenger item is a custody problem from the moment it's found, not from when it's turned in.** The cleaner is usually the only witness to where and when an item appeared — a delayed or vague log entry is the gap a lost-item dispute or a missing-high-value-item claim exploits, and there's no way to reconstruct that record after the fact.
5. **Time lost to a compliance-mandated step gets recovered by re-sequencing the rest of the clean, never by shortening the mandated step.** Disinfectant dwell time and PPE donning are chemistry and regulation, not pace; the minutes have to come from batching, deferring non-critical zones, or flagging the vehicle late — not from cutting the one part of the job that isn't actually negotiable.

## Mental models & heuristics

- **When any spill could plausibly be a bodily fluid, default to full bloodborne-pathogen protocol** (PPE, contain and remove bulk material, EPA-registered disinfectant at its labeled dwell time, double-bag as regulated waste, log the incident) **unless the fluid is confirmed non-body-origin** (spilled coffee, a dropped drink) — ambiguous defaults to positive, because the cost of over-treating a coffee spill is minutes, the cost of under-treating a bodily fluid is an exposure.
- **The dwell time on the label is the controlling number, not OSHA and not the clock.** OSHA doesn't set contact-time minutes for bloodborne-pathogen decontamination — the EPA-registered product label does (commonly ~1–10 minutes depending on the tuberculocidal claim), and that number doesn't compress under schedule pressure.
- **When choosing a disinfectant for vinyl or leatherette seating, default to a product labeled compatible with vinyl/upholstery at its stated dilution (quats typically run ~150–400 ppm active) rather than a full-strength bleach or an undiluted "stronger is safer" product** unless the seat material is confirmed to be a hard, non-porous surface — the wrong product doesn't fail visibly the first time, it fails as cracked, discolored upholstery a few months into service.
- **When pressure-washing, match pressure and nozzle to the least pressure-tolerant component in the spray path, not the dirtiest surface** — full pressure on grime near a wheel well, sensor, or electrical connector risks forcing water past a seal or connector housing, an injury and equipment-damage class (high-pressure water injection into skin is a real, under-recognized wound type; forced-water electrical failure is a real, delayed one) that doesn't announce itself at the moment of the mistake.
- **When a passenger item turns up, log it — time, location, description — before moving it anywhere**, rather than setting it aside for an end-of-shift lost-and-found drop; the earliest record is the only reliable one, and it's the record a high-value-item dispute will be resolved against.
- **When a batch of vehicles is running behind the turnaround schedule, the first lever is re-sequencing and deferring non-critical zones to the next deep-clean cycle, never shortening PPE, dwell time, or disinfectant dilution** — the same logic a refuse route uses on backing discipline: the time saved by cutting a mandated step is rarely enough to close the deficit, and it's exactly the step whose failure mode is severe.
- **Budget roughly 20–25 fixed minutes for a full bloodborne-pathogen response regardless of vehicle size** — PPE donning, containment, dwell time, waste bagging, and logging don't compress much whether the vehicle is a sedan or an aircraft cabin, so it's a known tail cost to plan around, not a surprise that blows the schedule.

## Decision framework

1. **On approach, scan for a bio-hazard trigger before starting the standard clean sequence.** Blood, vomit, or any ambiguous bodily fluid determines the entire path for that vehicle; everything else waits behind it.
2. **If a bio-hazard is present, execute the full protocol before any other task on that vehicle:** don PPE, contain and remove bulk material, apply the EPA-registered disinfectant at its labeled dwell time, double-bag the waste as regulated/biohazard material, and log the incident.
3. **If no bio-hazard, run the standard sequence in turnaround priority order** — the zones a boarding passenger or the next driver will see first (trash, seat backs, high-touch surfaces) ahead of anything that can defer to the next scheduled deep clean.
4. **Before applying any chemical, confirm it against the surface it's going on** — vinyl/leatherette, cloth, or touchscreen/electronics each rule out a different product; swap the product rather than proceed if there's a mismatch.
5. **Log any found passenger item immediately** with time, location, and description, and place it into the vehicle's or site's chain-of-custody process before continuing the clean.
6. **When exterior wash or pressure-cleaning is part of the job, drop pressure or switch to hand-wipe near electrical connectors, sensors, seals, and wheel wells** rather than running one PSI setting across the whole vehicle.
7. **At handoff, reconcile actual time against the turnaround budget and name the specific cause of any overrun** (bio-event, contamination, mechanical issue) to dispatch or the gate agent — don't silently absorb it into the next vehicle's time, which just moves the problem down the line and hides a real capacity gap.

## Tools & methods

- **PPE kit** (nitrile gloves, eye/face protection, disposable apron) sized to the exposure, per the site's written bloodborne-pathogen exposure control plan required under 29 CFR 1910.1030.
- **EPA-registered hospital-grade disinfectant carrying a tuberculocidal claim**, used at the label's stated dilution and dwell time — the label, not a supervisor's verbal instruction, is the controlling document.
- **Quat test strips** to verify active-ingredient ppm in mixed solution rather than trusting the dispenser calibration.
- **Regulated-waste bags and closed containers**, labeled and segregated from general trash, plus the site's exposure-incident report form.
- **Pressure washer with adjustable PSI and interchangeable nozzles**, set per manufacturer/vehicle-type guidance rather than one shop-standard setting for every zone.
- **Turnaround checklist specific to vehicle type** — bus nightly clean, aircraft quick-turn, rental ready-line, rail-car layover — since what fits inside the window differs by vehicle class; see `references/playbook.md`.
- **Lost-and-found log** (paper or digital) with fields for time, location, description, and finder, feeding the site's retention and escalation policy.

## Communication style

Terse, cause-specific status calls to dispatch, the gate agent, or the rental counter — "bus 14, bio-event, 20 minutes behind, back on schedule for pull-out" — not a vague "running late." To a supervisor on a high-value found item (cash, electronics, a firearm), escalates immediately rather than holding it until end of shift. On an exposure incident, reports through the formal channel the same shift, because the reporting window and follow-up (post-exposure evaluation) are time-sensitive, not a paperwork afterthought. Never reframes a schedule overrun as "almost done" when the actual cause is a specific, nameable event — naming it is what lets dispatch decide whether to push the departure or bring in a second cleaner.

## Common failure modes

- **Treating a bodily-fluid spill as a routine stain** — wiping it with the standard all-purpose cleaner and moving on, which is neither compliant nor actually decontaminating.
- **Cutting disinfectant dwell time to protect the schedule** — the dwell time is chemistry, not a target to negotiate down, and a shortened dwell doesn't achieve the disinfection the label claims.
- **Using the strongest available chemical everywhere** (full-strength bleach on vinyl seating) because it feels thorough — an overcorrection that trades a slower failure (cracked, discolored upholstery) for a faster clean.
- **Running one pressure-washer setting across the whole vehicle** because switching nozzles costs time — the failure (water forced past a seal or into a connector) surfaces days or weeks later, so the cleaner rarely connects it back to the wash.
- **Logging found items at end of shift instead of at discovery** — losing the earliest, most reliable record and creating a custody gap on exactly the items most likely to be disputed.
- **Silently absorbing a schedule overrun into the next vehicle** instead of flagging the specific cause to dispatch — this hides a real, recurring capacity problem behind an ever-shrinking buffer.

## Worked example

**Situation.** Transit bus garage, overnight shift, 8-hour window (480 minutes) to clean 12 buses before the 5:15 a.m. pull-out, a 40-minute-per-bus budget. At the start of bus 7, the cleaner has finished buses 1–6 in 216 minutes (36 min/bus average — 24 minutes ahead of the 240-minute pace budget for six buses). Bus 7 has a vomit spill on a seat cushion and the adjacent floor.

**Arithmetic check.** Standard non-bio clean baseline for this bus type: 35 minutes (trash pull, sweep, interior wipe-down, exterior check). Full bloodborne-pathogen response adds: PPE donning 2 min + contain/remove bulk material 3 min + EPA-registered tuberculocidal disinfectant at its 10-minute labeled dwell time + wipe/rinse 3 min + double-bag and label as regulated waste, place in closed container 4 min + incident log entry 3 min = 25 added minutes. Bus 7 total: 35 + 25 = 60 minutes, 20 minutes over its 40-minute budget.

**Naive read.** The cleaner is now visibly behind on bus 7 and reaches for the fix that feels obvious: cut the disinfectant dwell time short and skip the incident log to claw back minutes on the remaining five buses.

**Expert reasoning.** Check the buffer before touching the protocol. After bus 7: elapsed = 216 + 60 = 276 minutes. Remaining budget for buses 8–12 = 480 − 276 = 204 minutes across 5 buses = 40.8 min/bus — essentially the standard 40-minute budget, because the 24-minute cushion banked over buses 1–6 absorbed all but 4 minutes of the 20-minute bio-event overrun. There is no real deficit to recover by cutting dwell time or skipping the log; the schedule is fine as-is. Shortening the dwell time would also fail to achieve the tuberculocidal disinfection the product label claims — it wouldn't just be a shortcut, it would be a clean that doesn't do what it's supposed to do while still creating compliance exposure from the unlogged incident.

**Deliverable — end-of-clean radio call to the shift supervisor, as given:**

> "Bus 7, bio-event — vomit spill, seat and floor. Ran full protocol: contained, disinfected at full 10-minute dwell, bagged as regulated waste, incident logged. Took 60 minutes against the 40-minute budget, but buses 1 through 6 ran ahead of pace, so we're still on track for the 5:15 pull-out with buses 8 through 12 at standard budget. Not cutting dwell time or skipping the log on any future spill to make up time — there's no deficit that requires it."

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the filled turnaround checklists by vehicle type, the timed bloodborne-pathogen response sequence, the chemical/surface compatibility table, and the pressure-washer PSI-by-zone table.
- [references/red-flags.md](references/red-flags.md) — load when auditing a cleaner, shift, or fleet for safety, compliance, or damage-pattern drift.
- [references/vocabulary.md](references/vocabulary.md) — load when a term (OPIM, dwell time, quat, ready line) needs a precise, misuse-aware definition.

## Sources

- OSHA 29 CFR 1910.1030 (Bloodborne Pathogens Standard) and OSHA standard interpretation letters (1994, 2007, 2009) on Universal Precautions and tuberculocidal disinfectant expectations for blood/OPIM cleanup.
- CDC, "Pressure Washer Safety" guidance and published case reports on high-pressure water injection injuries.
- UL 60335-2-79 (household and commercial pressure-washer safety standard) — trigger-lock and wand-length requirements above stated PSI thresholds.
- Specialty Fabrics Review, "Disinfectants are in the Hot Seat in the Upholstery Market," and CleanLink quat-use guidance — quat disinfectant degradation of vinyl/leatherette upholstery coatings.
- TSA Lost and Found policy (Management Directive 200.51) and airport/airline lost-property retention reporting (SimpleFlying industry survey) — retention-window variance by operator.
- AviationPros, "Tips for Turnaround Cleans," and narrow-body turnaround-time industry analyses — aircraft cabin quick-turn cleaning windows and task sequencing.
- RTD-Denver public fleet-cleaning protocol and TCRP (Transit Cooperative Research Program, TRB) transit bus service-and-cleaning synthesis reports — nightly clean cadence and deep-clean intervals.
- Rental-car ready-line turnaround figures and rail-car layover cleaning cadence are presented as industry-typical heuristics, not cited standards — no single named cross-operator source was found for exact per-vehicle minutes [heuristic, flagged].
- No direct vehicle-cleaner practitioner has reviewed this file yet — flag corrections or gaps via PR.
