# Red flags

Smell tests a dispatcher or senior chauffeur catches early. Format for each: what it usually means, the first question to ask, and the data to pull before anyone reacts.

### 1. Passenger running >15 minutes late with no contact attempt logged

**Usually means:** the driver is absorbing lateness silently instead of tracking slack burn against the manifest's remaining stops — the deadline is being protected by hope, not by a number.

**First question:** "How many minutes of contingency slack were left when this passenger went late, and against how many minutes of remaining stops and drive time?"

**Data to pull:** the run's planned slack-burn log; text/call timestamps to the late passenger; remaining stop count and drive-time estimate at the moment lateness was reported.

### 2. Same property runs over its stop buffer on 3+ runs in a month

**Usually means:** the generic 5-minute (+2/passenger) default is wrong for this specific property — a slow valet queue, long lobby-to-curb distance, or a front-desk process that reliably eats extra minutes — and nobody has updated the property's default.

**First question:** "What's this property's actual median boarding time over its last 10 pickups, and why are we still scheduling it at the generic default?"

**Data to pull:** per-run actual-vs-budgeted stop time for that property over the trailing 90 days; any dispatcher notes about valet/lobby delays specific to it.

### 3. Vehicle cargo capacity not checked against the manifest's luggage count before dispatch

**Usually means:** dispatch assigned a vehicle by class/name ("it's an SUV") rather than by its actual rated cargo volume in its current seating configuration, which varies widely within the same nameplate depending on row folding.

**First question:** "What's this specific vehicle's cargo cubic footage in its current seating configuration, and does it clear the manifest's checked-bag-plus-carry-on total?"

**Data to pull:** vehicle spec sheet for the assigned configuration; manifest luggage count; any day-of vehicle swap log (swaps are the most common source of this failure).

### 4. Client or coworker repeats a detail from a prior passenger's ride

**Usually means:** a confidentiality breach already happened, whether or not anyone flagged it as one — "harmless" repetition of overheard conversation is the actual failure mode, not a dramatic leak.

**First question:** "Where did that detail come from, and was it ever authorized for disclosure by the passenger it belongs to?"

**Data to pull:** which driver/run the detail traces to; the account's NDA or confidentiality terms; whether the disclosure reached anyone who could identify the passenger.

### 5. Following-distance telematics show hard-braking events above the vehicle's baseline

**Usually means:** the driver is running solo-driving following distances (the generic 3-second rule) on passenger-carrying runs rather than the wider 4–6 second standard, and hasn't yet had an incident severe enough to surface it.

**First question:** "What following distance is this driver running on this route, and does it match the passenger-transport standard for these conditions (day/night, wet/dry)?"

**Data to pull:** hard-braking event count and following-distance telemetry over the trailing 30 days; time-of-day and weather conditions for each event; whether the same driver/route pairing recurs.

### 6. Contract or account has no stated no-show grace period

**Usually means:** the driver is left to define "how long is too long" ad hoc per run, which produces inconsistent client experience and disputes over no-show billing after the fact.

**First question:** "What does this account's contract actually say about grace period and no-show billing — and if it says nothing, why hasn't that been added?"

**Data to pull:** the account's service contract terms; history of no-show billing disputes for that account; the default grace periods currently being applied informally by drivers.

### 7. Curbside citations or repeated dwell-time warnings at the same airport

**Usually means:** the driver is treating the passenger-boarding buffer as something to absorb curbside rather than recovering time upstream (asking passengers to be ready before arrival), running past the airport authority's commercial dwell limit (commonly 3–5 minutes).

**First question:** "Were passengers asked to be curbside with bags down before the vehicle arrived, or did the wait happen after arrival at the curb?"

**Data to pull:** citation/warning log by airport and driver; curb-arrival-to-departure timestamps for the flagged runs; whether the recovery tactic (bags-down-before-arrival) was used.

### 8. Dispatcher schedules a multi-stop run using a single flat pad instead of per-stop buffers

**Usually means:** the schedule was built as "drive time plus a round number," which hides exactly which stop is going to run over — the plan looks fine until the deficit surfaces at the last stop with no slack left to fix it.

**First question:** "Show me the per-stop buffer breakdown, not the total — which stop is budgeted for how long, and why?"

**Data to pull:** the run's planned schedule broken out stop by stop; the luggage-vs-cargo check (or its absence); the contingency margin actually built in versus the flat pad used.

### 9. A driver reports "we made it on time" as if the schedule had no near-misses

**Usually means:** slack was fully or nearly fully consumed without escalation to dispatch, so the deadline was met by luck or by the driver quietly absorbing risk the client and dispatcher never knew about.

**First question:** "How much contingency slack was left at the final stop, and was dispatch notified when it dropped below the remaining stops' time need?"

**Data to pull:** the run's slack-burn log; any dispatch notifications sent mid-route; whether the near-miss was logged for the next driver assigned to that property/account.

### 10. As-directed (hourly) account billed or scheduled like a fixed point-to-point run

**Usually means:** dispatch or the driver is applying scheduled-service buffer discipline to a service type where the client is actively redirecting the route in real time — producing either unnecessary rigidity with the client or missed billing for genuine idle/wait time.

**First question:** "Is this account contracted as-directed or point-to-point, and does the run log match that contract type?"

**Data to pull:** the account's service-type contract; the run's actual route log versus the originally planned stops; billed hours versus active-transport hours.
