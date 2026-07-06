# Compensation & benefits artifacts — templates with real structure

Working templates an agent can fill in. Example numbers throughout follow the Software Engineer III job family from SKILL.md's worked example (45 incumbents, current midpoint $140,000) plus a separate benefits-renewal example noted where it starts.

## 1. Market pricing worksheet

One row per benchmark job. `$/point` = (P75 − P50) ÷ 25, used to interpolate any target percentile between P50 and P75.

| Field | Value |
|---|---|
| Job title (internal) | Software Engineer III |
| Survey source | Radford Global Technology Survey, US National Cut |
| Benchmark match | Software Engineer — Career Level P3 (Individual Contributor track) |
| Match quality | Direct (>85% duty overlap with survey job description) |
| Survey P25 | $128,000 |
| Survey P50 | $145,000 |
| Survey P75 | $170,000 |
| $/point (P50→P75) | ($170,000 − $145,000) ÷ 25 = $1,000/point |
| Stated philosophy for this family | P60 (moderate attrition risk, not top-decile critical) |
| Target midpoint | $145,000 + (60−50) × $1,000 = **$155,000** |
| Current midpoint | $140,000 |
| Δ vs. current | +10.7% — exceeds 6–8% single-cycle threshold, phase over 2 cycles |

**Percentile philosophy reference (interpolate linearly between the two nearest survey points you have):**

| Philosophy | Typical use case |
|---|---|
| P25 (lag) | Cost-constrained roles, high local labor supply, low criticality |
| P50 (match) | Default for most job families absent a specific reason to move off it |
| P60–P65 (lead-lag blend) | Moderate attrition risk or moderately hard-to-fill |
| P75 (lead) | Named critical/hard-to-fill roles only — applying broadly inflates budget for marginal retention gain |

## 2. Compa-ratio & range-penetration table

Band: min = 80% of midpoint, max = 120% of midpoint (40% spread). Compa-ratio = base salary ÷ midpoint. Range penetration = (base − min) ÷ (max − min).

**Current band (mid $140,000, min $112,000, max $168,000):**

| Employee | Base | Compa-ratio | Zone | Tenure |
|---|---|---|---|---|
| Priya | $118,000 | 0.843 | Q1 (developing) | 8 mo |
| Sarah | $135,000 | 0.964 | Q3 (fully proficient) | 4.2 yr |
| Marcus | $152,000 | 1.086 | Q3–Q4 | 6.1 yr |
| David | $171,000 | 1.221 | Above max (red-circle candidate) | 9.5 yr |

**Proposed band (mid $155,000, min $124,000, max $186,000) — same salaries, band moved:**

| Employee | Base | New compa-ratio | Zone shift |
|---|---|---|---|
| Priya | $118,000 | 0.761 | Drops below min — priority increase candidate |
| Sarah | $135,000 | 0.871 | Q3 → Q1, no pay change (the "silent demotion" effect) |
| Marcus | $152,000 | 0.981 | Q3–Q4 → Q2–Q3 |
| David | $171,000 | 1.103 | Above max → within band, red-circle resolved |

**Compa-ratio zone reference:** Q1 80–90% (developing) · Q2 90–100% (proficient) · Q3 100–110% (fully proficient/market rate) · Q4 110–120% (expert/top performer ceiling). Below 80% on a tenured (2+ yr) employee = unexplained-gap flag, not normal early-career positioning. Above 120% = red-circle: freeze increases until the band catches up, don't cut pay.

## 3. Pay-equity regression output

Model: `ln(base_salary) = β0 + β1(tenure_years) + β2(performance_rating) + β3(prior_level_tenure) + β4(location_tier) + β5(gender) + ε`, run on the 45-person Software Engineer III cohort.

| Variable | Coefficient | Std. error | p-value | Interpretation |
|---|---|---|---|---|
| Tenure (years) | +0.018 | 0.004 | <0.01 | Each year of tenure associated with ~1.8% higher pay, holding other factors constant |
| Performance rating (1–5) | +0.041 | 0.011 | <0.01 | Each rating point ~4.1% higher pay |
| Prior-level tenure | +0.009 | 0.006 | 0.14 | Not significant — small, noisy effect |
| Location tier (1=HCOL) | +0.052 | 0.019 | 0.02 | HCOL location ~5.2% higher pay |
| **Gender (1=woman)** | **−0.031** | **0.015** | **0.04** | **Statistically significant 3.1% unexplained gap, women paid less, controlling for the above** |
| Model R² | **0.81** | — | — | Above the 0.70 reliability threshold — trust the coefficients |

**Remediation calculation:** 12 women in the cohort, average base $138,000. 3.1% × $138,000 ≈ $4,280/employee × 12 = **$51,336** total remediation budget.

**When R² comes back below 0.70:** stop before reading any coefficient. Add the missing legitimate factors first — most commonly job level/grade (if the cohort spans more than one level), function/business unit, and a cleaner tenure measure (time-in-role vs. time-in-company are different variables). Only re-run the coefficient read once R² clears ~0.70.

**Cohort (not regression) fallback**, for cells under ~30 observations: group into similarly-situated-employee-groups (same job title + level + location tier), compare mean/median pay within each group by protected class, and flag any group with a gap exceeding 5% — smaller cells can't support a reliable regression coefficient, but a raw within-cell comparison is still directionally useful.

## 4. FLSA job-architecture duties-test decision tree

Built once per job family, revisited on scope-change or a 3-year cycle — distinct from hr-specialist's individual-case duties-test recheck for one employee's drifted role.

**Job family: "Store Manager" (I / II / III), 210 incumbents across all levels.**

| Question | Store Manager I | Store Manager II | Store Manager III |
|---|---|---|---|
| Primary duty is managing the enterprise or a recognized department? (29 CFR §541.100) | No — floor coverage is primary duty | Borderline — ~50/50 floor vs. management | Yes — management is primary duty |
| Customarily/regularly directs work of 2+ FTEs? | No | Yes (2–4 direct reports) | Yes (5+ direct reports) |
| Authority to hire/fire, or recommendations given particular weight? | No | Recommendations weighted, not final say | Yes, final hire/fire authority |
| Meets salary-level threshold ($684/wk federal floor, higher in some states)? | N/A (paid hourly) | Yes | Yes |
| **Classification** | **Non-exempt** | **Exempt (executive) — borderline, monitor scope** | **Exempt (executive)** |

**Family-level flag:** if more than ~15% of a nominally-exempt level's incumbents fall on the "No" side of the primary-duty question in a duties-test sampling audit, the level's classification itself is drifting, not just individual employees — that's a job-architecture reclassification project (this role's scope), separate from hr-specialist correcting one employee's individual drift.

## 5. Benefits cost model — loss ratio & self-funded vs. fully insured

**Fully insured renewal trend (medical plan, 850 covered lives):**

| Renewal cycle | Premium PEPM | Claims PEPM | Loss ratio | Carrier renewal ask |
|---|---|---|---|---|
| Year 1 | $720 | $612 | 85.0% | — |
| Year 2 | $760 | $665 | 87.5% | +5.6% |
| Year 3 | $810 | $731 | 90.2% | +6.6% |

Loss ratio above ~85% for two consecutive cycles (years 2–3 here) is the trigger to model self-funding, not just accept the renewal. ACA MLR floor for large-group carriers is 85% — a carrier running above that on your block specifically (not their whole book) is pricing your risk at cost or worse, and the renewal ask reflects it.

**Self-funded feasibility at 850 lives:** specific stop-loss attachment point typically set $100,000–$150,000 per individual claim; aggregate stop-loss caps total plan liability near 125% of expected claims. At this population size (well above the ~100-life threshold where self-funding economics typically start favoring the employer), modeled annual savings ≈ carrier's retention/margin load (typically 12–18% of premium) minus the stop-loss premium cost — model both before recommending a switch, since a bad claims year under-covered by a too-high attachment point can wipe out the modeled savings in one year.
