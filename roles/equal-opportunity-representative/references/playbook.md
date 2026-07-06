# Equal Opportunity Representative — Playbook

## Four-fifths rule and significance test worksheet (filled example)

| Step | Value |
|---|---|
| Male applicants / hires | 120 / 24 |
| Female applicants / hires | 80 / 8 |
| Male selection rate | 24/120 = 20% |
| Female selection rate | 8/80 = 10% |
| Four-fifths ratio (female ÷ male) | 10% ÷ 20% = 50% |
| **Four-fifths result** | 50% < 80% → **adverse impact indicated** |
| Overall selection rate | 32/200 = 16% |
| Expected female hires at overall rate | 80 × 16% = 12.8 |
| Observed − expected | 8 − 12.8 = −4.8 |
| Standard deviation | √(120×80×0.16×0.84 ÷ 200) ≈ 2.54 |
| **Z-score** | −4.8 ÷ 2.54 ≈ **−1.89** |
| **Significance result** | \|Z\| = 1.89 < 2.0 threshold → **borderline, not conclusively significant** |
| **Combined interpretation** | Tests disagree — investigate at stage level, don't conclude either way from aggregate alone |

**Use:** Run both tests every time sample size supports the significance test — a four-fifths finding without a significance check (or vice versa) is an incomplete analysis.

## Stage-level breakdown (filled example, continuing above)

| Stage | Male rate | Female rate | Ratio | Flag? |
|---|---|---|---|---|
| Application → Interview | 45% | 43% | 96% | No |
| Interview → Offer | 44% | 23% | 52% | **Yes — below 80%** |
| Offer → Hire | 95% | 92% | 97% | No |

**Use:** The stage-level breakdown is what turns an aggregate finding into an actionable one — here, the disparity concentrates entirely in interview-to-offer, telling you exactly what process to review.

## Availability analysis worksheet (illustrative structure)

| Source | Weight (typical fill pattern for this job group) | Female availability % |
|---|---|---|
| External labor market (census/labor-force data for relevant job category and region) | 70% (job group is mostly external hire) | 22% |
| Internal promotable pool | 30% (some internal promotion occurs) | 15% |
| **Weighted availability** | | 0.70×22% + 0.30×15% = **19.9%** |
| Current incumbency in this job group | | 12% |

**Use:** Set the placement goal from the weighted availability figure (here, ~20%), not from the external-only or internal-only number alone, when the job group draws from both sources — and never from a general company-wide diversity aspiration untethered to this specific job group's data.

## Compensation equity regression checklist

1. Define the population (job group, level) being analyzed.
2. Collect compensation data along with legitimate factors: tenure, performance rating, education, job level, prior relevant experience.
3. Run a multiple regression with compensation as the outcome and the legitimate factors plus protected-class indicator as predictors.
4. Check whether the protected-class coefficient is statistically significant after controlling for the legitimate factors.
5. If significant, break down which specific roles, levels, or individuals contribute most to the gap — don't stop at the aggregate coefficient.
6. Document findings and any remediation (pay adjustment, further investigation) tied to the specific roles/individuals identified.

## Findings memo — filled example

> **Adverse Impact Analysis — Software Engineer II, Q[x] Hiring Cycle**
> Selection rates: Male 20% (24/120), Female 10% (8/80). Four-fifths ratio: 50% — **below 80% threshold, adverse impact indicated.**
> Statistical significance: Z = −1.89 — borderline, just under the ±2.0 significance threshold.
> Stage-level analysis: Application-to-interview rates comparable (45% vs. 43%); **interview-to-offer rates diverge sharply (44% vs. 23%)** — disparity is isolated to this stage.
> **Recommendation: Review interview-to-offer decision criteria and interviewer calibration for this requisition cycle before the next hiring round; continue monitoring at the stage level, not just the aggregate hire rate.**
