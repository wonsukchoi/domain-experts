### Takt time
The pace demand requires: available production time divided by required output. It is a target rate, not a measured one.
**In use:** "This station is running 8 seconds over takt — it doesn't matter that the other five stations are fast, the line ships at this station's rate."
**Common misuse:** treating takt time as interchangeable with cycle time; takt comes from demand, cycle time comes from the process — they only match by design, not by definition.

### Cycle time
The actual measured time a station or process takes to complete one unit of work.
**In use:** "Station 3's cycle time is 71 seconds against a 67.5-second takt — that's our constraint."
**Common misuse:** quoting an average cycle time across a shift as if it represents every cycle; a widely varying cycle time with an acceptable average can still miss takt on its slow cycles.

### Line balancing
Assigning tasks to stations so every station's workload is as close as possible to takt without violating task precedence.
**In use:** "We rebalanced from four stations to three and picked up 25 points of line efficiency without touching throughput."
**Common misuse:** treating line balancing as purely a headcount-reduction exercise; its actual output is matching capacity to demand — headcount changes are a consequence, not the goal.

### Ranked Positional Weight (RPW)
A line-balancing heuristic that assigns tasks to stations in order of a task's positional weight (its own time plus the time of all tasks that must follow it), filling each station up to takt before opening the next.
**In use:** "RPW gave us a 3-station solution; largest-candidate-rule alone would have stalled at 4 because it ignores what's downstream of each task."
**Common misuse:** assuming any heuristic guarantees an optimal (minimum-station) solution — RPW is a good fast heuristic, not a proof of optimality; large or oddly constrained lines may need exact optimization.

### Theory of Constraints (TOC)
Goldratt's framework that a system's throughput is governed entirely by its single tightest constraint (the bottleneck); the five focusing steps are identify, exploit, subordinate, elevate, repeat.
**In use:** "We exploited the bottleneck by removing its lunch-relief gap before spending capital on elevating it with a second machine."
**Common misuse:** applying TOC once and stopping — "repeat" is in the name because relieving one constraint reveals the next one, and skipping the re-identification step is the most common way an improvement stalls without anyone noticing.

### Standard time
The time a qualified, correctly rated worker should take to complete a task under specified conditions, including allowances — not the fastest or average time observed.
**In use:** "The standard is 48.5 seconds; that's rated time plus a 15% PFD allowance, not the raw stopwatch average."
**Common misuse:** using a raw, unrated stopwatch average as "the standard" — this silently assumes the observed operator worked at exactly normal pace, which is rarely checked and rarely true.

### PFD allowance
Personal, fatigue, and delay allowance — a percentage added to rated time to account for unavoidable non-productive time (bathroom breaks, physical fatigue recovery, minor unavoidable stoppages).
**In use:** "We used a 15% PFD allowance — 5% personal, 4% fatigue, 6% unavoidable delay — appropriate for light standing assembly."
**Common misuse:** applying a single generic allowance (e.g., a flat 10-15%) to every task regardless of physical demand; heavy lifting or awkward-posture tasks warrant a higher fatigue component, and using a generic number understates the real requirement.

### MTM (Methods-Time Measurement)
A predetermined time system that assigns standard times to basic human motions (reach, grasp, move, position) so a labor standard can be built before a task physically exists to observe.
**In use:** "We used MTM-1 to time the new fixture design before build, since there's no line yet to run a stopwatch study on."
**Common misuse:** treating MTM values as universally exact rather than as validated averages for normal-paced, well-practiced motion — a novel or awkward motion pattern still needs practitioner judgment to apply the right predetermined elements.

### Learning curve (Wright's Law)
The empirical pattern that unit labor hours decline by a consistent percentage each time cumulative production volume doubles.
**In use:** "We're planning to an 85% learning curve on this new assembly — day-one labor hours aren't the steady-state number."
**Common misuse:** quoting first-week or first-month labor hours as the ongoing standard, which overstates program labor cost for its entire life; equally wrong is assuming the curve continues indefinitely rather than flattening once workers reach practical proficiency.

### OEE (Overall Equipment Effectiveness)
Availability × Performance × Quality — a single composite metric for how much of a machine or line's theoretical capacity is actually realized as good output.
**In use:** "OEE is 82% — availability is fine at 90%, the gap is in performance, so look at minor stops and speed losses, not planned downtime."
**Common misuse:** treating a low OEE number as inherently a "speed" problem; the three components have different root causes and different fixes, and diagnosing the wrong one wastes the improvement cycle.

### SMED (Single-Minute Exchange of Die)
Shingo's methodology for reducing changeover time, primarily by converting internal steps (require the line stopped) to external steps (can happen while the line still runs).
**In use:** "We didn't make anyone move faster — we just pre-staged the fixture externally and cut 17 minutes off the changeover."
**Common misuse:** assuming SMED means "work faster during changeover"; its highest-leverage lever is sequencing (internal-to-external conversion), not speed of execution.

### Systematic Layout Planning (SLP)
A structured method for facility layout using a relationship chart (closeness ratings between department pairs: A/E/I/O/U/X) to score candidate layouts before committing to a floor plan.
**In use:** "The relationship chart flagged paint and QA as an 'I' — important but not critical — so we didn't need to co-locate them at the cost of shipping access."
**Common misuse:** designing a layout from intuition about which departments "obviously" belong near each other, which works for small facilities but silently degrades as department count grows past what one person can hold in their head.

### Value stream mapping (VSM)
Mapping a process end-to-end with both value-added (touch) time and non-value-added (wait, motion, inventory) time made visible, to find where the waste actually lives.
**In use:** "The VSM showed 30% touch time and 70% wait time — the redesign target isn't the operators, it's the queue between stations."
**Common misuse:** mapping only process/cycle times without separating value-added from non-value-added time, which produces an accurate map that still hides the actual opportunity.

### Gemba
The actual place where the work happens — the floor, not the office or the dashboard.
**In use:** "Before we touch the balance, we're walking the line — the WIP count in the ERP report doesn't say why operators are waiting."
**Common misuse:** treating a gemba walk as a courtesy or a formality before "the real analysis" in the spreadsheet, rather than as the primary data-collection step it is.

### Five focusing steps
TOC's improvement sequence: identify the constraint, exploit it (get more from it without spending capital), subordinate everything else to that decision, elevate it (spend capital if still needed), then repeat from the start.
**In use:** "We're only at 'exploit' — before buying a second machine, we removed the constraint's scheduled lunch overlap and picked up 6% capacity for free."
**Common misuse:** jumping straight to "elevate" (buy more capacity) without exhausting the free or cheap exploit-and-subordinate steps first.
