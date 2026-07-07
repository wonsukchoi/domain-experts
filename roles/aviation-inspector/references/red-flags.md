### A dual-threshold AD shows compliant on the calendar leg with no corresponding check of the flight-hour leg (or vice versa)
- **Usually means:** The record review checked the easier-to-read column and inferred the other, which is exactly how a fleet goes overdue on the unchecked leg without anyone noticing.
- **First question:** Was the flight-hour leg computed independently from current total time and the last compliance entry, or was it assumed compliant because the calendar leg passed?
- **Data to pull:** Total time at last AD compliance, current total time, and the exact AD interval language ("whichever occurs first" or independent thresholds).

### A maintenance-records custody or tracking-system transition occurred within the last 12 months
- **Usually means:** A data migration is the single most common point where dual-threshold AD logic gets miscoded, defaulted to one leg only, or dropped entirely.
- **First question:** Were dual-threshold ADs re-verified against source records after the migration, or was the new system trusted to have carried the logic over correctly?
- **Data to pull:** Migration date, a sample of dual-threshold AD records pre- and post-migration on the same aircraft, vendor confirmation of how the migration handled multi-condition intervals.

### Sampled compliance dates cluster suspiciously close to the scheduled surveillance visit date
- **Usually means:** Either a genuinely well-timed maintenance schedule, or records backfilled or completed just ahead of an announced inspection rather than on the actual due date.
- **First question:** Do the underlying work orders and parts/labor records support the recorded compliance date, or does only the logbook entry exist?
- **Data to pull:** Work order with technician sign-off and date, parts records if replacement was involved, comparison against the aircraft's flight-hour log for that period.

### A hazard report in the SMS is closed with no documented risk assessment attached
- **Usually means:** The Safety Risk Management pillar processed the report as an administrative close-out rather than actually assessing the risk before the hazard was accepted or mitigated.
- **First question:** Was a risk assessment completed before the hazard was closed, or was the closure entered without one?
- **Data to pull:** The hazard report, any attached risk-assessment documentation, the date of closure versus the date of any related operational change.

### A safety metric has trended in the wrong direction for 2 or more consecutive quarters
- **Usually means:** Either a known, already-being-addressed issue, or a Safety Assurance pillar that isn't generating the management review the trend should trigger.
- **First question:** Is there a documented management review of this trend, and did it produce a corrective action with a tracked completion date?
- **Data to pull:** The metric's quarterly history, minutes or records of any management review, status of any resulting corrective action.

### A certificate holder self-discloses a finding after a records review or inspection on the same item has already begun
- **Usually means:** A disclosure timed to look voluntary but made after FAA discovery, which does not meet the VDRP/ASAP eligibility test regardless of the operator's stated intent.
- **First question:** What is the exact date and scope of the FAA-initiated review, and did the disclosure precede or follow it?
- **Data to pull:** Inspection or review opening date and scope, the disclosure's submission date and content, whether the disclosure covers items already within the review's scope.

### The same regulatory citation or AD tracking failure appears a second time on the same certificate within 12–24 months
- **Usually means:** What looks like an isolated inadvertent finding is actually a recurrence, which changes the compliance-philosophy classification from compliance/administrative action toward legal enforcement.
- **First question:** Does the surveillance history show a prior finding, Letter of Correction, or corrective-action commitment for this same citation or failure mode?
- **Data to pull:** Certificate's surveillance and enforcement history for the prior cycle(s), the prior corrective action taken and whether it was actually implemented.

### A finding is scoped to a single aircraft when the root cause is a shared system, vendor, or process
- **Usually means:** The audit stopped at the sampled aircraft instead of following the cause to every aircraft exposed to it.
- **First question:** What is the root cause of this specific finding, and which other aircraft or records share that same cause?
- **Data to pull:** The root-cause determination, a list of all aircraft that went through the same migration, vendor change, or process the finding traces to.

### An operator requests deferral of a scheduled National Program Guidelines surveillance activity for scheduling convenience
- **Usually means:** Legitimate operational pressure, not new information about the state of compliance — deferring the one check designed to catch a problem is itself a risk during the deferred interval.
- **First question:** Does the certificate's risk tier and surveillance plan permit deferral, and if so, what specifically justifies it beyond scheduling convenience?
- **Data to pull:** The certificate's SAS risk tier and current surveillance plan, the specific reason given for deferral, history of prior deferral requests on this certificate.

### A terminating action exists for a recurring AD but the operator continues repetitive inspections without evaluating it
- **Usually means:** Either a deliberate cost decision (terminating action, e.g. a part replacement, costs more up front than continued inspections) or an overlooked option that would eliminate recurring compliance risk.
- **First question:** Has the operator evaluated the terminating action's cost against the cumulative cost and risk of continued repetitive compliance, and is that evaluation documented?
- **Data to pull:** The AD's terminating-action provision, the operator's cost/decision documentation if any, count of repetitive-inspection cycles completed to date.
