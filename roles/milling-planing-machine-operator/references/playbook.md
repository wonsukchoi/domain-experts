# Playbook

## Multi-pass depth strategy worksheet

Fill for any deep pocket/slot operation.

| Field | Value |
|---|---|
| Feature | Slot, 0.250" wide x 1.500" deep |
| Cutter | 0.250" dia. end mill |
| Length-to-diameter at full stickout | ~6:1 or higher |
| Single-pass risk assessment | High deflection/breakage risk — NOT used |
| Roughing pass 1 | 0.500" depth |
| Roughing pass 2 | 0.500" depth (cumulative 1.000") |
| Roughing pass 3 | 0.500" depth (cumulative 1.500") |
| Finishing pass | 0.010"-0.020" stepover, full depth, reduced feed |
| Measured result (top/mid/bottom) | 0.250"/0.249"/0.249" — within ±0.002" straightness spec |

**Rule:** for any feature with a cutter length-to-diameter ratio of roughly 4:1 or higher at full depth, default to a multi-pass strategy rather than a single deep pass.

## Cutter deflection/length-to-diameter reference table (illustrative — always use the specific cutter manufacturer's guidance)

| Length-to-diameter ratio | Deflection risk | Recommended approach |
|---|---|---|
| Up to 3:1 | Low | Standard single-pass parameters generally acceptable |
| 3:1-5:1 | Moderate | Consider reduced feed/depth per pass |
| 5:1-8:1 | High | Multi-pass strategy recommended, reduced feed on deeper passes |
| Over 8:1 | Very high | Multi-pass required; consider specialized long-reach cutter design or alternative process |

**Rule:** always verify against the specific cutter's actual rigidity data — this table is illustrative of the general risk trend, not a substitute for manufacturer-specific deflection data.

## Climb-vs-conventional selection guide

1. Determine this specific machine's backlash characteristics (check machine specification or perform a backlash test).
2. If backlash is minimal/well-controlled, climb milling is generally usable and often produces better finish/tool life.
3. If backlash is significant, default to conventional milling to avoid dig-in risk, or address backlash (machine maintenance) before using climb milling.
4. For a new or unfamiliar machine, verify backlash before assuming climb milling is safe — don't default to climb milling based on general preference without machine-specific verification.
5. Document the milling direction selected and the backlash consideration that informed the choice.
