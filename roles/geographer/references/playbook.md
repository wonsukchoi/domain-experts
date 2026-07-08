# Playbook

Filled workflows extending the SKILL.md worked example (8-county opioid mortality dataset: A-H, populations, deaths, rates per 100k, rook contiguity in a 2×4 grid). Load this when the task requires the full computation, not just the method name.

## 1. Full Getis-Ord Gi* table (all 8 counties)

Gi* (with self included) = [Σj wij·xj − x̄·Σwij] / [S·√((n·Σwij² − (Σwij)²)/(n−1))], x̄ = 55.75, S = 30.173, n = 8. Corner counties (A, D, E, H) have a local set of 3 (2 rook neighbors + self); edge counties (B, C, F, G) have a local set of 4 (3 neighbors + self).

| County | Local set | Σ values | Numerator | Denominator | Gi* z | Call |
|---|---|---|---|---|---|---|
| A | A,B,E | 183 | 15.75 | 44.166 | 0.36 | not significant |
| B | A,B,C,F | 238 | 15.00 | 45.615 | 0.33 | not significant |
| C | B,C,D,G | 203 | -20.00 | 45.615 | -0.44 | not significant |
| D | C,D,H | 78 | -89.25 | 44.166 | **-2.02** | **cold spot (95%)** |
| E | A,E,F | 228 | 60.75 | 44.166 | 1.38 | not significant |
| F | B,E,F,G | 323 | 100.00 | 45.615 | **2.19** | **hot spot (95%)** |
| G | C,F,G,H | 248 | 25.00 | 45.615 | 0.55 | not significant |
| H | D,G,H | 120 | -47.25 | 44.166 | -1.07 | not significant |

Only F and D clear the ±1.96 threshold. E (z = 1.38) sits inside the hot cluster visually but is not statistically distinguishable from random arrangement on its own — it borrows significance from being adjacent to F, not from its own local sum. This is the standard behavior of a distance/contiguity-based local statistic: don't read every visually warm-colored unit on a LISA/Gi* map as individually significant — check the z-score column, not the fill color, before naming a specific county in a funding recommendation.

## 2. MAUP demonstration — re-aggregating the same 8 counties

Collapse the grid into two 4-county regions along the row boundary already used for contiguity (North = E,F,G,H; South = A,B,C,D):

| Region | Pop | Deaths | Rate /100k |
|---|---|---|---|
| North (E,F,G,H) | 210,000 | 177 | 84.29 |
| South (A,B,C,D) | 200,000 | 89 | 44.50 |

At this aggregation the story is a clean binary: "North is nearly double South." But the county-level Gi* table above shows the real structure is not North-vs-South — it's a single hot spot (F) and a single cold spot (D), and D's cold spot (South, rate 15) is statistically identical to H's rate (North, rate 15, non-significant on its own because its neighbors are less extreme). Collapsing to two regions erases the fact that the North region's headline rate is being pulled up almost entirely by F and G, while H inside "North" is running as cold as D in "South." Any funding rule keyed to the 2-region aggregation (e.g., "North gets double the South's allocation") would misallocate relative to the county-level evidence. Always report which aggregation a headline statistic was computed at, and re-run at a second scale before a policy conclusion goes out the door.

## 3. Empirical Bayes rate smoothing (Clayton-Kaldor / Marshall method-of-moments)

Purpose: a raw rate from a small event count (D and H: 3 deaths on 20,000 population each) carries sampling variance that can dominate true geographic signal. Shrink it toward the global mean, weighted by how much true between-county variance exists relative to that county's own sampling noise.

Per-county Poisson variance of the rate (per 100k units): Var(Ri) = di · (100,000/popi)².

| County | di | popi | k=100,000/popi | Var(Ri) | Weight (pop/Σpop) |
|---|---|---|---|---|---|
| A | 27 | 60,000 | 1.6667 | 75.00 | 0.14634 |
| B | 35 | 70,000 | 1.4286 | 71.43 | 0.17073 |
| C | 24 | 50,000 | 2.0000 | 96.00 | 0.12195 |
| D | 3 | 20,000 | 5.0000 | 75.00 | 0.04878 |
| E | 44 | 50,000 | 2.0000 | 176.00 | 0.12195 |
| F | 76 | 80,000 | 1.2500 | 118.75 | 0.19512 |
| G | 54 | 60,000 | 1.6667 | 150.00 | 0.14634 |
| H | 3 | 20,000 | 5.0000 | 75.00 | 0.04878 |

Global rate R̄ = 266 total deaths / 410,000 total pop × 100,000 = 64.878.
Population-weighted average within-variance = Σ weighti·Var(Ri) ≈ **108.78**.
Population-weighted variance of the raw rates around R̄ ≈ **707.69**.
Between-county variance (method of moments) = 707.69 − 108.78 = **598.91**.

Shrinkage weight wi = Between / (Between + Var(Ri)):
- D: w = 598.91 / (598.91 + 75.00) = **0.8887**
- F: w = 598.91 / (598.91 + 118.75) = **0.8345**

Smoothed rate = wi·Ri + (1−wi)·R̄:
- D: 0.8887 × 15.0 + 0.1113 × 64.878 = 13.33 + 7.22 = **20.55**
- F: 0.8345 × 95.0 + 0.1655 × 64.878 = 79.28 + 10.74 = **90.02**

Both counties shrink only modestly (D moves from 15.0 to 20.55, F barely moves from 95.0 to 90.02) because the between-county variance (598.91) dominates each county's own sampling noise — the method correctly concludes most of the observed spread is real geographic signal, not small-number noise, which is consistent with D and F both being the only two Gi*-significant counties. Report both the raw and smoothed rate when a unit's event count is under ~20; if the smoothing had instead pulled D sharply toward 64.878, that would be the signal to *not* name it in a funding memo without a larger sample.

## 4. Kernel density estimation — point-pattern example

Scenario: 6 pedestrian-crash locations along a corridor, positions in meters from corridor start: 120, 340, 360, 380, 900, 950. Estimate crash density at query point x0 = 350 m.

**Bandwidth (Silverman's rule of thumb):** h = 0.9 · min(σ, IQR/1.34) · n^(-1/5).
σ = 307.16 (sample SD of the 6 positions). Q1 = 285, Q3 = 912.5 (linear interpolation), IQR = 627.5, IQR/1.34 = 468.28. min(307.16, 468.28) = 307.16.
n^(-1/5) = 6^(-0.2) = 0.6989.
h = 0.9 × 307.16 × 0.6989 = **193.2 m**.

**Gaussian kernel density at x0 = 350:** f(x0) = (1/(n·h)) Σ K((x0−xi)/h), K(u) = (1/√2π)·e^(−u²/2).

| xi | u = (350−xi)/h | K(u) |
|---|---|---|
| 120 | 1.1905 | 0.19645 |
| 340 | 0.0518 | 0.39841 |
| 360 | -0.0518 | 0.39841 |
| 380 | -0.1553 | 0.39415 |
| 900 | -2.8468 | 0.00693 |
| 950 | -3.1056 | 0.00321 |

ΣK(u) = 1.39756. f(350) = 1.39756 / (6 × 193.2) = 1.39756 / 1159.2 = **0.0012057 crashes/m**.

The three clustered points (340, 360, 380) contribute 1.19 of the 1.398 total kernel weight — about 85% — while the two isolated points near 900-950 contribute under 1%. The bandwidth (193 m) is wide enough to merge the three close points into one continuous density peak centered near 350-360 m, which is the correct behavior for flagging a corridor segment for engineering review; a bandwidth much narrower than 193 m would show three separate small bumps and understate that they're one cluster, and a much wider bandwidth would smear the peak into the isolated points and hide the cluster's edges. Re-run at 0.5h and 2h as a sensitivity check before naming a specific segment in a report — KDE hot spots are visually persuasive and bandwidth-sensitive in roughly equal measure.

## 5. OLS vs. spatial lag vs. spatial error — decision sequence

1. Fit OLS. Compute Moran's I on the OLS residuals (not the raw dependent variable — residual autocorrelation is what invalidates the model's standard errors).
2. If residual Moran's I is not significant, OLS coefficients and standard errors stand.
3. If residual Moran's I is significant, run the Lagrange Multiplier (LM) diagnostics for both the lag and error specifications (available in GeoDa/PySAL `spreg` output alongside OLS).
4. LM-lag significant, LM-error not (or robust LM-lag > robust LM-error) → fit a spatial lag model (neighboring values of the *dependent* variable enter as a regressor — appropriate when the process itself diffuses across boundaries, e.g. a housing-price spillover).
5. LM-error significant, LM-lag not (or the reverse ranking) → fit a spatial error model (spatial dependence lives in unobserved/omitted variables, not a diffusion process) — appropriate when the autocorrelation is plausibly a stand-in for an unmeasured regional covariate.
6. If a LISA/Gi* map shows the *relationship's* sign or strength (not just the outcome variable) visibly varies by region, prefer geographically weighted regression (GWR) over either global spatial model, and choose its bandwidth by cross-validated AICc rather than a fixed default.
