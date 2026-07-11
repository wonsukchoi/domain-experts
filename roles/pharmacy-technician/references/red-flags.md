# Red Flags

Smell tests for dispensing, compounding, and claims work. Format per flag: what it usually means, the first question to ask, the data to pull.

### Days'-supply math doesn't match the sig on file

- **Usually means:** the system computed days' supply off a stale sig (before a dose change) or off the wrong frequency assumption for a PRN order.
- **First question:** "Has the sig changed since the last fill, and was the last days'-supply calc done at fixed frequency or at the PRN maximum?"
- **Data to pull:** the two most recent fills' sigs side by side, and the raw quantity ÷ frequency math for each.

### Reject 79 (refill too soon) on a controlled substance, more than once in 90 days

- **Usually means:** either a legitimate dose titration the system hasn't caught up with, or an early-refill/possible-diversion pattern — these look identical at the reject-code level and only the sig history and PDMP tell them apart.
- **First question:** "Did the sig or prescriber change between these fills, or is it the same sig, same prescriber, just earlier?"
- **Data to pull:** PDMP query across all prescribers and pharmacies for this patient and drug class, not just this pharmacy's own fill history.

### New patient, new prescriber, cash pay, targeted controlled substance

- **Usually means:** most of the time it's a legitimate new patient — but this combination (no insurance history to check, no prior fill pattern, a commonly diverted drug like oxycodone or promethazine-codeine) is also the classic profile flagged in diversion training.
- **First question:** "Does the PDMP show fills from other pharmacies or prescribers for this patient in the last 30 days?"
- **Data to pull:** PDMP report; prescriber's DEA registration status and specialty match to the drug prescribed.

### Sig contains an error-prone abbreviation

- **Usually means:** "q.d." misread as "q.i.d.," "U" misread as "0" (10x insulin overdose), or trailing zeros/no leading zero causing a 10x dosing error — all on ISMP's Do-Not-Use abbreviation list for a reason.
- **First question:** "Can I get this order in unabbreviated units and confirm the intended frequency directly?"
- **Data to pull:** the original prescription image or verbal-order documentation; compare against the ISMP error-prone abbreviations list.

### A look-alike/sound-alike drug pulled from bin position rather than label read

- **Usually means:** time pressure or interruption caused a habitual reach instead of a read — the bin layout itself may be contributing if two LASA drugs sit adjacent.
- **First question:** "Did I read the full label — name, strength, form — or did I grab by where it usually sits?"
- **Data to pull:** ISMP Confused Drug Names list; bin/shelf layout map for adjacency of known LASA pairs.

### Beyond-use date assigned past the USP <795>/<797> default with no stability reference on file

- **Usually means:** someone extended a BUD based on how the preparation looked or how long a similar mix "usually lasted," not a validated study.
- **First question:** "What published stability reference supports this specific BUD, and does it match this exact formulation, concentration, and container?"
- **Data to pull:** the cited stability study or reference (Trissel's, manufacturer data); compare against the <795>/<797> default table.

### Technician performing final verification the state board doesn't authorize

- **Usually means:** a workflow habit carried over from a previous employer or state where tech-check-tech was permitted, applied somewhere it isn't.
- **First question:** "Does this state's board of pharmacy, and this technician's specific certification, authorize tech-check-tech for this drug category?"
- **Data to pull:** current state board of pharmacy rules and the technician's certification/registration status.

### Same drug class, multiple concurrent prescribers, no coordination note

- **Usually means:** legitimate multi-specialty care (e.g., oncology and primary care both prescribing pain medication) or an early sign of uncoordinated/duplicate therapy — DUR reject 88 often surfaces this first.
- **First question:** "Do the prescribers appear to be coordinating, or is each apparently unaware of the other's prescription?"
- **Data to pull:** DUR alert detail; PDMP cross-prescriber history.

### NDC billed doesn't match package size dispensed

- **Usually means:** a 10-digit product NDC (used for identification) was keyed instead of the 11-digit billing NDC (which encodes package size), or the wrong package size was scanned.
- **First question:** "Does the billed NDC's package size match what's physically being dispensed?"
- **Data to pull:** NDC lookup cross-referencing product identifier against billed package size.

### Independent double-check skipped or rubber-stamped under high volume

- **Usually means:** the check happened in name only — same person re-reading their own work, or a second person signing off without physically re-verifying.
- **First question:** "Did a different person independently re-check drug, strength, and patient identity, separately from the original fill?"
- **Data to pull:** verification log timestamps and initials; queue volume at the time, to see if the skip correlates with rush periods.
