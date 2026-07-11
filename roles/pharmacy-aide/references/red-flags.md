# Red Flags

### Schedule II delivery arrives with a broken seal or a physical count that doesn't match the invoice
- **Usually means:** wholesaler packing error at the distribution center, then in-transit tampering or short-fill, then internal loss after receipt if the discrepancy wasn't caught at the dock
- **First question:** was the seal broken when the driver handed it over, or discovered only after it was already shelved
- **Data to pull:** wholesaler invoice, delivery manifest signature, CSOS order confirmation, receiving log entry timestamp

### Same SKU or register shows a discrepancy 2+ times in a rolling 30 days
- **Usually means:** a recurring receiving/count error tied to that item's shelving process, or the same shift/employee combination each time
- **First question:** is it the same shift, same employee, or same physical location every time it happens
- **Data to pull:** POS shrink report by SKU, register assignment log, shift schedule

### Vaccine fridge log shows only twice-daily manual readings, no min/max or continuous logger on file
- **Usually means:** the site is relying on a monitoring method that structurally misses most excursions rather than an intentional gap
- **First question:** when was the digital data logger (or min-max thermometer) last verified or calibrated
- **Data to pull:** DDL calibration record, 30-day temperature history, VFC program enrollment status

### Cash drawer variance recurs on the same register across 2+ consecutive shifts
- **Usually means:** multiple people sharing one drawer without individual accountability, or an actual skimming pattern
- **First question:** how many people had access to that specific drawer during the affected shifts
- **Data to pull:** register assignment log, void/refund transactions for those shifts

### A new or cross-trained staff member is keying/counting prescriptions in a state where clerical roles are defined as intake-only
- **Usually means:** well-intentioned scope creep to save time, sometimes implicitly condoned by a supervisor under volume pressure
- **First question:** does this state's board of pharmacy scope-of-practice rule explicitly exclude this task from clerical duties
- **Data to pull:** state board of pharmacy technician/clerical scope-of-practice statute or registration rule

### An insurance card, ID, or prescription label is readable by the next customer in line at every transaction, not just occasionally
- **Usually means:** a counter or queue layout problem, not an individual staff lapse
- **First question:** is this happening on this specific transaction only, or does the physical layout make it happen every time
- **Data to pull:** none for a one-off; a layout/spacing review if it's structural

### A wholesaler delivery is signed for with zero counting discrepancies logged across several consecutive months
- **Usually means:** deliveries are being signed before counting, not that counts are genuinely perfect every time
- **First question:** what's the actual discrepancy rate on receiving logs over the last two quarters
- **Data to pull:** receiving log discrepancy history, dock camera footage if available

### A controlled-substance delivery arrives outside the wholesaler's scheduled window
- **Usually means:** a routine reschedule, but is also a known diversion-risk window worth confirming rather than assuming
- **First question:** was this delivery actually expected today, per the wholesaler's published schedule
- **Data to pull:** wholesaler delivery schedule confirmation, order history for the SKU

### A phone caller asks to confirm whether a specific named person has a prescription ready, without offering identifying details first
- **Usually means:** an innocent pickup-for-a-family-member call in most cases, but is also the exact pattern used to confirm someone else's medication or health status
- **First question:** is the caller listed as an authorized contact on that patient's account
- **Data to pull:** patient's authorized-pickup/communication designee list, if on file
