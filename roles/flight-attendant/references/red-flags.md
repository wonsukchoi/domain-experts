# Red Flags — Flight Attendant

### Door reported "armed" or "disarmed" verbally, with no confirmation callout from the crossing flight attendant
- **Usually means:** the arming step was completed physically but the cross-check half of the procedure was skipped under time pressure; second most likely: the crossing flight attendant was mid-task (galley, boarding) and answered on autopilot without actually checking the mode indicator.
- **First question:** "Who confirmed the mode indicator, and what exactly did they say back?"
- **Data to pull:** cabin door status card/log, boarding-close timestamp vs. the cross-check callout timestamp if recorded, crew debrief.

### Assigned flight attendant count sits within 1 of the 121.391 computed minimum for the booked seat configuration
- **Usually means:** crew count was pulled from a typical/previous-flight number rather than recomputed for this specific seat configuration and any blocked/deactivated seats; second: a ceiling-function boundary (e.g., 150→151 seats) was missed because the seat count "felt" the same as last time.
- **First question:** "Walk me through 2 + ceil((seats−100)/50) for today's actual seat count — what did you get?"
- **Data to pull:** today's seating chart/load manifest, the crew-count worksheet, any deactivated-seat notice.

### An MEL-deferred or otherwise inoperative exit with no documented check against the certification's assumed-blocked-exit side
- **Usually means:** the MEL item was treated as a maintenance/dispatch matter only, without the cabin crew reconciling which side of the aircraft the evacuation certification assumes stays open; second: no seating restriction was applied near the inoperative exit despite reduced worst-case capacity.
- **First question:** "Which side does the certification assume stays open, and does that change with this exit down?"
- **Data to pull:** MEL entry and its cabin-safety procedure (M)/(O) conditions, the aircraft's evacuation certification exit map, current seating chart near the affected exit.

### A passenger-conduct incident reaches Tier 3 (captain notified / restraint considered) with no Tier 1 or Tier 2 report on file
- **Usually means:** the situation escalated quickly enough that documentation was skipped in the moment; second: earlier warnings were given verbally but never logged, so there's no paper trail even though the behavior was already escalating.
- **First question:** "What warnings were given before this point, and where's the written record of each one?"
- **Data to pull:** Passenger Disturbance Report (if any), crew statements with timestamps, any prior verbal-warning notes.

### Enhanced medical kit medication administered before a ground-based physician consult, for a presentation that wasn't immediately life-threatening
- **Usually means:** a flight attendant made an independent treatment call under pressure rather than waiting for or attempting consult; second: the consult service was attempted but the call didn't connect, and the decision to proceed wasn't separately justified as time-critical.
- **First question:** "What made this presentation too time-critical to wait for ground consult?"
- **Data to pull:** medical event log, consult-attempt timestamp (if any), the EMK medication administration record.

### A safety-relevant call to the flight deck made below 10,000 ft that wasn't itself safety-critical
- **Usually means:** sterile cockpit was not observed for an administrative or service matter that could have waited; second: a genuinely safety-critical item was buried in non-essential framing, making it harder for the flight deck to triage quickly.
- **First question:** "Could this specific call have waited until above 10,000 ft or out of the critical phase?"
- **Data to pull:** cockpit voice/communication log entry (if available), the item actually communicated, timing relative to takeoff/landing.

### Silent review completed in under the time it takes to actually scan this flight's exit rows
- **Usually means:** the review defaulted to a memorized generic script rather than this flight's actual seating, exit, and equipment configuration; second: turnaround time pressure compressed the review into a formality.
- **First question:** "What's different about today's exit row seating or equipment compared with your last flight on this aircraft type?"
- **Data to pull:** turnaround time available before doors-close, today's seating chart at the assigned exit, any equipment or MEL notes specific to this tail.

### AED or medical kit seal/expiration not checked and logged at the start of the trip pairing
- **Usually means:** the pre-flight equipment check was treated as a formality carried over from a previous crew's check rather than independently verified; second: the item was checked but not logged, so there's no record it happened.
- **First question:** "When was this AED/kit last independently verified, and by whom?"
- **Data to pull:** equipment check log, kit seal/expiration date, maintenance/logistics record for the tail.

### An unruly-passenger incident reaching the diversion/Tier 4 threshold with no law-enforcement handoff or FAA referral filed
- **Usually means:** the incident was resolved informally at the gate or on arrival without completing the formal referral that the behavior's severity actually warranted; second: the company treated it as a customer-service matter rather than a safety/enforcement one.
- **First question:** "Given what's documented here, why wasn't this handed to law enforcement or referred to the FAA?"
- **Data to pull:** full incident package, company security log, any correspondence about the decision not to refer.

### A passenger with a known mobility or language limitation seated adjacent to an inoperative or MEL-deferred exit
- **Usually means:** the standard exit-row screening process wasn't cross-referenced against the specific exit affected by the day's MEL item; second: the seat assignment was made before the MEL was entered and never rechecked.
- **First question:** "Was this seat assignment made before or after the MEL was logged, and was it rechecked?"
- **Data to pull:** exit-row passenger screening record, seating chart, MEL entry timestamp vs. seat-assignment timestamp.
