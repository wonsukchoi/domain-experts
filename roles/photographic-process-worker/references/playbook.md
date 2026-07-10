# Playbook

## Time-temperature compensation calculation (filled example)

C-41 process, standard time 195 sec at standard temperature 100.4°F. Actual tank temperature: 96.8°F.

| Step | Value |
|---|---|
| Standard time | 195 sec (3:15) |
| Standard temperature | 100.4°F |
| Actual temperature | 96.8°F |
| Temperature deviation | 100.4 − 96.8 = 3.6°F below standard |
| Compensation rate (illustrative, per process class) | ~5% additional time per °F below standard |
| Total compensation | 3.6 × 5% = 18% |
| Compensated time | 195 × 1.18 = 230.1 sec ≈ 3:50 |
| Shortfall if standard time used instead | 230.1 − 195 = 35.1 sec (≈15.3% of required time) |

**Comparison across temperature deviations (same process):**

| Deviation below standard | Compensation | Compensated time |
|---|---|---|
| 1.0°F | 5% | 195 × 1.05 = 204.75 sec (3:25) |
| 2.0°F | 10% | 195 × 1.10 = 214.5 sec (3:35) |
| 3.6°F | 18% | 195 × 1.18 = 230.1 sec (3:50) |
| 5.0°F | 25% | 195 × 1.25 = 243.75 sec (4:04) |

## Control-strip monitoring log (filled example)

| Time in run | Densitometer reading (density units) | Control limit | Status |
|---|---|---|---|
| Start of shift | 1.02 | 0.95–1.05 | Within limits |
| After 200 rolls | 1.04 | 0.95–1.05 | Within limits, trending up |
| After 400 rolls | 1.09 | 0.95–1.05 | **Out of limits — correct chemistry before continuing** |

**Action at 400-roll checkpoint:** Replenish chemistry per the standard replenishment schedule for this throughput before running additional production, rather than continuing on the assumption the drift will self-correct.

## Fixer exhaustion verification (filled example)

Fixer rated capacity: 500 rolls of 35mm film equivalent. Current volume processed: 420 rolls (84% of rated capacity).

| Volume processed | % of rated capacity | Action |
|---|---|---|
| Under 300 rolls (60%) | Under 60% | Standard fixing time, no additional check needed |
| 300–450 rolls (60–90%) | 60–90% | Run fixer-check test before continuing; extend fixing time if indicated |
| Over 450 rolls (90%+) | 90%+ | Replace fixer before continuing production |

At 420 rolls (84%), a fixer-check test is required before continuing — not yet at replacement threshold, but past the point where fresh-chemistry fixing time can be assumed adequate without verification.
