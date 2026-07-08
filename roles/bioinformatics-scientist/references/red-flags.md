# Red flags

### A hit list with more genes at raw p<0.05 than expected by chance under the number of tests run
- **Usually means:** the multiple-testing correction wasn't applied, or was applied to the wrong m (e.g. corrected against the number of *significant* genes rather than the number of genes *tested*).
- **First question:** "What's m in your correction — total genes tested, or genes passing an earlier filter?"
- **Data to pull:** the analysis script's correction call and the pre-filter gene/SNP count from the count matrix or VCF.

### Fold-change or p-value threshold chosen after seeing how many features clear it
- **Usually means:** threshold shopping — the cutoff was tuned to hit a target list size rather than set from a power calculation or a pre-registered design.
- **First question:** "Was this threshold decided before or after you looked at the ranked list?"
- **Data to pull:** the analysis notebook's commit history or the pre-analysis plan, if one exists.

### Coverage histogram is bimodal despite an acceptable mean depth (e.g., mean 30x but bimodal 5x/55x clusters)
- **Usually means:** GC bias in library prep or hybrid-capture, not a loading-concentration problem.
- **First question:** "Is the low-depth cluster correlated with GC content or with known repeat/capture-boundary regions?"
- **Data to pull:** per-region coverage plotted against local GC%, and the capture kit's target BED file.

### Variant allele frequency near 50% but genotype quality (GQ) below ~20 at depth under 15x
- **Usually means:** true heterozygote call at insufficient depth to be confident, or a mapping artifact (multi-mapping region, segmental duplication) inflating apparent alt-read support.
- **First question:** "Does this locus fall in a known low-complexity or segmental-duplication region (per RepeatMasker/segdup track)?"
- **Data to pull:** mapping quality (MAPQ) distribution at the locus and the reference genome's repeat/mappability track.

### Case samples and control samples cluster separately on a PCA of the full expression or genotype matrix, driven by non-biological covariates
- **Usually means:** batch effect confounded with condition — samples were processed or sequenced in separate batches that align with the biological grouping.
- **First question:** "Were cases and controls extracted, prepped, or sequenced on the same day/run/lane?"
- **Data to pull:** the sample metadata sheet with extraction date, sequencing run/lane, and reagent lot alongside the biological label.

### A germline variant caller run on tumor-only sequencing data
- **Usually means:** the pipeline default wasn't checked against the sample type — germline callers assume a diploid prior (0%, 50%, 100% VAF) that tumor purity and subclonality violate.
- **First question:** "Is this tumor-only or tumor-normal paired, and does the caller's ploidy/purity assumption match?"
- **Data to pull:** the sample sheet's tumor/normal designation and the caller's configuration (Mutect2 tumor-only mode vs. HaplotypeCaller germline mode).

### A short-read taxonomic classifier reports species-level confidence for a genus with known low sequence divergence between species
- **Usually means:** the reference database lacks resolution at that clade, and the classifier is reporting its best guess, not a well-supported call.
- **First question:** "How many species in this genus are represented in the reference database, and how divergent are their marker sequences?"
- **Data to pull:** the classifier's per-read confidence score distribution and the reference database's species list for the genus in question.

### An E-value reported without the database size or query length it was computed against
- **Usually means:** the number is being treated as a universal significance threshold, when it's search-space-dependent and not comparable across searches run against different databases.
- **First question:** "What database and query length produced this E-value?"
- **Data to pull:** the BLAST/DIAMOND command line or job parameters (database, `-db`, query length).

### RNA-seq normalization method mismatched to the comparison being made (e.g., TPM used for a between-sample DESeq2-style test)
- **Usually means:** confusion between within-sample (TPM/FPKM, for comparing genes to each other in one sample) and between-sample (median-of-ratios/TMM, for comparing one gene across samples) normalization purposes.
- **First question:** "Is this comparison within one sample across genes, or the same gene across samples?"
- **Data to pull:** the normalization function call in the analysis script and which axis of the count matrix it's normalizing.

### A GWAS hit reported below genome-wide significance (p > 5×10⁻⁸) as a finding without a stated replication cohort
- **Usually means:** the analysis is treating a suggestive signal as a discovered locus without the independent replication genome-wide significance implicitly assumes.
- **First question:** "Has this locus been tested in an independent cohort, or is this the discovery p-value alone?"
- **Data to pull:** the manuscript or report's replication section, or its absence.

### Sample or cell-line identity not confirmed (no STR profiling / SNP fingerprinting) before a multi-week sequencing and analysis effort
- **Usually means:** cross-sample contamination or a swapped/misidentified sample won't surface until a downstream biological result fails to make sense — by which point weeks of compute and interpretation are built on the wrong input.
- **First question:** "Was this sample's identity confirmed against its expected genotype/STR profile before analysis started?"
- **Data to pull:** the sample-tracking log's identity-confirmation step, or a quick SNP-fingerprint concordance check against a known reference sample.
