# Red flags

Smell tests a technician or a reviewer catches on a first pass over a chain of custody, field log, or QC dataset.

### Cooler temperature blank reads above ~6°C at lab receipt with no exception noted

- **Usually means:** ice melted or was insufficient during transport, or the cooler sat too long before pickup — the samples inside may have degraded outside their intended preservation state even if the holding-time clock hasn't technically expired.
- **First question:** how long between collection and icing, and is there a documented reason (e.g., collected <2 hours before pickup, actively cooling) that would still support the data as compliant?
- **Data to pull:** the field log's collection and pickup timestamps, and the cooler receipt log's temperature-blank reading.

### Chain of custody shows a date but not a time for a holding-time-sensitive analyte

- **Usually means:** the technician didn't record collection time precisely enough to verify a 24- or 48-hour holding time was met — the lab can't determine if BOD5 setup at "day 2" is within or past the 48-hour window without knowing the hour of collection.
- **First question:** does the field logbook (not just the COC) have a precise collection time that can reconcile the gap?
- **Data to pull:** the original field logbook or electronic data sheet, cross-checked against the COC's date-only entry.

### Field meter's post-use calibration check is missing from the log

- **Usually means:** only a pre-use calibration was performed, so there's no evidence the meter held its calibration through the sampling run — data collected with this meter has an unquantified drift risk.
- **First question:** was a post-use check performed and simply not logged, or genuinely skipped, and if skipped, is there any other meter cross-check (duplicate reading with a second instrument) that can substitute?
- **Data to pull:** the calibration log for that meter and date, and the field log's equipment list for a second instrument used that day.

### Composite sampler's totalizer or pump fault alarm triggered mid-run with no notation

- **Usually means:** the compositing method was interrupted or degraded (missed aliquots, pump stall) for part of the event, which can silently convert a flow-proportional composite into a partial or biased one.
- **First question:** what portion of the run (by time or by expected flow volume) was affected by the fault, and was a corrective pacing switch documented?
- **Data to pull:** the autosampler's event/fault log and the field log's entries for the fault window.

### VOC vial has visible headspace or bubbles

- **Usually means:** the container wasn't filled to zero headspace at collection, or a bubble formed during transport — volatile loss through the headspace can bias VOC results low, and some labs will reject the vial outright.
- **First question:** was the vial re-filled and re-collected on site, or is this the only vial available for that location and time?
- **Data to pull:** the field log's container-fill notation and, if available, a photo or lab receiving note confirming headspace presence.

### Field duplicate RPD exceeds the QAPP control limit but the primary result is reported without a qualifier

- **Usually means:** the duplicate check was run and the number calculated, but the out-of-control result wasn't carried through to the reported data as a precision flag — a downstream user of the data has no way to know the result's reliability is in question.
- **First question:** what is this project's QAPP-stated RPD control limit, and does this pair's calculated RPD exceed it?
- **Data to pull:** the primary and duplicate raw results and the QAPP's data-quality-objectives table.

### Metals sample container shows the wrong preservative (or none) noted on the COC

- **Usually means:** either the wrong preservative was added in the field, or it was added but not recorded — both cases require the lab to determine whether the sample can still be salvaged (some labs can add preservative on receipt if within a short window) or must be rejected.
- **First question:** was the correct acid preservative (typically HNO3 to pH<2 for metals) added at collection, and if not documented, can the technician confirm from memory or field kit inventory what was actually used?
- **Data to pull:** the field preservation log and the lab's sample-receiving notes on pH-check-on-receipt (labs commonly verify preservation pH at login).

### Stack test run's isokinetic ratio falls outside 90-110% but the run wasn't flagged for repeat

- **Usually means:** the %I calculation was done after the fact (as it must be) but the result wasn't checked against the EPA Method 5 validity criterion before the data was reported as a valid run.
- **First question:** what was the calculated %I for this run, and does the field data sheet show it was checked against the 90-110% criterion before the crew left the site?
- **Data to pull:** the Method 5 field data sheet's post-run isokinetic calculation and the test report's stated run validity determination.

### Trip blank missing from a cooler containing VOC samples

- **Usually means:** the lab-prepared trip blank wasn't included with the cooler, or was used/opened in the field — without it, there's no way to distinguish transport/storage contamination from a genuine field detect in the VOC results.
- **First question:** was a trip blank included in this shipment, and if not, is this a one-time oversight or a systemic gap in the sampling program's blank protocol?
- **Data to pull:** the COC's listed sample IDs (a trip blank should appear as its own line item) and the lab's cooler-receipt checklist.

### Grab sample location doesn't match the permit-specified monitoring point

- **Usually means:** the sample was collected somewhere more convenient (upstream of a mixing zone, at an access hatch other than the designated one) rather than at the exact point the permit or method specifies — the result may not represent what the permit actually regulates.
- **First question:** does the field log's GPS coordinate or location description match the permit's designated outfall/monitoring point exactly?
- **Data to pull:** the permit's monitoring-point description or diagram and the field log's recorded location.

### Calibration buffer or standard solution is past its expiration or has been open longer than the manufacturer's in-service shelf life

- **Usually means:** an aged or contaminated standard can calibrate a meter to a value that no longer matches its labeled concentration, producing a calibration that "passes" against a wrong reference.
- **First question:** what is the expiration date and open-container shelf life printed on the standard's lot, and does today's date fall within both?
- **Data to pull:** the standard's certificate of analysis / lot documentation and the field kit's inventory log showing when the container was opened.
