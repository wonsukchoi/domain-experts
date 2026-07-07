# Vocabulary

Terms generalists conflate that an outside-plant fiber technician keeps sharply separate, because the difference changes what's actually being measured or authorized.

## Communication worker safety zone vs. NESC clearance

The **communication worker safety zone** is the specific vertical buffer (commonly 40 in for 751V–8.7kV primary distribution) reserved below the lowest power conductor on a joint-use pole, sized so a lineworker can climb or bucket through it. **NESC clearance** more broadly covers every minimum-distance rule in the code — conductor-to-ground, conductor-to-structure, phase-to-phase — of which the safety zone is one specific application to joint-use poles.

**In use:** "The pole's overall NESC clearance is fine — what I need confirmed is whether our attachment clears the 40-inch safety zone under the primary, because that's the number make-ready actually checks."

**Common misuse:** treating any general pole clearance figure as if it were the specific safety-zone distance that governs communication attachment height.

## Make-ready vs. pole attachment application

The **pole attachment application** is the request a telecom provider files with a pole owner to attach to specific poles. **Make-ready** is the survey-and-relocation work the pole owner (or existing attachers, or the applicant under one-touch make-ready) performs afterward to create space and clearance for the new attachment. Filing the application starts the clock; it does not authorize attachment.

**In use:** "The application's been in for three weeks, but make-ready hasn't been confirmed complete on six of these poles yet — we don't have permission to climb those."

**Common misuse:** treating "the application is filed" as equivalent to "we're cleared to attach," skipping the make-ready confirmation step.

## OTDR trace vs. power meter reading

An **OTDR (optical time-domain reflectometer)** sends a pulse down the fiber and reads back reflections to localize individual events (splices, connectors, breaks) and estimate their loss at specific distances. A **power meter / light source pair** measures total end-to-end insertion loss across the whole link, without localizing where along the way the loss occurred. The two answer different questions: OTDR says *where*, the power meter pair says *how much total*.

**In use:** "Power meter shows 3dB more loss than the design budget — now we OTDR it to find out which specific splice is eating the extra loss."

**Common misuse:** relying on OTDR-reported total loss as the definitive end-to-end number, when a power meter/light-source test is the more accurate measurement for total insertion loss on a finished link.

## Splice loss vs. link loss

**Splice loss** is the loss at one specific joint, in dB, as read from an OTDR event or the splicer's own estimate. **Link loss** (or total loss) is the cumulative loss across the entire fiber run — fiber attenuation plus every splice plus every connector plus any splitter — that gets compared against the transceiver's rated optical budget.

**In use:** "That one splice loss is fine at 0.04dB, but let's check whether the cumulative link loss with all five splices and the splitter still clears budget."

**Common misuse:** checking individual splice losses as pass/fail without reconciling the sum against the overall link budget.

## Fusion splice vs. mechanical splice

A **fusion splice** melts two fiber ends together with an electric arc, producing a low-loss, permanent joint (typically 0.02–0.05dB). A **mechanical splice** aligns two fiber ends inside a fixture with index-matching gel, without fusing them — faster to make in the field but higher and less consistent loss (roughly 0.3dB), and considered a temporary or emergency repair method rather than new-build practice.

**In use:** "This is a permanent build, so we're fusion splicing every joint — mechanical splices are for the emergency patch tonight, not what goes in the closure long-term."

**Common misuse:** using a mechanical splice for permanent new construction because it's faster, without accounting for its higher steady-state loss against the budget.

## Loose tube vs. tight-buffered cable

**Loose-tube cable** houses fibers inside gel- or dry-filled tubes that let the fiber move independently of the outer jacket, standard for outside-plant aerial and buried runs where temperature swings and installation stress are significant. **Tight-buffered cable** has a buffer coating bonded directly to the fiber, more flexible and easier to terminate directly, standard for indoor/premise runs, not outside-plant distances.

**In use:** "We're specifying loose-tube for the feeder run — tight-buffered wouldn't survive the thermal cycling on an aerial span this length."

**Common misuse:** specifying tight-buffered cable for a long outside-plant run because it's easier to handle at the termination end, without accounting for its poorer performance under outdoor thermal and mechanical stress.

## Feeder vs. distribution vs. drop cable

**Feeder cable** runs from the central office or headend to a distribution point (e.g., an FDH), typically the highest fiber count. **Distribution cable** runs from that point toward a neighborhood or splitter location. **Drop cable** is the final short run from a distribution point or pole tap to an individual premise. Loss-budget math treats each tier differently — feeder loss dominates by distance, drop loss is small but its connector count matters disproportionately at low overall fiber counts.

**In use:** "Feeder's already budgeted at 3dB for the 12km run — the drop's only 300 meters, but don't forget its connector pair still costs half a dB."

**Common misuse:** budgeting loss only for the long feeder run and treating short drop cables as negligible, ignoring that a drop's connector and splice loss is a fixed cost regardless of its short length.

## Insertion loss vs. return loss (reflectance)

**Insertion loss** is how much signal power is lost passing through a splice, connector, or component — measured in dB, lower is better. **Return loss (reflectance)** is how much signal reflects backward at a connector or joint instead of passing through — measured in dB, higher (more negative in some conventions) is better, since a strong reflection can degrade a transmitter's own signal or trigger false OTDR events. A connector can have acceptable insertion loss and still have poor return loss from a bad polish or air gap.

**In use:** "Insertion loss on this connector looks fine, but the return loss is high enough that it's reflecting back into the transmitter — repolish it before we accept it."

**Common misuse:** checking only insertion loss on a connector and assuming that clears it, without checking return loss separately.

## One-touch make-ready (OTMR) vs. traditional make-ready

**Traditional make-ready** requires each existing attacher on a pole to perform its own relocation work in sequence, one attacher at a time, often stretching the timeline out for months. **One-touch make-ready (OTMR)**, under the FCC's 2018 rules, lets the new attacher (or its approved contractor) perform simple, non-complex make-ready work itself in a single pass, without waiting for each existing attacher to schedule its own crew.

**In use:** "This is simple make-ready — we're self-performing under OTMR instead of waiting on three separate attachers to each send a crew."

**Common misuse:** assuming OTMR applies to every make-ready scenario, including complex work (which still requires the traditional sequenced process) or poles owned by entities not subject to the FCC's pole attachment rules.

## Overlash vs. new strand placement

**Overlashing** attaches new cable to an existing messenger strand already on the pole, using the original attachment hardware. **New strand placement** installs a new dedicated messenger strand and its own attachment point. Overlashing is faster and often exempt from a full new make-ready review, but it adds load to an attachment engineered for the original cable's weight alone.

**In use:** "We're overlashing onto the incumbent's strand here, so no new attachment point — but I still want the combined-load calculation before we hang the extra cable."

**Common misuse:** treating overlash as automatically clearance- and load-neutral just because it reuses existing hardware, without checking the strand's remaining tension capacity for the added cable.
