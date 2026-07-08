# Vocabulary

Terms of art generalists misuse — not terms they could just look up. Each entry gives the practitioner definition, an in-use example, and the specific way it gets misapplied.

## Conformality / step coverage

**Definition.** The ratio of coating thickness at the bottom (or sidewall) of a feature to the thickness at the top, expressed as a percentage or fraction — a measure of how uniformly a deposition process coats a non-planar surface, not how thick the coating is.

**In use:** "Bottom-of-feature reading is 3.6 nm against a 4.4 nm target — that's 82% conformality, well outside the >95% self-limiting regime ALD is supposed to deliver at this aspect ratio."

**Misuse note.** Generalists treat a passing top-surface measurement as proof the process is "conformal." Conformality is a top-to-bottom ratio; a recipe can be dead-on at the trench opening and starved at depth, and reporting only the top number silently drops the number that actually defines the term.

## Self-limiting (surface reaction)

**Definition.** A reaction mechanism, central to ALD, where the precursor saturates the available surface sites and then stops reacting regardless of further exposure — growth per cycle is fixed by surface chemistry, not by how long or how much precursor is dosed.

**In use:** "Extending the pulse time by 25% isn't overdosing the film — we're still inside the self-limiting window, just giving the precursor enough time to reach saturation at the bottom of a 100:1 feature."

**Misuse note.** Generalists assume "self-limiting" means the process is insensitive to timing, so a conformality failure gets diagnosed as a hardware or chemistry problem instead of the correct read: at high aspect ratio, insufficient pulse/purge time can prevent the reaction from ever reaching its self-limiting saturation point at depth, even though the mechanism itself is self-limiting.

## Stiction

**Definition.** Permanent adhesion of a released MEMS/NEMS structure to an adjacent surface, caused by capillary force during the liquid-vapor interface of wet release (or by van der Waals/electrostatic forces after drying) — not friction, and not a fabrication defect in the structure itself.

**In use:** "The cantilever didn't break during etch — it survived release and then stiction pulled it flat against the substrate as the rinse solvent evaporated."

**Misuse note.** Non-specialists read "stiction" as a portmanteau of "stuck friction" and assume it's a mechanical wear phenomenon. It's a surface-force failure mode specific to nanoscale surface-area-to-volume ratios, and the fix is process-side (supercritical CO2 drying, SAM coating) — not a material or geometry redesign.

## Aspect ratio (in deposition context)

**Definition.** The ratio of a feature's depth to its width, used to predict whether a deposition technique can reach the bottom of the feature — not a generic shape descriptor.

**In use:** "Past roughly 10:1 aspect ratio, CVD's line-of-sight deposition starts starving the bottom of the trench; that's the threshold where switching to ALD is worth its slower deposition rate."

**Misuse note.** Generalists use "high aspect ratio" loosely to mean "deep" or "narrow" without tying it to a specific technique's known crossover point. In this domain the number is a decision threshold (roughly 10:1 CVD/PVD-to-ALD, >100:1 for ALD's >95% step-coverage claim to hold) — stating aspect ratio without stating which regime it falls in leaves the actionable part out.

## Critical dimension (CD)

**Definition.** The smallest feature width or spacing on a fabricated pattern that a process is specified to hold within tolerance — the number a lithography or etch process is qualified against, measured by CD-AFM or CD-SEM.

**In use:** "If CD-AFM reads outside 4.4 nm ± 0.3 nm, stop and check tip calibration before restarting — don't requalify the process off a single out-of-spec CD reading."

**Misuse note.** Generalists use "CD" as a synonym for "resolution" or "smallest feature the tool can make." CD is a spec number tied to a specific measured feature on a specific process, with a stated tolerance and measurement uncertainty — conflating it with the tool's theoretical resolution limit skips the tolerance-and-uncertainty framing that makes the number actionable.

## Overlay

**Definition.** The alignment accuracy between two successive lithography layers, typically reported as a 3-sigma value — a registration metric, distinct from resolution (the smallest feature a single layer can print).

**In use:** "Nanoimprint's ~10 nm 3-sigma overlay is fine for this device, even though its resolution is coarser than e-beam's — overlay and resolution are different specs and this design is overlay-limited, not resolution-limited."

**Misuse note.** Generalists use "overlay" and "resolution" interchangeably as both being about "how small/precise the pattern is." A process can have excellent resolution and poor overlay (or vice versa), and which one is the binding constraint determines the technique choice — collapsing the two terms collapses a real decision axis.

## Defect density (yield context)

**Definition.** Defects per unit area used as the input to a yield model — related to yield nonlinearly (via a model like the Poisson or negative-binomial yield equation), not proportionally.

**In use:** "Going from 0.01 to 0.05 defects/cm² is a 5x increase in defect density but can drop yield from ~70% to ~12% — don't budget the process window as if yield degrades linearly with defect count."

**Misuse note.** Generalists treat "5x more defects" and "5x worse yield" as roughly the same statement. The relationship is nonlinear and the collapse can be much steeper than the defect-density increase suggests — a process window set against a linear mental model will look fine at pilot scale and fail at production scale.

## REL vs. PEL

**Definition.** PEL (permissible exposure limit) is an OSHA-enforceable legal ceiling; REL (recommended exposure limit) is a NIOSH-published advisory guideline with no independent legal force. For engineered nanomaterials, no OSHA nano-specific PEL exists — only RELs.

**In use:** "There's no PEL for carbon nanotubes — the 1 µg/m³ NIOSH REL is the number we've chosen to enforce internally, and that's a judgment call, not a compliance requirement we're satisfying."

**Misuse note.** Generalists treat any published exposure number as equally binding and say things like "we're within the PEL" when citing a REL. The distinction matters because meeting a REL isn't a regulatory safe harbor — the engineer, not the regulator, is accountable for the exposure control design.

## Nano-object / nanoparticle / nanoplate / nanofibre

**Definition.** ISO/TS 27687 terms distinguished by dimensionality: a nano-object is the umbrella term (any of the three below); a nanoparticle has all three external dimensions in the nanoscale; a nanoplate has one dimension in the nanoscale; a nanofibre has two dimensions in the nanoscale. Not interchangeable synonyms for "small particle."

**In use:** "This is a nanoplate, not a nanoparticle — only one dimension is under 100 nm — so the applicable characterization and exposure protocol is different from the isotropic-nanoparticle case."

**Misuse note.** Generalists use "nanoparticle" as a catch-all for anything nanoscale. Because the ISO terms are dimensionality-specific and different protocols attach to each, calling a nanofibre a "nanoparticle" in a report or exposure plan misapplies the protocol that's supposed to follow from the classification.

## EPR (enhanced permeability and retention)

**Definition.** A passive tumor-accumulation mechanism relying on leaky tumor vasculature and poor lymphatic drainage to trap circulating nanoparticles — one candidate delivery mechanism among several, with a documented median systemic-delivery efficiency under 1% in a large literature survey, not a reliable design default.

**In use:** "Don't size the delivery system around EPR alone — the survey data puts median tumor delivery at 0.7%, so active receptor-mediated targeting needs to be the primary mechanism, with EPR as a secondary contributor at best."

**Misuse note.** Generalists who've encountered EPR in an intro-level source treat it as the mechanism nanomedicine delivery is built on. Citing EPR as if it were sufficient justification for a delivery design, without the reproducibility/efficiency data, is exactly the naive read the field has since moved past.

## More Moore vs. More than Moore

**Definition.** Two distinct roadmap regimes from the IEEE IRDS: "More Moore" is classical CMOS dimensional/density scaling; "More than Moore" covers non-scaling functional diversification — sensors, actuators, energy harvesting, flexible electronics — with different economics and failure modes than density scaling.

**In use:** "This is a More than Moore program — a MEMS pressure sensor — so cost and timeline should be modeled against sensor-integration precedents, not against a logic-node scaling curve."

**Misuse note.** Generalists apply CMOS-scaling cost/timeline intuition (cost-per-transistor curves, node-shrink cadence) to projects that are actually in the More than Moore regime, where those economics don't hold — the classification isn't just labeling, it's the input to which cost model applies.

## Pilot scale

**Definition.** A production run at reduced volume/throughput used specifically to characterize the defect-density-to-yield curve and failure mechanisms before committing to full production volume — not simply "a smaller batch" or "a test run" in the generic sense.

**In use:** "The pilot run's job is to map where the yield curve starts collapsing, not just to confirm the process works at small scale — a process window that looks clean at pilot's low defect density can still fail once scaled."

**Misuse note.** Generalists treat a successful pilot as evidence the process is ready for production, because it demonstrated the effect at some volume. Given yield's nonlinear relationship to defect density, a pilot that looks fine is only informative about the part of the curve it sampled — it doesn't validate the process at production-scale defect rates unless that's explicitly what was measured.

## Self-assembled monolayer (SAM)

**Definition.** A single-molecule-thick coating that spontaneously organizes on a surface via a headgroup-substrate chemical bond, used in this domain as an anti-stiction surface treatment (e.g., OTS, FDTS, DDMS) — a surface-chemistry fix, not a bulk material coating.

**In use:** "If the supercritical CO2 dryer isn't available, fall back to an OTS SAM coating — it changes the surface energy enough to prevent stiction during a conventional wet release."

**Misuse note.** Generalists reach for "coating" language and assume thicker or more coating is more protective. A SAM is deliberately monomolecular; its function is to change surface energy, not to add bulk thickness, and the fallback order (OTS, then FDTS, then DDMS) trades hydrophobicity against process compatibility — treating them as interchangeable "extra coating" options skips that tradeoff.
