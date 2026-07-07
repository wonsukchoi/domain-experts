# Artifacts

Filled skeletons. Populate bracketed fields; structure and thresholds are the reusable part.

## Statistical Analysis Plan (SAP) skeleton

```
Study: [name]
Primary hypothesis: [treatment] increases/decreases [outcome] by at least [MDE] relative to [control], from a baseline of [X%/units].
Design: [randomized / observational], [arms], unit of randomization = [user/session/patient/cluster].
Sample size: [N] per arm ([total]), power [80%/90%], α=[0.05] [one/two]-sided.
  Justification: computed for detecting a shift from [baseline] to [baseline + MDE] using [test name, e.g. two-proportion z-test].
Duration: fixed at [N days] at current [traffic/enrollment rate].
Interim analysis: [none / group sequential with O'Brien-Fleming boundary at looks: day X (α=Y), day Z (final α=W)].
Primary analysis: [test name] on the full pre-specified sample at [endpoint time].
Secondary/exploratory analyses: [list], explicitly labeled exploratory, [correction method] applied if >1 comparison.
Missing data handling: [complete case / multiple imputation], sensitivity analysis under [alternative assumption].
Reporting: point estimate + [95%] CI required in every readout; p-value alone is insufficient.
```

## Sample-size calculation worksheet (two-proportion comparison)

```
Baseline rate (p1): [___]
Target rate (p2): [___]  (= p1 × (1 + relative MDE) or p1 + absolute MDE)
Absolute difference (Δ): [p2 - p1]
Power: [0.80 / 0.90]
α (two-sided): [0.05]
Approx. per-arm n (z-test, α=0.05, power=0.80): n ≈ 16 × p̄(1-p̄) / Δ²   where p̄ = (p1+p2)/2
  [worked value]
Current traffic/enrollment: [N per day, split across arms]
Days to reach required n: [per-arm n ÷ per-arm daily rate]
Decision if timeline exceeds budget: [reduce MDE requested / extend duration / reject as underpowered — do not silently ship at whatever n is convenient]
```

## Missing-data sensitivity report skeleton

```
Outcome variable: [name]
% missing on primary outcome: [X%]
Missingness mechanism assumed for primary analysis: [MCAR / MAR / MNAR — state and justify]
Primary estimate (complete case): [effect size, 95% CI]
Sensitivity estimate (multiple imputation, m=[N] imputations, method=[e.g. predictive mean matching]): [effect size, 95% CI]
Sensitivity estimate (pattern-mixture / tipping-point under MNAR assumption [delta value]): [effect size, 95% CI]
Conclusion: [does the effect direction/significance hold across all three estimates, or does the conclusion depend on the missingness assumption — state explicitly which]
```

## Multiple-comparisons correction decision table

| Number of tests | Correlation among tests | Recommended method | Note |
|---|---|---|---|
| 2–5 | Low/unknown | Bonferroni | Simple, acceptably conservative at this count |
| 6–20 | Low/unknown | Holm-Bonferroni | Less conservative than Bonferroni, same family-wise control |
| 20+ | Any | Benjamini-Hochberg (FDR) | Family-wise correction becomes too conservative; control false discovery rate instead |
| Any | High (correlated outcomes, e.g. repeated measures) | Permutation-based or FDR | Correlation violates independence assumption behind Bonferroni's bound |

## Alpha-spending boundary reference (O'Brien-Fleming, 2 looks, final α=0.05)

| Look | Information fraction | Nominal α at this look |
|---|---|---|
| Interim (1 of 2) | 0.50 | ≈0.0031 |
| Final (2 of 2) | 1.00 | ≈0.0480 |

Use a statistics package (e.g. R's `gsDesign`) to compute exact boundaries for the actual number and timing of looks — this table is illustrative, not a substitute for the calculation.
