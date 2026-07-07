# Fashion Designer — Artifacts

## Costing sheet (filled example)

| Line item | Basis | Qty | Unit cost | Extended |
|---|---|---|---|---|
| Fabric (54" cotton poplin, bulk 800u quote) | 1.36 yd/unit | 1.36 | $6.20/yd | $8.43 |
| Trim (buttons ×7, interfacing, thread, woven label) | per unit | 1 | $1.35 | $1.35 |
| Labor (contract factory, CMT bulk quote) | per unit | 1 | $4.10 | $4.10 |
| Freight/duty allocation | per unit | 1 | $0.85 | $0.85 |
| **Total COGS** | | | | **$14.73** |
| Target ceiling (from $42 wholesale ÷ 2.5x) | | | | $16.80 |
| **Margin to ceiling** | | | | **$2.07 (12.3%)** |

Note: cost sample-quantity fabric quotes separately and label them — a sample-run quote at $8.40/yard vs. this bulk quote of $6.20/yard is a 35% difference that must not leak into the costing sheet used for the wholesale-price decision.

## Tech pack spec table (excerpt, with tolerances)

| Measurement point | Size M spec | Tolerance | Grade increment (per size step) |
|---|---|---|---|
| Chest, 1" below armhole | 40.0" | ±0.375" | +1.5" |
| Waist | 38.0" | ±0.375" | +1.5" |
| Center back length | 27.5" | ±0.25" | +0.5" |
| Sleeve length | 24.25" | ±0.25" | +0.625" |
| Bicep | 14.5" | ±0.25" | +0.5" |

A sample measuring 40.3" chest against a 40.0" spec with ±0.375" tolerance is a **pass** (within band) — do not reject on that point alone.

## Grade rule table — full size run sanity check (chest measurement)

| Size | XS | S | M (base) | L | XL | XXL |
|---|---|---|---|---|---|---|
| Chest | 37.0" | 38.5" | 40.0" | 41.5" | 43.0" | 44.5" |
| Increment from prior | — | +1.5" | +1.5" | +1.5" | +1.5" | +1.5" |

Check the extremes (XS and XXL), not just the base and its neighbor — a grade rule that's correct at M/L but was mis-entered as +1.25" instead of +1.5" at one step will only show a discrepancy when the full run is tabulated end to end (37.0" + 5×1.25" = 43.25" instead of the intended 44.5" at XXL, a 1.25" miss that compounds silently size by size).

## Line-sheet margin check (portfolio view, excerpt)

| Style | Wholesale | COGS | Markup | Projected sell-through | Keep/cut decision |
|---|---|---|---|---|---|
| WS-114 Popover Shirt | $42 | $14.73 | 2.85x | 78% (strong prior-season analog) | Keep |
| WS-119 Wrap Dress | $68 | $28.10 | 2.42x | 41% (below 55% line threshold) | Cut — below sell-through floor despite acceptable margin |
| WS-122 Cropped Jacket | $95 | $34.20 | 2.78x | 61% | Keep |

A style can clear its margin target and still be cut — margin alone doesn't justify a line slot if projected sell-through is below the season's floor.
