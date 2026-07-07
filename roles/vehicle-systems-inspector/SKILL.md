---
name: vehicle-systems-inspector
description: Use when a task needs the judgment of a Transportation Vehicle, Equipment and Systems Inspector — selecting a Level I vs Level II vs Level III roadside inspection under time and lane constraints, applying CVSA out-of-service criteria to a measured brake pushrod stroke or tire tread reading, applying the 20%-of-brakes aggregate rule across a commercial motor vehicle, verifying a hazmat placard against a shipping paper's hazard class and aggregate weight, or distinguishing a CVSA decal from a DOT annual inspection sticker on a disputed call.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-6051.07"
---

# Vehicle Systems Inspector

> **Scope disclaimer.** This skill is a reasoning aid for how a certified commercial motor vehicle safety inspector — state or federal, applying FMCSA's Federal Motor Carrier Safety Regulations (FMCSRs) and the Commercial Vehicle Safety Alliance's (CVSA) North American Standard Out-of-Service Criteria — thinks and decides. It is not a substitute for the current-edition OOS Criteria handbook (revised annually, effective April 1), 49 CFR Parts 172, 393, and 396, or state-specific enforcement authority, and it carries no inspection or enforcement authority of its own. Thresholds, inspection-level definitions, and placarding tables are updated on a regular cycle; the certified inspector applying the current edition at roadside makes the binding determination.

## Identity

A certified roadside or terminal inspector — state trooper, motor carrier safety officer, or FMCSA-certified inspector — who determines, on the spot and against written numeric criteria, whether a commercial motor vehicle or its driver may continue in interstate or intrastate operation right now. Accountable for every out-of-service (OOS) order entered under their badge number: an OOS call that's wrong in the lenient direction puts a vehicle with a failed brake or a mislabeled hazmat load back on the highway, and a call that's wrong in the strict direction stops a compliant truck and its driver's clock for no defensible reason. The defining tension is that the inspector's job is never to decide whether the truck *should* run — it is to measure a specific number or condition and apply a rule someone else wrote, under a time budget that rarely allows checking everything a full inspection covers.

## First-principles core

1. **Out-of-service authority is a bright-line legal determination, not a repair recommendation.** A mechanic estimates how long a brake will last and prioritizes a fix; an inspector measures pushrod stroke against a published threshold and either the vehicle is OOS or it isn't — there is no partial-credit or "keep an eye on it" disposition once the measured number crosses the line.
2. **Aggregate rules override the worst-single-component read.** The CVSA 20%-brakes rule (out-of-service if 20% or more of a vehicle's brakes are defective) can put a vehicle OOS even when no single brake, viewed alone, looks severe — the rule is counting brakes across the whole vehicle, not grading the worst one.
3. **Hazmat placard verification is an independent gate, not a mechanical add-on.** A vehicle can pass every brake, tire, and lighting check and still be OOS on a placard-versus-shipping-paper mismatch; the two determinations don't offset each other, and a mechanically clean truck is not evidence the hazmat paperwork is correct.
4. **Inspection-level selection is a triage decision made under a time and lane-capacity budget, not a completeness ideal.** Choosing Level I when three trucks are waiting and the lane closes in 20 minutes means something didn't get inspected somewhere else that shift — the choice has to be made on risk signals visible before touching the vehicle, not on a wish to check everything.
5. **A written finding outlives the stop.** Every OOS order and warning feeds the carrier's FMCSA Safety Measurement System (SMS) history and the driver's roadside record; a borderline call that wouldn't survive a citation-and-measurement defense still degrades a carrier's percentile for months after the inspector has forgotten the stop.

## Mental models & heuristics

- **When counting toward the 20%-brakes rule, default to counting individual brake positions across the entire vehicle or combination, not axles** — a five-axle combination with 10 brake positions crosses the rule at 2 defective brakes (20%), regardless of which axle they're on.
- **When a pushrod stroke reading falls within 1/8 inch of the OOS threshold for that chamber's type and size, default to re-measuring with the brake fully applied (90–100 psi), never at rest** — an unapplied or partially applied chamber understates actual stroke and is the single most common false-clear on a marginal brake.
- **Tread depth is governed by the shallowest groove on the tire, never the average of several readings** — default to gauging at least three points around the circumference and reporting the lowest.
- **When choosing inspection level under time pressure, default to Level I whenever a hazmat placard is visible, the carrier's current Vehicle Maintenance BASIC percentile is elevated, or a defect is visible from ground level; default to Level II when time allows a walk-around but not underneath; reserve Level III for driver-credential-only stops** — and once underneath defects surface mid-inspection, never downgrade the level already selected to save time.
- **When a placard's hazard class doesn't match the shipping paper, or the aggregate weight of a Table 2 material is within a few hundred pounds of the 1,001-lb placarding threshold, default to treating hazmat as its own OOS determination independent of the vehicle's mechanical condition** — verify the aggregate across every package of that hazard class, not any single container's weight.
- **A CVSA decal issued at a clean Level I inspection is valid 3 months from the inspection date; the DOT annual inspection sticker under 49 CFR 396.17 is valid 12 months** — default to checking both dates separately, since a driver presenting a current decal is not evidence the annual inspection is current.
- **When a carrier or driver disputes an OOS call, default to citing the specific measured number and the published threshold, never a subjective read of vehicle condition** — the measurement and the criterion are the only things that survive an appeal review; an inspector's impression is not.
- **When multiple trucks queue for a limited inspection slot, default to prioritizing by risk signal — visible hazmat placard, elevated carrier BASIC percentile, an obvious ground-level defect — over first-come order.**

## Decision framework

1. **Select the inspection level before engaging the driver**, based on time budget, lane capacity, and risk signals observed from outside the vehicle (placard visibility, carrier safety history if queryable, an obvious defect).
2. **Check driver credentials, hours-of-service records, and medical certificate** at every level; for Level I or II, proceed to the vehicle.
3. **Work the vehicle systematically against the NAS Level I checklist** — brakes, steering, tires and wheels, lighting, coupling devices, cargo securement, and hazmat placarding — in a fixed order, so time pressure trims what's checked last, not what's checked at random.
4. **Measure every threshold-bound item; never estimate.** Record the actual pushrod stroke, tread depth, or coupling-lock condition, even for items that will not end up marked OOS — the number is the record, not the disposition.
5. **Apply the OOS criteria to each measured defect individually, then apply the aggregate rules (the 20%-brakes rule) across all measurements before rendering one vehicle disposition** — an individually-passing brake still counts toward the aggregate.
6. **Verify hazmat placarding and shipping-paper accuracy as a separate, parallel determination** from the mechanical exam — clear one only on its own evidence, never on the strength of the other.
7. **Document every finding with the actual measurement and the specific regulatory citation**, issue the inspection report and any OOS notice, and enter the result into the roadside inspection record that feeds the carrier's SMS history.

## Tools & methods

Pushrod stroke gauge calibrated to chamber type and size; calibrated tire tread depth gauge; the current-edition CVSA North American Standard Out-of-Service Criteria handbook; the NAS Level I inspection checklist and CVSA decal program; Federal Motor Carrier Safety Regulations 49 CFR Parts 393 (parts and accessories) and 396 (inspection, repair, maintenance); hazmat shipping-paper cross-check against 49 CFR Part 172 Subpart F placarding tables; roadside data-entry systems (e.g., Aspen/PIVIC-class software) that push results into FMCSA's SAFER and MCMIS databases and the carrier's SMS BASIC scores. Filled thresholds and worked calculations in `references/playbook.md`.

## Communication style

With the driver at roadside: the specific citation, the measured value against the published threshold, and a plain statement of disposition — "this axle is out of service, stroke measured at 2-1/4 inches against a 2-inch threshold for this chamber" — never a vague "this needs attention." With the carrier's safety office in a follow-up letter or dispute: the measurements and citations as recorded, with no narrative characterization of the carrier's overall maintenance practices beyond what this inspection's evidence supports. With a supervisor or a second inspector on a disputed or complex call: the specific criterion applied, the exact measurement, and which rule (individual threshold vs. aggregate rule) governed the disposition — not a request to validate a gut call.

## Common failure modes

- Marking a single brake pass/fail without running the 20%-of-brakes aggregate count across the whole vehicle, missing an OOS condition that only exists in aggregate.
- Estimating tread depth by eye or averaging groove readings instead of gauging the shallowest point.
- Clearing hazmat because the placard "looks plausible" without cross-checking the shipping paper's hazard class and the aggregate weight against the 1,001-lb Table 2 threshold.
- Downgrading an already-selected Level I to a faster level partway through once an easy pass looks likely, missing an underside defect that prompted the Level I selection in the first place.
- Confusing the 3-month CVSA decal with the 12-month DOT annual inspection sticker and waving a vehicle through on a decal that says nothing about annual-inspection currency.
- Overcorrecting after a missed defect on a prior shift: writing every borderline measurement as OOS regardless of the actual threshold, which inflates a carrier's BASIC percentile on a call that wouldn't survive a citation-and-number defense.

## Worked example

A five-axle tractor-semitrailer combination (steer axle, drive tandem, trailer tandem — 10 brake positions total: 2 steer, 4 drive, 4 trailer) is pulled into a Level I inspection lane. A Class 3 flammable-liquid placard is visible on the trailer, which is one of the risk signals that justified selecting Level I over a faster level given the 25-minute lane window.

**Brake exam (pushrod stroke, Type 30 long-stroke chambers, published OOS threshold 2.00 in at full application):**

| Position | Stroke reading (full application) | Threshold | Status |
|---|---|---|---|
| Steer L/R | 1.50 in / 1.50 in | 2.00 in | OK |
| Drive axle 1, L | 2.25 in | 2.00 in | **Defective** (2.25 − 2.00 = 0.25 in over) |
| Drive axle 1, R | 2.25 in | 2.00 in | **Defective** |
| Drive axle 2, L/R | 1.75 in / 1.75 in | 2.00 in | OK |
| Trailer axle 1, L | 2.125 in | 2.00 in | **Defective** (0.125 in over) |
| Trailer axle 1, R | 1.625 in | 2.00 in | OK |
| Trailer axle 2, L/R | 1.50 in / 1.625 in | 2.00 in | OK |

Defective brakes: 3 of 10 positions = 30%. 30% ≥ the CVSA 20%-brakes threshold, so the *combination* is OOS on the aggregate rule — independent of whether each individual defective brake alone would justify it.

**Tire exam:** steer-axle left tire tread measured at three points around the circumference: 5/32, 4/32, 3/32 in. Governing reading is the shallowest, 3/32 in, against a 4/32-in minimum for steer-axle tires (all other positions: 2/32 in minimum). 3/32 < 4/32 → **OOS on the steer tire**, a second, independent OOS condition.

**Hazmat check:** shipping paper lists 8 drums of Class 3 flammable liquid at 55 gal each = 440 gal; at approximately 7.2 lb/gal that's 440 × 7.2 = 3,168 lbs gross, well over the 1,001-lb Table 2 aggregate placarding threshold (49 CFR 172.504) — so placarding is required, and required as Class 3. The placard actually mounted on the trailer reads **Class 8 (Corrosive)**, left over from the prior load. Hazard class mismatch between placard and shipping paper is its **own OOS condition**, independent of both brake and tire findings.

**Naive read a generalist might produce:** "One brake position is a quarter-inch over on stroke, one tire is a little thin, and the placard is probably just an oversight — write up the brake and move the truck along with a warning on the tire and placard."

**Expert reasoning:** The 0.25-in overage on drive axle 1 is real, but it is not the governing finding — three separate brake positions across two axles are defective, which is 30% of the vehicle's total brake count, clearing the CVSA 20% aggregate threshold on its own regardless of any single reading. That makes the combination OOS for brakes as a whole, not "one bad brake plus two near-misses." The steer tire at 3/32 in is a second, fully independent OOS condition — steer tires carry the tighter 4/32-in minimum precisely because a steer-tire failure removes directional control, and this reading fails that standard regardless of the brake finding. Third, the placard mismatch is not a documentation oversight to be waved through with a mechanical pass: the shipping paper's 3,168-lb aggregate of Class 3 material clears the 1,001-lb threshold by more than 3x, Class 3 placarding is mandatory, and a Class 8 placard on a Class 3 load is a hazmat OOS violation that stands entirely on its own — a perfect brake and tire inspection would not clear it. All three findings are independently sufficient for OOS; none offsets or substitutes for another.

**Deliverable — Level I North American Standard Inspection Report, OOS Notice section:**

> **Inspection Level:** I (North American Standard) — Combination Unit, 5 axles / 10 brake positions.
> **Brake finding:** OOS — 3 of 10 brake positions defective (30%), exceeds CVSA 20% out-of-service threshold. Drive axle 1 L/R: pushrod stroke 2.25 in vs. 2.00 in threshold (Type 30 LS chamber). Trailer axle 1 L: 2.125 in vs. 2.00 in threshold. Citation: 49 CFR 393.47 / CVSA OOS Criteria, Brake Systems.
> **Tire finding:** OOS — Steer axle, left tire: tread 3/32 in at shallowest groove vs. 4/32 in minimum for steer position. Citation: 49 CFR 393.75(a).
> **Hazmat finding:** OOS — Placard displayed (Class 8, Corrosive) does not match shipping paper (Class 3, Flammable Liquid, aggregate 3,168 lbs, exceeds 1,001-lb Table 2 threshold). Correct placarding required: Class 3. Citation: 49 CFR 172.504 / 172.506.
> **Disposition:** Vehicle combination placed out of service on three independent grounds (brakes, steer tire, hazmat placarding). Any one alone is sufficient for OOS; correcting one does not clear the others. Vehicle may return to service only after all three conditions are corrected and reinspected on-site or at an approved facility, with corrected hazmat placarding verified before departure.
> **CVSA decal:** Not issued — decal requires a Level I pass with zero OOS violations.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when working brake pushrod stroke math, the 20%-brakes aggregate calculation, tire tread minimums, hazmat placarding thresholds, or selecting an inspection level under time constraints.
- [references/red-flags.md](references/red-flags.md) — load when a specific measurement, placard, or credential looks off and you need to know what it usually means.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in an inspection report or citation needs a precise definition.

## Sources

CVSA (Commercial Vehicle Safety Alliance) North American Standard Out-of-Service Criteria, revised annually and effective each April 1, covering brake adjustment, tire, and coupling-device OOS thresholds and the 20%-brakes aggregate rule; 49 CFR Part 393 (Parts and Accessories Necessary for Safe Operation), specifically §393.47 (brakes) and §393.75 (tires); 49 CFR Part 396 (Inspection, Repair, and Maintenance), specifically §396.17 (periodic/annual inspection, 12-month cycle) and §396.9 (inspection authority); 49 CFR Part 172, Subpart F (hazmat placarding requirements and the Table 1/Table 2 quantity thresholds, including the 1,001-lb aggregate trigger under §172.504); CVSA's International Roadcheck annual data releases and FMCSA's Compliance, Safety, Accountability (CSA) Safety Measurement System (SMS) BASICs methodology, including the Vehicle Maintenance BASIC. Specific readings in the worked example (stroke measurements, tread depths, drum counts) are constructed for reconciling arithmetic and are not a specific historical inspection — verify the current-edition OOS Criteria handbook's chamber-type stroke tables before issuing an actual finding, since thresholds are revised on a regular schedule.
