# Vocabulary

Terms generalists flatten together that a mining/geological engineer keeps sharply separate — the value is in the misuse, not the definition.

## Factor of safety (FS) vs. probability of failure (PoF)

**Factor of safety** is a deterministic ratio of resisting to driving force at one set of input values. **Probability of failure** is the output of treating those same inputs as distributions (Monte Carlo or similar) and reporting the fraction of outcomes below FS = 1.0. A slope can carry an FS comfortably above 1.0 on best-estimate inputs and still carry an unacceptable PoF if the input parameters are highly variable.

**In use:** "FS = 1.4 on best-estimate strength, but the PoF run shows 12% of iterations below FS 1.0 — that's outside our interim criterion even though the deterministic number looks fine."

**Common misuse:** treating a single deterministic FS as a complete risk statement, when two slopes with the same FS can carry very different PoF depending on how well-constrained the input parameters are.

## RMR vs. Q vs. GSI

**RMR (Rock Mass Rating, Bieniawski)** and **Q (Barton)** are both empirical classification systems built from different but overlapping input parameters (RMR: UCS, RQD, spacing, condition, groundwater; Q: RQD, joint sets, roughness, alteration, water, stress) and correlate roughly but aren't interchangeable. **GSI (Geological Strength Index, Hoek-Brown)** is a separate index used specifically as an input to the Hoek-Brown strength criterion for numerical modeling, not primarily a support-selection tool.

**In use:** "Score both RMR and Q independently at this station — don't back-calculate one from the other — and use GSI separately when it feeds the Hoek-Brown parameters for the FLAC model."

**Common misuse:** using the RMR-to-Q correlation formula to generate one system's score from the other instead of independently field-rating both, which hides rater disagreement that the correlation is supposed to surface.

## Cutoff grade — marginal (mill) vs. breakeven (mine) vs. internal

**Marginal/mill cutoff** covers only the incremental cost of processing already-broken material (mill vs. waste-dump decision). **Breakeven/mine cutoff** covers the full cost including mining (whether to move the material at all). **Internal cutoff** (a further Lane refinement) applies inside a pit-limit optimization to material that must be mined anyway to access ore below it, where even the marginal processing cost may not need to be recovered from that specific block. Confusing which one applies to a given decision misallocates real tonnage.

**In use:** "That block only needs to clear the internal cutoff — we have to mine through it to get to the ore underneath regardless, so don't hold it to the full mine-limiting cutoff."

**Common misuse:** applying the full mine-limiting cutoff to a mill-vs-waste-dump decision on material already mined, which sends economically millable ore to the waste dump.

## Dilution vs. mining recovery

**Dilution** is waste rock (or lower-grade material) unintentionally included in the mined tonnage, lowering the delivered grade below the in-situ block grade. **Mining recovery** is the fraction of the in-situ ore tonnage actually extracted, distinct from dilution — a stope can have high dilution and high recovery simultaneously, or low dilution and significant ore loss left behind (e.g., in pillars).

**In use:** "Reconcile separately: dilution is why delivered grade is lower than the model, recovery is why delivered tonnage is lower than the block model's ore tonnage — don't fold both into one 'grade control factor.'"

**Common misuse:** using a single blended "mine call factor" that conflates dilution and recovery, which hides which one is actually driving a reconciliation miss.

## Strip ratio

The ratio of waste tonnes moved to ore tonnes mined for a given pit or pushback, distinct from the **stripping ratio limit (breakeven strip ratio)**, the maximum strip ratio at which mining the ore still covers the incremental waste-removal cost at the current price/cost basis.

**In use:** "Current strip ratio on this pushback is 3.2:1 — the breakeven limit at today's copper price and cost basis is 3.8:1, so it's still economic, but re-check that limit before the next price review."

**Common misuse:** treating strip ratio as a fixed pit-design input rather than an economic variable that moves with price and cost, and comparing it against a stale breakeven limit.

## Interramp angle vs. overall slope angle vs. bench face angle

**Bench face angle** is the steepest, single-bench slope face. **Interramp angle** is the angle across several benches between ramps, excluding ramp width. **Overall slope angle** is the angle from toe to crest of the entire pit wall, including all ramps and berms, and is always shallower than the interramp angle, which is always shallower than the bench face angle. Reporting one when the acceptance criterion specifies another materially misstates the design.

**In use:** "The interramp FS check passes at 45°, but confirm which angle the design criterion actually specifies — the overall slope angle at this same location is closer to 38° once the haul ramp is subtracted."

**Common misuse:** using bench-scale or interramp-scale angle and FS interchangeably with overall-slope-scale criteria, which are set at different consequence levels and shouldn't be substituted for each other.

## Ore reserve vs. mineral resource

**Mineral resource** (measured/indicated/inferred, under JORC, NI 43-101, or SME reporting codes) describes what's estimated to be in the ground with reasonable geological confidence, with no requirement that it's currently economic to mine. **Ore reserve** (proven/probable) is the subset of a measured or indicated resource that has been demonstrated economically and technically mineable under a stated cutoff grade, mining method, and cost/price assumption — an inferred resource can never convert directly to a reserve without upgrading the confidence category first.

**In use:** "That tonnage is still resource, not reserve — it hasn't cleared the economic and technical study the reporting code requires, and the inferred-category material can't be counted in the reserve at all."

**Common misuse:** using "reserves" loosely to describe any estimated tonnage, when the reserve category carries a specific, code-defined economic and confidence bar that resource tonnage hasn't cleared.

## Convergence-confinement (ground reaction curve)

A model of the interaction between an excavated opening's inward displacement (convergence) and the confining pressure provided by installed support, plotted as two curves (the ground reaction curve and the support characteristic curve) whose intersection gives the equilibrium support load. Support installed too early intersects the ground reaction curve while it's still steep, taking more load than necessary; installed too late, the rock has already loosened past the point the support curve can reconfine it.

**In use:** "Delay shotcrete application by one round to let some convergence happen first — installing it right at the face on this ground puts it on the steep part of the reaction curve."

**Common misuse:** treating support timing as purely a schedule/logistics question, when the ground reaction curve makes it a structural design variable with a wrong-answer zone on both the too-early and too-late sides.

## Pore pressure ratio (ru)

A dimensionless simplification (Bishop) expressing pore pressure at a point as a fraction of the total overburden stress at that point: u = ru·γ·h. Used to run slope stability sensitivity when piezometer coverage is sparse, distinct from directly measured pore pressure, which should replace the ru assumption wherever it exists.

**In use:** "No piezometers in this domain yet, so the design runs an ru sweep from 0 to 0.3 rather than assuming a single dry or wet case."

**Common misuse:** treating a single assumed ru value as equivalent to measured pore pressure data, rather than as a placeholder sensitivity range pending actual monitoring.

## Kinematic analysis / daylighting

A stereonet-based check of whether a discontinuity (or the intersection of two) is oriented such that it can physically slide or topple out of a slope or opening face, independent of the rock mass's overall classification rating. A structure "daylights" when its dip direction and dip angle allow it to exit the excavated face; a structure that doesn't daylight can't kinematically fail regardless of how weak the joint infill is.

**In use:** "RMR says fair rock, but the kinematic check shows this joint set daylights into the north wall at a dip flatter than the slope angle — that wedge governs regardless of the RMR class."

**Common misuse:** relying on the RMR/Q empirical support chart alone and skipping the kinematic check, missing a structurally controlled failure that an average rock-mass rating is not designed to catch.

## ESR (excavation support ratio)

A Q-system input reflecting how much risk an opening's use tolerates — lower ESR (e.g., 1.0 for a permanent civil structure) demands more support for the same Q value than a higher ESR (e.g., 3–5 for a temporary mine opening); it's a consequence/use factor, not a rock property.

**In use:** "Same Q value, but this is a permanent ventilation drift, not a temporary access — use ESR 1.6, not the 3.0 we'd use for a short-life exploration drive, and the bolt length comes out longer."

**Common misuse:** applying one blanket ESR value across every opening in a mine regardless of its intended service life and consequence, under- or over-supporting openings that don't match the assumed use.

## Net smelter return (NSR)

The revenue per tonne of ore actually received after applying metal price, recovery, payability, and smelter treatment/refining deductions — the number that belongs in a cutoff-grade or block-value calculation, as distinct from gross in-situ metal value, which ignores all of those deductions.

**In use:** "Don't rank blocks by contained metal value — rank by NSR per tonne, since payability and TC/RC deductions change the ranking once you account for them."

**Common misuse:** using gross contained-metal value (price × grade, no deductions) to compare ore blocks or set a cutoff, which overstates value and biases the ranking toward metals or deposits with worse payability/deduction terms.
