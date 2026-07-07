# Red flags

Smell tests a senior field-service technician catches before signing off a ticket or reviewing a fleet report.

### Same error code recurs 2+ times on one asset within 30 days

- **Usually means:** the first visit fixed the proximate symptom, not the root cause — a jam cleared without checking why it jammed, or a component swapped without confirming the actual failure mode.
- **First question:** "Pull the last three tickets on this asset — same code, same fix, or different fix each time?"
- **Data to pull:** ticket history by asset ID, root-cause codes (not just "resolved") for the last 90 days, parts consumed per visit.

### Cash-dispenser reject-bin fill rate rising above historical baseline

- **Usually means:** dispense-mechanism wear (belt, gear, or sensor drift) is starting, well before it throws a hard fault code — the reject bin is the leading indicator, the error code is the lagging one.
- **First question:** "What's this unit's reject-bin fill rate over the last 90 days versus the fleet median for the same transaction volume?"
- **Data to pull:** reject-bin count per service visit, transaction volume over the same period, wear-gauge reading at last PM.

### Technician requests FRU swap approval without a diagnostic counter reading on the ticket

- **Usually means:** the swap decision was made from the error code alone, skipping the counter/gauge check that would confirm or rule out the cheaper procedural or bench-repair fix.
- **First question:** "What was the cycle counter and PM-interval position at the time of the call?"
- **Data to pull:** diagnostic log timestamped before the panel was opened; comparison against the swap-vs-repair worksheet.

### Cash reconciliation variance beyond ±2 notes or ±$50 at cassette reseal

- **Usually means:** either a counting error under time pressure or an actual custody break — both require investigation before the ticket closes, not after.
- **First question:** "Was two-person integrity maintained for the full compartment-open window, start to finish?"
- **Data to pull:** count-in/count-out log with both signatures, timestamp of compartment open/close, any interruption in custodian presence.

### SLA response clock shows on-time arrival but resolution clock breached

- **Usually means:** dispatch or the technician is tracking only the response metric and treating on-site arrival as "done," while diagnosis or parts delay blew the resolution window.
- **First question:** "What happened between on-site arrival and ticket close that took longer than the resolution budget?"
- **Data to pull:** timestamped ticket log (open, on-site, fix-start, fix-complete, verified), parts-availability record for that visit.

### Fleet MTTR stable or improving while MTBF is falling

- **Usually means:** the service org is getting faster at responding to a fleet that's failing more often — a maintenance-plan problem masked by a dispatch-efficiency win.
- **First question:** "Pull MTBF trend by asset class over the last four quarters, not just this quarter's MTTR."
- **Data to pull:** failure counts and uptime hours by asset over rolling quarters, PM-interval compliance rate over the same period.

### Repeated "no fault found" (NFF) closures on the same asset

- **Usually means:** either an intermittent fault the diagnostic tools aren't catching (loose connector, thermal-dependent fault) or a training gap where the technician doesn't recognize the actual failure signature.
- **First question:** "What conditions was the customer describing when the fault occurred, and did we reproduce those conditions on-site?"
- **Data to pull:** customer-reported symptom detail per call, environmental conditions (temperature, load, time of day) logged against each NFF visit.

### Technician logs solo cash-compartment access on an ATM ticket

- **Usually means:** either an emergency exception that should have been escalated instead, or a shortcut taken under SLA time pressure — both need a name attached, not a shrug.
- **First question:** "Was there a documented, pre-approved single-custodian exception for this action, and where's the paperwork?"
- **Data to pull:** site's cash-operations exception log, ticket timestamp vs. the two custodians' logged presence, branch manager confirmation.

### PM-interval overrun rate rising across the fleet (assets serviced >10% past their interval)

- **Usually means:** either staffing/scheduling can't keep pace with the PM calendar, or the interval itself is set wrong for actual usage (a branch running higher transaction volume than the interval assumed).
- **First question:** "Is the overrun concentrated in a few high-volume sites, or spread evenly across the fleet?"
- **Data to pull:** PM completion date vs. scheduled date by asset, transaction/impression volume per asset since last PM, technician headcount vs. route size.

### High-runner FRU part consistently at zero stock on the truck

- **Usually means:** either genuine demand growth the parts plan hasn't caught up with, or over-swapping — technicians defaulting to FRU replacement for faults a cheaper bench repair would have fixed.
- **First question:** "What's the swap rate for this part per 100 tickets with its associated error code, and how does that compare to the OEM's expected failure rate for the same code?"
- **Data to pull:** parts-consumption log by part number and technician, ticket-level swap-vs-repair worksheet completion rate, OEM failure-rate benchmark for the code.
