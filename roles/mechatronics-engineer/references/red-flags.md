# Red Flags

### Positioning error settles to a value close to measured gear/belt backlash, and flips sign with direction of approach
- **Usually means:** motor-side (upstream) sensing with no reversal-dither or pre-load compensation — the loop is faithfully holding the motor shaft on target while the load sits anywhere within the backlash band.
- **First question:** is the encoder or resolver mounted on the motor shaft or on the load, and is there a compensation move on direction reversal?
- **Data to pull:** mechanism backlash measurement (mm or degrees), sensor location in the kinematic chain, and a position-error log tagged by direction of last motion.

### Reflected load-to-rotor inertia ratio above 10:1 on a geared or belted axis
- **Usually means:** the axis will be difficult or impossible to tune to target bandwidth without excessive gain reduction, and will re-excite compliance resonance as damping drops in the field.
- **First question:** was the gear ratio chosen for torque/speed matching alone, or was reflected inertia checked against the servo's stable range?
- **Data to pull:** motor rotor inertia, load inertia, gear ratio, and the vendor's stable inertia-ratio range for the selected drive/motor combination.

### Structural resonance frequency less than 3x the velocity-loop bandwidth (or less than 6x the position-loop bandwidth)
- **Usually means:** the loop is tuned close enough to the mechanical resonance that gain margin will erode as bearings wear or seals stiffen, producing field instability that didn't appear at commissioning.
- **First question:** what is the measured (not modeled) first structural resonance from a Bode sweep, and what bandwidth was the loop actually tuned to?
- **Data to pull:** frequency-response (Bode) plot from the servo autotuner, commissioning-time bandwidth setting, and any field reports of audible buzz or hunting.

### Intermittent fault clears after a firmware reflash on more than one unit from the same build
- **Usually means:** genuine firmware/calibration defect (state corruption, stale calibration table) rather than a hardware or wiring problem — but only if the pattern repeats across builds; a single-unit fix is weaker evidence.
- **First question:** does the fault recur after reflash on the same unit, and does it appear on units from a different manufacturing lot or supplier batch?
- **Data to pull:** field-return log cross-referencing serial number, build/lot date, firmware version at failure, and post-reflash recurrence rate.

### EMC/noise complaint after a cable or connector redesign, with no change to loop area or shield termination
- **Usually means:** the redesign changed conductor routing or loop area (even without changing cable spec), or a shield was pigtailed instead of terminated 360 degrees at one end.
- **First question:** was the shield terminated at both ends (ground loop) or pigtailed into a single lead, and did the new routing increase the loop area between signal and return?
- **Data to pull:** cable routing diagram before/after the redesign, shield termination photos or drawings, and an oscilloscope capture of the induced noise waveform correlated to a known switching event (e.g., motor commutation).

### Bypass capacitor present on the schematic but supply rail still shows switching-frequency ripple at the IC pin
- **Usually means:** the 0.1 uF ceramic cap is placed too far from the IC's power pin (trace inductance defeats it), or the bulk capacitor (10s-100s uF) is missing or undersized for the transient current.
- **First question:** what is the physical trace length from the bypass cap to the IC power pin, and is there a separate bulk cap on the same rail?
- **Data to pull:** PCB layout showing cap placement and trace length, and an oscilloscope measurement of rail ripple at the IC pin during a load transient.

### Qualification test report shows pass/fail results with no traceability to a requirement ID
- **Usually means:** the V-model's verification leg was skipped or done informally — measured results were never tied back to the RFLP decomposition, so a marginal pass can hide a requirement that was quietly loosened.
- **First question:** can every measured result in the report be traced to a specific requirement ID in the RFLP documents?
- **Data to pull:** the RFLP requirement-to-verification traceability matrix and the raw qualification test data (not just the pass/fail summary table).

### A single mechanical or electrical subsystem redesign lands late in the program with no cross-domain sign-off
- **Usually means:** disciplines were run sequentially instead of concurrently, and the late change (e.g., a gear ratio bump for torque margin) may have silently invalidated an electrical/control assumption (sensor resolution, achievable bandwidth) made earlier.
- **First question:** which other domain's design assumptions (sensor resolution, drive current, control bandwidth) depend on the parameter that just changed?
- **Data to pull:** the cross-domain dependency list from concept design and the change-request record showing who reviewed the late change.

### Motor current or torque saturating during normal operation, not just at startup or fault
- **Usually means:** either the reflected inertia is too high for the selected motor/drive (undersized for the load), or mechanical friction/binding is higher than modeled and is being masked by the controller commanding more torque to compensate.
- **First question:** does current saturate during steady-state motion or only during acceleration, and does manually back-driving the mechanism (motor de-energized) reveal excess friction?
- **Data to pull:** motor current/torque log time-aligned with the motion profile, and a manual back-drive torque measurement at the load.

### Backlash-compensation value has not been recalibrated since initial qualification, and the unit has passed 500k duty cycles (or 6 months in service)
- **Usually means:** gear wear has increased actual backlash beyond the calibrated compensation value, so the dither move under- or over-travels and positioning error creeps back in gradually rather than failing sharply.
- **First question:** when was backlash last measured directly (not inferred from position error), and how many duty cycles or operating hours has the unit accumulated since?
- **Data to pull:** the maintenance/PM log showing last recalibration date and duty-cycle count, plus a fresh direct backlash measurement for comparison against the compensation value on file.
