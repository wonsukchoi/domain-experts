# Playbook

Filled worksheets for the four recurring judgment calls: a door-obstruction sensor decision, a headway hold-vs-run recompute, an ATC-to-manual mode transition, and a tunnel unscheduled-stop communication sequence. Numbers below are stated industry-typical figures and cited standards, not a substitute for a specific agency's approved rulebook or a specific door/signal vendor's certified spec — those always control over this worksheet.

## 1. Door-obstruction sensor decision

**Why the sensor can miss an obstruction:** a sensitive-edge door system is certified to reopen when it meets resistance from a rigid test object at a stated force — commonly cited in industry practice around 15–35 lbf (65–155 N), depending on agency/vendor spec [heuristic — varies by system]. That threshold is tuned to catch a rigid obstruction (a cane, a bag, a limb) without nuisance-tripping on light contact. A soft or narrow object — a scarf, a canvas strap, a loose sleeve — presents a fraction of that resistance because it compresses or slips through the door edge rather than pushing back against it, so the door can close and hold on it without ever reaching the reopen-trigger force.

**Decision sequence at a reported obstruction:**

| Event | Action | Reasoning |
|---|---|---|
| 1st obstruction signal, door reopens automatically | Allow normal reclose cycle | Sensor did its job on a rigid-enough obstruction; routine |
| 2nd signal at the same door within one stop | Reclose once more, but start a CCTV/visual check of that door pocket in parallel | Two signals at the same location is no longer routine noise |
| Door closes with no further signal, but a passenger or bystander reports something caught | Do not accept the sensor's silence as evidence — reopen and check manually | The sensor's failure mode is exactly this: closed on something without tripping |
| 3rd recycle requested with no visual confirmation the pocket is clear | Refuse the blind third cycle; hold the train and check visually first | A third identical action against an unconfirmed cause is not a bigger safety margin, it's repeating a test that already failed twice |

**Worked example.** A door reports an obstruction at a busy station, recycles once, and closes clean on the second attempt with no further signal. As the train starts to move, a platform bystander shouts that a bag strap is caught. Naive read: the door log shows no active fault, so there's nothing to check. Expert reasoning: a canvas strap presenting roughly 5–10 lbf of resistance is well under a 15–35 lbf reopen threshold — the sensor working exactly as specified is fully consistent with a strap being caught and the door reporting nothing wrong. Stop, reopen, and visually clear the door before proceeding; the sensor's clean log is not exculpatory here, it's expected.

## 2. Headway hold-vs-run recompute

**Method, in order:**
1. Compute the current gap to the train ahead: scheduled headway − this train's delay (or + lead time if ahead of schedule).
2. Compare that gap to the line's ATP-enforced minimum train separation. If the gap is already at or below the floor, forward speed is capped regardless of dwell or throttle — shortening dwell buys nothing.
3. Compute the gap to the train behind using the same method; if it's also near the floor, the delay is about to cascade to that train independent of anything done at this stop.
4. If the floor isn't yet binding (gap comfortably above it) and the delay is small relative to headway, running at normal speed with a normal dwell is usually sufficient — don't invent a hold that isn't needed.
5. If the floor is already binding, take the dwell time actually needed for safe boarding rather than rushing it, and notify the control center early enough for them to hold the following train upstream rather than let ATP brake it in motion.

**Comparative worked example — two delay scenarios on a 240 s (4 min) scheduled headway, 105 s ATP minimum separation:**

| Quantity | Scenario A: 60 s late | Scenario B: 150 s late |
|---|---|---|
| Gap to train ahead (240 − delay) | 180 s | 90 s |
| Gap vs. 105 s floor | 75 s of margin | 15 s under the floor |
| Is forward speed already capped? | No | Yes |
| Correct dwell choice | Normal scheduled dwell; no hold needed | Full dwell needed for safe boarding, even if longer than scheduled |
| Correct control-center flag | Not urgent | Immediate — recommend holding the following train upstream |

**Decision rule:** the moment the gap to the train ahead drops to at or below the line's minimum separation, further schedule recovery by rushing dwell is not physically available — the lever that still works is upstream metering of the following train, communicated early, not a faster door cycle on this one.

## 3. ATC/ATO-to-manual mode transition

**Mode spectrum (per IEC 62290 Grade-of-Automation framing, adapted to a semi-automatic subway/streetcar context):**
- **Full ATO (system nominal):** ATP enforces safe separation and speed envelope; ATO drives to a target speed/stopping point within that envelope; operator owns doors, platform monitoring, and obstruction judgment.
- **Manual with ATP active:** operator drives, but ATP still enforces the speed envelope and will penalty-brake an overspeed or authority violation.
- **Restricted manual / ATP degraded or absent:** operator drives with no automatic speed enforcement; the agency's rulebook imposes a stated reduced speed cap (commonly well below normal ATO/ATP line speed in this mode, particularly through interlockings and curves) [heuristic — exact cap is agency-specific; confirm against the current rulebook, not a memorized number from another territory].

**Transition procedure:**
1. On any ATC/CBTC fault alarm or automatic mode-drop indication, treat the alarm itself as the trigger to check current authorized mode — don't wait for a speed problem to notice the mode changed.
2. Confirm the newly authorized mode and its associated speed restriction before the next throttle input; do not carry over the prior ATO-authorized speed.
3. Report the mode change to the control center with train ID, location, and mode, so following trains and dispatch are aware the block is now operating under reduced protection.
4. Resume higher-speed authority only on an explicit restoration confirmation from the control center or a positive on-board indication that ATP/ATO is re-established — never on the assumption that a fault "probably cleared."

## 4. Tunnel unscheduled-stop communication sequence

**Why detraining is a second hazard, not a fallback:** a subway/streetcar tunnel has no shoulder — the space beside the train is an adjacent track's clearance envelope, and on third-rail systems, an energized rail. Detraining without instruction risks a struck-by or electrical-contact event that didn't exist before the detrain decision. NFPA 130 governs tunnel egress design (cross-passage/emergency-exit spacing and full-train evacuation timing) precisely because uncontrolled self-evacuation is the failure mode being designed against, not stopping itself.

**Sequence:**
1. **0–90 seconds after an unscheduled stop:** first PA announcement to passengers, factual, even with no new information — state that the train has stopped, that the cause is being checked, and that instructions will follow. This substitutes for the decision passengers would otherwise start making on their own.
2. **Parallel:** report to the control center — exact location (nearest milepost/station reference), suspected cause if known, and whether conditions (smoke, fire, smell) require an immediate escalation.
3. **Every 2–3 minutes without resolution:** repeat the passenger announcement with whatever incremental information exists, even if it's only "still working the issue, thank you for your patience" — the interval matters more than the content.
4. **Detrain only on an explicit trigger** — visible fire/smoke, direct control-center instruction, or an official evacuation order — never as a unilateral response to passenger pressure or extended dwell time alone.
5. **After resolution:** log exact stop duration, location, cause if known, and the announcement timestamps for the incident report.
