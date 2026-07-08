# Vocabulary

Terms generalists flatten together that a marine engineer/naval architect keeps sharply separate — the value is in the misuse, not the definition.

## Metacentric height (GM) vs. righting arm (GZ)

**GM** is the small-angle (initial) measure of stability — the height of the metacenter above the center of gravity. **GZ** is the actual righting lever at any specific heel angle, read from the hull's cross curves and corrected for the loading condition's true KG; GZ ≈ GM×sin(θ) only holds for small angles, not the 30-40° range the IS Code actually checks.

**In use:** "GM clears the minimum, but we still need the GZ curve out to 40° — GM only describes the first few degrees."

**Common misuse:** treating a passing GM as proof the whole stability envelope is acceptable, skipping the large-angle GZ curve entirely.

## Block coefficient (Cb) vs. waterplane coefficient (Cwp)

**Cb** = ∇/(L×B×T), the ratio of the underwater hull volume to its enclosing box. **Cwp** = Aw/(L×B), the ratio of the waterplane area to the same box at the waterline. They move together but aren't interchangeable — BM depends on Cwp (via waterplane inertia), not on Cb directly.

**In use:** "Cb is 0.72 for the displacement calc, but BM needs Cwp — don't substitute one for the other."

**Common misuse:** using Cb in a formula that actually calls for Cwp, most often in hand BM/KM approximations.

## Free surface correction (FSC) vs. free surface effect (FSE)

**FSE** is the physical phenomenon — liquid in a partially full tank shifting toward the low side as the ship heels, moving the effective center of gravity outward. **FSC** is the specific numeric reduction (in meters) applied to GM to account for it, computed from the tank's transverse free-surface moment of inertia, not its total liquid weight.

**In use:** "FSC on the No. 2 fuel tank is 0.09 m at this sounding — full or empty it would be near zero, it's the half-full state that costs GM."

**Common misuse:** assuming a tank's free surface effect scales with how much liquid is in it, rather than with breadth cubed and specifically peaking near the half-full condition.

## Displacement vs. deadweight vs. lightship

**Displacement (Δ)** is the total weight of the ship afloat, equal to the weight of water it displaces. **Lightship** is the empty-ship weight (steel, outfit, machinery, no cargo/fuel/stores). **Deadweight (DWT)** is everything variable the ship can carry — cargo, fuel, water, stores, crew — so Δ = lightship + deadweight actually loaded, and DWT is the ship's maximum carrying capacity, not its current loaded weight.

**In use:** "Deadweight is 3,200 t max, but at this call we're only carrying 2,900 t of cargo plus stores — actual displacement is well under the deadweight-plus-lightship ceiling."

**Common misuse:** using deadweight as if it were displacement in an Archimedes-based hydrostatic calculation, which needs the actual total weight afloat, not the maximum carrying capacity.

## Freeboard vs. draft vs. depth

**Depth (D)** is a fixed hull dimension, keel to the freeboard deck. **Draft (T)** is how deep the hull sits in the water at a given loading condition. **Freeboard** is what's left above water: D − T. Regulatory minimum freeboard sets a maximum permissible draft for a given depth, not the other way around.

**In use:** "Depth is fixed at 7.20 m — the load line calculation is really solving for the maximum allowable draft, freeboard is just D minus that draft."

**Common misuse:** treating freeboard as a design input chosen freely, rather than the regulatory output that constrains the maximum draft.

## Admiralty coefficient

A dimensionless powering approximation, Ac = Δ^(2/3)×V³/SHP, calibrated from a reference vessel's actual trial data and applied to a new, form-matched design to estimate required shaft horsepower at concept stage.

**In use:** "Ac of 430 comes from a sister-form coastal cargo ship's trial data — that's the calibration this estimate is only as good as."

**Common misuse:** applying a published Ac from an unrelated ship type (different Cb or speed range) as if the coefficient were a universal constant rather than a form- and speed-specific calibration.

## Downflooding angle

The heel angle at which water first enters the hull through an opening that is not weathertight (an unsecured vent, a non-watertight door) — distinct from the angle at which GZ crosses zero (the angle of vanishing stability).

**In use:** "Downflooding angle is 38° through the engine room vent — that's what actually caps the 40° area-under-curve integration, not the vanishing-stability angle."

**Common misuse:** confusing downflooding angle with the angle of vanishing stability, or assuming the IS Code's area integration always runs to a full 40° regardless of where downflooding actually occurs.

## Cross curves of stability (KN curves)

A family of curves, generated once per hull form independent of loading condition, giving KN (a geometric righting-arm term) at a range of heel angles for a range of assumed displacements — GM/GZ for any actual loading condition is then derived from this same KN set using that condition's real KG.

**In use:** "Pull KN at 30° for this displacement off the cross curves, then subtract KG×sin(30°) to get the actual GZ for this condition."

**Common misuse:** treating the KN curve itself as the ship's GZ curve, without the KG-dependent correction that makes it condition-specific.

## Parametric rolling

A resonant rolling phenomenon driven by periodic waterplane-area (and hence GM) variation as a ship pitches through waves, distinct from ordinary beam-sea resonant rolling — most severe on hull forms with pronounced flare/tumblehome (container ships, some ro-ros) in head or following seas near twice the roll natural period.

**In use:** "This hull's flared bow sections make it a parametric-rolling candidate in following seas — the weather criterion alone doesn't check for that."

**Common misuse:** treating parametric rolling as just another name for beam-sea resonance, missing that it's driven by pitch-coupled GM variation and occurs in head/following seas, not beam seas.

## Load line / freeboard deck

The **freeboard deck** is the specific deck used as the reference for freeboard calculations under ICLL — normally the uppermost complete deck exposed to weather and sea with permanent means of closing all openings, not automatically "whatever deck looks uppermost" on the arrangement drawing.

**In use:** "Confirm which deck is designated the freeboard deck in the stability booklet before pulling the depth (D) used in the ICLL calculation."

**Common misuse:** assuming the freeboard deck is always the true uppermost continuous deck, when a lower deck may be designated instead depending on closing arrangements.

## Subdivision index (A-index, SOLAS 2009 harmonized damage stability)

A probabilistic measure (0 to 1) of a ship's ability to survive random flooding across a range of damage cases, compared against a required index (R) set by ship type and size — replaces the older deterministic "must survive flooding of any single compartment" standard.

**In use:** "Attained index A = 0.82 against required R = 0.78 — that's a probabilistic pass across the full damage-case matrix, not a single-compartment check."

**Common misuse:** treating damage stability as a pass/fail single-worst-case test, as under the pre-2009 deterministic standard, instead of the probabilistic weighted-average result SOLAS 2009 actually requires.

## Sea margin vs. service margin

**Sea margin** covers added resistance from wind, waves, and current on the intended route. **Service/fouling margin** covers hull and propeller roughness growth between drydockings. Both add to calm-water clean-hull power, but from different physical causes and different design decisions (route notation vs. drydocking interval).

**In use:** "20% total margin here is 15% sea margin for the coastal route plus 5% service margin for an 18-month docking cycle — they're not the same allowance."

**Common misuse:** applying a single blended margin percentage without distinguishing which physical effect it's meant to cover, making it unclear whether a longer docking interval or a rougher route drove the number.

## Scantling draft vs. design (summer load line) draft

**Scantling draft** is the maximum draft the hull structure is designed to withstand. **Design/summer load line draft** is the draft actually assigned for normal loaded operation, which may be equal to or less than scantling draft. A ship can be built to a scantling draft deeper than its assigned load line, leaving structural reserve not available for normal loading.

**In use:** "Scantling draft is 6.20 m, but the assigned summer load line is 5.80 m — the extra 0.40 m of structural capacity isn't usable without a load line amendment."

**Common misuse:** assuming the deepest draft the structure can handle is the same as the deepest draft the ship is legally permitted to load to.

## Weather criterion (severe wind and rolling)

A dynamic stability check under the IS Code that verifies a vessel can survive a specified beam wind combined with synchronous rolling, evaluated by comparing wind heeling energy against righting energy — a distinct pass/fail criterion from the static GM and GZ-area checks, not a restatement of them.

**In use:** "Static GZ-area criteria all pass, but we still owe the weather criterion calculation before the booklet is complete."

**Common misuse:** treating the static intact stability criteria (GM, GZ area) as covering dynamic wind/roll survivability, and skipping the separate weather criterion calculation.

## Trim vs. list

**Trim** is the fore-aft difference between forward and aft draft, normally from cargo/ballast distribution along the ship's length. **List** is a sustained athwartships (port/starboard) inclination, normally from asymmetric loading — distinct from **heel**, a temporary athwartships inclination from an external force (wind, turning) that returns to upright when the force is removed.

**In use:** "There's a 2° list from the asymmetric ballast tank fill — that's a loading fix, not a heel we'll ride out once we're underway."

**Common misuse:** using "list" and "heel" interchangeably, obscuring whether the athwartships angle is a persistent loading problem to fix or a transient response to an external force.
