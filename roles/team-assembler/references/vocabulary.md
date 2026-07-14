# Vocabulary

### Takt time
The rate at which a unit must be completed to match customer demand, calculated as available production time divided by required output — the pace every station on the line has to match.
**In use:** "Takt's 45 seconds — that's not a suggestion, every station needs to land there or we're either starving downstream or building up WIP."
**Common misuse:** Confusing takt time with cycle time — takt time is the *required* pace set by demand, cycle time is the *actual* time a station takes; a station's cycle time is compared against takt time to check if it's balanced, they're not the same measurement.

### Cycle time
The actual time it takes to complete one unit of work at a specific station, measured and compared against takt time to check line balance.
**In use:** "Station 6's cycle time crept from 40 to 52 seconds — that's the number driving the imbalance, not takt time itself, which hasn't changed."
**Common misuse:** Treating a station's cycle time as fixed once established — cycle time can drift due to tooling wear, material changes, or operator fatigue, and needs ongoing monitoring, not a one-time measurement.

### Standard work
The documented, agreed-upon method for performing a task at a station — the specific sequence, timing, and technique every operator follows, serving as the comparison baseline for detecting deviations.
**In use:** "Standard work calls for the retention clip every time — skipping it isn't a faster method, it's a deviation."
**Common misuse:** Treating standard work as a suggestion that can be improved on individually in the moment — an undocumented "better" method removes the baseline that lets anyone (including the operator) detect when something's actually gone wrong.

### Andon (stop-the-line)
A visual/physical signal system (a cord, button, or light) allowing any worker to alert the team or halt production when a defect, safety issue, or abnormality is detected.
**In use:** "Pulled andon the moment I saw the part was off — didn't wait to see if it was actually a problem first."
**Common misuse:** Treating andon as a last resort reserved for certain or severe problems — the system is designed to be pulled on suspicion, not certainty, since the cost of a false alarm is far lower than the cost of a defect that continues downstream because someone waited for certainty.

### Line balance
The state where every station's cycle time is matched closely enough to takt time that work flows smoothly without starving downstream stations or building excess work-in-process upstream.
**In use:** "We're out of balance at Station 6 — that's a structural issue, not something any one operator can fix by working faster."
**Common misuse:** Treating a line-balance problem as something an individual operator should personally absorb (by working ahead or rushing) rather than a systemic issue requiring investigation and a structural fix (tooling, staffing, method change).

### Containment
The process of identifying and isolating units potentially affected by a known quality deviation, so they can be inspected or reworked before reaching the customer.
**In use:** "We know roughly which units were built during the disruption window — pulling those specific ones for containment, not guessing at the whole day's run."
**Common misuse:** Treating containment as unnecessary once the root cause is fixed going forward — units already produced during the affected window carry the risk regardless of whether the process is now corrected, and need their own separate identification and check.

### Limit sample / boundary sample
A physical reference sample representing the acceptable edge of variation for a visual or tactile quality characteristic, used to distinguish normal variation from an actual defect.
**In use:** "Compare it to the limit sample before flagging it — if it's within that range, it's normal variation, not a defect."
**Common misuse:** Flagging any visible variation as a defect without checking it against the documented acceptable range — over-flagging normal variation as if every difference is a problem erodes the credibility of real defect flags.

### Station rotation
The practice of moving workers between different stations on a line over time, rather than permanently assigning one worker to one station.
**In use:** "Rotation's not just for variety — it's how you build the sense of what 'normal' looks like at more than one station, so you can actually notice when something's off."
**Common misuse:** Treating rotation purely as a fairness or ergonomic measure without leveraging the cross-station comparison awareness it's meant to build — the safety/quality value comes from operators actively using that awareness, not just experiencing different tasks.

### Work-in-process (WIP)
Partially completed units currently between stations on the line, whose quantity indicates whether stations are balanced or one station is running ahead/behind its neighbors.
**In use:** "WIP's building up in front of Station 6 — that's the visible symptom of the cycle time problem there."
**Common misuse:** Treating a WIP buildup as a problem to solve by pushing units through faster, rather than recognizing it as a symptom pointing back to whichever station is actually out of balance.

### Root cause containment
The combination of fixing the underlying cause of a deviation going forward AND identifying/addressing units already affected before the fix was in place — treating these as two separate, both-necessary actions.
**In use:** "Fixing the tooling handles it going forward, but we still need to pull and check the units made before the fix — that's the containment half of this."
**Common misuse:** Considering an issue resolved once the forward-going fix is in place, without separately addressing units already produced under the deviated condition — the two are distinct obligations, and completing one doesn't substitute for the other.
