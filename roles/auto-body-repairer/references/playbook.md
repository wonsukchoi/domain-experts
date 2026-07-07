# Playbook

Operational sequences a repairer actually runs, with structure, example numbers, and thresholds. Starting points to adapt to the vehicle and claim in front of you, not scripts.

## 1. Blueprinting / teardown sequence

Run before any estimate is treated as final — ideally within the first 24-48 hours of intake, before parts are ordered against guesswork.

**Steps, filled example (rear-end collision, unibody sedan):**

1. **Pre-repair scan** — pull DTCs on every module (not just the obviously affected ones) before touching the vehicle. *Example: pre-scan shows one pre-existing ABS code unrelated to the collision — logged and photographed so it isn't billed to the claim or mistaken for repair-caused damage later.*
2. **Remove cosmetic panels to bare structure** in the damage zone — bumper cover, trim, headliner edge if needed to see rail tops. Photograph before, during, and after removal of each layer.
3. **Set up 3D measuring system, establish centerline/datum first.** Measure the undamaged reference points before the damage area, to confirm the datum itself is sound.
4. **Measure all OEM-specified points in the damage zone**, record actual vs. spec for each, and calculate span deviation between point pairs, not single-point deviation.
5. **Classify each damaged component**: elastic deformation within OEM tolerance (no action), elastic deformation beyond tolerance (pull/measure/verify), or kinked/cracked/torn (replace, no exceptions regardless of measurement).
6. **Pull the OEM position statement for every component in the replace/repair path** before finalizing the write-up — confirms whether sectioning is permitted, where the OEM-approved cut line is, and whether full-assembly replacement is mandatory.
7. **Identify every ADAS sensor, bracket, or mount in or adjacent to the damage zone** and flag for the calibration decision (Section 4).

**Output artifact:** teardown photo set (before/during/after each layer), measurement printout with spec vs. actual per point, and a marked-up repair plan citing the OEM procedure page for each structural line — this packet is what the supplement in Section 3 is built from.

## 2. Frame / unibody pull-vs-replace decision

**The core test, in order:**

1. **Visual/tactile check first: is it kinked, cracked, or torn?** If yes — replace. Stop here; do not measure to look for a reason to keep it.
2. **If no visible kink/crack/tear, measure.** Compare actual reading to OEM-published tolerance for that point. If none is published, use the I-CAR UPCR fallback of ±5mm.
3. **Calculate span deviation as the sum of both endpoints' error**, not either endpoint alone.

**Example measurement table (rear rail, pinch-weld reference points, OEM tolerance ±3mm):**

| Point pair | Point A actual | Point B actual | Span deviation | OEM tolerance | Verdict |
|---|---|---|---|---|---|
| Rail pinch weld, L/R | +4mm | −3mm | 7mm | 3mm | exceeds — pull required |
| Rail pinch weld, front | +1mm | 0mm | 1mm | 3mm | within tolerance — no action |
| Rocker centerline | −1mm | +1mm | 2mm | 3mm | within tolerance — no action |

4. **If within tolerance:** no structural repair needed on that point; proceed to cosmetic repair only.
5. **If beyond tolerance but not kinked/cracked/torn:** pull to spec, re-measure to confirm return to tolerance, then check the component's steel-strength class before deciding sectioning is even an option.
6. **Steel-strength gate:** if the component is UHSS or boron-alloyed (~980-1,500 MPa class) and the OEM has not published a sectioning procedure for that exact location, do not section — replace the full assembly. If a sectioning procedure exists, section only at the OEM-specified location, using the OEM-specified weld type and pattern.
7. **Re-measure after any pull or replacement** before releasing the vehicle to paint — a component "fixed" but not re-verified is unconfirmed, not repaired.

## 3. Supplement documentation packet

**Rule:** every supplement line pairs a dollar amount with a source. No line ships without one of: a teardown photo, a measurement printout, an OEM procedure citation, or a parts-price update.

**Filled example (from the CR-V worked example in SKILL.md):**

```
SUPPLEMENT REQUEST — Claim #[xxxx]
Original estimate total: $4,150
Teardown date: [date]   Prepared by: [tech name / I-CAR credential #]

LINE 1: Rear frame rail deformation, pull + reinforce         +$980
  Source: measurement printout, point pair "rail pinch weld L/R,"
  7mm span deviation vs. 3mm OEM tolerance (attached)

LINE 2: Radar sensor mounting bracket, replace                +$210
  Source: teardown photo, bracket bent at weld point (attached)

LINE 3: Rear radar + camera calibration, static + dynamic      +$650
  Source: OEM procedure [manufacturer, doc #], calibration
  required following structural repair in this zone (attached)

LINE 4: Paint materials, quarter panel added to blend          +$340
  Source: direct consequence of Line 1 reopening adjacent panel

New total: $6,330 (52.5% over original — expect desk review;
all four lines are independently sourced above)
```

**Escalation threshold:** supplements under roughly 25-30% of the original total typically clear adjuster review without additional contact. Above that, expect a request for a phone review or in-person reinspection — have the physical measurement printouts and OEM procedure pages ready to reference live, not just attached as PDFs.

**Timing rule:** submit the supplement before committing to paint or reassembly, not after. A supplement submitted post-paint has already spent the shop's strongest leverage (the ability to show the insurer the open, un-repaired damage) and reads as an afterthought regardless of how well it's documented.

## 4. ADAS calibration decision process

**Step through, per sensor, for every repair:**

1. **Was this sensor, or anything that establishes its mounting reference, removed, replaced, or repaired?** (Bumper cover over a radar, windshield with a camera bracket, any bracket welded near the sensor, any structural component the sensor is indirectly referenced to.)
2. **Did ride height, wheel alignment, or steering geometry change?** Suspension or structural repairs can shift a camera or radar's aim reference even with zero direct contact with the sensor itself.
3. **Check the OEM procedure for that specific repair operation** — do not infer from a similar repair on a different trim or model year; calibration requirements vary by exact configuration.
4. **If required, determine static, dynamic, or both.** Static needs a level bay, OEM-specified target boards, and exact measured distances; dynamic needs a specific road-speed drive meeting lane-marking and traffic conditions the OEM specifies. Sublet to a calibration specialist if the shop lacks the static bay space or target equipment for that OEM.
5. **Run the calibration and generate the confirmation report** — most OEM-required calibration tools output a pass/fail printout; this is the artifact that goes in the delivery file, not a technician's verbal confirmation.
6. **Do not release the vehicle without the calibration confirmation report on file**, regardless of schedule pressure — an uncalibrated ADAS system with no dashboard warning is the shop's liability, not a visible defect the customer will catch.

## 5. Cycle-time benchmarks by severity

| Severity tier | Example damage | Typical cycle time | Common stall point |
|---|---|---|---|
| Cosmetic-only | Bumper cover scuff, no structural involvement | 1-3 days | Paint match / color code issue |
| Moderate, non-structural | Panel replace + blend, no ADAS sensor in zone | 4-7 days | Parts backorder |
| Moderate, structural | Rail pull within tolerance, no replacement | 7-10 days | Supplement approval delay |
| Major structural + ADAS | Rail replacement or sectioning + calibration | 10-16 days | Calibration sublet scheduling, or a supplement stuck in desk review |
| Total-loss candidate | Repair cost approaches state ACV threshold | N/A — routes to total-loss desk | Shop sinking labor into a repair the numbers already killed |

A repair running meaningfully past its tier's benchmark is a diagnostic prompt, not just a scheduling problem: check parts-order status, supplement approval status, and whether new damage was found mid-repair that was never blueprinted, in that order.
