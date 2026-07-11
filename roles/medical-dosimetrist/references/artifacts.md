# Artifacts — filled templates a dosimetrist actually produces

Real structures with plausible numbers. Populate directly; don't treat these as descriptions of what a table should contain.

## 1. Site-specific dose-volume constraint table (starting point, adjust per protocol)

Prostate, conventional fractionation, 78 Gy/39 fx (2 Gy/fx):

| Structure | Metric | Constraint | Source |
|---|---|---|---|
| PTV | D95 | ≥ 95% of Rx (73.9 Gy) unless overlap trade documented | Dept. protocol |
| PTV | Max dose (D2 or D0.03cc) | ≤ 107% of Rx (83.5 Gy) | ICRU 83 |
| Rectum | V70 | < 20% | QUANTEC (Marks 2010) |
| Rectum | V75 | < 15% | QUANTEC |
| Bladder | V65 | < 50% | QUANTEC |
| Bladder | V80 | < 15% | QUANTEC |
| Femoral heads | V50 | < 5% | Dept. protocol |

Whole-breast tangential, 40.05 Gy/15 fx (hypofractionated, START-B regimen):

| Structure | Metric | Constraint | Source |
|---|---|---|---|
| PTV (breast) | D95 | ≥ 95% of Rx | Dept. protocol |
| Ipsilateral lung | V17 (Gy) | < 15–20% | Dept. protocol (scaled from conventional V20<30%) |
| Heart (left-sided only) | Mean dose | < 4 Gy (DIBH target), flag if > 7 Gy | Darby et al. NEJM 2013 dose-response |
| Contralateral breast | Mean dose | < 1 Gy | ALARA / Dept. protocol |

Head & neck IMRT/VMAT, 70 Gy/35 fx to gross disease, 56–63 Gy/35 fx elective:

| Structure | Metric | Constraint | Source |
|---|---|---|---|
| PTV70 | D95 | ≥ 95% of Rx | ICRU 83 |
| Spinal cord | Max (D0.03cc) | < 45 Gy | QUANTEC |
| Brainstem | Max (D0.03cc) | < 54 Gy | QUANTEC |
| Parotid (contralateral) | Mean dose | < 25 Gy | QUANTEC |
| Larynx (if not target) | Mean dose | < 45 Gy | Dept. protocol |

## 2. Optimization objective priority ladder (fill per case, example shown = prostate VMAT)

1. Spinal cord / brainstem / other serial-organ max dose (if present in field) — non-negotiable ceiling.
2. Rectum V70 < 20%, V75 < 15% — escalate to physician if conflicts with PTV coverage.
3. PTV D95 ≥ 95% (whole volume); in a documented overlap subvolume, D98 ≥ 90% is an acceptable trade if approved.
4. Bladder V65 < 50%, V80 < 15%.
5. Conformity index (target 1.05–1.2) and homogeneity index (target < 0.10) — tiebreakers only, never traded against 1–4.
6. Minimize monitor units / modulation factor for deliverability once 1–5 are satisfied.

## 3. Plan-check / physics handoff note (filled example)

```
PATIENT: [ID]           SITE: Prostate            Rx: 78 Gy / 39 fx
PLAN: VMAT, 2 arcs, 6 MV FFF
-----------------------------------------------------------
PTV coverage:        D95 = 94.8% (73.9 Gy) — whole volume
                      D98 (overlap subvolume, 8cc) = 91% (71.0 Gy)
                      Max dose = 105.2% (82.1 Gy), located inside PTV
OAR results:          Rectum V70 = 17% (target <20%) — PASS
                      Rectum V75 = 11% (target <15%) — PASS
                      Bladder V65 = 42% (target <50%) — PASS
                      Femoral heads V50 = 2.1% (target <5%) — PASS
Deliverability:       Total MU = 612/arc, modulation factor 4.1 — within facility norm (<5.0)
                      Collision check: clear at all gantry/couch combinations used
Independent MU check: TPS 612 MU/arc vs. secondary calc 601 MU/arc — 1.8% difference,
                      within 3% tolerance — PASS
Overlap trade note:   Approved by Dr. [name] on [date] per attached coverage/constraint
                      comparison (28% vs 17% rectum V70).
QA STATUS:            Pending — routed to physics [date]
```

## 4. Patient-specific QA report (filled example, TG-218 criteria)

```
QA METHOD: Portal dosimetry, per-arc analysis
CRITERIA: 3%/2mm local dose, 10% low-dose threshold, global normalization to max dose
RESULTS:
  Arc 1: 96.8% pass         Arc 2: 95.4% pass
ACTION LIMIT: <90% triggers investigation before treatment (TG-218)
RESULT: Both arcs pass; plan cleared for treatment.

[If either arc had come in at 88%:]
INVESTIGATION STEPS TAKEN:
  1. Reviewed MLC log files for leaf-position error trends — checked for systematic
     bias vs. random noise (systematic bias implicates calibration; random noise
     implicates plan complexity).
  2. Compared modulation factor (4.1) against facility's QA-failure-correlated
     threshold (historically, MF>4.5 correlates with higher failure rate here).
  3. Re-measured after MLC recalibration if log files showed systematic drift;
     re-optimized to reduce modulation if plan complexity was the driver.
  DO NOT simply re-measure without a root-cause note — a second passing measurement
  with no explanation just defers the same risk to fraction 1.
```

## 5. Fallback ladder for coverage vs. OAR constraint conflict (prostate example)

1. Localize the conflict to a specific overlap subvolume before trading anything globally.
2. Apply a lower-priority optimization objective to the overlap subvolume only; hold full coverage elsewhere.
3. If constraint still fails: present physician with 2–3 named tradeoff points (e.g., "V70 17% at D95 94.8%" vs. "V70 20% at D95 96%") and get an explicit choice.
4. If physician wants full coverage regardless: document the elevated toxicity-risk estimate in the chart and get written acknowledgment before treating.
5. Escalate to physics only for deliverability/QA issues, not for coverage-vs-constraint clinical tradeoffs — that decision belongs to the physician.
