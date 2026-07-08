# Vocabulary

### DR (Direct/Reverse)
A pair of angle observations to the same target, one with the telescope in Direct (Face I) position and one in Reverse (Face II, transited 180°), averaged to cancel instrument-specific systematic errors and to check for a pointing blunder.
**In use:** "That angle's only got a single-face shot on it — put a DR pair on it before we call this a control point."
**Common misuse:** treating "DR" as just repeating the same-face shot twice, which cancels nothing and provides no real check.

### PDOP (Positional Dilution of Precision)
A unitless number describing how much satellite geometry at a moment in time amplifies GNSS positioning error — lower is better; it degrades under sky obstruction or when visible satellites cluster in part of the sky rather than spreading out.
**In use:** "PDOP's sitting at 6 under that tree line — let's move the rod before we log this shot."
**Common misuse:** ignoring PDOP entirely once the receiver shows "fixed," as if fix type alone certified the shot's quality.

### Fixed vs. float solution
The GNSS receiver's report of whether it has resolved the integer carrier-phase ambiguity (fixed, centimeter-level) or is still working with a real-valued estimate of it (float, decimeter-level or worse) — a status flag, not a precision guarantee on its own.
**In use:** "It went fixed after twelve minutes near the tree line, but check the PDOP before logging — fixed doesn't mean flawless."
**Common misuse:** treating "fixed" as synonymous with "accurate enough," without checking the PDOP, baseline length, or epoch count behind it.

### HI (Height of Instrument)
In leveling, the elevation of the instrument's line of sight (backsight elevation + backsight reading); in a total station setup, the vertical distance from the ground point to the instrument's trunnion axis.
**In use:** "HI for this setup is 484.29 — carry that forward to reduce the foresight."
**Common misuse:** confusing the leveling HI (a computed elevation) with the total-station instrument height (a measured field distance) — they're different quantities that happen to share an abbreviation.

### Turning point (TP)
A temporary, stable point used to carry a level run forward when the backsight and foresight can't both be read from a single instrument setup — the point itself isn't a permanent monument, only a momentary pivot in the elevation chain.
**In use:** "Set the turning point on that rebar, not the loose gravel — it needs to hold still until both readings are done."
**Common misuse:** using an unstable or movable object (a wood stake, loose rock) as a turning point, letting it shift between the foresight and the next setup's backsight.

### Backsight / foresight
In leveling, the rod reading taken toward a point of known or previously determined elevation (backsight) versus toward the point whose elevation is being determined (foresight); in a total station traverse, the backsight is the reference direction the instrument is oriented to before turning an angle to the foresight.
**In use:** "Backsight's 5.812 on the benchmark, foresight's 4.230 on TP-2 — that gives us the new HI."
**Common misuse:** using the terms interchangeably as if they just meant "first reading" and "second reading," losing the directional/reference meaning that makes the reduction correct.

### Benchmark (BM) / temporary benchmark (TBM)
A benchmark is a permanently monumented point with a published, trusted elevation (often NGS or a local agency); a TBM is a temporary point the crew establishes on-site, tied to a benchmark by a level run, for repeated use during a project.
**In use:** "Tie the TBM to BM-4 with a closed loop before the crew starts using it for daily grade checks."
**Common misuse:** treating a TBM as if it carried the same authority as a published benchmark, without documenting the tie-in run that gives it any trustworthy elevation at all.

### Link traverse
A traverse that starts on one known control point and ends on a different known control point, allowing the closing coordinates to be checked against an independently published value — distinct from a loop traverse, which starts and ends at the same point and can only check internal consistency, not absolute position.
**In use:** "Run it as a link traverse between CP-1 and CP-2 so we get an actual check against published coordinates, not just a closed loop."
**Common misuse:** assuming any traverse that "closes" numerically has been checked against outside control, when a loop traverse only proves internal consistency, not correctness.

### EDM (Electronic Distance Measurement)
The total station's laser/infrared distance-measuring component; its raw reading requires an atmospheric (ppm) correction for temperature and pressure, and a prism constant offset matching the specific reflector in use, before it's a correct distance.
**In use:** "Update the EDM's ppm setting — it's still on this morning's temperature and we've picked up ten degrees since then."
**Common misuse:** assuming the EDM's displayed distance is already fully corrected regardless of the instrument's current atmospheric and prism-constant settings.

### Prism constant
A small, reflector-specific offset (often a few millimeters to several centimeters, varying by manufacturer and prism type) that must be set in the total station to correct EDM distances for that particular reflector's optical center offset.
**In use:** "We swapped to the mini-prism at lunch — did anyone update the constant, or is every shot since then off by the difference?"
**Common misuse:** assuming all prisms share the same constant, or forgetting to update the instrument setting after switching reflector types mid-day.

### Closure ratio
The relationship between a traverse's total measured length and its linear misclosure, expressed as 1:N — a measure of relative precision for that specific traverse, not an absolute accuracy statement about any single point in it.
**In use:** "1:15,200 clears the 1:10,000 classification for this job, so we're good to move off CP-2."
**Common misuse:** treating a passing closure ratio as proof the traverse is free of blunders, when a large compensating error pair can still pass a ratio check.

### Angular misclosure
The difference between the sum of a traverse's measured interior (or exterior) angles and the geometrically required sum for that figure, before any angle adjustment is applied.
**In use:** "Angular misclosure came in at 10 seconds against a 20-second allowable — distribute it and move on to linear closure."
**Common misuse:** confusing angular misclosure (a check on the angles alone) with linear misclosure (a check on the resulting coordinates), which are separate checks answering different questions.

### Party chief
The field crew lead responsible for the day's task assignment, on-site QC decisions (re-observe or accept), and the first point of escalation for evidence anomalies — a field-management role, not necessarily a licensed surveyor.
**In use:** "Flag that disturbed monument to the party chief before we do anything else at that corner."
**Common misuse:** assuming the party chief is automatically the licensed surveyor of record; the two roles often are the same person on a small crew but aren't synonymous.

### Cut/fill
In stakeout, the vertical difference between existing/staked ground and design grade at a point — "cut" means material must be removed to reach design, "fill" means material must be added — displayed live on the data collector during a robotic stakeout shot.
**In use:** "That stake's showing 0.3 cut — flag it, that's outside what the grading plan calls for at this station."
**Common misuse:** reading cut/fill as a pass/fail result on its own, without separately checking the horizontal offset — a point can be at the right elevation and badly off in plan position, or the reverse.
