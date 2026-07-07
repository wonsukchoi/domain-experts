# Playbook

Filled reference material: the DTC systematic-diagnosis sequence, labor-guide time tables, ASE certification map, and a warranty-vs-customer-pay job-costing worksheet.

## 1. DTC systematic-diagnosis sequence (don't skip steps under time pressure)

| Step | Action | What it prevents |
|---|---|---|
| 1. Duplicate | Reproduce the complaint or confirm it's currently active before scanning. | Chasing a code with no matching symptom (may be a self-clearing pending code). |
| 2. Retrieve & record | Pull all codes; note pending / confirmed / history status and full freeze frame. Do **not** clear yet. | Losing the only record of conditions when the fault occurred. |
| 3. Research | Cross-reference code + VIN against OEM diagnostic tree and open TSBs (ALLDATA/Mitchell/OEM subscription). | Re-diagnosing a fault the manufacturer has already published a fix sequence for. |
| 4. Interpret live data | Pull the system-relevant live stream (fuel trims, voltage, pressure) and read sign/magnitude before hypothesizing. | Guessing the failed component from the code's plain-language name alone. |
| 5. Confirm | Run the specific test that proves the hypothesis (smoke test, voltage-drop test, bi-directional actuator command, pressure test). | Installing a part based on correlation instead of a confirmed fault. |
| 6. Repair | Replace/repair only the confirmed cause; log advisories separately. | Bundling unconfirmed parts into the billed repair. |
| 7. Verify | Clear codes only now; run OEM drive cycle or re-scan; confirm trims/monitors normal and no code return. | Releasing a vehicle where the original fault could still be present. |

**Fuel-trim read reference (idle, warmed engine):**

| LTFT at idle | Likely direction |
|---|---|
| −10% to +10% | Within normal range for the system. |
| Above ~+10%, sustained | Lean condition — check for vacuum leak, weak fuel pump, clogged injector, before treating as ignition. |
| Below ~−10%, sustained | Rich condition — check for leaking injector, high fuel pressure, contaminated MAF, before treating as ignition. |

## 2. Flat-rate labor-guide time reference (representative book-time ranges — confirm against the shop's actual Mitchell/Motor/ALLDATA subscription for the specific VIN before quoting)

| Job | Typical book time | Notes |
|---|---|---|
| Diagnostic — check engine light, single system | 1.0 hr | Shop's posted diagnostic flat fee; often credited toward the repair if authorized same visit. |
| Diagnostic — multi-code, cross-system (e.g., misfire + fuel trim) | 1.0–1.5 hr posted, frequently exceeds this in practice | Gap between posted and actual time is the flat-rate/diagnostic-quality tension. |
| Front brake pads + rotors, single axle | 1.0–1.4 hr | Varies with caliper bracket design and whether rotors are pressed-on vs. slide-off. |
| Alternator R&R | 0.7–1.8 hr | Wide range driven by accessory-belt routing and accessibility behind other components. |
| Water pump (belt-driven, external) | 1.5–2.5 hr | |
| Water pump (behind timing cover/chain) | 3.5–4.5 hr | Frequently bundled with a timing service since the cover is already off. |
| Timing chain/belt service | 3.0–8.0 hr | Interference-engine platforms at the high end; always confirm against interval mileage (commonly 60k–105k for belts) before recommending proactively. |
| Intake manifold gasket R&R (4-cyl, accessible) | 1.2–2.0 hr | Example used in SKILL.md worked example: 1.5 hr. |

## 3. ASE certification map (Automotive Service Excellence)

| Code | Category |
|---|---|
| A1 | Engine Repair |
| A2 | Automatic Transmission/Transaxle |
| A3 | Manual Drive Train & Axles |
| A4 | Suspension & Steering |
| A5 | Brakes |
| A6 | Electrical/Electronic Systems |
| A7 | Heating & Air Conditioning |
| A8 | Engine Performance |
| A9 | Light Vehicle Diesel Engines |
| L1 | Advanced Engine Performance Specialist (add-on, requires A8 first) |

**Master Automobile Technician** = A1–A8 passed. A9 and L1 are separate, not required for master status. A shop posting "ASE Certified" without naming the category is a documentation gap worth asking about — certification in A5 (Brakes) says nothing about competence in A6 (Electrical).

## 4. Warranty vs. customer-pay job-costing worksheet

Same repair, two different economics, on the same lift:

| | Customer-pay | Manufacturer warranty |
|---|---|---|
| Labor rate applied | Shop's posted door rate (e.g., $165/hr) | OEM warranty labor rate — historically set well below door rate; most states now require it be tied to the shop's own average customer-pay rate via a retail-reimbursement statute, recalculated periodically (commonly from a sample of the shop's last ~100 sequential customer-pay ROs). |
| Labor time source | Shop's labor guide (Mitchell/Motor/ALLDATA) | OEM's own warranty time standard, which can differ from the aftermarket labor guide's time for the identical job. |
| Parts markup | Shop's standard margin | OEM-set warranty parts markup, typically lower than the shop's standard customer-pay margin. |
| Diagnostic time | Billed per shop policy, may be waived if repair authorized | Often capped at a fixed OEM-allowed diagnostic time regardless of actual complexity — a mismatch that recreates the same time-pressure tension as customer-pay flat rate, but at a lower reimbursement rate. |

**Reconciling example:** intake manifold gasket job from the SKILL.md worked example, run as a warranty claim instead of customer-pay, assuming a warranty labor rate reimbursed at the shop's retail-reimbursement-statute rate of $148/hr (state-mandated average of the shop's last 100 customer-pay ROs) and OEM warranty parts markup instead of retail margin:

- Labor: 2.5 hr × $148/hr = $370.00 (vs. $412.50 customer-pay — a $42.50 gap on identical work).
- Parts: $115 at OEM warranty markup (assume 10% lower margin than retail) ≈ $103.50.
- **Warranty total reimbursed to shop: $473.50**, against a customer-pay-equivalent value of $527.50 — a $54 gap the shop absorbs as the cost of doing warranty work, which is exactly why a technician working a mixed warranty/customer-pay day is not earning the same effective rate on every job even when the labor hours flagged are identical.

## 5. Repair-order documentation checklist (every job, before release)

- [ ] All codes recorded with status (pending/confirmed/history) before any clearing.
- [ ] Freeze frame and relevant live-data values (trims, voltage, pressure) logged, not just the code number.
- [ ] Confirming test named and result stated (not just "diagnosed").
- [ ] Confirmed repair and any advisory findings on clearly separate lines, each with its own supporting data point.
- [ ] Labor source noted (customer-pay book time vs. warranty time standard) and rate applied.
- [ ] Post-repair verification method and result recorded (drive cycle, re-scan, trim values) before the vehicle is released.
