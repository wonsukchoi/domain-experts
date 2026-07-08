# Bioinformatics scientist playbook

Filled worked calculations and threshold tables, not descriptions of them. Test: could an agent execute or populate this as-is.

## 1. Coverage planning (Lander-Waterman)

C = N·L/G, where N = number of reads, L = read length (bp), G = genome/target size (bp).

**Whole-genome sequencing, 30x target, human genome (G = 3.2 Gb), 150bp paired-end reads:**

- Required total bases = C × G = 30 × 3,200,000,000 = 96,000,000,000 bp.
- Reads needed = 96,000,000,000 / 150 = 640,000,000 reads = 320,000,000 read pairs.
- Sanity check at an actual run size: a NovaSeq X lane yielding 320,000,000 read pairs (640,000,000 reads × 150bp) gives 640,000,000 × 150 / 3,200,000,000 = **30x mean coverage** — confirms the forward calculation.

**Whole-exome sequencing, 100x target, exome target size 45 Mb, 100bp paired-end reads:**

- Required total bases = 100 × 45,000,000 = 4,500,000,000 bp.
- Reads needed = 4,500,000,000 / 100 = 45,000,000 reads = 22,500,000 read pairs.
- On-target rate matters: if only 70% of sequenced bases land in the capture target (typical hybrid-capture efficiency), the raw sequencing order must scale by 1/0.70 — order ≈ 32,150,000 read pairs, not 22,500,000, to hit 100x **on-target**.

**Reading a coverage distribution, not just the mean:** mean depth 30x with a flat histogram (most bases within 20-40x) indicates a clean, evenly-loaded library. Mean depth 30x with a bimodal histogram (a cluster near 5x and a cluster near 55x) indicates GC-bias or a capture-efficiency problem, not a loading-concentration problem — same headline number, different root cause, different fix (adjust PCR cycles/enzyme for GC bias vs. re-titrate library concentration).

## 2. BLAST/DIAMOND E-value interpretation

E-value = K·m·n·e^(−λS): expected number of chance alignments at score S or better, given database size n and query length m (K, λ are scoring-matrix-specific constants).

| Query length | Database | Bit score | E-value | Call |
|---|---|---|---|---|
| 350 aa | nr (~5e11 residues) | 620 | 2e-176 | near-certain orthology |
| 350 aa | nr | 95 | 3e-18 | reportable homology, confirm domain architecture |
| 350 aa | nr | 42 | 0.08 | not reportable — expected by chance at this database size |
| 30 aa (short peptide) | nr | 58 | 2e-3 | borderline — short-query E-values are inflated versus a full-length ortholog at the same % identity; corroborate with a conserved-domain (Pfam/InterPro) hit before calling homology |
| 350 aa | custom 500-sequence panel | 95 | 4e-22 | same bit score, much stronger E-value than against nr — E-value is search-space-dependent, bit score alone is not comparable across database sizes |

## 3. Variant confidence: phred quality, depth, and VAF

Phred-scaled base quality: Q = −10·log₁₀(P_error). Q20 = 1% error rate per base; Q30 = 0.1% error rate; Illumina NGS QC commonly filters below Q20 pre-alignment and reports %≥Q30 as a run-level metric (typical acceptance threshold ≥80% of bases at Q30 for a passing run).

Variant allele frequency (VAF) = alt-supporting reads / total reads at the position. Same VAF, different confidence by depth:

| Total depth | Alt reads | VAF | Genotype-likelihood read | Action |
|---|---|---|---|---|
| 8 | 3 | 37.5% | Wide credible interval (roughly 15-65% at 95% CI for n=8 binomial); consistent with true het (50%) or partial artifact | Do not call without depth ≥20x or orthogonal confirmation |
| 40 | 15 | 37.5% | Tight credible interval (roughly 27-49%); clearly inconsistent with a clean 50% het | Flag as possible subclonal/somatic signal or mapping artifact at this locus — check strand bias and mapping quality before reporting |
| 400 | 150 | 37.5% | Very tight interval (roughly 33-42%); reproducible signal | Somatic VAF consistent with ~75% cellularity at a heterozygous locus (2×VAF ≈ tumor cell fraction under a simple diploid model) — report with the caveat that purity/ploidy correction (e.g., FACETS, ASCAT) refines this further |

Genotype likelihood (GATK-style, simplified): for genotype G given read data D, P(G|D) ∝ P(D|G)·P(G), where P(D|G) is the product of per-read error-model probabilities conditioned on the assumed genotype and P(G) is the population-prior (Hardy-Weinberg for germline, tumor-purity-adjusted for somatic) — this is why two variants at identical VAF can carry different reported genotype quality (GQ) scores once depth, base quality, and mapping quality are folded in.

## 4. Differential expression / GWAS threshold sequence

**RNA-seq DE (DESeq2), standard sequence:**
1. Filter genes with count < 10 summed across all samples (removes untestable low-count genes before correction, reducing the effective m and improving power — DESeq2's independent filtering does this automatically via `results()`).
2. Fit negative-binomial GLM, shrink dispersion estimates across genes (empirical Bayes borrowing across the gene set stabilizes single-gene dispersion estimates at small n).
3. Wald test per gene against the null log2FC = 0 (or a specified non-zero threshold via `lfcThreshold` for a stricter test).
4. BH-FDR correct across the *filtered* gene count (post independent-filtering m), not the pre-filter total.
5. Threshold on q < 0.05 AND |log2FC| > 1 (2-fold) jointly — report the count passing both, not either alone.

**GWAS (PLINK/SAIGE), standard sequence:**
1. QC genotypes: call rate ≥95% per SNP, minor allele frequency ≥1% (common-variant GWAS) or a specified rarer cutoff with power caveats, Hardy-Weinberg equilibrium p>1e-6 in controls.
2. Check population stratification via PCA on genotypes; include top 5-10 PCs as covariates in the association model.
3. Fit mixed model (accounts for cryptic relatedness) or logistic regression for case-control.
4. Apply genome-wide significance threshold p < 5×10⁻⁸ (the standard Bonferroni-equivalent for ~1,000,000 independent common-variant tests in a European-ancestry panel — adjust the multiple-testing correction for admixed or multi-ancestry panels, where the effective number of independent tests changes).
5. LD-clump significant hits (r² > 0.1 within 500kb) to a set of independent lead SNPs before reporting a locus count.
