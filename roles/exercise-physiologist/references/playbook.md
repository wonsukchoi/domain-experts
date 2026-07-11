# Exercise physiology playbook

Filled reference tables and step sequences — populate with a real patient's numbers, don't just describe the categories.

## 1. GXT protocol selection

| Patient profile | Protocol | Stage structure | Why |
|---|---|---|---|
| Healthy or well-conditioned, screening only | Standard Bruce | 3-min stages, ~3 MET jumps (1.7mph/10% → 2.5mph/12% → 3.4mph/14%...) | Fast to a diagnostic endpoint; large jumps are fine when the ceiling is high |
| Deconditioned, elderly, early post-MI, or heart failure | Modified/low-level Bruce | Adds 0% and 5%-grade warm-up stages (1.7mph/0%, 1.7mph/5%) before standard Stage 1 | Avoids skipping over a low true threshold with the first stage already at 3 METs |
| Frailty, orthopedic limits on treadmill walking, or need for finer resolution | Naughton or ramp cycle ergometry | ~1 MET/stage (Naughton) or continuous ~10–25W/min ramp | Finds the ischemic/symptom threshold within a narrow band instead of bracketing it |
| Pulmonary disease, functional tracking rather than diagnostic ceiling | 6-Minute Walk Test (ATS protocol) | Self-paced, flat 30m corridor, standardized encouragement phrases only | Reflects submaximal functional capacity relevant to daily activity, not peak cardiac ceiling |

**Functional capacity from a standard/modified Bruce time** (Foster et al. 1984 regression, T = minutes on protocol):
`VO2 (ml/kg/min) = 14.76 − (1.379 × T) + (0.451 × T²) − (0.012 × T³)`; METs = VO2 / 3.5.

## 2. AACVPR risk stratification (applied at program entry)

| Category | Typical entry criteria (any one qualifies) | Required monitoring |
|---|---|---|
| Low | Uncomplicated MI/revascularization, EF ≥50%, no exercise-induced ischemia or arrhythmia, normal hemodynamic response, functional capacity ≥7 METs, no significant CHF | Supervised, ECG spot-checks; telemetry not required past session 1–2 |
| Moderate | EF 40–49%, or exercise capacity <5–7 METs without other high-risk markers, or mild-to-moderate silent ischemia | Continuous telemetry for at least the first 6 sessions or until a stable response is documented |
| High | EF <40%, survived cardiac arrest/sudden death, complex ventricular arrhythmias, exercise-induced ischemia or hypotensive BP response, uncontrolled heart failure symptoms | Continuous telemetry for 12+ sessions or until physician documents step-down; 1:1 or near-1:1 supervision ratio |

First question when the category is ambiguous: "which single criterion pushed this patient up a tier, and has the supervising physician signed off on the resulting monitoring plan?"

## 3. Intensity prescription build (fill in per patient)

1. Pull measured peak HR and termination reason from the GXT — not an age-predicted number.
2. Compute HRR = peak HR − resting HR (resting HR taken on the patient's current medication regimen).
3. Pick the % HRR band for program phase:
   - Early phase II (weeks 1–2, post-acute-event): 40–60% HRR
   - Established phase II (weeks 3+, tolerating current load): 50–70% HRR
   - Phase III/maintenance (independent, stable): 60–80% HRR
4. Target HR = resting HR + (%HRR low × HRR) to resting HR + (%HRR high × HRR).
5. Cross-check against Borg RPE 6–20 scale: 11–13 for early phase, 12–14 established, 13–15 maintenance. If HR-based and RPE-based targets disagree by more than one RPE-equivalent step, trust RPE when a chronotropic-limiting factor (beta blocker, pacemaker, AFib) is present.

**Worked fill-in example** (from SKILL.md worked example): peak HR 118, resting HR 62, HRR 56, early-phase band 40–60% → target HR 84–96 bpm, cross-checked RPE 11–13.

## 4. Progression / hold / regress rule

| Observation across the last 2 sessions | Action |
|---|---|
| Target workload completed, no symptom, BP/HR response normal | Advance %HRR band by ~5 points and/or +5 min duration (not both same step) |
| Target workload completed but RPE trending up (e.g., 11→14) at same load | Hold current load one more session cycle before advancing |
| Missed target workload, or any BP/HR abnormality, or new symptom | Hold at last-tolerated load; reset the "2 consecutive good sessions" counter to zero |
| Absolute termination indication occurred | Stop program advancement entirely; physician review before any further exercise session |

## 5. Functional-capacity retest cadence and MCID comparison

| Test | Retest interval | MCID to clear before calling it a real change |
|---|---|---|
| 6MWT — COPD | Every 4 weeks | 54–80 m |
| 6MWT — heart failure | Every 4 weeks | ~25–33 m |
| GXT-derived METs — cardiac rehab | Program entry, mid-program (~week 6), discharge | No universal MCID; compare against the patient's own entry value and flag any METs decline regardless of magnitude for physician review |

Always take the second of two baseline 6MWTs as the reference value — the first test alone reflects unfamiliarity with the corridor and pacing as much as fitness.
