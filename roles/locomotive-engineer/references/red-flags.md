# Red flags

Smell tests an engineer or a reviewer catches before signing a trip report, reusing a train-handling plan, or dismissing an enforcement event. Each entry: what it usually means, the first question a veteran asks, and the data to pull before proceeding.

### Same brake-application landmark used for a train more than roughly 1.5x the length or tonnage of the norm for that symbol

**Usually means:** the landmark was sized for a reference consist, and a longer or heavier train needs more of that same distance just for the brake pipe signal to propagate to the rear car — the margin the landmark was built for has eroded.
**First question:** "What length and tonnage was this card actually built for, and what's today's consist against that?"
**Data to pull:** the timetable special instruction's reference consist (if documented), today's actual train list (length, tonnage, car count), and the last time the card was reviewed against current typical train sizes.

### PTC penalty brake application dismissed as "PTC being conservative" with no review of the signal call

**Usually means:** the enforcement threshold exists because the engineer's own reaction to the displayed authority or speed restriction was already late — the penalty application is downstream evidence, not a coincidence.
**First question:** "What was displayed, and when did I actually acknowledge or act on it, against the PTC event timestamp?"
**Data to pull:** the PTC onboard event log, the event/data recorder trace for throttle and brake position, and the signal aspect in effect at the location and time.

### A signal call correctly names the aspect but the crew's action doesn't match its authority (absolute vs. permissive)

**Usually means:** the aspect and the authority are being treated as one fact when they're independently determined — a numbered (permissive) signal at Stop and an unnumbered (absolute) signal at Stop require different actions even when the displayed aspect looks identical from a distance.
**First question:** "Was there a number plate on that signal, and does the action taken match what that specific authority permits?"
**Data to pull:** the signal's classification in the employee timetable or track chart, and the recorder/radio trace of what was called and what movement followed.

### Restricted-speed movement logged with no reference to stopping within half the range of vision

**Usually means:** restricted speed is being treated as "go slow" rather than as the specific, numeric requirement (not exceeding 20 mph, and able to stop within half the range of vision, short of a train, obstruction, or improperly lined switch) that it actually is.
**First question:** "At the speed actually run, could this train have stopped within half of what was visible at every point on the move?"
**Data to pull:** recorded speed through the restricted-speed segment and the sight-distance conditions (curvature, structures, weather) along that segment.

### Independent or dynamic brake released abruptly right at a grade transition

**Usually means:** the train's slack state is about to shift (bunched to stretched or the reverse) in one uncontrolled step, which is how a run-in or run-out damages equipment even when the resulting speed profile looks fine.
**First question:** "Was slack extended or bunched going into this transition, and was the release timed to manage that, or just to hit a speed target?"
**Data to pull:** the recorder's throttle/brake trace across the transition point, correlated against the track chart's grade profile at that milepost.

### Engineer nearing the 12-hour on-duty mark with the train still short of the terminal, and no relief point identified yet

**Usually means:** the rest-period risk wasn't flagged early enough for the dispatcher to plan a relief crew or siding, turning a routine crew change into a stopped train on short notice.
**First question:** "At current speed and remaining distance, what time do we actually reach the terminal against the 12-hour mark?"
**Data to pull:** on-duty start time, current position and speed, remaining distance to the terminal, and whether a relief point has already been requested.

### An interim release at an away-from-home terminal logged as satisfying the rest requirement despite being called back early

**Usually means:** the off-duty clock is being counted as if the interruption didn't happen, when an interrupted rest period doesn't satisfy the Hours of Service Act's undisturbed-rest requirement.
**First question:** "Was this rest period actually undisturbed for the full required duration, or was there a call before it completed?"
**Data to pull:** the timestamp of release, the timestamp of the callback, and the carrier's crew management record of the rest period logged.

### Wheel slip or slide event during a brake application, with the next application at the same location made the same way

**Usually means:** a rail-condition factor (leaves, moisture, contamination) at that specific location wasn't accounted for before repeating the same brake technique, risking a repeat or worse slide.
**First question:** "What caused the slip/slide there, and does today's application account for it, or is it identical to the one that slid?"
**Data to pull:** the wheel slip/slide event log, sanding system activation record, and any track condition reports for that milepost.

### Emergency brake application returned to normal service with no examination of the recorder trace before the next trip

**Usually means:** the assumption that a safe stop closes the question, when the trace can show whether the application was appropriately timed or a late reaction to something that should have been caught earlier.
**First question:** "What does the trace show led up to the application, not just that the train stopped safely?"
**Data to pull:** the full event recorder trace for the minutes preceding the application, and the signal/speed authority in effect at the time.

### Dynamic brake relied on through an extended descending grade with no reference to thermal or grid limits

**Usually means:** dynamic braking capacity is being treated as unlimited, when sustained heavy use on a long grade can fade or reach a control system limit, at which point air brake application becomes the only remaining retarding force.
**First question:** "What's this grade's length and the locomotive consist's rated dynamic brake duration against it, and is there an air brake plan if dynamics fade?"
**Data to pull:** the grade profile and length from the track chart, the locomotive consist's dynamic brake rating, and any carrier guidance on combined dynamic/air use for that specific grade.
