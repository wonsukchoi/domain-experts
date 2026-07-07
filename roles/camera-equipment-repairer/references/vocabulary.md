# Vocabulary

Terms customers and junior techs conflate that a bench technician keeps sharply separate.

## Actuation count vs. rated shutter durability

**Actuation count** is the number of times a specific unit's shutter has actually fired, read from a diagnostic menu or EXIF tag. **Rated shutter durability** is the manufacturer's published cycle-life spec for that model (e.g., 150,000 for a Canon 5D Mark IV), established through the manufacturer's own durability testing, not a guarantee of failure at that exact number.

*In use:* "It's at 142,500 against a 150,000 rating — that's 95%, which is why I want to bench-test the curtain timing before we talk about a sensor clean."

**Common misuse:** treating the rated number as a hard failure point ("it's rated for 150,000, it'll die at 150,001") or, in the other direction, dismissing a high ratio because the unit "still looks new" — cycle count, not cosmetic condition, predicts shutter-mechanism failure risk.

## AF micro-adjustment (AFMA) vs. collimation

**AFMA** is an in-camera electronic offset applied to autofocus, correcting a constant front/back-focus bias measured at one reference distance. **Collimation** is the physical alignment of a lens's optical elements (and, on interchangeable-mount systems, the flange focal distance) to the mount's mechanical spec — a hardware property, not a software correction.

*In use:* "AFMA at +8 fixed it at three meters but it still misses at infinity — that's not an AFMA problem anymore, that's a collimation check."

**Common misuse:** applying AFMA to any reported focus complaint without first checking whether the offset is constant across distance; a variable offset is a mechanical fault that AFMA papers over rather than fixes.

## Flange focal distance vs. registration distance

**Flange focal distance (FFD)** is the specified distance from a lens mount's flange to the sensor/film plane for a given camera system (e.g., roughly 44mm on Canon EF, with a manufacturer tolerance typically in the ±0.01–0.03mm range). **Registration distance** is sometimes used loosely as a synonym, but properly refers to the as-built distance on a specific unit, which should match FFD within tolerance but is what's actually being measured and corrected during a repair.

*In use:* "Measured registration on this body comes in 0.04mm long — that's outside FFD tolerance, and it's why infinity focus never quite lands."

**Common misuse:** using the terms interchangeably in a way that hides which one is the spec (FFD) and which is the measured, correctable value (registration distance) on the unit in front of you.

## IS/VR unit vs. sensor-shift stabilization

**IS/VR (lens-based image stabilization / vibration reduction)** stabilizes via a floating lens element driven by gyro sensors and electromagnetic actuators inside the lens barrel. **Sensor-shift (in-body/IBIS) stabilization** achieves the same end by moving the sensor itself on a suspended stage inside the camera body. They are physically separate mechanisms with separate failure modes and separate repair procedures, even on bodies that combine both.

*In use:* "The buzzing is coming from the lens's IS group, not the body — on this combined system we still have to isolate which unit is actually engaged when the noise happens."

**Common misuse:** diagnosing "stabilization is broken" as one fault when the body has both systems active; each requires its own isolation test (power lens-only stabilization off in-menu, or vice versa) before quoting a repair.

## Dust spot vs. fungus vs. haze

**Dust spot** is discrete airborne debris on the sensor or an internal lens surface — sharp-edged, small, and removable by cleaning. **Fungus** is biological growth on internal glass surfaces, often filamentary, that can etch the lens coating permanently. **Haze** is a diffuse film (frequently oil migrated from aperture-blade grease, or general internal fogging) that softens contrast across the whole frame rather than producing discrete spots.

*In use:* "That's not dust, the branching pattern under the loupe is fungus — cleaning removes the growth but the coating's still etched underneath, so quote it as a partial-improvement job, not a full fix."

**Common misuse:** calling any internal-lens defect "dust" regardless of appearance, which leads to under-quoting a fungus or haze job as a simple cleaning when it may require element replacement or coating repair.

## Donor part vs. NOS vs. aftermarket

**Donor part** is a component pulled from a non-functional unit of the same model, with its own unknown wear history. **NOS (new old stock)** is unused factory-original inventory of a discontinued part, still in original condition despite its age. **Aftermarket** is a third-party-manufactured replacement, not made by the OEM, of variable and sometimes untested quality.

*In use:* "OEM stock is gone — I found NOS shutter units through a parts distributor, which I'd trust over a donor pull with unknown cycle count."

**Common misuse:** representing any non-OEM-current-stock part as equivalent to new without disclosing which category it falls into — a donor part's actuation history matters as much as the customer's own unit's did.

## Curtain travel time vs. shutter lag vs. flash sync speed

**Curtain travel time** is how long the first or second shutter curtain takes to physically cross the frame, measured on a timing rig against factory spec. **Shutter lag** is the delay between the shutter-release press and the exposure actually starting, a separate electronic/mechanical response-time property. **Flash sync speed** is the fastest shutter speed at which both curtains are ever fully open at once, a property that changes if curtain travel time drifts from spec.

*In use:* "Second-curtain travel is 1.8ms off spec — that's also why sync speed crept down from 1/250s to something the flash system won't reliably hit."

**Common misuse:** treating a "the flash won't sync" complaint as a flash-unit problem before checking whether curtain-timing drift on the camera body is the actual cause.

## Economic total loss (repair-vs-replace threshold)

The point at which a repair's cost, relative to the equipment's current used-market value at its actuation/wear state, no longer makes financial sense for a given customer's use case — a threshold that shifts by context (casual owner vs. working professional with sunk workflow costs), not a fixed percentage.

*In use:* "At 51% of used value this is right on the line — for a hobbyist I'd call it total loss, but for a working pro who needs this exact body's calibration, I'm still recommending repair."

**Common misuse:** applying a single fixed percentage rule to every customer regardless of whether the equipment has replaceable-in-minutes value (a casual body) or embedded workflow value (a professional's calibrated, matched set).

## Bathtub curve (infant mortality vs. wear-out failure)

The reliability-engineering pattern where failure rate is elevated early in a component's life (infant mortality — manufacturing defects), flat through most of its service life, then rises again as it approaches and passes its rated wear-out point. Applied to shutters, this is why a unit failing at 5,000 actuations and one failing at 145,000 actuations point to different root causes even though both "failed."

*In use:* "This shutter failed at 8,000 cycles — that's infant mortality territory, worth escalating as a possible defective unit, not wear."

**Common misuse:** assuming any shutter failure is simply "wear," which misses early-failure cases that may indicate a manufacturing defect (and a warranty claim) rather than end-of-life degradation.
