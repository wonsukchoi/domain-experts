# Vocabulary

Terms generalists flatten together that a materials engineer keeps sharply separate — the value is in the misuse, not the definition.

## Hardness vs. hardenability

**Hardness** is a point measurement (Rockwell, Brinell, Vickers) of resistance to indentation at the spot tested. **Hardenability** is how *deep* a section hardens on quenching, governed by alloy content, independent of the maximum hardness a carbon level allows. Two steels can share a surface hardness spec and differ enormously at the core of a thick section.

**In use:** "1040 and 4140 can both hit 55 HRC at the surface — the difference shows up at the core of a 2-inch bar, and that's a hardenability question, not a hardness question."

**Common misuse:** treating a passing surface hardness reading as proof the part through-hardened, when only a sectioned hardness traverse (or a Jominy/H-band spec check) actually answers that.

## Toughness (Charpy) vs. fracture toughness (KIC)

**Charpy V-notch (CVN) toughness** is an impact energy (joules) absorbed breaking a notched bar — a comparative, code-driven screening test. **Fracture toughness (KIC or JIC)** is a quantitative material property (MPa*m^0.5) used directly in a fracture-mechanics calculation to find critical flaw size or applied stress intensity. Correlations exist between the two but are approximate and grade-specific — CVN energy is not a substitute for a KIC value in a fitness-for-service calculation.

**In use:** "The code's impact test just tells us we're above the DBTT for this thickness — for the actual critical crack size calculation we need a real KIC number, not a CVN-to-KIC correlation."

**Common misuse:** plugging a Charpy energy value directly into a fracture-mechanics formula that requires KIC, or treating a passing CVN test as equivalent to having toughness data for a flaw-tolerance assessment.

## Endurance limit (Se) vs. fatigue strength

The **endurance limit** is the stress below which a material (some steels and titanium alloys) can theoretically endure infinite cycles without fatigue failure. **Fatigue strength** is the stress corresponding to a *specified finite life* (e.g., the stress at 10^7 cycles) — the term to use for materials, like most aluminum alloys, that never show a true endurance limit and keep losing strength as cycle count increases.

**In use:** "Don't call it an endurance limit for the aluminum bracket — quote the fatigue strength at the design life, because aluminum's S-N curve never flattens out."

**Common misuse:** applying an "endurance limit" mindset (infinite life below a threshold) to a material class that doesn't exhibit one, understating long-term fatigue risk on aluminum, copper, and most nonferrous alloys.

## Yield strength vs. 0.2% offset (proof) stress

For metals without a sharp yield point, **yield strength** as reported on a datasheet is almost always the **0.2% offset stress** — the stress at which the stress-strain curve deviates from linear-elastic by 0.2% permanent strain, not a physically distinct "yield event." Materials with a sharp yield point (some low-carbon steels) have an actual yield point distinct from any offset construction.

**In use:** "That 1370 MPa 'yield strength' on the 4340 datasheet is the 0.2% offset value — there's no sharp yield point at this hardness level."

**Common misuse:** treating "yield strength" as a universally sharp, physically observed transition, when for most engineering alloys it's a defined construction on a smooth curve.

## Stress concentration factor (Kt) vs. fatigue notch factor (Kf)

**Kt** is a purely geometric, theoretical elastic stress-concentration factor from the part's shape alone. **Kf** is the *effective* concentration factor under cyclic loading, always <= Kt, reduced from Kt by the material's notch sensitivity (q): Kf = 1 + q(Kt - 1). Applying Kt directly to a fatigue calculation overstates the concentration for any material with q < 1.

**In use:** "Kt from the chart is 1.7, but this alloy's notch sensitivity at that radius is 0.85, so the Kf we actually apply to the alternating stress is 1.6, not 1.7."

**Common misuse:** using Kt and Kf interchangeably, most commonly applying the geometric Kt directly in a fatigue calculation and overstating the effective concentration, or conversely applying Kf to a static/monotonic strength check where Kt (or no concentration factor at all, for ductile static loading) is the correct one.

## Residual stress — compressive vs. tensile

**Residual stress** is stress locked into a part with no external load applied, from prior processing (machining, welding, quenching, shot peening). **Compressive** residual stress at a surface is generally beneficial for fatigue (it must be overcome before a cyclic tensile stress can open a surface crack); **tensile** residual stress (common from welding or grinding burn) is detrimental, effectively adding to the applied mean stress.

**In use:** "Shot peen the fillet to put the surface into compression — that's buying fatigue life the Goodman calculation alone doesn't show."

**Common misuse:** treating "residual stress" as inherently bad, when compressive residual stress from a controlled process (shot peening, cold rolling of a fillet) is a deliberate and effective fatigue-life improvement.

## Case depth — total vs. effective

**Total case depth** is the full visible depth of microstructural change (carburized or nitrided layer) on a metallurgical section. **Effective case depth** is the depth to a specified hardness value (commonly 50 HRC), the number that actually correlates with fatigue and wear performance. A spec that says "case depth 0.8 mm" without specifying which one is ambiguous and can pass or fail the same part depending on interpretation.

**In use:** "Confirm whether the 0.8 mm case depth callout on this drawing means total or effective — at 50 HRC effective, the total case is usually noticeably deeper."

**Common misuse:** comparing a measured total case depth against a spec written for effective case depth (or vice versa), producing a false pass or false reject.

## Retained austenite

Untransformed austenite remaining in a quenched steel's microstructure instead of converting to martensite, more prevalent in high-carbon and high-alloy steels quenched from a temperature where the martensite-finish (Mf) temperature is below room temperature. It can transform later under stress or over time, causing dimensional growth or delayed cracking.

**In use:** "XRD shows 12% retained austenite on this D2 tool steel — spec calls for a cryogenic treatment before final grind to knock that down before it causes dimensional drift."

**Common misuse:** assuming a passing as-quenched hardness reading means the microstructure is stable, when retained austenite can sit invisibly under a hardness spec and still cause delayed dimensional or cracking problems.

## Stress corrosion cracking (SCC) vs. corrosion fatigue

**SCC** is crack initiation and growth under a *static* (or near-static) tensile stress in a specific alloy/environment combination (e.g., austenitic stainless steel in chloride service), often with little visible general corrosion. **Corrosion fatigue** is crack growth under *cyclic* stress in a corrosive environment, with no specific alloy/environment susceptibility threshold — any cyclic load in a corrosive environment reduces fatigue life, unlike SCC which requires a specific susceptible combination.

**In use:** "This is corrosion fatigue, not SCC — the load is cyclic and this alloy isn't classically SCC-susceptible in this chloride level, but the corrosive environment is still degrading the S-N curve."

**Common misuse:** labeling any crack found in a corrosive environment "SCC" regardless of whether the loading was static or cyclic, which points the corrective action at the wrong mechanism (alloy substitution for SCC susceptibility vs. coating/cathodic protection for general corrosion-fatigue degradation).

## Creep vs. stress rupture

**Creep** is the time-dependent, progressive strain a material accumulates under sustained load at elevated temperature, characterized by a creep curve (primary/secondary/tertiary stages) and often reported as a strain rate. **Stress rupture** is the time to actual fracture under a sustained load and temperature — a related but distinct property; a material can be within an acceptable creep-strain limit and still be closer to its stress-rupture life than assumed if the tertiary (accelerating) creep stage has begun.

**In use:** "The creep-strain budget still has margin, but check where we are on the stress-rupture curve separately — tertiary creep can accelerate fast once it starts."

**Common misuse:** treating an acceptable creep-strain reading as proof of remaining life, without separately checking stress-rupture time, especially once tertiary creep onset is suspected.

## Anisotropy / grain flow

Mechanical properties (especially toughness and fatigue strength) that differ by direction relative to the material's grain flow, from forging, rolling, or extrusion. A forged part with grain flow following its contour typically has meaningfully better transverse toughness and fatigue resistance than a part machined from bar stock where the load direction cuts across the grain.

**In use:** "Spec a forging for that highly loaded flange, not a machined-from-plate part — the transverse properties across bar stock's grain direction won't meet the fatigue requirement."

**Common misuse:** assuming a material's datasheet properties apply equally in every direction, when longitudinal and transverse properties from the same heat and process can differ by 20% or more in ductility and toughness.

## Quench and temper vs. normalize vs. anneal

**Quench and temper** hardens by rapid cooling to form martensite, then reheats (temper) to trade some hardness for toughness — the process behind most structural-steel strength specs. **Normalize** is air-cooling from above the transformation temperature to refine and homogenize grain structure without the hardness of a full quench. **Anneal** is slow furnace cooling to maximize softness and machinability, minimizing internal stress. These are distinct thermal cycles with different property outcomes, not interchangeable steps in a generic "heat treatment."

**In use:** "The forging needs to be normalized before final machining to break up the as-forged grain structure — that's separate from, and prior to, the quench-and-temper cycle that sets final strength."

**Common misuse:** using "heat treated" as if it specifies an outcome, when quench-and-temper, normalizing, and annealing produce very different hardness, toughness, and residual-stress results from the same starting material.

## Alloy designation — AISI/SAE vs. UNS

**AISI/SAE** numbers (e.g., 4340, 6061) are the common trade designations tied to a nominal chemistry range, widely used in drawings and casual reference. **UNS (Unified Numbering System)** numbers (e.g., G43400 for 4340, A96061 for 6061) are the ASTM/SAE cross-referenced formal identifiers used in procurement specs and material certifications to remove ambiguity across standards bodies. A drawing citing only the AISI number without a governing ASTM/SAE spec number leaves the actual required chemistry and property range underspecified.

**In use:** "Call out ASTM A29 4340 (UNS G43400) on the drawing, not just '4340' — the bare AISI number doesn't tell the mill which chemistry and condition spec governs."

**Common misuse:** treating the AISI number alone as a complete material specification, when procurement and certification actually require the governing ASTM/SAE standard number to define chemistry limits, condition, and test requirements.
