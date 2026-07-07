# Weighers, Measurers, Checkers, and Samplers — Playbook

## Scale-ticket reconciliation sequence

| Step | Action | Pass condition | If failed |
|---|---|---|---|
| 1. Calibration check | Confirm scale's seal/calibration date is current | Seal unexpired, last calibration within site interval | Use alternate certified scale; flag reading as provisional |
| 2. Gross weigh | Weigh loaded vehicle, log ticket # and timestamp | Reading stable (no wind/vibration flag on indicator) | Re-weigh after settling; note if repeat readings differ >0.1% |
| 3. Tare determination | Check age of last tare ticket for this specific vehicle | Tare ≤ site re-tare interval (e.g. 7 days) and no visible change | Re-weigh empty after unload; log new tare ticket |
| 4. Net calculation | Net = Gross − Tare | — | — |
| 5. Tolerance check | Compare Net to BOL/PO claimed quantity | Variance within tolerance (e.g. ±0.5%) | Re-weigh gross once; if still outside tolerance, escalate |
| 6. Disposition | Accept and release, or escalate to discrepancy report | — | — |

## AQL sampling-plan application (ANSI/ASQ Z1.4 style)

| Lot size | Inspection level II, Normal | Sample size | AQL 1.0% Ac/Re |
|---|---|---|---|
| 91–150 | Code E | 20 | 1 / 2 |
| 151–280 | Code F | 32 | 2 / 3 |
| 281–500 | Code G | 50 | 3 / 4 |
| 501–1,200 | Code H | 80 | 5 / 6 |
| 1,201–3,200 | Code J | 125 | 7 / 8 |

Ac = accept if defects found ≤ this number. Re = reject if defects found ≥ this number. Example: lot of 400 units, Normal inspection, AQL 1.0% → sample 50 units; 3 or fewer defects accepts the lot, 4 or more rejects it. There is no partial-credit zone — a count of exactly 3 accepts, exactly 4 rejects.

**Switching rules** (apply after each lot's result, not just once):
- Two consecutive lots rejected under Normal inspection → switch to Tightened (smaller Ac/Re numbers at the same sample size, or a larger sample) until five consecutive lots are accepted.
- Ten consecutive lots accepted under Normal inspection (and no other disqualifying condition) → eligible to switch to Reduced inspection (smaller sample, tighter reject margin).
- A single lot rejected under Reduced inspection → return to Normal immediately.

## Filled example: net-weight reconciliation (grain elevator)

```
Ticket:            WE-48213
Commodity:          Soybeans, bulk
BOL claimed net:    48,000 lbs
Scale:              Platform Scale #2 — cal. seal current through 2026-11-01

Gross (loaded):     76,340 lbs   [confirmed on re-weigh, delta 0.0%]
Tare (prior ticket): 28,200 lbs  [14 days old — REJECTED, exceeds 7-day re-tare interval;
                                   vehicle modified (toolbox added) since last tare]
Tare (re-weighed):   28,850 lbs  [current, empty, post-unload]

Net weight:          76,340 - 28,850 = 47,490 lbs
Variance vs. BOL:    47,490 - 48,000 = -510 lbs  (-1.06%)
Tolerance:           ±0.5% (±240 lbs)
Result:              OUTSIDE TOLERANCE — escalate to weight-discrepancy report
```

## Filled example: AQL disposition (incoming component lot)

```
Lot:                 PO-88214, 620 units, injection-molded housings
Inspection level:    II, Normal (no switching-rule trigger active)
Sample size (Code H): 80 units
AQL 1.0% Ac/Re:      5 / 6

Sample result:        4 defective units found (crack, flash, short-shot mix)

Disposition:          4 <= Ac(5) -> ACCEPT lot
                       Log defect types for trend tracking even though lot accepted —
                       this vendor's last two lots also showed flash defects.
                       Trend flag raised for quality: 3 consecutive lots with flash
                       defects, though each individually accepted, warrants a
                       vendor-corrective-action request.
```

## Weight-discrepancy report template

```
WEIGHT DISCREPANCY REPORT — Ticket #[ticket]
Commodity: [commodity]. BOL claimed net: [X] lbs.
Gross (scale, calibration seal current through [date]): [Y] lbs, confirmed on re-weigh: [yes/no].
Tare: [prior ticket age / re-weighed], [Z] lbs.
Calculated net: [Y-Z] lbs. Variance from BOL: [delta] lbs ([pct]%), [within/exceeds] [tolerance]% tolerance.
Disposition: [accepted at measured weight / rejected / partial] — [claim filed / referred to shipper].
```
