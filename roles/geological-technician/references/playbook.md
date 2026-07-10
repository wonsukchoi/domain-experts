# Playbook

Filled formats and thresholds. Defaults, not laws — deviate consciously and log why.

## 1. Core logging and RQD

### Run-by-run log entry (fields, filled example)

| Field | Entry |
|---|---|
| Hole ID | DDH-14 |
| Run # / interval | Run 9 / 82.00–88.00 m |
| Drilled run length | 6.00 m (600 cm) |
| Core recovered | 5.82 m (582 cm) |
| Recovery % | 582 / 600 = 97.0% |
| Sound pieces ≥10 cm (raw) | 312 cm |
| Mechanical breaks rejoined | 2 clusters, +47 cm (26 cm @ ~84.1 m, 21 cm @ ~86.4 m) |
| Sound pieces ≥10 cm (corrected) | 359 cm |
| RQD | 359 / 600 = 59.8% → 60% (fair) |
| Photo IDs | DDH14_R9_wet, DDH14_R9_dry, DDH14_R9_breaks_annotated |
| Flags | Rubble zone 85.6–86.3 m; recommend orientation follow-up if coincides with target contact |

### RQD classification bands (Deere, 1964)

| RQD | Rock quality |
|---|---|
| 90–100% | Excellent |
| 75–90% | Good |
| 50–75% | Fair |
| 25–50% | Poor |
| 0–25% | Very poor |

### Natural vs mechanical break — the call, in order

1. Surface texture: fresh, sharp, angular = mechanical; weathered, oxidized, slickensided, or mineral-coated = natural.
2. Orientation: roughly perpendicular to the core axis and matching the drill's rotation/torque pattern = mechanical; irregular or matching a known structural fabric = natural.
3. Fit: pieces fit back together cleanly with no material loss = supports mechanical; a gap, gouge, or infill material at the break = natural.
4. When still ambiguous after 1–3, log it as natural (the conservative call — understating rock quality is a cost/schedule problem; overstating it is a safety problem) and flag for geologist review, don't silently pick one.

### Recovery-loss log gap (filled example)

"Run 12, 94.00–97.00 m: recovered 2.10 m of 3.00 m (70%). Missing interval not assumed to match adjacent lithology — probable cause: heaving sand noted by driller at 95.4 m, consistent with a fault gouge zone inferred from Run 11's slickensided contact at 93.8 m. RQD not computed for this run (recovery below the ~90% threshold where RQD is considered representative); flagging for possible re-drill or wireline deviation."

## 2. QAQC sample-insertion scheme (exploration drilling default)

| Insert type | Frequency | Placement rule |
|---|---|---|
| Certified reference material (CRM/standard) | 1 per ~20 samples (5%) | Rotate through 3–4 CRMs spanning low/mid/high grade; never the same one twice in a row |
| Blank | 1 per ~20 samples (5%), plus always immediately after any interval expected to assay high | Coarse blank (barren material) submitted through the same prep stream as real samples |
| Field duplicate | 1 per 20–25 samples | Split from the same interval (quarter-core or 1/4-split of RC chips), submitted as a separate, sequentially-numbered sample |
| Lab/pulp duplicate | Per lab's own internal QAQC — technician confirms it's requested on the submittal sheet, doesn't run it | N/A — lab-side check |

**Acceptance thresholds, checked on return:**

- CRM result within ±2 standard deviations of the certified mean → pass. Outside ±2 SD once → recheck, note it. Outside ±3 SD, or 2 consecutive CRMs outside ±2 SD → batch flagged, hold reporting, notify geologist of record before any results go into a model.
- Blank result above 5–10× the lab's detection limit → contamination flag; trace back through the prep sequence (which samples were processed immediately before/after) before accepting the surrounding batch.
- Field duplicate pair relative percent difference (RPD) — `RPD = |A − B| / ((A + B)/2) × 100` — under ~20% is typical for a competent, well-mixed sample at grades well above detection limit; RPD routinely above 30% signals a nugget-effect or sampling-heterogeneity problem the geologist needs to know about before trusting single-sample grades.

**Submittal sheet discipline:** insert IDs are tracked on the technician's own control sheet, never on the sample tag or the lab-facing submittal list — the lab must receive the batch as an unbroken sequence of unknowns.

## 3. Soil/rock field classification (ASTM D2488 visual-manual)

Minimum fields to record before assigning a USCS group symbol: gradation estimate (coarse vs fine fraction by dry mass, visually), plasticity (dry strength, dilatancy, toughness field tests), color (Munsell), moisture condition, and any HCl reaction (carbonate content indicator). A field call of "SM" (silty sand) without at least the gradation and plasticity checks recorded is not a defensible classification — it's a guess with a symbol attached.

## 4. Sieve analysis reconciliation (ASTM D6913)

Filled example — original dry sample mass 500.0 g:

| Sieve | Retained mass (g) | % Retained | Cumulative % passing |
|---|---|---|---|
| No. 4 (4.75 mm) | 12.5 | 2.5% | 97.5% |
| No. 10 (2.00 mm) | 48.0 | 9.6% | 87.9% |
| No. 40 (0.425 mm) | 165.5 | 33.1% | 54.8% |
| No. 200 (0.075 mm) | 210.0 | 42.0% | 12.8% |
| Pan (fines) | 63.5 | 12.7% | — |
| **Sum retained + pan** | **499.5** | **99.9%** | — |

Sum should reconcile to the starting dry mass within ±0.3%; here 499.5 g against 500.0 g starting mass is a 0.1% loss (within tolerance — normal handling loss). A discrepancy beyond ~0.3–0.5% means a transcription error or spilled material and the run gets redone, not adjusted to force a fit.

## 5. Downhole survey schedule

Default: a deviation survey (azimuth/dip) at the start of the hole, then every 30 m, and again at end-of-hole — tighter (every 15–20 m) on holes planned steeper than 60° from horizontal or through known structurally complex ground, since azimuth drift compounds fastest where torque is highest. A survey skipped because the rig kept running is not recoverable after the hole is capped — stopping costs minutes; a missing survey can invalidate the down-hole-to-true-depth conversion for the whole hole below that point.
