# Red flags

Smell tests a working test technician catches before a reading goes on a signed record. Each entry: what it usually means, the first question to ask, and the data to pull before accepting the number.

### Sample rate set at less than 5x the channel's expected highest frequency of interest

**Usually means:** the DAQ setup was copied from a prior channel's settings without re-deriving the bandwidth for this component, or the "highest frequency of interest" was never actually estimated before the session started.
**First question:** "What's the estimated highest frequency of interest for this channel, and where did that number come from?"
**Data to pull:** the DAQ configuration log (sample rate, anti-alias filter corner); the source of the bandwidth estimate (prior test, FEA modal result, or a guess); recomputed ratio of sample rate to estimated frequency.

### Anti-alias filter corner set at or above 1/4 of the sample rate

**Usually means:** the filter was left at a DAQ software default instead of being derived from the chosen sample rate, letting content above Nyquist fold back into the passband before it's even digitized.
**First question:** "What sample rate is this channel running at, and does the filter corner sit inside the 1/4-1/10 window below it?"
**Data to pull:** configured sample rate and filter corner frequency from the DAQ setup sheet; recomputed ratio; a look at the raw waveform for a stair-step or beat-frequency artifact consistent with aliasing.

### A structural or durability channel is running CFC 180 or higher with no test-plan justification

**Usually means:** the class was set to "capture everything" instead of matched to the load's actual frequency content, and a downstream peak or damage calculation is now reading through noise the channel should have filtered out.
**First question:** "What does the test plan or a comparable prior test on this component specify for this channel's CFC, and if nothing exists, why was this class chosen over CFC 60?"
**Data to pull:** the test plan's channel list with specified CFC per channel; a comparable prior test record for the same or similar component; the raw vs. filtered trace overlay for the channel in question.

### Shunt-calibration error exceeds 1% of predicted output on a pre-test check

**Usually means:** excitation voltage has drifted, a connector has degraded since the gauge was last verified, or the bridge itself has been damaged — most commonly from thermal cycling or a reseated connector between sessions.
**First question:** "When was this bridge last shunt-checked, and what changed physically since then — reseated connectors, temperature exposure, handling?"
**Data to pull:** predicted vs. measured shunt-cal output and computed error percentage; date and result of the last shunt-cal on this bridge; excitation voltage reading at the amplifier.

### A strain-gauge bridge is being used for a test session with no shunt-cal check logged that day

**Usually means:** the bridge was verified once at initial bonding and the technician is treating that as still valid, without accounting for the drift a week or more of thermal cycling and handling introduces.
**First question:** "Has a shunt-cal check been run today, or is the last one on record from initial bonding?"
**Data to pull:** date-stamped shunt-cal log for this bridge; number of days since the last check; any intervening thermal exposure or connector work.

### A torque wrench's calibration certificate is more than 12 months old, or the fastener's spec falls outside the wrench's last-verified 20/60/100% range

**Usually means:** the wrench is being used past ISO 6789's stated interval, or a reading is being extrapolated beyond the points it was actually checked at — both substitute an assumption for a verified measurement.
**First question:** "When was this wrench last calibrated, and does the applied torque fall within the 20-100% range that was actually checked?"
**Data to pull:** calibration certificate date and cycle count against the 12-month/5,000-cycle interval; the certificate's tested percentages of rated capacity; the actual spec torque as a percentage of the wrench's rated capacity.

### A Class I mechanical wrench is specified for a safety-critical fastener (wheel hub, suspension mount, cylinder head)

**Usually means:** tool selection defaulted to whatever was on the cart instead of matching tolerance class to fastener consequence — Class I's ±4% band is wider than a safety-critical joint typically warrants.
**First question:** "Is this fastener safety-critical, and if so, why is a Class I wrench being used instead of Class II?"
**Data to pull:** the fastener's classification on the build record or engineering spec; wrench class and its ISO 6789 tolerance; any documented exception approving Class I for this application.

### A dyno-reported horsepower figure is being compared against a prior number with no correction-standard check

**Usually means:** one figure is on SAE J1349 and the other on the older J607 basis, and the roughly 4% gap between them is being read as a real engine difference instead of a units mismatch.
**First question:** "Are both numbers corrected to the same standard — J1349 or J607 — or is that being assumed?"
**Data to pull:** the correction standard stated on each dyno report; ambient conditions at each run (temperature, pressure) used in the correction; recomputed figures on a common basis if they differ.

### A Miner's-rule damage fraction or predicted remaining life is reported as a single number with no error band

**Usually means:** the extrapolation from cumulative damage to a point life estimate was reported at face value, hiding the method's documented 2.7-31% correlation error against actual fatigue life.
**First question:** "Is this point estimate bracketed by the documented rainflow/Miner's correlation error band, or is it being presented as exact?"
**Data to pull:** the cycle-bin table and cumulative damage fraction D; the S-N curve reference used; the correlation study or standard cited for the error band applied (or the absence of one).

### A rainflow/Miner's damage calculation used only one S-N curve reference with no cross-check

**Usually means:** the first S-N curve found (a handbook value, a similar-but-not-identical material) was used without checking it against a second reference, leaving the damage fraction more sensitive to curve selection than the report shows.
**First question:** "What S-N curve was used, and has the damage fraction been checked against a second reference curve for the same material and surface condition?"
**Data to pull:** the S-N curve source and its material/surface/loading conditions versus the actual component; a second reference curve and the resulting damage fraction for comparison.

### A multi-fluid thermal-limit test (coolant, transmission, hydraulic) is being monitored as separate single-channel checks

**Usually means:** the test procedure was executed as a sequence of individual limit checks instead of one simultaneous multi-channel watch, creating a window where a channel that isn't currently being observed can trip its limit unnoticed.
**First question:** "Were all thermal-limited channels displayed and watched simultaneously for the full run, or checked one at a time?"
**Data to pull:** the DAQ display/log configuration showing whether all limited channels were captured on the same timebase; timestamp of any limit exceedance against which channel was actively being watched at that moment.

### A Type K thermocouple reading is being held to a tolerance tighter than ±2.2°C without confirming SLE grade

**Usually means:** the required accuracy for this measurement (e.g., EGT near a control limit) needs Special Limits of Error grade, but a standard-grade thermocouple was installed by default without checking the spec against the standard ±2.2°C (or ±0.75%) tolerance.
**First question:** "What accuracy does this measurement need, and is the installed thermocouple standard-grade or SLE-grade?"
**Data to pull:** the thermocouple's grade per its calibration/purchase record; the required accuracy from the test spec; the reading's proximity to a control limit where the tolerance difference would matter.

### An out-of-tolerance or ambiguous result was closed out on the test record without an engineer-of-record disposition

**Usually means:** the technician made a judgment call on a result that falls outside their authority — accepting, rejecting, or re-running without documented sign-off from the engineer who owns the design or test target.
**First question:** "Who disposed this out-of-tolerance result, and where's the documented concurrence from the engineer of record?"
**Data to pull:** the test record's disposition field and signature/approval trail; the original engineer's target and stated tolerance; any email or change record showing the engineer was actually consulted.
