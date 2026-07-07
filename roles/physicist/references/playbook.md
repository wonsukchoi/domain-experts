# Physicist — Playbook

## Error-budget worksheet (filled example, pendulum-g measurement)

| Source | Type | Estimate | Relative size | Notes |
|---|---|---|---|---|
| Timing (period, N=20 trials) | Statistical | SD 0.0032 s / √20 = 0.000716 s | 0.0712% (×2, since g∝1/T²) | Shrinks with more trials |
| Length calibration | Systematic | ±0.0005 m on 1.0000 m | 0.05% | Fixed — doesn't shrink with more trials |
| Amplitude-angle measurement | Systematic | θ₀ known to ±0.3°, propagated through correction term | ~0.01% | Only matters because of the θ₀²/16 correction |
| Air buoyancy / finite-wire mass | Systematic (budgeted) | Theory estimate | ~0.02% | Not measured directly — carried as a budgeted term |
| **Combined (quadrature, independent sources)** | — | √(0.0712²+0.05²+0.01²+0.02²) | **0.0898%** | Valid only if all four are truly independent |

Rule of thumb for when to stop taking more data: once the statistical row is smaller than the largest systematic row, additional trials shrink the total budget by less than 5% — redirect effort to characterizing systematics instead.

## χ²/dof worksheet (filled example)

| Trial | g_i (amplitude-corrected, m/s²) | Residual (g_i − ḡ) | Residual² |
|---|---|---|---|
| 1 | 9.798 | −0.005 | 0.000025 |
| 2 | 9.811 | +0.008 | 0.000064 |
| ... | ... | ... | ... |
| 20 | 9.806 | +0.003 | 0.000009 |
| **Sum** | — | — | **χ² = 18.3** |

- Degrees of freedom = N − (number of fitted parameters) = 20 − 1 = 19 (one parameter: the mean).
- χ²/dof = 18.3 / 19 = 0.96.
- Interpretation: 0.96 is close to 1 → the assumed per-trial timing uncertainty (used to weight each residual) matches the observed scatter. A value like 0.3 would mean the assumed per-trial error was too large (padding); a value like 3.0 would mean either the model is wrong or the per-trial error was underestimated.

## Blind-analysis checklist (filled example, small-signal search)

1. **Define the signal region and sidebands before any data is examined** — e.g., signal window = expected peak ± 2σ, sidebands = regions used to estimate background shape.
2. **Freeze all analysis cuts using sideband/simulation data only** — event-selection thresholds, binning, fit-model choice (e.g., linear vs. quadratic background) are all fixed before the signal region is unmasked.
3. **Document the freeze with a timestamp** — analysis-cut freeze log entry, e.g.: "2024-03-14 — cuts frozen: pT > 20 GeV, |η| < 2.4, background model = 2nd-order polynomial. Signal region [124, 126] GeV remains masked."
4. **Unmask and run the frozen procedure exactly as specified** — no post-hoc adjustment of cuts based on what the unmasked result shows.
5. **If a cut needs to change after unmasking, that constitutes a new analysis** — re-blind and re-freeze; a post-hoc cut change on already-seen data invalidates the significance calculation.

## Upper-limit reporting (filled example, null result)

Search yields 3 observed events in the signal region against an expected background of 4.2 ± 0.9 (statistical) ± 0.5 (systematic) events.

- Combined background uncertainty: √(0.9² + 0.5²) = 1.03 events (independent sources — statistical counting error and systematic background-model error).
- Observed (3) is consistent with background (4.2 ± 1.03) — no excess.
- 95% CL upper limit on signal yield, computed via the CLs method against this background model: **≤ 3.8 events** (illustrative — exact value depends on the statistical method and is computed with dedicated software, not by hand).

**Deliverable excerpt:** "No significant excess observed (3 events observed vs. 4.2 ± 1.03 expected background). We set a 95% CL upper limit of 3.8 events on the signal yield, corresponding to a cross-section limit of [value] under the assumed signal model."
