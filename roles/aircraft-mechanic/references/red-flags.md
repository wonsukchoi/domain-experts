# Red flags

Smells a veteran A&P catches reviewing a logbook, discrepancy history, or open-deferral list before signing anything.

### "No fault found" / "checks good" logged three or more times on the same system

- **Usually means:** intermittent fault that hasn't been root-caused, not a fault that's gone away — the underlying condition (loose connector, chafed wire, marginal sensor) is still present and will resurface, usually at a worse moment.
- **First question:** "What's different about the flights where it *did* show up versus the ones where the check came back clean?"
- **Data to pull:** full squawk history for that ATA chapter over the last 90 days, correlated with flight phase, weather, and which crew/leg reported it; component swap history for that position.

### MEL deferral at day 8 of a 10-day Category C window with no parts on order

- **Usually means:** the deferral was logged and then forgotten — nobody owns the countdown, and the item will either get an emergency same-day fix or force an unplanned grounding on day 10.
- **First question:** "Who owns this repair, and what's the parts ETA against the March 13 expiration?"
- **Data to pull:** open-deferral list with expiration dates sorted by days remaining; parts order status and lead time; whether a spare aircraft/routing swap is available if the repair slips past expiration.

### Torque seal broken or absent on a fastener known to have been torqued at the last inspection

- **Usually means:** the fastener has been disturbed since the seal was applied — could be legitimate rework that wasn't logged, or could be actual back-off; either way the torque state is now unverified, not "probably fine."
- **First question:** "When was this fastener last worked, and is there a log entry for it?"
- **Data to pull:** the maintenance log entries for that access panel/zone since the last seal application; torque spec for that fastener from the current-revision manual; whether the same discrepancy zone has any other open or recent squawks.

### Maintenance log entry missing certificate number or with an illegible/ambiguous signature

- **Usually means:** either a training gap (the mechanic doesn't know the entry is legally incomplete) or a rushed sign-off under schedule pressure where the paperwork was an afterthought.
- **First question:** "Who actually performed and verified this work, by certificate number?"
- **Data to pull:** the full entry against the 14 CFR 43.9 required-content checklist (description, data reference, date, total time, name, certificate number, signature); shift roster for who was on duty at that time.

### Component replaced with same part number but no 8130-3 tag or traceable serial number

- **Usually means:** the part came from an unapproved source (unapproved parts distributor, cannibalized without paperwork, or counterfeit/"suspected unapproved part") — same part number is not proof of airworthiness pedigree.
- **First question:** "Where's the 8130-3 or equivalent airworthiness tag for this exact serial number?"
- **Data to pull:** the parts receiving/traceability record; the vendor's certification; whether this supplier appears on any FAA Suspected Unapproved Parts notice.

### Recurring squawk on the same system reported by different crews across different legs

- **Usually means:** a real intermittent fault that each individual write-up is treating as a one-off, so nobody is looking at the pattern across write-ups.
- **First question:** "Pull every write-up on this ATA chapter for this tail number over the last 60 days — how many, and what's common?"
- **Data to pull:** consolidated discrepancy history by tail and ATA chapter; component removal/reinstall history; any related SDR filed for this fleet type.

### AD compliance logged without a reference to the specific method used or the aircraft's effectivity check

- **Usually means:** the compliance was recorded as complete but the mechanic may not have confirmed this specific serial number/configuration was actually within the AD's effectivity, or used data that doesn't match this aircraft's actual configuration.
- **First question:** "Show me the effectivity check against this aircraft's serial number and configuration, and which paragraph of the AD was actually performed."
- **Data to pull:** the AD's effectivity section; the aircraft's configuration/modification records; the specific inspection or repair data referenced in the log entry.

### An item deferred that doesn't have a matching MEL entry

- **Usually means:** the deferral was made by analogy to a similar-looking MEL item rather than the item actually listed — MEL entries are specific to a system and function, not a general "seems minor" judgment.
- **First question:** "Which exact MEL item number authorizes deferring this?"
- **Data to pull:** the MEL index for the relevant ATA chapter; whether the item is a "no-MEL-relief" item (meaning it grounds the aircraft by default).

### Safety wire twisted with fewer than the specified twists per inch, or in the wrong direction

- **Usually means:** a rushed or undertrained install — under-twisted wire can back out under vibration, and wire twisted the "loosening" direction actively helps a fastener back off instead of resisting it.
- **First question:** "What's the twist count and direction against the manual's spec for this fastener?"
- **Data to pull:** the applicable safety-wire spec (AC 43.13-1B Chapter 7 or the type manual); who performed and who inspected the install; whether this mechanic's other recent safety-wire jobs show the same pattern.

### Tool inventory doesn't reconcile at shift close after work inside an open panel

- **Usually means:** a tool is inside the aircraft, in a toolbox that wasn't checked, or genuinely lost — until proven otherwise it is treated as the first, worst case.
- **First question:** "What's the last confirmed count, and which panels were open since then?"
- **Data to pull:** tool control log/foreign object debris (FOD) checklist for the shift; list of panels opened and by whom; whether the aircraft has already been released for the next flight.

### Discount/"good enough" repair proposed to make a departure bank

- **Usually means:** schedule pressure is pushing a shortcut past what the data allows — a legitimate time-saving option exists only if the manual or MEL actually authorizes it, not because the pressure is high.
- **First question:** "Which manual section or MEL item authorizes doing it this way, versus the standard procedure?"
- **Data to pull:** the applicable procedure and any alternate/expedited procedure the manual explicitly allows; the actual delay cost versus the cost of a compliance finding.
