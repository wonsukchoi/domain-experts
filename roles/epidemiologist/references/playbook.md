# Epidemiologist — Playbook

## The CDC ten-step outbreak investigation sequence (filled example)

| Step | Action | Example (wedding GI outbreak) |
|---|---|---|
| 1 | Prepare for field work | Confirm lab capacity, assign roles, gather PPE/sampling kits before site visit |
| 2 | Establish existence of outbreak | 68 cases vs. expected ~0 for this population over 3 days — confirmed excess |
| 3 | Verify diagnosis | Confirm symptom pattern (vomiting/diarrhea) consistent with foodborne illness, not coincidental unrelated illness |
| 4 | Construct case definition | Vomiting or diarrhea, onset within 48h of reception, among the 210 guest list |
| 5 | Find cases systematically | Survey full guest list, not just self-reported cases — avoids case-finding bias |
| 6 | Descriptive epidemiology | Epi curve by onset time; single peak at 14h — point-source pattern |
| 7 | Generate hypotheses | Menu-item-specific attack rates flag chicken salad as leading candidate |
| 8 | Evaluate hypotheses (analytic study) | Cohort study: RR = 16.2 for chicken salad exposure |
| 9 | Refine / additional studies | Cross-check kitchen temperature logs for a physical mechanism |
| 10 | Implement control measures | Discard remaining product, review holding-time procedure |
| 11 | Communicate findings | File outbreak summary; route to caterer, health department, and (if applicable) press |

## 2x2 table and calculation worksheet (filled — chicken salad exposure)

| | Ill | Well | Total | Attack rate |
|---|---|---|---|---|
| Ate chicken salad | 61 | 13 | 74 | 82.4% |
| Did not eat chicken salad | 7 | 129 | 136 | 5.1% |
| **Total** | **68** | **142** | **210** | 32.4% |

- **Relative risk (cohort)** = attack rate exposed / attack rate unexposed = 82.4% / 5.1% = **16.2**
- **Attributable risk (exposed)** = 82.4% − 5.1% = **77.3 percentage points**
- **Population attributable fraction** = (overall attack rate − unexposed attack rate) / overall attack rate = (32.4% − 5.1%) / 32.4% ≈ **84%** of the *exposed subgroup's excess*; expressed against the whole cohort using exposed proportion (74/210 = 35.2%): 35.2% × 77.3pp ≈ 27.2 percentage points of the 32.4% overall attack rate, i.e. **~27% of the total population's risk**.

## Case-control worksheet (template — use when population isn't enumerable)

| | Cases (n) | Controls (n) |
|---|---|---|
| Exposed | a | b |
| Unexposed | c | d |

- **Odds ratio** = (a × d) / (b × c)
- Valid as an approximation of relative risk only when the outcome is rare in the source population (commonly cited threshold: population prevalence below ~10%).
- Match controls on the strongest known confounders (age, geography, season) before analysis; unmatched comparisons require statistical adjustment instead.

## Surveillance system evaluation checklist

| Property | Question | Red flag |
|---|---|---|
| Sensitivity | What fraction of true cases does the system capture? | Hospital-only reporting misses cases managed outpatient or untreated |
| Timeliness | Median lag from case onset to system report? | Lag exceeding one incubation period defeats early control action |
| Representativeness | Does the reporting population match the at-risk population? | Sentinel-site systems skew toward whoever happens to test there |
| Positive predictive value | Of reported signals, what fraction are true cases? | Low PPV burns investigator time chasing false alarms |

## Baseline comparison worksheet (is this a true outbreak?)

| Period | Case count | 5-yr seasonal average (same weeks) | Ratio |
|---|---|---|---|
| Current period | 68 | 4 | 17.0x |

Ratio meaningfully above 1 (commonly a working threshold of 2x baseline) supports declaring a true excess rather than expected variation — always paired with a plausibility check (a known common exposure, not just a numeric threshold).
