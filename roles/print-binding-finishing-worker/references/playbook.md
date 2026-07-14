# Playbook

## Creep-compensation worksheet (saddle-stitch)

Fill per job before imposition is finalized.

| Field | Value |
|---|---|
| Total page count | 32 |
| Pages per signature | 4 |
| Number of nested sheets | 8 |
| Stock caliper (per sheet) | 0.004" |
| Total nested stack thickness | 8 × 0.004" = 0.032" |
| Estimated total creep (stack × π/2) | 0.032" × 1.57 ≈ 0.050" |
| Target trim-edge margin | 0.375" |
| Per-sheet progressive shift (approx.) | ~0.006"-0.007" per sheet position |
| Sample pull-test required before full run? | Y (always, for any new job/stock/page-count combo) |
| Sample measured margins (innermost/outermost) | record actual |
| Within ±0.010" of target? | Y/N — if N, revise compensation and re-test |

## Collating sampling-plan table

| Run quantity | Minimum spot-check interval |
|---|---|
| Under 500 | 1-in-25 |
| 500-5,000 | 1-in-50 |
| 5,000-25,000 | 1-in-100, plus a check after any feeder fault/jam event |
| Over 25,000 | 1-in-100, plus a check every hour and after any fault event |

Always add an additional spot-check immediately following any collator fault, jam, or hopper-refill event, regardless of the run's baseline interval — faults are where sequence errors actually enter the run.

## Glue-stock compatibility reference (perfect binding)

| Stock coating | Glue formulation consideration | Verification step |
|---|---|---|
| Uncoated text/cover | Standard hot-melt or PUR adhesive typically adequate | Confirm via standard pull-test on first bound sample |
| Coated (gloss/matte) | Requires a coated-stock-rated formulation or roughened/notched spine prep for adhesion | Sample binding required before full run; verify pull strength meets spec |
| Heavy coated / laminated cover | Highest risk for pull-out; may require PUR adhesive and spine roughening | Sample binding mandatory; consider extended pull-test (e.g., after a heat/cold cycle) before approving full run |

## Grain-direction fold test (quick field check)

1. Cut a small sample strip in each direction (with and against suspected grain) from the actual stock lot.
2. Fold each strip and observe: the fold made *with* the grain stays smooth; the fold made *against* the grain shows visible fiber cracking or a rougher fold line, especially on coated stock.
3. Confirm the imposition's planned fold direction matches the grain direction that folds smoothly.
4. If the job requires folding against the grain for layout reasons, score before folding and flag the job for a sample check before running the full quantity.
