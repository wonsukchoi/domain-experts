# Light Truck Driver — Red Flags

### Vehicle GVWR/GCWR reassigned above 26,001 lb with no CDL on file for the assigned driver
- **Usually means:** a fleet or route reassignment swapped in a larger truck (or added a trailer) without checking the new rating against the CDL threshold
- **First question:** what does the certification/data plate say the GVWR or GCWR actually is, not what the load looks like today?
- **Data to pull:** vehicle data plate or spec sheet, driver's license class on file, GCWR calculation if a trailer is involved

### Vehicle GVWR between 10,001–26,000 lb with no current DOT medical card in the driver-qualification file
- **Usually means:** the route was treated as "non-CDL, so no federal rules apply," missing the separate 10,001 lb CMV threshold
- **First question:** when was the vehicle's rating last checked against 10,001 lb, and is there a current medical certificate on file?
- **Data to pull:** vehicle GVWR rating, driver-qualification file, medical certificate expiration date

### Route pace running more than roughly 25% above the density benchmark for the route type
- **Usually means:** pace is being compressed to hit a cutoff or beat a personal record, most often on backing-heavy stops where speed matters least
- **First question:** which stops are being completed faster than the benchmark, and are they the ones requiring backing?
- **Data to pull:** stop-by-stop timestamp log, route density classification, GOAL-check completion flags if tracked

### Backing incident or near miss logged twice at the same address or address type within a season
- **Usually means:** the approach or backing angle at that stop or stop type is genuinely difficult and hasn't been flagged for a route-sequencing override
- **First question:** was a route note or hazard flag added after the first incident, and did it carry over to subsequent deliveries?
- **Data to pull:** incident/near-miss log, route hazard-flag history for the address, telematics event log for that stop

### Delivery scanned as complete before the geotagged photo timestamp or GPS position matches the delivery address
- **Usually means:** the package was scanned before being physically placed, most often under time pressure near a cutoff
- **First question:** does the photo timestamp and GPS pin match the scan time and the delivery address within a reasonable margin?
- **Data to pull:** scan timestamp, photo metadata (time, GPS), route timing around that stop

### Signature-required or adult-signature package marked delivered with only a release photo
- **Usually means:** the package requirement was misread, or a shortcut was taken to avoid a redelivery attempt
- **First question:** what did the package's delivery-method flag actually require, and was that requirement met?
- **Data to pull:** package delivery-method flag from the manifest, delivery record (photo vs. signature vs. ID check)

### Telematics safety score drops sharply during a specific multi-day window
- **Usually means:** the decline correlates with an added-stop period, a compressed cutoff, or a temporary route reassignment rather than a general skill issue
- **First question:** what changed operationally in that window — added stops, new route, different dispatcher?
- **Data to pull:** day-by-day event log (not just the average score), route/stop-count records for the same window

### Dog-related incident or near miss with no hazard flag added to the address afterward
- **Usually means:** the report was filed but not connected to the route system, so the next driver on that route has no warning
- **First question:** was a route-level flag created for this address, and does it show up on today's route notes?
- **Data to pull:** incident report, route hazard-flag list, delivery history for the address

### Dispatcher request to add stops that would exceed the on-duty time budget with no reroute or second-driver discussion
- **Usually means:** the shortfall wasn't calculated before the request was made, or a shortcut is being assumed to cover the gap without checking its actual savings
- **First question:** what is the specific minute shortfall, and what would the proposed shortcut actually save?
- **Data to pull:** current route stop count and pace, remaining on-duty budget, any proposed shortcut's estimated time savings

### Route deviation or incident not logged the same shift
- **Usually means:** the driver intended to report it later from memory, or judged it too minor to log at the time
- **First question:** what happened, at which stop, and why wasn't it logged when it occurred?
- **Data to pull:** end-of-shift log entries, GPS/telematics track for the shift, any customer or dispatch report filed separately

### Customer delivery-placement complaints clustering at the same stop or stop type
- **Usually means:** a specific placement instruction is being skipped under pace pressure, not a random one-off
- **First question:** what does the delivery instruction for this address actually specify, and does the delivery photo show it was followed?
- **Data to pull:** address-level delivery instructions, delivery photos for recent visits, complaint history for the address
