# Playbook — battery selection, PVT cutoffs, and serial-testing math

## Battery-selection matrix by referral question

| Referral question | Core battery | Domains covered | Validity requirement |
|---|---|---|---|
| Mild TBI / personal-injury litigation | WAIS-IV (4 index scores), CVLT-3, Trail Making A/B, D-KEFS Verbal Fluency, Grooved Pegboard | attention, memory, executive, motor | ≥3 independent PVTs (e.g., TOMM + WMT/MSVT + embedded RDS) — forensic stakes raise the bar above the clinical default |
| Dementia differential (memory clinic) | RBANS or WAIS-IV brief form, CVLT-3 or HVLT-R, Boston Naming Test, Trail Making A/B, Clock Drawing | memory, language, executive, visuospatial | 1 PVT (e.g., Rey 15-Item + recognition, or embedded RDS) usually sufficient absent secondary gain; add a second if a disability filing is in progress |
| Pre-surgical epilepsy workup | Wada test or fMRI language/memory lateralization, WAIS-IV, CVLT-3 or Rey AVLT (hemisphere-specific memory), Boston Naming | language and memory lateralization, post-resection risk | Standard PVTs still given, but content is interpreted only after checking the lateralization result — norms assume typical dominance |
| Pediatric ADHD / learning-disability workup | WISC-V, CVLT-C, D-KEFS, WIAT academic achievement | attention, learning, executive | Age-normed PVT (e.g., pediatric MSVT) if an accommodation or IEP filing creates secondary gain |
| Fitness-for-duty / return-to-duty (pilot, first responder, post-concussion) | Full battery above plus computerized reaction-time measure (e.g., ImPACT) | all domains + reaction time | ≥2 independent PVTs plus an occupational functional measure tied to the specific duty |

## PVT cutoff table (multiple-failure model)

| Instrument | Primary index | Fail cutoff |
|---|---|---|
| TOMM | Trial 2 (of 50) | < 45/50 (90%) |
| Word Memory Test (WMT) | Immediate/Delayed Recognition, Consistency | < 82.5% on any primary subtest |
| Medical Symptom Validity Test (MSVT) | Immediate/Delayed Recognition, Consistency | < 85% on any primary subtest |
| Reliable Digit Span (embedded, WAIS-IV Digit Span) | Longest span forward+backward summed reliably | ≤ 7 |
| Rey 15-Item Test + recognition | Combined free recall + recognition score | < 20 |
| Dot Counting Test | E-score (grouped vs. ungrounded time + errors) | > 17 |

**Interpretation rule (Larrabee, 2003, 2008):** 0 failures across independent PVTs = valid; exactly 1 failure = indeterminate, do not conclude either way, add another PVT; ≥2 independent failures = probable invalid performance, cognitive content scores are not interpretable as true-ability measures. Forensic referrals: treat 1 failure as grounds to add a third PVT before drawing any conclusion, given the higher base rate of exaggeration under litigation incentives.

## Worked Reliable Change Index (RCI) calculation — serial testing

Scenario: a 58-year-old post-stroke patient is retested on WAIS-IV Working Memory Index (WMI) 12 months after a baseline evaluation, to check whether cognitive rehab produced real gains or whether an observed increase is just practice.

Inputs (from the WAIS-IV technical manual): WMI test-retest reliability r = 0.85; population SD = 15.

1. Standard error of measurement: SEM = SD × √(1 − r) = 15 × √0.15 = 15 × 0.387 = **5.81**
2. Standard error of the difference: SEdiff = SEM × √2 = 5.81 × 1.414 = **8.21**
3. Reliable Change Index (90% CI, z = 1.645): RCI = 1.645 × SEdiff = **13.5 points**
4. Published 12-month practice-effect gain for WMI (independent of true change): **+2.0 points**
5. Observed scores: baseline WMI = 95, retest WMI = 90 (raw drop of 5 points)
6. Practice-adjusted observed change: (90 − 95) − 2.0 = **−7.0 points**
7. Compare to threshold: |−7.0| < 13.5 → **not a reliable change**

**Conclusion to write in the report:** "The 5-point raw decrease in Working Memory Index, after accounting for the +2-point practice effect expected at a 12-month retest interval, is a 7-point adjusted change — within the ±13.5-point range attributable to measurement error alone at 90% confidence. This is not evidence of cognitive decline or of failure to benefit from rehabilitation; a change exceeding ±13.5 points would be required to call it reliable."

Use the same four-step arithmetic (SEM → SEdiff → RCI → compare to practice-adjusted observed change) for any instrument with a published test-retest reliability coefficient; substitute that instrument's r and SD.
