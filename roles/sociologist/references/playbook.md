# Sociologist — Playbook

## Codebook development sequence

1. **Draft codebook v1 from theory + pilot reading.** 8-15 codes for a first pass; each code gets a one-sentence operational definition and one included/one excluded example, not just a label.
2. **Double-code a pilot batch (10-20% of planned sample, minimum 10 units).** Two coders work independently, no discussion until both finish.
3. **Compute Cohen's kappa per code.** Interpretation bands (Landis & Koch, 1977, stated heuristic):

| Kappa | Interpretation | Action |
|---|---|---|
| < 0.40 | Poor | Redefine the code's boundary — the concept as written isn't coherent to two independent readers |
| 0.40-0.59 | Fair | Revise definition, add a worked example, retrain, re-pilot |
| 0.60-0.79 | Good | Acceptable for a single-coder-with-spot-check design |
| >= 0.80 | Excellent | Acceptable for any design, including fully independent double-coding |

4. **Revise codes below 0.60**, re-pilot on the same batch, recompute. Repeat once; if still below 0.60 after one revision, the code is likely two codes merged (see worked example) or not a codeable construct — drop or fundamentally redesign it, don't force a third revision cycle.
5. **Scale to full sample** once all codes clear 0.60, with periodic spot-check double-coding (5-10% of remaining transcripts) to catch coder drift over a long project.

## Intercoder reliability worksheet (filled example)

| Code | Coder A yes | Coder B yes | Both yes | Both no | Po | Pe | Kappa | Action |
|---|---|---|---|---|---|---|---|---|
| Identity loss (v1) | 11/15 | 8/15 | 7 | 3 | 0.667 | 0.516 | 0.31 | Split code |
| Professional identity loss (v2) | 10/15 | 10/15 | 9 | 4 | 0.867 | 0.556 | 0.70 | Proceed |
| Provider-role loss (v2) | 9/15 | 9/15 | 8 | 6 | 0.933 | 0.520 | 0.86 | Proceed |
| Financial anxiety | 12/15 | 11/15 | 9 | 1 | 0.667 | 0.640 | 0.07 | Revise — likely conflated with "identity loss," check definitional overlap |

## Mixed-methods triangulation template

| Finding | Quant signal | Qual signal | Agreement? | Interpretation |
|---|---|---|---|---|
| Reemployment predicts wellbeing | Survey: reemployed workers report 1.4pt higher life-satisfaction (10pt scale), p<.01 | Interviews: reemployed workers describe relief but many still report grief over craft-identity loss | Partial | Quant captures the average effect; qual shows the mechanism is incomplete — income/routine recovers, identity doesn't fully |
| Union membership buffers income shock | Survey: union members report 18% smaller income drop post-layoff | Interviews: union members describe severance negotiation and job-placement-service access as the proximate cause | Consistent | Union effect operates through concrete institutional resources, not solidarity/morale as initially hypothesized |
| Age predicts reemployment speed | Survey: workers 50+ take 3.2 months longer to reemploy | Interviews: workers 50+ describe both employer age discrimination and self-selecting out of retraining | Consistent, mechanism split | Report both mechanisms — policy response differs (anti-discrimination enforcement vs. retraining incentive design) depending on which dominates |

When quant and qual disagree outright (a survey shows no group difference but interviews surface a strong theme in one subgroup), report the disagreement explicitly rather than picking the "stronger" method — it usually means the quant measure isn't capturing the qual mechanism, which is itself a finding about measurement validity.

## Age-period-cohort screening checklist

Before claiming a generational difference from repeated cross-sectional data:

- [ ] At least 3 distinct cohorts and 3 distinct survey periods available (2x2 is underidentified — APC requires enough cells to separate the three effects)
- [ ] Same-age comparison run across survey years (controls for period holding age constant)
- [ ] Same-cohort comparison run across ages (controls for cohort holding period constant)
- [ ] Explicit statement of which of the three effects (age/period/cohort) the finding is attributed to, and why the data can identify that one specifically
