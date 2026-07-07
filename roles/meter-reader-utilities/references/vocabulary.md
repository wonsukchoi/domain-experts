# Meter Reader, Utilities — Vocabulary

### AMI (Advanced Metering Infrastructure)
Meters that transmit reads automatically over a network, eliminating most manual visits except for verification, dispute investigation, or AMI-outage fallback.
**In use:** "This account's on AMI, but the signal's been dropping — that's why we're sending a walker to true it up manually."
**Common misuse:** Treated as interchangeable with AMR — AMI is two-way and near-real-time, AMR is typically drive-by/walk-by one-way collection, and the fallback procedures differ.

### AMR (Automated Meter Reading)
Meters read via a handheld or drive-by radio-frequency receiver rather than visually — faster than manual reads but still requires physical proximity, unlike AMI.
**In use:** "We AMR'd the whole block in under an hour, no need to walk up to each meter."
**Common misuse:** Assumed to eliminate the need for physical inspection — an AMR read can still be anomalous and require the walker to physically check the meter.

### Actual read
A reading taken directly from the meter (visually, AMR, or AMI) for the current cycle, as opposed to an estimate.
**In use:** "Two estimates in a row — I need an actual read this cycle or the true-up's going to be a mess."
**Common misuse:** Assumed always more accurate than an estimate — an actual read can still be a misread digit or a compromised meter's output.

### Estimated read
A projected consumption figure used when an actual read can't be obtained, typically based on the account's historical usage pattern for that billing period.
**In use:** "It's estimated based on last September — if the customer's usage pattern changed, that estimate's going to be off."
**Common misuse:** Treated as a neutral placeholder with no consequence — accumulated estimates create a true-up liability that grows the longer actual reads are missed.

### Register
The meter's running cumulative total (of kWh, therms, or gallons), from which a cycle's consumption is calculated by subtracting the previous register value.
**In use:** "The register jumped 40,000 units between cycles — that's a rollover, not real consumption."
**Common misuse:** Confused with "consumption" itself — the register is a cumulative odometer-style total; consumption is the difference between two register readings.

### Register rollover
When a mechanical or older digital register reaches its maximum digit capacity and resets to zero, producing an apparent negative-consumption read if not accounted for.
**In use:** "Don't post that as negative consumption — check the register's max digits first, this looks like a rollover."
**Common misuse:** Assumed to only happen on old mechanical meters — some digital registers have lower rollover thresholds than expected and can roll over within a normal billing cycle for high-usage accounts.

### Tamper seal
A numbered, single-use seal installed on a meter's access points; a broken or mismatched seal is direct physical evidence of possible unauthorized access.
**In use:** "Seal number doesn't match what's on file for this account — that's going straight to revenue protection."
**Common misuse:** Treated as proof of theft by itself — a broken seal is strong evidence of *access*, not proof of what was done once inside; it still routes to investigation rather than an on-site accusation.

### Bypass / jumper
A wire or connection installed to route current or flow around the meter, so consumption isn't fully registered — the primary mechanical signature of theft-of-service.
**In use:** "There's a jumper behind the meter bridging the load lugs — photograph it, don't touch it."
**Common misuse:** Assumed obvious/visible on casual glance — bypasses are often concealed inside the meter housing or behind panels and require a deliberate physical inspection to find.

### Revenue protection
The utility function — often a specialized investigations team — that handles confirmed or suspected theft-of-service and meter-tamper cases, distinct from routine field operations.
**In use:** "This one's revenue protection's case now — I documented the evidence, I don't confront the customer."
**Common misuse:** Confused with routine customer service or billing disputes — revenue protection cases follow a distinct evidentiary and legal process because they can lead to fines or service termination.

### Seasonally-adjusted baseline
An account's expected consumption for a given billing period, based on the same period in a prior year rather than a flat trailing average, to account for weather-driven usage swings.
**In use:** "Don't compare this January bill to the July average — pull last January's number instead."
**Common misuse:** Skipped in favor of a simple trailing 12-month average, which smooths out seasonality and produces false anomalies on genuinely normal seasonal swings.

### Vacancy flag
An account-level marker indicating the property is unoccupied, which resets the expected baseline consumption to near-zero.
**In use:** "No wonder it's near zero — this account's had a vacancy flag since March."
**Common misuse:** Assumed to be automatically updated — vacancy flags require someone to log the status change, and a stale or missing flag is a common source of false anomaly alerts.

### Multiplier / CT ratio
A factor (from a current transformer, on larger commercial meters) that the raw meter reading must be multiplied by to get actual consumption — a mismatch between the recorded multiplier and the meter's actual nameplate value produces large false readings with no tampering involved.
**In use:** "Before you flag this as theft, check the multiplier — a lot of 'anomalies' on commercial accounts are just a wrong CT ratio on file."
**Common misuse:** Overlooked entirely on residential-focused routes, then misapplied when a walker is unexpectedly assigned a commercial account with a CT-metered service.

### Walk order / route
The sequenced list of accounts assigned to a reader for a given day, typically optimized for geographic efficiency.
**In use:** "I'm behind on the walk order because of the dog at the Fillmore address — flagging it for an alternate-access note."
**Common misuse:** Treated as a strict quota that overrides safety judgment — falling behind on the route is recoverable; skipping the safety check to stay on schedule is not.
