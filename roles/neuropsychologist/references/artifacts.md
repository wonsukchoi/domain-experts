# Artifacts — battery design, validity cutoffs, and reliable change

Filled examples an evaluator can populate directly, not descriptions of what to include.

## 1. Battery matrix by referral question

| Referral question | Core domains to hit | Example instruments (minimum) | Typical session time |
|---|---|---|---|
| Dementia workup (MCI vs. depression vs. normal aging) | Delayed memory (free recall + recognition), executive function, language, mood screen | CVLT-II or WMS-IV Logical Memory + Visual Reproduction, Trail Making A/B, BNT, PHQ-9/GDS | 3-4 hrs |
| Mild TBI / return to work or duty | Processing speed, attention, working memory, executive function, symptom validity | WAIS-IV PSI + WMI subtests, Trail Making A/B, D-KEFS, PVT + PAI or MMPI-3 validity scales | 3-5 hrs |
| Pre-surgical epilepsy (lateralization) | Verbal vs. nonverbal memory dissociation, language dominance data, naming | CVLT-II or selective reminding test, Rey Complex Figure, BNT, COWAT, Wada or fMRI language data (from neurology) | 4-6 hrs |
| Pediatric ADHD / learning disorder | Attention/executive function, processing speed, academic achievement, behavior rating scales | Conners-3 or BASC-3, WISC-V, WIAT-4 or WJ-IV Achievement, D-KEFS or NEPSY-II executive tasks | 4-6 hrs |
| Forensic capacity / competency | Global cognition, executive/judgment tasks, symptom and performance validity (mandatory, both sides) | WAIS-IV abbreviated, MoCA or RBANS, TOMM + PAI/MMPI-3 validity scales, capacity-specific instrument (e.g., MacCAT) | 3-5 hrs |
| Sports concussion (baseline vs. post-injury) | Processing speed, reaction time, verbal/visual memory, symptom checklist | ImPACT or CNS Vital Signs baseline comparison, symptom checklist (PCSS), balance/vestibular screen (from athletic trainer) | 30-45 min (computerized) |

## 2. Performance/symptom validity cutoff table

| Instrument | Metric | Cutoff for likely invalid performance | Source |
|---|---|---|---|
| TOMM | Trial 2 (or Retention trial) raw score | <45/50 | Tombaugh, 1996 |
| Reliable Digit Span (WAIS-IV Digit Span embedded) | Longest span forward + backward summed across trials | <=7 | Greiffenstein, Baker & Gola, 1994 |
| Rey 15-Item Test + recognition | Free recall + recognition combined score | <20/30 combined (free recall alone is a weak standalone cutoff) | Boone et al., 2002 |
| CVLT-II Forced Choice | Correct out of 9 | <=7/9 | CVLT-II manual, Delis et al., 2000 |
| Word Memory Test (WMT) | Immediate + delayed recognition | <82.5% on either | Green, 2003 |
| MMPI-3 | F-r (infrequency) T-score | >=80 | MMPI-3 manual |
| PAI | Negative Impression Management (NIM) T-score | >=92 | PAI manual |

**Rule of thumb:** administer at least two independent PVTs (one freestanding, one embedded) per evaluation — a single failed PVT is a flag; two independent failures meet the Slick, Sherman & Iverson (1999) evidentiary threshold for probable non-credible performance.

## 3. Reliable Change Index — worked calculation

Patient retested 12 months after initial evaluation on WMS-IV Logical Memory II (age-scaled score, mean 10, SD 3).

- Time 1 score: 6
- Time 2 score: 9
- Test-retest reliability (r) at this interval, per manual: 0.75
- Standard deviation of the normative sample: 3
- Standard error of measurement (SEM) = SD x sqrt(1 - r) = 3 x sqrt(0.25) = 3 x 0.5 = 1.5
- Standard error of the difference (SEdiff) = sqrt(2 x SEM^2) = sqrt(2 x 2.25) = sqrt(4.5) = 2.12
- Published practice-effect estimate at a 12-month interval for this subtest: +1.0 scaled-score point
- Expected score if no true change = Time 1 + practice effect = 6 + 1.0 = 7.0
- Observed change from expected = 9 - 7.0 = 2.0
- 90% confidence RCI threshold = 1.645 x SEdiff = 1.645 x 2.12 = 3.49

**Interpretation:** the raw 3-point gain (6 -> 9) looks like improvement, but after subtracting the expected +1.0 practice effect, the true observed change is 2.0 scaled-score points — below the 3.49-point threshold needed for 90% confidence the change is real rather than measurement noise plus practice. Conclusion for the report: "no reliable change in verbal delayed memory since the prior evaluation" — not "improved."

## 4. Score classification and percentile conversion

| Standard score (mean 100, SD 15) | Percentile range | Classification (Heaton-convention labels) |
|---|---|---|
| 130+ | 98th+ | Very Superior |
| 120-129 | 91st-97th | Superior |
| 110-119 | 75th-90th | High Average |
| 90-109 | 25th-74th | Average |
| 80-89 | 9th-24th | Low Average |
| 70-79 | 2nd-8th | Borderline |
| <70 | <2nd | Impaired |

For scaled scores (mean 10, SD 3) and T-scores (mean 50, SD 10), convert to the same percentile before applying this table — mixing scaled-score and standard-score numbers directly in a report invites a reader to misread a 7 (scaled) as worse than a 70 (standard) when both sit at roughly the 16th percentile.

## 5. CPT billing structure (2019 AMA revision)

| Code | Service | Unit |
|---|---|---|
| 96132 | Neuropsychological test evaluation services by physician/QHP (interpretation, integration, report) | First hour |
| 96133 | Same, each additional hour | Per hour |
| 96136 | Test administration and scoring by physician/QHP | First 30 minutes |
| 96137 | Same, each additional 30 minutes | Per 30 min |
| 96146 | Automated/computer-administered test with automated result, no interpretation by clinician | Per test |

A typical 4-hour dementia-workup evaluation (1 hr interview/interpretation, 2.5 hrs testing, 0.5 hr scoring/report) bills roughly as 96132 x1 (interpretation/report, first hour) + 96136 x1 + 96137 x4 (testing time in 30-min units) — no 96133 add-on unless interpretation itself runs past 60 minutes. Confirm current-year payer authorization limits before scheduling, since many payers cap authorized units below what a full battery requires.
