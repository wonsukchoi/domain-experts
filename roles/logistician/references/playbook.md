# Logistician Playbook

Filled worksheets, not descriptions of worksheets. Defaults, not laws — deviate consciously and note why.

## 1. Safety stock / reorder point walkthrough

**Step 1 — pull the right demand series.** Use the echelon closest to true end-customer demand. If only DC-to-DC order history is available, check its coefficient of variation (CV = σ/mean) against a known downstream POS or sell-through series for the same product family; a DC-order CV more than ~1.5× the sell-through CV is a bullwhip signal — go get the truer series before proceeding.

**Step 2 — clean the series.** Exclude or correct:
- Stockout windows: don't use realized sales as demand; either use the pre-stockout run rate for that window or a statistical demand-during-stockout estimator. Flag the correction in the output, don't silently patch it.
- One-time promotional or bulk-buy spikes: pull them into a separate "promotional demand" bucket, modeled separately (its own lead time and buffer, since promo replenishment usually runs on expedited terms).

**Step 3 — compute variability.**

| Input | Example value |
|---|---|
| Mean weekly demand (d) | 340 units |
| σ of weekly demand (σ_d) | 85 units |
| Mean lead time (L) | 3 days = 0.4286 wk |
| σ of lead time (σ_L) | 1 day = 0.1429 wk |
| Lead-time CV (σ_L / L) | 0.333 (33%) → above the 25% flag threshold; lead-time variance likely dominates |

**Step 4 — pick the formula by review system.**

- Continuous review (Q, R) — reorder the moment inventory hits R, order a fixed Q each time:
  `SS = z · σ_LTD`, where `σ_LTD = √(L·σ_d² + d²·σ_L²)`
  `ROP = d·L + SS`
- Periodic review (order-up-to S) — review every R time units, order up to S:
  `SS = z · σ_(R+L)`, where `σ_(R+L) = √((R+L)·σ_d² + d²·σ_L²)`
  `S = d·(R+L) + SS`

Using continuous review on the example above (L = 0.4286 wk, no fixed review interval):
`σ_LTD = √(0.4286 × 85² + 340² × 0.1429²) = √(3,096.6 + 2,357.9) = √5,454.5 = 73.9`
`SS = 1.96 × 73.9 ≈ 145 units` — smaller than the periodic-review number in SKILL.md's worked example (221 units at R=1 week) because continuous review doesn't carry the extra week of review-interval exposure. **This is the single most common real-world sizing error**: applying the continuous-review formula to a system that actually reviews weekly (or on a truck schedule) understates safety stock by omitting the R term.

**Step 5 — translate to fill rate.** Cycle service level (probability of no stockout in a cycle) is not the same number as fill rate (% of units demanded that ship from stock). At z = 1.96 (97.5% cycle service level) with a coefficient of variation around 0.25, expect fill rate in the high 98–99% range — always state which one is being quoted; a "97.5% service level" claim describing fill rate versus cycle service level implies different buffer sizes.

## 2. Mode/frequency total landed cost worksheet

Fixed inputs: lane 1,200 mi, unit cost $14, unit weight 23.5 lb, 22%/yr holding rate ($3.08/unit/yr), demand mean 340/wk, σ_d 85/wk.

| Option | Rate basis | Transit (days, σ) | R (wk) | Freight/shipment | Shipments/yr | Freight/yr | Avg inventory (SS+cycle) | Carrying/yr | **Total/yr** |
|---|---|---|---|---|---|---|---|---|---|
| Weekly LTL | $38/cwt, 80 cwt | 3, ±1 | 1 | $3,040 | 52 | $158,080 | 391 | $1,204 | **$159,284** |
| Biweekly TL | $2.10/mi flat | 2, ±0.5 | 2 | $2,520 | 26 | $65,520 | 596 | $1,836 | **$67,356** |
| 4-week TL | $2.10/mi flat | 2, ±0.5 | 4 | $2,520 | 13 | $32,760 | 1,028 | $3,166 | **$35,926** |

Read the table as a curve, not three isolated points — check at least one interval past the apparent winner (here, 5–6 weeks) before recommending, and check the physical constraint (truckload legal weight limit, ~44,000 lb) that will eventually reverse the curve. The point where order weight would exceed one truckload is the real search boundary, not an arbitrarily chosen stopping interval.

**When NOT to use this worksheet as-is:** if the SKU has a shelf-life or engineering-change-obsolescence risk inside the review interval, add an expected-obsolescence cost term to the carrying cost before comparing — a 4-week interval that's cheaper on pure holding cost can still lose if 3% of the extra cycle stock is written off before it sells.

## 3. ABC/XYZ segmentation — where to spend analysis time

| | X (CV < 0.5, steady) | Y (CV 0.5–1.0) | Z (CV > 1.0, erratic) |
|---|---|---|---|
| **A (top ~80% of $ volume)** | Full statistical SS/ROP, reviewed quarterly | Full statistical SS/ROP, reviewed monthly | Statistical SS/ROP + manual override review; consider vendor-managed inventory or supplier buffer instead |
| **B (next ~15%)** | Statistical SS/ROP, reviewed semi-annually | Statistical SS/ROP, annual review | Simplified buffer (e.g., 1.5× average demand during lead time) — full modeling cost exceeds the value at risk |
| **C (remaining ~5%)** | Flat buffer (2–4 weeks of demand), annual sanity check | Flat buffer, annual sanity check | Flat buffer or make-to-order where the supplier allows it; do not build a statistical model for a CZ item |

Rule of thumb: if the annual value of a SKU is under ~$5K and demand CV exceeds 1.0, the analyst-hours to build and maintain a proper statistical model usually cost more than the inventory saved by having one — default to the flat buffer and revisit only if that SKU crosses into a higher tier.

## 4. Center-of-gravity pass for a DC-count question

Weighted centroid: `X = Σ(volume_i × x_i) / Σvolume_i`, `Y = Σ(volume_i × y_i) / Σvolume_i`, using customer/demand-point coordinates weighted by shipment volume (not customer count — a low-volume, far-flung account shouldn't pull the centroid).

Example: evaluating whether a 4-DC network (East, Central, West, South) should add a 5th DC in the Southeast to relieve the Central DC's coverage of that region.

| Step | Result |
|---|---|
| 1. Demand-weighted centroid of Southeast-region customers | Lands ~140 miles from a candidate site near Atlanta |
| 2. Current avg outbound distance from Central DC to Southeast customers | 610 miles |
| 3. Avg outbound distance from Atlanta candidate site | 95 miles |
| 4. Estimated outbound freight saved per year (515 mi saved × 2,100 tons/yr to that region × $0.18/ton-mile blended rate) | ≈ $195,000/yr |
| 5. Added fixed cost of a 5th DC (lease, labor, systems) | ≈ $410,000/yr |
| 6. Added inventory (new DC needs its own safety stock layer, not just a slice of Central's) | ≈ $85,000/yr carrying cost, per the SS formula above applied per-SKU at the new node |

Net result: -$300,000/yr — a 5th DC does not pay for itself on freight savings alone at this volume; the freight-savings curve has already flattened per the diminishing-returns heuristic (SKILL.md). The decision should hinge on a factor this worksheet doesn't price — same-day/next-day service commitments the Southeast region needs that the current 610-mile lane can't hit — not on the cost table alone. State that explicitly rather than letting a negative NPV silently answer a service-level question it wasn't built to answer.
