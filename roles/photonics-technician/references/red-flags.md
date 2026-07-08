# Red Flags — Photonics Technician

### End-face defect measured but not checked against IEC 61300-3-35 zone diameter
- **Usually means:** the tech eyeballed the fiber scope image as "clean" or "minor" instead of measuring the defect against the applicable zone's numeric threshold; second most likely, the analysis software's auto-pass/fail overlay was dismissed without reading the actual µm figure.
- **First question:** what zone is the defect in, and what did it measure in µm against that zone's threshold?
- **Data to pull:** the fiber-scope image with zone overlay and the IEC 61300-3-35 zone table for the connector's polish type.

### OTDR trace flat for >12 m immediately after a reflective event ≥-30 dB
- **Usually means:** the flat stretch is an attenuation dead zone masking a real splice or connector loss, not confirmation the segment is fault-free; second most likely, the launch cord is too short to push the reference plane past the zone.
- **First question:** was this section re-measured with a launch cord long enough to clear the dead zone, or independently confirmed by power-meter cutback?
- **Data to pull:** the OTDR trace with reflectance value at the preceding event and the launch-cord length used.

### Mechanical splice loss measured ≥0.25 dB on a budget line sized for fusion-grade loss
- **Usually means:** a mechanical splice was substituted for a fusion splice without re-checking the loss budget, consuming most of the segment's margin in one joint; second most likely, poor fiber cleave or misalignment in the mechanical splice itself.
- **First question:** was this splice authorized on the traveler as mechanical, and does the total budget still clear with this measured value?
- **Data to pull:** the traveler's authorized splice type and loss ceiling, and the bidirectional OTDR or power-meter splice-loss reading.

### Optoelectronic die or module handled without a verified-live ESD station
- **Usually means:** the wrist strap or grounded mat wasn't checked before handling, or the part was assumed rugged enough to handle bare because it's packaged; second most likely, the ESD station's last verification/calibration lapsed.
- **First question:** when was this ESD station last verified against ANSI/ESD S20.20, and was the wrist strap tested at the start of this session?
- **Data to pull:** the ESD station verification log and the part's datasheet HBM/CDM susceptibility rating.

### Helium leak-test result recorded as "no leak detected" with no threshold comparison noted
- **Usually means:** the result reflects the mass spectrometer's detection floor, not a genuine pass against the package's required leak rate; second most likely, the technician didn't check whether Internal Gas Analysis sampling was required as a fallback.
- **First question:** does the recorded leak rate sit below the spec's required threshold, or below the instrument's stated sensitivity floor?
- **Data to pull:** the leak detector's calibration/sensitivity spec and the package's GR-468-CORE required leak-rate threshold.

### L-I-V sweep threshold current shifted >10% from the datasheet or prior burn-in baseline
- **Usually means:** early degradation or an infant-mortality failure mode the burn-in is meant to screen for; second most likely, a test-station calibration drift or a temperature-control error during the sweep.
- **First question:** does this shift track across repeated sweeps, or was it a single reading — and has the test station been calibrated since the last known-good baseline?
- **Data to pull:** the L-I-V sweep data (threshold current, slope efficiency) plotted against the datasheet spec and any prior burn-in baseline for this part.

### Return loss measured below -50 dB on a link with an inline amplifier or return-loss-sensitive component
- **Usually means:** a UPC connector was used where the design called for APC, or the connector end-face has contamination/damage reflecting light back up the link; second most likely, a mismatched or degraded mating connector on the other side.
- **First question:** does the traveler specify APC or UPC for this link, and does the installed connector's polish match what was measured?
- **Data to pull:** the traveler's specified connector polish and the return-loss measurement from the power meter or OTDR.

### Assembly step run in a cleanroom class not matched to the traveler's stated requirement
- **Usually means:** the step defaulted to whatever class bay was open rather than the traveler's specified class, either over- or under-protecting the step; second most likely, the traveler's class requirement was never checked before starting.
- **First question:** what cleanroom class does the traveler specify for this step, and does the bay used match it?
- **Data to pull:** the traveler's cleanroom class requirement and the particle-count log for the bay used during the step.

### Traveler closed out on loss-budget numbers with an open or failed inspection item elsewhere on the record
- **Usually means:** the technician treated a passing loss budget as sufficient to ship without confirming every required inspection (end-face, ESD, leak test) also passed; second most likely, a rework was completed but the re-inspection step was skipped before sign-off.
- **First question:** are all required inspection line items on this traveler marked pass, or is one still open/failed while the loss number looks clean?
- **Data to pull:** the full traveler record with every inspection line item and its pass/fail status.

### Equipment calibration date on the traveler older than the instrument's stated calibration interval
- **Usually means:** a measurement (OTDR, power meter, fiber scope, L-I-V station) was taken on out-of-cal equipment, putting the recorded value's accuracy in question; second most likely, the calibration sticker was checked but not actually logged on the traveler.
- **First question:** what is this instrument's stated calibration interval, and how far past due is the date on the traveler?
- **Data to pull:** the instrument's calibration certificate/interval and the traveler's logged calibration date for the equipment used.

### Burn-in completed for fewer hours than the stated screening duration
- **Usually means:** the burn-in was cut short to meet a shipment deadline, undermining the infant-mortality screen it exists to perform; second most likely, an interruption (power loss, chamber fault) wasn't backfilled with additional hours.
- **First question:** how many hours did this part actually accumulate at the specified temperature/current, against the stated screening duration?
- **Data to pull:** the burn-in fixture log (hours, temperature, current) for this part's lot.

### Zone A defect passes but Zone B or C on the same end-face is not separately reported
- **Usually means:** the technician reported only the most visually prominent defect (often core) and didn't check every zone independently, missing that a single failing zone fails the whole inspection regardless of other zones being clean; second most likely, the fiber-scope software's summary view was trusted without opening each zone's detail.
- **First question:** was every zone (A through the standard's applicable cutoff) measured and reported individually, not just the one that looked worst?
- **Data to pull:** the per-zone measurement table from the fiber-scope inspection software for this connector.
