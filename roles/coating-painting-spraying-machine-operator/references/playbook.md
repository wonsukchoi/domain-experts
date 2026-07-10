# Playbook

## WFT/DFT calculation (filled example)

Target DFT: 75 microns. Coating volume solids: 50%.

| Step | Value |
|---|---|
| Target DFT | 75 microns |
| Volume solids | 50% |
| Required WFT | 75 / 0.50 = 150 microns |
| Result if naive 75-micron WFT applied | 75 × 0.50 = 37.5 microns DFT — 50% shortfall |

**Comparison across volume solids percentages (same 75-micron DFT target):**

| Volume solids | Required WFT | DFT if naive 75-micron WFT applied instead | Shortfall |
|---|---|---|---|
| 70% | 75 / 0.70 = 107.1 microns | 75 × 0.70 = 52.5 microns | 30% short |
| 50% | 75 / 0.50 = 150.0 microns | 75 × 0.50 = 37.5 microns | 50% short |
| 30% | 75 / 0.30 = 250.0 microns | 75 × 0.30 = 22.5 microns | 70% short |

**Rule applied:** Lower volume solids coatings require proportionally more wet film to hit the same dry film target, and produce proportionally larger shortfalls if the WFT-equals-DFT naive assumption is used.

## Flash-off time reference by coat type (filled example)

| Coat type | Minimum flash time (typical ambient conditions) | Consequence if shortened |
|---|---|---|
| Primer to primer (multi-coat primer) | 10–15 minutes | Reduced intercoat adhesion, minor solvent entrapment risk |
| Primer to basecoat | 15–20 minutes | Solvent entrapment risk increases, potential for basecoat defects |
| Basecoat to clearcoat | 5–10 minutes (flash) | Solvent popping, clouding, or poor gloss if entered clear too soon |
| Final coat before bake/cure | Full specified flash time before oven entry | Blistering during cure from trapped solvent flashing rapidly under heat |

**Rule applied:** The final flash before bake/cure entry is typically the least forgiving step — entering the oven with inadequate flash time causes trapped solvent to flash rapidly under heat rather than gradually at ambient, producing blistering defects that are far more severe than a shortened intercoat flash alone would cause.

## Cure verification worksheet (filled example)

Cure schedule: 30 minutes at 350°F, actual part temperature (not oven setpoint) must reach and hold 350°F.

| Time | Oven setpoint | Actual part temperature | Cure clock running? |
|---|---|---|---|
| 0 min | 350°F | 210°F (heating up) | No |
| 10 min | 350°F | 340°F | No — still below 350°F |
| 13 min | 350°F | 350°F | Yes — cure clock starts |
| 43 min | 350°F | 350°F | Cure complete (30 min held from minute 13) |

**Naive error:** Tracking cure time from oven entry (time 0) or elapsed time alone would release this part at the 30-minute mark — 13 minutes before the part itself actually reached cure temperature — producing an under-cured part indistinguishable from a fully cured one on visual inspection.
