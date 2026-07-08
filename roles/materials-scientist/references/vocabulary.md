# Vocabulary

Terms generalists flatten together that a materials scientist keeps sharply separate — the value is in the misuse, not the definition.

## Crystallite size vs. grain size vs. particle size

**Crystallite size** is the size of a coherently diffracting domain, extracted from XRD peak broadening (Scherrer/Williamson-Hall) — it can be smaller than the visible grain. **Grain size** is a microstructural feature boundary seen by microscopy (an optical or SEM grain, bounded by a grain boundary, which can contain multiple coherent sub-domains). **Particle size** is the size of a discrete physical particle (e.g., in a powder), which can itself be a polycrystalline aggregate of many grains.

**In use:** "XRD gives us a 50 nm crystallite size, but the SEM grains are visibly 300-500 nm — each grain is a few coherent sub-domains, not a single crystal."

**Common misuse:** treating an XRD-derived crystallite size as if it equals the particle or grain size seen in an image, when a single visible grain routinely contains several smaller coherent diffracting domains.

## Crystallinity (XRD) vs. crystallinity (DSC)

**XRD crystallinity** compares the integrated area under crystalline peaks to the total scattered intensity (crystalline + amorphous halo) — a structural, diffraction-based fraction. **DSC crystallinity** compares the measured heat of fusion (ΔHm, corrected for any cold-crystallization ΔHcc) to a reference 100%-crystalline heat of fusion for that material — a thermodynamic, enthalpy-based fraction. The two use different physics and routinely give different absolute numbers on the same sample; neither is "more correct," but they answer different questions.

**In use:** "DSC says 34% crystalline by heat of fusion — before we compare that to the XRD number, confirm which reference ΔH100% was used and that the two methods aren't being treated as interchangeable."

**Common misuse:** quoting a single "crystallinity" number without specifying which method produced it, or directly comparing an XRD-derived and a DSC-derived crystallinity as if measurement method didn't matter.

## Exfoliated vs. intercalated vs. tactoid (layered nanocomposite structure)

**Exfoliated** means individual clay/layered-filler platelets are fully separated and dispersed — the basal (00l) XRD reflection disappears below detection because the regular stacking periodicity is gone. **Intercalated** means polymer has entered between the layers and expanded the gallery spacing, but the layers remain in a regular, still-diffracting stack — the basal peak shifts to lower angle but does not vanish. A **tactoid** is the resulting stack of a few to tens of intercalated (or unmodified) platelets acting as one larger, lower-aspect-ratio reinforcing unit rather than individual sheets.

**In use:** "The (001) peak shifted but didn't disappear — that's intercalation, and the reinforcing unit in any stiffness model needs to use the tactoid's effective aspect ratio, not a single platelet's."

**Common misuse:** calling any nanocomposite with an XRD-detectable structural change "exfoliated," when a persisting (even shifted) basal peak specifically rules out full exfoliation.

## Instrumental broadening vs. size/strain broadening

**Instrumental broadening** is the peak width contribution from the diffractometer itself (slit geometry, wavelength dispersion, sample-height error), measured with a strain-free, large-crystallite reference standard. **Size broadening** and **strain broadening** are sample-intrinsic contributions from finite crystallite size and lattice microstrain, respectively — the quantities Scherrer and Williamson-Hall are meant to extract. Reported crystallite size or microstrain is only meaningful after the instrumental contribution is deconvolved from the raw measured FWHM.

**In use:** "Before running Scherrer on this peak, subtract the instrumental FWHM from the LaB6 standard scan at this 2θ — otherwise we're reporting an apparent crystallite size that's smaller than the real one."

**Common misuse:** applying Scherrer or Williamson-Hall directly to raw, uncorrected FWHM values, which systematically understates crystallite size and inflates apparent microstrain.

## Amorphous halo vs. crystalline peak

An **amorphous halo** is a broad, low-intensity diffuse hump in an XRD pattern from material with no long-range periodic order — it has no well-defined Bragg angle and cannot be indexed to a lattice. A **crystalline peak** is a sharp, indexable reflection at a specific 2θ obeying Bragg's law. Semicrystalline materials show both simultaneously, and the ratio of crystalline peak area to total (peak + halo) area is the basis of XRD crystallinity.

**In use:** "Integrate the halo under the 110/200 peak region separately before computing %crystallinity — otherwise the amorphous contribution gets counted as crystalline area."

**Common misuse:** treating a broad, low hump as a poorly resolved crystalline peak and attempting to index it, when its defining feature is the absence of a specific lattice periodicity to index.

## Cold crystallization

An exothermic crystallization event that occurs *on heating* (not cooling) a DSC sample, when a polymer quenched too fast to crystallize during processing has enough chain mobility to crystallize once heated above its Tg but before it melts. Its enthalpy (ΔHcc) must be subtracted from the melting enthalpy (ΔHm) to get the crystallinity the sample actually had *before* the DSC scan began — otherwise the scan credits crystallinity that only formed during the measurement itself.

**In use:** "This sample shows a cold-crystallization exotherm at 105°C — subtract that ΔHcc from ΔHm before reporting as-processed crystallinity, or we're crediting crystallinity the part didn't have when it left the mold."

**Common misuse:** reporting ΔHm alone as the crystallinity-determining enthalpy when a cold-crystallization exotherm is present, overstating the as-processed (pre-scan) crystallinity.

## Rule of mixtures vs. Halpin-Tsai

**Rule of mixtures** gives the theoretical upper bound (Voigt, iso-strain, continuous aligned fiber along the load direction) and lower bound (Reuss, iso-stress) for a composite modulus — simple but only exact for idealized, high-aspect-ratio continuous reinforcement. **Halpin-Tsai** is a semi-empirical interpolation that explicitly takes filler aspect ratio (via the ζ parameter) as an input, correctly predicting a lower modulus gain for low-aspect-ratio or platelet/tactoid reinforcement where the simple rule-of-mixtures upper bound overstates the real gain.

**In use:** "Don't use the rule-of-mixtures upper bound for a tactoid-reinforced system — Halpin-Tsai with the measured aspect ratio is the right model once the filler isn't continuous, aligned fiber."

**Common misuse:** applying the rule-of-mixtures upper bound to any composite regardless of filler geometry, overpredicting stiffness for anything short of continuous aligned-fiber reinforcement.

## Preferred orientation / texture

A non-random distribution of crystallite orientations in a sample (from platy or needle-like crystal habit, or from processing-induced alignment such as rolling or extrusion), which biases the relative intensities of XRD reflections away from the random-powder pattern a database match assumes. Uncorrected, it distorts intensity-ratio-based phase-fraction or texture-sensitive property estimates.

**In use:** "The (00l) reflections are way stronger than the reference pattern predicts — that's preferred orientation from the platy crystal habit, not evidence of a phase-fraction difference."

**Common misuse:** interpreting an intensity mismatch against a reference powder pattern as a phase-identification or phase-fraction problem, when it is actually a texture artifact from non-random crystallite packing.

## Rietveld refinement vs. single-peak (or peak-matching) phase ID

**Peak-matching phase ID** compares a pattern's peak positions against a reference database to identify phases present — fast, qualitative. **Rietveld refinement** fits a full calculated pattern (all peaks, intensities, and shapes simultaneously) against the measured data, refining lattice parameters, phase fractions, and crystallite size/strain with quantified uncertainty — the method required for a precise lattice parameter or a defensible quantitative phase fraction, not a single-peak calculation.

**In use:** "The single-(311)-peak lattice parameter is fine for a quick check, but the number going in the paper needs a full Rietveld refinement across all reflections, with the goodness-of-fit reported."

**Common misuse:** reporting a single-peak-derived lattice parameter or phase fraction with the same confidence as a Rietveld-refined value, when the single-peak number carries no cross-checking from the rest of the pattern.

## Aspect ratio — nominal (formulation) vs. effective (structural)

The **nominal aspect ratio** is what the raw filler's dimensions would imply if fully dispersed as specified in the formulation (e.g., a single clay platelet's length/thickness). The **effective aspect ratio** is what the filler's *actual* dispersed structure — as characterized by XRD, TEM, or SAXS — implies once tactoid stacking, agglomeration, or partial breakdown is accounted for. A structure-property model needs the effective value; the nominal value only applies if full dispersion is independently confirmed.

**In use:** "Don't plug the single-platelet aspect ratio into Halpin-Tsai — TEM shows 15-20-platelet tactoids, so the effective aspect ratio is an order of magnitude lower."

**Common misuse:** using the filler's as-supplied or as-formulated aspect ratio in a predictive model without confirming, structurally, that the filler actually achieved that state of dispersion in the finished material.

## Solid solution vs. two-phase mixture

A **solid solution** is a single crystalline phase with a continuously variable composition and a single set of lattice parameters that shift smoothly with composition (Vegard's law). A **two-phase mixture** shows two distinct sets of reflections (or a split/broadened single reflection) corresponding to two different compositions coexisting — a fundamentally different microstructure with different property implications (e.g., different corrosion behavior at phase boundaries, different mechanical response).

**In use:** "One unsplit (311) peak, lattice parameter tracking Vegard's law within 0.4% — call this a solid solution, not a two-phase mixture."

**Common misuse:** assuming any nominally single-composition synthesis target produced a true solid solution without checking for peak splitting or a Vegard's-law deviation large enough to indicate phase segregation.

## Degree of polymerization / molecular weight vs. crystallinity

**Molecular weight** (or degree of polymerization) describes chain length, a molecular-scale property set primarily by the polymerization or processing history (e.g., thermal/hydrolytic chain scission during melt processing). **Crystallinity** describes what fraction of that material has organized into an ordered, crystalline structure — a distinct, though related, structural level; processing that lowers molecular weight (e.g., excessive shear or residence time) can independently change crystallization kinetics and shift crystallinity even when no compositional variable was intentionally changed.

**In use:** "Before attributing the crystallinity shift to the new dopant, check GPC — if molecular weight dropped from extra extrusion passes, that alone changes crystallization kinetics."

**Common misuse:** attributing a crystallinity change entirely to an intentional formulation variable without ruling out an unintended molecular-weight change from processing as a confound.
