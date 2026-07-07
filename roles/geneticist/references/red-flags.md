# Geneticist — Red Flags

### Classification request with no phenotype specified
- **Usually means:** requester wants a generic "is this variant bad" answer, or the phenotype was assumed obvious from the gene name.
- **First question:** "What condition is this classification for — the same variant can be pathogenic for one indication and benign for another."
- **Data to pull:** the ordering indication/ICD code, or the specific research question driving the request.

### PVS1 applied to a gene without an established loss-of-function disease mechanism
- **Usually means:** the null-variant-equals-pathogenic shortcut was applied without checking whether LOF is actually how this gene causes disease (some genes cause disease only via gain-of-function or dominant-negative missense).
- **First question:** "Does ClinGen's gene-specific PVS1 guidance confirm LOF as a mechanism for this gene, or could a null variant here be benign?"
- **Data to pull:** ClinGen gene-specific ACMG rule specifications, if published for this gene.

### De novo variant claimed from duo (not trio) sequencing
- **Usually means:** only one parent was sequenced, or parentage was assumed rather than confirmed — a common source of false PS2 application.
- **First question:** "Was biological parentage confirmed with informative markers, and were both parents sequenced?"
- **Data to pull:** trio sequencing confirmation, or STR/SNP-based parentage-confirmation result.

### Single-family segregation described as "confirms pathogenicity"
- **Usually means:** the LOD score from this family alone (typically <2 for a few affected relatives) is being treated as equivalent to genome-wide significance (LOD ≥3).
- **First question:** "How many informative meioses, and what's the calculated LOD — does it clear PP1_Strong or just default PP1?"
- **Data to pull:** the pedigree with ages of onset/current ages marked, to recompute informative-meiosis count.

### Population frequency compared against the wrong population/ancestry
- **Usually means:** allele frequency was pulled from the "all populations" gnomAD aggregate instead of the ancestry-matched subpopulation, understating or overstating rarity.
- **First question:** "What's the frequency in the proband's specific ancestry group, not the pooled database average?"
- **Data to pull:** gnomAD population-specific allele frequency and count, filtered for the matching ancestry.

### Variant classified in a gene with no ClinGen gene-disease validity curation
- **Usually means:** the gene was included on a testing panel based on a single case report or biological plausibility, not curated evidence.
- **First question:** "Is there a ClinGen Definitive/Strong curation for this gene-disease pair, or are we scoring a variant in an unvalidated gene?"
- **Data to pull:** ClinGen Gene-Disease Validity search result for the specific gene-disease pair.

### ClinVar shows conflicting classifications across submitters
- **Usually means:** either a genuinely borderline evidence profile, or one submitter used outdated criteria (pre-2015 ACMG, or PP5/BP6 which are now deprecated).
- **First question:** "What evidence and criteria version did each conflicting submitter cite, and is the conflict resolvable with current data?"
- **Data to pull:** ClinVar submission details including assertion criteria and submission date for each conflicting record.

### Recurrence-risk percentage quoted without a named penetrance study
- **Usually means:** a textbook rule-of-thumb number (e.g. "50% for autosomal dominant") is being presented as the patient-specific risk without adjusting for the gene's actual penetrance data.
- **First question:** "Is that the Mendelian transmission risk or the clinical penetrance-adjusted risk, and which published cohort is it from?"
- **Data to pull:** the penetrance study's ascertainment method (population-based vs. clinic-based cohorts give very different penetrance estimates).

### In-silico predictor score used as the sole basis for classification
- **Usually means:** REVEL/CADD/AlphaMissense scored the variant as damaging and no other evidence was gathered.
- **First question:** "What population-frequency and segregation evidence exists beyond the computational prediction — in-silico alone caps at VUS."
- **Data to pull:** gnomAD frequency, ClinVar prior submissions, and any available family/functional data.

### Functional study cited as PS3 without checking assay validity
- **Usually means:** a functional assay result is being weighted as strong evidence without confirming the assay is validated to actually reflect the disease mechanism (e.g. an in-vitro enzyme assay for a gene where the disease mechanism is haploinsufficiency, not catalytic).
- **First question:** "Does this functional assay measure the actual disease-relevant mechanism, and has it been validated against known pathogenic/benign controls?"
- **Data to pull:** the functional-study methods section and its validation against reference variants.
