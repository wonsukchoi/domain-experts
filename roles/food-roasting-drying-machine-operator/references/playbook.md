# Playbook

## Declining-rate process time comparison (filled example)

Initial moisture 20%, target 5%. Early-stage data: 20% → 15% in 10 minutes.

| Step | Value |
|---|---|
| Early-stage loss | 20% − 15% = 5 percentage points |
| Early-stage time | 10 minutes |
| Early-stage rate | 5 ÷ 10 = 0.5 points/min |
| Naive linear projection (constant rate assumed) | Total loss needed: 20% − 5% = 15 points; time = 15 ÷ 0.5 = 30 min |
| Validated actual process time (from moisture-loss curve testing) | 45 minutes |
| Shortfall if naive 30-minute time used | 45 − 30 = 15 minutes (33.3% short of required time) |

**Comparison across target moisture levels (same 20% start, same early-stage rate):**

| Target moisture | Naive linear projection | Validated actual time (illustrative, reflecting falling-rate curve) | Naive shortfall |
|---|---|---|---|
| 10% | (20−10)/0.5 = 20 min | ~25 min | 20% short |
| 5% | (20−5)/0.5 = 30 min | ~45 min | 33% short |
| 2% | (20−2)/0.5 = 36 min | ~65 min | 45% short |

**Rule applied:** The lower the final target moisture, the larger the gap between naive linear projection and actual required time — because reaching a lower target requires more time spent in the slow, falling-rate period, which a constant-rate extrapolation entirely misses.

## Batch-size scaling verification checklist (filled example)

| Check | Validated batch (50kg) | New batch (200kg) | Action |
|---|---|---|---|
| Time/temperature profile | Validated 45-min profile at 300°F | Same profile applied initially | Verify, don't assume |
| Loading density | 1 kg per tray-ft² | 1.5 kg per tray-ft² (denser load) | Flag — airflow penetration may differ |
| Internal moisture at process end | Verified 5% via moisture analyzer | Not yet verified at new scale | **Required before release** |
| Transition point timing | Observed at 28 min in validation | Not yet observed at new scale | Monitor and log actual timing |

**Result:** The new 200kg batch's higher loading density means the validated 45-minute profile cannot be assumed to produce the same 5% moisture result — direct moisture testing at this scale is required before releasing product, not just running the same time/temperature settings that worked at 50kg.
