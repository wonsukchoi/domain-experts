# Atmospheric Scientist — Playbook

## Reliability-diagram calibration table (SREF severe-parameter agreement, 3-season sample)

| Raw ensemble agreement bin | Sample size (forecast-events) | Observed severe-report frequency | Calibration adjustment |
|---|---|---|---|
| 85-100% | 41 | 79% | -6 to -21 pp |
| 65-75% | 63 | 54% | -11 to -21 pp |
| 45-55% | 88 | 38% | -7 to -17 pp |
| 25-35% | 112 | 19% | -6 to -16 pp |
| 5-15% | 97 | 7% | -2 to -8 pp |

Rule: never quote raw agreement in a public product. Interpolate from this table (or the site's live reliability diagram) before comparing against an outlook or warning threshold. Rebuild this table each season — model versions change and stale calibration silently reintroduces the bias it was built to correct.

## Verification worksheet (post-event scoring)

For a defined warning polygon and event window:

| Outcome | Definition | This event |
|---|---|---|
| Hit (a) | Warning issued, event occurred in polygon | 1 |
| False alarm (b) | Warning issued, no event occurred | 0 |
| Miss (c) | No warning, event occurred | 0 |
| Correct negative (d) | No warning, no event | — (not scored per-event) |

- POD (probability of detection) = a / (a + c) = 1 / 1 = 100% for this event
- FAR (false alarm ratio) = b / (a + b) = 0 / 1 = 0% for this event
- CSI (critical success index) = a / (a + b + c) = 1 / 1 = 100% for this event

Aggregate these counts over a season, not a single event — single-event PODs of 100% or 0% are not meaningful; the metric is only informative pooled across dozens of warnings.

## Lead-time calculation

```
Lead time (minutes) = (distance from storm to point of interest, miles) / (storm speed, mph) x 60
```

Example: storm 18 miles out, moving at 40 mph → 18 / 40 x 60 = 27 minutes.

Compare against the hazard-specific national average lead-time benchmark (tornado ~13 minutes, flash flood ~machine-dependent on basin response time) to judge whether issuing now versus waiting for stronger confirmation (e.g., a spotter report) preserves an acceptable safety margin. If calculated lead time is already below the benchmark, issue immediately on radar signature alone — waiting for confirmation trades away the only lead time you have left.

## Forecast discussion (AFD) skeleton — filled example

```
.SYNOPSIS...
Upper low deepening over the region will support increasing
instability (SBCAPE 2000-2800 J/kg by peak heating) atop 45-55 kt
0-6km bulk shear -- combination favorable for organized severe,
including a low-end tornado threat with any discrete cells that can
separate from the line before upscale growth.

.DISCUSSION...
Model spread on timing has narrowed over the past two cycles (HRRR
and NAM now within 1 hour of each other on initiation, vs 3+ hours
24h ago) -- confidence in the 2-6 PM window is now higher than this
morning's discussion suggested. SREF member agreement on the severe
parameter space sits at 69%, which calibrates to ~54% observed
frequency per this season's reliability table -- supports an Enhanced
risk categorical rather than Moderate.

.IMPACTS...
Primary threat is damaging wind (70+ mph gusts) with isolated large
hail; low-end tornado threat where cells remain discrete. Confidence
in exact corridor placement is moderate -- expect the watch box to be
wider than the eventual warned area.
```
