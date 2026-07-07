# Playbook

Filled scale-rule computations, a defect-deduction worksheet, and grade thresholds — populate these rather than describing them.

## 1. Scale rule formulas and when each governs

| Rule | Formula (D = small-end diameter inside bark, in inches; L = length, in feet) | Where it's the governing rule |
|---|---|---|
| Doyle | bf = (D − 4)² × L ÷ 16 | Much of the South and parts of the Northeast/Appalachia; many private mill contracts |
| Scribner Decimal C | Diagram-derived, tabulated (not a closed formula); rounded to nearest 10 bf | USFS Pacific Northwest Region (Region 6) national forest sales; common PNW private-mill standard |
| International 1/4-inch | Tabulated per 4-ft section with a 1/4-inch assumed saw kerf and a taper allowance | USFS Northeastern and Lake States sales; considered the closest of the three rules to actual sawn lumber recovery |

**Doyle's structural bias:** because the formula subtracts a flat 4 inches before squaring, it assumes the same absolute slab loss on a 10-inch log as a 40-inch log. At D = 4 inches, Doyle scales the log at exactly 0 board feet regardless of length — a log that self-evidently contains merchantable wood. The bias direction: Doyle under-scales small-diameter logs (often 20–50% below Scribner/International under ~16 inches) and over-scales large-diameter logs relative to actual mill recovery, with the two rules converging near 26–30 inches diameter (Freese, 1973). Never use Doyle's output as a sanity check for Scribner or International readings on small logs, or vice versa — they are not supposed to agree away from the crossover range.

## 2. Doyle worked table (16-ft length, varying diameter)

| Scaling diameter (in) | Doyle bf = (D−4)²×16/16 | Note |
|---|---|---|
| 8 | 16 | Near minimum merchantable; Doyle already reading low relative to actual recovery |
| 10 | 36 | |
| 12 | 64 | |
| 14 | 100 | |
| 16 | 144 | See SKILL.md worked example |
| 20 | 256 | |
| 24 | 400 | Approaching the Doyle/Scribner crossover range |
| 28 | 576 | Near crossover — Doyle and Scribner typically within a few percent here |

## 3. Defect deduction worksheet

Apply in this order; each step operates on the output of the previous one.

**Step A — Sweep / crook (diameter-reduction method).**
1. Measure maximum displacement of the sweep or crook from a straight chord, in inches, over the affected length.
2. If displacement ≤ 1 inch per 8 feet of affected length: no deduction (within merchantable tolerance).
3. If displacement > 1 inch per 8 feet: reduce the scaling diameter by the full displacement (in inches) and recompute gross volume under the governing rule using the reduced diameter.
4. Record: displacement measured, affected length, diameter before/after, resulting bf deduction.

**Step B — Internal decay indicators (rot, conk, punk knots).**
1. If a conk or other external decay indicator is present: assume decay extends a minimum of 3 feet from the indicator along the log axis (conservative field default; extend further if probing confirms).
2. Estimate the percentage of cross-sectional area affected in that section (visual/probe estimate; use 20% as the default starting assumption for a single conk with no probe data, adjust up if probing confirms more).
3. Deduction (bf) = (affected length ÷ total length) × (% cross-section affected) × volume-after-Step-A.
4. Record: indicator observed, affected length assumed, % cross-section assumed, source of the estimate (visual vs. probed).

**Step C — Other cull (seams, forks, foreign material, fire scar).**
1. Estimate the volume of the log rendered unmerchantable by the defect directly (not as a percentage of the whole) where the defect is localized and clearly bounded (e.g., a fork above a stated height).
2. Deduct that volume directly from the Step B result.

**Net scale = gross volume − Step A deduction − Step B deduction − Step C deduction.**

## 4. Softwood grade thresholds (Pacific Northwest convention, generalized from USFS Region 6)

| Grade | Minimum scaling diameter | Defect allowance | Typical use |
|---|---|---|---|
| Peeler | 20 in+ (species-dependent) | Clear on 3+ faces over merchantable length; no sweep beyond tolerance; no visible decay indicators | Veneer |
| #1 Sawmill (Select) | 14–20 in | Minor sweep within tolerance; no visible decay | High-grade lumber |
| #2 Sawmill | 10–16 in | Sweep beyond tolerance and/or one localized decay indicator, deducted per worksheet above | Standard dimension lumber |
| #3 Sawmill / Utility | 8–10 in minimum merchantable | Multiple defects, deducted individually; below this diameter or beyond ~50% net cull, log is typically diverted to pulpwood or rejected | Low-grade lumber, pulp |

A log disqualifies from a grade the moment it fails any single threshold for that grade — a 22-inch log with sweep beyond tolerance does not average its way into Peeler on diameter alone; it drops to the grade its worst qualifying defect allows.

## 5. Board feet to MBF and stumpage arithmetic

A truckload scaling at 4,200 net board feet across all logs = 4.2 MBF. At a stumpage rate of $600/MBF for that grade mix: payable value = 4.2 × $600 = **$2,520** for that load. A scaler who is systematically 5% high or low on every load moves that number by roughly $126/load in one direction — the reason check-scaling tracks a scaler's average bias across many loads rather than auditing single tickets.
