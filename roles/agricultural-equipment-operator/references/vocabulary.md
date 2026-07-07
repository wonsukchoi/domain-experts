# Vocabulary

Terms generalists conflate or use loosely that practitioners keep sharply separate. Each: definition, how a practitioner actually uses it, and the common misuse.

### Header loss vs. separator (or threshing/tailings) loss

**Header loss** is grain that never enters the combine — shattered, dropped, or left ungathered by the header/platform. **Separator loss** (also called threshing or tailings loss) is grain that entered the machine but exited unthreshed or was blown out with the chaff. They require different fixes: header loss responds to speed, reel index, and header height; separator loss responds to cylinder/rotor speed, concave clearance, and fan settings.

**In use:** "Total loss is 3 bu/acre, but it's almost all header — separator's clean. Don't touch the rotor, slow the header down."

**Common misuse:** running a whole-machine drop-pan test, getting one combined number, and adjusting rotor/fan settings because that's the "combine setting" people think of first — without isolating which stage is actually losing grain.

### Pre-harvest loss vs. machine (harvest) loss

**Pre-harvest loss** is shatter or drop that happens before the header ever reaches the plant — weathering, wind, pod dehiscence. **Machine loss** is everything attributable to the combine's pass. A drop-pan reading behind the machine captures both; only the difference from a baseline sample taken ahead of the header is true machine loss.

**In use:** "14 seeds a square foot behind the machine, but 2 of that was already on the ground before we got there — call it 3 bu/acre machine loss, not 3.5."

**Common misuse:** reporting the raw behind-the-machine count as "combine loss" without subtracting the pre-harvest baseline, which overstates what an adjustment can actually recover.

### Field capacity vs. throughput capacity

**Field capacity** (acres/hour) is how much ground a machine covers per hour of field time — the speed × width × efficiency ÷ 8.25 number. **Throughput capacity** (bushels/hour or tons/hour) is how much material the machine's internal systems (cylinder, separator, cleaning shoe) can process before losses climb. A machine can have plenty of field capacity left while its throughput capacity is already maxed out in a high-yield field.

**In use:** "We've got field capacity to spare at this speed, but yield's up 30 bu/acre from last year — we're throughput-limited now, not speed-limited. Slowing down is a throughput fix, not a scheduling loss."

**Common misuse:** treating "the combine can go faster" (a field-capacity statement) as license to increase ground speed in a high-yield field, ignoring that throughput capacity is the actual constraint on loss.

### Singulation vs. population vs. spacing CV

**Population** is total seeds planted per acre. **Singulation** is the percentage of seeds metered and dropped one at a time (vs. skips or doubles). **Spacing CV** (coefficient of variation) measures how evenly spaced those single seeds are down the row. A planter can hit the right population with poor singulation (doubles offsetting skips) and still yield below potential because uneven spacing means some plants compete and others have excess room.

**In use:** "Population's dead on at 34,000, but singulation's only 94% and CV's at 16% — we're getting there on average with doubles covering for skips. Fix the vacuum before we call this calibrated."

**Common misuse:** checking only final population (easy to verify from a bag count) and declaring the planter calibrated, without pulling singulation and CV off the monitor.

### RTK vs. WAAS/SBAS correction

**WAAS/SBAS** is a free, satellite-based correction giving roughly 4–6 inch accuracy that can drift year to year. **RTK** (real-time kinematic) uses a fixed base station or network correction for sub-inch, repeatable accuracy that holds pass to pass and year to year — at a subscription or infrastructure cost.

**In use:** "WAAS is fine for spraying where a few inches of overlap doesn't matter, but strip-till needs RTK — we're planting into last year's RTK lines and can't afford the drift."

**Common misuse:** assuming any "GPS auto-steer" system delivers RTK-level repeatability, then being surprised when year-over-year pass alignment (critical for strip-till or controlled traffic) has drifted several inches.

### Field efficiency

The percentage of theoretical field capacity actually achieved once turns, overlap, unloading stops, and idle time are accounted for — always well below 100%, and different by operation (tillage, planting, combining) and field shape.

**In use:** "Theoretical capacity says 15 ac/hr, but this field's full of point rows — real field efficiency's closer to 65%, not the 80% we used for the big rectangular fields."

**Common misuse:** using one blanket field-efficiency number for every field and operation in a capacity worksheet, which silently over-promises how many acres a given number of days will actually cover.

### PTO entanglement vs. general machine guarding

**PTO entanglement** specifically refers to a rotating power take-off shaft catching loose clothing or a limb and wrapping it around the shaft — a distinct hazard from pinch points, crush points, or other guarded machine hazards because of how fast it escalates (a fraction of a second at operating rpm) and because standard shielding failure (a missing or degraded master shield) is the near-universal precondition.

**In use:** "That's not a general guarding issue, that's a PTO entanglement risk specifically — the master shield's the one thing standing between a loose sleeve and a fatality at 540 rpm."

**Common misuse:** lumping PTO shielding in with generic "machine guarding" maintenance priority, rather than treating a missing PTO shield as an immediate stop-work item regardless of what else is on the repair list.

### Grain engulfment vs. entrapment

**Entrapment** is being caught or partially buried in grain (e.g., legs) such that a person cannot self-extricate without assistance. **Engulfment** is complete submersion. The progression from standing on flowing grain to entrapment can take seconds; entrapment to engulfment can complete within roughly 20–25 seconds in flowing grain — the two terms mark different points on the same very short timeline, not different scenarios.

**In use:** "By the time someone yells that they're stuck, you may have seconds before entrapment becomes engulfment — that's why the observer's job is prevention, not reaction."

**Common misuse:** treating "entrapment" as the worst-case outcome to plan around, when the real planning horizon is the much shorter and more severe engulfment endpoint.

### Drop-pan loss test vs. combine loss monitor

The **loss monitor** is an in-cab sensor giving a continuous relative estimate of loss, useful for noticing a change in real time. The **drop-pan test** is a manual physical count that converts to an actual bushels/acre figure using a known area and a seed/kernel-to-bushel conversion factor. The monitor tells you loss changed; only the pan test tells you how much, in units you can put a dollar figure on.

**In use:** "Monitor's been climbing for the last hour — let's pull a pan test now instead of guessing whether that's 1 bushel or 4."

**Common misuse:** relying on the loss monitor's relative reading alone to decide whether an adjustment worked, without periodically grounding it against an actual pan count.
