# Red flags

### A critical-classified defect found within an otherwise-passing AQL sample
- **Usually means:** the overall sample math (major/minor Ac/Re) still applies to those categories, but a critical finding overrides them entirely and requires immediate hold.
- **First question:** has this defect been classified using the defined severity criteria, or lumped in with the general defect count?
- **Data to pull:** the facility's defect classification criteria, the critical-defect acceptance plan (typically Ac=0).

### A borderline measurement result close to a specification limit
- **Usually means:** measurement system uncertainty (gauge R&R) may be large enough relative to the tolerance that the true part condition can't be confidently called from this single reading.
- **First question:** what is this measurement system's known gauge R&R relative to the tolerance being checked?
- **Data to pull:** gauge R&R study results for this measurement system/characteristic, the specific reading's distance from the limit.

### An AQL sampling plan applied to a safety-critical characteristic
- **Usually means:** a standard economic sampling approach was used where the consequence of an escaped defect is too severe for accepted statistical risk.
- **First question:** does this characteristic's failure mode carry a safety consequence that warrants 100% inspection instead of sampling?
- **Data to pull:** the characteristic's risk classification, the facility's policy on inspection method by risk category.

### A disposition decision made that appears to exceed the inspector's defined authority level
- **Usually means:** schedule pressure or an assumption that the decision was "obviously fine" bypassed the required escalation.
- **First question:** does this disposition type (accept, reject, engineering deviation) fall within this inspector's defined sign-off authority?
- **Data to pull:** the facility's disposition authority matrix, the actual sign-off recorded for this decision.

### A supplier or process showing a rising defect rate across consecutive lots, each individually passing its sample
- **Usually means:** a developing trend that lot-by-lot sampling doesn't surface on its own, since each individual lot's pass doesn't account for the pattern across lots.
- **First question:** does defect rate data across recent lots from this source show a trend, or is variation within normal random range?
- **Data to pull:** defect rate history across recent lots for this supplier/process.

### A measurement system used for pass/fail decisions without a current, valid gauge R&R study
- **Usually means:** the system's actual capability for this specific characteristic hasn't been verified, so pass/fail confidence is unknown.
- **First question:** when was gauge R&R last verified for this measurement system and this specific characteristic?
- **Data to pull:** gauge R&R study date and results, measurement system calibration record.

### A defect classified as "minor" that could plausibly affect product function or safety under certain use conditions
- **Usually means:** the classification may not have fully considered the failure mode's actual consequence, only its immediate appearance.
- **First question:** does the defined classification criteria address this specific failure mode explicitly, or was severity assigned by visual impression?
- **Data to pull:** the classification criteria's definition for this defect type, any engineering assessment of the failure mode's consequence.

### A sample size or inspection level selected without matching it to the lot's actual risk profile
- **Usually means:** a default plan was applied without considering whether this specific product/characteristic/supplier history warrants a different level.
- **First question:** does this lot's risk profile (safety-critical characteristic, new supplier, history of issues) justify a tighter plan than the default?
- **Data to pull:** the product/characteristic's risk classification, supplier quality history.

### An accepted lot later associated with a field failure or customer complaint
- **Usually means:** either the sampling plan's accepted risk level was realized (an expected, if unlucky, outcome), or an inspection/classification error occurred.
- **First question:** does the field failure match a defect type this inspection plan was actually designed to catch at this AQL level, or does it suggest a gap in the plan itself?
- **Data to pull:** original inspection record for the lot, the field failure's defect type and how it maps to the classification system.

### A rejected lot re-submitted for inspection without documented rework or corrective action
- **Usually means:** the lot may be re-presented hoping for a different sampling outcome rather than an actual quality improvement.
- **First question:** what specific corrective action was taken between the rejection and this re-submission?
- **Data to pull:** the original rejection record, documented rework/corrective action for this specific lot.
