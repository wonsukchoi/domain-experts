# Red flags

Smell tests a signal maintainer catches before signing a test record or releasing a location back to service. Each entry: what it usually means, the first question a veteran asks, and the data to pull before proceeding.

### Shunting-sensitivity test only run at the signal case, not mid-circuit or at the far end

**Usually means:** the discrete pass/fail result is real but incomplete — a leakage path that only matters at distance from the feed point (fouled ballast, a bad bond wire near the far joint) won't show up in a near-end-only test.
**First question:** "Where along this circuit was the 0.06-ohm shunt actually applied, and when was ballast resistance last measured at the far end?"
**Data to pull:** the test record's shunt-application location(s), the section's ballast resistance history, and any recent track work (surfacing, rail renewal) that could have disturbed bonding.

### Intermittent failure-to-shunt report dismissed as a relay contact issue without a ballast resistance check

**Usually means:** the leakage-path explanation (ballast fouling competing with the train's wheel-axle shunt) fits an intermittent symptom better than a hardware defect, which tends to fail consistently once it fails.
**First question:** "What's the shunt-to-ballast-leakage ratio at this location today, not six months ago?"
**Data to pull:** current portable ballast resistance measurement, the design-minimum comparison, and the date of the last formal ballast resistance test.

### Switch point flat spot measured just under the 5/16-inch threshold and rounded down

**Usually means:** the measurement is being read generously to avoid an immediate out-of-service call — a measurement within a few thousandths of the threshold should be treated as a re-measurement trigger, not a comfortable pass.
**First question:** "Who took this measurement, with what gauge, and would it read the same on a second measurement?"
**Data to pull:** the raw measurement with tool identification, and the point's wear trend from the last two inspection cycles.

### Switch throws and locks normally but point-to-stock-rail fit hasn't been separately checked

**Usually means:** throw-and-lock function and point geometry are being treated as one check when they're independent failure modes — a switch can operate correctly and still have a point a wheel flange can pick.
**First question:** "When was the point-to-rail fit itself last measured, separate from the throw-and-lock test?"
**Data to pull:** the switch's mechanical test record specifically for point fit (not just circuit controller/lock test), and the flange-contact-angle gauge reading.

### Vital relay's construction type not recorded, defaulting to the longest test interval

**Usually means:** whoever logged the relay assumed the 4-year default applied without confirming it isn't an AC centrifugal, AC vane, DC polar, or soft-iron-structure type — each of which requires a shorter interval.
**First question:** "What's this relay's actual nameplate construction type, and is that documented anywhere besides this test record?"
**Data to pull:** the relay's nameplate/manufacturer data, the interlocking's relay inventory, and the last test date under whichever interval was assumed.

### A vital circuit was jumpered to isolate a fault before alternative protection was confirmed in effect

**Usually means:** troubleshooting urgency overrode the sequencing rule — protection first, then defeat the circuit — which is the most cited procedural root cause in signal-related close calls.
**First question:** "What protection was in place, confirmed how, before this circuit was defeated?"
**Data to pull:** the job briefing or track warrant/flagging record time-stamped against the time the circuit was actually jumpered.

### Switch heater didn't activate during a cold, precipitating event and the ticket was logged as routine

**Usually means:** a heater failure during active snow/ice is a mechanical fail-open risk (points can't fully close) that no amount of correct track-circuit logic downstream can compensate for.
**First question:** "Can this switch physically achieve full point closure right now, checked in person, not inferred from the heater controller's status light?"
**Data to pull:** current ambient temperature and precipitation status, heater controller activation log, and an in-person point-closure check.

### PTC wayside interface unit reports the location as healthy and that's treated as the vital test

**Usually means:** PTC telemetry reflects what the WIU can see and report, which is not the same as an independent 236.56 shunting-sensitivity test or switch-point geometry check having actually been run.
**First question:** "When was this location's own vital test last run, separate from what PTC status shows?"
**Data to pull:** the location's 236.56 test record and switch-point inspection record, compared against the PTC WIU's last reported status timestamp.

### Test record shows "passed" with no numeric value logged

**Usually means:** the test was likely run correctly but documented in a way that erases the margin information a trend analysis or incident investigation would need — a shunt test that passed at 0.058 ohms effective and one that passed with wide headroom look identical as a bare "pass."
**First question:** "What was the actual measured value, not just the pass/fail outcome?"
**Data to pull:** the raw test instrument reading, if the instrument logs it, or a re-test with the numeric value recorded this time.
