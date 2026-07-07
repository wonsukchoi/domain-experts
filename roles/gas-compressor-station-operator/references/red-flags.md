# Red flags

Smell tests a senior compressor station operator catches on the first pass through a shift log, a trend screen, or a compliance calendar. Format for each: what it usually means, the first question to ask, and the data to pull before committing to a response.

## 1. Discharge pressure is compliant but a cooler fan is confirmed down or fouled

**Usually means:** discharge temperature has climbed well past the pipe-coating/tariff limit (commonly ~140°F/60°C) even though pressure monitoring shows nothing wrong — cooling loss is a temperature problem, not a pressure problem, and pressure gauges won't catch it.

**First question:** "What's current discharge temperature relative to the coating limit, not just relative to MAOP?"

**Data to pull:** discharge/interstage temperature trend since the fan went down, cooler fan run-status log, ambient temperature at the time.

## 2. Discharge temperature above ~140°F/60°C at the pipeline tie-in point

**Usually means:** aftercooler capacity loss, fouled cooler tubes/fins, high ambient temperature beyond design basis, or a compression ratio pushed higher than the cooling system was sized for.

**First question:** "Is this a cooling-capacity problem or a compression-ratio problem — has suction pressure or discharge target changed recently?"

**Data to pull:** cooler fan/tube fouling inspection record, discharge temperature trend, suction pressure/temperature trend, current compression ratio versus design ratio.

## 3. Relief valve set point is at or below the ESD high-pressure trip point

**Usually means:** the two independent overpressure-protection layers have been collapsed into one — the ESD is supposed to act before the relief valve ever needs to lift, and this ordering defeats that design intent.

**First question:** "What's the ESD trip set point relative to the relief valve set point, and relative to MAOP?"

**Data to pull:** ESD trip configuration record, relief valve set-point certification, MAOP determination for the segment.

## 4. Odorant sampling is performed only near the injection point

**Usually means:** the sampling program is verifying odorant is present at the source, not that it's still detectable at the far, most-dilute end of the system where a leak actually needs to be smelled.

**First question:** "Where's the sampling point relative to the injection point and the system's farthest reach?"

**Data to pull:** odorization sampling location log, system map showing injection point and test points, most recent far-point sample result.

## 5. Odorant concentration below the 1/5-LEL detectability threshold at any test point

**Usually means:** under-dosing at the injector, odorant fade/absorption over distance (common in new steel or through certain soils), or a failed odorant injection pump — any of which leaves gas that won't be smelled at a real leak.

**First question:** "Has the injection rate and pump function been verified independently of the test-point reading itself?"

**Data to pull:** odorant injection rate log, pump maintenance record, sample concentration result and test-point distance from injector.

## 6. A PHMSA §192.739/§192.743 test is due within 30 days of the 15-month deadline with no test scheduled

**Usually means:** the interval is being tracked reactively against the hard deadline instead of proactively, leaving no time to repair and retest if the device fails on first attempt.

**First question:** "When exactly is the test scheduled, and is there float built in to retest if it fails?"

**Data to pull:** PHMSA compliance tracking log, last test date and result, current scheduling window.

## 7. Discharge pressure setpoint is routinely run within 1–2% of MAOP

**Usually means:** normal control variation (load swings, ambient effects) will periodically breach MAOP or force an ESD trip, when a wider working margin would absorb the same variation without an event.

**First question:** "Why is the setpoint this close to MAOP — is there a throughput reason, or has margin just eroded over time?"

**Data to pull:** discharge pressure trend over the last operating cycle, ESD trip history, setpoint change log.

## 8. ESD/blowdown functional test is overdue against the station's O&M schedule

**Usually means:** the emergency isolation and depressurization path hasn't been proven to work since the last test — a station relying on an untested ESD/blowdown path in a real event is relying on an assumption, not a verified system.

**First question:** "When was the ESD/blowdown sequence last functionally tested, start to finish, not just visually inspected?"

**Data to pull:** O&M plan test schedule, last functional test record and any deficiencies noted, current test status.

## 9. Repeated high-temperature trips are cleared by reset without a cooling-system check

**Usually means:** the crew is treating the trip as a nuisance alarm rather than investigating cooler fan status, fouling, or a suction-condition shift — the trip will keep recurring, likely at a worse point in the cycle, until the actual cause is found.

**First question:** "Has cooler fan run-status and suction trend been checked for each of these trips, or has each one just been reset?"

**Data to pull:** trip/alarm history with timestamps, cooler fan run-status log for the same windows, suction pressure/temperature trend.

## 10. Suction pressure or temperature has crept up without a matching review of cooling duty

**Usually means:** a higher suction condition raises the compression ratio's resulting discharge temperature even at an unchanged discharge target, and the cooling system sized for the old suction condition may no longer have margin.

**First question:** "Has the discharge-temperature calculation been rerun against the current suction condition, or is the cooling system still assumed adequate from when it was sized?"

**Data to pull:** suction pressure/temperature trend over the review period, original cooling-system design basis, current discharge temperature trend.
