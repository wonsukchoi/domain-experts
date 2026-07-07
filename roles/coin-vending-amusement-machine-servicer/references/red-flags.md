# Red flags

Smell tests a senior route technician catches before closing a stop or reviewing a route's monthly numbers.

### Cash variance beyond the greater of $10 or 3% of telemetry-expected collection

- **Usually means:** a coin mechanism under-crediting vends, an unlogged test-vend or refund, or an actual custody problem — in roughly that order of likelihood before assuming theft.
- **First question:** "Does the variance direction and size match anything in the machine's own vend/refund log, or is it unexplained?"
- **Data to pull:** telemetry vend count and expected cash for the period, physical count with timestamp, any logged test-vends or manual refunds since the last visit.

### Bill validator first-insert acceptance below ~95%, or false-reject above 2–3%

- **Usually means:** dirty optical sensors or a worn transport belt causing genuine bills to be rejected, driving customers to abandon the purchase — a lost-sales problem, distinct from any cash-variance question.
- **First question:** "What's the accept/reject counter reading since last service, and when was the path last cleaned?"
- **Data to pull:** validator's internal accept/reject log, date of last cleaning/recalibration, currency-tolerance test-note results if recalibration was attempted.

### Same jam or fault code recurs on one mechanism across 2+ visits within a rolling 2-week window

- **Usually means:** the first clear addressed the symptom (debris, jam) without resolving the underlying wear or sensor drift causing it.
- **First question:** "Pull the last three service entries on this mechanism — same fix each time, or different?"
- **Data to pull:** service history by machine/mechanism ID, jam counter trend, any wear-gauge or sensor-drift readings from prior visits.

### TCS/perishable slot logged above safe holding temperature past the documented time allowance

- **Usually means:** a defrost cycle or door-seal issue causing repeated excursions, not a one-off ambient spike — check whether this is the first occurrence or part of a pattern before assuming a fluke.
- **First question:** "Is this the first excursion on this unit, or has it happened on prior visits too?"
- **Data to pull:** cumulative time-above-threshold log for the current excursion, excursion history over the last 4 visits, defrost-cycle schedule and door-seal condition.

### A slot's average daily velocity × route cycle length consistently exceeds its physical capacity

- **Usually means:** the slot is undersized for that location's actual demand, not a restocking-habit problem — every visit restocked to full still runs out before the next one.
- **First question:** "What's this slot's lost-sale value per cycle, and does it exceed the cost of a second slot or a shorter cycle at this stop?"
- **Data to pull:** velocity history for the slot, route cycle length, slot capacity, retail price, route's standard per-visit cost.

### A stop's net contribution falls below the route's marginal-stop threshold for 2+ consecutive cycles

- **Usually means:** genuine declining traffic at that location, or an assortment mismatched to current demand — not a machine reliability issue, and more service visits won't fix it.
- **First question:** "Is the shortfall spread across all machines at the stop, or concentrated in one or two low-velocity SKUs that could be consolidated?"
- **Data to pull:** per-machine revenue at the stop over the last 3 cycles, SKU-level velocity, any known site-traffic change (staffing cut, facility closure).

### DEX telemetry inventory count persistently disagrees with physical count at the same machine

- **Usually means:** a stuck or miscalibrated fill sensor, which will keep distorting that machine's par-level calculation and the route's restocking schedule until it's corrected.
- **First question:** "How many consecutive visits has this machine's telemetry count been off, and by roughly the same amount each time?"
- **Data to pull:** telemetry-reported inventory vs. physical count for the last 3–4 visits, sensor/counter service history for that machine.

### Coin mechanism shows a rising false-reject rate on valid coins

- **Usually means:** mechanical tooling or optical-sensor wear inside the mechanism, not a currency-quality problem — customers switching to bills or giving up is the downstream symptom.
- **First question:** "What's the reject rate on coins that test as valid against the OEM gauge, and how has it trended over the last few services?"
- **Data to pull:** coin mechanism accept/reject counter, gauge test results on a sample of rejected coins, service/cleaning date history.

### Arcade or amusement PCB shows a reset loop or blank screen on power-up

- **Usually means:** a power-supply rail out of tolerance or a dying battery-backed RAM/CMOS battery, more often than a failed board — condemning the board first is how working boards end up replaced for no reason.
- **First question:** "What do the rail voltages read against spec before anything on the board itself is touched?"
- **Data to pull:** power-supply rail voltage readings, board self-test output if it gets that far, battery age/condition on the board.

### Route-level shrinkage concentrated on one machine or stop rather than spread across the fleet

- **Usually means:** a targeted mechanical or custody issue at that specific location, not a fleet-wide calibration or process problem — treating it as systemic (recalibrating every machine) misses the actual cause.
- **First question:** "Is the variance pattern isolated to this machine/stop, or does it show up fleet-wide at a similar rate?"
- **Data to pull:** variance history by machine and stop over the last quarter, fleet-wide baseline variance rate for comparison.
