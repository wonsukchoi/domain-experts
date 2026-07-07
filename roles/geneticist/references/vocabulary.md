# Geneticist — Vocabulary

### Variant of uncertain significance (VUS)
A classification meaning current evidence is insufficient to call a variant pathogenic or benign — not a diagnosis, not a "probably fine" or "probably bad" hedge.
**In use:** "This is a VUS under the current point total — we don't act on it clinically, but I've flagged what evidence would move it."
**Common misuse:** treated as a soft-pathogenic finding ("probably bad, just not proven yet") when it should carry zero clinical weight until reclassified — this drives both unnecessary anxiety and inappropriate prophylactic intervention.

### Penetrance
The proportion of people with a given pathogenic genotype who go on to display the associated phenotype.
**In use:** "This variant has age-dependent penetrance — roughly 50% by age 40 and 80% by age 70 in the largest published cohort, so a negative exam at 35 doesn't rule it out."
**Common misuse:** treated as a fixed, gene-level constant rather than a study-specific, ascertainment-dependent, often age-dependent number that varies by cohort.

### Expressivity
The degree to which a phenotype varies among individuals who share the same pathogenic genotype.
**In use:** "Variable expressivity explains why the proband has severe cardiomyopathy and her carrier mother has only mild wall-thickening."
**Common misuse:** confused with penetrance — expressivity is about severity/presentation *given* the phenotype occurs, penetrance is about *whether* it occurs at all.

### Segregation analysis
Testing whether a variant is inherited together with a disease phenotype across a family's pedigree, at a rate more consistent with causation than chance.
**In use:** "Segregation in this family gives us an LOD of about 0.9 — supportive but nowhere near confirmatory on its own."
**Common misuse:** any cosegregating family is described as "confirming" pathogenicity regardless of the number of informative meioses, when small families rarely provide strong quantitative evidence alone.

### Loss of function (LOF)
A variant type (nonsense, frameshift, canonical splice-site, start-loss) predicted to substantially or completely disrupt normal protein production.
**In use:** "This is a clear LOF allele, but PVS1 only applies at full strength because haploinsufficiency is the established mechanism for this gene."
**Common misuse:** assumed to automatically qualify for PVS1 regardless of whether the specific gene's disease mechanism is actually loss-of-function-mediated.

### Genotype-phenotype correlation
The relationship between a specific variant (or variant class/location) and the resulting clinical presentation.
**In use:** "Variants in the motor domain correlate with earlier-onset, more severe HCM than variants in the tail domain in this cohort."
**Common misuse:** applied as a firm predictive rule for an individual patient when the underlying study was a population-level association with wide individual variation.

### Compound heterozygous
Carrying two different pathogenic variants, one on each copy of a gene, causing a recessive condition.
**In use:** "The proband is compound heterozygous — one variant inherited from each unaffected carrier parent — consistent with autosomal recessive inheritance."
**Common misuse:** confused with "homozygous" (two copies of the *same* variant) — the distinction matters because compound heterozygosity requires confirming the two variants are in trans (on different chromosome copies), not both on the same copy (in cis).

### In trans / in cis
Describes whether two variants sit on the same chromosome copy (cis) or opposite copies (trans) inherited from each parent.
**In use:** "We need parental testing to confirm these two variants are in trans before calling this compound heterozygous recessive disease."
**Common misuse:** assumed from the variants simply both being present, without phasing data (parental genotyping or long-read sequencing) to actually establish trans configuration.

### Maximum credible population allele frequency
The highest allele frequency a variant could plausibly have in the general population and still cause a given rare disease, calculated from disease prevalence, penetrance, and genetic heterogeneity.
**In use:** "At 1 in 10,000 disease prevalence and 70% of cases attributable to this gene, the maximum credible frequency here is roughly 0.0002 — this variant's gnomAD frequency of 0.001 is too common to be causal."
**Common misuse:** a single fixed frequency threshold (e.g. "anything under 1%") applied across all genes and diseases regardless of prevalence and genetic architecture.

### Proband
The first affected family member through whom a family is ascertained for genetic study or testing.
**In use:** "The proband's variant wasn't found in either parent's blood sample, consistent with a de novo origin pending parentage confirmation."
**Common misuse:** used interchangeably with "patient" generally, losing the specific meaning of "the index case that led to the family being studied."

### Reduced representation vs. clinical-grade sequencing
The distinction between research-grade sequencing (may have gaps, lower depth, no CLIA validation) and clinical-grade sequencing (validated, complete coverage of reportable regions, CLIA/CAP-accredited).
**In use:** "That variant call comes from a research exome — it needs Sanger confirmation in a CLIA lab before it goes in a clinical report."
**Common misuse:** research-sequencing findings reported to patients or clinicians as if clinically validated, skipping the orthogonal confirmation step clinical labs require.

### Gene-disease validity
A formal, evidence-graded assessment (e.g. ClinGen's framework) of whether a gene is actually causally linked to a given disease, independent of any specific variant.
**In use:** "Before we score this variant, check ClinGen — is *this gene's* relationship to *this disease* even Definitive, or just Limited?"
**Common misuse:** assumed automatically valid because a gene appears on a commercial testing panel — panel inclusion is not the same as curated evidential support.

### Actionability
Whether a genetic finding, if returned, would change clinical management (screening, surveillance, treatment, reproductive planning).
**In use:** "This VUS isn't actionable regardless of classification — even if reclassified pathogenic, there's no established intervention for this gene yet."
**Common misuse:** conflated with "clinical significance" generally — a variant can be confidently pathogenic but not currently actionable, or actionable findings can arise from genes with only moderate classification confidence in specific contexts (e.g. ACMG secondary-findings list).
