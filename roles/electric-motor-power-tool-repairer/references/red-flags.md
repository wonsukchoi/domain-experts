# Red flags

Smell tests a senior motor repairer catches at intake, before opening the frame. Format for each: what it usually means, the first question to ask, and the data to pull before quoting or condemning anything.

## 1. Polarization Index below 2.0 (Class B/F/H) despite absolute IR passing its minimum

**Usually means:** moisture or surface contamination degrading the winding faster than the absolute IR number shows — the intermittent-trip pattern customers report is often this, not a hard ground fault yet.

**First question:** "What's the 10-minute-to-1-minute ratio, not just the 1-minute reading?"

**Data to pull:** temperature-corrected 1-min and 10-min IR readings, winding temperature at test, insulation class from the nameplate/data tag (default to the conservative 2.0 minimum if undocumented). Then open the frame for a visual check before deciding dry-out vs. rewind.

## 2. Non-synchronous vibration peaks the tech immediately calls "a bearing"

**Usually means:** frequently correct, but sometimes a rotor-bar or eccentricity fault mistaken for a bearing because nobody ran the numbers — bearing defect frequencies (BPFO/BPFI/BSF/FTF) are fixed by geometry, not by ear.

**First question:** "What's the calculated BPFO/BPFI for this bearing at this running speed, and does the peak actually land there?"

**Data to pull:** bearing part number and geometry, measured running speed, vibration spectrum peak frequencies, and — if any doubt remains — an MCSA current spectrum checked for slip-locked sidebands before ordering bearings.

## 3. Sidebands at ±2×slip×line-frequency around the fundamental current spectrum

**Usually means:** a broken or cracked rotor bar, or rotor/end-ring asymmetry — not a bearing or stator winding fault.

**First question:** "What's this motor's slip at the load point it was running, and do the sideband offsets match 2×slip×line-frequency?"

**Data to pull:** nameplate synchronous speed and measured actual speed (for slip calculation), MCSA spectrum, and vibration spectrum cross-check — a rotor-bar fault motor should not get a bearing replacement quote.

## 4. Vibration overall velocity above ISO 10816-3 Class II "unsatisfactory" (>7.1 mm/s RMS)

**Usually means:** active mechanical degradation regardless of which specific fault is confirmed — this is a schedule-the-repair-now threshold, not a monitor-and-wait one.

**First question:** "Where does today's reading sit against the last three readings — is this a step change or a slow climb?"

**Data to pull:** trended vibration history if available, current spectrum for fault-type identification, and load/speed conditions at time of measurement (loose base or misalignment can inflate the reading independent of bearing/rotor condition).

## 5. Rewind quote at or above ~65% of current new-unit replacement cost

**Usually means:** the shop is defaulting to "rewind because that's what we do" rather than running the actual ratio against today's new-motor pricing.

**First question:** "What's a current delivered price for this exact frame size and efficiency class, not last year's number?"

**Data to pull:** current new-unit quote at matching HP/voltage/enclosure/efficiency class, rewind labor-and-parts breakdown, and the motor's HP (ratio math almost never favors rewind under ~3–5 HP regardless of the percentage).

## 6. Burnout done by open flame or an oven with no logged temperature

**Usually means:** core steel damage risk — uncontrolled burnout temperatures above roughly 700°F (371°C) measurably increase core loss, and there's no way to verify after the fact without a no-load test.

**First question:** "What was the peak burnout temperature, logged how, and do we have a pre-strip no-load reading to compare against?"

**Data to pull:** burnout oven temperature log (if none exists, that's the finding), pre-strip and post-rewind no-load (core-loss) test results — an increase over ~5% confirms core damage.

## 7. Rewind delivered with no before/after core-loss test on record

**Usually means:** there's no evidence the rewind preserved efficiency, whether or not it actually did — this is the shop skipping the one verification step that matters.

**First question:** "Do we have a pre-strip no-load power reading for this motor?"

**Data to pull:** shop's standard intake checklist (if core-loss test isn't a line item, that's the process gap to fix, not just this one job).

## 8. Universal-motor brushes worn below ~50% of new length, tool still "runs fine"

**Usually means:** the tool is functional today and close to commutator-damaging arcing — brush wear doesn't announce itself until sparking is visible, by which point pitting has usually started.

**First question:** "What's the measured brush length against this model's new-brush spec, not just whether it still sparks visibly?"

**Data to pull:** brush length measurement, spring-tension gauge reading against manufacturer spec, commutator surface condition under magnification.

## 9. Commutator discoloration on a consistent every-Nth-bar pattern

**Usually means:** an open or shorted armature coil, not general mechanical wear — resurfacing the commutator without checking the armature just masks the electrical fault until it recurs.

**First question:** "Is the discoloration uniform across all bars, or does it repeat at a fixed interval matching the number of armature coils?"

**Data to pull:** armature coil resistance/continuity check (growler test), bar-to-bar pattern photographed before any resurfacing work.

## 10. New winding's wire gauge or turns count doesn't match the nameplate data

**Usually means:** a rewind done with whatever wire was on hand rather than to the original spec — changes the torque/current/speed curve even if the motor "runs."

**First question:** "Does the rewind spec sheet list the original turns-per-coil and wire gauge from the nameplate/data tag, and does the finished winding match it?"

**Data to pull:** original nameplate/data-tag winding data (if available), rewind shop's spec sheet, no-load current draw comparison against nameplate full-load amps.

## 11. Motor under ~5 HP quoted for rewind rather than replacement

**Usually means:** the shop is applying a large-motor rule of thumb to a size class where it doesn't hold — rewind labor cost is close to flat across frame sizes, so it dominates the ratio on small motors.

**First question:** "What does a new unit at this HP and voltage cost delivered, compared to the rewind quote?"

**Data to pull:** current new-unit price, rewind quote breakdown — if the ratio is anywhere near 50%+ at this size, replacement is almost always the better economics.
