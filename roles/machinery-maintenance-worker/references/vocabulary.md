# Vocabulary

Terms generalists blur together that a route worker keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## Relube interval vs. grease quantity

**Relube interval** is *how often* a point gets serviced — a duty-cycle-adjusted number of operating hours or a calendar conversion of it. **Grease quantity** is *how much* goes in at each service, calculated from bearing dimensions. They're independent numbers; getting one right doesn't fix the other.

*Practitioner usage:* "Interval's corrected to every 7 weeks now, but I was still eyeballing the quantity — turns out it should be 15 grams, not 'until it looks full.'"

*Common misuse:* treating a shortened interval as license to add more grease each time, or believing a correct quantity at the wrong interval solves an under-lubrication problem — both numbers have to be right independently.

## Duty-cycle / environmental factor

A multiplier applied to an OEM baseline relube interval to account for conditions worse than "normal duty" — contamination, heat, shock load, continuous operation. Factors compound when more than one applies.

*Practitioner usage:* "OEM says 2,000 hours, but this one's got heavy dust — that's a 0.5 factor, so 1,000 hours effective, not 2,000."

*Common misuse:* applying the OEM's stated interval unchanged to every environment the equipment happens to sit in, regardless of how far it diverges from the "normal duty" assumption the manual was written for.

## Deflection vs. tension (belt)

**Deflection** is how far a belt moves under a perpendicular force at midspan, measured in inches (or fraction of span length). **Tension** is the actual force required to produce that deflection, read from a gauge and checked against the belt section's force chart. A belt can hit the target deflection distance at the wrong force if the gauge reading is ignored.

*Practitioner usage:* "Deflection's right at 9/16 inch, but the gauge only reads 3 pounds against a 5-to-7 spec — it's still loose, the distance alone doesn't confirm tension."

*Common misuse:* checking deflection distance by eye or feel and skipping the force-gauge reading, which is how belts end up tensioned "close enough" in either direction.

## PM compliance vs. PM effectiveness

**PM compliance** is the percentage of scheduled preventive-maintenance points completed on time. **PM effectiveness** is whether those completed services actually catch and prevent the failures they're meant to — a program can run high compliance and still miss real leading indicators if the checks themselves are shallow.

*Practitioner usage:* "We're at 95% compliance, but effectiveness is the real question — are the missed items low-criticality, or is the 5% hiding the points that actually matter?"

*Common misuse:* reporting compliance percentage alone as proof the maintenance program is working, without checking whether the completed services are catching anything or just going through the motions.

## Baseline vs. absolute threshold

A **baseline** is a specific asset's own recent history (its last several readings). An **absolute threshold** is a fixed number applied across assets or industry-wide. A reading can be unremarkable against an absolute threshold and still be a real finding against its own baseline, or vice versa.

*Practitioner usage:* "175°F isn't an alarming absolute number, but it's 44 degrees above this bearing's own baseline — that's the finding, not the 175."

*Common misuse:* judging every reading only against a single fixed "danger number" and ignoring that a fast rise relative to an asset's own quiet history is often the earlier and more reliable signal.

## Escalation vs. work order

**Escalation** is a route worker's flag that a finding is outside their scope, handed to a mechanic or reliability tech with the specific data behind it. A **work order** is the formal, scheduled task that may or may not result from that escalation, after someone with authority to plan it decides urgency and scope. Not every escalation becomes an immediate work order, and not every work order originates from an escalation.

*Practitioner usage:* "I escalated the temperature reading same-shift; whether it becomes an emergency work order or gets folded into next week's PM window is the mechanic's call, not mine."

*Common misuse:* treating "I flagged it" as equivalent to "it's being fixed," or conversely writing up a full repair work order from the route sheet without the diagnostic step that's supposed to happen in between.

## Over-lubrication / churning

**Over-lubrication** is adding more grease than the bearing housing is designed to hold or dissipate heat from. **Churning** is the specific mechanism by which excess grease causes damage — the rolling elements work the excess grease instead of just the intended film, generating heat and pressure that can blow a seal or accelerate degradation.

*Practitioner usage:* "It's not under-greased, it's over-greased — the housing's hot from churning, not from lack of lubricant."

*Common misuse:* assuming a hot bearing always means it needs more grease, when a housing packed past its fill fraction is frequently the actual cause of the heat.

## CMMS route vs. condition-based monitoring (CBM) route

A **CMMS route** (as used here) is the fixed-interval checklist of lubrication, filter, belt, and cleaning tasks the worker executes on schedule. **CBM** is condition-triggered monitoring (vibration, oil analysis, thermal survey) that decides service timing from measured data rather than a calendar — that's the mechanic's or reliability tech's instrumented layer, feeding a different, threshold-triggered work queue.

*Practitioner usage:* "My route is calendar-and-duty-cycle based; if this point needs vibration trending to catch something my checklist can't, that's a CBM add-on request to the reliability tech, not something I do on the route."

*Common misuse:* assuming a basic IR-thermometer or stethoscope check on the route is equivalent to full condition-based monitoring — it catches gross deviations, not the early-stage spectral or oil-chemistry signatures CBM instruments are built to find.

## Wrench time

The percentage of a maintenance worker's paid shift actually spent doing hands-on task work, as opposed to travel between points, waiting on parts, or administrative logging. Industry studies commonly cite reactive-heavy operations in the 25–35% range versus 50%+ for well-planned, route-based work.

*Practitioner usage:* "A well-sequenced route with parts staged ahead of time gets my wrench time well above a shop that's constantly interrupted for breakdowns."

*Common misuse:* treating low wrench time as purely a worker-effort problem rather than a routing, staging, and scheduling problem the route design itself can fix.

## Deferred item vs. backlog

A **deferred item** is a single checklist finding pushed to a later, specific date with a logged reason. **Backlog** is the accumulated set of deferred items and open escalations across the whole route or facility. A healthy program has deferred items with dates and reasons; an unhealthy one has a backlog with neither.

*Practitioner usage:* "That's deferred to next Tuesday because the replacement filter's on order — it's not just sitting in the backlog with no plan."

*Common misuse:* logging something as "deferred" with no target date or reason, which is functionally indistinguishable from forgetting about it, just with better paperwork.
