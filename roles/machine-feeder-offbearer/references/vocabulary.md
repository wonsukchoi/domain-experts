# Vocabulary

Terms generalists blur together that a machine feeder/offbearer keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

### Point of operation vs. pinch point

The **point of operation** is the specific area on a machine where work is actually performed on material — where a die cuts, a punch forms, a blade shears. A **pinch point** is any location where two parts come together with enough force to trap something, which can exist anywhere on a machine, not just where the work happens. The point of operation gets a different regulatory treatment (guarded "so far as practicable," backed up by distance/timing devices) precisely because material must pass through it, unlike a general pinch point that can usually be fully enclosed.

**In use:** "That's the point of operation at the die — it can't be fully boxed in like the pinch point at the flywheel guard can."

**Common misuse:** treating every hazard on the machine as equally guardable, missing that the point of operation is the one place a full barrier is often not an option.

### Two-hand control vs. two-hand trip

A **two-hand control** requires both hands to remain on the actuating buttons for the entire hazardous part of the cycle (anti-tie-down) — releasing either hand stops the stroke. A **two-hand trip** only requires both hands to press simultaneously to *start* the cycle; hands can then be withdrawn or moved before the stroke completes. Using a two-hand trip on a fast-cycling operation where hands could re-enter before the stroke finishes provides materially less protection than a two-hand control, even though both devices "require two hands."

**In use:** "This press needs a two-hand control, not a two-hand trip — the cycle's fast enough that a trip alone doesn't stop a hand from re-entering."

**Common misuse:** assuming any device requiring two hands provides the same level of protection, without checking whether it holds through the full cycle or only initiates it.

### Anti-tie-down vs. anti-repeat (two-hand control features)

**Anti-tie-down** defeats an attempt to disable one button (tape, a block, a zip tie) by requiring both buttons to be operated within a set time window of each other — one permanently-held button won't trigger a stroke. **Anti-repeat** requires releasing and re-pressing both buttons to get a subsequent stroke, preventing a continuous run from holding the buttons down once. Both features address different defeat attempts; a control missing either one is not equivalent to a fully compliant one.

**In use:** "Check the anti-tie-down setting too — someone taping one button won't get past anti-repeat alone."

**Common misuse:** verifying that a two-hand control is present and functioning without confirming which specific defeat-resistant features are active on it.

### Minimum safety distance (Ds) vs. installed distance

**Minimum safety distance** is the calculated value (Ds = K × T for two-hand controls, or the fuller formula including Dpf for presence-sensing devices) below which a hand could reach the point of operation before the machine can stop. **Installed distance** is what's physically measured on the floor right now. The two only match if someone re-verifies installed distance every time stopping time or layout changes — they are not the same number by default.

**In use:** "Ds comes out to 18.9 inches at this stop time — installed is only 14. That's a finding, not a rounding difference."

**Common misuse:** citing the distance recorded at commissioning as still valid without re-measuring after a layout change or re-checking stop time.

### Cycle time vs. stroke rate (spm)

**Cycle time** is the actual time one complete cycle takes, measured from real operation. **Stroke rate (strokes per minute, spm)** is the nameplate figure, the reciprocal of design cycle time under ideal conditions. A machine's nameplate spm assumes the feed task keeps pace without interruption — it is not itself a measurement of what the station is actually achieving.

**In use:** "Nameplate's 20 spm, but our measured cycle time with the feed task included only gets us to 14.6."

**Common misuse:** reporting nameplate spm as the station's output rate without separately timing the actual feed-and-clear cycle.

### Feed rate vs. cycle time

**Feed rate** is how quickly material is actually being delivered into the machine by the feeder or feed mechanism. **Cycle time** is the machine's own fixed repeat interval. The two have to match; a feed rate faster than cycle time causes pile-up and jams at the infeed, and slower creates idle machine time — neither is corrected by adjusting the other in isolation without addressing the mismatch itself.

**In use:** "Feed rate's outrunning the press's cycle time — that's why we're jamming at the infeed, not a material problem."

**Common misuse:** treating a jam or idle-time issue as a material-handling problem to route around, rather than a feed-rate-to-cycle-time mismatch to fix directly.

### Pullback device vs. restraint device

A **pullback device** is physically attached to the operator's hands and mechanically withdraws them from the point of operation as the machine cycles. A **restraint device** tethers the hands at a fixed safe distance, preventing entry into the point of operation at all rather than pulling them out after they've entered. Pullback suits operations where the hand must enter and be withdrawn each cycle; restraint suits operations where the hand never needs to enter the hazard area in the first place.

**In use:** "This job needs a restraint, not a pullback — the hand never has to go anywhere near the die on this part."

**Common misuse:** treating the two as interchangeable "hand safety" devices rather than selecting by whether the operation requires hand entry into the point of operation at all.

### Nuisance trip vs. safeguard defeat

A **nuisance trip** is a presence-sensing device activating from something other than a genuine hazard exposure — debris, an awkward reach angle, a placement issue — that should be fixed at the device or process level. A **safeguard defeat** is a deliberate bypass of a device's protective function — muting it, taping a button, standing to its side. Treating repeated nuisance trips as something to route around rather than fix is exactly how a nuisance trip turns into a habitual safeguard defeat.

**In use:** "We're getting nuisance trips from the tote overhang, not a real crossing — fix the tote position, don't mute the curtain."

**Common misuse:** responding to a nuisance trip by disabling or working around the device instead of correcting whatever is triggering the false activation.

### Stop-time monitor reading vs. rated stopping time

The **stop-time monitor reading** is the machine's actual, currently measured stopping time from a periodic check. **Rated stopping time** is a specification or design value that may no longer reflect current brake condition. The Ds calculation uses the current monitor reading, not the rated figure, because brake wear moves the real number over time.

**In use:** "Ds is based on this quarter's stop-time reading, not the spec sheet number from when the press was new."

**Common misuse:** using a machine's original rated stopping time to compute Ds indefinitely, missing that the actual value drifts upward as brakes wear.

### Takt time vs. cycle time

**Takt time** is the rate demand requires — how often a completed unit needs to come off the station to meet production need. **Cycle time** is what the machine and feed task actually take, independent of demand. A feeder's job is matching cycle time to takt, not maximizing feed speed regardless of what demand actually calls for; pushing pace past takt just to hit a machine's nameplate rate creates the pressure that erodes safeguard margins for no demand-side benefit.

**In use:** "Takt only calls for 12 units a minute — we don't need to chase the press's 20 spm nameplate to meet the order."

**Common misuse:** treating a machine's maximum nameplate rate as the target pace regardless of what the actual production schedule requires.
