# Pharmacy Aide Playbook

Filled procedures for the four recurring process types: receiving, cold-chain logging, phone/counter triage, and cash reconciliation.

## Receiving — count rules by schedule and container status

| Product type | Container status | Count method | Action if mismatch |
|---|---|---|---|
| Schedule II (e.g., oxycodone, Adderall, fentanyl) | Any | Exact physical count, every unit | Hold off shelf; flag pharmacist-in-charge same day |
| Schedule III–V | Unopened, ≤1,000 dosage units | Estimated count acceptable | Recount exactly if invoice and estimate diverge by more than 1 unit per 100 |
| Schedule III–V | Unopened, >1,000 dosage units, or any opened container | Exact physical count | Hold off shelf; flag pharmacist-in-charge |
| Non-controlled stock | Any | Count by case/carton against invoice | Note shortage on invoice; restock normally, no hold required |

Steps at the loading dock:
1. Match the invoice line count to physical units before signing the wholesaler's manifest — never sign first and count later.
2. For any Schedule II line, count every bottle/unit even if the invoice total looks correct; a correct total can still hide a short bottle offset by an extra one elsewhere.
3. If a seal is broken or a count doesn't match: do not shelve. Log the exact discrepancy (invoiced quantity, counted quantity, which container) and route to the pharmacist-in-charge same day. They decide whether it meets the threshold for a DEA in-transit loss report.
4. File the receiving log entry with date, time, invoice number, wholesaler, and counting method used (exact vs. estimated) — the biennial inventory review depends on this trail existing, since a perpetual/receiving log by itself does not substitute for the physical biennial count.

## Cold-chain (vaccine refrigerator/freezer) logging

| Monitoring method | What it actually catches | Default use |
|---|---|---|
| Twice-daily manual reading, no min/max | A single digit percentage of true excursions | Backup only, never primary |
| Twice-daily min/max thermometer reading | Better than spot-reading, still misses excursions between resets | Minimum acceptable if no logger installed |
| Continuous digital data logger (reading ≥ every 30 min) | Full excursion history, retrievable | Required for VFC-enrolled sites; default assumption everywhere else |

Daily steps:
1. Record the current reading at open and close of business, but pull the logger's stored min/max (or full log) rather than relying on the two spot readings alone.
2. Compare the stored min/max against the vaccine manufacturer's storage range (commonly 2–8°C refrigerated, -25 to -15°C frozen — confirm per product insert, ranges vary by vaccine).
3. Any excursion beyond range, however brief: don't just note it and move on — flag the pharmacist immediately; affected vaccine may need to be quarantined (not discarded or used) pending manufacturer or VFC-coordinator guidance.
4. Log the DDL's last calibration/verification date monthly; a device with no recent calibration is itself a flag, independent of what its readings show.

## Phone/counter triage table

| Request | Default action |
|---|---|
| "Is my prescription ready?" | Handle directly — lookup by name + DOB, confirm status |
| "How much will this cost with my insurance?" | Handle directly if already adjudicated; if not yet run, route to technician |
| "Can I take this with [other drug]?" | Route to pharmacist by name, with the exact question — never answer |
| "What's this medication for / what are the side effects?" | Route to pharmacist |
| "Can you confirm if [other person] has a prescription ready?" | Check authorized-contact list first; if caller isn't listed, don't confirm — offer to have the pharmacist call the patient directly |
| "I need this filled right now, it's urgent" | Log the request and timestamp, hand to pharmacist/technician queue with the urgency noted — don't promise a fill time you don't control |
| Delivery driver dropping off outside the scheduled window | Confirm against the day's expected delivery schedule before accepting; unscheduled drop-offs get extra scrutiny on the receiving count |

## Cash and shrink reconciliation

1. Reconcile the register drawer at shift change: expected total (opening float + sales – refunds) vs. counted total.
2. A variance under approximately 0.5% of the shift's transaction total is normal register-handling noise; log it and move on.
3. A variance recurring on the same register or same shift across two or more consecutive shifts stops being noise — flag it to the manager as a pattern, not a fresh one-off each time.
4. When a shelf/SKU count comes up short, check the receiving log for that SKU before assuming in-store theft — a meaningful share of retail shrink traces to process error (miscounted receiving, misshelving), not stealing, so the receiving trail is the first thing to pull.
