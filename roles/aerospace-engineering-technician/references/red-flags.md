# Red flags

Smell tests this role catches on a first pass over a torque/preload record, a strain-gauge test result, an NDI report, an FAI package, or a calibration log.

### Torque wrench calibration certificate shows uncertainty >4% of the value being verified on a flight-critical joint

- **Usually means:** the test uncertainty ratio (TUR) against the drawing's torque tolerance band is below the 4:1 (or site-specified 10:1) threshold, so the measurement can't actually distinguish a good joint from a marginal one.
- **First question:** what is this wrench's current calibration uncertainty, and what is the TUR against the specific torque tolerance band it's verifying?
- **Data to pull:** the wrench's current calibration certificate, the drawing's torque tolerance callout.

### Fastener finish on the part doesn't match the K-factor assumption used to compute required torque

- **Usually means:** the joint analysis assumed dry (or wet) K, but the as-received hardware is lubricated (or bare) — the same torque value now delivers a different preload than the analysis assumed.
- **First question:** what finish/lube condition does the fastener actually have, and does the torque callout's basis document state which K it assumed?
- **Data to pull:** the fastener's finish/plating spec, the work order's lubrication instruction, the joint analysis's stated K-factor.

### Strain gauge zero reading drifts more than roughly 50 µε between bridge balance and load application with no load applied

- **Usually means:** thermal drift (gauge or lead-wire temperature not stabilized), a bonding defect, or a bridge-completion wiring issue — not yet a structural signal.
- **First question:** has the gauge and DAQ channel been allowed to thermally stabilize, and does a shunt-calibration check reproduce the expected resistance change?
- **Data to pull:** the pre-load zero-strain time history, the shunt-cal verification record.

### Single uniaxial gauge reporting a stress-critical result where the local stress state is known to be biaxial (near a hole, fillet, or fitting radius)

- **Usually means:** the gauge is bonded along one axis and can't recover the principal stress direction or magnitude — the reported number is strain along an arbitrary axis, not the governing stress.
- **First question:** is this location one where a rosette was specified in the test plan, and if a uniaxial gauge was substituted, was the biaxial correction (or a stated conservative assumption) applied before reporting stress?
- **Data to pull:** the test plan's gauge-type callout for this location, the rosette reduction (if available) or the stated single-axis limitation.

### Measured test stress or strain diverges from the engineering-predicted (FEA/hand-calc) value by more than roughly 15%

- **Usually means:** either a real structural discrepancy (unmodeled load path, unexpected stiffness) or an instrumentation/setup error (gauge misalignment, wrong gauge factor entered, load application not matching the analysis boundary condition).
- **First question:** has this specific gauge location and load case been seen before, and does the divergence fall inside or outside prior test-to-analysis correlation history for this structure?
- **Data to pull:** the stress report's predicted value at this gauge location, the DAQ's applied gauge factor and excitation setting, the load-application record.

### NDI method used doesn't match the drawing or process spec's called-out method

- **Usually means:** the available rig or the technician's default method was used instead of the specified one, and the substitute method may not be sensitive to the specific defect type the print requires screening for.
- **First question:** what method does the drawing or process spec actually call out, and if a different one was run, is there a documented equivalence justification?
- **Data to pull:** the drawing's NDI callout or the applicable process spec, the inspection record's method-used field.

### Eddy current or ultrasonic indication length/amplitude sits within roughly 10% of the accept/reject threshold

- **Usually means:** a borderline call where probe lift-off, coupling variation, or reference-standard calibration drift could move the reading across the line in either direction.
- **First question:** was the calibration/reference standard re-verified immediately before this reading, and does a repeat scan reproduce the same indication amplitude?
- **Data to pull:** the reference-standard calibration record, the repeat-scan data.

### AS9102 first article inspection record has fewer ballooned characteristics than the drawing's total dimension/GD&T/note count

- **Usually means:** the FAI was scoped to a subset the technician judged likely to fail, not the full drawing — an incomplete FAI can pass while a real out-of-tolerance characteristic goes unmeasured.
- **First question:** does every dimension, GD&T callout, and material/finish note on the drawing have a corresponding balloon number and measured value on the FAI record?
- **Data to pull:** the ballooned drawing, the FAI characteristic-accountability record (AS9102 Form 3).

### Tool, gauge, or DAQ channel calibration due-date has passed and a measurement was still recorded on it

- **Usually means:** the measurement's uncertainty is no longer traceable — the tool may still read correctly, but there's no current basis to state its accuracy.
- **First question:** what is the tool's calibration due-date, and was any measurement recorded on it after that date?
- **Data to pull:** the tool's calibration log/asset record, the timestamp of the measurement in question.

### Wind-tunnel test-point Reynolds number is compared directly against a flight-condition prediction without a stated Re-mismatch caveat

- **Usually means:** boundary-layer transition and separation behavior can differ materially between test and flight Reynolds numbers, and a direct CL/CD comparison without acknowledging the mismatch overstates the test's predictive validity.
- **First question:** what is the ratio of flight Re to test Re for this data point, and does the test report state whether the difference is inside or outside the tunnel's established correlation range?
- **Data to pull:** the test-point Re calculation, the tunnel's Re-correlation history for this configuration class.
