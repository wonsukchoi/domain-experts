# Red flags — what a site civil PE notices instantly

Smell tests with thresholds. Any one can be innocent; two or three together in the same calc package or submittal is a pattern worth stopping the review for.

### Post-development peak discharge exceeds the ordinance release rate by any margin, even 1–2%
- **Usually means:** the hydrology inputs (C, CN, tc, or the IDF intensity value) were pulled from a template rather than re-derived for this site, or the detention volume calc used the wrong critical storm duration.
- **First question:** "Which storm duration governs — did you check durations other than the design storm's stated one, since the critical duration for storage isn't always the design storm's nominal duration?"
- **Data to pull:** the full IDF table used, the tc calculation worksheet, and the storage-volume calc at 2–3 candidate durations bracketing the assumed one.

### Provided detention storage within ±2% of the calculated requirement
- **Usually means:** either a genuinely tight, well-executed design, or — more often — a units, duration, or area error that happened to produce a plausible-looking number with no real margin for as-built grading tolerance.
- **First question:** "Walk me through the storage calc by hand, in the units you started with, before I accept the output."
- **Data to pull:** the raw triangular-hydrograph or routing worksheet, not just the summary table.

### Bearing pressure check uses a presumptive IBC Table 1806.2 value when a project-specific geotechnical report exists
- **Usually means:** the drafter defaulted to a generic table instead of opening the report — common when foundation design happens before the geotech report is in hand and nobody circles back.
- **First question:** "Does a site-specific geotechnical report exist for this parcel, and does it supersede the presumptive value?"
- **Data to pull:** the geotechnical report's boring logs and bearing-pressure recommendation table, dated and matched to this footing's location.

### Factor of safety on bearing capacity below 2.5, or a calc that divides the report's allowable value by an additional FS
- **Usually means:** either genuinely marginal soil requiring re-design, or a double-counted factor of safety that makes an adequate footing look inadequate (over-conservative and expensive) or vice versa if the direction of the error is reversed.
- **First question:** "Is qa already a net allowable value with the report's FS applied, or are you comparing against qult?"
- **Data to pull:** the geotechnical report's page stating whether the quoted bearing value is allowable or ultimate, and the exact FS used to derive it.

### Time of concentration for post-development conditions equal to or greater than the pre-development value
- **Usually means:** the modeler reused the pre-development tc instead of recalculating for curbed/piped conveyance, which understates post-development peak intensity and undersizes the whole downstream system.
- **First question:** "What conveyance path did you trace for post-development tc — sheet flow, shallow concentrated flow, or channel/pipe flow — and does it match the actual site plan?"
- **Data to pull:** the tc worksheet segment-by-segment (sheet flow / shallow concentrated / channel flow) for both conditions.

### Water table encountered within one footing width of the bearing elevation, not addressed in the foundation calc
- **Usually means:** the boring log was reviewed for the bearing value but not cross-checked against groundwater depth, which affects both capacity and long-term settlement.
- **First question:** "What's the water table depth at this specific footing location, and does the bearing value already account for submerged unit weight?"
- **Data to pull:** boring log groundwater readings (including any seasonal-high note), and the geotech's assumption on whether the quoted bearing value is dry or submerged condition.

### Detention basin design shows storage volume and outlet sizing but no emergency spillway sized independently for a storm larger than the design event
- **Usually means:** the design was optimized to the design storm (often 10-yr or 25-yr) and never checked against overtopping in a 100-yr or greater event — the most common cause of basin failure isn't undersized primary storage, it's no planned path for water that exceeds it.
- **First question:** "Where does water go when this basin overtops, and is that path on a drawing?"
- **Data to pull:** the 100-yr routing calc and the spillway/overflow drawing detail.

### Value-engineering request reduces pipe size, pond volume, or footing size to exactly the code or ordinance minimum, with no new supporting calculation
- **Usually means:** a cost-driven change is being justified by "it still technically meets code" rather than by new data — this removes whatever margin was absorbing construction tolerance, debris, or a conservative original assumption.
- **First question:** "What new data — not new preference — justifies removing this margin?"
- **Data to pull:** the original calc's stated margin, and any new boring, survey, or hydrology data submitted with the request.

### RFI log shows a field decision referenced only by a verbal instruction or a phone call, with no written follow-up
- **Usually means:** a design change happened in the field without documentation — invisible until a dispute or failure forces reconstruction of what was actually authorized.
- **First question:** "Where's the written RFI response for this — and if there isn't one, why did construction proceed?"
- **Data to pull:** the RFI log, the daily field report for that date, and any change order tied to the same item.

### Structural load takeoff used in the foundation calc doesn't match the latest structural drawing revision
- **Usually means:** the civil/foundation calc was run against an earlier structural issue and never updated when the structural engineer revised loads — a common cross-discipline version-control gap.
- **First question:** "What revision of the structural load takeoff is this calc built on, and is it the current one?"
- **Data to pull:** the structural drawing revision log and the date stamp on the load takeoff used in the foundation calc.

### Local code amendment (wind speed, flood elevation, seismic design category) not cited on the drawing cover sheet
- **Usually means:** the design defaulted to the national ASCE 7/IBC minimum without checking whether the jurisdiction amended it upward — amendments almost never relax a national minimum.
- **First question:** "What does this jurisdiction's adoption ordinance say, specifically, beyond the base IBC/ASCE 7 edition?"
- **Data to pull:** the jurisdiction's code adoption ordinance or amendment table, dated to the permit application date.
