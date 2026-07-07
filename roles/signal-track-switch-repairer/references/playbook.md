# Playbook

Filled worksheets for the three tests that gate whether a location is actually fail-safe: shunting-sensitivity testing, switch-point geometry inspection, and vital-relay/interlocking-logic test-interval tracking. Numbers below are the cited regulatory thresholds and industry design conventions, not a substitute for a specific carrier's approved test procedure or a signal engineer's circuit design — those always control over this worksheet.

## 1. Track circuit shunting-sensitivity test (49 CFR 236.56)

**Requirement:** with the track circuit dry, a 0.06-ohm resistive shunt applied across the rails (including fouling sections of turnouts) must drop the track relay to de-energized, or the device functioning as a track relay to its most restrictive state — at any point in the circuit, not only near the signal case.

**Test sequence:**
1. Confirm the track circuit is dry (recent rain or wash-down can transiently mask a real degradation — note weather conditions on the test record).
2. Apply the calibrated 0.06-ohm shunt at the near end of the circuit (closest to the signal case); confirm the relay drops.
3. Move the shunt to the mid-point of the circuit; confirm the relay drops. This step is the one most often skipped, and it's the one that catches a leakage path that only matters at distance from the feed point.
4. Move the shunt to the far end of the circuit (including any turnout fouling section); confirm the relay drops.
5. Record the ballast condition (dry/wet, visible fouling) and the last ballast-resistance measurement date alongside the pass/fail result — a "pass" with no ballast context is an incomplete record.

**Ballast resistance context (industry design convention, not itself a CFR figure):** a commonly used design minimum for reliable DC track circuit operation is 2 ohms per 1,000 feet of track. Parallel ballast leakage resistance for a section of length *L* (in thousands of feet) combines approximately as (design value per 1,000 ft) ÷ *L*.

**Worked example — margin check, not just pass/fail.** Section length 4,000 ft (*L* = 4).
- Design-minimum total ballast leakage resistance: 2 ÷ 4 = 0.5 ohms.
- Field-measured total (fouled with coal dust): 0.4 ohms/1,000 ft ÷ 4 = 0.1 ohms measured total.
- Shunt-to-leakage ratio at design minimum: 0.06 ÷ 0.5 = 0.12 (shunt dominates — wide margin).
- Shunt-to-leakage ratio at measured condition: 0.06 ÷ 0.1 = 0.6 (shunt and leakage are the same order of magnitude — margin has collapsed even though the last discrete 0.06-ohm test at the signal case still passed).
- Decision rule: if the shunt-to-leakage ratio exceeds roughly 0.3–0.4 at any point tested, treat the section as a candidate for ballast cleaning or renewal before the next scheduled interval, regardless of whether the discrete pass/fail test still passes today.

## 2. Switch-point geometry inspection (49 CFR 213.135 fit requirement, field-applied thresholds)

**Thresholds:**
| Condition measured | Threshold | Action |
|---|---|---|
| Flat/worn spot on switch point, width at 3/4 in. below top of rail | ≥ 5/16 in. | Remove from service immediately |
| Blunt face on point, width along closed stock rail | ≥ 3/16 in. | Schedule repair before next train |
| Flange-contact angle (60° gauge) | Contact below the gauge's marked line ("in the red") | Fails — treat as wheel-climb risk, same urgency as the flat-spot threshold |

**Inspection sequence:**
1. Close the switch normally (not by hand-forcing) and confirm full point-to-stock-rail contact along the closing length.
2. Apply a straightedge and feeler gauge at the location 3/4 inch below the top of rail; measure any flat or worn spot width against the 5/16-inch threshold.
3. Measure blunt-face width along the stock rail against the 3/16-inch threshold independent of the flat-spot measurement — a point can fail one threshold without failing the other.
4. Apply the 60-degree flange-contact-angle gauge at the point of switch; if contact reads below the marked line, treat as failing regardless of the two width measurements, since this gauge directly assesses wheel-climb geometry rather than point wear.
5. Confirm throw-and-lock function separately — a point that passes all three geometry checks can still fail if the connecting rod has excessive lost motion; these are independent failure modes and both must be checked.

**Worked example.** A switch point inspection at MP 118.6 measures a flat spot 0.31 inch wide (just under the 5/16-inch = 0.3125-inch threshold) at 3/4-inch depth, and a blunt face of 0.22 inch (above the 3/16-inch = 0.1875-inch threshold). The flat-spot measurement passes by 0.0025 inch — close enough that it should be re-measured, not rounded generously — but the blunt-face measurement fails independently. Action: schedule repair before the next train regardless of the flat-spot result, since the blunt-face threshold failed on its own; re-measure the flat spot at the next inspection cycle rather than treating today's narrow pass as settled.

## 3. Vital-relay and interlocking-logic test-interval tracking (49 CFR 236.106, 236.109)

| Component type | Test interval |
|---|---|
| Vital relay, unspecified/default construction | 4 years |
| AC centrifugal-type relay | 12 months |
| AC vane-type or DC polar-type relay | 2 years |
| Relay with soft-iron magnetic structure | 2 years |
| Time releases, timing relays, timing devices | 12 months |
| Mechanical locking, approach locking, time locking, route locking | 2 years (or immediately on new installation or any change to the locking) |

**Worked example — building a test schedule for a small interlocking.** An interlocking has 14 relays: 2 AC centrifugal (12-month), 5 AC vane-type (2-year), 3 soft-iron-structure (2-year), and 4 unspecified/general-purpose (4-year default), plus mechanical route locking (2-year) and 2 timing relays (12-month). A maintainer building the annual test plan cannot use one interval for the whole location: year 1 requires testing the 2 AC centrifugal relays and the 2 timing relays (4 components); year 2 requires testing the 5 AC vane, 3 soft-iron, and the route locking (9 components) in addition to that year's centrifugal/timing retest; year 4 additionally requires the 4 unspecified-type relays. Missing the distinction and testing everything on a single 2-year cycle would under-test the centrifugal relays and timing devices (due at 12 months) and over-test the 4-year-default relays two years early — the second error wastes test hours, the first is a compliance and safety gap.
