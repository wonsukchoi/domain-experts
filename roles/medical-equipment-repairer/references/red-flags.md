# Red flags

Smell tests a biomed shop lead catches in the first review of a work order, a fleet report, or a survey-prep binder. Format for each: what it usually means, the first question to ask, and the data to pull before anyone signs a device back into service.

### 1. Leakage current within 20% of its IEC 60601/62353 limit

**Usually means:** an aging ground path, corrosion at a connector, or accumulated moisture ingress in a patient-care environment — the reading will likely cross the limit before the next PM cycle even if it technically passes today.

**First question:** "What did this exact device read on its last two electrical-safety tests — is this reading trending toward the limit or stable?"

**Data to pull:** the device's last three electrical-safety test values from the CMMS history, ambient humidity/environment notes for the test location, and whether the same model elsewhere in the fleet is trending the same direction.

### 2. Second fault report on the same asset within ~30 days

**Usually means:** an intermittent hardware or calibration issue that a single bench test won't reproduce reliably — the first "couldn't duplicate" close often just means the failure mode hadn't fully developed yet.

**First question:** "What was logged and closed on the first event — same fault code, same conditions?"

**Data to pull:** both work orders side by side, the device's downloaded event log (not just the technician's summary), and the manufacturer's service-bulletin feed for that model/firmware.

### 3. PM completion rate reported as one blended number across all equipment classes

**Usually means:** a comfortable facility-wide average (e.g. ~96%) is masking a life-support/high-risk subclass running well behind — Joint Commission and CMS weight that subclass far more heavily than the average.

**First question:** "Break the completion rate out by AAMI risk tier — what's the number for life-support equipment alone?"

**Data to pull:** PM completion rate segmented by composite risk score band, list of any life-support asset past its grace period, and the equipment manager's escalation log for those assets.

### 4. A device returned to service after "cleaning the error log and it seemed fine"

**Usually means:** the log was cleared before the fault was actually root-caused, destroying the evidence needed if the same device fails again — especially dangerous if the device was tied to any reported patient event.

**First question:** "Was the event log downloaded and preserved before it was cleared, and is that download attached to the work order?"

**Data to pull:** the work order's attached log export (or lack of one), technician notes on root cause versus just "reset and retested," and whether this asset has any prior events.

### 5. New equipment placed on an AEM (extended) PM interval immediately at install

**Usually means:** someone copied the interval from a similar, longer-fielded model without the one to two years of in-house failure history CMS's AEM policy expects before deviating from the OEM's recommended schedule.

**First question:** "What in-house failure data justifies this interval, or is it still on the OEM default until we have a cycle of history?"

**Data to pull:** install date, OEM-recommended interval, any documented risk-scoring worksheet for this specific model, and whether the equipment class is on the AEM-ineligible list (imaging/radiologic, first maintenance cycle, open recall).

### 6. Vague symptom description sent to the manufacturer on a recall/bulletin inquiry

**Usually means:** the technician is asking a general question ("it alarms sometimes") instead of providing the serial number, firmware version, and exact fault code — which gets a generic or wrong answer back and wastes a cycle.

**First question:** "What's the exact fault code, firmware version, and serial number on the ticket sent to the OEM?"

**Data to pull:** the downloaded fault log, current firmware/software version, and serial number cross-referenced against the manufacturer's known-issue bulletin list.

### 7. A repeat-fault device closed as "no patient harm, no report needed" without a documented determination

**Usually means:** the reporting-obligation question (FDA MDR, internal risk log, recall classification) was skipped rather than answered — the work order shows the repair but not the reasoning that no report was required.

**First question:** "Where's the documented determination that this didn't meet the death/serious-injury reporting threshold under 21 CFR 803.30?"

**Data to pull:** the risk-management sign-off (or absence of one), the facility's incident-classification policy, and the event timeline versus the 10-working-day reporting clock.

### 8. Functional test passed, electrical safety test skipped "because it obviously passed last time"

**Usually means:** schedule pressure short-circuited the return-to-service sequence — the exact failure mode (leakage, ground fault) that electrical safety testing exists to catch is invisible to a functional check.

**First question:** "Show me this repair's electrical-safety test values from today, not from the last PM cycle."

**Data to pull:** today's dated test record, the technician's time-in/time-out on the work order, and whether the shop's return-to-service checklist was completed in full or partially skipped.

### 9. A high-composite-risk equipment class quietly moved to a longer PM interval with no re-score noted

**Usually means:** interval got stretched under capacity pressure ("we're behind, let's push these out") without an actual risk re-score — this is the inverse of over-maintaining, and it's the one that produces a survey finding.

**First question:** "What changed in the risk score to justify the new interval — or did the interval move and the score didn't?"

**Data to pull:** the risk-scoring worksheet's revision history for that equipment class, current PM completion rate for that class, and any recent failure events that should have moved the score in the opposite direction.

### 10. Ground/protective-earth resistance measured with a general multimeter instead of a dedicated electrical safety analyzer

**Usually means:** the test wasn't run at the correct rated test current per IEC 62353, so the reading isn't comparable to the standard's limit and can't be trusted as a pass.

**First question:** "What instrument and test current was used for this ground-continuity reading?"

**Data to pull:** the calibration record of the test instrument used, the test-current setting logged (or its absence), and whether the shop's electrical safety analyzer was available and functioning that day.
