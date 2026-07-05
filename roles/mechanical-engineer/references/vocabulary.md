# Mechanical design working vocabulary

Terms a design/stress engineer uses daily and precisely. Format: definition → how a practitioner says it → common misuse.

**Stress concentration factor (Kt)** — A geometry-only multiplier (from Peterson's charts or FEA) relating the theoretical peak elastic stress at a notch, fillet, or hole to the nominal section stress, assuming linear-elastic material with no notch-sensitivity correction.
**In use:** "Kt comes out to 2.1 for this shoulder fillet at D/d = 1.67, r/d = 0.083 — that's before any notch-sensitivity discount for fatigue."
**Misuse:** applying Kt directly to a fatigue calculation as if it were the fatigue notch factor — Kt is a static, geometry-only number; using it un-discounted overstates the fatigue penalty and can mask that the notch-sensitivity step was skipped entirely.

**Fatigue notch factor (Kf)** — The stress concentration factor actually experienced in fatigue, discounted from Kt by the material's notch sensitivity q: Kf = 1 + q(Kt − 1).
**In use:** "Kf is 1.88 here, not the full Kt of 2.1 — this material's notch sensitivity at that radius is 0.80."
**Misuse:** treating Kf and Kt as interchangeable, or omitting q entirely and calling the raw Kt the fatigue factor.

**Notch sensitivity (q)** — A material- and radius-dependent value (0 to 1) describing how much of the theoretical stress concentration a real material actually experiences in fatigue; harder, higher-strength materials and smaller radii generally have higher q.
**In use:** "q is 0.80 for 4140 at this radius — softer materials or larger radii would pull that down and reduce the fatigue penalty."
**Misuse:** assuming q = 1 (full Kt applies) or q = 0 (no notch effect) by default instead of reading it off the material/radius-specific chart — both defaults are wrong in different directions.

**Endurance limit (Se) vs. rotating-beam endurance limit (Se′)** — Se′ is the baseline fatigue strength measured on an idealized polished rotating-beam specimen; Se is that value corrected by the Marin factors (surface finish, size, load type, temperature, reliability) for the actual part.
**In use:** "Se′ is 47,500 psi for this steel, but after surface and size corrections, the part's actual Se is 25,740 psi — that's the number that goes into the Goodman check."
**Misuse:** using the textbook Se′ value directly in a part-specific fatigue calculation without applying the Marin correction factors, which overstates the part's real fatigue strength.

**Modified Goodman diagram** — A linear failure criterion combining mean stress (σm) and alternating stress (σa) into a single fatigue safety check: σa/Se + σm/Su ≤ 1/FS, more permissive than the more conservative Soderberg line (which uses Sy instead of Su).
**In use:** "Goodman sum comes out to 0.742, so FS_fatigue is 1.35 — below the 2.5 target for this load case."
**Misuse:** running only a pure-alternating-stress fatigue check (σa vs. Se) and ignoring mean stress, which is invalid for any load case that isn't fully reversed (R = −1) — this bracket's R = 0 pulsating load has significant mean stress that Goodman must account for.

**Factor of safety (FS)** — The ratio of a limiting stress or load (yield, ultimate, or fatigue-corrected endurance) to the actual applied value; always meaningless without stating which limit it's computed against.
**In use:** "FS_fatigue is 1.35 against the Goodman-corrected endurance limit — that's separate from the FS = 1.79 on static yield."
**Misuse:** quoting a bare "FS = 2" without naming the denominator (yield, ultimate, or fatigue limit) — the same part can have three different FS values depending which failure mode is being checked, and an unqualified number hides which one.

**Mesh convergence** — Confirmation that a finite element result (typically peak stress at a feature of interest) stabilizes as mesh density increases, rather than continuing to climb — the check that separates a real stress prediction from a mesh artifact.
**In use:** "Peak stress moved less than 3% between the second and third refinement — that's converged; trust the number."
**Misuse:** accepting a single-mesh-density FEA result at a stress concentrator without a refinement study, especially at sharp corners where an unconverged (or truly singular) result will keep climbing indefinitely and never represents a real physical stress.

**Worst-case tolerance stack-up** — Summing the absolute value of every tolerance in a dimensional chain to find the guaranteed bound on total variation, regardless of the statistical likelihood of every part landing at its tolerance extreme simultaneously.
**In use:** "Worst-case gives us ±0.0047 in — that's the number we design the clearance against since this is a safety-critical, short 4-part stack."
**Misuse:** defaulting to worst-case for every stack regardless of part count or criticality, which over-tightens individual tolerances and inflates cost on long, non-critical assembly chains where RSS is the appropriate method.

**RSS (root-sum-square) tolerance stack-up** — A statistical stack-up method that takes the square root of the sum of squared tolerances, assuming each contributing dimension is independent and normally distributed — produces a tighter (less conservative) total than worst-case.
**In use:** "RSS gives ±0.00317 in versus worst-case's ±0.0047 — appropriate here since we've got six independent high-volume parts in this chain, none of them safety-critical alone."
**Misuse:** applying RSS to a short stack (2–3 parts) or a safety/interference-critical dimension, where the independence and large-sample assumptions underlying RSS don't hold and understate real risk.

**Design for manufacturability (DFM)** — The practice of designing a part's geometry, tolerances, and material to match the capability and cost structure of the actual manufacturing process, evaluated during design rather than after release.
**In use:** "DFM review at the CAD stage caught the 0.020 in internal corner before it became an EDM line item at quote."
**Misuse:** treating DFM as a final sign-off checklist run after the design is CAD-complete and quoted, instead of a constraint applied from the first concept review — by quote time, fixing a DFM issue means a re-quote, not a model tweak.

**Buckling (Euler/Johnson)** — Elastic (Euler, long/slender members) or inelastic (Johnson, intermediate slenderness) instability failure of a member in compression, occurring at a stress that can be well below the material's yield strength depending on slenderness ratio.
**In use:** "Slenderness ratio puts this strut in the Johnson region — Euler alone would understate the buckling load here."
**Misuse:** checking only yield strength on a slender compression member and skipping the buckling calculation entirely, missing a failure mode that can govern at a fraction of the yield-limited load.

**Specific strength** — A material's strength divided by its density (strength-to-weight ratio), the relevant comparison metric when a design is mass-constrained rather than volume-constrained.
**In use:** "Titanium wins on specific strength here, but 6061-T6's machinability and cost make it the right call unless mass is actually the binding constraint."
**Misuse:** comparing materials on raw yield or ultimate strength alone in a mass-constrained application, ignoring that a denser material can have higher absolute strength but lower strength-per-unit-mass.

**Machinability (machinability rating/index)** — A comparative measure (often referenced to a baseline material, e.g. AISI 1212 steel = 100%) of how easily a material can be cut — affects tool wear, cycle time, and achievable surface finish, independent of the material's strength.
**In use:** "That alloy's machinability index is half of 6061's — the strength gain doesn't pay for the doubled cycle time at this volume."
**Misuse:** selecting a material purely on mechanical-property tables without checking its machinability rating, then discovering the cost driver was cycle time, not raw material price.
