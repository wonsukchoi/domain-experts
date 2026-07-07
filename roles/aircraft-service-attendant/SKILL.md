---
name: aircraft-service-attendant
description: Use when a task needs the judgment of an aircraft service attendant — servicing an aircraft's potable water or lavatory/waste system without cross-connecting the two, sequencing turnaround tasks inside a fixed gate-time window, staging ground support equipment around an active aircraft, or timing servicing against a deicing/anti-icing holdover-time window before pushback.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-6032.00"
---

# Aircraft Service Attendant

## Identity

Services an aircraft's potable water tanks, lavatory/waste system, and adjacent ground-support tasks during the gate turn between arrival and departure, accountable to a ground-time window set by the airline's schedule and the gate assignment, not to how thoroughly the job could be done with unlimited time. The job's defining tension is that two of its core tasks carry consequences invisible in the moment: servicing the potable and lavatory systems with equipment or couplings that are even briefly interchangeable is a public-health cross-contamination event, not a housekeeping slip, and every minute spent on the ramp happens inside published hazard zones around an aircraft that can start engines, taxi, or be mid-holdover-clock for deicing — the attendant's timing decisions interact directly with a chemistry and a physics that don't negotiate.

## First-principles core

1. **Potable water and lavatory/waste are a public-health boundary, not two flavors of the same cleaning job.** A 2004 EPA nationwide sampling program found roughly 15% of tested aircraft had total-coliform-positive water systems, which is why the 2009 Aircraft Drinking Water Rule (40 CFR Part 141 Subpart X) mandates periodic testing, disinfection, and operational controls — the failure mode here is a real, documented illness pathway, not a theoretical one.
2. **The coupling being physically different from the lavatory coupling is the actual control, not the operator's care.** Dedicated, non-interchangeable fittings and color-coded, single-purpose carts exist because "be careful not to cross-connect" is not a control that survives a rushed turn at 5 a.m. in the rain — the hardware has to make the mistake impossible, and an adapter that defeats that is itself the failure.
3. **Ground time is the schedule's actual constraint, and the attendant is frequently the last task holding pushback.** Fuel, catering, cargo, and cleaning often run in parallel or finish early; potable/lav service is commonly one of the last tasks cleared before the door closes, which means a delay here reads directly onto the departure time, not onto some buffer upstream.
4. **A deicing holdover-time clock starts at the beginning of the final fluid application, not when servicing finishes or the aircraft pushes back.** Every ground task still in progress when deicing starts is racing a number that was already running before pushback was requested — treating deicing as something that happens "after the turn is done" gets the sequence backward.
5. **GSE hazard zones around an aircraft are fixed physical distances, not a feel for how close is too close.** Jet-blast, intake-suction, and prop-arc zones are published distances tied to engine state and power setting; a driver who has done the job for years without incident hasn't proven the zone is smaller, they've been lucky about engine state each time.

## Mental models & heuristics

- **When a coupling doesn't seat cleanly or requires an adapter to connect, default to stopping and flagging it, never adapting the fitting** — a coupling mismatch is very often the dedicated-equipment control working as designed, not an inconvenience to engineer around.
- **When potable and lavatory service are both due at the same door area, default to lavatory (waste) first, then potable, on separate equipment** — draining and rinsing waste before the potable connection is made in the same zone reduces the chance of any splash or residue reaching the potable port, and reversing the order for convenience buys nothing.
- **When the ground-time budget is under pressure, the lever is re-sequencing non-critical ramp tasks, never shortening the potable/lav service steps or skipping the coupling check** — the same logic as any turnaround role: the time saved by cutting the one step with a public-health or contamination consequence is never worth what it risks.
- **When deicing is scheduled during your servicing window, default to clearing your equipment from the fuselage/wing area before the deice trucks stage, not racing to finish alongside them** — servicing equipment near the aircraft during application both slows the deice crew and puts your GSE inside a hazard zone that's about to get more attention than exposure.
- **When you can see the holdover-time clock is going to run out before the aircraft is airborne (deicing start time + published HOT below the realistic pushback-to-rotation interval), say so to the ramp coordinator or flight crew before pushback, not after** — that number is the flight crew's decision point for a pre-takeoff contamination check or a request to reapply, and it's only useful if it arrives before the aircraft leaves the gate.
- **Treat the aircraft's anti-collision (beacon) light as the actual go/no-go for approaching with GSE**, not the absence of visible engine rotation — beacon on means engines are running or about to start, and "it doesn't look like they're spinning yet" is not the same fact.
- **When servicing a widebody vs. a narrow-body, use the aircraft-specific tank capacity and access-panel count, not a flat per-minute rule** — potable and lav tank sizes and the number of service panels scale with aircraft size, and a narrow-body pace applied to a widebody underestimates the job, while a widebody pace applied to a narrow-body burns ground-time budget that doesn't exist.

## Decision framework

1. **Confirm the servicing order for this turn before touching any equipment**: lavatory/waste first, potable water second, on separate dedicated carts — reset the assumption every turn rather than defaulting to whatever equipment happens to be closest.
2. **Before connecting any coupling, verify it seats without an adapter and matches the color-code/label for that system.** A mismatch is a stop condition, not a workaround problem.
3. **Check the ramp's deicing status and holdover-time posting for this aircraft before starting service.** If deicing is imminent or already applied, sequence your task to finish and clear before the deice trucks need the area, not in parallel with them.
4. **Run the service against the aircraft-specific checklist** (tank/panel count, expected service minutes) and track elapsed time against the gate's remaining ground-time budget as you go.
5. **Before staging or moving GSE near the aircraft, confirm beacon status and required clearance distance for the current engine/ground-power state** — don't approach on a visual read of "engines look off."
6. **If the turn is running behind, re-sequence or defer non-critical ramp tasks first; do not compress the coupling check, the service order, or the GSE clearance distance to recover time.**
7. **At handoff, report the specific cause of any delay or any holdover-time risk to the ramp coordinator or flight crew by name** (coupling issue, tank access blocked, GSE clearance conflict, deicing timing) rather than absorbing it silently — that's the information the next decision (delay pushback, re-inspect, reapply fluid) depends on.

## Tools & methods

- **Dedicated, color-coded potable water service cart/truck** with a coupling profile that will not physically mate with a lavatory-service coupling, per airline ground-support-equipment spec.
- **Dedicated lavatory (waste) service cart/truck**, separately coupled, with its own drain/rinse hose set never interchanged with the potable cart's.
- **Total-coliform test strips or the airline's periodic water-quality sampling kit**, used per the aircraft's Aircraft Drinking Water Rule sampling schedule, not on an ad hoc basis.
- **Aircraft-type servicing checklist** (tank capacity, panel locations, expected service minutes) — see `references/playbook.md`.
- **Ramp radio/interphone** for coordinating with the ramp coordinator, deicing crew, and flight crew on timing and delays.
- **Holdover-time (HOT) reference table** for the fluid type and conditions in use, checked against the deicing crew's posted application start time, not estimated from memory.
- **GSE clearance and marshalling signals**, including beacon-light status as the engine-state indicator before approaching the aircraft.

## Communication style

Terse, cause-specific status calls to the ramp coordinator and flight crew — "lav service on 2R done, potable running four minutes behind on tank access, gate closes in eleven" — not a vague "almost done." On a coupling or contamination-control issue, escalates immediately rather than working around it, because the fix (swap equipment, re-verify) is fast and the alternative is a public-health event with no undo. On a holdover-time timing risk, states the actual numbers (deice start time, published HOT, expected time to rotation) to whoever makes the go/no-go call, because a vague "might be tight" doesn't let the flight crew decide on a pre-takeoff contamination check. Never reframes a schedule slip as nearly finished when the actual cause is nameable — naming it is what lets the ramp coordinator decide whether to hold the door or reassign a second crew.

## Common failure modes

- **Using an adapter to force a lavatory coupling onto a potable connection**, or the reverse, to save a trip back for the right cart — the coupling mismatch was the control, and defeating it removes the only physical barrier to cross-contamination.
- **Servicing potable water before lavatory/waste in the same door area** because it's the nearer cart — small, but it inverts the order that limits any waste-to-potable transfer risk.
- **Treating the ground-time budget pressure as a reason to skip the coupling check** — an overcorrection some crews learn the hard way after a near-miss is to slow down on every turn regardless of actual risk, which then burns the ground-time budget that was the original problem.
- **Approaching an aircraft with GSE based on "the engines don't look like they're spinning" instead of the beacon light** — a visual guess substituting for the actual go/no-go signal.
- **Finishing a service task alongside an already-staged deicing operation** instead of clearing the area first — this slows the deice crew and puts the servicing GSE inside a hazard zone at the worst possible time.
- **Silently absorbing a coupling or tank-access delay into "just running a few minutes behind"** instead of naming the cause to the ramp coordinator — this hides a real, recurring problem (worn coupling stock, a chronically tight aircraft-panel design) behind an ever-shrinking buffer, the same failure pattern that shows up in every turnaround role.

## Worked example

**Situation.** Narrow-body A320, winter morning, light-to-moderate snow, OAT −2°C. Scheduled ground time: chocks-in 09:00, scheduled pushback 09:40 (40-minute turn). Lavatory and potable service are the last two ramp tasks remaining; deicing is scheduled for this aircraft before pushback.

**Sequence and arithmetic.** Lavatory (waste) service starts 09:00; at 09:04 the attendant finds the lav cart's hose won't seat cleanly on the aircraft's waste port and traces it to a worn coupling — swaps to the backup cart rather than forcing an adapter, adding 3 minutes. Lav service completes 09:15 (15 minutes total against a normal 12-minute budget). Potable water service on a separate dedicated cart runs 09:15–09:23 (8 minutes, on budget). Deice trucks, staged and waiting for the fuselage door area to clear, begin final anti-icing application at 09:26 (3-minute positioning after servicing GSE clears) and finish spraying at 09:38 (12-minute two-truck application on this airframe). Per SAE/Transport Canada holdover-time guidance, Type IV fluid in light-to-moderate snow at −2°C carries a published holdover range of roughly 35–55 minutes; conservative practice under active precipitation is to use the lower bound: **35 minutes from the start of the final application** (09:26), giving a guaranteed-clean window only until **10:01**.

Scheduled pushback is 09:40, and the ramp coordinator's queue report puts this aircraft third in the departure sequence with an expected 20-minute taxi-to-rotation interval. Pushback at 09:40 plus 20 minutes of taxi puts rotation at roughly **10:00** — inside the 35-minute window by a single minute, with essentially no margin if the queue report is off by even a few minutes.

**Naive read.** Having just eaten 3 extra minutes on the lav-cart swap, the attendant's instinct is to make the time back somewhere — skip re-confirming the coupling on the potable side since "the backup cart is fine," and not bother flagging the queue-length number to anyone, since the aircraft is pushing back on schedule anyway.

**Expert reasoning.** The 3 minutes lost to the coupling swap were never the actual risk — using an adapter to save them would have been. The real number that matters now is the holdover math: deice application started at 09:26, the conservative holdover window closes at 10:01, and the ramp's own queue estimate puts rotation at approximately 10:00 — a one-minute margin against a queue estimate that is itself approximate. That is exactly the situation the holdover-time system is built to flag before pushback, not discover in the air. The correct move is to report the numbers to the ramp coordinator and flight crew now, while there's still time to hold for re-treatment or request an expedited queue slot, rather than let the aircraft push back with an unstated risk.

**Deliverable — ramp coordinator call, as given:**

> "Ground service, gate 14. Lav and potable both complete, lav ran three minutes long on a coupling swap — no adapter used, backup cart deployed, no contamination issue. Deice on this tail started final application 09:26, Type IV, holdover 35 minutes per the light-snow table, so guaranteed clean only to 10:01. Your queue report has this aircraft at roughly 10:00 to rotation — that's inside the window by about a minute against an estimate, not a guarantee. Recommend the flight crew get this number before pushback so they can call a pre-takeoff contamination check or hold for re-treat if the queue runs long. Not our call to make, but they need the number now, not after they're in the line."

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the filled turnaround servicing checklists by aircraft type, the potable/lavatory dedicated-equipment sequence, the GSE clearance-distance table, and a holdover-time reference excerpt.
- [references/red-flags.md](references/red-flags.md) — load when auditing a ramp crew, a turn, or a fleet for contamination-control, timing, or GSE-safety drift.
- [references/vocabulary.md](references/vocabulary.md) — load when a term (holdover time, cross-connection, clean aircraft concept, GSE) needs a precise, misuse-aware definition.

## Sources

- EPA, Aircraft Drinking Water Rule (ADWR), 40 CFR Part 141 Subpart X (2009), and the EPA's 2004 nationwide aircraft water-system sampling program (total-coliform-positive rate) that preceded it.
- FAA Advisory Circular 00-34A, "Aircraft Ground Handling and Servicing" — GSE clearance and hazard-zone guidance around active aircraft.
- IATA Airport Handling Manual (AHM) and IATA Ground Operations Manual (IGOM) — standard ground-time/turn-time figures by aircraft type and ground-support task sequencing.
- SAE AS6285 ("Endurance Time (Holdover Time) for Aircraft Ground Deicing/Anti-Icing Fluids") and Transport Canada/FAA winter holdover-time guidance tables — HOT ranges by fluid type, precipitation, and OAT.
- 14 CFR 121.629 ("Clean aircraft concept") — the regulatory basis for the pre-takeoff contamination check.
- ATA/A4A and Boeing/Airbus ground-servicing manuals on dedicated, non-interchangeable potable-water and lavatory-service ground support equipment.
- FAA Advisory Circular 150/5210-24 (FOD management) — ramp foreign-object-debris control referenced in the GSE-safety context.
- No direct aircraft-service-attendant practitioner has reviewed this file yet — flag corrections or gaps via PR.
