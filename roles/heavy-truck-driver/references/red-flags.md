# Heavy Truck Driver — Red Flags

### 30-minute break not logged by the time cumulative driving hits 8 hours
- **Usually means:** driver or dispatch is treating a short fuel or scale stop as a qualifying break, less commonly a genuine oversight under schedule pressure
- **First question:** was there a logged 30+ consecutive minutes of off-duty, sleeper-berth, or non-driving on-duty time since the last break, or just a stop under 30 minutes?
- **Data to pull:** ELD driving-time-since-last-break counter, duty-status change log for the shift

### Aggregate tiedown working load limit below 50% of cargo weight
- **Usually means:** tiedown count was set by article count or habit ("we always use 4 straps") rather than calculated against the actual weight and length
- **First question:** what's the WLL rating stamped on the hardware being used, and does the count match the length-based minimum table too?
- **Data to pull:** cargo weight from bill of lading/scale ticket, WLL tag on each tiedown, tiedown count against the minimum-by-length table

### Cumulative 60/7 or 70/8-day on-duty hours within 8 hours of the limit with no restart planned
- **Usually means:** the driver or dispatcher is sequencing loads day-to-day without tracking the rolling cumulative clock, common when hopping between short local loads that each look individually compliant
- **First question:** when was the last 34-hour restart, and is one scheduled before the next multi-day commitment?
- **Data to pull:** ELD 7/8-day cumulative on-duty total, restart history

### Out-of-service-level defect noted on a DVIR but truck dispatched anyway
- **Usually means:** schedule pressure led to treating an out-of-service item as a minor one, or the defect was miscategorized at inspection
- **First question:** does this defect appear on the current CVSA out-of-service criteria table, and under which classification?
- **Data to pull:** DVIR from the trip, CVSA out-of-service handbook item reference, maintenance sign-off if repaired

### Active ELD malfunction code with electronic logging continuing past the same duty period
- **Usually means:** driver or carrier is unaware a malfunction (vs. a routine data diagnostic event) requires an immediate switch to paper logs
- **First question:** is this a data diagnostic event or a malfunction code, and how many days has it been active?
- **Data to pull:** ELD malfunction/diagnostic code history, paper log reconstruction if past day 1, carrier notification timestamp

### Personal conveyance logged for distances that track directly toward the next dispatched load
- **Usually means:** driver or carrier is using the PC exception to bank extra legal driving time rather than genuine off-dispatch movement
- **First question:** was the driver actually released from the load at the time this PC segment was logged?
- **Data to pull:** dispatch release timestamp, GPS track for the PC segment, destination compared to next load's origin

### Detention time at shipper or receiver exceeding roughly 2 hours with no timestamped record
- **Usually means:** driver didn't document arrival/departure precisely enough to support a detention pay claim, or the facility is a repeat slow-turn location
- **First question:** what are the exact gate-in and gate-out (or appointment vs. actual load-start) timestamps?
- **Data to pull:** check-in/check-out log or ELD location timestamps, facility's historical detention pattern across prior loads

### Reported hours-awake exceeding roughly 16–18 hours with no sleeper-berth split used
- **Usually means:** driver is running the legal clock without managing actual fatigue, often under delivery-window pressure
- **First question:** when did the driver last get consolidated sleep, and does the route cross the 2 a.m.–6 a.m. circadian window?
- **Data to pull:** duty-status log for sleep/off-duty periods over the last 24–34 hours, route timing against circadian trough hours

### Same pre-trip or roadside defect cited twice within 90 days
- **Usually means:** the underlying issue was patched rather than fixed at the prior write-up
- **First question:** what repair was actually done against this defect the last time it was cited?
- **Data to pull:** prior DVIR/repair order for the same component, current inspection finding against the same threshold

### Gross combination weight at or above 80,000 lb without an axle-spacing (bridge formula) check
- **Usually means:** load was weighed for total tonnage but not checked against the federal bridge formula for axle-group spacing, which can make a truck illegal below 80,000 lb or legal above it depending on configuration
- **First question:** what's the axle spacing on this configuration, and does the bridge formula clear it at this weight?
- **Data to pull:** scale ticket with per-axle-group weights, axle spacing measurements, bridge formula table for the configuration

### Repeated short-haul (150 air-mile) exception claims that don't reconcile against GPS distance
- **Usually means:** the exception is being claimed on trips that actually exceed the radius, misapplying the reduced-logging provision
- **First question:** what's the actual GPS-measured distance from the work-reporting location on this trip?
- **Data to pull:** GPS/ELD location history for the trip, work-reporting-location address of record

### PSP (Pre-Employment Screening Program) report showing multiple prior HOS violations
- **Usually means:** a pattern of running the clock too close to the limit at prior carriers, not an isolated incident
- **First question:** were the violations self-reported discrepancies or roadside-cited out-of-service HOS violations?
- **Data to pull:** full PSP report, violation dates and codes, carrier of record at time of each violation
