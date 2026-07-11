# Respiratory Therapist — Playbook

## Predicted body weight (PBW) worksheet

Male: PBW (kg) = 50 + 2.3 × (height in inches − 60)
Female: PBW (kg) = 45.5 + 2.3 × (height in inches − 60)

| Height | Sex | Calculation | PBW | Vt at 6 mL/kg | Vt at 4 mL/kg |
|---|---|---|---|---|---|
| 62 in | F | 45.5 + 2.3×2 = 45.5+4.6 | 50.1 kg | 301 mL | 200 mL |
| 66 in | F | 45.5 + 2.3×6 = 45.5+13.8 | 59.3 kg | 356 mL | 237 mL |
| 68 in | M | 50 + 2.3×8 = 50+18.4 | 68.4 kg | 410 mL | 274 mL |
| 70 in | M | 50 + 2.3×10 = 50+23 | 73.0 kg | 438 mL | 292 mL |
| 74 in | M | 50 + 2.3×14 = 50+32.2 | 82.2 kg | 493 mL | 329 mL |

Use height, not actual weight — an obese patient at 70 in and 140 kg actual weight still has a 73 kg PBW; ventilating at 6 mL/kg of actual weight (840 mL) would nearly double the lung-protective target.

## ARDSNet lower-PEEP/FiO2 table (starting reference)

| FiO2 | 0.3 | 0.4 | 0.4 | 0.5 | 0.5 | 0.6 | 0.7 | 0.7 | 0.7 | 0.8 | 0.9 | 0.9 | 0.9 | 1.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PEEP | 5 | 5 | 8 | 8 | 10 | 10 | 10 | 12 | 14 | 14 | 14 | 16 | 18 | 18–24 |

Higher-PEEP table (for more refractory hypoxemia) pairs the same FiO2 values with PEEP 5 higher on average at each step — institutional protocol determines which table applies; don't mix rows from both tables in one titration.

## Static compliance and driving-pressure worksheet

Static compliance = Vt ÷ (Pplat − PEEP). Driving pressure = Pplat − PEEP.

Worked: Vt 440 mL, Pplat 32, PEEP 10 → compliance = 0.440 ÷ 22 = 0.020 L/cmH2O (20 mL/cmH2O). To project the new plateau pressure at a smaller Vt with the same compliance: new Pplat = PEEP + (new Vt ÷ compliance). At Vt 365 mL: 10 + (0.365 ÷ 0.020) = 10 + 18.25 ≈ 28 cmH2O.

**Ceiling:** Pplat > 30 cmH2O → reduce Vt in 1 mL/kg PBW steps (down to a 4 mL/kg floor) and recheck. Pplat < 25 cmH2O with Vt already at 6 mL/kg → no forced reduction; some protocols allow titrating up to the 8 mL/kg ceiling with a low plateau if patient comfort or dyssynchrony demands it.

## Weaning-readiness screen and spontaneous breathing trial (SBT)

**Screen before attempting an SBT** (all should be true):
- FiO2 ≤ 0.4–0.5, PEEP ≤ 5–8 cmH2O, with adequate oxygenation (P/F > 150–200 or SpO2 ≥ 90% on those settings)
- Hemodynamically stable: no or minimal vasopressor requirement
- Adequate mental status: arousable, following commands (or at baseline for a chronic patient)
- Manageable secretions and an intact cough

**Weaning parameters (secondary screen, effort-dependent — interpret with clinical context):**

| Parameter | Threshold favoring wean | Caveat |
|---|---|---|
| Rapid shallow breathing index (f/Vt, Vt in liters) | < 105 | Most validated single predictor; still has false positives/negatives |
| Negative inspiratory force (NIF) | More negative than −20 to −30 cmH2O | Effort-dependent; poor effort looks identical to poor strength |
| Vital capacity | > 10 mL/kg PBW | Same effort-dependence caveat |

**SBT protocol:** 30–120 minutes on T-piece, CPAP ≤ 5 cmH2O, or low-level pressure support (5–8 cmH2O). Monitor continuously for: RR > 35/min or < 8/min, SpO2 < 90%, heart rate change > 20% from baseline, systolic BP change > 20%, diaphoresis, accessory muscle use, or mental-status change — any of these terminates the trial as a failure. At the end of a tolerated trial, calculate RSBI = RR ÷ Vt(L).

**Cuff leak test (high-risk patients — prior difficult intubation, prolonged intubation >6 days, traumatic intubation, large tube-to-airway ratio):** deflate cuff, measure exhaled Vt over several breaths; leak volume < 110 mL or < 15–20% of the pre-deflation Vt predicts a meaningfully elevated post-extubation stridor/reintubation risk — consider steroids pre-extubation or extubating to NIV standby.

## Extubation and weaning-trial documentation template (filled)

"SBT initiated [time], [duration] on [T-piece / CPAP X cmH2O / PSV X cmH2O]. Vitals stable throughout: RR [baseline]→[end], SpO2 [baseline]→[end]%, HR [baseline]→[end], no accessory muscle use, mental status unchanged. RSBI at trial end: [RR] ÷ [Vt in L] = [value] — [below/above] the 105 threshold. [Cuff leak test performed: leak volume [X] mL, [above/below] 110 mL threshold]. Extubated to [room air / HFNC at X L/min / NIV], tolerating well at [time + interval] recheck: SpO2 [value]%, RR [value], no stridor or increased work of breathing noted."
