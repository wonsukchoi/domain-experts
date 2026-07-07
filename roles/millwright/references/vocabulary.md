# Vocabulary

Terms generalists flatten together that a millwright keeps sharply separate — the value is in the misuse, not the definition.

## Sling angle vs. included angle

**Sling angle** is measured from the horizontal plane to the sling leg. **Included angle** is the angle between the two legs of a bridle, measured at the hook. A 60° sling angle (from horizontal) corresponds to a 60° included angle only in the specific case of a symmetric 2-leg vertical bridle — for other configurations they diverge, and load-factor tables built for one don't transfer directly to the other.

**In use:** "Quote me the sling angle from horizontal, not the included angle at the hook — I'll do the load-factor math from that."

**Common misuse:** using the two interchangeably when reading a capacity chart, which silently applies the wrong load factor and can understate per-leg tension.

## Working load limit (WLL) vs. rated capacity vs. safety factor

**WLL** is the maximum load a specific piece of rigging gear (sling, shackle) is rated to lift under normal conditions, as stamped or tagged. **Rated capacity** is the same concept applied to a system (crane, hoist, lifting beam) at a given configuration (boom angle, radius). **Safety factor** (or design factor) is the ratio built into WLL between rated load and actual breaking strength — commonly 5:1 for wire rope slings — already baked into the WLL tag, not something to be re-applied on top of it.

**In use:** "The sling's WLL already has the 5:1 built in — don't derate it again on top of that unless the hitch type or angle changes the effective capacity."

**Common misuse:** stacking an extra informal safety margin on top of the tagged WLL "to be safe," which either wastes capacity unnecessarily or, worse, masks that the actual limiting factor was never checked (angle, hitch type, sling condition).

## Soft foot

A condition where a machine's mounting foot doesn't sit flush against the baseplate, so tightening its anchor bolt distorts the casing — showing up as an alignment reading that changes when bolts are torqued in a different order, or that won't hold under running conditions.

**In use:** "Foot two moved 0.004 inches on the soft-foot check — shim it before we trust any alignment number off this machine."

**Common misuse:** treating soft foot as a problem to fix by adding shims at the coupling instead of at the actual foot, which papers over a cold reading and fails once the machine reaches operating temperature.

## Offset vs. angularity (shaft alignment)

**Offset** (parallel misalignment) is the perpendicular distance between the two shaft centerlines. **Angularity** is the angle between the two shaft centerlines, expressed as mils of gap change per inch of measurement diameter. A coupling can have near-zero offset and significant angularity, or the reverse — correcting one without checking the other leaves a real misalignment uncorrected.

**In use:** "Offset's inside tolerance at 1.5 mils, but angularity's still at 0.9 — we're not done, the shim stack needs another pass on the outboard feet."

**Common misuse:** reporting "alignment's good" from a single combined-looking number without stating offset and angularity separately, which hides which correction (shim thickness vs. shim distribution) is actually needed.

## Cold check vs. hot check (alignment)

**Cold check** is an alignment reading taken with the machine at ambient temperature, before running. **Hot check** is taken at or near operating temperature, accounting for thermal growth of the casing and supports. A cold reading inside tolerance can walk outside it once the machine heats up, especially on equipment with significant temperature differential between casings.

**In use:** "Cold reading's clean, but this pump runs 180°F hotter than the motor — we need a hot check before we sign off, not just the cold one."

**Common misuse:** treating the cold check as final on equipment with meaningful thermal growth, then being surprised when a "properly aligned" machine develops a vibration signature once it reaches operating temperature.

## Backlash vs. runout vs. endplay

**Backlash** is the rotational play between meshing gear teeth or a coupling, measured tangentially. **Runout** is the radial or axial deviation of a rotating shaft or gear face from true, caused by eccentricity or a bent shaft. **Endplay** is axial (thrust-direction) float in a shaft's bearing support. All three can produce similar symptoms (noise, vibration) but require different corrections.

**In use:** "The noise isn't backlash — runout's the actual problem, it's reading 0.006 inches at the coupling face and that's eccentricity, not gear mesh."

**Common misuse:** diagnosing any drivetrain noise as "backlash" and adjusting mesh or shimming, when a runout or endplay check would have found the actual cause.

## Cure time vs. set time vs. strike-off time (grout)

**Set time** is when the grout has stiffened enough not to flow — not load-bearing. **Strike-off time** is when excess material can be trimmed/finished without disturbing the pour. **Cure time** is the full schedule to reach specified strength, with intermediate milestones (walk-on, torque-ready, alignment-ready) each tied to a different strength threshold, not one single "done" point.

**In use:** "It's past strike-off, but we're nowhere near the 72-hour mark for precision alignment — that base isn't ready for laser work yet."

**Common misuse:** treating "the grout looks solid" (set/strike-off appearance) as equivalent to reaching the strength milestone required for the next step, which is a strength threshold, not a visual one.

## Non-shrink grout vs. epoxy grout vs. cementitious grout

**Non-shrink grout** is any grout formulated to not shrink away from the baseplate as it cures — a property, not a material type. **Cementitious grout** is a non-shrink portland-cement-based product; cheaper, slower strength gain, more sensitive to water ratio and temperature. **Epoxy grout** is a resin-based non-shrink product; higher strength, better chemical/vibration resistance, faster strength gain, and roughly 3–5x the cost of cementitious.

**In use:** "Cementitious would've been fine for a static skid, but this is a high-vibration compressor base — epoxy's worth the premium."

**Common misuse:** using "non-shrink" and "epoxy" as if synonymous, which leads to specifying epoxy-only cure schedules for a cementitious pour (or vice versa) and getting the milestone timing wrong.

## Center of gravity (CG) vs. center of lift vs. pick point

**Center of gravity** is a physical property of the load — where its weight is balanced, calculated from component weights and distances. **Pick point** is the physical location(s) where rigging attaches to the load. **Center of lift** is where the crane hook sits relative to the load when picked — for a level pick, the hook must be directly above the CG, which is why pick points on an asymmetric load are chosen to put the resultant lift line through the CG, not at the load's geometric center.

**In use:** "The CG's 10 inches off the geometric center because of the overhung motor — move the pick point, don't fight it with a longer sling leg on one side."

**Common misuse:** treating "center of the skid" and "center of gravity" as the same thing, which is only true for a symmetric load.

## Shimming vs. jacking vs. chocking

**Shimming** is inserting precise thin material under a foot or coupling to correct a small, known vertical or angular offset. **Jacking** is using screw or hydraulic jacks to move or support a heavy load during rough positioning, before precision work begins. **Chocking** is wedging temporary material to hold a load's position or prevent movement, not to make a precision correction. Using one where another belongs produces either an imprecise final alignment (chocking used for fine correction) or damage/instability (shimming loads meant for jacks).

**In use:** "Jack it into rough position first, chock it there so it can't shift, and only then start shimming to the actual alignment numbers."

**Common misuse:** using shims to absorb gross positioning error that should have been corrected by jacking or re-rigging, which stacks an unstable pile of shims instead of fixing the actual position.

## Thermal growth

The dimensional change (typically expansion) a machine casing and its supports undergo between ambient and operating temperature, which shifts shaft centerline position and can move an alignment that was correct cold outside tolerance once hot, or vice versa.

**In use:** "OEM's thermal growth chart says this pump rises 4 mils at the outboard bearing once it's up to temperature — we align it 4 mils low cold on purpose."

**Common misuse:** ignoring thermal growth data and aligning purely to a cold "perfect zero," which guarantees a hot misalignment on any machine with meaningful temperature differential across its structure.
