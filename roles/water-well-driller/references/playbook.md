# Water Well Driller Playbook

Filled calculations and sequences for the four recurring driller decisions: drilling method selection, annular seal / gravel pack volumes, well development, and pump-test interpretation. Numbers below are worked examples with plausible field values — substitute the well's actual borehole diameter, casing size, and test readings.

## Drilling method selection by formation

| Formation | Method | Why | Typical penetration rate |
|---|---|---|---|
| Unconsolidated sand/gravel, running sand | Mud rotary | Weighted mud column hydrostatically holds the hole open; air alone collapses it | 20-40 ft/hr |
| Competent rock (granite, limestone, sandstone) | Air rotary (DTH hammer) | No fluid to mud off a producing fracture zone; drills 2-3x faster than mud rotary in hard rock | 40-100+ ft/hr |
| Boulders, cobbles, lost-circulation zones where rotary repeatedly fails | Cable tool (percussion) | Slow but unaffected by circulation loss; can drill through material that stalls a rotary bit | 5-15 ft/hr |
| Shallow monitoring wells, small diameter, no water production required | Air or dual-rotary | Fluid contamination of samples is a bigger concern than hole stability at shallow depth | 20-50 ft/hr |

Default: pick the method for the *next* formation interval, not the one already drilled — a well that starts in clay and moves into running sand at 80 ft needs mud circulation staged before the bit crosses that contact, not after the hole starts sloughing.

## Annular seal and gravel pack volume (gallons per foot of annulus)

```
gal/ft = 0.0408 × (D_hole² − D_casing_OD²)     [diameters in inches]
```

| Borehole (in) | Casing OD (in) | gal/ft annulus |
|---|---|---|
| 8 | 4.5 (4-in nominal steel) | 0.0408 × (64 − 20.25) = 1.79 |
| 10 | 6.625 (6-in nominal steel) | 0.0408 × (100 − 43.89) = 2.29 |
| 12 | 6.625 | 0.0408 × (144 − 43.89) = 4.08 |
| 12 | 8.625 (8-in nominal steel) | 0.0408 × (144 − 74.39) = 2.84 |

**Neat cement grout:** 94-lb sack + 6 gal water yields **8.82 gal of slurry per sack**. Sacks needed = (seal interval ft × gal/ft annulus) ÷ 8.82, rounded up, plus 10% contingency for hole washout/enlargement.

Example: 10-in hole, 6.625-in OD casing, 65-ft seal → 65 × 2.29 = 148.9 gal ÷ 8.82 = 16.9 → 17 sacks minimum, order 19.

**Seal depth default:** the greater of (a) the state code minimum, and (b) the depth of the first confining layer actually logged in cuttings. Never use (a) alone when (b) is deeper — check the log before ordering cement, not after.

**Gravel pack volume:** same gal/ft formula over the packed interval (typically 5-10 ft above the screen top, for bridging, down to the sump bottom), converted to cu ft (÷7.48) and then to tons using the pack material's bulk density (commonly ~100 lb/cu ft for clean silica gravel pack, i.e., roughly 20 cu ft per ton).

## Gravel pack and screen slot sizing from sieve data

1. Run a sieve analysis on a representative sample of the water-bearing interval; plot percent passing vs. grain size; read D50 (and D10, D60 for uniformity coefficient Cu = D60/D10).
2. Target pack D50 = formation D50 × 4 to 6. Use the lower end of the ratio (4x) for fine, uniform formations; the higher end (6x) for coarser or less uniform formations.
3. Select the closest commercial mesh pack whose D50 falls in that range (e.g., formation D50 0.55 mm → target range 2.2-3.3 mm → an 8x12 mesh pack at D50 ≈ 2.4 mm fits).
4. Size screen slot to retain roughly 85-90% of the selected pack — i.e., slot opening approximates the pack's D10-D15, not its D50. A slot cut to the pack's D50 passes half the pack material into the well.
5. Naturally developed exception: if the formation itself is coarse and well-graded (low Cu, roughly Cu < 3), an artificial pack may not be needed — size the screen slot directly to the formation's own D10-D15 instead and develop aggressively to remove fines from the formation immediately around the screen.

## Well development sequence

1. **Surge.** Run a surge block through the screen interval, working from the top of the screen down, to break down mud cake (if mud rotary was used) and pull fines through the screen into the sump.
2. **Airlift or bail.** Remove the fines/sediment pulled in by surging before they resettle; alternate surge-and-remove cycles rather than surging continuously, or displaced fines just recirculate past the screen.
3. **Repeat until discharge runs sand-free** to the naked eye over a sustained pumping period (commonly 30-60 minutes of clear discharge at a development rate at or above the anticipated production rate) — a few minutes of clear water is not the same test as a sustained one.
4. **Overpump** briefly at a rate above the planned production rate to confirm the well holds up under a rate higher than it will normally see, before moving to formal testing.

## Step-drawdown then constant-rate pump test

1. **Step-drawdown test.** Pump at 3-4 increasing rates (e.g., 40%, 60%, 80%, 100% of the anticipated design rate), each held roughly 1 hour with drawdown logged, without stopping the pump between steps. Compute specific capacity at each step (rate ÷ drawdown); if specific capacity falls sharply at higher steps, well loss (construction) is dominating over aquifer loss.
2. **Recovery check.** Stop the pump after the step test and log recovery to at least 90% of the pre-test static level before starting the constant-rate test — starting on an unrecovered aquifer understates the well's real capacity.
3. **Constant-rate test.** Pump at a single rate (commonly at or slightly below the highest sustainable step) for 4-8 hours (domestic) or 24-72 hours (public supply / high-capacity), logging drawdown at increasing intervals (every minute early, every 30-60 minutes once the rate of change slows).
4. **Confirm stabilization** — drawdown must be flat (commonly <0.1-0.2 ft change) over the final 1-2 hours before calling the test complete; a curve still declining at test's end means the test wasn't run long enough to size a pump against.
5. **Specific capacity = pumping rate ÷ stabilized drawdown.** Recommend a continuous pumping rate at roughly 75% of the tested rate, leaving margin below the point where well loss was climbing steeply in the step test.
