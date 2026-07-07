# Vocabulary

Terms generalists blur together that a control-valve tech keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## Cv vs. Cg

**Cv** is the liquid flow coefficient (Cv = Q√(SG/ΔP), incompressible flow assumption). **Cg** is the gas/vapor capacity coefficient, which accounts for compressibility and the choked-flow limit at high pressure ratios — a fundamentally different equation form, not a unit conversion of Cv.

*Practitioner usage:* "Don't back into a gas trim size using the liquid Cv formula with an average density plugged in — run the Cg equation and check whether the pressure ratio is choked before you trust the number."

*Common misuse:* using the liquid Cv sizing formula for a compressible-flow service by substituting a single "average" gas density, which silently ignores choked flow and undersizes or oversizes the trim.

## Rangeability vs. turndown

**Rangeability** is the trim's cataloged ratio of maximum to minimum controllable Cv at a fixed test ΔP — commonly 50:1 for equal-percentage trim, 30:1 for linear. **Turndown** is what's actually achievable in the installed application, where piping losses and varying ΔP always push the real number below the cataloged rangeability.

*Practitioner usage:* "The trim's rated 50:1, but with this system's ΔP swinging the way it does, we're only getting about 20:1 turndown in the field — size the control range off that, not the catalog number."

*Common misuse:* quoting the trim's cataloged rangeability as the field-achievable turndown when specifying a valve for a wide-turndown service.

## Stiction vs. backlash/deadband vs. hysteresis

**Stiction** is static friction: the valve doesn't move until the driving force exceeds the friction, then it jumps. **Backlash/deadband** is mechanical looseness — a signal reversal has to travel through slack linkage before the stem moves at all. **Hysteresis** is the broader symptom, output differing for the same input depending on direction of approach, and is usually produced by some combination of the two.

*Practitioner usage:* "The signature test shows a 6% stick-then-jump pattern — that's stiction, not backlash; backlash would show as a smooth dead zone on reversal, not a sudden jump."

*Common misuse:* lumping all three under "the valve is sticky" and jumping to a positioner retune, when the fix (packing, linkage, or tuning) depends on telling them apart.

## Positioner vs. I/P transducer

A **positioner** closes a control loop on measured stem/disc position — it compares actual position against the command signal and corrects. An **I/P transducer** just converts a 4–20 mA signal into a proportional pneumatic pressure with no position feedback; it's open-loop.

*Practitioner usage:* "This is a straight I/P, not a positioner — there's no position feedback, so a stiction problem downstream of it won't show up as an error the instrument itself can correct."

*Common misuse:* calling any actuator-mounted pneumatic device a "positioner," which implies closed-loop position correction that a plain I/P transducer doesn't provide.

## Leakage class (ANSI/FCI 70-2)

A standardized rating (Class I–VI) of allowable seat leakage rate at a specified test differential and medium — Class IV allows 0.01% of rated capacity, Class VI allows only a handful of bubbles per minute depending on seat diameter.

*Practitioner usage:* "It's spec'd Class IV for this isolation service — we don't need to chase it to bubble-tight Class VI just because the last valve on this skid leaked."

*Common misuse:* treating Class VI as simply "the good one" and specifying it by default, ignoring that tighter seats trade off actuation smoothness, debris sensitivity, and cost against a safety margin the service may not need.

## Shell test vs. seat (closure) test

The **shell test** (hydrostatic, typically 1.5× CWP) verifies the pressure-boundary integrity of the body/bonnet. The **seat test** (typically 1.1× CWP, valve closed) verifies the seat's leakage class. They test entirely different failure modes.

*Practitioner usage:* "It passed the shell test clean, but that tells us nothing about the seat — run the closure test before anyone assumes this valve won't pass flow when it's supposed to be shut."

*Common misuse:* treating a passed shell test as evidence the seat is also tight, or reporting one test result and letting it stand in for both.

## Cavitation vs. flashing

**Cavitation**: vapor bubbles form in the vena contracta and then collapse downstream as pressure recovers above vapor pressure — the collapse causes trim erosion and noise. **Flashing**: bubbles form and never collapse because downstream pressure stays below vapor pressure — no collapse damage, but choked flow and different erosion patterns (typically at the outlet, not distributed through the trim).

*Practitioner usage:* "Downstream pressure never recovers above vapor pressure here — this is flashing, not cavitation, so an anti-cavitation multi-stage trim is the wrong (and more expensive) fix; we need hardened trim rated for flashing erosion instead."

*Common misuse:* attributing any trim noise or erosion in a two-phase service to cavitation by default and specifying anti-cavitation trim, when a flashing service needs a different (and often simpler) solution.

## Fail-open (FO) vs. fail-closed (FC) vs. fail-last/fail-in-place (FL)

The action the valve takes on loss of air or signal, set by the actuator's spring/fail-safe configuration. Chosen based on which failure direction is safer for the specific process, never as a default.

*Practitioner usage:* "This is fail-open by design — on this vent service, losing air and going closed would be the dangerous direction, not the safe one."

*Common misuse:* assuming fail-closed is always the "safe" choice; for vent, relief-feed, or cooling-water services, fail-open is frequently the safety-critical direction instead.

## MAOP vs. MAWP

**MAOP** (maximum allowable operating pressure) is the PHMSA/49 CFR 192 pipeline-system term, tied to a pipeline segment's established operating limit. **MAWP** (maximum allowable working pressure) is the ASME pressure-boundary rating term for an individual vessel or valve. They can coincide numerically but come from different regulatory/design bases.

*Practitioner usage:* "The regulator's set point has to respect this segment's MAOP, but the valve body itself is only rated to its ASME MAWP — check both, they're not automatically the same number."

*Common misuse:* using the two terms interchangeably in documentation, which obscures which standard is actually governing a given limit.

## Overpressure protection vs. pressure regulation

A **regulator's** job is holding downstream pressure at setpoint during normal operation. **Overpressure protection** (relief valve, monitor regulator, or slam-shut device) is a separate, independently tested safety function for when the regulator itself fails.

*Practitioner usage:* "The regulator holding setpoint isn't overpressure protection — per 192.743 we still need the monitor or relief device tested independently, on its own schedule."

*Common misuse:* treating a working regulator as if it also satisfies the overpressure-protection requirement, without independently testing the separate protective device.

## Valve signature test vs. stroke test

A **stroke test** times full travel open-to-close (and back) against a pass/fail specification. A **valve signature test** continuously logs commanded versus actual position (and often supply pressure) through the stroke, extracting friction, stiction, and deadband values a timer alone can't show.

*Practitioner usage:* "It passed the stroke-time spec clean, but the signature test shows a 6% stiction band the timer would never catch — that's the actual problem."

*Common misuse:* running only a stroke-time pass/fail check and concluding the valve is mechanically fine, when a signature test on the same valve would reveal a stiction or backlash problem driving the process complaint.
