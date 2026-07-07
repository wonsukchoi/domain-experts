# Playbook

Operational sequences an installer actually runs, with structure, example numbers, and thresholds. Starting points to adapt to the vehicle, glass, and conditions in front of you, not scripts.

## 1. Damage inspection and repair-vs-replace decision

Run before quoting anything past the initial phone estimate — a phone quote is a placeholder, not a repair plan.

**Repair-disqualifier checklist (any single hit routes to replacement):**

| Criterion | Repairable range | Replace trigger |
|---|---|---|
| Crack length | Up to ~6 inches | Past ~6 inches |
| Distance from edge | More than ~2 inches from any edge | Within ~2 inches of an edge |
| Location | Outside driver's direct forward-vision area | Inside driver's direct forward-vision area, regardless of size |
| Depth | Damage confined to outer glass layer | Reaches or penetrates the inner laminate layer (felt on inside surface, delamination bubble present) |
| Repair history | First or second repair on this pane | Third or later repair on the same pane |
| Break type | Single chip, bullseye, or star break under ~1 inch diameter | Combination break (multiple crack types radiating from one impact point) |

**Filled example (customer-reported "small chip," on inspection):**

1. Measure length: 9 inches — fails the ~6-inch criterion on its own.
2. Measure edge distance at nearest point: 1 inch — fails the ~2-inch criterion independently.
3. Check location against driver's seated eye position: upper end of crack crosses the direct forward-vision area — fails independently of the first two.
4. Result: replace. Do not attempt resin injection to save the customer money; a resin fill in the driver's direct view leaves optical distortion regardless of whether the fill holds structurally.

**If repairable:** clean the break of contamination, warm the glass if cold (resin viscosity is temperature-sensitive), inject resin under vacuum/pressure cycling per the resin manufacturer's process, cure with UV, then scrape and polish flush. Recheck for stress cracks radiating from the injection point before releasing the vehicle.

## 2. Cut-out and pinch-weld preparation

1. **Protect interior and cowl** before starting — urethane and glass fragments contaminate trim and electronics if unprotected.
2. **Identify every sensor, bracket, or mount referencing the glass** before cutting: forward camera bracket, rain/light sensor pad, HUD combiner area, embedded antenna or heating grid leads. Photograph mounting positions before removal.
3. **Cut along the OEM-specified line** using cold-knife or wire-out technique — avoid gouging the pinch-weld flange; a full cut-out (removing essentially all old adhesive down to a thin base layer) is the default unless the OEM procedure specifies a partial-cut (short-cut, leaving ~1-2mm of old adhesive as a bonding base) method for that model.
4. **Inspect the exposed bonding surface** for scratches, gouges, or bare metal where the e-coat has been breached.
5. **Prime any bare metal or exposed e-coat damage** with the adhesive manufacturer's pinch-weld primer before proceeding — an unprimed scratch under the new bead is a corrosion site that surfaces at the next replacement, not this one.
6. **Dry-fit the new glass** before applying primer/activator to the glass edge, checking gap and setting-block positions match the vehicle's mounting geometry.

## 3. Adhesive selection and SDAT lookup

**Step through, per job:**

1. **Confirm adhesive class matches vehicle requirement** — airbag-equipped structural vehicles require a crash-rated urethane system; never substitute a lower-strength or non-structural sealant class to save cost or time.
2. **Apply glass primer/activator and body-side primer where required**, and respect each product's flash/dry time before beading — this is a separate clock from SDAT, measured in minutes, not hours.
3. **Pull today's actual temperature and humidity**, not an assumed shop-average, especially on mobile/onsite jobs.
4. **Cross-reference the adhesive's SDAT table for those exact conditions.**

**Example SDAT cross-reference (illustrative of the table pattern manufacturers publish — always confirm against the specific product's current data sheet):**

| Condition | SDAT (airbag-equipped / structural bond) |
|---|---|
| 73°F / 50% RH | 1 hour |
| 55°F / 40% RH | 3 hours |
| 40°F / 30% RH | 6 hours |
| Below 32°F or below ~20% RH | Consult manufacturer — many moisture-cure products are not rated for use below their published minimum application temperature at all |

5. **Communicate the resulting SDAT to the customer as a fixed release time**, not a range, before the job starts — "ready at 3:15pm," not "should be a few hours."
6. **Do not move the vehicle before SDAT clears, including for in-bay repositioning.** The clock starts at bead completion, not at job start.

## 4. ADAS calibration decision and procedure

**Step through, per vehicle, on every windshield replacement:**

1. **Identify whether a forward-facing camera, rain/light sensor with camera-adjacent functions, or HUD combiner references this glass.** If none, no calibration is owed — do not calibrate by default on jobs with no sensor in the reference path.
2. **Check the OEM procedure for that exact model/trim/build** — calibration requirements and static-vs-dynamic sequencing vary by configuration; never infer from a similar job on a different trim.
3. **If required, set up static calibration first where the OEM procedure calls for it**: level bay (commonly within a fraction of a degree of level), target board(s) at the OEM-specified distance and height from the vehicle's centerline, even lighting with no glare on the target, vehicle at specified tire pressure, fuel level, and unladen cargo state.
4. **Run dynamic calibration** (a road drive at a specified speed range with clear, visible lane markings, typically requiring daylight and dry conditions) if the OEM procedure requires it — in the sequence specified (commonly static before dynamic, since static gives the system its rough aim before the dynamic drive fine-tunes against real lane data).
5. **Generate and retain the calibration confirmation report** — a pass/fail printout from the calibration tool, not a technician's verbal "it drove fine."
6. **Do not release the vehicle without the confirmation report on file**, even under schedule pressure — an unaimed camera with no warning light is the shop's liability, not a visible defect the customer will catch.

## 5. Job-sequencing and cycle-time benchmarks

| Job type | Typical duration | Common stall point |
|---|---|---|
| Chip repair (resin injection) | 20-30 minutes | Break contamination requiring extended cleaning before injection |
| Standard windshield replace, no camera | 1-1.5 hours install + SDAT hold | SDAT extending past quoted time on cold/mobile jobs |
| Windshield replace with camera, static calibration only | 1.5-2 hours install + calibration + SDAT hold | Bay not level, or lighting/glare failing target setup |
| Windshield replace with camera, static + dynamic calibration | 1.5-2 hours install + calibration + SDAT hold, calibration drive gated behind SDAT clear | Dynamic drive can't start until SDAT clears, pushing calibration into a second time block same day |
| Back glass / door glass, no ADAS reference | 45 minutes-1 hour | Regulator or trim clip damage discovered mid-job |

A job running past its tier's benchmark is a diagnostic prompt: check whether the stall is cure-time driven (expected, don't rush it) or process-driven (target setup, parts mismatch, sensor compatibility issue) — the response to each is different, and only one of them is safe to compress.
