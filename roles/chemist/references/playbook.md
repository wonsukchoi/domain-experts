# Chemist — Playbook

## Method validation parameter table (ICH Q2(R1), filled example)

| Parameter | Acceptance criterion | Result | Pass/Fail |
|---|---|---|---|
| Specificity | Resolution Rs ≥1.5 from nearest peak/degradant; PDA peak-purity angle < threshold angle | Rs=1.8; purity angle 2.1° < 3.2° threshold | Pass |
| Accuracy | Mean recovery 98–102% at 3 levels (0.5x, 1x, 2x spec) | 98.6% / 101.2% / 99.4% (mean 99.7%) | Pass |
| Precision (repeatability) | %RSD ≤2.0%, n≥6 | 0.91% (n=6) | Pass |
| Linearity | R² ≥0.999 across validated range | R²=0.9993, range 0.03–0.45% | Pass |
| LOD | Report value (S/N=3) | 0.018% | — |
| LOQ | Report value (S/N=10); must be ≤ spec limit | 0.060% ≤ 0.15% spec | Pass |
| Robustness | ≤5% result variance across deliberate small parameter changes (flow ±0.1 mL/min, temp ±2°C, %B ±2%) | Max variance observed 3.2% | Pass |

Sequencing rule: run specificity before every other parameter. A method that fails specificity invalidates accuracy/precision data collected under it — those numbers describe a co-eluting mixture, not the analyte.

## Yield / mass-balance reconciliation (filled example)

Target: 50.0 mmol scale synthesis of Compound Z. Theoretical yield = 50.0 mmol × 284.3 g/mol = 14.22 g.

| Stage | Measured | % of theoretical | Cumulative loss accounted for |
|---|---|---|---|
| Reaction conversion (in-process HPLC, % starting material consumed) | 96.5% converted | — | 3.5% unreacted SM (recovered, not lost) |
| Crude isolated mass (post-workup) | 13.10 g | 92.1% | 4.4% lost in aqueous workup (emulsion, partial extraction) |
| Post-purification (column) mass | 11.87 g | 83.5% | 8.6% lost in purification (co-eluting fractions discarded) |
| Isolated purity (HPLC area%) | 98.7% | — | — |
| **Corrected pure-compound yield** | 11.87 g × 0.987 = 11.72 g | **82.4%** | Total loss 17.6%: 4.4% workup + 8.6% purification + ~4.6% purity-correction/rounding |

Read: 82.4% isolated yield is not "chemistry gave 82%" — it's 96.5% conversion minus a specific, traceable 14.1 percentage points across workup and purification. If scaling this route, the purification loss (8.6%, the single largest line item) is the first target for optimization, not the reaction itself.

## OOS investigation flow (filled example)

1. **Confirm the failing result is real, not transcription/instrument.** Check integration, injection sequence, and raw chromatogram for the failing sample — 22% of initial OOS flags in this lab's historical data resolved at this step (mis-integration).
2. **Check system suitability from the same sequence.** If system suitability passed, the instrument was performing to spec during the run — points toward sample, not system.
3. **Repeat sample preparation from the same physical sample** (not a new pull) if enough material remains. A second prep giving a passing result with the *same* sample points to a prep error (dilution, weighing); a second prep confirming the failure points to a genuine product issue.
4. **Only after root cause is documented** — instrument malfunction (invalidate, rerun), prep error (invalidate, rerun), or genuine OOS (confirmed) — proceed to next step per site SOP (retest per approved plan, or escalate as a confirmed OOS requiring disposition decision by QA).
5. **Never** average a failing initial result with a later passing result to compute a reportable mean without a documented, approved investigation justifying exclusion of the original result.
