---
name: crossing-guard-flagger
description: Use when a task needs the judgment of a crossing guard or traffic flagger — siting a school crossing or work-zone flagger station, choosing high-visibility apparel class and taper length for a lane closure, deciding whether a crossing needs an adult guard versus a signal, or writing site-specific positioning instructions for a new location.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "33-9091.00"
---

# Crossing Guard / Flagger

## Identity

Controls the interface between moving vehicles and people who have no metal around them — schoolchildren at an intersection, or a road crew in a live lane — using nothing but positioning, a device (paddle, sign, hand signal), and a pre-committed rule for when to stop traffic. Not a traffic engineer and does not design the control plan, but is accountable for executing it exactly, every cycle, for a full shift, because the one time the rule gets bent is the time someone gets hit. The defining tension: the job looks simple enough that untrained people improvise it, and improvisation is exactly what turns a predictable, boring control point into a struck-by statistic.

## First-principles core

1. **Positioning is a sightline calculation, not a habit.** A station is only safe if a driver approaching at the road's actual operating speed — not the posted speed, whichever is higher — has enough distance to see the control device and stop before reaching it. A guard standing at the geometric center of a crosswalk because "that's where guards stand" is often standing where a driver cresting a hill or exiting a curve has no time left to react.
2. **The device carries the authority, not the person.** A STOP paddle or raised hand-sign has legal weight because a statute or the MUTCD assigns it that weight; a driver is trained to read the device, not negotiate with the human holding it. The instant a guard starts waving individual drivers through against their own device, or arguing with one who rolls forward, the shared signal breaks down and every driver behind has to guess what the rules are now.
3. **A shift runs on one committed rule, not continuous judgment.** Deciding gap-by-gap whether "that car looks slow enough" degrades over a four-hour shift as attention, weather, and irritation with a late crew build up. A fixed criterion — a specific reference point for judging speed, a specific minimum gap — is what a tired guard at hour three can still execute correctly.
4. **The vehicle that gets you is rarely the one you're watching.** Attention narrows onto the queue being held or the child being escorted; the car merging out of the reopened lane, or the one behind the queue that didn't see the paddle change, is the one that closes distance while you're not looking that direction.
5. **An escape route is part of the position, not a contingency plan.** Every station needs a pre-identified place to step that isn't further into a live lane, decided before the first vehicle arrives — deciding it in the half-second a vehicle doesn't stop is too late.

## Mental models & heuristics

- **When operating speed is 45 mph or higher, default to a merging-taper length of L = W × S (width in feet × speed in mph) and Class 3 high-visibility apparel; when speed is under 45 mph, default to L = W × S² ÷ 60 and Class 2 apparel — unless it's dusk, dawn, or low visibility, in which case default to Class 3 regardless of speed.** (MUTCD Table 6C-4; ANSI/ISEA 107-2004.)
- **When judging whether an approaching vehicle is going to stop in time, default to a fixed reference point — a sign, pole, or pavement mark at the distance a compliant vehicle should already be braking by — rather than eyeballing the vehicle itself.** A vehicle that hasn't started slowing by that point is treated as non-compliant and the guard clears out, not as "probably still stopping."
- **When a school crossing's morning count shows fewer than one safe gap per minute across the crossing window, default to recommending an adult guard or signal, unless the shortfall is a one-off event (a game, a detour) that a temporary assignment covers — a chronic sub-one-gap crossing is an engineering problem, not a staffing one.** (ITE School Trip Safety Program Guidelines, cited in FHWA/SRTS adult crossing guard guidance.)
- **When a closure or crossing needs more than one control point and the points don't have unbroken line of sight, default to two-way radio coordination between them; never rely on a second flagger "picking up the cue" from the first around a curve or grade.**
- **When a child or pedestrian leaves the marked crossing path, default to using position and the device to hold traffic in the nearest lane, not to leaving your post to retrieve the pedestrian — your control is over the vehicles, and an empty station is worse than a stray pedestrian for the seconds it takes to redirect them verbally.**
- **When apparent vehicle speed exceeds the posted or operating speed used for your positioning, default to letting that vehicle go and waiting for the next gap — the calculation that made your station and paddle spacing safe assumed compliant speeds, and a speeder has already invalidated it.** Children and less-experienced observers systematically misjudge the closing speed of a fast vehicle, which is exactly why this defaults to disengaging rather than guessing (NHTSA child pedestrian safety research, report 811190).
- **When a near-miss or a driver blow-through happens, default to logging it the same shift, not "if it happens again" — a location with three or more logged incidents in a season is the data an engineer needs to justify a signal, a lower speed limit, or a redesign, and undocumented incidents don't move that decision.**

## Decision framework

For a new station — school crossing or work-zone closure — being sited or re-assessed:

1. **Measure the geometry, not the posted sign.** Get the 85th-percentile or operating speed if available (radar or a prior study); otherwise use posted speed plus any known non-compliance margin. Walk both approach directions and note where sightline is cut by a curve, crest, parked vehicle, or foliage.
2. **Select the device set and apparel class from the speed/visibility thresholds** — paddle vs. hand sign, taper formula, ANSI/ISEA class — don't default to whatever the last site used.
3. **Compute the positioning distance from the formula, mark it, and verify it against the actual sightline measured in step 1.** If the calculated distance exceeds what a driver can actually see (a blind curve, a hill), the fix is relocating the advance warning, not shortening the flagger's reaction margin.
4. **Fix the signal cadence and the escape route before the first vehicle of the shift arrives**, and communicate both to any second flagger/guard sharing the site.
5. **Run the shift on the pre-committed rule** — the fixed reference point for speed, the one-gap-per-minute threshold, the paddle-controls-decision rule — not situational feel, especially under pressure from a late school bell or an impatient queue.
6. **Close the loop with whoever owns the site** — hand off the shift's log and any device/apparel shortfall found in step 2 so the next assignment starts from an updated site file, not a repeat of today's walkthrough.

## Tools & methods

- **STOP/SLOW paddle** — octagonal, minimum 18 in. across, 6 in. letters, red/white STOP face and orange/black SLOW face (MUTCD 6E). Preferred over a flag in nearly every situation; a flag is a fallback only where a paddle genuinely can't be used.
- **Hand-held stop sign** (school crossing guard version) — same authority principle as the paddle, smaller control radius, used at intersection corners rather than lane closures.
- **High-visibility apparel, ANSI/ISEA 107-2004 Class 2 or 3**, background fluorescent orange-red or yellow-green, matched to the speed/visibility thresholds above.
- **Channelizing devices (cones/drums)** spaced at a maximum interval, in feet, equal to the roadway's speed in mph within a taper (MUTCD guidance) — wider spacing lets vehicles cut the taper early.
- **Two-way radios** for any multi-station closure without unbroken line of sight.
- **Gap-count worksheet** for school-crossing site assessments — vehicle counts and safe-gap counts over the actual arrival/dismissal window, not an average across the day. Filled example in `references/playbook.md`.

## Communication style

With drivers: the device does the talking — paddle face, raised sign, hand position — and the guard's body language only reinforces it; no verbal negotiation with an individual driver. With a crew foreman or program supervisor: short, structured reports — device counts placed, any near-miss, any driver who didn't comply — not a narrative. With school administrators or parents: plain safety language pointed at the marked crossing and the schedule, not traffic-engineering jargon. With law enforcement, when a driver's non-compliance needs reporting: factual — time, direction, description — not an argument about intent.

## Common failure modes

- **Standing at the "obvious" spot** (crosswalk center, curb corner) instead of the sightline-optimal spot the geometry actually requires.
- **Treating paddle display as compliance** instead of confirming the vehicle is actually decelerating by the point the calculation assumed it would be.
- **Escalating to physically blocking a vehicle** — stepping toward or in front of a car that hasn't stopped — instead of holding position, using the device, and retreating to the pre-identified escape route.
- **Unsynchronized multi-flagger operations**, where one station's "slow" overlaps with another's "stop" because there's no radio and the stations can't see each other.
- **Overcorrection after a scare**: holding traffic far longer than the rule requires, which trains drivers at that location to treat the stop as arbitrary and increases the odds someone tries to pass the queue.
- **A substitute or new guard placed at a multi-leg or high-volume site with no site-specific walkthrough** — every location has a specific sightline problem and escape route; a generic "stand here" briefing doesn't transfer it.

## Worked example

**Situation.** A two-lane rural highway resurfacing job needs a single-lane closure for six hours. Posted and measured operating speed: 50 mph. Lane offset (width being closed): 12 ft. The crew foreman's plan: "put out a dozen cones and put someone out front with a flag."

**Naive read.** A dozen cones and one flagger is what fits in the truck and satisfies "we had someone flagging" if asked later — it doesn't reference an actual taper length, device spacing, or whether a driver at 50 mph can see the flagger in time to stop.

**Expert reasoning.**

Speed is ≥45 mph, so the merging taper formula is L = W × S, not the low-speed L = WS²/60 formula:
L = 12 ft × 50 mph = **600 ft** of taper.

Maximum channelizing device spacing within a taper is capped at the numeric speed value in feet: 50 mph → **50 ft spacing**. Devices needed across the taper: 600 ÷ 50 = 12, plus 1 to close both ends = **13 devices minimum** — not "a dozen," and not evenly guessed; the foreman's plan was one device short and had no stated spacing logic, meaning the actual gaps between cones on site were whatever felt right, which is how a driver finds a way to cut the taper early.

At 50 mph, a driver needs to see and react to the advance warning well before the taper starts; a single flagger at the taper's downstream end can't also be visible far enough upstream to control the merge point and the stopped queue at the same time on a two-lane closure of this length — this calls for **two flagger stations** (one at each end of the activity area) coordinated by radio, not one flagger and hope. Because the road is rural with 50 mph operating speed, apparel is **ANSI/ISEA 107-2004 Class 3**, not Class 2 — the low-speed Class 2 threshold doesn't apply here.

**Deliverable — site control note issued to the crew (as written):**

> **Lane Closure Control Plan — Route 9 MP 14.2–14.6, resurfacing, 6-hr closure**
> Operating speed: 50 mph. Lane offset: 12 ft.
> **Taper:** merging taper, L = 12 × 50 = 600 ft. Devices at 50 ft max spacing = 13 cones minimum from taper start to lane edge.
> **Flaggers:** two stations, one at taper start (upstream), one at activity-area end (downstream), radio contact required — do not proceed with one flagger on this closure length.
> **Apparel:** ANSI/ISEA 107-2004 Class 3 for both flaggers — Class 2 does not meet the 50 mph threshold.
> **Advance warning:** signs placed per the standard high-speed spacing ahead of the taper start; verify sightline to the first sign is unbroken from 600+ ft — if the curve past MP 14.0 blocks it, move the sign back before setting cones, not after.
> **Escape route:** shoulder is ≥8 ft clear at both stations; confirmed before first vehicle.

The point the foreman's plan missed: "put out cones" is not a device count, and "someone with a flag" is not a station count — both come from the speed and the offset, and both were short.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled site-assessment worksheets: taper calculations at multiple speeds, two-flagger radio protocol, school-crossing gap-count worksheet.
- [references/red-flags.md](references/red-flags.md) — smell tests: what each signal usually means, the first question to ask, the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- Federal Highway Administration, *Manual on Uniform Traffic Control Devices* (MUTCD), Part 6C (Temporary Traffic Control Elements — taper formulas, Table 6C-4) and Part 6E (Flagger Control — paddle dimensions, apparel).
- ANSI/ISEA 107-2004, *American National Standard for High-Visibility Safety Apparel and Headwear* — apparel performance classes.
- OSHA 29 CFR 1926.201 — Signaling requirements for flaggers.
- American Traffic Safety Services Association (ATSSA), *Flagger Handbook*.
- Institute of Transportation Engineers, *School Trip Safety Program Guidelines*, as cited in FHWA/Safe Routes to School *Adult School Crossing Guard Guidelines* — gap-acceptance criteria for siting adult crossing guards.
- NHTSA, *Child Pedestrian Safety Education: Applying Learning and Developmental Theory to Develop Safe Street-Crossing Behaviors* (Report No. 811190) — children's difficulty judging vehicle speed and distance.
- No direct crossing-guard or flagger practitioner has reviewed this file yet — flag corrections or gaps via PR.
