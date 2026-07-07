# Biochemist — Vocabulary

### Km (Michaelis constant)
The substrate concentration at which reaction velocity is half of Vmax; a measure of the enzyme's apparent affinity for substrate under the assay conditions (not a true thermodynamic binding constant).
**In use:** "The Km shifted from 48 to 290 µM across the inhibitor titration, with Vmax unchanged — that's the competitive signature."
**Common misuse:** treated as a fixed physical constant of the enzyme, when it's actually assay-condition-dependent (pH, temperature, ionic strength all shift it) and can change if the active-enzyme concentration used to fit it was wrong.

### Vmax
The maximum reaction velocity at saturating substrate concentration, proportional to active enzyme concentration.
**In use:** "Vmax stayed flat at ~24 µM/min across all four inhibitor concentrations, which rules out noncompetitive or uncompetitive inhibition."
**Common misuse:** reported without normalizing to active enzyme concentration, making it impossible to compare Vmax across preps with different active fractions.

### Kd (dissociation constant)
The equilibrium constant for a binding interaction, equal to the ligand concentration at which half the binding sites are occupied; lower Kd means tighter binding.
**In use:** "SPR gave a Kd of 12 nM, but we confirmed it by ITC before committing the program to this lead."
**Common misuse:** confused with Ki (an inhibition constant specific to enzyme kinetics) or IC50 (a functional potency measure that depends on assay conditions) — the three are related but not interchangeable.

### Ki (inhibition constant)
The dissociation constant specifically for an inhibitor binding to an enzyme, derived from a full kinetics dataset (not a single IC50).
**In use:** "The secondary replot of apparent Km versus inhibitor concentration was linear, giving a Ki of 187 nM from the slope."
**Common misuse:** used interchangeably with IC50, when IC50 is assay-condition-dependent (varies with substrate concentration for a competitive inhibitor) while Ki is a fixed property of the inhibitor-enzyme pair.

### Active-site titration
A method for determining the concentration of catalytically active enzyme (as opposed to total protein), typically using a stoichiometric irreversible inhibitor or a burst-kinetics assay.
**In use:** "A280 said 3.4 µM total protein, but active-site titration showed only 2.1 µM was actually active — a 62% active fraction."
**Common misuse:** skipped entirely in favor of total protein concentration by A280 or Bradford assay, silently biasing every downstream kinetic constant.

### Competitive inhibition
An inhibition mechanism where the inhibitor competes with substrate for the same binding site; raises apparent Km, leaves Vmax unchanged, because enough substrate can always outcompete the inhibitor.
**In use:** "Vmax was flat and Km rose 6-fold across the inhibitor range — textbook competitive inhibition."
**Common misuse:** inferred from a docking pose or binding-site overlap prediction alone, without the kinetic data (Km/Vmax shift pattern) that's the actual evidence for mechanism.

### Noncompetitive inhibition
An inhibition mechanism where the inhibitor binds a site distinct from the substrate site and doesn't block substrate binding; lowers Vmax, leaves Km unchanged (in the simple/pure case).
**In use:** "Km stayed at 50 µM but Vmax dropped from 24 to 8 µM/min across the titration — that's noncompetitive, not competitive."
**Common misuse:** used as a catch-all for "not competitive" when the actual pattern (both Km and Vmax shifting) indicates mixed inhibition, a distinct mechanism.

### Peak-purity / structural resolution
In structural biology, the level of detail (in Ångströms) at which atomic positions can be distinguished; lower numbers mean higher resolution.
**In use:** "The cryo-EM map resolved to 3.2 Å, enough to place side chains but not to resolve bound-water positions with confidence."
**Common misuse:** treated as a single number describing the whole structure, when resolution is often anisotropic (better in a rigid core, worse in a flexible loop or domain) and the worst-resolved region is where interpretation risk concentrates.

### Orthogonal confirmation
Verifying a result (binding affinity, structure, purity) using a second method based on a different physical principle, so the two methods don't share the same blind spot or artifact.
**In use:** "We don't advance a Kd to a go/no-go decision on SPR alone — ITC confirmation is required first."
**Common misuse:** satisfied by running the same method twice (e.g., two SPR runs) rather than a genuinely different physical principle — same-principle replication catches random error, not systematic artifact.

### Size-exclusion chromatography (SEC) / SEC-MALS
A chromatography method separating molecules by size; SEC-MALS pairs it with multi-angle light scattering to give an absolute molecular weight and detect aggregation or oligomeric state.
**In use:** "SEC-MALS showed the target running as a stable dimer at 84 kDa, which ruled out cryo-EM as premature — not enough mass for routine resolution yet."
**Common misuse:** SEC retention volume alone (without MALS) used to estimate molecular weight, when retention volume depends on shape as well as mass and can be misleading for non-globular proteins.

### Isothermal titration calorimetry (ITC)
A label-free binding-assay method measuring the heat released or absorbed during a binding interaction, giving Kd, stoichiometry, and the enthalpic/entropic decomposition of binding in one experiment.
**In use:** "ITC confirmed the SPR-derived Kd within 2-fold and showed the binding is entropy-driven, which changes the med-chem optimization strategy."
**Common misuse:** run at only one temperature and treated as fully characterizing the thermodynamics, when enthalpy/entropy decomposition from a single-temperature ITC run can be confounded by linked protonation events unless checked with a buffer-ionization control.

### Burst kinetics
A pre-steady-state kinetics method that reveals a fast initial "burst" phase distinct from steady-state turnover, often used to determine active enzyme concentration or identify a rate-limiting step.
**In use:** "The burst-phase amplitude gave us the active-site concentration directly, without needing a separate titration."
**Common misuse:** conflated with steady-state kinetics; a burst-phase experiment requires fast time-resolution (stopped-flow or quench-flow) that a standard steady-state assay setup can't capture.

### Specific activity
Enzyme activity (e.g., µmol substrate converted per minute) normalized to the amount of protein present, typically reported as units per milligram.
**In use:** "Specific activity dropped from 45 to 12 U/mg after the freeze-thaw cycle — that's activity loss, not a change in the enzyme's intrinsic properties."
**Common misuse:** compared across preps without confirming both were normalized to active (not total) protein concentration, making an apparent activity change actually reflect a change in active fraction.

### Cryo-EM particle classification
Computational sorting of individual cryo-EM particle images into distinct 2D or 3D classes, used to separate genuine structural/conformational heterogeneity from noise or damaged particles.
**In use:** "3D classification split the dataset into two conformational states — the apo and substrate-bound forms were both present in the same grid."
**Common misuse:** treated as a purely technical cleanup step, when classification results are themselves biological data (revealing conformational heterogeneity) that can get discarded if the analyst only keeps the "best" class without examining what the discarded classes represent.
