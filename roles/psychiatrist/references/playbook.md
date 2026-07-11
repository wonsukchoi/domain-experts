# Playbook — differential build, psychopharm sequencing, risk assessment

Filled procedures an agent can execute or populate, not descriptions of them.

## 1. New-presentation differential build (first psychiatric contact)

| Step | Action | Threshold / decision rule |
|---|---|---|
| 1 | Collateral + timeline | Onset over days = suspect organic/substance/medical; onset over months-years with prior baseline = more likely primary psychiatric |
| 2 | Medical rule-out (if atypical age of onset, no psychiatric history, or acute/fluctuating course) | TSH, CBC, CMP, B12/folate, urine tox, RPR/HIV per history; head imaging if focal neuro signs or first-episode psychosis over age 40 |
| 3 | Substance timeline | Map substance use against symptom onset — symptoms starting within days of new use/withdrawal = substance-induced until >4 weeks of abstinence disproves it |
| 4 | DSM-5-TR criteria match | Symptom count AND duration AND functional impairment AND exclusion criteria all four must be satisfied — three of four is not a diagnosis |
| 5 | Differential ranking | List top 3 with the specific finding that would confirm or exclude each — not a bare list of names |

**Example filled differential (new-onset psychosis, age 22, 3-week course):**

| Rank | Diagnosis | Confirms if | Excludes if |
|---|---|---|---|
| 1 | Substance-induced psychotic disorder | Symptom onset within days of stimulant/cannabis use; resolves within 4 weeks of abstinence | Symptoms persist >4 weeks post-abstinence, confirmed by repeat urine tox |
| 2 | Brief psychotic disorder | Symptoms 1 day–1 month, full return to baseline | Symptoms exceed 1 month |
| 3 | Schizophreniform / early schizophrenia | Symptoms ≥1 month, active-phase symptoms (delusions/hallucinations/disorganized speech) present | No active-phase symptoms meeting Criterion A count |

## 2. Antidepressant trial sequencing (STAR*D-informed)

| Step | Trial | Adequate = | If remission (PHQ-9 <5) | If response, not remission (≥50% reduction) | If partial (20–49% reduction) | If non-response (<20%) |
|---|---|---|---|---|---|---|
| 1 | SSRI, e.g., sertraline 100–200mg or escitalopram 10–20mg | Full-dose range x 6–8 weeks | Continue x 6–12 months | Continue, reassess at 4 wk intervals | Augment (see table 3) | Switch to different class |
| 2 | If switched: SNRI (venlafaxine XR 150–225mg) or bupropion | Full-dose range x 6–8 weeks | Continue | Continue | Augment | Consider MAOI or ECT referral, reassess diagnosis |

Cumulative STAR*D remission rates by step (reference point, not a per-patient guarantee): ~33% step 1, cumulative ~50% by step 2, ~67% cumulative by step 4 — each successive step has lower per-step yield, which is why re-auditing diagnosis and adherence matters more than mechanically cycling agents.

## 3. Augmentation options at partial response (adequate trial, 20–49% reduction)

| Augmenting agent | Starting dose | Target / monitoring | First recheck |
|---|---|---|---|
| Lithium carbonate | 300mg BID (600mg/day) | Level target 0.6–0.8 mEq/L; BMP + TSH baseline | Level + BMP at day 5 (steady state ≈5 half-lives) |
| Aripiprazole | 2–5mg/day | Titrate by 2–5mg q1–2wk to max 15mg/day for augmentation | Akathisia check at 1–2 wk |
| Bupropion XL | 150mg/day | Titrate to 300mg/day at wk 2 if tolerated | Symptom recheck at 4 wk |
| Thyroid (T3) | 25mcg/day | Titrate to 25–50mcg/day | TSH/free T4 at 4–6 wk |

**Lithium dose-adjustment math (linear kinetics in typical range):** new dose = target level ÷ current level × current dose. Example: current 600mg/day → level 0.3 mEq/L, target 0.6 mEq/L → new dose = (0.6/0.3) × 600mg = 1200mg/day.

## 4. Structured risk assessment (every visit where risk is a live question)

Five data points, elicited in order, each recorded even if answer is negative:

1. **Ideation** — passive ("wish I wouldn't wake up") vs. active ("I think about ending my life")
2. **Intent** — does the patient intend to act on the ideation
3. **Plan** — specificity (method, timeframe, has patient taken steps like acquiring means)
4. **Means/access** — firearms in home, stockpiled medication, access to a specific method named in the plan
5. **Protective factors** — reasons for living, social support present today, ambivalence expressed, treatment engagement

**Disposition decision table:**

| Ideation | Plan | Means | Protective factors | Disposition |
|---|---|---|---|---|
| Passive only | None | N/A | Present, engaged | Outpatient, safety plan, close follow-up (1–2 wk) |
| Active | Vague/none | Limited | Present | Outpatient with safety plan + means restriction counseling, follow-up within days |
| Active | Specific | Available | Weak or absent | Evaluate for involuntary hold under jurisdiction's statutory criteria (danger to self/others or grave disability) |
| Active | Specific | Available, steps taken (e.g., acquired means) | Any | Emergency evaluation / hold regardless of stated protective factors — behavioral evidence overrides verbal reassurance |

## 5. Antipsychotic initiation and monitoring schedule

| Timepoint | Draw / measure |
|---|---|
| Baseline (before first dose, or within prior 3 months) | Weight/BMI, waist circumference, BP, fasting glucose, fasting lipid panel; ANC + genotype-based schedule if clozapine |
| 4 weeks | Weight/BMI, BP |
| 8 weeks | Weight/BMI, BP |
| 12 weeks | Weight/BMI, BP, fasting glucose, fasting lipids |
| Annually thereafter (quarterly weight) | Full metabolic panel repeat |
| Clozapine only | ANC weekly x 6 months → biweekly x 6 months → monthly indefinitely; ANC 500–999/µL = interrupt and monitor closely; ANC <500/µL = discontinue, do not rechallenge without hematology consult |

## 6. Handoff / consult note skeleton (fill, don't describe)

```
CONSULT REQUEST RESPONSE
Reason for consult: [one line]
Risk level: [low/moderate/high] — based on: [ideation/plan/means/protective factors, one line each]
Current safety plan: [specific, not "safety planned"]
Diagnostic impression: [primary + top differential + what would distinguish them]
Medication recommendation: [drug, dose, titration schedule, monitoring parameter, recheck date]
Follow-up: [who, when, what trigger prompts earlier contact]
```
