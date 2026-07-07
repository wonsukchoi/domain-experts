# Vocabulary

Terms generalists conflate or misuse. Each: definition, how a practitioner actually uses it, and the common misuse.

### DTC (Diagnostic Trouble Code)
A standardized code (SAE J2012 format, e.g., P0301) that a vehicle's computer sets when a monitored parameter falls outside expected range — it identifies the circuit or condition detected, not the failed component.

**In use:** "P0301 tells us cylinder 1 is misfiring — it doesn't tell us if that's the coil, the plug, the injector, or a vacuum leak leaning out that cylinder."

**Common misuse:** treating the code's plain-language description as a parts list — replacing "the ignition coil" because the code mentions a misfire, without a confirming test.

### Freeze frame
A snapshot of engine parameters (RPM, load, fuel trims, coolant temp, and more) that the computer records at the exact moment a DTC sets — the only record of the conditions under which the fault occurred.

**In use:** "Freeze frame shows this set at idle with LTFT over 20% — that's a lean condition at idle, not a load-related fault."

**Common misuse:** clearing codes before pulling freeze frame data, which destroys this evidence and leaves nothing to compare against on a re-scan.

### Fuel trim (STFT / LTFT)
Short-term (STFT) and long-term (LTFT) fuel trim are the percentage adjustments the ECU makes to injector pulse width to hold the target air-fuel ratio; a positive number means the computer is adding fuel (lean condition), negative means it's pulling fuel (rich condition).

**In use:** "LTFT is pinned at +22% at idle — that's the ECU compensating for unmetered air, so start with a smoke test, not a coil."

**Common misuse:** reading only the code and ignoring the trim's sign and magnitude, which is what actually distinguishes a lean-air-intrusion cause from an ignition cause.

### Pending vs. confirmed vs. history code
A **pending** code has triggered once and needs a second occurrence (or drive cycle) to confirm; a **confirmed/active** code has met the threshold and set the MIL; a **history** code previously confirmed but is not currently active.

**In use:** "It's a pending code with no matching symptom right now — document it, don't chase it as if it were active."

**Common misuse:** treating any retrieved code as equally urgent regardless of status, which leads to diagnosing an intermittent, self-clearing condition as if it were a persistent fault.

### Book time
The labor hours a repair-information labor guide (Mitchell 1 ProDemand, Motor, ALLDATA) assigns to a specific job on a specific vehicle, used to calculate flat-rate pay and customer billing regardless of the technician's actual clock time on the job.

**In use:** "Book time on this water pump is 4.2 hours because it's behind the timing cover — that's what gets billed and what the tech gets paid, even if it takes him 3.5."

**Common misuse:** treating book time as a ceiling on how much diagnostic thinking a job deserves, rather than as a labor-billing figure separate from diagnostic quality.

### Comeback
A vehicle returning with the same complaint (or the same code) after a repair was billed as complete, typically handled under a shop's no-charge redo policy.

**In use:** "That's a comeback, not a new complaint — the original RO shows no confirming test was run before the coil was replaced."

**Common misuse:** logging a returning vehicle as a brand-new billable job instead of a comeback, which hides the diagnostic-quality signal a rising comeback rate is supposed to surface.

### Flat rate / efficiency percentage
Flat rate is a pay structure compensating a technician per the labor guide's book time on completed jobs rather than clock hours worked; efficiency percentage is flagged (billed) hours divided by clock hours actually on site.

**In use:** "He's running 140% efficiency this month, but almost all of it is on brake jobs — his diagnostic-heavy jobs are closer to 90%, which is the number that actually matters here."

**Common misuse:** treating overall efficiency as a single quality signal, rather than breaking it down by job type — high efficiency on routine jobs is good; sustained high efficiency specifically on ambiguous multi-system diagnostics is a flag.

### TSB (Technical Service Bulletin) vs. recall
A TSB is a manufacturer-published repair guidance document for a known issue on specific VIN ranges, usually not safety-related and not free to the customer unless covered by warranty; a recall is a safety- or emissions-related mandatory free repair.

**In use:** "There's a TSB for exactly this symptom on this platform with a revised part number — check it before diagnosing from scratch."

**Common misuse:** assuming a TSB means the repair is free, or assuming a recall notice covers a similar-sounding but functionally different complaint.

### Warranty labor rate vs. customer-pay (door) rate
The customer-pay/door rate is the shop's posted hourly labor rate charged to non-warranty customers; the warranty labor rate is what the manufacturer reimburses the shop for warranty work, which most states now tie by statute to the shop's own recent customer-pay average rather than letting the OEM set it unilaterally low.

**In use:** "This is inside the powertrain warranty, so it's billed at our retail-reimbursement rate, not our $165 door rate — check which one applies before quoting the customer a number."

**Common misuse:** assuming warranty work pays the same as customer-pay work at the same labor hours, which ignores the rate and markup differences that make the two economically different jobs.

### Parts cannon
Informal trade term for replacing components sequentially based on a code's likely-associated parts, without a confirming test, until the symptom happens to go away.

**In use:** "That's a parts-cannon repair order — three components swapped, no freeze frame, no confirming test on any of them."

**Common misuse:** using it only to describe obviously bad diagnosis, when it equally describes a technically-competent tech skipping the confirming test under time pressure on a single, seemingly obvious part swap.

### Needed repair vs. advisory (upsell) finding
A needed repair addresses the customer's stated complaint with data confirming the cause; an advisory finding is a wear condition observed during the job that isn't the cause of today's complaint but is worth flagging against a stated threshold or interval.

**In use:** "The intake gasket is the needed repair for the misfire complaint. The belt cracking and the marginal battery are advisories — separate line, separate decision, customer can decline either."

**Common misuse:** presenting an advisory finding with the same urgency and on the same line as the confirmed repair, so the customer can't tell what's required today from what's merely prudent soon.

### ASE certification (by letter code)
Certification from the National Institute for Automotive Service Excellence in a specific system category (A1 Engine Repair through A9 Light Vehicle Diesel, plus specialist add-ons like L1); "Master Automobile Technician" specifically means A1–A8 all passed.

**In use:** "He's A5 and A6 certified, not a Master Tech — brakes and electrical, not engine performance, so route the misfire diagnostic to someone else."

**Common misuse:** treating "ASE certified" as a single undifferentiated credential, when the letter category is the entire point — a brakes certification says nothing about electrical-diagnostic competence.
