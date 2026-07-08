# Molecular and Cellular Biologist — Playbook

## qPCR primer efficiency validation (standard curve)

Run a 5-point, 5-fold serial dilution of template (pooled cDNA) in triplicate; plot Ct vs. log10(relative dilution).

| Dilution (relative) | log10(dilution) | Ct (mean of triplicate) |
|---|---|---|
| 1 | 0 | 19.8 |
| 1/5 | −0.699 | 22.1 |
| 1/25 | −1.398 | 24.5 |
| 1/125 | −2.097 | 26.9 |
| 1/625 | −2.796 | 29.3 |

Linear regression: slope = −3.405, R² = 0.999. Efficiency E = 10^(−1/slope) − 1 = 10^(0.294) − 1 = 0.967 → **96.7% efficiency.**

- Acceptable range: slope −3.10 to −3.58 (90–110% efficiency). This primer pair passes — use the simple 2^−ΔΔCt formula.
- Outside that range: use the Pfaffl formula instead — ratio = (E_target)^ΔCt_target(control−sample) / (E_ref)^ΔCt_ref(control−sample) — plugging in each primer pair's own measured efficiency rather than assuming 2.0 (100%) for both.
- Re-validate efficiency whenever primer lot, master mix, or template source (cDNA synthesis kit) changes — efficiency is a property of the specific reaction, not just the primer sequence.

## Cell culture doubling-time and seeding-density worksheet

**Step 1 — measure doubling time from a growth-curve pilot.** Seed a T25 flask at N0 = 2.0×10⁵ cells; count at t=48h: Nf = 1.28×10⁶ cells.

Doubling time: Td = t × ln(2) / ln(Nf/N0) = 48 × 0.6931 / ln(6.4) = 33.27 / 1.856 = **17.9 hours.**

**Step 2 — back-calculate seeding density for a target confluence at a target time.** Next experiment needs cells at ~60% confluence (≈1.2×10⁶ cells in a T25, given a typical max of ~2.0×10⁶ cells/T25 at full confluence for this line) at exactly 72h, to stay in log-phase growth for a synchronized treatment start.

Number of doublings in 72h at Td=17.9h: 72 / 17.9 = 4.02 doublings. Growth factor = 2^4.02 = 16.2.

Required seeding density: N0 = target / growth factor = 1.2×10⁶ / 16.2 = **7.4×10⁴ cells** (per T25, at this line's measured doubling time).

- Re-measure Td after any passage-number jump, media lot change, or supplement change — doubling time drifts with both passage-related senescence and lot-to-lot serum variability, and a stale Td silently over- or under-seeds every downstream experiment.
- Flag if actual confluence at the target timepoint is off by >15% from the calculated target — recheck Td rather than adjusting seeding density empirically next time, since a wrong Td will keep producing wrong seeding calculations.

## Multi-group ANOVA and post-hoc table (dose-response viability assay)

Four-group dose-response, relative viability (% of untreated control), n=4 independent wells (biological replicates: separate plates seeded on separate days) per group.

| Group | Rep 1 | Rep 2 | Rep 3 | Rep 4 | Mean | SD |
|---|---|---|---|---|---|---|
| Control | 100 | 98 | 102 | 101 | 100.25 | 1.71 |
| Low dose | 92 | 90 | 94 | 91 | 91.75 | 1.71 |
| Med dose | 68 | 71 | 65 | 70 | 68.50 | 2.65 |
| High dose | 40 | 38 | 43 | 41 | 40.50 | 2.16 |

One-way ANOVA (computed in Prism/R, not hand-derived — standard practice for this test): F(3,12) = 214.7, p < 0.0001.

Tukey post-hoc pairwise comparisons:

| Comparison | Mean difference | Adjusted p |
|---|---|---|
| Control vs. Low | 8.50 | 0.0021 |
| Control vs. Med | 31.75 | <0.0001 |
| Control vs. High | 59.75 | <0.0001 |
| Low vs. Med | 23.25 | <0.0001 |
| Low vs. High | 51.25 | <0.0001 |
| Med vs. High | 28.00 | 0.0003 |

- Rule: with 4 groups there are 6 pairwise comparisons — running 6 separate unpaired t-tests at raw α=0.05 gives a family-wise error rate of 1−0.95⁶ ≈ 26%, not 5%. ANOVA + Tukey holds the family-wise rate at 5%.
- Dunnett's test (not shown) is the right substitute when the only comparisons of interest are each dose vs. control, not all pairwise combinations — it's less conservative than Tukey for that narrower question.
