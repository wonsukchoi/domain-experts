# Vocabulary

Terms generalists conflate that a service unit crew keeps sharply separate. Each: definition, practitioner usage, and the common misuse.

## SICP vs. SITP

**SICP** (shut-in casing pressure) is the pressure read at the casing valve with the well shut in. **SITP** (shut-in tubing pressure) is the pressure read at the tubing valve. On a well with tubing and casing both present, they can differ substantially depending on what's communicating with what downhole — reading one and assuming it represents the other misreads the well.

*In use:* "SICP's building back to 340, SITP's holding flat at 60 — the pressure's coming from behind the casing, not up the tubing."

*Common misuse:* calling either one just "shut-in pressure" without specifying which, especially when relaying a number to someone who wasn't on location and will size a kill fluid or a stack rating off the wrong one.

## Overpull vs. pull rating (string yield)

**Overpull** is the extra force applied above a string's own weight to work it free when stuck, read directly off the weight indicator. **Pull rating** (body yield strength) is the calculated maximum tension the pipe grade and wall thickness can take before parting — a fixed number from pipe tables, not a feel.

*In use:* "We're at 18,000 lb overpull against a 22,000 lb rated limit for this string — one more increment and we call for the free-point tool instead."

*Common misuse:* treating overpull as a subjective "feels tight" versus "feels loose" judgment instead of a number tracked against the calculated rating in real time.

## Lubricate-and-bleed vs. bullhead vs. volumetric method

**Lubricate-and-bleed** pumps kill fluid in at the top and bleeds gas or fluid off at the choke in small increments, working weighted fluid down without forcing flow into the formation. **Bullhead** pumps kill fluid down at rate to force it into the formation, requiring known injectivity. The **volumetric method** controls a well by bleeding gas off in metered increments while tracking wellbore volume, used when no liquid kill fluid is readily available.

*In use:* "Injectivity's unconfirmed on this zone — we're lubricating and bleeding, not bullheading, even though it's slower."

*Common misuse:* defaulting to bullhead because it's faster without checking whether the zone will actually take fluid, which risks breaking down the formation at surface instead of controlling pressure downhole.

## Kill weight mud (KWM) vs. original mud/fluid weight

**Original fluid weight** (OMW) is the density of fluid already in the wellbore. **Kill weight mud** is the calculated density needed to balance a specific measured shut-in pressure at a specific TVD — a job-specific number, not a standard "kill weight" the lease keeps on file.

*In use:* "OMW's 8.4, but with 340 psi SICP at 6,150 ft TVD, KWM comes out to 9.46 — round up to 9.7 with trip margin."

*Common misuse:* reusing a prior job's kill weight on a different well or a different day without recalculating from that day's SICP and TVD.

## Trapped pressure vs. build-back pressure

**Trapped pressure** is pressure held in the wellbore behind a closed valve or barrier, generally static once isolated. **Build-back pressure** specifically describes pressure that returns after a bleed-down, from gas migrating up through a static fluid column and separating out at surface — it's why a single bleed-to-zero doesn't prove a dead well.

*In use:* "That's build-back, not just trapped — we bled it to zero twice already and it keeps coming back up."

*Common misuse:* using "trapped pressure" loosely to describe any nonzero reading, obscuring whether it's a one-time residual (resolves after a thorough bleed) or an ongoing migration source (needs a kill).

## Tally vs. well file depth

The **tally** is the physical, job-day measurement of joint count times joint length as pipe comes out or goes in the hole. The **well file** (or completion record) is the historical documented depth from a prior job, which may predate re-completions, tubing changes, or measurement errors.

*In use:* "File says 6,148, tally says 6,150.1 — within tolerance, going with the tally."

*Common misuse:* treating the well file as authoritative over a fresh tally, especially on older wells where undocumented workovers have changed what's actually downhole.

## Free point vs. stuck point

**Free point** is the depth a wireline tool measures as the deepest point of the string still moving (elastic stretch under tension) — everything below it is mechanically stuck. **Stuck point** is used loosely by non-specialists to mean the same thing, but a free-point survey gives an actual measured depth, not an estimate.

*In use:* "Free point came back at 4,220 ft — we back off there, not where we guessed the fill started."

*Common misuse:* estimating where a string is stuck from drag pattern or job history instead of running a free-point survey before deciding where to back off or fish from.

## Fishing vs. milling vs. sidetrack

**Fishing** recovers a stuck or parted object from the wellbore intact using specialized tools (overshot, spear, jars). **Milling** grinds away an object that can't be fished intact, using a mill to clear the bore. **Sidetrack** abandons the original wellbore path below a point and drills or completes around the obstruction — the option of last resort when fishing and milling both fail or aren't economic.

*In use:* "Overshot didn't grab it clean — we're milling the fish top before we try fishing again."

*Common misuse:* calling any downhole recovery operation "fishing" generically, which obscures which tool and cost tier is actually in play when relaying status to a company representative or engineer.

## Line of fire

The physical space where a person could be struck by moving or energized equipment — a line under tension, a swinging tong, a traveling block — if it fails or moves unexpectedly. It's a position, assessed and called out before a task starts, not a general safety attitude.

*In use:* "Get out of the line of fire on that snub line before we take up slack."

*Common misuse:* treating "line of fire" as a synonym for "be careful" rather than a specific position relative to a specific piece of loaded equipment that changes throughout a job and has to be reassessed at each step.

## BOP function test vs. pressure test

A **function test** cycles the BOP's rams and annular open and closed to confirm they operate, typically done at the start of every job. A **pressure test** applies test pressure to the closed stack to confirm it holds at its rated working pressure, done on a longer interval (often per regulation) and after certain rig-up changes. Passing one says nothing about the other.

*In use:* "We function-tested at rig-up this morning; last full pressure test was Tuesday, still within interval."

*Common misuse:* calling a function test "testing the BOP" as if it verifies pressure integrity — it verifies the rams move, not that the stack holds pressure.
