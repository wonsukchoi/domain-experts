# Industrial-Organizational Psychologist — Playbook

## Adverse-impact worksheet (4/5ths ratio + significance test)

| Group | Applicants | Hired | Selection rate | Ratio vs. highest | Flag (<0.80)? |
|---|---|---|---|---|---|
| White (highest rate) | 250 | 75 | 30.0% | 1.00 | — |
| Black | 150 | 30 | 20.0% | 0.667 | **Yes** |
| Hispanic | 90 | 24 | 26.7% | 0.889 | No |
| Asian | 60 | 19 | 31.7% | 1.06 | No |

Two-proportion z-test (White vs. Black, the flagged pair):
```
pooled p = (75 + 30) / (250 + 150) = 0.2625
SE = sqrt(0.2625 × 0.7375 × (1/250 + 1/150)) = 0.0454
z = (0.300 − 0.200) / 0.0454 = 2.20   →  p < .05, significant
```
Rule: flag on 4/5ths, confirm on z (or Fisher's exact if any cell < 30). Only a significant z result triggers the job-relatedness defense obligation below — a 4/5ths flag alone with p>.05 gets noted and monitored, not acted on as confirmed impact.

## Validity-correction worksheet (range restriction, Case II Thorndike)

```
Inputs:
  raw r (incumbent sample)         = 0.28
  SD, applicant pool (unrestricted) = 13.0
  SD, incumbents (restricted)       = 8.0
  U = SD_unrestricted / SD_restricted = 13.0 / 8.0 = 1.625

Correction:
  r_c = (r × U) / sqrt(1 + r² × (U² − 1))
      = (0.28 × 1.625) / sqrt(1 + 0.0784 × 1.6406)
      = 0.455 / sqrt(1.1286)
      = 0.455 / 1.0623
      = 0.43
```
Reliability ceiling check — never report a correction implying validity above what criterion reliability allows:
```
max possible r = sqrt(reliability_predictor × reliability_criterion)
               = sqrt(0.85 × 0.65)
               = sqrt(0.5525) = 0.74
```
0.43 < 0.74 ceiling — the corrected coefficient is plausible, not an artifact of over-correction.

## Job-analysis to KSAO linkage table (filled excerpt — Sales Associate)

| Task (from task inventory) | % time | Criticality (1-5) | KSAO required | Assessment component that measures it |
|---|---|---|---|---|
| Approach and qualify walk-in customer needs | 20% | 5 | Active listening, rapport-building | Structured interview, situational item 3 |
| Handle price/product objections | 15% | 4 | Persuasion under resistance | Role-play work sample |
| Process transaction, upsell add-on | 25% | 3 | Numerical accuracy, product knowledge | Knowledge test, cash-handling simulation |
| Resolve escalated complaint | 10% | 5 | Emotional regulation, de-escalation | Situational judgment test item 7 |
| Restock and merchandise floor | 30% | 2 | Attention to detail, initiative | Not directly assessed — trained post-hire |

Rule: every assessment component must trace to a task row with criticality ≥3; a component that doesn't map to any task is a content-validity gap, not a bonus measure.

## Technical validation report skeleton (SIOP Principles format)

1. **Purpose and scope** — position(s) covered, decision the tool supports (hire/promote/place).
2. **Job analysis summary** — method, date, task/KSAO table (see above), currency check.
3. **Validation strategy and rationale** — which of content/criterion/construct, and why given sample size and tool type.
4. **Sample description** — N, how selected, demographic composition, restriction-of-range description.
5. **Results** — raw and corrected validity coefficients, reliability estimates, adverse-impact ratios and significance tests for every protected-group comparison with adequate N.
6. **Fairness and alternative-procedures review** — differential prediction check (does the regression line differ by subgroup?), lower-impact alternatives considered and why rejected or adopted.
7. **Operational recommendation** — cut score or banding method, monitoring cadence, revalidation trigger (job change, applicant-pool shift, elapsed time).

## Rater calibration check (performance-rating criterion audit)

| Rater | N rated | % rated "exceeds" | % rated "meets" | % rated "below" | Flag? |
|---|---|---|---|---|---|
| Manager A | 22 | 91% | 9% | 0% | **Yes — leniency** |
| Manager B | 18 | 44% | 50% | 6% | No |
| Manager C | 25 | 40% | 52% | 8% | No |
| Manager D | 20 | 85% | 15% | 0% | **Yes — leniency** |

Threshold: any rater with >80% top-category ratings and 0% bottom-category flags for calibration review before that rater's ratings are trusted as validation criterion data — leniency this skewed compresses variance and biases the validity coefficient toward zero, understating the predictor.
