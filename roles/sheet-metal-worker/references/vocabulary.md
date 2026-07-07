# Vocabulary

Terms generalists and adjacent trades conflate that a sheet metal worker keeps sharply separate.

## Gauge vs. pressure class

**Gauge** is the sheet steel's thickness (U.S. Standard Gauge for galvanized steel — a lower number is thicker). **Pressure class** is the system's design static-pressure rating (2", 3", 4", 6", 10" wg) that, together with the duct's longest dimension, determines the minimum gauge from the SMACNA tables.

*In use:* "It's not a 24-gauge duct because that's what we ran last job — it's 24-gauge because it's a 24-inch side at 2-inch pressure class. Bump the pressure class and we bump the gauge."

*Common misuse:* treating gauge as a fixed spec per duct size regardless of pressure class, or assuming a heavier gauge is always "safer" without checking whether the extra material and labor is buying anything the spec requires.

## Leakage class vs. seal class

**Leakage class (CL)** is the numeric ceiling on cfm-per-100-sqft leakage at a stated test pressure (Class 30 down to Class 3, lower number = tighter). **Seal class (A/B/C)** is the specification for which joint and seam types must be sealed to achieve that leakage class — A is everything, B is transverse joints and longitudinal seams, C is transverse joints only.

*In use:* "Spec calls for Class 6 at 2 inches wg — that's Seal Class A, full stop, not 'seal the seams and see how it tests.'"

*Common misuse:* treating "sealed" as a binary (sealed vs. not) rather than a joint-type-specific requirement tied to a numeric target, or assuming more sealant compensates for the wrong seal class applied to the wrong joints.

## Static pressure vs. velocity pressure vs. total pressure

**Static pressure** is the potential energy pushing air outward against the duct walls, independent of flow direction. **Velocity pressure** is the kinetic energy from air movement, a function of velocity squared. **Total pressure** is their sum, and the true measure of the fan's work at any point in the system.

*In use:* "The trunk's static pressure reading is fine, but velocity pressure at that necked section is what's driving the noise complaint — check total pressure loss across the whole run, not just the static gauge."

*Common misuse:* quoting static pressure alone as "the" pressure loss and ignoring the velocity-pressure component that a resize or restriction actually changes.

## Fire damper vs. smoke damper vs. combination fire/smoke damper

**Fire damper** (UL 555) closes on heat detection (typically a 165°F fusible link) at a fire-rated wall/floor penetration. **Smoke damper** (UL 555S, smoke-only) closes on smoke detection via an actuator tied to the fire alarm system, at a smoke barrier. **Combination fire/smoke damper** does both, required where a wall is both fire-rated and a smoke barrier.

*In use:* "That's not just a fire-rated wall on A-5 — it's flagged as a smoke barrier too, so we need the combination-rated damper, not a straight UL 555."

*Common misuse:* installing a standard fire damper at a location that's also a smoke barrier, or assuming "fire-rated" and "smoke barrier" are the same designation on the life-safety plan.

## TDC/TDF vs. Pittsburgh lock vs. snap lock

**TDC/TDF** (transverse duct connection/flange) is a roll-formed flange system joining duct sections end-to-end. **Pittsburgh lock** is a folded longitudinal corner seam, the standard for pressure-tight rectangular duct. **Snap lock** is a simpler longitudinal seam for lighter-duty, lower-pressure applications.

*In use:* "Low-pressure return, snap lock is fine on the seams; supply trunk at 3-inch wg gets Pittsburgh lock corners and TDC transverse joints — don't mix them up on the cut list."

*Common misuse:* specifying seam/joint type by habit rather than by the pressure class and leakage requirement actually governing that segment.

## Triangulation vs. parallel-line vs. radial-line development

**Triangulation** is the pattern-development method for transitions between unlike shapes (round-to-rectangular), breaking the surface into triangles to develop a true flat pattern. **Parallel-line development** is for constant-cross-section pieces (elbows, offsets). **Radial-line development** is for tapering pieces (cones, reducers) radiating from an apex.

*In use:* "It's a round-to-rectangular transition, so it's triangulated, not parallel-line — laying it out like an offset will leave the corners puckered."

*Common misuse:* using one development method for all fitting types, or skipping pattern development entirely and cutting "by eye" on a transition, which produces an approximate rather than a true developed surface.

## Duct liner vs. duct wrap

**Duct liner** is acoustic/thermal insulation installed inside the duct, in the airstream, requiring a fire-rated (UL 181) facing since it's exposed to conditioned air. **Duct wrap** is insulation applied to the exterior of the duct, out of the airstream, for thermal control only.

*In use:* "Spec calls for liner on the return for noise control near the mechanical room — that's UL 181-listed material inside the duct, not wrap on the outside."

*Common misuse:* substituting exterior wrap for interior liner (or vice versa) without checking whether the requirement was acoustic (liner) or purely thermal (wrap adequate).

## Transition vs. offset vs. elbow

**Transition** changes duct cross-sectional shape or size (round to rectangular, or one rectangular size to another) without necessarily changing direction. **Offset** shifts the duct's centerline laterally while keeping the same cross-section and general direction. **Elbow** changes direction (typically 90° or 45°) with the cross-section usually constant.

*In use:* "We don't need an elbow there, we need an offset — same duct size, just has to jog around the column, direction doesn't change."

*Common misuse:* calling any non-straight fitting "a transition" regardless of whether shape, direction, or lateral position is what's actually changing — each has a different geometry-development method and loss coefficient.

## Positive pressure duct vs. negative pressure duct

**Positive pressure duct** (supply, discharge side of the fan) is pressurized above ambient — seams and joints are stressed outward, so leakage pushes air out. **Negative pressure duct** (return, exhaust, suction side) is below ambient — leakage pulls unconditioned air in, and joint/seam orientation and sealing practice differ accordingly.

*In use:* "It's on the return side, negative pressure — seams get lapped the other direction than they would on supply, or it'll suck in ceiling air right at the joint."

*Common misuse:* applying supply-side sealing and seam-orientation habits to return/exhaust ductwork without adjusting for the reversed pressure differential.

## NC (noise criteria) vs. dB

**NC** is a single-number rating derived from a sound-pressure-level spectrum across octave bands, designed to reflect how HVAC noise is actually perceived across frequencies. Raw **dB** (or dBA) is a single sound-pressure measurement that doesn't capture the frequency shape HVAC noise complaints are usually about.

*In use:* "The space spec is NC-35, not '35 dB' — a duct system can measure under 35 dBA overall and still fail NC-35 if the noise is concentrated in the frequencies people notice most."

*Common misuse:* treating an NC target and a dB target as interchangeable numbers, or citing a dB reading as if it satisfies an NC spec.

## Equal friction method vs. velocity/static regain method

**Equal friction method** sizes duct so every run has the same friction rate (in wg per 100 ft), common for smaller low-pressure systems. **Static regain method** sizes duct so velocity decreases at each branch take-off enough that the resulting pressure regain offsets downstream friction loss, keeping static pressure roughly constant at each terminal — used on larger, higher-pressure systems.

*In use:* "This is a big medium-pressure system with a lot of branch take-offs — static regain sizing, not equal friction, or the terminals furthest out will be starved."

*Common misuse:* applying equal-friction sizing logic (same friction rate everywhere) to a system that was actually designed with static regain, leading to over- or under-sized branches relative to the design intent.
