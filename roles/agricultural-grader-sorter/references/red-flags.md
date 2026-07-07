# Red flags

Line and lot smell tests a senior grader/sorter catches before a bad lot ships or a good lot gets dumped for no reason.

### Sample defect count sits exactly at the accept number (Ac), lot after lot, for the same grower

- **Usually means:** the field/grower is drifting toward the tolerance ceiling and every marginal lot is technically passing while the trend goes unflagged; second: sampling isn't actually randomized (grabbing from the accessible top layer of the bin).
- **First question:** "Pull the last ten lots' sample defect rates for this grower/field — is it trending up toward Ac?"
- **Data to pull:** lot-level disposition log by grower/field over the trailing 30 days; sampling method/randomization notes for those lots.

### A decay or serious-damage defect turns up even once in an otherwise-clean sample

- **Usually means:** at least one piece has active fungal or bacterial rot, and in a shared bin under humid storage that spreads to adjacent fruit faster than a cosmetic bruise does; second: a storage temperature excursion upstream.
- **First question:** "What else was touching this piece in the bin, and how long has this lot been in storage?"
- **Data to pull:** storage temperature/humidity log for the lot; bin/pallet adjacency map; days in storage before packing.

### Optical sorter pass rate is unusually high on fruit picked less than 4 hours ago

- **Usually means:** fresh mechanical bruising hasn't discolored enough yet for camera/NIR detection to catch it; second: sorter threshold calibration has drifted looser than spec.
- **First question:** "When was this fruit picked, and is a human station running downstream of the sizer for it right now?"
- **Data to pull:** harvest timestamp vs. pack timestamp; sorter calibration/QC check log; hand-grade override rate on same-day fruit versus older stock.

### A downgrade decision gets made without the resort-vs-downgrade math being run

- **Usually means:** the line is defaulting to whichever disposition is fastest to execute, not the one that's cheapest; second: nobody on shift is assigned to own that call.
- **First question:** "What would a 100% hand re-sort of this lot cost in labor, versus the grade-spread loss from downgrading it outright?"
- **Data to pull:** grade price spread by tier; expected re-sort time at this lot's piece count and grader throughput; fully loaded labor rate.

### The same grader has been on station for four-plus hours without rotation

- **Usually means:** fatigue-driven miss rate is climbing and is invisible because nobody is auditing grader-level accuracy in real time; second: a staffing shortage is forcing extended stations.
- **First question:** "When did this grader last rotate, and has anyone run a blind check-sample against their calls today?"
- **Data to pull:** rotation schedule log; blind re-check sample results by grader and shift-hour.

### Customer claim rate is rising on loads that all passed line QC clean

- **Usually means:** the line is grading to the legal minimum tolerance instead of this specific buyer's tighter contract spec; second: the buyer's own receiving inspection is using a stricter sampling plan than the packer's outbound one.
- **First question:** "What defect tolerance does this customer's contract actually specify, versus what the line graded this lot to?"
- **Data to pull:** customer spec sheet; outbound disposition record for the claimed lot; the customer's receiving-inspection report if available.

### One grower/field's cull rate is running roughly double the seasonal average, across several consecutive lots

- **Usually means:** a field-level agronomic issue (irrigation stress, pest pressure, rough or late harvest) rather than a packing-line problem; second: that grower's fruit is being handled or transported more roughly before it reaches the line.
- **First question:** "Is this grower's cull rate elevated across every commodity and variety they supply, or isolated to one field?"
- **Data to pull:** cull rate by grower/field across the season; harvest date and days-in-storage before packing; any recent agronomic notes from the grower relationship.

### Sample size pulled doesn't match the declared lot size on the sampling table

- **Usually means:** someone is using a fixed sample count regardless of lot size (e.g., always pulling 100 pieces), which understates risk on larger lots; second: lot size is being misreported to land in a smaller, looser sampling tier.
- **First question:** "What lot size was declared for this sample, and does the sample size actually pulled match the Ac/Re table row for that size?"
- **Data to pull:** declared lot size/piece count; the sampling table in use; the actual sample size pulled and recorded.

### Lot holds are occurring but escalations to the QA supervisor haven't, for weeks

- **Usually means:** station-level staff are quietly resolving holds themselves (re-sorting or downgrading) without logging the escalation, which hides a developing pattern from management; second: the escalation threshold is set so high it almost never triggers.
- **First question:** "How many lot holds happened this week, and how many were actually escalated versus resolved at the station?"
- **Data to pull:** lot hold log versus escalation log; the documented escalation threshold; station-level disposition notes for holds that weren't escalated.
