# Weighers, Measurers, Checkers, and Samplers — Red Flags

### Net-weight variance from BOL/PO exceeds 0.5% (or the site's stated tolerance)
- **Usually means:** A stale tare weight, a genuine short/over-shipment, or a scale-calibration drift — in roughly that order of likelihood.
- **First question:** Was the tare weight re-verified for this specific vehicle within the site's re-tare interval?
- **Data to pull:** Current and prior tare tickets for the vehicle, the scale's calibration/seal log, and the re-weigh confirmation.

### Scale's calibration seal is expired or within 7 days of expiring
- **Usually means:** Readings taken on it are legally and practically unreliable, even if they "look right."
- **First question:** Is there an alternate certified scale available, or must this reading be flagged as provisional?
- **Data to pull:** Calibration log, seal expiration date, last third-party verification report.

### A vehicle's tare ticket is older than the site's re-tare interval
- **Usually means:** Fuel level, accumulated residue, or an equipment change has likely altered the true tare since that ticket was cut.
- **First question:** Has anything visibly changed on the vehicle since the last tare (toolbox, tank residue, trailer swap)?
- **Data to pull:** Date of last tare ticket, vehicle ID, any maintenance/modification log.

### An AQL sample fails but the lot "looks fine" on visual inspection
- **Usually means:** The defects the sample caught are real per the plan's definition, even if they're not visually obvious — the plan exists because visual inspection alone misses exactly this kind of defect.
- **First question:** What is the sampling plan's disposition rule for this Ac/Re outcome, and has it been followed without exception?
- **Data to pull:** The sample's defect log, the lot's inspection-level/AQL assignment, and the plan's accept/reject table.

### Two consecutive lots from the same vendor fail inspection
- **Usually means:** A vendor process issue, not two unrelated bad-luck lots — this is exactly the switching-rules trigger for tightened inspection.
- **First question:** Has inspection been switched to Tightened per the sampling plan's rule, or is it still running at Normal?
- **Data to pull:** Lot-by-lot pass/fail history for this vendor over the trailing 10 lots.

### A repeat defect type shows up across multiple accepted lots
- **Usually means:** A vendor process drift that individual lot-level AQL disposition won't catch, since each lot can pass while the pattern persists.
- **First question:** Has this defect type and rate been logged and trended across lots, or only recorded per-lot and forgotten?
- **Data to pull:** Defect-type log across the vendor's last 5-10 lots, not just the current one.

### A discrepancy is "corrected" in the record without a filed report
- **Usually means:** Someone adjusted the number to make it match rather than documenting why it didn't — this destroys the evidence a claim or audit would need.
- **First question:** Is there a discrepancy report on file for this ticket, or just a quietly revised weight?
- **Data to pull:** Original scale ticket, any subsequent edits with timestamps/user IDs, and the discrepancy-report log.

### A driver or vendor pushes back hard on a re-weigh request
- **Usually means:** Sometimes genuine time pressure, occasionally an indicator that the original weight won't hold up — the pressure itself isn't evidence either way.
- **First question:** Does policy allow releasing the load provisionally pending a re-weigh, or must the re-weigh happen before release?
- **Data to pull:** Site's stated policy on re-weigh-before-release versus release-then-reconcile.

### A "legal for trade" sticker or seal looks tampered with or missing
- **Usually means:** The scale may not be certified for commercial transactions regardless of how accurate its readings appear.
- **First question:** Who is the site's weights-and-measures authority of record, and when was the seal last verified by them?
- **Data to pull:** State weights-and-measures inspection records for this scale.
