# Playbook

Filled worksheets and reference tables for the four recurring judgment calls: wage-floor reconciliation, pesticide re-entry, heat-protocol timing, and harvest/greenhouse condition checks. Adapt the numbers to the specific crop, state, and label — these are structures with plausible example values, not universal constants.

## 1. Piece-rate reconciliation worksheet

Run at the end of every pay period, per worker, per workweek — not just when a complaint arises.

**Filled example (California, $16.50/hr minimum wage):**

| Field | Value |
|---|---|
| Piece units completed | 35 flats |
| Piece rate | $2.75/flat |
| Piece earnings | $96.25 |
| Active picking hours | 6.5 |
| Average piece-rate ($/hr) | $96.25 ÷ 6.5 = **$14.81/hr** |
| Applicable floor | $16.50/hr |
| Shortfall per hour | $16.50 − $14.81 = $1.69 |
| Reconciliation pay owed | $1.69 × 6.5 = **$10.99** |
| Paid rest-break hours | 0.33 hr (two 10-min breaks) |
| Rest-break pay rate | higher of floor or average piece-rate → $16.50/hr (floor wins here) |
| Rest-break pay | 0.33 × $16.50 = **$5.45** |
| Other nonproductive hours | 0.67 hr (high-heat cool-down + trailer delay) |
| Nonproductive pay rate | $16.50/hr floor |
| Nonproductive pay | 0.67 × $16.50 = **$11.06** |
| **Total owed** | $96.25 + $10.99 + $5.45 + $11.06 = **$123.75** |
| Check | 7.5 total compensable hours × $16.50 = $123.75 ✓ |

**Rule of thumb:** whenever average piece-rate for the workweek is at or above the floor, reconciliation pay is $0 but rest-break and nonproductive pay still get itemized separately at the higher of the floor or that average rate — piece-rate systems don't get to fold rest time into piece output even on a good day.

**For H-2A workers**, substitute the posted Adverse Effect Wage Rate (AEWR) for the state/crop in place of the state minimum wage wherever it is higher; AEWR is published annually by USDA/DOL and is frequently above the state floor.

## 2. Restricted-entry interval (REI) lookup

Check the specific product label posted at the field/greenhouse entrance before any re-entry — never estimate from memory or from a "similar" product.

**Representative WPS toxicity-category intervals (label governs; these are the regulatory defaults where the label doesn't specify a longer interval):**

| Toxicity category | Example signal word | Default REI |
|---|---|---|
| I (Danger/Poison) | most organophosphates, some fumigants | 24–48 hours (some labels specify up to 72+) |
| II (Warning) | many pyrethroids | 12 hours |
| III (Caution) | many fungicides | 12 hours |
| IV (Caution, lowest) | some biologicals, low-toxicity fungicides | 4 hours |

**Application Exclusion Zone (AEZ):** no worker may be within 25 feet of ground applications (100 feet for certain aerial/airblast applications) while the application is in progress, independent of the REI that follows it.

**Re-entry checklist before a crew enters any recently treated block:**
1. Confirm the posted application record: product, application date/time, labeled REI.
2. Compute elapsed time; if elapsed < labeled REI, the block is not clear — no early entry regardless of harvest deadline.
3. Confirm PPE requirement for any activity permitted *during* the REI (e.g., irrigation checks under specific early-entry exceptions) before assigning anyone in.
4. Confirm decontamination supplies (water, soap, towels, emergency eyewash) are stocked and accessible at the field edge.
5. Log the re-entry time and who confirmed it clear.

## 3. Heat-protocol trigger table

Based on measured heat index, not felt temperature or ambient air temperature alone.

| Heat index | Trigger | Required action |
|---|---|---|
| < 80°F | Baseline | Water and shade available on request. |
| ≥ 80°F | Basic provisions | Water within reach at all times (min. 1 quart/worker/hour); shade sufficient for the crew on any break; supervisors trained to recognize heat-illness signs. |
| ≥ 95°F | High-heat procedures | Mandatory 10-minute cool-down rest at least every 2 hours (paid, separate from meal/rest breaks); buddy system or direct observation; pre-shift reminder to drink water; effective communication method to reach a supervisor. |
| Any level + symptoms observed (dizziness, confusion, stopped sweating, rapid pulse) | Emergency | Stop work for that individual immediately, move to shade/cooling, call emergency services if symptoms don't resolve quickly — do not wait for shift end to report. |

**Rule of thumb:** high-heat cool-down time is nonproductive time for piece-rate reconciliation purposes (see Worksheet 1) — it must be paid at the floor rate, not absorbed into the piece rate.

## 4. Harvest maturity indicators by crop (filled reference)

| Crop | Maturity indicator | Typical harvest threshold | Note |
|---|---|---|---|
| Wine grapes | Brix (refractometer) | 22–26° Brix depending on varietal/style | Sampled across the block, not just sun-exposed clusters. |
| Fresh-market tomatoes | USDA 6-stage color classification | Picked "breaker" to "turning" for shipping, "pink" to "light red" for near-market sale | Non-climacteric-adjacent handling: color develops post-harvest but sugar/acid largely locked in at pick. |
| Strawberries | Visual color, non-climacteric | 3/4 to full color at pick — will not ripen further off the plant | Picking under-color for shipping loses eating quality permanently, not just temporarily. |
| Hass avocado | Dry-matter % (oven test) | Minimum ~20–23% dry matter (CA Hass Avocado Commission standard) before legal harvest | Firmness alone is a poor indicator; avocados don't soften on the tree regardless of maturity. |
| Peaches/stone fruit | Firmness (penetrometer, lb-force) | ~12–14 lb-force for shipping, softer for direct local sale | Softer-at-pick fruit has a shelf life measured in days, not weeks. |

## 5. Greenhouse IPM scouting schedule

Weekly minimum, twice-weekly during high-pressure season (early vegetative growth, high humidity stretches).

**Filled example — sticky-trap action thresholds (per card, per week, greenhouse tomato):**

| Pest | Trap type | Action threshold | Typical response |
|---|---|---|---|
| Whitefly | Yellow sticky card | >5 adults/card/week sustained 2 weeks | Release *Encarsia formosa* parasitoid before escalating to chemical control. |
| Thrips | Blue sticky card | >10/card/week | Increase scouting frequency; consider targeted spinosad application if biological control lagging. |
| Spider mite | Leaf inspection (hand lens) | Visible webbing or >2 mites/leaflet on sampled leaves | Release *Phytoseiulus persimilis* predatory mite; humidity increase can also suppress mite population. |

**Climate setpoints (greenhouse tomato, representative):**

| Parameter | Day target | Night target | Disease-risk trigger |
|---|---|---|---|
| Temperature | 70–75°F (21–24°C) | 62–65°F (17–18°C) | N/A |
| Relative humidity | 65–75% | 65–75% | >85–90% sustained → increase ventilation/heating before considering a fungicide for botrytis/powdery mildew. |
| Vapor pressure deficit (VPD) | 0.8–1.2 kPa | 0.8–1.2 kPa | Below ~0.4 kPa (too humid) raises disease pressure; above ~1.5 kPa (too dry) stresses plants and can affect fruit set. |

**Rule of thumb:** adjust ventilation/heating first when RH or VPD drifts out of range; reach for a fungicide only once the climate lever has been tried and pressure persists.
