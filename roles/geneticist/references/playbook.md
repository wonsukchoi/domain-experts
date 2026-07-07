# Geneticist — Playbook

## ACMG/AMP evidence-scoring worksheet (Bayesian point system, Tavtigian 2018)

| Code | Category | Points | Applies when |
|---|---|---|---|
| PVS1 | Pathogenic Very Strong | +8 | Null variant (nonsense, frameshift, canonical ±1/2 splice, start-loss) in a gene where loss-of-function is a known disease mechanism |
| PS1-PS4 | Pathogenic Strong | +4 each | Same amino-acid change as established pathogenic variant (PS1); functional studies show damaging effect (PS3); confirmed de novo with paternity/maternity confirmed (PS2); prevalence in affected significantly greater than controls (PS4) |
| PM1-PM6 | Pathogenic Moderate | +2 each | Mutational hot spot/functional domain (PM1); absent/rare in population databases (PM2); in trans with a pathogenic variant for recessive disease (PM3); protein length change from in-frame indel (PM4); novel missense at a residue with a different known-pathogenic missense (PM5); assumed de novo, parentage unconfirmed (PM6) |
| PP1-PP5 | Pathogenic Supporting | +1 each | Cosegregation with disease, default strength (PP1); missense in a gene with low benign-missense rate (PP2); multiple computational tools predict damaging (PP3); phenotype highly specific for the gene (PP4); reputable source classifies pathogenic without evidence shown (PP5, deprecated in most labs — do not use as sole support) |
| BA1 | Benign Stand-Alone | -8 | Allele frequency >5% in a general population database |
| BS1-BS4 | Benign Strong | -4 each | Frequency greater than expected for disorder (BS1); observed in a healthy adult for a fully penetrant early-onset disorder (BS2); functional studies show no damaging effect (BS3); lack of segregation in affected family members (BS4) |
| BP1-BP7 | Benign Supporting | -1 each | Missense in a gene where only truncating variants cause disease (BP1); observed in trans with a dominant pathogenic variant (BP2); in-frame indel in a repetitive region with no known function (BP3); multiple computational tools predict benign (BP4); synonymous variant with no predicted splice impact (BP7) |

**Classification tiers** (sum all applicable codes): Pathogenic ≥10 · Likely Pathogenic 6-9 · VUS 0-5 · Likely Benign -1 to -6 · Benign ≤-7.

## Pedigree segregation LOD-score quick reference

Perfect cosegregation (all affected carry variant, all unaffected past typical age of onset do not carry it) across *n* informative meioses:

| Informative meioses | Approx. LOD (perfect segregation) | PP1 strength |
|---|---|---|
| 1-4 | 0.30-1.20 | PP1 default (1 pt) |
| 5-6 | 1.51-1.81 | PP1_Moderate (2 pts) |
| ≥7 | ≥2.11 | PP1_Strong (4 pts) — genome-wide-significant needs LOD ≥3, i.e. ~10 meioses |

An "informative meiosis" is a transmission event where the outcome (variant present/absent) is consistent with disease status and could plausibly have gone the other way — an unaffected 22-year-old relative in a disease with 90% penetrance by age 50 is *not* yet informative; wait for them to clear the typical-onset age or exclude them from the count.

## Filled example: variant triage decision table

| Variant | gnomAD AF | Domain hit | Segregation | In-silico | Points | Tier |
|---|---|---|---|---|---|---|
| *MYH7* c.2167C>T | 0/1,589,320 (PM2, +2) | motor domain (PM1, +2) | 3 meioses, LOD 0.90 (PP1, +1) | REVEL 0.81 (PP3, +1) | 6 | Likely Pathogenic |
| *MYBPC3* c.3628-41_3628-17del | 12/1,589,320, AF 7.5e-6 (PM2 borderline — below threshold but not zero, +2) | not in curated hot spot (no PM1) | not evaluated, proband simplex (no PP1) | splice-prediction ambiguous (no PP3/BP4) | 2 | VUS |
| *TTN* c.34561C>T (p.Gln11521*) | absent gnomAD | truncating, exon included in >90% cardiac transcripts (PVS1, +8) | not evaluated | n/a | 8 | Likely Pathogenic (PVS1 alone caps here without a second code, per ACMG rule that PVS1 alone requires supporting frequency data too — treat as Likely Pathogenic, not Pathogenic, pending PM2 confirmation) |

## Gene-disease validity check (before scoring any variant)

1. Search ClinGen Gene-Disease Validity curations for the gene-disease pair.
2. If **Definitive/Strong**: proceed with variant scoring as normal.
3. If **Moderate/Limited**: proceed, but flag in the report that the underlying gene-disease association itself has limited evidential support — a well-scored variant in a Limited-validity gene should be reported as "of uncertain significance pending confirmation of gene-disease relationship," not as a confident Pathogenic call.
4. If **Disputed/Refuted** or **no curation exists**: do not issue a clinical classification; escalate to research-context reporting only.
