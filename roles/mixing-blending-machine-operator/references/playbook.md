# Playbook

## Premix concentration calculation (filled example)

Vitamin premix: 2.5 kg, total batch: 500 kg, target 0.5%.

| Step | Value |
|---|---|
| Premix weight | 2.5 kg |
| Target concentration in full batch | 0.5% (2.5 / 500) |
| Ratio of batch to premix if added directly | 500 / 2.5 = 200× — must disperse through 200x its own mass |
| Intermediate blend excipient weight | 25 kg |
| Intermediate mixture total | 2.5 + 25 = 27.5 kg |
| Intermediate concentration | 2.5 / 27.5 = 9.1% |
| Remaining batch after intermediate incorporation | 500 − 27.5 = 472.5 kg |

**Comparison — dispersion difficulty at different intermediate ratios:**

| Excipient added to premix | Intermediate total | Intermediate concentration | Dispersion difficulty |
|---|---|---|---|
| None (direct addition) | 2.5 kg (added to 500 kg batch) | 0.5% at full scale | Hardest — must disperse through full 500 kg in one step |
| 10 kg | 12.5 kg | 20.0% | Easier — verified at high concentration in small mass first |
| 25 kg (standard) | 27.5 kg | 9.1% | Standard validated approach |
| 50 kg | 52.5 kg | 4.8% | Lower intermediate concentration, less aggressive premix |

## Blend uniformity sampling worksheet (filled example)

500 kg batch, 10 samples pulled from distinct locations (varying depth and position within the blender), target ingredient at 0.5% nominal concentration.

| Sample location | Measured concentration | Deviation from 0.5% target |
|---|---|---|
| Top-front | 0.52% | +0.02 |
| Top-back | 0.48% | −0.02 |
| Middle-front | 0.51% | +0.01 |
| Middle-back | 0.49% | −0.01 |
| Middle-center | 0.50% | 0.00 |
| Bottom-front | 0.53% | +0.03 |
| Bottom-back | 0.47% | −0.03 |
| Bottom-center | 0.50% | 0.00 |
| Mid-depth-left | 0.51% | +0.01 |
| Mid-depth-right | 0.49% | −0.01 |

| Statistic | Value |
|---|---|
| Mean concentration | 0.500% |
| Standard deviation | ~0.019% |
| CV (SD / mean × 100) | ~3.8% |
| Specification limit | ≤ 5.0% CV |
| Result | Within spec |

**Note:** A single sample pulled only from the top-front location (0.52%) would have looked reasonable in isolation but would have said nothing about the actual batch-wide uniformity, which required all 10 locations to calculate.
