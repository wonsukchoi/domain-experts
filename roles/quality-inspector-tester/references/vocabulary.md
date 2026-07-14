# Vocabulary

### AQL (Acceptable Quality Level)
The maximum percent defective (or defects per hundred units) that, for sampling inspection purposes, is considered acceptable as a process average, defining the statistical basis of a sampling plan.
**In use:** "This characteristic runs at AQL 1.0% — that's the accepted risk level built into the sample size and acceptance number."
**Common misuse:** Treating AQL as "the defect rate we're guaranteeing" rather than "the defect rate threshold the sampling plan is designed to statistically detect at an accepted risk level" — a passed sample under an AQL plan doesn't mean the lot's actual defect rate is exactly at or below the AQL, only that it's statistically unlikely to be meaningfully worse.

### Acceptance number (Ac) / Rejection number (Re)
In an attribute sampling plan, the maximum number of defects in the sample that still results in lot acceptance (Ac), and the minimum number that results in rejection (Re).
**In use:** "Ac=3, Re=4 for this plan — three defects and we still accept, four and it's an automatic reject."
**Common misuse:** Assuming Ac/Re values are the same across all defect severity categories on the same lot — critical, major, and minor defects typically each have their own separate Ac/Re pair, and a critical defect's plan (often Ac=0) overrides the major/minor plans entirely when triggered.

### Gauge R&R (Repeatability and Reproducibility)
A measurement systems analysis (MSA) study quantifying how much variation in measurement results comes from the measurement system itself (repeatability: same operator/same part variation; reproducibility: different operator/same part variation) rather than actual part-to-part variation.
**In use:** "Gauge R&R on this caliper eats up 35% of our tolerance band — we can't trust a borderline reading from it without accounting for that."
**Common misuse:** Trusting a measurement system's readings as exact without knowing its gauge R&R relative to the tolerance being checked — a system with high R&R relative to tolerance can produce a "fail" reading on a truly good part or a "pass" reading on a truly bad one.

### Critical, major, and minor defects
A defect classification hierarchy: critical defects present a safety hazard or render the product unsafe/unusable; major defects substantially reduce usability without safety risk; minor defects are cosmetic or don't affect function.
**In use:** "That's critical, not major — the classification criteria specifically call out anything at a load-bearing point as critical regardless of visible size."
**Common misuse:** Classifying defect severity by visual impression (how big or obvious it looks) rather than by the defined criteria tied to actual consequence — a small crack at a structural point can be critical while a large cosmetic blemish is minor, and size isn't the deciding factor.

### Producer's risk / Consumer's risk
In sampling inspection, producer's risk is the probability of rejecting a lot that's actually at or better than the acceptable quality level; consumer's risk is the probability of accepting a lot that's actually worse than acceptable.
**In use:** "Tightening the sample size reduces consumer's risk, but it raises producer's risk and inspection cost — there's no free lunch here."
**Common misuse:** Treating sampling plan risk as something that can be eliminated with a "good enough" plan — both risks are inherent to any sampling approach short of 100% inspection, and design choices trade between them rather than removing them.

### Disposition
The formal decision made on an inspected lot or nonconforming item — accept, reject, rework, or hold for further review — recorded with the authority basis for the decision.
**In use:** "Disposition is HOLD, pending engineering review — that's beyond my sign-off authority for a critical finding."
**Common misuse:** Treating disposition as simply "what seems like the right call" rather than a decision bounded by defined authority levels — different disposition types (routine accept/reject vs. an engineering deviation) require different levels of sign-off, and an inspector exceeding their authority creates an improperly authorized record.

### 100% inspection
Inspecting every unit in a lot rather than a statistical sample, typically reserved for safety-critical characteristics or when a sampling plan has failed and root cause hasn't been isolated.
**In use:** "This characteristic gets 100% inspection, not sampling — the consequence of a single escape is too high for AQL economics to apply."
**Common misuse:** Assuming 100% inspection guarantees zero escapes — even full inspection carries some human/measurement error rate, though it's generally lower risk than sampling for catching a low-frequency defect.

### Nonconformance report (NCR)
A documented record of a part, lot, or process deviating from specification, used to track the defect, its classification, investigation, and disposition.
**In use:** "NCR's open on this lot — critical defect found, engineering notified, disposition pending."
**Common misuse:** Treating an NCR as closed once the immediate defect is noted, without recording the actual disposition decision and its authority basis — the NCR's value as a traceability record depends on capturing the full resolution, not just the initial finding.

### Sampling plan (single, double, multiple)
A defined statistical inspection scheme specifying sample size(s) and acceptance/rejection criteria — single plans use one sample, double and multiple plans allow a second (or more) sample if the first is inconclusive, often reducing average inspection cost.
**In use:** "This is a double sampling plan — first sample was inconclusive, so we're pulling the second sample before the accept/reject call."
**Common misuse:** Treating any additional sampling after an initial inconclusive result as "extra scrutiny" rather than recognizing it as a defined part of the plan's own structure — double/multiple sampling plans are designed with this second-sample step built in, not an ad hoc escalation.

### Escape (defect escape)
A defective unit that passes inspection and reaches the customer or the next process stage undetected.
**In use:** "We had a field escape on this exact defect type — that's what triggered the review of whether AQL sampling was the right method for this characteristic."
**Common misuse:** Treating any single escape as proof the inspection process failed — under a sampling plan, some escape rate is a statistically expected, accepted risk, and a single escape doesn't necessarily indicate the plan itself is inadequate (though a pattern of escapes does warrant that review).
