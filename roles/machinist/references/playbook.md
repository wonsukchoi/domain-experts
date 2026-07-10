# Playbook

## True-position / MMC bonus-tolerance calculation (filled example)

Part XYZ-114, two ⌀0.250"+0.002/-0.000 holes, true position ⌀0.010" at MMC, datums A (face), B (pin).

| Step | Value |
|---|---|
| MMC size (minimum allowed hole diameter) | ⌀0.250" |
| Measured actual hole diameter | ⌀0.253" |
| Bonus tolerance (actual − MMC) | 0.253 − 0.250 = 0.003" |
| Base positional tolerance (printed) | ⌀0.010" |
| Total allowable positional tolerance | 0.010 + 0.003 = ⌀0.013" |
| Measured deviation, X axis | 0.004" |
| Measured deviation, Y axis | 0.003" |
| Radial deviation | √(0.004² + 0.003²) = √0.000025 = 0.005" |
| Positional deviation as diameter equivalent | 2 × 0.005 = ⌀0.010" |
| Margin vs. total allowable | 0.013 − 0.010 = 0.003" (23.1% of the allowance) |

**Result:** Accept — 0.010" measured deviation is within the 0.013" total allowable position tolerance once the 0.003" bonus tolerance from the oversize hole is applied.

## Tolerance stack-up worksheet (filled example)

Assembly: a shaft (Part A) must pass through and seat against a housing bore (Part B), with a required minimum running clearance of 0.003" and maximum clearance of 0.015" to avoid excess play.

| Dimension | Nominal | Tolerance | Contributes to stack |
|---|---|---|---|
| Part A shaft diameter | 0.7480" | ±0.0005" | Max shaft: 0.7485", Min shaft: 0.7475" |
| Part B bore diameter | 0.7510" | ±0.0005" | Max bore: 0.7515", Min bore: 0.7505" |
| Worst-case minimum clearance | — | — | Min bore − Max shaft = 0.7505 − 0.7485 = 0.0020" |
| Worst-case maximum clearance | — | — | Max bore − Min shaft = 0.7515 − 0.7475 = 0.0040" |

**Result:** Worst-case minimum clearance (0.0020") falls below the required minimum (0.003") — this stack-up fails at the tolerance extremes even though both parts individually machine within print. Either tighten one part's tolerance band or widen the nominal gap before releasing both prints to production.

## Speeds and feeds tuning log (filled example)

4140 steel, 0.500" 4-flute carbide end mill, roughing pass.

| Parameter | Catalog starting value | Actual running value | Reason for adjustment |
|---|---|---|---|
| Cutting speed (SFM) | 350 | 300 | Chip color trending toward straw/blue at 350 — backed off to hold silver/gold chip |
| Feed rate (IPM) | 42 | 42 | No change — feed unrelated to observed heat signal |
| Depth of cut (roughing) | 0.150" | 0.150" | No change |
| Depth of cut (finishing pass, same tool) | — | 0.020" | Reduced from roughing depth per finishing-pass default |
