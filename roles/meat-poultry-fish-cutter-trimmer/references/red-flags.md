# Red flags

### Batch yield falling more than the spec's stated tolerance below target
- **Usually means:** blade sharpness overdue for service, or the incoming lot's fat/bone content running above typical for that supplier.
- **First question:** when was this blade last sharpened, and does the current incoming lot's receiving-QC data show elevated fat/bone content?
- **Data to pull:** blade sharpening log, receiving QC record for the current supplier lot, historical yield data for this cut/supplier combination.

### Product surface temperature reading at or above a CCP's upper limit
- **Usually means:** a chiller or refrigeration fault, or cumulative dwell time across stations has run longer than normal.
- **First question:** what is the cumulative time this product has spent above the limit across all prior stations, not just this reading?
- **Data to pull:** the HACCP plan's cumulative exposure allowance, station-by-station temperature/time log for this batch.

### Metal detector or X-ray reject on the line
- **Usually means:** equipment wear introducing metal fragments (blade nicks, worn conveyor parts) or a foreign object present in incoming raw material.
- **First question:** has the root cause been identified, or was the rejected piece simply removed and the line restarted?
- **Data to pull:** reject log with piece location/timestamp, equipment maintenance log for blades and conveyor components upstream of the detector.

### A CCP monitoring value out of range with no logged corrective action
- **Usually means:** the deviation was noticed but resolved informally rather than through the HACCP plan's documented procedure.
- **First question:** does the corrective-action log show an entry matching this specific out-of-range reading's timestamp?
- **Data to pull:** CCP monitoring log, corrective-action log, HACCP plan's specified procedure for this CCP.

### Allergen-designated or raw/ready-to-eat-segregated equipment used for a different product
- **Usually means:** a changeover-time pressure led to a "just this once" exception to the segregation protocol.
- **First question:** was this equipment cleaned and verified per the segregation protocol before or after this use?
- **Data to pull:** equipment usage log, cleaning/changeover verification record, allergen/segregation protocol for this equipment.

### Repeated rejects at the same line position across multiple shifts
- **Usually means:** a persistent equipment issue (a specific blade station, a specific conveyor section) rather than a one-off material issue.
- **First question:** do the rejects across shifts share the same line position or equipment, or are they scattered?
- **Data to pull:** reject log by line position across multiple shifts, equipment maintenance history for that specific position.

### A supplier lot showing a pattern of elevated fat/bone content across multiple deliveries
- **Usually means:** a shift in the supplier's own processing or animal sourcing, not a one-time anomaly.
- **First question:** does receiving QC data show this trend across the last several deliveries from this supplier, or is it isolated to today's lot?
- **Data to pull:** receiving QC records for this supplier over recent deliveries, any supplier communication on sourcing changes.

### Blade or knife requiring noticeably more force than normal to complete a cut
- **Usually means:** the blade is overdue for sharpening or has a nick/defect, both an injury risk and a yield/quality risk.
- **First question:** when was this specific blade last sharpened or inspected?
- **Data to pull:** blade sharpening/inspection log, time elapsed since last service against the schedule.

### A yield or quality deviation logged without an explanation or root cause noted
- **Usually means:** the deviation was recorded procedurally but not actually investigated.
- **First question:** does the log entry identify a specific, checkable cause, or just the deviation itself?
- **Data to pull:** the deviation log entry, any supporting data (blade log, receiving QC, temperature log) that should accompany it.

### Product held past its logged corrective-action resolution without a documented release decision
- **Usually means:** the corrective action was completed but the release/continue-hold decision wasn't formally recorded.
- **First question:** does the record show who made the release decision and when, referencing the specific corrective action completed?
- **Data to pull:** corrective-action completion timestamp, release/hold decision record.
