# Vocabulary

Terms generalists conflate or misuse. Each: definition, how a practitioner actually uses it, and the common misuse.

### MECP (Mobile Electronics Certified Professional)
The 12V-install trade's certification, administered by CTA (Consumer Technology Association), with tiers from Installer 1/2 up through Advanced Level 1 (car audio), 2 (mobile video), and 3 (security/convenience — remote start, alarms).

**In use:** "This is a CAN-bus remote start integration on a push-button-start trim — that's Advanced 3 scope, route it to someone certified at that level, not a general installer."

**Common misuse:** treating "MECP certified" as one undifferentiated credential, when the level and specialty (audio vs. video vs. security/convenience) is the entire point — Advanced Level 1 says nothing about competence integrating with a factory data bus.

### DVC (Dual Voice Coil) vs. SVC (Single Voice Coil) subwoofer
A DVC sub has two separate voice coils on one former, each independently wired, giving multiple final-impedance options depending on whether the coils are wired in series, parallel, or split across amp channels; an SVC sub has one coil and one fixed per-unit impedance.

**In use:** "These are DVC 4-ohm subs — wiring each sub's coils in series gets us 8-ohm per sub, which is the only path to a safe 4-ohm final load with two of them in parallel."

**Common misuse:** assuming any DVC sub pair can be wired to any arbitrary target impedance — the achievable final loads are a fixed small set determined by the coil rating and sub count, not a continuous range.

### Bridged (mono) vs. stereo stable-impedance rating
An amplifier's spec sheet lists a minimum stable impedance separately for two-channel (stereo) operation and for bridged (mono, summed) operation; the bridged-mono minimum is always numerically higher than the stereo minimum for the same amp.

**In use:** "This amp is 2-ohm stable in stereo but 4-ohm stable bridged — since we're running one mono sub channel, we compute against the 4-ohm bridged number, not the 2-ohm stereo number."

**Common misuse:** reading only the lower stereo-mode number off a spec sheet and applying it to a bridged-mono wiring job, which understates the actual load risk.

### Gain
An amplifier's input-sensitivity control, which sets how much preamp-level signal is required to reach the amp's full rated output — it is not a volume control and does not directly set loudness.

**In use:** "Gain is set to hit 34.6V AC at the speaker output on a reference tone — that's the amp's full rated power right at the edge of clipping, regardless of what volume the head unit is at."

**Common misuse:** treating gain like a second volume knob and turning it up "until it sounds loud enough," which pushes the preamp stage into clipping well before the amp's rated power is reached.

### Clipping
The point at which an amplifier (or the stage feeding it) can no longer reproduce a signal's peaks and instead outputs a flattened, distorted waveform; a distortion detector or oscilloscope identifies this point directly, the ear does not reliably detect it.

**In use:** "The clip light came on at 60% of the volume we thought we needed — the gain was set too high and the amp's been running clipped the whole time."

**Common misuse:** assuming a speaker or amp failure means the amp was "too powerful" for the speaker, when sustained clipped signal (not rated power itself) is the more common cause of voice-coil and output-stage failure.

### Line Output Converter (LOC)
A device that converts a factory (or aftermarket) head unit's speaker-level output into a preamp-level (RCA) signal an aftermarket amplifier's gain stage can accept, matched to the source deck's actual output voltage.

**In use:** "The factory deck outputs a high-voltage swing at full volume — we need an LOC rated for that input range, not a generic low-voltage one, or the signal clips before it even reaches the amp's gain control."

**Common misuse:** treating any LOC as interchangeable, ignoring that a mismatch between the deck's actual output voltage and the LOC's rated input range reintroduces clipping upstream of the amp entirely.

### CAN bus (Controller Area Network) — CAN-H / CAN-L
A twisted differential two-wire network (CAN-H and CAN-L) that vehicle modules share to communicate, terminated at each end by a resistor and designed around a fixed set of expected nodes and loading characteristics.

**In use:** "That's a CAN-H/CAN-L pair — we don't splice into it for the remote start trigger, we use the bypass module that reads it instead."

**Common misuse:** treating the CAN pair like any other wire that can be spliced into for a simple 12V-logic tap, when a splice changes the bus's electrical loading and can produce intermittent faults on modules that were never physically touched.

### Bypass module / T-harness ("listen, don't inject")
A trim-specific adapter that plugs inline at a factory connector (ignition switch, BCM harness) and reads the signals an accessory needs directly off the factory system, without adding a physical splice into a shared data-bus wire.

**In use:** "We used the Fortin harness built for this exact trim — it reads the door-lock and brake signals off the factory connector, no splice into the CAN pair at all."

**Common misuse:** using a universal splice-in harness in place of a trim-specific bypass module to save cost or because the correct part wasn't in stock, without documenting that substitution for a later comeback diagnosis.

### Parasitic draw (key-off draw)
The current a vehicle continues to pull from the battery after the key is removed and all modules have entered their normal sleep state, typically measured 20–40 minutes after the last door closes.

**In use:** "Baseline parasitic draw was 42 mA before we touched anything — that's the number we compare the post-install reading against, not some generic table value."

**Common misuse:** measuring only the post-install draw and comparing it to a generic "normal is X mA" rule without ever establishing this specific vehicle's own pre-install baseline.

### Reserve capacity / depth of discharge (DoD)
Reserve capacity is roughly how long a battery can sustain a given discharge current before reaching a practical low-charge floor; depth of discharge is the percentage of a battery's capacity that's been drawn down from full.

**In use:** "At 35Ah usable to our 50% DoD floor and a 288 mA draw, this battery hits that floor in about five days — that's a dead battery on any week-long trip."

**Common misuse:** assuming a "healthy" battery can tolerate any parasitic draw indefinitely, without running the Ah-over-current arithmetic against how long the vehicle is actually expected to sit.

### ADAS calibration (static vs. dynamic)
Static calibration aims a camera or radar using fixed target boards at OEM-specified distances on a level surface; dynamic calibration is performed by driving the vehicle at a specified speed on roads with clear lane markings for a set duration — which method (or both) applies depends on the OEM and the specific system.

**In use:** "The windshield camera needs a static calibration with the target board at the OEM-specified distance before it can be trusted again — driving it around isn't sufficient for this platform."

**Common misuse:** assuming any ADAS system can be "recalibrated" just by driving it normally for a while, when many platforms require the specific static procedure and equipment or the system remains out of spec with no driver-facing warning.

### Trigger wire (switched vs. constant)
The wire an accessory monitors or is powered from to determine its on/off or sleep state — switched wires change state with ignition/accessory position, constant wires stay at battery voltage regardless of key position.

**In use:** "That trigger wire is landed on a constant-hot circuit instead of the switched accessory wire the harness diagram calls for — that's why the module never sleeps."

**Common misuse:** treating any convenient always-hot wire as an acceptable power tap for a device that's designed to sleep with the vehicle, rather than matching the wire's switched/constant behavior to what the device actually needs.
