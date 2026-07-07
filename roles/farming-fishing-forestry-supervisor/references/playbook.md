# Playbook

Filled procedures for the three recurring judgment calls: setting/testing a piece rate, computing overtime on piece-rate pay, and making the weather push-vs-hold call. Numbers are worked examples — recompute against the current year's AEWR and minimum wage before use.

## 1. Piece-rate wage-floor test (run every pay period, per crew)

Sample actual output for 2–3 representative workers over the last 2–3 days, not the whole crew's payroll total — a payroll total can look fine on days a fast picker skews the average while several workers ran under floor.

| Step | Formula | Worked value |
|---|---|---|
| 1. Sample pace | lugs picked ÷ hours worked | 96 lugs ÷ 8 hrs = 12 lugs/hr |
| 2. Piece earnings | pace × hours × rate | 96 × $1.10 = $105.60 |
| 3. Effective hourly | earnings ÷ hours | $105.60 ÷ 8 = $13.20/hr |
| 4. Compare to floor | effective hourly vs. applicable minimum wage | $13.20 < $16.50 CA floor → **fails** |
| 5. Make-up pay owed (per worker per day) | (floor × hours) − earnings | ($16.50 × 8) − $105.60 = $26.40 |
| 6. New rate to clear floor at same pace | floor ÷ pace | $16.50 ÷ 12 = $1.375 → round up to **$1.40/lug** |

Rule: if step 4 fails for 2 consecutive days, pay make-up immediately for the days already worked and set the new rate before the next shift starts — don't wait for a full pay period to close before deciding.

## 2. Overtime on a piece rate (state ag-overtime threshold: 8 hrs/day, this employer size)

Piece-rate workers who work overtime are owed a premium on top of piece earnings, not a separate hourly recompute of the whole day.

| Step | Formula | Worked value (10-hr push day, $1.40/lug, 12 lugs/hr pace) |
|---|---|---|
| 1. Total piece earnings | pace × hours × rate | 120 lugs × $1.40 = $168.00 |
| 2. Regular rate | earnings ÷ total hours | $168.00 ÷ 10 = $16.80/hr |
| 3. OT hours | hours worked − 8 | 10 − 8 = 2 |
| 4. OT premium | regular rate × 0.5 × OT hours | $16.80 × 0.5 × 2 = $16.80 |
| 5. Total daily pay | piece earnings + OT premium | $168.00 + $16.80 = **$184.80** |

Check regular rate (step 2) against the applicable minimum wage before adding the OT premium — a regular rate already below floor means make-up pay is owed first, then OT premium is computed on the corrected rate, not the failing one.

## 3. Weather push-vs-hold decision

Set the threshold before the season starts; the call during a live forecast is a lookup, not a debate.

**Pre-set triggers (example, adjust per crop):**
- Rain probability ≥ 60% within 48 hours **and** crop within ~1 Brix point (or equivalent ripeness measure) of target → evaluate push.
- Frost risk ≥ 40% with unharvested tonnage on the vine/tree/plant → evaluate push.
- Below both thresholds → hold original schedule, recheck forecast next day.

**When triggered, run the tradeoff:**

| Input | Worked value |
|---|---|
| Unpicked acreage | 20 acres |
| Yield/acre | 8 tons |
| Price/ton | $1,400 |
| Exposed crop value | 20 × 8 × $1,400 = $224,000 |
| Historical loss rate from rain-on-ripe event | 25% |
| Value at risk | $224,000 × 0.25 = $56,000 |
| Incremental labor cost of push vs. compliant hold plan | $184.80/worker/day × 3 days × 50 workers − $16.50 × 8 × 3 × 50 = $27,720 − $19,800 = $7,920 |
| Decision | $7,920 cost << $56,000 at risk → **authorize push** |

If incremental labor cost exceeds value at risk, hold the original schedule and accept the exposure — pushing is not automatically correct just because a threshold fired.

**Before authorizing any push, clear these two gates for every surge block:**
1. **REI status** — pull the application log; if any target block is inside its label REI, redirect surge crew to a compliant block or delay entry, never override on schedule pressure.
2. **Sanitation relocation** — if the surge crew moves more than roughly a quarter mile from the current toilet/handwash/water station, relocate coverage before crew arrival, at the 1-unit-per-20-workers planning ratio (50 workers → 3 units).

## 4. Crew-source cost comparison (H-2A vs. day-haul vs. overtime on existing crew)

| Line item | H-2A | Day-haul (via FLC) | OT on existing crew |
|---|---|---|---|
| Base wage floor | AEWR ($19.97/hr, CA 2024 example) | State minimum wage or FLC-quoted rate | Existing piece rate + OT premium |
| Housing | Employer-provided, mandatory | Not employer-provided | N/A |
| Transport | Inbound/outbound reimbursement required | Contractor-arranged, cost passed through | N/A |
| Guarantee obligation | 3/4 of contract-period workdays | None | None |
| Lead time to deploy | Weeks (recruitment/visa) | Days | Same day |
| Best use | Planned season-length labor | Short, unplanned gap-fill | Weather-driven short push |

Rule of thumb: price the full landed cost (wage + housing + transport + guarantee exposure) before comparing hourly rates across sources — H-2A's higher posted wage often nets cheaper per finished box once a day-haul contractor's markup and turnover are counted, and vice versa for a one-week gap.
