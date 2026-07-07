# Playbook

Filled templates a chef/head cook actually runs, not descriptions of them. Numbers are worked examples — swap in real costs, but keep the structure and the math.

## 1. Recipe/plate costing card

One card per menu item. AP (as-purchased) cost is what the invoice says; EP (edible portion) cost accounts for trim/waste via yield %. Formula: **EP cost = AP cost ÷ yield %**.

**Item: Seared Salmon, 6oz portion**

| Component | AP cost | Yield % | EP cost | Portion | Extended cost |
|---|---|---|---|---|---|
| Salmon fillet, skin-on | $11.20/lb | 88% (pin-bone/skin trim) | $12.73/lb | 6oz (0.375 lb) | $4.77 |
| Jasmine rice | $0.90/lb cooked | 100% | $0.90/lb | 4oz (0.25 lb) | $0.23 |
| Charred broccolini | $2.60/lb | 85% (stem trim) | $3.06/lb | 3oz (0.1875 lb) | $0.57 |
| Beurre blanc | — | — | — | 2oz | $0.65 |
| Garnish (herb oil, micro) | — | — | — | — | $0.18 |
| **Total plate cost** | | | | | **$6.40** |

Menu price $24.95 → food cost % = 6.40 ÷ 24.95 = **25.6%**. Target for a protein-forward entrée at this price point: 28–32%; this item runs under target, meaning it has room to absorb a price freeze if a lower-mix item elsewhere needs a subsidy, or room for portion generosity if guest-facing value is the goal.

**Reading the card:** if EP cost is more than ~10% above what the last costing cycle showed, the yield % or the AP price moved — check both before assuming theft or waste; a new purveyor's fillets trimming heavier is a yield problem, not a portioning problem.

## 2. Menu-engineering worksheet

Run monthly per category (entrées, apps, etc. scored separately — don't mix a $9 app against a $32 entrée).

**Category: Entrées, 4 items, 1,000 units sold this period**

| Item | Units | Mix % | Price | Cost | CM $ | Classification |
|---|---|---|---|---|---|---|
| Chicken Parmesan | 450 | 45% | $18.95 | $5.98 | $12.97 | Plowhorse |
| Braised Short Rib | 300 | 30% | $26.95 | $11.20 | $15.75 | Star |
| Seared Salmon | 150 | 15% | $24.95 | $8.20 | $16.75 | Puzzle |
| Wild Mushroom Risotto | 100 | 10% | $19.95 | $4.10 | $15.85 | Puzzle |

- Popularity threshold = 70% × (100% ÷ 4 items) = 70% × 25% = **17.5% mix**.
- Average CM = (12.97 + 15.75 + 16.75 + 15.85) ÷ 4 = **$15.33**.
- Classification rule: mix ≥ 17.5% and CM ≥ $15.33 → **Star**. Mix ≥ 17.5% and CM < $15.33 → **Plowhorse**. Mix < 17.5% and CM ≥ $15.33 → **Puzzle**. Mix < 17.5% and CM < $15.33 → **Dog**.

**Action by quadrant:**
- **Star (Short Rib):** protect — don't change the recipe, don't discount it, feature it on any menu redesign.
- **Plowhorse (Chicken Parm):** reformulate cost down before touching price; it's carrying volume the rest of the menu depends on.
- **Puzzle (Salmon, Risotto):** reposition — move up the menu, add a server upsell script, or pair with a promotion; if mix doesn't move in one full cycle (usually 60–90 days), consider cutting.
- **Dog (none this cycle):** default to cutting at the next menu print unless it serves a non-financial role (a vegan option required for group bookings, a dish tied to a chef's signature).

## 3. Prime-cost tracker

Run weekly, not monthly — prime cost drifts fast and a monthly view catches it a month late.

| Week | Food sales | Food cost $ | Food cost % | Labor $ | Labor % | Prime cost % | Band |
|---|---|---|---|---|---|---|---|
| Wk 1 | $47,200 | $14,632 | 31.0% | $14,160 | 30.0% | 61.0% | Needs a plan |
| Wk 2 | $48,000 | $16,320 | 34.0% | $14,400 | 30.0% | 64.0% | Needs a plan |
| Wk 3 (post-fix) | $47,600 | $14,708 | 30.9% | $14,280 | 30.0% | 60.9% | Needs a plan (improving) |
| Wk 4 (post-fix) | $48,400 | $14,278 | 29.5% | $14,520 | 30.0% | 59.5% | Acceptable |

Bands: **≤60% acceptable, 60–65% needs a plan, >65% survival-level red flag.** Track the trend line, not a single week — one bad week (a large comped event, a delivery miss) is noise; three consecutive weeks above 62% is signal.

## 4. Receiving and par sheet

Every delivery gets scale-checked and date-labeled on arrival — not at prep time.

| Item | Par (min/max) | Delivered qty | Invoice weight | Scale-checked weight | Variance | Action |
|---|---|---|---|---|---|---|
| Roma tomatoes, case | 2 / 6 cases | 4 cases | 100 lb (25/case) | 94 lb | −6% | Note on invoice, photo, notify vendor same day |
| Salmon fillets, 6oz | 20 / 60 portions | 45 portions | 16.9 lb | 16.85 lb | −0.3% | Within tolerance (±2%), accept |
| Heavy cream, case | 1 / 3 cases | 2 cases | — | — | — | Date-label, rotate to back of walk-in behind existing stock (FIFO) |

**Rule:** variance beyond ±2% on any delivery over $200 gets documented same-day (photo + note on invoice) and is the first item raised at the next vendor call — undocumented variance has no leverage at contract renewal or if the pattern repeats.

## 5. HACCP temperature log (excerpt)

| Time | Check | Reading | Standard | Pass/Fail | Initials |
|---|---|---|---|---|---|
| 7:15am | Walk-in cooler | 38°F | ≤40°F | Pass | J.M. |
| 7:20am | Reach-in, line | 41°F | ≤40°F | **Fail — recheck** | J.M. |
| 7:35am | Reach-in, line (recheck) | 39°F | ≤40°F | Pass (door seal adjusted) | J.M. |
| 11:00am | Chicken breast, cooked | 168°F | ≥165°F | Pass | R.T. |
| 11:00am | Cooling curve start (soup, 190°F) | — | 135°F→70°F in 2 hrs | logged, recheck 1:00pm | R.T. |
| 1:00pm | Cooling curve, 2hr check | 68°F | ≤70°F at 2hrs | Pass, continue to 41°F by 5:00pm | R.T. |

**Rule:** any single Fail gets a same-shift recheck logged, not just a note to "watch it" — a second Fail on the same unit within 24 hours escalates to a work order, and product in that unit gets moved or discarded per the danger-zone rule (out of 40–140°F for more than 4 hours cumulative = discard, no exceptions for cost).
