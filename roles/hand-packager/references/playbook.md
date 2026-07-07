# Playbook

Filled procedures a hand packager or line lead actually runs, with real numbers plugged in.

## 1. Net-weight / MAV compliance check

**Concept:** a sold-by-weight package must clear two independent checks — the sample's **average** must equal or exceed the labeled weight, and no individual package may fall below its **Maximum Allowable Variation (MAV)** floor. Passing one does not excuse failing the other.

**Illustrative MAV bands by declared-weight class** (planning-level, drawn from NIST Handbook 133's approach — verify the current published table before citing a figure to an inspector):

| Labeled net weight | Typical MAV (% of labeled weight)* |
|---|---|
| Under 1 oz (28 g) | ~9% |
| 1–2 oz | ~6% |
| 2–4 oz | ~4% |
| 4–8 oz | ~3% |
| 8–16 oz (1 lb) | ~1.5% |
| Over 1 lb | ~1% |

*Bands are illustrative planning figures, not the legal MAV table itself.

**Worked check — 1.5 oz (42.5 g) bag, 12-count carton:**

1. MAV floor = 42.5 g × (1 − 0.06) = 39.95 g. Any bag below this is an individual-package failure.
2. Pull the skip-lot sample (every 30th carton is a common interval; facility SOP sets the actual rate).
3. Weigh all 12 bags; compute the sample average.
4. If average < 42.5 g **or** any bag < 39.95 g, hold the batch — do not average away an individual failure, and do not wave off a low average because every single bag individually cleared MAV.
5. Trace to cause: a dispenser/scoop-calibration drift affects every unit since the last check, not just the sampled carton — flag the calibration, not the one carton.

## 2. Void-fill / cushioning selection by fragility class

**Concept:** cushioning thickness is read off a material's measured cushion curve at the shipment's expected fragility rating (G) and drop height — not a fixed "more is safer" allowance.

**Illustrative cushion guidance by fragility class** (2 ft drop, corrugated interior — illustrative of the cushion-curve method, not a substitute for the specific foam/paper's tested curve):

| Fragility class (G-rating) | Example product | Approx. cushion thickness needed |
|---|---|---|
| 100G (rugged) | canned goods, hand tools | ~0.5 in |
| 60G | small appliances, padded glassware | ~1 in |
| 40G | consumer electronics, ceramics | ~2 in |
| 25G (fragile) | glass, precision instruments | ~3+ in |

**Field procedure:**

1. Identify the product's fragility rating (from the shipper's spec sheet or a standard fragility test) — do not guess it from how the item "feels" fragile.
2. Read the required cushion thickness off the specific material's cushion curve at that G-rating and the expected drop height, not the illustrative table above.
3. Apply that thickness; check that the item cannot shift or contact the outer wall under normal handling (a hand-shake test — no discernible movement).
4. If dimensional-weight cost is rising for a SKU with no fragility-class change, that's a signal the void-fill choice has drifted off the curve — re-check against spec rather than assuming it's a conservative margin.

## 3. Allergen changeover validation

1. **Sequence runs clean-to-dirty where scheduling allows**: allergen-free SKUs before allergen-containing SKUs in the same shift, to minimize the number of changeovers needed.
2. **On any transition into, out of, or between different allergens**, execute the full changeover: disassemble contact surfaces per SOP, dry-clean (remove bulk residue) then wet-clean, and visually inspect.
3. **Swab cleaned contact surfaces with an ATP test**; require a reading below the facility's set threshold (commonly under 10 relative light units, RLU — confirm the facility's validated threshold) before approving restart.
4. **For a validated changeover on a known major allergen**, run an allergen-specific lateral-flow (ELISA) strip on a sample from the first units packed; a commonly used industry clearance threshold is under 5 ppm of the target allergenic protein — confirm against the facility's validation study.
5. **Log the changeover**: date/time, allergens cleared, ATP reading, strip result if run, approver signature.
6. **A failed swab or strip means re-clean and re-test** — never restart on a failed reading because the line "looks clean."

## 4. Repetitive-motion (hand-activity) self-check

**Concept:** risk is a function of Hand Activity Level (frequency/duty cycle of exertion) and peak force, plotted against an action-limit/TLV curve — not how a given rep felt.

| Signal | Zone | Action |
|---|---|---|
| Low repetition, low-to-moderate force, task varies within the shift | Below action limit | Continue as-is |
| High repetition (short cycle time, same motion most of the cycle) with low force | Caution zone | Monitor; consider task rotation before symptoms appear |
| High repetition combined with moderate-to-high peak force | Above TLV | Redesign task, add mechanical assist, or rotate — don't wait for a symptom report |
| Worker reports soreness concentrated in one hand/wrist tied to a specific station | Investigate now | Pull the station's cycle time and force data; treat as a task-design signal, not an individual-conditioning issue |

## 5. Rate-vs-check self-check

| Signal | Action |
|---|---|
| Current pace ≥ target, checkweigher/void-fill/changeover checks all passing | Continue as-is |
| Current pace below target, checks passing | Flag pace gap to lead as a calibration/staffing issue; do not skip checks to close the gap |
| Current pace at or above target, checkweigher failures or changeover swab failures appearing | Slow down to the pace that holds the checks; report the trend rather than waiting for an audit to catch it |
| Skip-lot sampling interval being informally widened during high-volume periods | Treat as a leading indicator — investigate before a lot-level failure ships |
