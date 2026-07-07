# Survey Researcher — Playbook

## Response-rate disposition table (AAPOR RR3)

| Disposition | Count | Category |
|---|---|---|
| Complete interview | 1,000 | Interview (I) |
| Partial interview (≥50% of key items) | 40 | Interview (I) |
| Refusal | 620 | Non-interview, eligible (R) |
| Non-contact (no answer after 6 attempts) | 890 | Non-interview, eligible (NC) |
| Language barrier / other eligible non-interview | 50 | Non-interview, eligible (O) |
| Not a residential number / ineligible | 1,400 | Ineligible (INE) |
| Unknown eligibility (never resolved) | 500 | Unknown (UH/UO) |
| **Total dialed** | **4,500** | — |

**RR3 calculation:** e (estimated proportion of unknown-eligibility cases that are actually eligible) = eligible ÷ (eligible + ineligible) = (1,000+40+620+890+50) / (1,000+40+620+890+50+1,400) = 2,600 / 4,000 = 0.65.

RR3 = I / (I + P + R + NC + O + e×UH) = 1,040 / (1,040 + 620 + 890 + 50 + 0.65×500) = 1,040 / (2,600 + 325) = 1,040 / 2,925 = **35.6%**.

Below 20%: nonresponse-bias check is mandatory before fielding is considered done, not optional.

## Post-stratification weighting worksheet

| Category | Population target % | Achieved sample % | Achieved n | Raw weight (target/achieved) |
|---|---|---|---|---|
| Age 18–34 | 28% | 18% | 180 | 1.556 |
| Age 35–54 | 35% | 33% | 330 | 1.061 |
| Age 55+ | 37% | 49% | 490 | 0.755 |
| **Total** | **100%** | **100%** | **1,000** | — |

Weighted n check: 180×1.556 + 330×1.061 + 490×0.755 = 280.1 + 350.1 + 370.0 = 1,000.2 ≈ 1,000 — weights reconcile back to sample size (rounding only).

**Weight trimming rule:** cap any individual weight at 5× the median weight; recompute the trimmed weights' sum-to-n and redistribute the trimmed mass proportionally across untrimmed cases. Skipping this step lets a handful of underrepresented respondents dominate the topline.

**Design effect (Kish's deff):** deff = n × Σ(wᵢ²) / (Σwᵢ)². Effective sample size = n / deff. A deff above ~2.0 on a single-dimension weight is a signal the frame or sample source has a coverage problem worth fixing upstream, not just weighting around.

## Split-ballot pretest design (question-wording test)

| Form | n | Question wording | Result (% agree) |
|---|---|---|---|
| A | 250 | "Should the city **allow** overnight parking on residential streets?" | 61% |
| B | 250 | "Should the city **forbid** overnight parking on residential streets?" (reverse-coded to % who said no, i.e. effectively "allow") | 43% |

18-point gap between logically equivalent forms — the wording, not a genuine 18-point opinion split, is driving the difference. Fielding form A alone and reporting "61% support parking access" without disclosing the split-ballot result overstates confidence in the number.

## Methodology memo template (filled)

> **Study:** [Topic] tracking survey, Wave [N].
> **Population:** [Target population], N ≈ [population size].
> **Frame:** [Frame source — voter file, RDD phone, panel] — known coverage gap: [describe, e.g. "excludes cell-only households under X% if landline-only frame"].
> **Mode:** [Phone/web/mixed], fielded [dates].
> **Sample size:** [n] completes; response rate [RR3 %] per AAPOR standard definitions.
> **Weighting:** [Variables], targets from [source, e.g. Census ACS], design effect [value].
> **Margin of error:** ±[X]% at 95% confidence on the weighted sample — sampling error only; does not include coverage or nonresponse bias.
> **Caveat:** [Any known limitation — mode-effect risk from prior wave, small subgroup bases, frame gap].
