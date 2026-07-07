# Playbook

Filled worksheets and tables for route servicing, restocking, and cash reconciliation across snack/cold-drink/coffee/fresh-food vending, bill validators and coin mechanisms, and arcade/amusement units.

## 1. Par-level worksheet

Par = (average daily velocity × days until next scheduled visit) × safety factor, capped at physical slot capacity. Restock to par, not to capacity, unless par exceeds capacity — that's a signal the slot is undersized, not an instruction to overfill.

| Slot / SKU | Avg. daily velocity | Cycle length (days) | Safety factor | Computed par | Slot capacity | Restock to | Flag |
|---|---|---|---|---|---|---|---|
| Snack1 – Chips | 4.2 | 3.5 | 1.15 | 16.9 | 10 | 10 (full) | Undersized — demand exceeds capacity by cycle end; see §2 |
| Snack2 – Candy | 1.8 | 3.5 | 1.15 | 7.2 | 10 | 7 | none |
| Snack3 – Crackers (low velocity) | 0.6 | 3.5 | 1.15 | 2.4 | 10 | 2 | Candidate for SKU consolidation |
| Cold-drink1 – Soda | 6.5 | 3.5 | 1.15 | 26.2 | 30 | 26 | none |
| Coffee – Cup count | 12.0 | 3.5 | 1.10 | 46.2 | 50 | 46 | none |
| B-6 Fresh food (TCS) | 4.0 | 3.5 | 1.05 (low, spoilage risk if overstocked) | 14.7 | 16 | 15 | Restock conservative — excess unsold TCS product is a discard, not carried inventory |

Safety factor is lower on TCS/perishable slots deliberately: overstocking a non-perishable slot just ties up cash until the next cycle, but overstocking a perishable slot converts unsold inventory directly into a discard cost.

## 2. Slot-capacity-vs-demand check

When computed par exceeds physical slot capacity, the slot cannot carry a full cycle's demand no matter how it's restocked. Quantify before choosing a fix:

1. Days slot lasts at full restock = capacity ÷ daily velocity.
2. Days empty in the cycle = cycle length − days slot lasts.
3. Lost-sale units = days empty × daily velocity.
4. Lost-sale value = lost-sale units × retail price.
5. Compare lost-sale value per cycle (× visits/week) against the route's per-visit cost. Off-cycle top-off only justified if lost-sale value exceeds that visit cost; otherwise the correct fix is a second slot for the SKU, a shorter cycle at that stop, or accepting the loss as priced and documented.

**Example (Snack1 – Chips):** 10 ÷ 4.2 = 2.38 days lasts; 3.5 − 2.38 = 1.12 days empty; 1.12 × 4.2 = 4.7 units lost; 4.7 × $1.75 = $8.23/cycle, ~$16.45/week at 2 visits/week. Route's standard per-visit cost: $35. $16.45 < $35 → do not add an off-cycle visit; reallocate a second slot instead.

## 3. Route/stop viability table

Contribution margin assumption: 28% of gross vending revenue after cost of goods (vending industry typical range), amortized against route service cost per stop.

| Stop | Weekly revenue | Contribution (28%) | Visits/week | Cost/visit | Total route cost | Net contribution | Status |
|---|---|---|---|---|---|---|---|
| A (office park) | $890 | $249.20 | 2 | $35 | $70 | +$179.20 | Healthy |
| B (hospital break room) | $1,470 | $411.60 | 2 | $35 | $70 | +$341.60 | Healthy |
| C (manufacturing plant) | $310 | $86.80 | 2 | $35 | $70 | +$16.80 | Marginal — two consecutive cycles below $25 net triggers review |

**Marginal-stop decision gate, in order:**
1. Net contribution positive but below the route's marginal-stop threshold (here, $25/week) for 2+ consecutive cycles → review before dropping: consolidate low-velocity SKUs, reduce to 1 visit/week, or add a higher-velocity machine class if space allows.
2. Net contribution negative for 2+ consecutive cycles with no consolidation option → recommend removal to route management, with the per-cycle loss figure attached.
3. Never drop a stop on a single low-revenue cycle — check for a one-off cause (holiday, facility closure) before treating it as a trend.

## 4. Jam/fault triage tree by machine class

**Bill validator / coin mechanism:**
1. Pull the accept/reject counter before opening the path — first-insert acceptance rate and false-reject rate since last service.
2. Acceptance ≥ 95%, false-reject ≤ 2–3% → jam is likely a one-off (damaged note/coin); clear and test, no service needed.
3. Acceptance below 95% or false-reject above 2–3% → clean optical sensors and transport belt/coin path first.
4. Still out of spec after cleaning → recalibrate against OEM currency-tolerance test notes; only escalate to full mechanism swap if recalibration fails.

**Refrigeration / temperature (TCS product):**
1. Pull the cumulative time-above-threshold log, not just the current reading.
2. Past the documented allowance (e.g., 30 min above 41°F) → discard flagged product immediately, no exception.
3. Within allowance → no discard; if excursions are recurring (2+ of last 4 visits), flag the defrost-cycle interval or door-seal integrity for review regardless of this visit's outcome.

**Mechanical jam (spiral motor, delivery chute, hopper):**
1. Check jam counter and last-service date for that slot/mechanism.
2. First occurrence → clear debris/obstruction, test-vend, close out.
3. Second+ occurrence on the same slot within the current review window (rolling 2 weeks) → service or replace the motor/mechanism instead of clearing again.

**Arcade/amusement PCB:**
1. Check power-supply rail voltages (typically 5V logic, sometimes 12V for I/O) against the board's rated tolerance before condemning the board.
2. Voltages in spec, board still fails self-test → check battery-backed RAM/CMOS battery (common cause of reset-loops and setting loss on older custom PCBs) before ordering a replacement board.
3. Voltages out of spec → service or replace the power supply first; re-test the board only after supply is confirmed in spec.

## 5. Cash-reconciliation log

Per machine, per visit: compare telemetry-expected cash (vend count × price) against physical count.

| Field | Value |
|---|---|
| Machine ID | B-8 |
| Telemetry-expected cash (vend count × price) | $212.40 |
| Physical cash-box count | $187.15 |
| Variance ($) | $25.25 |
| Variance (%) | 11.9% |
| Threshold (greater of $10 or 3%) | $10 vs. $6.37 → $10 applies, both exceeded |
| Action | Open variance ticket; note coin/bill path condition separately; do not close as "recounted" |

**Investigation trigger, in order:**
1. Variance exceeds the greater of $10 or 3% of expected → open a ticket before leaving the stop.
2. Check whether the variance direction is consistent with a plausible mechanical cause (e.g., coin mechanism under-crediting, a documented refund/test-vend not logged) before treating it as custody-related.
3. No plausible mechanical explanation → escalate to route management as a custody-review item, with the exact figures attached, not a description.
