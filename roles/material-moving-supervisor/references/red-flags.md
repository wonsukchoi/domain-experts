# Red flags

Smell tests to catch on the fleet and roster before they become a missed target or an incident report.

### 1. An operator scheduled on a truck class whose 3-year OSHA evaluation date has passed with no renewal logged

**Usually means:** the certification-tracking roster is being checked reactively (after someone asks) rather than at every shift start, letting a lapsed evaluation sit unnoticed until an incident forces the question.

**First question:** "When was this operator's last logged evaluation on this specific truck class, and is a renewal already scheduled?"

**Data to pull:** the certification tracking roster/LMS record for that operator and truck class, today's shift schedule, renewal appointment status if one exists.

### 2. An operator involved in a near-miss or incident is back on the floor with no post-incident evaluation logged

**Usually means:** the standing certification's remaining validity is being treated as sufficient clearance, when the trigger event — not the calendar — is what OSHA 1910.178(l) requires an evaluation for.

**First question:** "Has this operator had a post-incident evaluation, separate from and in addition to their standing certification date?"

**Data to pull:** the incident/near-miss report, evaluation record (or its absence) since the event, date of the operator's last general certification versus date of the event.

### 3. Fleet-wide utilization tracking above ~85% for more than a few consecutive shifts

**Usually means:** the schedule has no slack for a breakdown or an overdue PM window — the next equipment failure will directly cost the shift's throughput target rather than being absorbed.

**First question:** "What happens to today's target if any one unit on this roster goes down mid-shift?"

**Data to pull:** fleet telemetry utilization report by unit and equipment class, PM schedule status for units currently in heavy use, recent unplanned-downtime incidents.

### 4. An equipment class sitting below ~40% utilization while a task backlog exists for a different class

**Usually means:** tasks are being routed to whichever machine is available rather than the class best suited to the task, wasting the idle class's capacity while another class runs hot.

**First question:** "Could any of the backlog on the busy class be reassigned to the idle class without a significant throughput penalty?"

**Data to pull:** utilization by equipment class, task backlog by type, throughput-rate comparison for the task in question across classes.

### 5. Near-miss reports have dropped sharply while damage claims or minor-incident counts stayed flat or rose

**Usually means:** near-misses are being underreported — operators have learned that reporting one draws scrutiny rather than triggering a fix, so the leading indicator has gone quiet right when the lagging numbers say it shouldn't have.

**First question:** "What changed in how near-miss reports are received or acted on in the last few months?"

**Data to pull:** near-miss report volume by month, incident/damage-claim volume over the same period, any recent change in supervision, discipline policy, or reporting process.

### 6. A shortage in one equipment class covered by reassigning its tasks to a different class with no throughput recalculation

**Usually means:** the substitution was made on availability alone, without checking whether the substitute class's slower or faster rate for that specific task type still gets the shift to its target.

**First question:** "What's this substitute class's actual measured rate for this specific task, and does the shift's capacity math still hold with it?"

**Data to pull:** WMS throughput report for both the original and substitute equipment class on this task type, recomputed shift capacity.

### 7. Multiple equipment classes sharing a blind corner or cross-aisle with no combined traffic protocol, only each class's own rule

**Usually means:** traffic rules were written per equipment type in isolation — a forklift's horn-and-look protocol and a reach truck's narrow-aisle rule don't specify what happens when both are approaching the same intersection at once.

**First question:** "What's the priority rule when this forklift and this reach truck approach this corner at the same time?"

**Data to pull:** current traffic protocol documentation by equipment class, layout of shared aisles/corners, recent near-miss reports at that location.

### 8. Certification records kept only on paper or in a decentralized file with no way to check currency mid-shift

**Usually means:** a lapse or an open trigger event can only be discovered by asking around, not by checking a single source before an assignment is made — the gap that produces red flag #1 and #2 in the first place.

**First question:** "If I needed to check every scheduled operator's certification status right now, how long would that take and who would I have to ask?"

**Data to pull:** current recordkeeping method for certifications, time-to-check estimate, any recent instance where a lapse was found after the fact rather than before.

### 9. A specific unit's idle-time (engine hours minus productive hours) rising steadily with no maintenance flag raised

**Usually means:** the unit is developing a mechanical issue that's making operators avoid it or slowing it down on tasks, and no one has connected the utilization telemetry to a maintenance conversation yet.

**First question:** "Has this unit's rising idle time been cross-checked against its maintenance log and last inspection?"

**Data to pull:** per-unit utilization/idle-time trend from fleet telemetry, maintenance log, most recent pre-shift inspection findings for that unit.

### 10. Same operator repeatedly reassigned across equipment classes without a logged class-specific evaluation for each

**Usually means:** a general certification is being treated as covering every class the operator happens to be put on, when a class-specific evaluation is required the first time an operator runs a truck type they haven't operated at this site.

**First question:** "Does this operator have a logged evaluation for every equipment class they've been assigned to this month, not just their primary one?"

**Data to pull:** assignment history for the operator across the period, certification/evaluation log by truck class.
