# Biochemist — Playbook

## Michaelis-Menten kinetics fit worksheet

| Step | Action | Threshold / check |
|---|---|---|
| 1. Prep QC | SDS-PAGE + A280/Bradford total protein, active-site titration (burst kinetics or stoichiometric inhibitor titration) | Report active enzyme concentration, not total protein, if active fraction <90% |
| 2. Substrate range | Run initial rates across at least 6 [S] points spanning 0.2x-5x expected Km | Include at least 2 points above 3x Km to constrain Vmax |
| 3. Initial-rate window | Measure only the linear portion of the progress curve (<10% substrate consumed) | Nonlinear progress curve → shorten timepoints or dilute enzyme |
| 4. Replicates | n≥3 independent preps (not just technical triplicate of one prep) for any reported Km/Vmax | Technical replicates alone understate true variability |
| 5. Fit | Nonlinear regression to v = Vmax[S]/(Km+[S]), not a Lineweaver-Burk linear fit for the primary estimate | Lineweaver-Burk weights low-[S]/high-error points most heavily; use for visualization only |
| 6. Inhibitor panel | Repeat steps 2-5 at 3-4 inhibitor concentrations spanning below and above expected Ki | Fewer than 3 inhibitor levels cannot distinguish mechanism from a single Km/Vmax shift |
| 7. Mechanism call | Plot apparent Km and Vmax vs. [I]; competitive = Km rises, Vmax flat; noncompetitive = Vmax falls, Km flat; uncompetitive = both fall proportionally; mixed = both shift non-proportionally | Secondary replot (apparent Km vs [I]) R² <0.95 → suspect mixed mechanism, not simple competitive |

## Structural-method selection table

| Factor | X-ray crystallography | Cryo-EM | NMR |
|---|---|---|---|
| Typical size range | No strict lower limit if it crystallizes; upper limit set by crystal quality, not MW | Historically ≥150-200 kDa for routine near-atomic resolution; extension methods (fiducial markers, smaller-particle optimization) push lower | Practical ceiling ~40-50 kDa without deuteration/TROSY; larger with those techniques |
| Sample requirement | Milligrams, must form ordered 3D crystal | Micrograms-to-low-milligrams, needs particle homogeneity, no crystal required | Milligrams, needs high solubility and stability over multi-day acquisition |
| Best for | Single well-ordered conformation, near-atomic detail, high-throughput ligand soaking (fragment screening) | Large complexes, membrane proteins in nanodiscs, conformationally heterogeneous assemblies (multiple states from one dataset via classification) | Solution-state dynamics, disordered regions, weak/transient interactions, small domains |
| Blind spot | Crystal packing can distort a genuinely flexible interface; won't form ordered crystal at all if flexible | Resolution for small/asymmetric targets still often lower than crystallography; preferred-orientation artifacts | Signal overlap and linewidth broadening scale badly with size; aggregation-prone samples fail |
| Timeline (rough) | Weeks-months (crystallization screening is the bottleneck) | Days-weeks once grids are optimized (grid optimization itself can take weeks) | Weeks (assignment) to months (full structure) |

Decision rule: start from sample properties (size, flexibility, quantity available), not lab default equipment. A target that has resisted crystallization for >6 months of screening is a candidate to re-route to cryo-EM or NMR rather than continuing indefinitely.

## Purification step yield/purity tracking template

| Step | Volume (mL) | Total protein (mg) | Purity (%, by densitometry) | Yield vs. prior step | Cumulative yield vs. lysate |
|---|---|---|---|---|---|
| Clarified lysate | 120 | 840 | 8% | — | 100% |
| Affinity capture (His-tag Ni-NTA) | 15 | 210 | 65% | 25.0% | 25.0% |
| Ion-exchange polish | 8 | 142 | 92% | 67.6% | 16.9% |
| Size-exclusion (final) | 4 | 98 | 99% | 69.0% | 11.7% |

Reconciliation check: cumulative yield (11.7%) should be consistent with the product of per-step yields (0.25 × 0.676 × 0.690 = 0.117). A mismatch signals a measurement error (e.g., a concentration reading taken before vs. after a concentrator step) — recheck before reporting.

Stopping-point rule: for a kinetics assay tolerant of 90-95% purity, stop after ion-exchange (92% purity, 16.9% cumulative yield) rather than running the size-exclusion polish, which costs another ~31% of remaining material for a purity gain the assay doesn't need.
