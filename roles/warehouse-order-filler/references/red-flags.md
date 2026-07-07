# Red flags

Smell tests to catch before they become a shipping error, a write-off, or an injury report.

### 1. Rolling weekly line-accuracy rate below ~99.5%

**Usually means:** pace pressure is trading speed for accuracy, often via skipped or overridden scan/voice confirmation, rather than a one-off bad batch.

**First question:** "What's this picker's scan-compliance rate over the same period?"

**Data to pull:** WMS pick-accuracy report by picker, scan/voice override log, paired rate-vs-accuracy trend.

### 2. An A-velocity (top-20%-by-frequency) SKU slotted below knee or above shoulder height

**Usually means:** the zone hasn't been re-slotted since a demand shift moved this SKU into A-class — pickers are compensating with extra reach or bend every cycle instead of the slot being fixed.

**First question:** "When was this zone last re-slotted against current velocity data, and has this SKU's class changed since then?"

**Data to pull:** trailing 30–60 day pick-frequency report, current slot assignment, date of last re-slot.

### 3. Cases with mismatched or widely spread code dates within the same bin location

**Usually means:** a recent replenishment was placed in front of or mixed with older stock, breaking FIFO/FEFO order at putaway rather than at picking.

**First question:** "Who put away the most recent replenishment, and was it checked against the dates already in the bin?"

**Data to pull:** putaway timestamp/log for that location, current lot/date codes present.

### 4. Units/hour trending up while accuracy trends down for the same picker over the same weeks

**Usually means:** a rate incentive or informal pace expectation is training the wrong behavior, and nobody has paired the two metrics to see it.

**First question:** "Is there a bonus threshold or informal rate expectation this picker is chasing right now?"

**Data to pull:** paired rate-and-accuracy trend by picker, incentive plan terms, recent schedule/staffing changes in that zone.

### 5. Repeated cycle-count discrepancies at one specific bin location

**Usually means:** either a slotting/replenishment error (wrong SKU or quantity keeps landing there) or a shrink pattern (mis-pick or loss) that hasn't been isolated yet.

**First question:** "Is the discrepancy consistently in one direction (short) or does it vary in sign?"

**Data to pull:** cycle-count history for that location, replenishment records, recent picker assignments to that zone.

### 6. Scan/voice confirmation override rate above baseline for a shift or picker, with no hardware fault logged

**Usually means:** confirmations are being treated as a bottleneck to work around under pace pressure rather than a control being genuinely blocked by a bad barcode or reader.

**First question:** "What's the reason code on these overrides, and does it match an actual equipment issue?"

**Data to pull:** override log with reason codes, correlation with that picker's or shift's error rate.

### 7. A picker reporting soreness concentrated in one body region tied to a specific bin or task

**Usually means:** a calculable Lifting Index concern at that specific slot (height, weight, frequency, reach), not an individual conditioning issue.

**First question:** "What's the exact lift weight, origin/destination height, and frequency at that task?"

**Data to pull:** the task's NIOSH LI inputs (weight, vertical origin/destination, horizontal distance, frequency, twist angle), injury/first-aid log for that task or location.

### 8. Markdown or write-off spikes on a dated SKU with no corresponding demand miss

**Usually means:** FEFO discipline broke somewhere between putaway and pick — older stock sat while newer stock shipped first.

**First question:** "What lot numbers are on the written-off units, and when were they picked relative to newer lots of the same SKU?"

**Data to pull:** markdown/write-off report by lot, pick history for those specific lot numbers.

### 9. A new or seasonal picker hitting full rate targets within days with no accuracy dip on record

**Usually means:** QA sampling isn't checking that picker's work as tightly as tenured staff yet, not that the picker is unusually fast and accurate from day one.

**First question:** "Is this picker's QA audit sampling rate the same as everyone else's, or has it lapsed to the standard reduced rate too early?"

**Data to pull:** QA audit sampling rate and results by picker tenure, ramp-up schedule for new hires.

### 10. Pick-path sequence frequently overridden back to bin-number order

**Usually means:** pickers don't trust or understand the WMS-generated sequence, or the sequence itself is stale after a re-slot and no longer reflects the fastest route.

**First question:** "Was the path re-optimized after the last slotting change in this zone?"

**Data to pull:** path-override frequency by picker or zone, date of last slotting/path re-optimization.
