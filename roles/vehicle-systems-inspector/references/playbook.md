# Vehicle Systems Inspector — Playbook

## Brake pushrod stroke — out-of-service thresholds by chamber type (illustrative, per CVSA OOS Criteria)

| Chamber type/size | Stroke at which brake is "out of adjustment" (OOS) |
|---|---|
| Type 9 | 1.375 in |
| Type 12 | 1.375 in |
| Type 16 | 1.50 in |
| Type 20 | 1.75 in |
| Type 24 | 1.75 in |
| Type 30 (standard stroke) | 1.75 in |
| Type 30 (long stroke) | 2.00 in |
| Type 36 (long stroke) | 2.25 in |

**Use:** Stroke is measured with the brake fully applied (90–100 psi service application), never at rest — an unapplied chamber reads short and produces a false clear. Always confirm the chamber's stamped type/size before reading the table; a Type 30 standard-stroke and Type 30 long-stroke chamber have different thresholds and are easy to conflate at a glance.

## 20%-brakes aggregate rule — worked calculation

| Step | Value |
|---|---|
| Total brake positions on vehicle/combination | 10 (2 steer + 4 drive + 4 trailer) |
| Defective positions found (stroke over threshold, out of adjustment, or non-functional) | 3 |
| Percentage defective | 3 / 10 = 30% |
| CVSA threshold | 20% |
| **Result** | OOS — 30% exceeds the 20% aggregate threshold, independent of how severe any single brake's overage is. |

**Use:** Count every brake position on the entire vehicle or combination, not per-axle. A straight truck with 2 axles (4 brakes) crosses the rule at 1 defective brake (25%); a 5-axle combination (10 brakes) crosses it at 2 (20%). Compute the aggregate even when only one brake initially looks bad — the vehicle can still be OOS in aggregate with three individually-marginal readings that would each pass alone.

## Tire tread depth — OOS minimums

| Axle position | Minimum tread depth (any groove) | Governing reading |
|---|---|---|
| Steer axle | 4/32 in | Shallowest of at least 3 points measured around the circumference |
| All other axles (drive, trailer) | 2/32 in | Shallowest of at least 3 points measured around the circumference |

**Use:** Report the shallowest reading, not an average. A tire reading 5/32, 4/32, 3/32 in across three points on a steer axle is OOS at 3/32 in even though two of the three readings pass — irregular wear from misalignment routinely produces exactly this spread.

## Hazmat placarding threshold check (per 49 CFR 172.504, Subpart F)

| Question | If yes | If no |
|---|---|---|
| Is the material a Table 1 hazard class (e.g., certain explosives, poison gas, highway route-controlled radioactive)? | Placard required at **any quantity** | Continue to aggregate-weight check |
| Is the aggregate gross weight of all Table 2 materials of that hazard class aboard ≥ 1,001 lbs? | Placard required for that hazard class | No placard required for that class at this weight |
| Does the placard actually mounted on the vehicle match the hazard class the shipping paper and weight calculation require? | Compliant — no hazmat OOS on placarding | **OOS** — placard/shipping-paper mismatch, independent of vehicle mechanical condition |

**Worked example:** 8 drums × 55 gal Class 3 flammable liquid = 440 gal × ~7.2 lb/gal ≈ 3,168 lbs. 3,168 ≥ 1,001-lb Table 2 threshold → Class 3 placard required. Vehicle displays Class 8 → mismatch → OOS on hazmat, regardless of brake/tire findings.

**Use:** Always sum the aggregate weight across every package of the same hazard class on the shipping paper — a shipper who calculates against a single container's weight instead of the aggregate is the most common source of an under-placarded load.

## Inspection-level selection matrix (time/resource triage)

| Level | Scope | Choose when |
|---|---|---|
| Level I — North American Standard | Full driver + vehicle exam, including underneath (brakes, steering, coupling) | Hazmat placard visible, carrier's Vehicle Maintenance BASIC percentile elevated, an obvious defect visible from ground level, or time budget allows the full 20–40 min average |
| Level II — Walk-Around Driver/Vehicle | Driver exam + vehicle exam of accessible components, no underneath | Time allows a full walk-around but the lane can't support going underneath; no elevated risk signal present |
| Level III — Driver-Only | Credentials, hours-of-service, medical certificate only | Only driver compliance is in question, or lane time is limited to a few minutes per truck |
| Level V — Vehicle-Only | Full vehicle exam, no driver present (e.g., at a terminal) | Vehicle is being inspected without its driver, such as a terminal or post-crash inspection |
| Level VI — Enhanced NAS Level I | Level I plus radiological/enhanced hazmat verification | Highway route-controlled quantity radioactive material aboard |

**Use:** Select the level before approaching the vehicle, based on what's visible or knowable from outside it (placard, carrier history if queryable, obvious defect). Never downgrade a level already selected once underneath — a Level I begun on a hazmat-placard risk signal stays a Level I even if the first few checks look clean.

## CVSA decal vs. DOT annual inspection — what each actually certifies

| Credential | Basis | Validity | What it does NOT certify |
|---|---|---|---|
| CVSA decal | A Level I (or Level V equivalent) inspection with **zero** OOS violations | 3 months from inspection date | Does not certify the vehicle passed its 12-month DOT annual inspection — a separate requirement |
| DOT annual inspection sticker | 49 CFR 396.17 periodic inspection by a qualified inspector | 12 months from inspection date | Does not exempt the vehicle from roadside OOS findings on that day — a vehicle can be current on its annual and still be placed OOS at a subsequent roadside stop |

**Use:** These are two different credentials on two different cycles issued for two different reasons. A driver presenting a current CVSA decal is not evidence the annual inspection is current, and vice versa — check both dates independently.
