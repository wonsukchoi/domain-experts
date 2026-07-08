# Molecular and Cellular Biologist — Red Flags

### Fold-change reported as 2^−ΔΔCt with no primer-efficiency validation on record
- **Usually means:** no standard curve was ever run for this primer pair, so an assumed 100% efficiency may be masking a systematically over- or under-stated fold-change.
- **First question:** what was the standard-curve slope and R² for this primer pair, and does the slope fall in the −3.10 to −3.58 (90–110%) acceptable range?
- **Data to pull:** the standard-curve dilution series Ct values and the fitted slope/R².

### Reference gene Ct shifts more than 0.5–1 cycle between experimental conditions
- **Usually means:** the "housekeeping" gene isn't actually stable under this specific perturbation (common with metabolic, hypoxic, or stress treatments), so ΔΔCt normalization is biased by the reference gene's own movement.
- **First question:** has this reference gene's stability been validated (geNorm/NormFinder M-value) for this exact condition, or only assumed from unrelated literature?
- **Data to pull:** raw reference-gene Ct values across all conditions in this experiment.

### A p-value built from technical replicates counted as biological n
- **Usually means:** triplicate wells from one culture, or triplicate qPCR wells from one cDNA prep, were entered into the statistical test as if independent — pseudoreplication that inflates apparent significance.
- **First question:** how many independent cultures, animals, or transfections actually contributed to each group's n?
- **Data to pull:** the raw replicate-level data with each value's originating culture/prep labeled.

### Western blot band quantified with any pixel at or near saturation
- **Usually means:** the exposure or antibody dilution was set to make a faint band visible, pushing a strong band outside the antibody's linear range — the true difference between conditions is compressed in the reported ratio.
- **First question:** was a dilution series run to establish this antibody's linear range, and does the quantified exposure fall inside it?
- **Data to pull:** the raw, unprocessed blot image (not just the cropped/adjusted figure) and the linear-range validation dilution series.

### mRNA knockdown reported >80% with no protein-level confirmation
- **Usually means:** the phenotype is being attributed to gene loss based on transcript data alone, when protein — the actual functional unit in most cases — hasn't been checked.
- **First question:** has a Western blot or functional assay confirmed protein-level depletion, and at what timepoint relative to transfection?
- **Data to pull:** Western blot densitometry data at the same or a later timepoint than the phenotype readout.

### mRNA and protein knockdown percentages differ by more than ~20 points with no turnover-lag explanation offered
- **Usually means:** either genuine turnover-lag biology (long protein half-life) that should be stated, or a timepoint too early relative to the protein's known half-life — not an assay failure, but it needs to be named as one or the other.
- **First question:** what is this protein's reported half-life, and how many half-lives have elapsed between transfection and the protein measurement?
- **Data to pull:** a time-course Western (multiple timepoints post-transfection), if one exists.

### Cell line has no STR authentication on file, or last mycoplasma test is more than ~3–6 months old
- **Usually means:** silent misidentification or contamination is possible and would bias every result generated on this line without any visible phenotype change.
- **First question:** when was this specific line last STR-authenticated and mycoplasma-tested, and by whom?
- **Data to pull:** the STR profile report and the mycoplasma PCR test log/date.

### CRISPR knockout phenotype reported from a single clone
- **Usually means:** the phenotype could be a clone-specific off-target effect or clonal selection artifact rather than a consequence of the intended edit.
- **First question:** does the phenotype replicate in a second, independently derived clone (or with a second guide RNA)?
- **Data to pull:** genomic indel sequencing (TIDE or amplicon-seq) and protein-loss confirmation for each clone tested.

### Cell line passage number not reported, or known to exceed this line's validated ceiling (commonly passage 20–30, line-dependent)
- **Usually means:** genetic drift, phenotypic drift, or senescence-related changes may be confounded with the experimental treatment effect.
- **First question:** what passage number was used, and has this assay been validated as passage-stable up to that number for this specific line?
- **Data to pull:** the passage log and, if available, a growth-curve or marker-expression comparison across passage ranges.

### More than 2 groups compared using a series of unpaired t-tests instead of ANOVA
- **Usually means:** the family-wise false-positive rate is inflated above the nominal 5% — with 4 groups (6 pairwise comparisons) the true error rate is closer to 26% if each test runs at raw α=0.05.
- **First question:** how many total pairwise comparisons were run from this dataset, and was any multiple-comparisons correction applied?
- **Data to pull:** the full statistical analysis log, not just the summary table of "significant" comparisons.

### Statistical significance (p<0.05) claimed from n=2 biological replicates
- **Usually means:** the variance estimate itself is unreliable at n=2 (one degree of freedom per group), regardless of how small the p-value looks.
- **First question:** was n=2 a deliberate, power-justified choice, or the number of replicates that happened to be run before time/reagents ran out?
- **Data to pull:** the raw per-replicate values (not just the summary statistic) and any prior power calculation.

### Fluorescence imaging intensities compared across images acquired at different exposure, gain, or laser-power settings
- **Usually means:** acquisition settings, not biology, are driving part or all of the intensity difference between conditions.
- **First question:** were all images being compared acquired in the same imaging session at identical acquisition settings?
- **Data to pull:** the acquisition metadata (exposure time, gain, laser power, objective) for each image file.

### siRNA/shRNA knockdown phenotype reported using only one sequence
- **Usually means:** the phenotype could be a sequence-specific off-target effect rather than a consequence of losing the intended gene product.
- **First question:** does a second, non-overlapping siRNA or shRNA sequence targeting the same gene reproduce both the knockdown and the phenotype?
- **Data to pull:** knockdown efficiency (qPCR/Western) and phenotype data for the second sequence.
