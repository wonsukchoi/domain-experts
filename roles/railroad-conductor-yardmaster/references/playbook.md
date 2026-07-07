# Railroad Conductor and Yardmaster — Playbook

Filled reference sequences: block-building against set-out order, the hazmat buffer-car check, the initial terminal brake test threshold, and the shoving-movement communication protocol.

## 1. Block-building sequence (reverse of set-out order)

Work destinations in order of how far down the road they're reached; the last stop's cars get built onto the departure track first.

| Step | Action | Why |
|---|---|---|
| 1 | List every set-out point in route order, nearest first (e.g., Town A, Town B, Town C-final) | Establishes the sequence the train physically stops at |
| 2 | Confirm which classification track holds each destination's block, and the current car count per track | Starting inventory before any pull |
| 3 | Pull the **farthest** block onto the departure track first | It sits at the bottom of the build and won't be touched again |
| 4 | Pull each successive block in order, working backward toward the **nearest** set-out point | Each block added sits closer to the end the crew reaches first |
| 5 | The **nearest** block goes on last | It's the first cars off the train, reachable without moving anything else |
| 6 | Cross-check: does the plan require touching any block twice? | If yes, the order is wrong — rebuild before releasing the plan |

**Worked check (from the Train 247 example):** Town A (nearest, MP 50) → Town B (MP 120) → Town C (farthest, final, MP 200). Build order onto the departure track: Block C first, Block B second, Block A last. Set-out order at the road: Block A off first at Town A, Block B off at Town B, Block C rides to the final terminal. No block is touched more than once.

**If the plan changes mid-shift** (a hot car, a bad-order pull, a missed connection): re-run this table from the yard's current physical state — car counts and track assignments as they are right now — never patch the old switch list by hand. A patched list is how re-switching creeps back in.

## 2. Track-capacity check (car-length, not car-count)

| Item | Check | Note |
|---|---|---|
| Nominal track rating | Published car capacity for the track (e.g., "60 cars") | Assumes an average car length, commonly cited around 50–55 ft |
| Actual block composition | Sum of actual car lengths for the cars assigned to that track | Tank cars, double-stacks, and articulated equipment run meaningfully longer than the average assumption |
| Available footage | Track's rated length in feet, minus any occupied footage | The real constraint — compare against actual, not nominal, car-length sum |
| Decision | If actual sum exceeds available footage, split the block or reassign before pulling | Catching this before the pull avoids a fouled switch or a foul-time violation |

## 3. Hazmat placement and buffer-car check (49 CFR 174.85)

Run this before releasing any consist with placarded cars, and re-run it after any late add or pull.

| Step | Check | Pass criterion | If fail |
|---|---|---|---|
| 1 | Identify every placarded car in the consist and its hazard class | Each car's placard and UN number recorded in the consist | Missing/mismatched placard info → hold, correct consist before release |
| 2 | Identify PIH (Poison Inhalation Hazard) cars specifically | Flagged separately from general placarded freight | PIH cars carry a stricter separation rule than general placarded cars |
| 3 | Confirm buffer car(s) between the locomotive consist and the nearest placarded/PIH car | Non-placarded buffer car(s) present per 174.85 | Missing → reposition before release, don't depart and fix en route |
| 4 | Confirm PIH cars are not directly adjacent to each other or to other incompatible placarded commodities | Buffer car separates them | Adjacent PIH cars → reposition, treat as a hold item, not a note for later |
| 5 | Record final hazmat car positions (from engine) in the consist | Position numbers match what's physically coupled | Mismatch → this is exactly the gap a responder finds at the worst possible time — correct it now |

**Example (from the Train 247 consist):** PIH tank cars UTLX 55021 and GATX 33087 at positions 19 and 22 from the engine, in Block B. Buffer car SOO 88213 placed ahead of the first PIH car (position 18). The two PIH cars are three car-positions apart with intervening non-placarded cars — not adjacent, no additional buffer action needed between them.

## 4. Initial terminal brake test and the operative-brake threshold

| Step | Action | Threshold | If below threshold |
|---|---|---|---|
| 1 | Run the initial terminal air brake test on every car in the consist | Each car tested individually | Any car not developing brake cylinder pressure is marked defective / cut out |
| 2 | Tally operative vs. total cars | Operative % = operative cars ÷ total cars | — |
| 3 | Compare against the regulatory minimum (commonly cited at 85% operative, per 49 CFR 232.103(n) — confirm current text) | ≥85% operative | Train may depart if the defective cars will be set out at the first point capable of it; below the minimum, movement is further restricted until corrected |
| 4 | Identify which forward point can perform the set-out or repair | Route knowledge — not every stop has repair capability | Plan the set-out at the first stop that does, and restrict train speed/movement until then per the rule |
| 5 | Record the actual percentage and the specific cut-out car identifiers in the consist | — | This record is what makes the departure decision defensible if it's ever questioned |

**Worked check:** 46 cars, 4 cut out (BNSF 71144, BNSF 71209, BNSF 71390 in Block A, plus one in Block B) = 42 operative ÷ 46 = 91.3%. Above the 85% minimum — legal to depart, with the 4 defective cars set out at Town A, the first stop, which also happens to be Block A's own set-out point.

## 5. Shoving-movement communication protocol

| Step | Action | Rule |
|---|---|---|
| 1 | Before the move, job-brief point protection method: radio, direct sightline, or hand/lantern signal | Method must be agreed before the first car moves |
| 2 | During the move, point person calls remaining car count continuously ("that's three cars... that's two cars to go...") | Continuous, not just a starting count |
| 3 | On loss of radio or visual contact at any point, stop the movement immediately | No "finish the move and check" — stop is the default, not an option |
| 4 | Re-establish contact and re-brief before resuming, including confirming the current car count and any change in conditions | Resuming on the old assumption is exactly where a coupling error happens |
| 5 | On any unexpected condition (obstruction, unexpected occupied track, blue-signal protection discovered) | Stop, verify, re-brief — the same discipline as a communication loss |
