# Cytogenetics Analysis Playbook

Filled protocols and decision tables, not descriptions of them. Use to size a metaphase count, pick a band resolution/turnaround combination, or route a case to the right test.

## 1. Specimen-to-protocol routing table

| Specimen | Typical indication | Culture | Target turnaround | Default band resolution |
|---|---|---|---|---|
| Peripheral blood (PHA-stimulated) | Constitutional (suspected aneuploidy, developmental delay, recurrent miscarriage) | 72h, PHA mitogen | 10–14 days | 550 bands |
| Bone marrow aspirate | New/relapsed leukemia, treatment response | 24h unstimulated + 24–48h stimulated | 3–5 days (stat) | 300–400 bands |
| Amniotic fluid | Prenatal, abnormal ultrasound/screen | 7–10 days, in situ culture | 10–14 days culture; 24–48h if rapid FISH also ordered | 550 bands |
| Chorionic villi (CVS) | First-trimester prenatal | Direct prep (1–2 days) + long-term culture (7–10 days) confirmatory | Direct: 2–3 days; confirmed: 10–14 days | 400–550 bands |
| Solid tumor | Sarcoma/pediatric tumor subtyping | 1–5 days, tissue-dependent | 7–14 days | 300–400 bands (often FISH-supplemented) |
| Products of conception | Miscarriage workup | 5–14 days, variable success | 10–14 days (or microarray if culture fails) | 400–550 bands |

**Fallback when culture fails or is slow to grow:** reflex to chromosomal microarray directly on extracted DNA (no culture required) — standard fallback for products-of-conception and low-cellularity CVS specimens; report as "karyotype unsuccessful due to culture failure, microarray performed as an alternative" rather than reporting a partial/marginal karyotype.

## 2. Metaphase count sizing (binomial detection basis)

Cells needed to detect a mosaic clone at level *p* with 95% confidence: n = ln(0.05) / ln(1 − p).

| Suspected minimum clone level | Cells to count | Use case |
|---|---|---|
| ≥14% | 20 (standard/default) | Routine constitutional and oncology workups, no mosaicism suspicion |
| ≥10% | 29 | Mild clinical suspicion, non-specific findings |
| ≥5% | 58 | Ambiguous genitalia, discordant NIPT/ultrasound, suspected low-level mosaicism |
| ≥2% | 149 | Strong clinical suspicion (e.g., confirmed mosaic result in a related tissue, discordant prior test) — usually paired with FISH on 200+ interphase nuclei rather than counting this many metaphases |

**Escalation rule:** if the first 20 cells include any single deviant cell that doesn't meet ISCN clonality (one loss, or one gain/structural not yet matched), do not discard it silently — count an additional 10–20 cells specifically screening for a second matching abnormality before finalizing as artifact.

## 3. ISCN clonality decision table

| Observation in the count | Clonal? | Action |
|---|---|---|
| 1 cell, extra chromosome or structural abnormality | No (yet) | Screen additional cells for a match; if none by 30–40 total, call non-clonal/artifact |
| 2 cells, identical extra chromosome or identical structural abnormality | Yes | Report as clonal |
| 1–2 cells, loss of a chromosome | No | Report as likely artifact (random loss is common in culture/prep) |
| 3 cells, identical chromosome loss | Yes | Report as clonal |
| 2 distinct abnormal cell lines, each independently meeting clonality | Yes (both) | Report as two clones (mosaic or composite karyotype) with cell counts for each |

## 4. Test-selection fallback order by clinical question

1. **"Is there a balanced structural rearrangement (translocation, inversion)?"** → Karyotype first (whole-genome, resolution ~5–10 Mb). If found, reflex FISH to confirm breakpoints/gene involvement. Microarray alone will miss balanced events — do not substitute.
2. **"Is there a known recurrent fusion (e.g., BCR-ABL1, PML-RARA)?"** → Targeted FISH (fastest, hours) as first-line; karyotype run in parallel for background/additional abnormalities, not as a replacement.
3. **"Is there a submicroscopic deletion/duplication (e.g., microdeletion syndrome, unexplained developmental delay)?"** → Chromosomal microarray first-line (resolution ~50–100 kb vs. karyotype's ~5–10 Mb); karyotype alone will miss it.
4. **"What is the true clonal burden of a known abnormality over time (monitoring)?"** → Interphase FISH on 200 nuclei (quantitative, less culture-selection bias) preferred over serial karyotype percentages for trend-following.
5. **"Is an abnormal prenatal result fetal or maternal in origin?"** → STR-marker maternal cell contamination study on a maternal blood comparator sample, not a repeat karyotype alone.

## 5. FISH cutoff validation example (interphase, quantitative)

Laboratory-established normal cutoff = mean signal-pattern frequency + 3 standard deviations, from ≥20 morphologically normal control specimens.

Example (CEP8 trisomy probe, 3-signal pattern):
- 20 normal controls, 200 nuclei each: mean 3-signal rate = 1.2%, SD = 0.9%.
- Cutoff = 1.2 + (3 × 0.9) = 3.9%, rounded to **4.0%** for reporting.
- Patient result 34/200 (17.0%) — clears cutoff by >4x, unambiguous positive.
- Patient result at, say, 4/200 (2.0%) — below cutoff, reported as "no evidence of trisomy 8 by FISH" even if 1 karyotype metaphase showed +8, consistent with karyotype-level artifact.
