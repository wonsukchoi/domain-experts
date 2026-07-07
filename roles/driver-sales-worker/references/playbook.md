# Driver/Sales Worker — Playbook

Filled reference sequences: space-to-sales facing calculation, par/order resizing, stale-rate tracking, and route revenue-per-stop reconciliation.

## 1. Space-to-sales facing calculation

Never assume an even split across facings — pull the account's own facing-test history (or the category's documented curve) and use the marginal, not average, unit.

**Facing-test data for this SKU line (trailing average from prior resets):**

| Facings | Units/week | Marginal gain vs. one fewer facing |
|---|---|---|
| 1 | 50 | — |
| 2 | 78 | +28 (56%) |
| 3 | 96 | +18 (23%) |
| 4 | 108 | +12 (11%) |

```
Naive (even-split) loss for cutting 1 of 3 facings = 96 ÷ 3        = 32 units/week
Actual (marginal) loss for cutting 3 → 2 facings   = 96 − 78       = 18 units/week
```

**Rule:** always compute the marginal loss between the current and proposed facing count from the account's own curve — the naive even-split number is a ceiling estimate, not the real one, and using it either over-concedes in a countertrade or under-prepares for the operational follow-through (par resize below).

**Share-of-shelf vs. share-of-$ leverage check**, run before agreeing to which SKU concedes:

```
Share of shelf = rep's facings ÷ total category facings
Share of $     = rep's category dollar sales ÷ total category dollar sales

Example: 3 facings ÷ 20 total facings = 15% share of shelf
         34% share of category $
         Gap = 34 − 15 = 19 points → underspaced; use as leverage
```

If the gap is under ~5 points, the account isn't obviously underspaced and a facing cut is harder to contest on data alone — shift the negotiation to *which* SKU concedes rather than *whether* one does.

## 2. Par/order resize after a facing or demand change

Standing order must track physical shelf capacity and trailing sell-through, recalculated the same visit a facing count changes — never carried forward.

```
New target order (units) = new expected sell-through/week + safety buffer

Example: facings cut 3 → 2, new expected demand = 78 units/week
         Case pack = 12 units
         Cases needed to cover demand = 78 ÷ 12 = 6.5 → round up to 7 cases (84 units)
         Buffer built in = 84 − 78 = 6 units (~7.7%), sized to the twice-weekly visit cadence
```

**If the order is left unresized** (still 8 cases/week = 96 units against 78 units/week of shelf-supported demand), the excess 18 units/week accumulates as backstock. On a 45-day code date, that backlog reaches roughly 108 excess units by week 6 before a routine stale-pull catches it — the point of resizing immediately is to never let that backlog form.

## 3. Stale-rate tracking and commission reconciliation

Stale rate = stale/return credit ÷ gross delivered value. Compare each account against its own trailing 8-week average, not a chain-wide number.

**Scenario A — order resized correctly at the facing cut:**

```
Delivered   = 84 units × $2.75           = $231.00/week
Stale (2.0% baseline)                    = $4.62/week
Net         = $231.00 − $4.62            = $226.38/week
Commission (10% of net)                  = $22.64/week
```

**Scenario B — order left unresized, backlog hits code date over a 6-week window:**

```
Delivered (unchanged)        = 96 units × $2.75 × 6 weeks   = $1,584.00
Excess accumulated           = (96 − 78) × 6                = 108 units
Stale credit on pull         = 108 × $2.75                  = $297.00  (18.75% of 6-wk gross, vs. 2.0% baseline)
Net over 6 weeks             = $1,584.00 − $297.00           = $1,287.00
Commission (10% of net)      = $128.70 total ($21.45/week avg)
```

**Reconcile:** Scenario A over the same 6 weeks = $226.38 × 6 − ($4.62 × 6 already netted) = $1,358.28 net → $135.83 commission. Difference vs. Scenario B = $135.83 − $128.70 = **$7.13** over 6 weeks — a real but modest dollar gap; the larger cost is a stale spike landing in front of the same account whose facing negotiation depends on the rep's credibility.

## 4. Route revenue-per-stop vs. cost-per-stop

```
Cost per stop  = (drive time × loaded labor/vehicle rate) + service time + fuel share per stop
Revenue per stop = average order value at that stop

Example: 30-stop route, 8-hour day, $34/hr fully loaded driver+vehicle cost, $46 fuel for the day
         Avg drive+service time per stop = 12 minutes = 0.2 hr → labor cost/stop = 0.2 × $34 = $6.80
         Fuel per stop = $46 ÷ 30                                                  = $1.53
         Fully loaded cost per stop                                               = $8.33

Rule of thumb: flag a stop if avg order value < 3 × cost-per-stop (here, < $25.00)
```

**Route-level reconciliation (weekly), built from the same $8.33/stop figure above:**

| | Stops/week | Revenue/week | Cost/week (180 or 2 stops × $8.33) | Net/week |
|---|---|---|---|---|
| Route total | 180 (30/day × 6 days) | $9,450 (avg $52.50/stop) | $1,499.40 | $7,950.60 |
| Weakest account (flagged) | 2 (twice-weekly) | $38 | $16.66 | $21.34 |

The weakest account still nets positive, but at $19/stop average order value it's under the $25 threshold — a candidate to fold into a neighboring stop's cycle or drop to weekly service rather than twice-weekly, freeing route time for higher-revenue stops rather than a reason to drop it outright on cost alone.
