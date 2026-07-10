# Agricultural Technician Playbook

Filled, executable references — not descriptions. Defaults, not laws; deviate consciously and note why in the field log.

## 1. Soil sampling grid density and collection

| Field variability | Sample density | Cores per composite | Depth | Pattern |
|---|---|---|---|---|
| Low (uniform soil series, flat, no manure history) | 1 sample per 2.5–5 acres | 8–10 cores, 8–10 ft radius of grid point | 0–8 in (row crops); 0–4 in for no-till pH-only checks | Scattered evenly within radius |
| Moderate (visible yield-map patches, mixed series) | 1 sample per 2.5 acres (grid) or per management zone | 8–10 cores | 0–8 in | Grid points on a fixed spacing, or zone-delineated by yield/soil map |
| High (manure history, variable topography, salinity concerns) | 1 sample per 1–2.5 acres | 10–15 cores | 0–8 in, plus a 8–24 in subsample if nitrate carryover is in question | Zone sampling weighted to management history, not a uniform grid |

**Rejection rule:** any single core taken within 15 ft of a fence line, gate, old manure/lime pile, dead furrow, or standing water gets discarded and replaced — do not composite it in "to save time." Note the discard and its replacement in the field log.

**Timing default:** sample at the same point in the crop rotation and season year over year (e.g., always post-harvest, pre-freeze) — comparing a spring sample one year to a fall sample the next manufactures a trend that is really a seasonal artifact.

## 2. Tissue sampling by crop and stage

| Crop | Stage | Plant part | Plants per composite |
|---|---|---|---|
| Corn | V6–V18 (pre-tassel) | First fully-developed leaf below the whorl (collar visible), cut at the base | 15–25 (default 20) |
| Corn | R1 (silking) | Ear leaf (leaf at the ear node) | 15–25 (default 20) |
| Soybean | Pre-bloom | Most recently mature trifoliate | 20–25 |
| Wheat | Feekes 6–8 | Uppermost fully-developed leaf | 30–40 (smaller plant mass per sample) |

**Default:** composite from plants spread across the field's full sampling pattern, never from a single row or the truck-accessible edge. Bag and label with field ID, date, growth stage, and sampler initials before moving to the next field — same-day mislabeling is the most common cause of a tissue result that "doesn't match" the visible symptom.

**Interpretation handoff:** report the lab's raw ppm/percent values plus whether each nutrient falls below, within, or above the published sufficiency range for that crop/stage — flag anything below sufficiency, don't just attach the lab sheet.

## 3. IPM scouting protocol and economic threshold framing

**Pattern:** zigzag or M/W-shape through the field, entering at least 50–75 ft past the edge to avoid border effects; minimum 5 unique sampling points per field under 40 acres, more for larger or irregularly shaped fields. After tasseling in row crops, switch to an X-pattern moving along rows.

**Frequency:** weekly during the growing season as a floor; increase to twice weekly during a pest's known peak emergence window (use a GDD model, not the calendar) or when weather favors rapid population growth (warm, humid stretches for many foliar pests and mites).

**Record with every count:** date, time of day, air temperature, wind, and plant growth stage — a count with no conditions attached can't be compared to next week's count.

**Threshold decision table (example structure — populate per crop/pest/region from the current extension guide, thresholds shift by region and year):**

| Pest | Crop | Threshold | Action if crossed |
|---|---|---|---|
| Soybean aphid | Soybean, R1–R5 | 250 aphids/plant, population increasing, on 80%+ of plants sampled | Flag for treatment decision within 5–7 days; recheck in 3–4 days if borderline |
| European corn borer | Field corn, whorl stage | 25–30% of plants with fresh whorl feeding | Flag for treatment window before larvae bore into stalk |
| Spider mites | Soybean, dry/hot stretch | Stippling visible on lower canopy + mites present on underside of leaves in majority of samples | Flag; recheck in 3 days — mite populations can double in under a week in hot, dry conditions |

**Threshold judgment call:** a raw count above the number in the table is a flag to escalate, not an automatic spray order — note beneficial-insect presence (lady beetles, parasitic wasps) and days remaining before the pest's damaging stage in the same report, since the supervising agronomist weighs both against the count.

## 4. Sprayer calibration — 1/128-acre catch method

1. Confirm nozzle type, rated GPM, target GPA, target ground speed, and nozzle spacing from the job's tank-mix label and rate sheet.
2. Compute catch time in seconds: `(43,560 ÷ 128) ÷ (nozzle spacing in ft) ÷ (speed in mph × 1.4667)`.
3. Verify actual ground speed with GPS over a measured 100–200 ft run before trusting the display — a slipping wheel or radar speed sensor under- or over-reports speed and throws off every downstream number.
4. Catch output from at least 3–4 nozzles across the boom for the computed time; ounces caught = GPA directly under this method.
5. Compute the coefficient of variation across catches. **CV ≤ 10%: within tolerance, individual nozzles are not the issue.** CV > 10–15%: inspect and replace the outlier nozzle tip(s) first.
6. If catches agree with each other (low CV) but the mean is off the target GPA by more than ~5%, treat it as a system-wide cause: pressure regulator setting, strainer restriction (check both the master strainer and the individual nozzle-body strainers — a boom-side gauge won't see a restriction downstream of it), pump wear, or an incorrect ground-speed reading feeding a rate controller.
7. Re-catch after any correction before releasing the rig for the field. Log pre- and post-correction catch values, CV, and root cause — not just "recalibrated."

**Not interchangeable:** airblast/orchard sprayers use tree-row-volume calibration, not the 1/128-acre method — matching output to canopy volume per row, not a flat-ground swath assumption.

## 5. Irrigation scheduling trigger

1. Establish field capacity for the sensor's install depth by reading volumetric water content (VWC) 12–24 hours after a saturating irrigation or rain event, once soil has drained freely.
2. Establish the management allowable depletion (MAD) for the crop and growth stage — default 50% of plant-available water (field capacity minus wilting point) for most row crops; tighten to 30–35% during a yield-critical stage (silking/pollination in corn, pod-fill in soybean, tuber bulking in potato) where stress has an outsized yield cost.
3. Flag for irrigation when current VWC depletion reaches the MAD threshold, not when the crop shows visible stress — visible wilting in many crops already reflects yield loss that already happened.
4. Cross-check the sensor-driven flag against a short-range forecast — hold off if 0.5+ inches of rain is reasonably likely within 24–48 hours, and note the held-off flag in the log so it isn't lost if the rain doesn't arrive.

## 6. Seed germination and viability testing (AOSA)

- **Standard germination test:** 4 replications of 100 seeds each (400 total), incubated per the AOSA-specified media/temperature/duration for that species; report percent normal seedlings, percent hard seed, and percent dormant seed as whole numbers.
- **Tetrazolium (TZ) test:** 200 seeds, used to distinguish a genuinely dead seed from a dormant-but-viable one when a germination test alone under-reports viability (common in freshly harvested or hard-seeded lots). Positive (pink/magenta) staining in the embryo and critical structures = viable; report percent viable and percent non-viable separately from the germination percentage — the two numbers answer different questions and should never be merged into one "quality" figure.
- **Discrepancy rule:** if a lab's germination result differs from the seed tag by more than 5 percentage points, resample from a different, larger portion of the same lot before flagging the lot itself — sampling variance at small seed counts is a common false alarm.
