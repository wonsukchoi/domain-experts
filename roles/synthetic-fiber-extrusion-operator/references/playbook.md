# Playbook

## Denier / take-up speed calculation (filled example)

Prior product: throughput 45 g/min, target denier 150. New product: throughput 50 g/min, same target denier 150.

| Step | Value |
|---|---|
| Formula | Denier = (throughput g/min × 9,000) ÷ take-up speed (m/min) |
| Prior product take-up speed | (45 × 9,000) ÷ 150 = 2,700 m/min |
| New product correct take-up speed | (50 × 9,000) ÷ 150 = 3,000 m/min |
| Result if prior 2,700 m/min reused | (50 × 9,000) ÷ 2,700 = 166.7 denier |
| Overshoot from 150 target | 166.7 − 150 = 16.7 (11.1%) |

**Comparison across throughput rates (same 150 denier target, same reused 2,700 m/min take-up speed):**

| Throughput rate | Denier if take-up speed left at 2,700 m/min | Deviation from 150 target |
|---|---|---|
| 45 g/min (original) | (45×9,000)/2,700 = 150.0 | 0% (correct — matches original calibration) |
| 50 g/min | (50×9,000)/2,700 = 166.7 | +11.1% |
| 55 g/min | (55×9,000)/2,700 = 183.3 | +22.2% |

**Rule applied:** Every increase in throughput without a corresponding take-up speed increase produces a proportional denier overshoot — the deviation scales directly with how much throughput changed relative to the speed setting's original calibration.

## Draw ratio range reference (filled example)

| Polymer type | Typical draw ratio range | Consequence outside range |
|---|---|---|
| Polyester (PET) | 3.5:1 – 5.0:1 | Below range: low tenacity, high elongation. Above range: filament breakage risk |
| Nylon 6,6 | 3.0:1 – 4.5:1 | Similar under/over-draw consequences, different absolute range |
| Polypropylene | 4.0:1 – 6.0:1 | Higher achievable range, but still has an upper breakage limit specific to this polymer |

**Applied check:** A draw ratio of 5.5:1 might be well within range for polypropylene but would be significantly over-range and breakage-prone for polyester — draw ratio limits are polymer-specific, and a setting validated for one material cannot be assumed safe for another without checking its own documented range.
