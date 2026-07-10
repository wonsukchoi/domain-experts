# Vocabulary

Terms of art generalists misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

### Rating (stage-discharge rating curve)

- **Definition:** the fitted, site-specific relationship that translates a continuously measured stage (water-surface elevation) into a discharge value, developed from a scatter of individual discharge measurements over a range of stages.
- **In use:** "We're not re-measuring because we doubt the flow — we're checking whether today's point still falls on the current rating or whether the rating itself has moved."
- **Common misuse:** treating the rating as a fixed physical law rather than a fitted curve that decays in accuracy as the channel control changes; assuming a discharge value from a gage is "measured" when in fact only the stage is measured continuously — discharge is computed through the rating.

### Shift (rating shift / shift-adjusted rating)

- **Definition:** a temporary or permanent adjustment applied to the current rating to account for a documented change in the stage-discharge relationship, without discarding and refitting the whole curve.
- **In use:** "Apply a −10% shift effective 5/14, not a whole new rating — the control changed, but not enough yet to justify a full refit."
- **Common misuse:** applying a shift after a single flagged deviation instead of confirming a trend first, which chases measurement noise instead of a real control change.

### Control (hydraulic control)

- **Definition:** the physical feature — a riffle, weir, channel constriction, or engineered structure — that governs the stage-discharge relationship at a gage for a given range of flows.
- **In use:** "The control's a natural riffle, so expect the rating to move every time there's a debris jam or a scouring high flow — this isn't a permanent structure."
- **Common misuse:** assuming all gages have a stable engineered control; natural-control sites need far more frequent measurement to catch rating changes than a weir or flume site does.

### Discharge measurement quality rating (excellent/good/fair/poor)

- **Definition:** a standardized uncertainty band (±2% / ±5% / ±8% / >8%, per Sauer & Meyer 1992) assigned to an individual discharge measurement based on the conditions and method used, independent of whether it agrees with the rating.
- **In use:** "It's a fair measurement, not a good one — the stage was still rising during the middle verticals, so an 8% deviation from the rating doesn't tell us much on its own."
- **Common misuse:** treating every measurement as equally trustworthy and comparing its raw percent-deviation from the rating without asking what uncertainty the measurement itself carries.

### Index-velocity method

- **Definition:** a discharge-computation method for sites where a simple stage-discharge rating doesn't hold (tidal, backwater-affected, or variable-slope reaches) — a continuously recorded index velocity (from an ADVM) is related to the mean channel velocity via a separate velocity rating, then combined with a stage-area relationship.
- **In use:** "This reach backs up under high tide, so we're running index-velocity, not a stage rating — velocity and stage move independently here."
- **Common misuse:** applying a standard stage-discharge rating at a site with variable backwater or slope, which produces discharge errors a normal single-visit measurement won't catch because the rating itself is the wrong tool.

### Mid-section method

- **Definition:** the standard discharge-computation method that divides a cross-section into verticals, computes each vertical's discharge as width × depth × mean velocity, and sums across all verticals.
- **In use:** "Ten verticals, mid-section, total comes to 351 — check the notesheet if you want the panel-by-panel breakdown."
- **Common misuse:** assuming more verticals is always better without cost; the actual standard is that no single vertical should dominate the total (roughly 10%), which sets the minimum number needed for a given cross-section, not an arbitrary target count.

### Spin test

- **Definition:** a pre- and post-measurement check of a mechanical current meter's rotor, comparing observed spin time against the meter's rated/calibrated spin time to confirm it's functioning within tolerance.
- **In use:** "Post-test was 2% off — inside tolerance, so the measurement stands, but log the drift for the maintenance record."
- **Common misuse:** running only a pre-test and skipping the post-test, which removes the only way to know whether something happened to the meter mid-measurement.

### Holding time

- **Definition:** the maximum allowable elapsed time, per EPA method (40 CFR 136) or state-equivalent regulation, between sample collection and laboratory analysis, beyond which a result is qualified or invalidated.
- **In use:** "We're not going to make the 48-hour hold on nitrate from this site — ice it and log the actual elapsed time so the lab can qualify the result instead of rejecting it blind."
- **Common misuse:** treating holding time as a soft guideline rather than a hard analytical constraint; shipping a late sample without documentation, which converts a qualifiable result into an untraceable one.

### Isokinetic sampling

- **Definition:** a suspended-sediment sampling technique where the intake velocity at the sampler nozzle matches the ambient stream velocity, so the sample isn't biased toward over- or under-representing coarser sediment.
- **In use:** "Nozzle size has to match the transit rate and stream velocity for this reach, or the sediment sample skews fine — check the isokinetic transit-rate chart before starting."
- **Common misuse:** treating any depth-integrating sampler as automatically isokinetic regardless of transit rate or nozzle size; mismatched transit rate breaks the isokinetic condition even with the right equipment.

### Provisional data

- **Definition:** field-collected or field-computed values (stage, discharge, water-quality results) that have been entered into the record but not yet reviewed and approved by the responsible hydrologist, and therefore subject to revision.
- **In use:** "That discharge is provisional until review — don't cite it in the compliance report yet, the shift hasn't been confirmed."
- **Common misuse:** treating provisional data as equivalent to approved/published data for a downstream decision; provisional values exist precisely because they can still change.

### Datum (gage datum)

- **Definition:** the fixed, surveyed reference elevation from which stage is measured at a gage; distinct from the specific instrument (staff gage, pressure transducer) reading against it.
- **In use:** "The step in the record isn't a flow event — the sensor got reinstalled two inches high after maintenance, so it's a datum shift, not a hydrologic one."
- **Common misuse:** assuming a sudden step change in a stage record must reflect a real hydrologic event, rather than checking the maintenance log for a datum change first.
