# Vocabulary

### E-value
The expected number of alignments with a score at least as good as the observed one, occurring by chance alone given the database size searched.
**In use:** "It's a 620-bit hit at E = 2e-176 against nr — that's not going to be chance."
**Common misuse:** Treating E-value as a universal significance threshold (like a p-value) that's comparable across searches, when it scales with database size and query length — the same bit score against a 500-sequence custom panel and against nr produces very different E-values.

### Phred quality score (Q)
A logarithmic measure of base-call error probability: Q = −10·log₁₀(P_error). Q30 means 1-in-1000 chance the base call is wrong.
**In use:** "We're filtering anything below Q20 pre-alignment and reporting %≥Q30 as the run-level QC metric."
**Common misuse:** Confusing base quality (confidence in one nucleotide read) with genotype quality (confidence in the called diploid or somatic genotype, which also depends on depth, mapping quality, and a population prior).

### Genotype likelihood
The probability of the observed sequencing reads given each possible genotype, combined with a prior to produce a posterior genotype call — the statistical core of Bayesian variant callers like GATK HaplotypeCaller.
**In use:** "GQ is only 12 at this locus — the genotype likelihood model isn't confident even though the VAF looks like a clean het."
**Common misuse:** Calling a variant "present" from raw read support (alt reads > 0) without running it through the genotype-likelihood model, which is what actually distinguishes a real call from sequencing noise at low depth.

### Variant allele frequency (VAF)
The fraction of sequencing reads at a position that support the alternate (non-reference) allele.
**In use:** "VAF is 37.5% at 400x depth — at roughly 2×VAF for tumor cellularity, that's consistent with ~75% purity for a het locus."
**Common misuse:** Reading VAF alone as a confidence measure — the same VAF at 8x and 400x depth carry very different statistical certainty, and VAF needs a purity/ploidy model to interpret in a somatic (non-diploid) context.

### False discovery rate (FDR) / Benjamini-Hochberg (BH) correction
A multiple-testing correction that controls the expected proportion of false positives among all features called significant, rather than the probability of any single false positive (family-wise error rate, which Bonferroni controls).
**In use:** "At q<0.05 across 20,000 genes, only 2 survive — the rest looked good at raw p<0.001 but that's within the noise a 20,000-test screen produces."
**Common misuse:** Reporting a "BH-corrected p-value" (a q-value) as if it retains the same interpretation as a raw p-value, or applying Bonferroni by default in exploratory genomics work where it's needlessly conservative.

### Q-value
The BH-adjusted p-value: the minimum FDR at which a given feature would be called significant. Computed as q(i) = p(i)·m/i, monotonized across the ranked list.
**In use:** "MMP9's q-value is 0.041 — it clears q<0.05, but just barely."
**Common misuse:** Treating q-value and raw p-value as interchangeable in a report; they answer different questions (expected false-positive proportion in the significant set vs. probability of this one result under the null).

### Coverage / depth
The number of sequencing reads overlapping a given genomic position, or the genome-wide average of that count (mean coverage, C = N·L/G, Lander-Waterman).
**In use:** "We're targeting 30x mean coverage for germline WGS, but the actual QC gate is the fraction of the genome at ≥20x, not the mean."
**Common misuse:** Reporting mean coverage alone as sufficient QC, when the distribution (uniformity, GC-bias pattern) determines whether low-coverage regions are a real problem.

### Log2 fold change (log2FC)
The base-2 logarithm of the ratio of normalized expression between two conditions; log2FC = 1 is a 2-fold change, log2FC = -1 is a 2-fold decrease.
**In use:** "It's |log2FC| > 1 and q < 0.05, jointly — either alone isn't the bar we report on."
**Common misuse:** Treating a large fold change as automatically meaningful without checking statistical significance, especially at low expression levels where fold change is noisy (a gene going from 2 to 8 counts is an easy 4-fold change with almost no statistical support).

### Negative binomial model
The count distribution used for RNA-seq read counts (DESeq2, edgeR), which allows variance to exceed the mean (overdispersion) unlike a Poisson model.
**In use:** "Dispersion is shrunk across genes via empirical Bayes before the Wald test runs — that's what stabilizes single-gene estimates at n=6."
**Common misuse:** Assuming RNA-seq counts are Poisson-distributed (variance = mean), which understates true variance and produces overconfident p-values — this is exactly the failure mode DESeq2/edgeR's negative-binomial model with dispersion shrinkage corrects.

### Batch effect
A systematic, non-biological source of variation introduced by processing samples in different technical groups (sequencing run, reagent lot, extraction date).
**In use:** "PCA shows samples separating by sequencing run, not by condition — that's a batch effect, and it's confounded with our case/control split."
**Common misuse:** Assuming any batch effect is correctable post-hoc with a covariate or ComBat; if batch and the biological variable are perfectly correlated, there's no statistical fix.

### Mapping quality (MAPQ)
A phred-scaled confidence score for how uniquely a read aligns to a specific genomic location, distinct from base quality.
**In use:** "MAPQ0 reads at this locus mean it's multi-mapping — pull the segmental-duplication track before calling a variant here."
**Common misuse:** Conflating MAPQ (alignment location confidence) with base quality (individual nucleotide confidence) — a read can have perfect base quality and still be unreliable because it maps equally well to five places in the genome.

### Linkage disequilibrium (LD)
The non-random association between alleles at different loci, such that genotypes at nearby SNPs are correlated rather than independent.
**In use:** "We LD-clumped at r²>0.1 within 500kb before counting independent lead SNPs — otherwise we'd be counting one signal five times."
**Common misuse:** Treating each genome-wide-significant SNP in a GWAS output as an independent discovery, when several may be tagging the same underlying causal variant through LD.

### N50
A sequence-assembly statistic: the contig/scaffold length at which 50% of the total assembly length is contained in contigs of that length or longer.
**In use:** "N50 jumped from 12kb to 340kb after switching to long-read assembly — that's a real improvement in contiguity, not just more sequence."
**Common misuse:** Treating N50 as a proxy for assembly correctness or completeness; a high N50 assembly can still be riddled with misassemblies, and N50 says nothing about accuracy.

### k-mer
A substring of length k extracted from a sequencing read, used as the unit of comparison in fast alignment-free tools (taxonomic classifiers, assemblers, some aligners).
**In use:** "Classification confidence at the species level depends on how many species in this genus share the same k-mers — it's not just about the classifier's score."
**Common misuse:** Assuming k-mer-based classification confidence is purely a property of the read, when it's bounded by how distinguishable the reference database's sequences are at that k.
