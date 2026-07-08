# Red Flags

### Megger reading clears IEEE 43 floor (kV + 1 MΩ) but PI (10-min ÷ 1-min) < 2.0
- **Usually means:** Winding contamination (moisture or conductive dust) that will progress to failure, not a healthy winding — the absolute floor and the trend disagree, and the trend wins.
- **First question:** What was the 1-minute reading, and what's the 10-minute reading — has anyone actually computed the ratio, or just checked the floor?
- **Data to pull:** Megger test log (1-min and 10-min DC readings at 500 V), IEEE 43 minimum-IR table for this voltage class, prior PI history for this motor if any.

### Overall vibration velocity reads in ISO 10816/20816 Zone A or B
- **Usually means:** No broadband problem is being flagged, but a bearing-race or gear-mesh defect frequency can sit undetected inside a Zone A/B overall reading — zone tells severity, not fault location.
- **First question:** Has an FFT spectral read ever been pulled on this machine, or only the overall RMS velocity?
- **Data to pull:** Overall RMS velocity trend, machine-class Zone A/B/C/D boundary table, most recent FFT spectrum if one exists.

### PLC output fails to fire despite ladder logic that "reads correct" on screen
- **Usually means:** The containing routine isn't actually being called (missing/conditional JSR from main), or an upstream MCR block is de-energized — the printed logic is necessary but not sufficient evidence it's executing.
- **First question:** Is this routine confirmed scanning right now — has anyone gone online and watched the rung execute, not just read the offline listing?
- **Data to pull:** Online monitor view of the rung with live status, JSR call-tree from main routine, MCR block status, any active forces on the I/O in question.

### Forced I/O tag shows true but downstream logic still behaves as if false
- **Usually means:** The force is changing the physical output/input point only, not the processor's internal logic-bit state that downstream rungs actually read — a common source of "it's forced true but nothing happens downstream."
- **First question:** Is this a native force, or a manual toggle branch — and has the internal bit status (not the forced physical point) been checked directly?
- **Data to pull:** Force table / forced-I/O list for the controller, internal tag status vs. physical point status, rung history showing when the force was applied.

### Shaft alignment "passes" the ~0.5 mils/inch rule-of-thumb but the coupling keeps failing
- **Usually means:** The rule of thumb is a screening check, not the accept/reject number for this machine's actual RPM — the coupling needs the RPM-indexed tolerance table, which is tighter at higher speeds.
- **First question:** What RPM is this coupling actually running at, and what does the RPM-indexed table (not the generic rule of thumb) allow at that speed?
- **Data to pull:** Laser alignment report (angular and offset readings), RPM-indexed tolerance table for the coupling class, alignment history showing prior "passing" attempts.

### Cylinder reported "slow" with no distinction made between internal and external leakage
- **Usually means:** Two different fault paths look identical from the outside — internal (piston-seal) leakage needs a pressure-decay test to isolate; external leakage needs ultrasonic leak detection — guessing which one skips a diagnostic step and risks an unnecessary teardown.
- **First question:** Has a pressure-decay test been run, or is "slow" based on visual/feel observation only?
- **Data to pull:** Pressure-decay test result (psi drop over time), ultrasonic leak-detector scan if run, cylinder spec sheet (bore, rated seal life).

### Crimp accepted on visual inspection ("looks tight") without a pull-test number
- **Usually means:** A crimp can look fully seated and still fail well below the wire's rated tensile strength — visual inspection is not an acceptance criterion under IPC/WHMA-A-620.
- **First question:** What did the pull-tester read for this wire gauge, and does it clear the IPC/WHMA-A-620 minimum for that gauge/class?
- **Data to pull:** Pull-test log (force at failure, mm/min rate used), IPC/WHMA-A-620 class and wire-gauge minimum table, terminal/wire spec.

### Motor trips repeatedly under load but vibration reads clean
- **Usually means:** A developing bearing or rotor-bar fault can show up in motor current signature analysis 90–120 days before it raises broadband vibration into a measurable zone — clean vibration alone doesn't clear a fault in progress.
- **First question:** Has an MCSA capture been run, or is "vibration is clean" being treated as "the motor is fine"?
- **Data to pull:** MCSA sideband capture (f₁(1±2s) rotor-bar sidebands, BPFI/BPFO/BSF-modulated current), current vibration spectrum, trip log with timestamps and load at trip.

### Arc-flash PPE selected by habit ("it's just a control cabinet") rather than by category table or incident-energy analysis
- **Usually means:** Undocumented PPE selection is a compliance flag on its own, independent of whether the technician happened to guess correctly this time — CAT 1–4 map to specific ≥cal/cm² thresholds at 18 inches, not to panel type by feel.
- **First question:** What's the documented incident-energy analysis or NFPA 70E Table 130.7(C)(15)(a) category for this specific panel, and where's that on file?
- **Data to pull:** Arc-flash study/label for the enclosure, NFPA 70E PPE category table, LOTO procedure on file for this equipment.

### No prior IR/vibration baseline on file for a unit now showing a fault
- **Usually means:** Without a baseline, "3.2 MΩ" or "2.6 mm/s" can't be judged as a trend — only against the generic floor — masking a unit that was already degrading before this event.
- **First question:** Is there a prior reading on file for this exact unit, or only the generic IEEE 43 / ISO 10816 floor to compare against?
- **Data to pull:** CMMS equipment history for this asset ID, last PM date and readings taken, generic floor/zone table used as fallback if no baseline exists.

### Repair completed and machine returned to service without a same-method re-measurement
- **Usually means:** A "fixed" call that isn't re-tested the same way the fault was characterized (same test, same points) produces a before/after pair that isn't actually comparable — the fix may not have addressed the measured problem.
- **First question:** What's the re-test reading, taken with the same test and same measurement points as the original fault characterization?
- **Data to pull:** Original fault measurement (method, points, value), post-repair re-measurement (same method/points), CMMS closeout note documenting both.
