# Playbook

Filled test sequences and thresholds for periodic testing, governor/buffer verification, and modernization cutover. Numbers below are worked from the ASME A17.1/CSA B44 rule structure described in `SKILL.md`'s Sources — always confirm against the code edition adopted by the local AHJ before treating a figure as the enforceable number at a given site.

## Periodic test category matrix

| Category | Interval | Load condition | What it verifies | Who witnesses |
|---|---|---|---|---|
| Category 1 | Annual | No load (empty car) | Safety-circuit logic: door interlocks, restrictors, governor overspeed switch continuity, final limits, brake set/lift, pit stop switch, car-top inspection station | Mechanic; QEI witness required in most jurisdictions |
| Category 3 | Varies by AHJ (commonly every 3–5 yrs, jurisdiction-dependent) | No load | Traction/rope-related checks not covered by Cat 1 or Cat 5 (varies by code edition — confirm locally) | QEI witness |
| Category 5 | Every 5 years | Full load: 100% rated capacity for car-safety drop, 125% for buffer strike per current edition — verify against adopted edition | Full mechanical load test: car safety, counterweight safety, governor trip under load, buffer strike at governor tripping speed | QEI witness required |

**Rule of sequencing:** if a Category 5 falls due on the same visit as the annual Category 1, run Category 1 items first (they gate whether it's even safe to load the car for Category 5). Never skip Category 1 items because "we're doing the bigger test anyway" — they test different failure modes.

## Governor overspeed test — step sequence

1. Confirm car's nameplate rated speed and pull the code table's tripping-speed band for that speed class (commonly 100–110% of rated for mid-speed cars; band narrows at higher rated speeds — read the actual table, don't assume).
2. Run car under controlled overspeed condition (test mode) until governor trips the safety linkage.
3. Read tripped speed off the calibrated tachometer, not the controller's displayed speed (controller display can lag or smooth the reading).
4. Compute percent of rated: `tripped speed ÷ rated speed × 100`.
5. Compare against the code band. Outside the band (either direction) → governor fails; do not field-adjust the trip point without manufacturer procedure and re-verification against the code table.
6. Record: rated speed, tripped speed, computed %, pass/fail, tachometer serial/calibration date.

**Example (from SKILL.md worked example):** rated 350 fpm, tripped 372 fpm → 106.3%, inside 100–110% band, pass.

## Buffer strike test — step sequence (Category 5)

1. Load car to the code-specified full-load test weight for the buffer test (verify current percentage — commonly cited at up to 125% of rated capacity; confirm the adopted edition's figure).
2. Determine governor tripping speed from the governor test above (use the measured value, not nameplate rated speed).
3. Convert tripping speed from fpm to ft/s: `fpm ÷ 60`.
4. Compute minimum required stroke at the 1g average-retardation ceiling: `d (ft) = v² ÷ (2 × 32.2)`.
5. Convert to inches (`× 12`) and compare against installed buffer's nameplate stroke.
6. Run the strike; measure actual stroke used and back-calculate actual average retardation: `a = v² ÷ (2 × d_actual)`.
7. Pass condition: measured average retardation ≤ 1g, with momentary peak retardation not exceeding roughly 2.5g for more than a fraction of a second (per the code's buffer rule) — a stop that "felt hard" but measures inside this window is still a pass; a stop that "felt fine" but measures outside it is still a fail.

| Item | Formula | Worked value (372 fpm trip, 9.0 in buffer) |
|---|---|---|
| Speed in ft/s | fpm ÷ 60 | 6.2 ft/s |
| Minimum required stroke | v² ÷ (2 × 32.2), then × 12 | 7.2 in |
| Installed stroke | nameplate | 9.0 in |
| Actual average retardation | v² ÷ (2 × d_actual) | 25.6 ft/s² ≈ 0.80g |
| Margin | (required stroke − installed) shortfall, or retardation vs. 1g ceiling | ~20% below the 1g ceiling |

## Door interlock / restrictor verification

1. **Interlock check:** with car at floor, doors closed and locked — attempt to move car with door circuit open (test mode). Car must not move. Any movement = immediate out-of-service.
2. **Restrictor check:** stop car mid-hoistway, outside the unlocking zone (commonly ~18 in / 450 mm above/below a landing — confirm the adopted edition's zone dimension). Apply a calibrated pry-test gauge to the hoistway door.
3. Record maximum manual opening distance achieved before the restrictor stops further travel. Compare against the code's maximum permitted opening outside the unlocking zone (commonly cited around 4 in / 100 mm — confirm locally).
4. Pass condition: restrictor stops opening at or below the threshold. A restrictor that lets the door past the threshold fails **even if the interlock circuit tested correctly** — they are independent devices covering independent failure paths.
5. Repeat at both directions of travel (door outside zone above and below nearest landing) if hoistway geometry allows movement in both directions from the test point.

## Safety-circuit continuity map (for troubleshooting)

Series order commonly encountered (verify actual wiring against the unit's as-built schematic — order and device set vary by installation and controller vintage):

1. Hoistway door interlocks (each landing)
2. Car door interlock/gate switch
3. Car door restrictor supervisory contact (where fitted)
4. Governor overspeed switch
5. Car safety operated switch
6. Final (terminal) limit switches
7. Pit stop switch
8. Car-top inspection station stop switch
9. Buffer switches (where fitted with a switch, e.g. oil buffers)

**Troubleshooting rule:** an intermittent "safety circuit open" fault with no drive-side fault code means one of the above opened and reclosed faster than the controller logged which one — check for the marginal contact (commonly a door lock or interlock reacting to thermal expansion or vibration) before assuming a governor or buffer problem.

## Escalator step-chain / comb-clearance check

1. Measure step-chain elongation with the manufacturer's gauge at the tensioning device; compare against the take-up device's remaining travel.
2. Record the measurement (not "OK") in the maintenance log with date, so elongation rate over 6–12 months is visible on the next visit.
3. Measure comb-to-step clearance at both combs (top and bottom landing) with a feeler gauge; compare against the code's maximum permitted clearance.
4. If elongation is within ~10% of the take-up device's remaining travel, or comb clearance is within ~10% of the code maximum, flag for near-term (not emergency) replacement/adjustment scheduling rather than waiting for an out-of-tolerance reading to force an emergency shutdown.

## Modernization cutover checklist (new controller, reused mechanical devices)

1. Re-verify governor tripping speed against the new controller's actual overshoot behavior — do not assume the governor's prior calibration still matches a different drive's speed curve.
2. Re-verify buffer stroke against the new controller's rated speed and any speed changes made during modernization (a modernization that increases rated speed requires the buffer stroke and governor trip band to be re-checked against the higher speed, not carried over from the old rating).
3. Confirm door restrictor and interlock wiring maps to the new controller's safety-circuit input the same way it did on the old controller — a rewiring error here is a common source of "circuit tests fine, restrictor doesn't actually gate car movement" defects.
4. Run a full Category 1 sequence before returning to normal service, even though the unit hasn't reached its annual date, since the controller and wiring changed.
5. File the modernization's re-test results as a new baseline in the maintenance record — don't merge them into the prior controller's test history.
