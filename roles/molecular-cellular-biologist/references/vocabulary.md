# Molecular and Cellular Biologist — Vocabulary

### ΔΔCt (delta-delta Ct)
The relative-quantification method comparing a target gene's Ct (cycle threshold) to a reference gene's Ct, in a treated sample vs. a control, converted to fold-change via 2^−ΔΔCt.
**In use:** "ΔΔCt gave us a 3.43-cycle shift, which is a 90.7% knockdown once you convert with 2^−ΔΔCt."
**Common misuse:** applied without checking the primer pair's amplification efficiency is near 100% (slope −3.10 to −3.58) — 2^−ΔΔCt silently assumes perfect doubling each cycle, and a primer pair outside that range needs the Pfaffl efficiency-corrected formula instead.

### Reference gene / endogenous control
A gene assumed to have stable expression across the experimental conditions being compared, used to normalize target-gene Ct values for input amount and reaction efficiency.
**In use:** "We validated GAPDH as stable under this transfection protocol before using it to normalize the PLK1 knockdown data."
**Common misuse:** chosen by lab tradition (always GAPDH or ACTB) without confirming stability under the specific perturbation being tested — some treatments (metabolic, hypoxic, stress) measurably shift "housekeeping" gene expression.

### Primer efficiency
The percentage by which template amount doubles each qPCR cycle for a specific primer pair, determined from the slope of a Ct-vs-log(dilution) standard curve; 100% efficiency corresponds to a slope of −3.32.
**In use:** "This primer pair's efficiency came out to 96.7% from the standard curve — close enough to 100% that we didn't need the Pfaffl correction."
**Common misuse:** assumed to be 100% by default and never measured, especially for newly designed primers, when efficiency below ~90% or above ~110% meaningfully distorts the simple 2^−ΔΔCt fold-change.

### Biological replicate vs. technical replicate
A biological replicate is an independently generated sample (separate culture, animal, or transfection); a technical replicate is a repeated measurement on the same sample (repeat pipetting, repeat qPCR well).
**In use:** "We ran technical triplicates per sample to reduce pipetting noise, but the n for the t-test is 3 — the number of independent transfections."
**Common misuse:** technical replicates averaged and then treated as if they were independent biological n in a statistical test, artificially shrinking the apparent variance and inflating significance.

### Linear range (Western blot)
The band-intensity range within which signal is proportional to the amount of protein loaded, for a given antibody, substrate, and detection system; established empirically with a dilution series.
**In use:** "We ran a 4-point loading dilution first to confirm our samples fell inside this antibody's linear range before quantifying."
**Common misuse:** assumed to hold for any exposure that produces a visible band, when a band strong enough to see clearly is often already past the linear range and into saturation, compressing real differences between samples.

### Loading control
A protein (or total-protein stain) used to normalize Western blot band intensity for the amount of total protein loaded per lane.
**In use:** "We used a stain-free total-protein loading control rather than a single housekeeping-protein band, since total-protein normalization isn't thrown off by one protein's own expression changing under treatment."
**Common misuse:** imaged once per gel and assumed to correct for lane-to-lane loading variation, when uneven transfer within that same gel can still leave individual lanes miscalibrated relative to each other.

### Cohen's d (effect size)
A standardized measure of the difference between two group means, expressed in pooled-standard-deviation units; d>0.8 is conventionally "large," d~0.2 is "small."
**In use:** "The proliferation assay came back with d=4.55 — a huge effect, which is why n=3 already gave us >99% power."
**Common misuse:** ignored in favor of reporting only the p-value, when the same p-value can come from a huge effect at low n or a tiny effect at high n — the effect size, not the p-value alone, is what determines whether the result matters biologically.

### Statistical power
The probability of correctly detecting a true effect of a given size, given the sample size and significance threshold — commonly targeted at 80%.
**In use:** "We power-calculated from the pilot's d=4.55 and confirmed n=3 already clears 80% power comfortably — no need for a bigger confirmatory cohort here."
**Common misuse:** treated as something you either "have" or "don't have" independent of effect size, rather than a function of the specific effect size, variance, and n in play — the same n can be badly underpowered for a subtle effect and massively overpowered for a strong one.

### Doubling time
The time required for a proliferating cell population to double in number, calculated from paired cell counts and elapsed time: Td = t × ln(2) / ln(Nf/N0).
**In use:** "Doubling time came out to 17.9 hours from the pilot growth curve, so we back-calculated the seeding density needed to hit 60% confluence at 72h."
**Common misuse:** assumed constant across passage number and media lot without re-measurement, when doubling time drifts with both passage-related changes and serum/media lot variability.

### Passage number
The count of times a cell culture has been subcultured (split) since it was thawed from a frozen stock or originally isolated.
**In use:** "That growth-rate drift showed up right around passage 28 — worth checking whether this line's assay is still validated that high."
**Common misuse:** left unreported in methods and unmonitored during experiments, when high-passage cultures of many lines drift genetically and phenotypically from the original characterized stock.

### STR profiling (cell line authentication)
Short tandem repeat DNA profiling used to confirm a cell line's identity against a reference database, detecting misidentification or cross-contamination with another line.
**In use:** "We re-authenticated by STR profile after the six-month gap in use, before trusting any new data off this line."
**Common misuse:** treated as a one-time check done at line acquisition, when misidentification/cross-contamination can be introduced later (mislabeled cryovial, shared incubator contamination) and periodic re-authentication is the actual safeguard.

### Knockdown vs. knockout
Knockdown reduces gene product (mRNA or protein) expression without eliminating the genomic sequence (siRNA/shRNA); knockout eliminates or disrupts the genomic sequence itself (CRISPR-Cas9), typically eliminating the product entirely if editing is complete.
**In use:** "siRNA gave us a 90% knockdown, which was enough to see the phenotype — we didn't need to go to a full CRISPR knockout for this question."
**Common misuse:** used interchangeably in casual conversation, when the distinction matters for interpretation — a partial knockdown leaving 10% residual expression can still support enough function to mask a phenotype that a true null (knockout) would reveal.

### TIDE / indel analysis
Tracking of Indels by DEcomposition — a method for quantifying and characterizing insertion/deletion mutations at a CRISPR target site from Sanger sequencing traces, used to confirm genomic editing.
**In use:** "TIDE showed 88% of alleles carrying a frameshift indel at the cut site, consistent with the near-complete protein loss we saw by Western."
**Common misuse:** used as the sole confirmation of a functional knockout, when an in-frame (multiple-of-3) indel can preserve a functional, just slightly altered, protein — genomic edit confirmation and protein-loss confirmation answer different questions and both are needed.

### Confluence
The percentage of a culture vessel's growth surface covered by adherent cells, used as a proxy for cell density and growth phase.
**In use:** "We seeded to hit 60% confluence at 72h, keeping cells in log-phase growth through the treatment window rather than letting them approach contact inhibition."
**Common misuse:** treated as a fixed target regardless of assay purpose, when different assays need different confluence windows — a proliferation assay needs log-phase (well below 100%), while some differentiation assays deliberately require near-confluent seeding.

### Post-hoc correction (Tukey, Dunnett, Bonferroni)
A statistical adjustment applied after an ANOVA to control the family-wise false-positive rate across multiple pairwise comparisons.
**In use:** "With 4 groups and 6 pairwise comparisons, we ran Tukey's post-hoc test rather than 6 separate t-tests, which would have pushed the true error rate to about 26%."
**Common misuse:** skipped in favor of running separate t-tests "because it's simpler," without accounting for how quickly the family-wise error rate compounds as the number of comparisons grows.
