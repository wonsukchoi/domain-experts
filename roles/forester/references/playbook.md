# Forester — Playbook

## Cruise-design worksheet (variable-radius point sampling)

| Input | Value | Notes |
|---|---|---|
| Stand area | 80 ac | From GIS/deed acreage, not visual estimate |
| BAF (prism factor) | 10 | Chosen so in-count runs 5-10 trees/point on this density |
| Sampling intensity | 1 point / 4 ac | 20 points, systematic grid |
| Mean in-count | 12 trees/point | → basal area = 12 × 10 = 120 sq ft/ac |
| Per-point SD | 4.2 trees | CV = 4.2 / 12 = 35% |
| Volume conversion | 52 bf (Doyle) / sq ft BA | From local volume table for this dbh/height class |
| Volume/ac | 6,240 bf | 120 × 52 |
| Total stand volume | 499,200 bf | 6,240 × 80 |
| SE of mean | 7.83% | CV ÷ √n = 35% ÷ √20 |
| 95% CI half-width | 15.4% | 1.96 × SE |
| **95% CI on total volume** | **422,300 – 576,100 bf** | 499,200 ± 15.4% |

**To tighten CI to ±10%:** required n = (CV ÷ target SE)² = (35 ÷ 5.10)² ≈ 47 points. Added field time: 27 extra points × ~15 min/point ≈ 6.75 hours.

## Land Expectation Value (LEV) / rotation-age comparison

Faustmann formula: LEV = [ (Harvest value at age R) × (1+i)^(-R) × (1+i)^R / ((1+i)^R − 1) ] − establishment cost annuity. Simplified single-rotation form used for a quick candidate-age comparison:

| Candidate age | Projected volume (MBF/ac) | Stumpage $/MBF | Harvest value/ac | Discount factor @ 6% | PV of harvest/ac | LEV/ac (perpetual series) |
|---|---|---|---|---|---|---|
| 25 | 5.8 | 305 | $1,769 | (1.06)^-25 = 0.2330 | $412 | $498 |
| 28 (current age) | 6.24 | 310 | $1,934 | (1.06)^-28 = 0.1956 | $378 | $416 |
| 32 | 6.9 | 315 | $2,174 | (1.06)^-32 = 0.1552 | $337 | $340 |

LEV/ac (perpetual) = PV of harvest/ac × (1+i)^R ÷ [(1+i)^R − 1]. Reading the table: LEV peaks at age 25 in this example — the stand's financial rotation age is earlier than its current age of 28, meaning waiting further destroys value even though volume keeps growing. Biological rotation (MAI-culmination) for this species/site is typically in the 30-35 year range — a materially later age than the financial optimum, illustrating core-truth #2.

## Silvicultural-system selection matrix

| Regeneration species shade tolerance | Recommended system | Overstory retention | Typical species examples |
|---|---|---|---|
| Intolerant | Clearcut (or seed-tree) | None to minimal (seed trees only, removed after regen established) | Loblolly/longleaf pine, Douglas-fir, aspen |
| Mid-tolerant | Shelterwood | Partial (30-50% canopy retained until regen established, then removed) | Yellow-poplar, white oak, red pine |
| Tolerant | Single-tree or group selection | High (uneven-aged structure maintained indefinitely) | Sugar maple, true firs, eastern hemlock |

**Override:** salvage or sanitation removal (storm damage, insect/disease outbreak) follows the damage footprint, not this matrix — state the override explicitly in the prescription rather than silently picking a system that looks mismatched to species.

## Stocking / thinning trigger

| Basal area vs. stocking guide | Action |
|---|---|
| Below lower stocking line | Understocked — no thinning; consider interplanting if persistent |
| Between lower and upper line ("B-line to A-line") | Fully stocked — hold, monitor |
| Above upper stocking line | Overstocked — schedule thinning within current growing season unless final harvest is within 2-3 years |
