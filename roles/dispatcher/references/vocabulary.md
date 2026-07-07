# Dispatcher — Vocabulary

### CAD (Computer-Aided Dispatch)
The software system showing live driver/technician locations, job queue, and status — the dispatcher's primary working interface.
**In use:** "Pull up the CAD board and check who's actually closest, not who the system defaulted to."
**Common misuse:** Treating CAD's suggested assignment as an instruction to execute rather than a starting point to verify against live conditions.

### Telematics
GPS/vehicle-data feed reporting real-time location, movement, and sometimes vehicle diagnostics — independent of the driver's self-reported status.
**In use:** "Telematics shows him stationary for 12 minutes even though the app still says 'en route.'"
**Common misuse:** Assuming telematics and self-reported status always agree; the gap between them is itself diagnostic information.

### ETA (Estimated Time of Arrival)
A probabilistic estimate, not a guarantee — accuracy degrades with every stop ahead of it on a multi-stop route.
**In use:** "That third-stop ETA is only as good as the first two stops staying on schedule."
**Common misuse:** Quoting a static-route-plan ETA for a later stop without adjusting for how the earlier stops are actually running.

### SLA (Service-Level Agreement)
A contracted response-time commitment to a specific customer/account, distinct from the standard service window quoted to a typical customer.
**In use:** "That's an SLA account — 2-hour response, not our normal 4-hour window."
**Common misuse:** Treating all "priority" flags as equivalent when only SLA accounts carry a contractual response-time obligation.

### Nearest-available assignment
A default dispatch heuristic assigning the closest driver by distance; a reasonable default that breaks down when distance doesn't predict realistic arrival time.
**In use:** "Nearest-available would send Tech C, but he's stuck in a job that's running long — realistically Tech B gets there first."
**Common misuse:** Applying it uncritically as a rule rather than a default to override when current job status changes the picture.

### Coverage gap
The shortfall when open jobs exceed available driver/technician capacity for a given window.
**In use:** "We've got a coverage gap of three jobs this afternoon — need to pull someone from on-call."
**Common misuse:** Trying to solve a coverage gap by re-sequencing existing assignments, which doesn't create capacity that isn't there.

### Check-in interval
The expected cadence at which a driver updates status (e.g. every 10 minutes on an active job); the threshold against which "gone quiet" is measured.
**In use:** "He's two minutes past his check-in interval with the truck stationary — that's a call, not a wait-and-see."
**Common misuse:** Treating the interval as a hard alarm threshold rather than the trigger point for escalating attention, not automatically an emergency.

### On-call / overflow roster
A secondary pool of drivers/technicians not on the regular schedule, available to absorb capacity gaps.
**In use:** "Pull someone from on-call before you start pushing today's jobs to tomorrow."
**Common misuse:** Treating on-call pulls as a free resource with no cost — repeated on-call use on the same day/shift is a staffing-level signal.

### Route sequencing
The tool-suggested order of stops for a multi-stop driver, optimized for drive-time or another objective function.
**In use:** "The sequencing tool put stop four before stop two — check whether that actually beats the original order given current traffic."
**Common misuse:** Executing the suggested sequence without checking it against live conditions the optimization didn't have when it ran.

### Welfare check
An escalation protocol triggered when a driver cannot be reached and telematics/context suggest a possible safety issue, distinct from a routine "running late" delay.
**In use:** "No answer on the direct call and he's still stationary — that's welfare-check territory now."
**Common misuse:** Conflating a driver who is simply late with one who has gone genuinely unreachable; the two require different response speeds.

### Priority stop / named-driver request
A customer-specified constraint (either urgency-based or requesting a specific technician) that overrides default distance-based assignment logic.
**In use:** "She asked for the same tech who did the last job — that's a named-driver request, not just a preference to ignore."
**Common misuse:** Treating customer driver requests as soft preferences rather than constraints the assignment logic needs to respect.

### Drive-time-minimized assignment
An optimization objective ranking candidate drivers by total fleet drive-time impact rather than single-job distance.
**In use:** "Minimizing this one job's distance isn't the same as minimizing total fleet drive-time once you account for what it does to his other stops."
**Common misuse:** Optimizing for the new job in isolation without accounting for the downstream disruption to that driver's existing schedule.
