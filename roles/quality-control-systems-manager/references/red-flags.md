# Red flags — what a quality manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A borderline test result released to production/shipping without additional testing to resolve genuine measurement ambiguity
- **Usually means:** the ambiguity is being resolved in favor of convenience rather than the conservative default the asymmetric cost of a false release calls for.
- **First question:** "Does the measurement uncertainty genuinely straddle the spec line, and if so, has additional testing been done to resolve it before deciding?"
- **Data to pull:** the test result and its stated measurement uncertainty, spec limit, any additional confirmatory testing performed.

### A quality hold decision overridden for schedule reasons with no documented, explicit override rationale
- **Usually means:** quality independence may be nominal rather than real — if holds are routinely overridden under production pressure, the quality function doesn't actually have the authority it claims.
- **First question:** "Was this override documented with a specific, deliberate rationale, or did the hold just quietly not happen?"
- **Data to pull:** the hold decision and override history for this and comparable cases, whether overrides are documented or informal.

### A quality function reporting zero or near-zero defects found over an extended period with no verification of detection capability
- **Usually means:** this could reflect genuine excellence or inadequate detection — the two look identical without data validating that the inspection/testing process actually catches real defects when they occur.
- **First question:** "Has our detection capability been validated (e.g., via a known-defect spike test or gauge R&R study), or are we assuming zero findings means nothing's wrong?"
- **Data to pull:** detection capability validation data, historical defect-finding rate trend.

### A non-conformance closed with a fix addressing only the specific instance, no documented root cause analysis
- **Usually means:** the systemic cause likely remains, and the same failure mode will probably recur, possibly in a different form that doesn't immediately look connected.
- **First question:** "What's the root cause, not just the specific fix applied to this instance?"
- **Data to pull:** the non-conformance's corrective action documentation, whether a root cause analysis (5 Whys, fishbone) was actually performed.

### A CAPA (corrective and preventive action) closed based on documentation completion with no verification the fix actually prevented recurrence
- **Usually means:** the closure may be a paperwork exercise rather than a real quality improvement — the underlying issue could still recur.
- **First question:** "Has recurrence been checked over a meaningful period since the fix was implemented, or was this closed once the paperwork was filed?"
- **Data to pull:** CAPA closure documentation, recurrence data for the relevant period after the fix.

### Cost-of-quality tracking that only shows prevention/appraisal spend, with no visibility into internal or external failure costs
- **Usually means:** the true cost of quality (and any chronic underinvestment in prevention) is invisible, since failure costs — often the largest category — aren't being tracked or attributed back to the quality function.
- **First question:** "What are our internal and external failure costs, not just our prevention and appraisal spend?"
- **Data to pull:** cost-of-quality data across all four categories (prevention, appraisal, internal failure, external failure).

### A supplier-originated defect treated as the supplier's problem alone, with no incoming inspection or corrective action extended to the supplier relationship
- **Usually means:** the receiving organization is treating supplier quality as external, when a shipped product with a supplier-originated defect is still its own quality failure to the end customer.
- **First question:** "Has this defect's root cause been traced into the supplier's process, and is supplier corrective action being tracked as part of our own quality system?"
- **Data to pull:** supplier audit and incoming inspection history, corrective action status with the supplier.

### A statistical process control chart showing a process trending toward a control limit with no investigation triggered before it actually breaches spec
- **Usually means:** an early warning signal is being observed but not acted on, missing the opportunity to catch a drifting process before it produces an actual non-conformance.
- **First question:** "Does this trend warrant investigation now, before it crosses the control limit, rather than waiting for an actual out-of-spec result?"
- **Data to pull:** the control chart trend data, any investigation triggered (or not) by the trend itself.
