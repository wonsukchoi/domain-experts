# Occupational Health and Safety Technician — Red Flags

### Post-calibration flow drift over 10% versus pre-cal
- **Usually means:** a pump mechanical fault, a partially blocked cyclone/filter, or a battery voltage sag late in a long shift.
- **First question:** did the pump pass its own periodic maintenance/service check recently, and was the battery fresh at deployment?
- **Data to pull:** pump maintenance log, battery-charge log, prior deployment drift history for the same unit.

### Field blank mass at or above 10% of the sample mass
- **Usually means:** media contamination during handling, transport, or storage rather than a genuinely low workplace concentration.
- **First question:** were the blanks stored and transported identically to the samples, or handled differently (e.g., left in a hot vehicle, opened early)?
- **Data to pull:** blank handling log, storage temperature record if available, media lot number cross-checked against other batches using the same lot.

### Sample duration under ~70% of the shift it's meant to represent
- **Usually means:** an early pump failure, a worker removing the sampler, or a technician cutting the deployment short without disclosing why.
- **First question:** what time did the sample actually start and stop, and is there a field note explaining the gap?
- **Data to pull:** pump on/off timestamps, field log, comparison against the planned shift schedule.

### A direct-reading instrument result used as the sole basis for a compliance decision
- **Usually means:** someone substituted a fast screening reading for the integrated method the standard actually requires, usually under time pressure.
- **First question:** is this instrument NIOSH- or method-validated for this specific analyte, or is it a general-purpose screening tool?
- **Data to pull:** instrument validation/certification for the analyte in question, and whether a confirmatory integrated sample was ever scheduled.

### Chain-of-custody form missing a signature, timestamp, or custody-transfer step
- **Usually means:** a handoff happened informally (handed to a courier without logging it, left on a desk overnight) rather than a deliberate custody break.
- **First question:** who had physical possession of the media during the unlogged gap, and can they confirm it wasn't opened or altered?
- **Data to pull:** the complete COC form, courier tracking record if shipped, lab intake log timestamp.

### Quantitative fit-test fit factor barely above the pass threshold (under ~20% headroom)
- **Usually means:** a seal that works today under ideal conditions but is one bad shave, one mask-model change, or one sweaty exercise away from failing.
- **First question:** was a refit or alternate mask model tried before accepting the marginal pass?
- **Data to pull:** individual exercise fit factors (not just the overall), prior fit-test history for the same employee.

### Calibration standard itself outside its own certification interval
- **Usually means:** the calibration equipment's own recertification schedule slipped, making every sample calibrated against it suspect regardless of how clean the drift numbers look.
- **First question:** when was this calibrator (Gilibrator, acoustic calibrator, gas standard) last certified against a traceable reference, and is that date current?
- **Data to pull:** calibrator's own certification record, list of every sample calibrated against it since the last valid cert.

### Sampling media deployed past its manufacturer shelf life or outside its storage temperature range
- **Usually means:** sorbent tube breakthrough capacity or filter tare stability has degraded, introducing bias that won't show up as an obvious lab error.
- **First question:** what's the lot's expiration date and documented storage condition, and does it match what's on the media package?
- **Data to pull:** media lot number, manufacturer shelf-life spec, storage log.

### A logged process or ventilation deviation during sampling that isn't mentioned in the data report
- **Usually means:** the deviation was noted in a field notebook but never made it into the formal package routed to the specialist.
- **First question:** does the raw field log for this sample mention anything the typed report omits?
- **Data to pull:** original field notes/logbook page, cross-checked line-by-line against the submitted data package.

### Same pump showing repeated near-threshold drift (7-9%) across multiple deployments
- **Usually means:** the unit is developing a mechanical issue (worn diaphragm, weakening motor) that hasn't yet crossed the void threshold on any single sample but is trending there.
- **First question:** what does this pump's drift history look like over its last 10 deployments?
- **Data to pull:** per-unit drift log across all recent deployments, service/maintenance history.

### A below-MDC lab result reported and used as a hard "zero exposure" finding
- **Usually means:** the report rounded a "less than the detection floor" result down to zero, overstating confidence that no exposure occurred.
- **First question:** what was the calculated MDC for this specific sample volume, and is it being disclosed alongside the result?
- **Data to pull:** lab LOD for the method, sample volume, calculated MDC.
