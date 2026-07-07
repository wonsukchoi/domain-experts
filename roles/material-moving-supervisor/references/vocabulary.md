# Vocabulary

Terms generalists conflate or oversimplify — a supervisor keeps them precise because the shift's target and the compliance ledger both depend on it.

## Fleet mix

The combination of equipment classes (forklifts, reach trucks, pallet jacks, tow tractors) assigned to a shift's tasks, chosen for each class's throughput rate on the specific task type rather than simple availability.

*In use:* "The fleet mix for today's putaway run is 4 forklifts and 2 reach trucks — the reach trucks are slower per move but the narrow-aisle racking makes them the only class that can actually reach those levels."

*Common misuse:* treating fleet mix as just "how many machines we have," rather than which class is matched to which task type and at what measured rate.

## Utilization rate (equipment)

The ratio of a shift's task target to the fleet's total available capacity (certified-available operators × throughput rate × hours), or equivalently the share of available machine-hours actually producing output. Has two failure directions: too low wastes cost on idle capacity, too high removes slack for a breakdown or maintenance window.

*In use:* "We're at 89% utilization on this roster — that's above our no-slack line, so we either add a unit or trim the target."

*Common misuse:* treating utilization as a KPI to maximize toward 100%, instead of a number with an upper failure threshold as well as a lower one.

## Trigger-event recertification

The requirement under OSHA 1910.178(l) that an operator be re-evaluated after specific events — an incident, a near-miss, an unsafe-operation observation, assignment to a new truck class, or a changed workplace hazard — independent of the standing 3-year evaluation cycle. The trigger, not the calendar date, determines whether the operator is cleared.

*In use:* "His card doesn't expire for another year, but he had a near-miss on Tuesday — that's a trigger event, so he's off the floor until the evaluation's logged."

*Common misuse:* treating a currently-valid standing certification as blanket clearance, ignoring that a trigger event resets the requirement regardless of remaining validity.

## Certification currency

The roster-wide, supervisor-owned tracking of which operators are actually cleared to run which equipment class right now — distinct from an individual operator's personal awareness of their own card status. It is a recordkeeping obligation under 1910.178(l), not a courtesy check.

*In use:* "Certification currency isn't 'ask each operator if they're good' — it's the roster I check against the tracking system before I build the shift assignment."

*Common misuse:* treating certification status as something each operator reports on their own, rather than a fact the supervisor is obligated to verify from records.

## Throughput rate

The measured moves-per-hour a specific equipment class achieves on a specific task type at this site, pulled from the WMS pick-rate report rather than assumed or remembered from a different site or a different task.

*In use:* "Forklifts are running 14 moves an hour on this route today — that's the number I use for the capacity math, not the 18 they hit on the shorter dock run."

*Common misuse:* applying one equipment class's rate on one task type as if it were a fixed property of the machine, when the actual rate varies by task distance, height, and racking density.

## Heinrich's triangle / accident ratio

The originally-proposed 1:29:300 ratio (H.W. Heinrich, 1931) of major injuries to minor injuries to no-injury near-misses, used as the argument for why near-miss reporting matters — later research (Bird, 1974) found a larger no-injury layer (roughly 1:10:30:600) using a different, larger dataset. Both are arguments for reporting culture, not literal predictions for any one site.

*In use:* "The ratio isn't 'we should expect exactly one serious injury per 300 near-misses here' — it's the reason we chase every near-miss report instead of letting it go as a non-event."

*Common misuse:* treating the specific ratio numbers as a predictive model for a given site's incident rate, rather than as the historical argument for why near-miss data is worth collecting at all.

## Near-miss

An event where no equipment or personal damage occurred but the conditions for an incident were present — a dropped load that missed a pedestrian, a near-tip caught by the operator, a blind-corner close call. Distinct from a recordable incident, but treated with the same investigation rigor because it's the same failure mode that hasn't produced harm yet.

*In use:* "Nobody got hurt and nothing broke, but that's still a near-miss report, not a non-event — log it and pull the operator for the same evaluation an incident would trigger."

*Common misuse:* treating the absence of injury or damage as the absence of anything worth reporting, which is exactly the underreporting pattern that erodes the leading-indicator value of near-miss data.

## PM (preventive maintenance) window / slack

The scheduled downtime a unit needs for maintenance, and the shift-capacity margin required to absorb it (or an unplanned breakdown) without missing the target. A fleet run at very high utilization has no such margin.

*In use:* "That forklift's PM is overdue by 40 hours — running the fleet at 89% utilization means if it goes down today, there's no other unit to absorb the difference."

*Common misuse:* scheduling PM windows without checking whether the shift's utilization has any slack to absorb the resulting capacity loss.

## Idle time / idle-cost

The gap between an equipment unit's engine or power-on hours and its actual productive (task-performing) hours, tracked by fleet telemetry. Rising idle time on a specific unit is either a task-assignment problem (nothing routed to it) or an early signal of a developing mechanical issue operators are avoiding.

*In use:* "Unit 12's idle time has crept up three shifts running — either we're not assigning it enough work, or operators are quietly steering around something wrong with it."

*Common misuse:* treating idle time only as a scheduling inefficiency, without checking whether it's actually a maintenance signal in disguise.

## Substitution cost (equipment)

The throughput penalty incurred when a task normally run on one equipment class is reassigned to a different class because the first is short-staffed or unavailable — expressed in the difference between the two classes' measured rates for that specific task type.

*In use:* "Putting this putaway run on pallet jacks instead of reach trucks isn't free — it's a 30% throughput hit on this specific task, and that has to come out of the shift's capacity math."

*Common misuse:* assuming any available machine can absorb a task at roughly the same rate, when the substitution's actual cost is a specific, calculable number.

## Labor-equipment capacity

The product of certified-available operators, an equipment class's measured throughput rate, and shift hours — the actual capacity figure a supervisor plans against, as opposed to a raw operator or machine count.

*In use:* "We have 6 forklifts, but labor-equipment capacity is only 4 operators times 14 moves times 8 hours, because two are pulled for certification reasons."

*Common misuse:* quoting equipment count or operator headcount alone as if either one, on its own, were the capacity number.
