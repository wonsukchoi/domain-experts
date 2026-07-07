# Playbook

Filled reference tables and step sequences for the four recurring decisions: welder/procedure qualification, repair-vs-alteration classification, rolled-joint sizing, and post-repair hydrostatic testing.

## 1. Welding procedure and welder qualification — ASME Section IX chain

| Document | What it establishes | Who issues it | Re-qualification trigger |
|---|---|---|---|
| WPS (Welding Procedure Specification) | The parameters (process, filler metal, preheat, amperage range, position) a welder must follow | Employer, backed by a PQR | Revised when a variable outside the PQR's qualified range is needed |
| PQR (Procedure Qualification Record) | Proof the WPS parameters actually produce a sound weld, via mechanical test coupons | Employer, one-time test per WPS | Only if the WPS is changed beyond an established variable |
| WPQ (Welder Performance Qualification) | Proof a specific welder can execute a specific process/material/position combination | Employer, via test coupon per welder | Lapses after 6 months without use of that qualified combination (continuity) |

**Sequence, applied in order before assigning a pressure-boundary weld:**
1. Confirm a WPS exists covering the base metal P-number, thickness range, and welding process for this job — if not, a new PQR/WPS must be qualified before work starts.
2. Confirm the assigned welder's WPQ record covers that same P-number/thickness/position/process combination.
3. Check the welder's continuity log for last use of that combination — if it exceeds roughly 6 months, re-qualify or document a supervised continuity weld before assigning the job unsupervised.
4. Log the WPS number, PQR number, and welder's WPQ number against the job traveler — this is the paper trail an Authorized Inspector will ask for at final sign-off.

## 2. Repair vs. alteration classification (NBIC Part 3)

| Situation | Classification | Authorization needed |
|---|---|---|
| Cracked weld seam repaired to original joint design, same material, same thickness | Repair | "R" stamp scope covering repairs |
| Corroded tube replaced with same-spec tube, same row, same rolled-joint design | Repair | "R" stamp scope covering repairs |
| Tube replaced with a heavier-wall tube to address a chronic thinning problem | Alteration (thickness/design change) | "R" stamp scope covering alterations, or a design review by the original manufacturer/engineer |
| Nozzle added or MAWP re-rated upward | Alteration | "R" stamp scope covering alterations, plus a re-rating calculation |
| Patch plate welded over a corroded shell section, restoring original thickness | Repair (if thickness and material match original) | "R" stamp scope covering repairs |

**Rule:** if the fix changes anything the original manufacturer's data report specifies — material, thickness, configuration, design pressure/temperature — it is an alteration. If it restores the component to what that data report already describes, it is a repair. When in doubt, the Authorized Inspector makes the call before work starts, not after.

## 3. Rolled tube-joint expansion — target and verification

**Target:** 4–6% wall-thickness reduction from original wall thickness, verified by direct measurement (ID gauge or drift pin), not by expander torque or turn-count alone.

| Tube OD | Original wall (BWG) | Original ID | 4% reduction → new wall / ID | 6% reduction → new wall / ID |
|---|---|---|---|---|
| 2.0 in | 0.120 in (BWG 11) | 1.760 in | 0.1152 in / 1.7696 in | 0.1128 in / 1.7744 in |
| 2.5 in | 0.105 in (BWG 12) | 2.290 in | 0.1008 in / 2.2984 in | 0.0987 in / 2.3026 in |
| 3.0 in | 0.134 in (BWG 10) | 2.732 in | 0.1286 in / 2.7428 in | 0.1260 in / 2.7480 in |

**Step sequence:**
1. Measure and record the tube's actual original wall thickness before rolling (mill tolerance means it may not match the nominal BWG figure exactly).
2. Calculate the target new wall thickness at 4% and 6% reduction, giving an acceptable ID range rather than a single point value.
3. Roll incrementally, checking ID with a drift pin or gauge at each pass rather than committing to a fixed number of expander turns.
4. Stop when the measured ID falls inside the calculated 4–6% range; do not continue rolling "for good measure" — every additional pass past 6% risks work-hardening the tube end past its ductility.
5. Record the final measured wall reduction per joint on the job traveler — this is the data that identifies an under- or over-rolled joint if it leaks later.

**Failure signature by direction:**
- **Under-rolled (<4%):** joint weeps under thermal cycling as the tube and drum ligament expand/contract at different rates; leak typically appears within the first several months of service, worse during load-following operation.
- **Over-rolled (>6%):** tube wall thinned and work-hardened at the joint; cracks initiate at the tube end (often visible as a circumferential crack just inside the drum ligament), sometimes not leaking until months later when thermal-cycling fatigue reaches the hardened zone.

## 4. Post-repair hydrostatic test

| Repair type | Test pressure | Minimum hold time | Who witnesses |
|---|---|---|---|
| Welded pressure-boundary repair | 1.5 × MAWP | 30 minutes at test pressure, full walk-down of repaired joints | Authorized Inspector |
| Rolled-joint reroll (no welding) | 1.5 × MAWP (unless owner/jurisdiction accepts a reduced test per NBIC provisions for joint-only work) | 10–30 minutes, sufficient to walk every rerolled joint under pressure | Authorized Inspector or owner-user inspector per jurisdiction |
| Alteration | 1.5 × new MAWP (post-alteration design basis) | 30 minutes minimum | Authorized Inspector, plus design review sign-off |

**Sequence:**
1. Confirm the test pressure is calculated against MAWP, not against the boiler's normal operating pressure — operating pressure is always lower and understates the test.
2. Bring the vessel to test pressure gradually, watching for pressure loss that indicates a leak before reaching full test pressure.
3. Hold at full test pressure for the full required time, walking every repaired or rerolled joint — a leak that only appears at minute 25 of a 30-minute hold is exactly what the hold time is for.
4. Depressurize gradually and document the result (pass/fail, any weeping location) on the "R" report before the vessel returns to service.
5. If any joint weeps during the hold, do not "snug it down" under pressure — depressurize fully, re-diagnose (under-roll, over-roll, or weld defect), and repeat the repair and test from the failed step forward.
