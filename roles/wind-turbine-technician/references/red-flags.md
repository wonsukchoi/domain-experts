# Red flags

Smell tests a senior technician catches before signing off on a climb or a maintenance call. Format for each: what it usually means, the first question to ask, and the data to pull.

## 1. Rescue plan hasn't been validated for this specific tower/crew/weather today

**Usually means:** the plan on file is a generic fleet-wide document, or was validated for a different crew composition or a different tower's anchor layout than what's present right now.

**First question:** "Walk me through exactly how we'd reach a suspended worker at the highest point on *this* tower, with the crew standing here right now."

**Data to pull:** the tower-specific rescue plan document, today's crew roster against the plan's assumed headcount, and the descender/rescue-device inspection tag date.

## 2. Iron or copper ppm doubles between two consecutive oil samples, even under the caution threshold

**Usually means:** an accelerating bearing spall or gear-tooth wear event that hasn't yet crossed an absolute threshold — the rate of change is the earlier signal, and waiting for the absolute critical line risks catching it after metal-to-metal contact has already propagated.

**First question:** "What were the prior two samples for this element, not just this one?"

**Data to pull:** the last three quarterly oil-analysis reports for the specific gearbox, load conditions at each sampling, and any corresponding SCADA vibration trend for the same component.

## 3. Vibration alarm on a single sensor/single axis with no harmonic match

**Usually means:** sensor drift, a mounting fault, or an electrical-noise artifact rather than a mechanical fault — genuine drivetrain faults typically show up at a gear-mesh or shaft-order harmonic and often corroborate across more than one sensor.

**First question:** "Is the alarm sitting at a known gear-mesh or shaft-order frequency, or somewhere arbitrary?"

**Data to pull:** the vibration spectrum (not just the alarm flag), sensor mounting/calibration log, and whether a second sensor on the same shaft shows any elevation.

## 4. Forecast wind at hub height sits just under the access-limit threshold with high gust variability

**Usually means:** the sustained-average number looks acceptable, but gust variance — which is what actually complicates a mid-tower rescue — is the harder hazard, and an average-only read understates the risk.

**First question:** "What's the gust spread, not just the sustained average, for the work window?"

**Data to pull:** hub-height wind forecast including gust range, site-specific access-limit policy, and time-of-day trend (many sites see gust variance rise in the afternoon).

## 5. Blade-root or tower-flange bolt check is overdue past the OEM-specified interval

**Usually means:** either a missed PM cycle or an OEM interval that was never loaded into the site's maintenance-management system correctly — both are common, and neither is a reason to defer further.

**First question:** "When was this joint last checked, and against which OEM document's interval?"

**Data to pull:** the OEM torque/tension procedure and interval for this specific bolt class and turbine model, the maintenance-management system's last-check date, and the fastener's lubrication/reuse history if available.

## 6. Anchorage strength or rating hasn't been verified for the fall-arrest system currently in use

**Usually means:** the anchor point is either OEM-certified for a different device than what's being used today, or was never formally rated at all — a routine gap on older platforms retrofitted with newer fall-arrest equipment.

**First question:** "Is this anchor certified for the specific system we're clipping into today, or are we assuming it because it's rated for something?"

**Data to pull:** the anchor's certification documentation (or, absent that, a qualified person's engineering sign-off that it sustains twice the maximum arrest force at a safety factor of at least 2 per OSHA 1910.140(c)(13)).

## 7. Nacelle or hub atmosphere untested, but not formally treated as a permit-required confined space

**Usually means:** the platform predates current confined-space classification practice, or the manufacturer's documentation never formally addressed it — the regulatory classification lagging the actual hazard is common on older turbine models.

**First question:** "Has the atmosphere actually been tested, or are we assuming it's fine because the paperwork doesn't call it confined space?"

**Data to pull:** the manufacturer's confined-space classification (if any), the site's permit-required confined-space list, and the atmospheric test log for this specific entry.

## 8. Down-conductor resistance reading above spec after a suspected lightning strike

**Usually means:** receptor damage or a degraded bond path in the lightning-protection system that, left unaddressed, both increases the chance of internal arcing on the next strike and can leave residual charge paths that standard electrical LOTO doesn't anticipate.

**First question:** "What's the down-conductor resistance reading against the OEM's spec value, and has the receptor been visually inspected for burn damage?"

**Data to pull:** IEC 61400-24-referenced resistance test results, receptor inspection photos, and the turbine's strike-count log (many SCADA systems log suspected strikes automatically).

## 9. Gearbox oil or bearing temperature climbing over consecutive SCADA intervals at constant load

**Usually means:** a developing lubrication or bearing-friction problem — but only once load is normalized, since temperature naturally tracks output and a raw temperature rise during a high-wind period can be a false trend.

**First question:** "Is this temperature rise happening at the same load as the baseline readings, or are we comparing different operating points?"

**Data to pull:** load-normalized temperature trend over the last several SCADA intervals, ambient temperature for the same period, and the gearbox's alarm setpoint.

## 10. Second climb of the day, or a climb shortly after a near-miss on the same site

**Usually means:** elevated fatigue or residual adrenaline/distraction that raises the risk of the highest-risk part of the job — the climb and transition points — independent of whether the actual repair task is routine.

**First question:** "Is this crew's second climb today, and has anyone on it had a near-miss in the last shift?"

**Data to pull:** crew climb log for the shift, any near-miss or incident report filed in the last 24–48 hours, and the site's fatigue-management policy trigger points.

## 11. Oil sample delayed or skipped past its scheduled interval

**Usually means:** either a logistics gap (lab turnaround, access difficulty) or a lower-priority classification of that turbine that's quietly eroding the predictive-maintenance program's coverage — a missed sample is a blind spot, not a neutral event.

**First question:** "How many intervals has this specific turbine missed, and why?"

**Data to pull:** the sampling schedule and actual sample-collection log per turbine, and whether missed turbines cluster on a specific pad, crew, or access difficulty.

## 12. Bolt torqued to spec without recorded lubrication or reuse state

**Usually means:** the applied torque may not correspond to the intended preload, since torque-to-tension depends on the friction coefficient, which shifts with lubrication and whether the fastener is new or reused — an unrecorded state makes the torque log unverifiable after the fact.

**First question:** "Was this bolt lubricated per the OEM spec, and is it a new or reused fastener?"

**Data to pull:** the torque log entry's lubrication field (if blank, that's the finding), the OEM's specified K-factor for that joint, and the fastener's install history.
