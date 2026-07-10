# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## RTK fix vs. float vs. autonomous

- **Definition:** three tiers of GNSS correction status. RTK fixed resolves the carrier-phase ambiguity for centimeter-level accuracy; RTK float is an unresolved intermediate solution accurate to roughly decimeters; autonomous (no correction) is meter-plus accuracy.
- **Practitioner usage:** "We were fixed for the first 40 acres then dropped to float behind the tree line — pull that segment before you build the rate file, it's not centimeter data anymore."
- **Common misuse:** treating "RTK" as a single accuracy guarantee. A system labeled RTK that's currently in float mode is not delivering RTK-grade accuracy; the display often doesn't make the distinction obvious to an untrained operator.

## Management zone

- **Definition:** a delineated area within a field treated as agronomically distinct for sampling or variable-rate purposes, built from layered evidence (yield stability, soil ECa, imagery) rather than a single measurement.
- **Practitioner usage:** "That's a provisional zone — only the yield layer agrees, ECa and imagery are ambiguous there, so I wouldn't set a rate program off it yet."
- **Common misuse:** treating any single-layer classification (just last year's yield map, just one NDVI pass) as a finished management zone, and building a capital-intensive rate program on a one-season hypothesis.

## Apparent electrical conductivity (ECa)

- **Definition:** a proxy measurement (via electromagnetic induction sensors like EM38 or Veris) of soil properties — primarily texture, moisture-holding capacity, and salinity — used to infer productivity zones without direct chemical analysis.
- **Practitioner usage:** "ECa split this field into a sandy low-CEC strip along the ridge and heavier ground in the draw — that lines up with the yield stability map, so I trust this boundary."
- **Common misuse:** treating ECa as a direct soil-fertility measurement. It measures physical/electrical soil properties, not nutrient levels — it still needs a soil test to translate into a fertility recommendation.

## ISOBUS / ISO-XML (ISO 11783)

- **Definition:** ISOBUS is the ISO 11783 standard for digital communication between tractors, implements, and displays across manufacturers; ISO-XML (ISO 11783-10) is the file format used to exchange task and rate data between farm-management software and an ISOBUS-compliant controller.
- **Practitioner usage:** "Export it as ISO-XML version this terminal's firmware actually supports — the newer export format is why it's showing unsupported file."
- **Common misuse:** assuming any "ISOBUS-compatible" label guarantees a file will load. Version mismatches between the exporting software and the terminal's firmware are a routine, specific failure mode, not a general compatibility question.

## As-applied map

- **Definition:** the record of what a controller actually delivered during a pass — rate, product, position, timestamp — as opposed to the prescription, which is what was intended.
- **Practitioner usage:** "The prescription called for 186 in Zone A; the as-applied shows it averaged 179 — check for controller lag on the zone transitions before you trust the prescription math."
- **Common misuse:** treating the prescription file as a record of what happened. Only the as-applied data confirms execution; controller lag, section-control overlap, and operator override can all make the two diverge.

## Headland trim / header-status filter

- **Definition:** the data-cleaning step that removes yield points recorded while the header is not in a fully engaged working position, typically concentrated at field borders and turns.
- **Practitioner usage:** "Don't read that low-yield ring around the field edge as a real agronomic zone — that's headland artifact, trim it before you build the stability map."
- **Common misuse:** either skipping the trim (headland artifacts leak into zone boundaries) or over-trimming (cutting real interior low-yield areas that happen to sit near an access point) without checking which case applies.

## Sample grid vs. zone sampling

- **Definition:** grid sampling collects soil samples on a uniform geometric grid (commonly 1–3 acres per point) regardless of known field variability; zone sampling collects composite samples within pre-delineated management zones built from other data layers.
- **Practitioner usage:** "No yield history on this rented ground yet, so we're grid-sampling this year at 2.5 acres and we'll shift to zone sampling once we have a stability map to work from."
- **Common misuse:** defaulting to grid sampling out of habit on fields that already have three-plus years of yield data and an ECa survey, where zone sampling would capture the same variability at a fraction of the sample count and cost.

## Variable rate technology (VRT)

- **Definition:** equipment and software that varies the application rate of an input (seed, fertilizer, chemical) across a field according to a prescription, rather than applying a single flat rate.
- **Practitioner usage:** "The VRT program isn't cutting total nitrogen this year — it's reallocating the same pounds from the wet zone to the sandy ridge, which is where the return actually is."
- **Common misuse:** marketing or assuming VRT inherently reduces total input use. Its value is usually in matching supply to zone-specific demand, not in a blanket reduction, and overselling it as automatic savings sets up a disappointing season-end comparison.

## NDVI (Normalized Difference Vegetation Index)

- **Definition:** a vegetation index derived from red and near-infrared reflectance (satellite, aerial, or drone imagery) that correlates with canopy vigor and chlorophyll activity.
- **Practitioner usage:** "NDVI flagged a low-vigor patch that doesn't match the yield-stability map — could be a new drainage issue or a sprayer skip, worth a scouting trip before we build it into next year's zones."
- **Common misuse:** reading NDVI as a direct yield predictor rather than a canopy-vigor proxy. A low-NDVI area can reflect nitrogen deficiency, disease, standing water, or simply a later planting date — the index flags where to look, not what's wrong.

## Task controller / rate controller

- **Definition:** the onboard hardware and software (often ISOBUS-based) that reads a prescription file and adjusts the physical application rate (seed metering, nozzle flow, product blend) in real time as the machine moves across zone boundaries.
- **Practitioner usage:** "The rate controller has a documented response lag of a few seconds at this ground speed — build the zone transitions with a buffer or the as-applied data will show blending across the boundary."
- **Common misuse:** assuming a rate change on the prescription map is instantaneous in the field. Every controller has a physical response time, and prescriptions built without accounting for it produce as-applied data that never matches the intended step change.

## Yield stability zone

- **Definition:** a management zone derived from multiple years of yield data, classifying areas by how consistently they perform relative to the field average rather than from a single season's result.
- **Practitioner usage:** "That's not a stability zone yet — it's one wet-year yield map. We need at least a dry year and a normal year in the mix before I'd call the boundary real."
- **Common misuse:** calling a single-season yield map a "stability zone." Stability specifically means consistency across different growing conditions, which single-year data cannot demonstrate.
