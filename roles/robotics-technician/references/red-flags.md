# Red flags

Smell tests a robotics technician catches on a first pass over a fault log, a remastering result, a TCP-calibration report, a cycle-time complaint, or a post-repair safety verification.

### Robot resumes smooth motion after an encoder battery replacement with no mastering check performed

- **Usually means:** the battery swap also dropped the mastering data (a common failure mode if power is lost before the new battery is seated), and the servo loop closes fine on the wrong reference — the robot moves smoothly to positions offset from every taught point.
- **First question:** was the stored pulse count read and compared against the nameplate/last-logged reference immediately at power-up, or was "it moves fine" treated as sufficient?
- **Data to pull:** the controller's mastering log timestamp and pulse-count value from before and after the battery swap.

### Mastering alarm cleared by a controller restart with no fixture remastering performed

- **Usually means:** the alarm was suppressed, not resolved — a lost-mastering alarm (as opposed to a low-battery-only alarm) requires physical remastering; a restart that clears the alarm screen without a fixture procedure leaves the offset in place.
- **First question:** does the alarm code correspond to lost mastering data specifically, or a recoverable low-battery/comms warning, and which procedure does the OEM manual require for each?
- **Data to pull:** the exact alarm code and the OEM fault-code reference entry for it.

### TCP-calibration residuals pass tolerance but show a consistent same-direction offset across all touch points

- **Usually means:** a systematic error (mastering drift, a bent tool, or a mis-seated calibration fixture) rather than normal probing variation — a scattered pattern is noise, a directional pattern is a real offset that happens to sit inside the tolerance band today and may not tomorrow.
- **First question:** does the per-touch residual vector (not just its magnitude) point the same direction across all four/six touches?
- **Data to pull:** the controller's raw per-touch position data, not just the summary residual number.

### Cycle-time complaint addressed by speeding up the process/weld segment without a segment breakdown

- **Usually means:** the visible, "obviously slow-looking" segment (arc time, a motion move) got blamed and adjusted while the actual driver — often a wait/handshake state — was never measured.
- **First question:** has each segment been timed independently against its spec baseline and ranked by absolute-second delta, or was the fix aimed at the segment that looked slowest to the operator watching?
- **Data to pull:** the servo-trend or PLC I/O trace segment timestamps, spec baseline per segment.

### Uniform percentage cycle-time increase across every program segment

- **Usually means:** a global speed/feedrate override percentage was changed (intentionally or accidentally) rather than a single-segment fault — every segment scaling by roughly the same factor points to one override value, not several independent problems.
- **First question:** what is the program's or controller's active speed override percentage, and does it match the value used when the spec baseline was set?
- **Data to pull:** the current override % setting and the commissioning record's baseline override %.

### Lockout applied only to the main electrical disconnect on a cell with pneumatic, hydraulic, or elevated-axis energy present

- **Usually means:** the technician treated electrical isolation as isolating the whole cell, missing that pneumatic accumulators, hydraulic accumulators, and gravitational energy on an elevated/counterbalanced axis each hold energy independently of the electrical bus.
- **First question:** what energy sources does this specific cell's isolation diagram list, and has each been independently verified at zero (gauge reading, brake-set confirmation), not just the electrical one?
- **Data to pull:** the OEM/site LOTO isolation diagram for this cell and the per-source verification readings.

### Zero-energy verification skipped in favor of "the light is off / the display is dark"

- **Usually means:** a dark HMI or an unlit indicator lamp is being used as a proxy for a metered, verified zero-energy state — a failed indicator lamp or a capacitor bank still above the touch-safe voltage threshold looks identical to a truly de-energized cell from the outside.
- **First question:** was the DC bus actually metered, and was a cycle-start attempted with locks in place to confirm no response?
- **Data to pull:** the meter reading against the site's touch-safe voltage threshold, and the pendant/HMI log of the attempted cycle-start test.

### Post-repair return to auto mode without a stopping-performance re-check, after a repair touching speed, payload, braking, or guarding

- **Usually means:** the repair (hard-stop replacement, brake service, payload-carrying end-of-arm tooling change, safety-scanner reconfiguration) can shift measured stopping time/distance away from the certified value the protective separation distance was originally calculated against, and nothing alarms on that drift by itself.
- **First question:** does this repair touch anything in the chain the original ISO/TS 15066 or ISO 13849 stopping-performance figure depended on, and if so, has a field measurement been taken and compared against the certified data-sheet value?
- **Data to pull:** the stopping-distance/time measurement device's reading and the certified data-sheet value it's compared against.

### Measured stopping distance/time worse than certified spec, but cell returned to production without re-verifying separation distance

- **Usually means:** the drift was noticed but treated as a maintenance note rather than a safety-relevant finding — a stopping-performance figure worse than certified invalidates the separation distance calculated from it until re-verified or the underlying cause (brake wear, parameter change) is fixed.
- **First question:** is the measured delta within the test equipment's stated repeatability tolerance, or does it represent a real performance shift?
- **Data to pull:** the test device's stated repeatability spec, and a second measurement to confirm the first wasn't an outlier.

### Fault recurs within days of a component replacement, logged as an unrelated new fault

- **Usually means:** the replacement part or its installation is the actual cause (bad batch, incorrect torque on a connector, a cable pinched during reassembly), not an independent second failure — treating it as unrelated skips the highest-probability diagnosis.
- **First question:** does the new fault's signature match a plausible failure mode of the part just replaced or the work just performed?
- **Data to pull:** the work order for the original repair (parts, torque values, cable routing) against the new fault's alarm code and timing.

### PM interval extended or skipped based on "no faults reported" alone

- **Usually means:** absence of an alarm is not the same as absence of drift — mastering offset, TCP drift, and brake wear all progress without throwing a fault until they cross a threshold (a collision, a missed weld, a failed stopping-performance check), and a PM interval exists specifically to catch the drift before that threshold.
- **First question:** what does the PM check that a fault log alone would not catch (pulse-count drift, TCP residual trend, measured stopping distance)?
- **Data to pull:** the trend of the last 3-5 PM cycles' pulse-count, TCP-residual, and stopping-distance readings, not just the current single reading.
