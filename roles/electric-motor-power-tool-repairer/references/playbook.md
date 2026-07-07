# Playbook

Diagnostic and repair protocols run in the shop, with the actual thresholds and step sequences used — not descriptions of what a protocol should contain.

## 1. Intake diagnostic sequence (industrial/three-phase motors)

Run in this order on every three-phase motor before opening a case, regardless of the customer's stated symptom:

1. **Megohmmeter IR/PI test.** Apply 500 VDC for windings rated ≤1 kV (1000 VDC for 1–2.5 kV rated windings). Record the 1-minute reading, then the 10-minute reading. Polarization Index = 10-min reading ÷ 1-min reading.
2. **Temperature-correct the 1-minute IR reading to 40°C** if winding temperature at test differs by more than ~5°C (IR roughly halves for every 10°C rise; use the shop's correction chart, not a flat estimate).
3. **Compare against the class-based minimum**: absolute IR minimum = (rated kV + 1) megohms; PI minimum by insulation class — Class A: 1.5, Class B/F/H: 2.0. If insulation class is undocumented, use the 2.0 minimum.
4. **Vibration spectrum** (accelerometer + FFT) at drive-end and non-drive-end bearing housings — baseline overall velocity against ISO 10816-3 bands before assuming a specific fault.
5. **Motor current signature analysis (MCSA)** if vibration or trip history suggests an electrical rotor issue — clamp on one phase, spectrum around line frequency, checked for slip-locked sidebands.
6. **Growler/surge test** if a turn-to-turn short is suspected and the megohmmeter reading alone doesn't explain the symptom (surge tests catch shorts a ground-fault-only IR test misses).

## 2. IR/PI decision tree

| Absolute IR vs. minimum (kV+1) | PI vs. class minimum | Action |
|---|---|---|
| Passes | Passes (≥2.0 Class B/F/H, ≥1.5 Class A) | Return to service, no action |
| Passes | Fails (below class minimum) | Open frame for visual inspection. No visible carbon tracking/embrittlement → dry-out cycle, retest IR/PI before quoting rewind. Visible physical damage found → rewind, do not rely on dry-out alone |
| Fails | Fails | Rewind or replace — run the economics tree (section 4) |
| Fails | Passes | Rare; treat as a probable test error (moisture on terminals, poor ground connection) — clean and retest before condemning the winding |

**Dry-out cycle:** controlled oven or space-heater ramp, winding temperature held at roughly 90–110°C (well below the insulation's thermal class limit) for 4–8 hours depending on motor mass, then retest cold. A PI that recovers to ≥ the class minimum with no physical damage found on inspection confirms a moisture/contamination cause; a PI that doesn't recover, or a carbon track/embrittled varnish found on teardown, means rewind regardless of what dry-out alone would have shown.

## 3. Bearing-fault vs. rotor-bar-fault isolation

1. Pull the vibration spectrum at both bearing housings; note peak frequencies as multiples of running speed and as absolute Hz.
2. **Non-synchronous peaks matching calculated bearing defect frequencies** (BPFO, BPFI, BSF, FTF — from the bearing's geometry and running speed, not from slip) → bearing fault. Confirm with bearing serial/part number lookup before ordering a replacement.
3. **Sidebands appearing at ±2×slip×line-frequency around the fundamental** (in either the vibration spectrum or the MCSA current spectrum) → broken or cracked rotor bar, or rotor-bar/end-ring asymmetry. Slip = (synchronous speed − actual speed) ÷ synchronous speed; for a 4-pole 60 Hz motor running at 1750 RPM against a synchronous 1800 RPM, slip = 50/1800 = 0.0278, so sidebands would appear at roughly ±3.3 Hz from the 60 Hz fundamental.
4. **Overall vibration velocity vs. ISO 10816-3 Class II (medium machines, 15–300 kW on rigid mounts):** <1.12 mm/s RMS good; 1.12–2.8 satisfactory; 2.8–7.1 unsatisfactory; >7.1 unacceptable. Above ~7.1 mm/s, schedule the repair regardless of which fault type is confirmed — the distinction changes what's replaced, not whether action is needed.
5. **Do not pull bearings on a confirmed rotor-bar signature.** A bearing swap on a rotor fault motor will read clean on reassembly vibration test and fail again within weeks once the actual fault resumes producing sidebands.

## 4. Rewind-vs-replace economics

1. Get current new-unit replacement price for the same frame size, enclosure, and efficiency class (not a price from memory or a dated catalog).
2. Get a rewind quote from a burnout process that is temperature-controlled (target ≤650–700°F/343–371°C) with core-loss (no-load) verification before and after.
3. Compute ratio = rewind cost ÷ new-unit cost.

| Ratio | HP range | Action |
|---|---|---|
| <60% | Any, but especially >15–20 HP | Rewind favored — confirm burnout is temperature-controlled before recommending |
| 60–65% | Mid-size (5–15 HP) | Borderline — weigh against downtime/lead-time on a new unit and any efficiency-standard mismatch (older motor may be pre-EISA/pre-premium-efficiency) |
| >65% | Any | Replace favored |
| Any ratio | <3–5 HP | Replace almost always — labor to strip/rewind is close to flat across frame sizes and dominates the ratio at small HP |

4. **Core-loss verification:** no-load (open-circuit) input power measured at rated voltage, before strip and after rewind. An increase of more than roughly 5% signals core damage from an over-temperature burnout even if the rewind otherwise looks clean — flag this to the customer rather than deliver silently.
5. **Wire gauge and turns count** on the rewind must match the original nameplate/data-tag values; a rewind done with a different gauge or turns "because it was on hand" changes the motor's torque/current curve and is a defect, not a substitution.

## 5. Universal-motor (power tool) brush and commutator wear

| Measurement | New/spec | Action threshold |
|---|---|---|
| Brush length | Manufacturer spec, typically 10–14mm depending on tool | Replace at ~50% of new length, or sooner if spring force reads below manufacturer spec on a tension gauge |
| Commutator TIR (runout) | <0.02mm (0.001in) typical for small motors | Above ~0.05mm (0.002in), expect brush chatter/arcing — resurface on a commutator lathe before it self-worsens |
| Mica undercut depth | 0.8–1.2mm (0.03–0.05in) below segment surface | Recut if mica has worn level with or above the copper (causes brush bridging and arcing) |
| Commutator segment discoloration | Even light-brown patina across all bars is normal | Discoloration/blackening on a consistent every-Nth-bar pattern indicates an open or shorted armature coil, not general wear — check armature continuity/resistance before resurfacing |

**Sequence:** measure brush length and spring force first (cheapest check); if both pass, check commutator TIR and undercut before returning the tool; if segment damage is patterned rather than uniform, stop and check the armature winding before doing any mechanical resurfacing work that would mask the electrical fault.

## 6. Bearing fit verification on reassembly

1. Check shaft-to-bearing-bore fit against the bearing manufacturer's tolerance class for the application (typical light-to-moderate interference fit for motor bearings: +0.0002 to +0.0007in / 0.005–0.018mm over nominal shaft diameter, depending on bearing bore size).
2. Verify housing bore fit separately — too loose a housing fit lets the outer race creep and produces the same non-synchronous vibration signature as a worn bearing within months of a "good" repair.
3. Use an induction heater (not a torch) to expand bearings for installation — localized torch heat risks uneven expansion and can alter the race's hardness/tolerance.
4. Re-run the vibration spectrum after reassembly and compare against the pre-repair baseline before calling the job complete.
