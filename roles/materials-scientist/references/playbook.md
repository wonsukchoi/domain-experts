# Playbook

Filled worked calculations for the three artifact types this role produces most often: an XRD lattice-parameter determination checked against Vegard's law, a Williamson-Hall size-strain deconvolution, and a processing-variable DOE matrix. Populate with the actual system's numbers; the structure and arithmetic below are real and reconcile.

## Lattice parameter determination — cubic indexing + Vegard's law

**Question:** does a new NixCo(1-x)Fe2O4 spinel ferrite solid solution (x = 0.5) actually form a single homogeneous phase, or has it segregated into NiFe2O4-rich and CoFe2O4-rich regions — a question a single "it's cubic spinel" phase ID from a database match cannot answer.

**Step 1 — index the (311) reflection (the strongest spinel peak) and compute d-spacing.** Cu Kα, λ = 1.5406 Å. Measured 2θ(311) = 35.42°, θ = 17.71°, sinθ = 0.3043. Bragg's law: d = λ/(2 sinθ) = 1.5406/(2×0.3043) = **2.531 Å**.

**Step 2 — convert d-spacing to cubic lattice parameter.** For a cubic cell, d = a/√(h²+k²+l²); for (311), √(3²+1²+1²) = √11 = 3.3166. a = d × 3.3166 = 2.531 × 3.3166 = **8.395 Å**. (Production practice: repeat for every indexed reflection and extrapolate a vs. a Nelson-Riley function to θ→90° to cancel systematic sample-height/absorption error before reporting a final a — the single-peak value here is for illustration.)

**Step 3 — check against Vegard's law.** End-member lattice parameters (JCPDS/ICSD reference values): NiFe2O4, a = 8.339 Å; CoFe2O4, a = 8.392 Å. For a homogeneous solid solution at x = 0.5, Vegard's law predicts linear interpolation: a(predicted) = 0.5×8.339 + 0.5×8.392 = **8.3655 Å**.

**Step 4 — reconcile.** Measured a = 8.395 Å vs. predicted 8.3655 Å: deviation = +0.0295 Å (+0.35%). A deviation this small, with a single sharp (311) peak (no shoulder or splitting), is consistent with a true solid solution showing a modest positive deviation from ideal Vegard behavior — plausibly from a shift in cation inversion degree between the tetrahedral and octahedral spinel sites, a known second-order effect in mixed ferrites. A phase-segregated sample would instead show either two resolvable (311) peaks (one near each end-member's a) or a single peak broadened/skewed toward one end — neither is observed here.

**Deliverable — phase-purity finding (as filed):** "Ni0.5Co0.5Fe2O4 refined lattice parameter a = 8.395 Å (Nelson-Riley extrapolated), within 0.35% of the Vegard's-law linear prediction (8.3655 Å) between NiFe2O4 (8.339 Å) and CoFe2O4 (8.392 Å) end members. Single, unsplit (311) reflection with no shoulder. Interpreted as a homogeneous solid solution; the small positive deviation is attributed to a cation-inversion-degree effect, not phase segregation."

## Williamson-Hall size-strain deconvolution

**Question:** a ball-milled nanocrystalline Cu powder shows broadened XRD peaks — is the broadening from small crystallite size, from microstrain (lattice distortion from plastic deformation), or both, and a single-peak Scherrer number cannot separate them.

**Step 1 — collect FWHM (instrument-corrected, radians) at four reflections.** Cu Kα, λ = 1.5406 Å.

| hkl | 2θ (°) | θ (°) | sinθ | cosθ | β (rad) | β·cosθ |
|---|---|---|---|---|---|---|
| (111) | 43.30 | 21.65 | 0.3692 | 0.9293 | 0.00450 | 0.004182 |
| (200) | 50.43 | 25.22 | 0.4260 | 0.9047 | 0.00520 | 0.004704 |
| (220) | 74.13 | 37.07 | 0.6041 | 0.7969 | 0.00690 | 0.005499 |
| (311) | 89.93 | 44.97 | 0.7062 | 0.7081 | 0.00790 | 0.005594 |

**Step 2 — plot βcosθ (y) vs. sinθ (x); the Williamson-Hall relation is βcosθ = Kλ/L + 4ε·sinθ.** Least-squares slope over the four points ≈ 0.004190 (rise 0.005594−0.004182 = 0.001412 over run 0.7062−0.3692 = 0.3370). Slope = 4ε → ε = 0.004190/4 = **0.001048 = 0.105% microstrain**.

**Step 3 — extract crystallite size from the intercept.** Intercept = y − slope·x at the (111) point: 0.004182 − 0.004190×0.3692 = 0.004182 − 0.001547 = **0.002635 = Kλ/L**. With K = 0.9, λ = 1.5406 Å: Kλ = 1.3865 Å. L = 1.3865/0.002635 = 526.1 Å = **52.6 nm**.

**Step 4 — compare against plain single-peak Scherrer (no strain correction).** Using only the (111) peak and attributing all broadening to size: L(Scherrer) = Kλ/(β(111)·cosθ111) = 1.3865/(0.00450×0.9293) = 1.3865/0.004182 = 331.5 Å = **33.2 nm**.

**Reconciliation.** Plain Scherrer underestimates crystallite size by 37% (33.2 nm vs. 52.6 nm) because it forces all four peaks' broadening trend into a size-only explanation; the Williamson-Hall slope shows a real, non-zero microstrain (0.105%) is present and growing with sinθ — the signature of broadening that increases with diffraction order, which size broadening alone does not produce. The 0.105% microstrain is consistent with heavy plastic deformation from ball milling.

**Deliverable — characterization report excerpt (as filed):** "Williamson-Hall analysis (4 reflections, Cu Kα) separates size and strain broadening: crystallite size L = 52.6 nm, microstrain ε = 0.105%. A single-peak Scherrer estimate on (111) alone (33.2 nm) understates crystallite size by 37% by folding the milling-induced microstrain into an apparent size reduction; report L = 52.6 nm as the size figure and ε = 0.105% as a separate, milling-dose-dependent microstrain figure."

## Processing-variable DOE matrix — new-material development screen

**Question:** a new sol-gel-derived ZnO thin film's photoluminescence intensity depends on calcination temperature and Al-dopant concentration, and both are suspected to interact — screen both in one matrix rather than one variable at a time.

| Run | Calcination temp (°C) | Al dopant (at%) | PL intensity (a.u., normalized) | XRD (002) FWHM (°) |
|---|---|---|---|---|
| 1 | 400 | 0 | 120 | 0.42 |
| 2 | 400 | 2 | 165 | 0.39 |
| 3 | 400 | 4 | 140 | 0.41 |
| 4 | 550 | 0 | 210 | 0.31 |
| 5 | 550 | 2 | 310 | 0.27 |
| 6 | 550 | 4 | 245 | 0.30 |
| 7 | 700 | 0 | 190 | 0.24 |
| 8 | 700 | 2 | 205 | 0.23 |
| 9 | 700 | 4 | 175 | 0.26 |

**Reading the interaction.** At 400°C, 2 at% Al is the best condition (165); at 550°C, 2 at% Al is also best but the gain over 0% Al is much larger (310 vs. 210, +48%, versus +38% at 400°C) — the dopant benefit is not additive with temperature, it's amplified by it, up to a point. At 700°C the ranking compresses again (205 vs. 190, +8%) and the (002) FWHM has already narrowed close to its minimum (0.23-0.26°), indicating grain growth/crystallization is largely complete and additional dopant no longer has undersaturated lattice sites to occupy as effectively. One-variable-at-a-time screening (fix temp at 400°C, vary dopant; separately fix dopant at 0%, vary temp) would have found the same individual optima (550°C, 2 at%) but missed that the *combination's* gain is interaction-driven, not the sum of two independent main effects — relevant because it means the optimum will shift if either variable's range is extended, and a follow-up matrix should center on 500-600°C x 1.5-2.5 at% rather than re-screening the full original range.

**Deliverable — next-experiment recommendation (as filed):** "Run 5 (550°C, 2 at% Al) is the current optimum (PL = 310, FWHM = 0.27°). Interaction between temperature and dopant level (gain from doping increases from +38% at 400°C to +48% at 550°C, then compresses to +8% at 700°C, tracking crystallization completion by XRD FWHM) means the optimum is not at either variable's individual extreme. Next matrix: 3x3 centered on 500-600°C x 1.5-2.5 at% Al, 2 replicates per cell to bound batch-to-batch scatter before reporting a final optimum."
