# Vocabulary

Terms generalists conflate or misuse. Each: definition, how a practitioner actually uses it, and the common misuse.

### Nyquist rate vs. practical sample rate
The Nyquist theorem's 2x-the-highest-frequency-of-interest is the mathematical minimum to avoid aliasing; it is not the rate a technician actually samples at.

**In use:** "Highest expected content is 50 Hz, so we're sampling at 500 Hz — 10x, not the bare 2x minimum — to preserve waveform shape, not just avoid aliasing."

**Common misuse:** citing "Nyquist says 2x" as if hitting exactly that rate were good practice, when a signal sampled right at 2x aliases into a clean-looking but wrong waveform the moment the true frequency drifts even slightly above the estimate.

### CFC (Channel Frequency Class)
An SAE J211-1 designation (CFC 60/180/600/1000) specifying a phaseless 4-pole digital low-pass filter corner frequency (corner ≈ CFC ÷ 0.6) applied to a data channel — it is a filter spec, not a sample-rate spec.

**In use:** "This is a durability load channel, so it gets CFC 60 with a 100 Hz corner — not CFC 600, which is for a crash-pulse channel with real high-frequency transient content."

**Common misuse:** treating CFC as interchangeable with sample rate, or picking a class by channel type alone without checking whether the corner frequency actually matches the content — too low smooths out a real peak, too high lets noise through that gets misread as signal.

### Shunt calibration
Simulating a known microstrain value by switching a fixed resistor across one arm of a strain-gauge Wheatstone bridge and comparing the predicted output (GF × ε × Vex) to the measured output — it verifies the entire signal chain (wiring, excitation, gain), not the gauge bond itself.

**In use:** "Shunt-cal predicted 61.80 mV, measured 61.42 mV — 0.61% error, signal chain verified good for today's run."

**Common misuse:** treating a shunt-cal done at initial bonding as still valid weeks later, when thermal cycling, connector reseating, and excitation drift make it a same-session check, not a one-time install step.

### Gauge factor (GF)
The proportionality constant relating a strain gauge's fractional resistance change to the mechanical strain it's experiencing, specific to the gauge part number, used to convert bridge output voltage into strain.

**In use:** "GF is 2.06 for this gauge — that's the multiplier in the shunt-cal prediction, not an adjustable calibration knob."

**Common misuse:** assuming gauge factor is a universal constant (like 2.0) rather than a part-specific certified value, which silently skews every strain reading taken with the wrong GF plugged into the conversion.

### SAE J1349 corrected power
A standardized correction of measured dyno power to a fixed reference condition (25°C, 99 kPa) and standardized mechanical-efficiency constant, so numbers from different days and altitudes are comparable — distinct from the older J607 correction basis.

**In use:** "247 hp corrected per J1349, dyno-day CA applied — that's the number that's comparable to the predicted curve."

**Common misuse:** comparing a J1349-corrected figure directly against an older J607-based figure (or an uncorrected as-run number) without checking the basis — the two bases commonly differ by roughly 4% on the same engine, and the gap gets mistaken for a real performance difference.

### Rainflow counting
An algorithm that decomposes an irregular, variable-amplitude stress or strain time history into discrete closed stress-cycle bins (amplitude and count), the standard input format for a fatigue damage calculation — it counts cycles, it does not itself estimate life.

**In use:** "Rainflow gave us three dominant bins — 180 MPa/1,200 cycles, 120 MPa/8,500, 80 MPa/45,000 — now those go against the S-N curve."

**Common misuse:** treating the rainflow output (the cycle bins) as the final damage or life number, skipping the separate step of running each bin against an S-N curve and summing fractional damage.

### Miner's rule / damage fraction
A linear cumulative-damage summation (Σ n/N across stress bins) estimating what fraction of a component's fatigue life has been consumed by a given load history — a directional estimate with a documented, non-trivial error band, not an exact remaining-life prediction.

**In use:** "D = 0.06775 after 500 test-hours. Linear extrapolation gives a central estimate of 7,380 hours, but published correlation studies show 2.7%-31% error against actual fatigue life, so we report 5,092-9,668 hours, not a single number."

**Common misuse:** reporting the linear extrapolation of a damage fraction as a precise remaining-life figure, hiding the method's documented correlation error band from the engineer making a release or inspection-interval decision on it.

### Calibration interval vs. calibration range
The interval is how long a certificate stays valid (e.g., 12 months / 5,000 cycles for a torque wrench under ISO 6789); the range is which specific points along the instrument's scale were actually verified (typically 20/60/100% of rated capacity) — an instrument can be within interval and still unverified at the point being used.

**In use:** "Wrench is 4 months into its 12-month interval, but the job needs 175 N·m and the cert only verified 20/60/100% of a 200 N·m-rated wrench — 175 N·m falls inside the verified range, so it's good."

**Common misuse:** checking only the date on the calibration sticker and assuming that covers any reading taken anywhere on the instrument's scale, when a reading past the last verified point (even if the cert hasn't expired) is an extrapolation, not a measurement.

### Class I vs. Class II torque wrench
Under ISO 6789, Class I covers mechanical/indicating wrenches (±4% tolerance) and Class II covers digital wrenches (±2% tolerance) — the class is a tolerance-band designation, not a brand or price tier.

**In use:** "Wheel hub is safety-critical, so it gets a Class II digital wrench at ±2%, not a Class I click wrench at ±4%."

**Common misuse:** assuming "digital" automatically means Class II-grade accuracy, or picking a wrench by convenience/availability rather than by whether the fastener's consequence of failure actually requires the tighter tolerance.

### Standard grade vs. SLE (Special Limits of Error) thermocouple
Under ASTM E230/IEC 60584-2, a standard-grade Type K thermocouple carries ±2.2°C (or ±0.75% of reading) tolerance; SLE grade tightens that to ±1.1°C (or ±0.4%) — a grade selection made based on required accuracy, not a universal upgrade.

**In use:** "EGT work sits close to a threshold where 2.2°C matters, so this channel gets SLE-grade thermocouples, not standard."

**Common misuse:** treating "Type K" as fully specifying the instrument's accuracy, when the grade (standard vs. SLE) is a separate spec that can double the effective tolerance if left unstated or assumed.

### Bridge configuration (quarter / half / full)
The number of active strain-gauge arms wired into a Wheatstone bridge circuit — quarter-bridge (1 active arm) is most sensitive to temperature drift, full-bridge (4 active arms) offers the highest output and best temperature compensation, and the choice changes both the sensitivity and what the reading actually represents.

**In use:** "This is a full-bridge setup for temperature-compensated axial load — a quarter-bridge here would pick up thermal drift as if it were mechanical strain."

**Common misuse:** treating bridge configuration as a wiring convenience decision rather than a measurement-physics decision — the configuration determines whether temperature effects cancel out or contaminate the reading.

### Pending vs. confirmed vs. cleared calibration status
Distinct from a DTC's pending/confirmed states — in an instrumentation context this refers to whether a given calibration certificate is current, expired-but-unused, or actively relied on for today's readings; conflating "has a cert on file" with "verified for today's use" is the failure mode.

**In use:** "The load cell has a current cert, but it wasn't shunt-checked this session — cert current isn't the same as verified for today's setup."

**Common misuse:** treating a filed, in-date calibration certificate as sufficient proof an instrument is reading correctly right now, skipping the same-session verification step (shunt-cal, zero check) that catches drift the certificate can't.

### Corrected vs. as-run (uncorrected) power
"Corrected" power has been adjusted to a standardized reference condition (temperature, pressure, humidity per SAE J1349); "as-run" is the raw dyno reading at whatever ambient conditions existed that day — the two numbers are not interchangeable, and only corrected figures are comparable across test days.

**In use:** "As-run was 251 hp today, but corrected to J1349 reference conditions it's 247 hp — that's the number that goes in the report against the predicted curve."

**Common misuse:** reporting or comparing an as-run figure as if it were corrected, which manufactures apparent day-to-day performance swings that are really just weather.
