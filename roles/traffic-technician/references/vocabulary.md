# Vocabulary

Terms generalists blur together that a traffic technician keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## Yellow change interval vs. all-red clearance interval

The **yellow change interval** is the perception-reaction-plus-braking time a driver needs to stop safely before the stop line, or safely clear it if too close to stop (Y = t + v/(2a+64.4G)). The **all-red clearance interval** is the separate time needed for a vehicle that entered on yellow to physically clear the conflict zone before the opposing phase gets green (AR = (W+L)/v) — a different physical event with a different formula.

*Practitioner usage:* "The yellow's fine at 3.5 seconds — it's the all-red that's undersized for this intersection's width, and that's two different numbers with two different fixes."

*Common misuse:* treating "the yellow's too short" as the default diagnosis for red-light-running or angle crashes when the actual deficit is almost always in the all-red, which most drivers never consciously notice.

## Warrant vs. justification

A **warrant** is a specific, numbered MUTCD Chapter 4C test (volume, pedestrian, crash-experience, etc.) with a documented pass/fail threshold. **Justification** is the broader engineering case for installing a signal, which requires meeting at least one warrant but also weighs alternatives — a met warrant is necessary, not automatically sufficient.

*Practitioner usage:* "It meets Warrant 1B on the count, but before we call it justified, check whether a roundabout or turn restriction handles the same crash pattern without adding a stop."

*Common misuse:* saying "the intersection warrants a signal" as a synonym for "a signal would help," when a warrant is a specific numbered test with a pass/fail result, not a general judgment call.

## Offset vs. cycle length

**Cycle length** is the total time for one complete sequence of phases at a single signal. **Offset** is the time difference between a reference point (usually start-of-green) at one signal and the same reference point at an adjacent coordinated signal, set to produce a progression band.

*Practitioner usage:* "Cycle length's fine at 90 seconds corridor-wide — it's the offset into signal 5 that's off by almost a full second since we trimmed signal 4's split."

*Common misuse:* changing a signal's cycle length to "fix" a coordination problem when the actual defect is a mis-set offset between two signals sharing the same cycle length.

## Green wave / progression band vs. bandwidth

The **green wave** (progression band) is the time window in which a vehicle traveling at the design progression speed hits consecutive green lights down a corridor. **Bandwidth** is the width (in seconds) of that window — how much timing slack exists before a vehicle at the edge of the platoon starts hitting red.

*Practitioner usage:* "We widened the bandwidth from 12 to 18 seconds on the northbound approach, so a platoon that starts a couple seconds late off the upstream signal still makes every green."

*Common misuse:* using "green wave" to describe any signal timing generally, rather than the specific progression band produced by coordinated offsets at a chosen design speed.

## Walk interval vs. pedestrian clearance interval

The **WALK interval** is the steady "walking person" display, minimum 7 seconds, during which a pedestrian is invited to start crossing. The **pedestrian clearance interval** (flashing "DON'T WALK"/upraised-hand countdown) is the separate time computed from crossing distance ÷ walking speed, during which a pedestrian already in the crosswalk finishes crossing — no new pedestrians should start during it.

*Practitioner usage:* "The countdown timer people see is the clearance interval, not the WALK interval — don't shorten it thinking you're just trimming 'the walk time,' you're cutting into the time someone already crossing needs to finish."

*Common misuse:* referring to the whole pedestrian phase as "the walk time" and trimming the flashing countdown portion to save cycle time, without checking it against the crossing-distance/walking-speed floor.

## Accessible pedestrian signal (APS) vs. pedestrian push button

A **pedestrian push button** simply calls the pedestrian phase. An **accessible pedestrian signal (APS)** adds audible and vibrotactile indication of the WALK interval, locator tone, and often directional guidance — a PROWAG-required feature at new or reconstructed signals, not an optional upgrade to a plain push button.

*Practitioner usage:* "This intersection got reconstructed last year, so it needed APS, not just a new push button — that's a PROWAG trigger, not a nice-to-have."

*Common misuse:* treating any pedestrian button as functionally equivalent to an APS, or assuming a plain push-button replacement satisfies an accessibility requirement triggered by reconstruction.

## Degree of saturation (v/c ratio) vs. level of service (LOS)

The **degree of saturation** (v/c) is a direct ratio of demand volume to capacity for a lane group in a given cycle. **Level of service (LOS)** is a lettered grade (A–F) derived mainly from average control delay per vehicle, which correlates with v/c but isn't the same measurement — two approaches can share a v/c ratio and land in different LOS grades depending on cycle length and progression quality.

*Practitioner usage:* "The v/c is only 0.72, comfortably under capacity, but LOS still comes out D because the cycle length is long and this approach doesn't get progression — the delay's structural, not a volume problem."

*Common misuse:* assuming a good v/c ratio guarantees a good LOS letter grade, when delay (and therefore LOS) depends heavily on cycle length and coordination quality independent of raw capacity.

## Pretimed (fixed-time) vs. actuated control

**Pretimed** control runs a fixed cycle, split, and phase sequence regardless of real-time demand. **Actuated** control uses detection to extend, skip, or terminate phases based on real-time calls and gaps, within programmed minimum/maximum and gap/passage parameters.

*Practitioner usage:* "This is fully actuated on the side street — if the detector's down, the minor phase never gets a call, and it'll look like a pretimed no-service problem when it's actually a bad loop."

*Common misuse:* diagnosing an actuated signal's phase-skipping behavior as a "broken" or "stuck" signal, without checking whether it's the actuated logic correctly responding to a detector fault or a genuine lack of demand.

## Critical lane group / critical flow ratio (Y)

The **critical lane group** for a phase is the movement with the highest volume-to-saturation-flow ratio among the movements sharing that phase — it, not the average, sets the phase's required green time. **Y** (critical flow ratio) is that ratio, and the sum of Y across all phases (ΣY) drives the Webster cycle-length calculation.

*Practitioner usage:* "The left-turn lane is the critical movement on this phase, not the through lanes — size the split off its Y, or the through movement will look fine while the left-turn queue spills back."

*Common misuse:* sizing a phase's green time off the average or the through-movement volume instead of identifying which specific lane group within that phase is actually critical.

## 85th-percentile speed vs. posted speed limit

The **85th-percentile speed** is the speed at or below which 85% of free-flowing traffic travels, measured directly by a spot-speed study — the value that belongs in clearance-interval and warrant calculations. The **posted speed limit** is a regulatory number that may or may not match actual observed behavior on that approach.

*Practitioner usage:* "Posted is 35, but the 85th-percentile study came back at 42 — run the clearance intervals off 42, not the sign, or you'll undersize the all-red for how people actually drive here."

*Common misuse:* plugging the posted speed limit directly into the yellow/all-red formulas without a current spot-speed study, especially on approaches where enforcement is light and actual travel speeds have drifted upward.

## Leading pedestrian interval (LPI)

An **LPI** gives pedestrians a several-second head start (typically 3–7 seconds) into the crosswalk before the concurrent vehicle phase, including permissive left/right turns, gets its green — intended to establish pedestrian presence and visibility before turning conflicts begin.

*Practitioner usage:* "We added a 5-second LPI on the north leg after the near-misses with permissive lefts — pedestrians are already established in the crosswalk by the time turning traffic gets its green."

*Common misuse:* adding an LPI as a blanket pedestrian-safety improvement everywhere without checking whether the approach even has a permissive left/right-turn conflict the LPI is meant to address, or checking that turn volumes don't create a new conflict at the LPI's own start.

## ADT vs. peak-hour volume

**ADT (average daily traffic)** is a 24-hour total, typically averaged over a representative count period, used for general planning and functional classification. **Peak-hour volume** is the count during the single highest-demand hour, the figure that actually drives signal-warrant and capacity calculations.

*Practitioner usage:* "ADT looks moderate for this road class, but the peak-hour volume is what matters for the warrant check — pull the classification count and isolate the peak hour, not the daily average."

*Common misuse:* citing ADT as evidence for or against a signal warrant or capacity concern, when the warrant and capacity thresholds are built around peak-hour (or 8-hour) volumes, not the daily average.
