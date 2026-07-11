# Red flags — what a medical dosimetrist notices instantly

Smell tests with thresholds. Any one can be innocent; two or three together mean the plan needs a second look before it moves forward.

### Patient-specific QA gamma pass rate <90% at 3%/2mm local-dose criteria (TG-218 action limit)
- **Usually means:** high modulation factor (>4.5) producing MLC positioning sensitivity, or a genuine machine calibration drift (dose rate, MLC leaf-bank offset).
- **First question:** "Is this systematic across arcs/beams, or isolated to one segment?"
- **Data to pull:** MLC log files for the delivered fractions, modulation factor and total MU for the plan, machine QA log for the week of measurement.

### Hot spot (>105–107% of Rx) located outside the PTV
- **Usually means:** optimizer found a low-resistance path to reduce OAR dose that dumps the spared dose just past the target boundary, or a contouring error left healthy tissue adjacent to a high-dose region unconstrained.
- **First question:** "What structure is the hot spot actually sitting in, and was that structure given an optimization constraint at all?"
- **Data to pull:** isodose overlay at the hot-spot slice, list of structures with no assigned optimization objective.

### PTV D95 <95% with no documented overlap or clinical-override justification
- **Usually means:** either an unaddressed OAR overlap that should have its own subvolume objective, or the optimizer simply ran out of room and nobody flagged it before evaluation.
- **First question:** "Is the shortfall localized to an OAR-overlap subvolume, or spread across the whole PTV?"
- **Data to pull:** DVH split into overlap vs. non-overlap PTV subvolumes, not just the aggregate curve.

### Modulation factor >4.5 or per-segment MU exceeding the linac's tested range
- **Usually means:** the optimizer over-fit to a marginal OAR-sparing gain at the cost of deliverability and QA reliability.
- **First question:** "What OAR metric improved enough to justify this much added complexity?"
- **Data to pull:** plan complexity metrics (MF, aperture area variability), the specific DVH delta gained versus a simpler plan.

### Isocenter or setup shift >5 mm on day-1 CBCT with no adaptive-replan discussion
- **Usually means:** anatomy has changed since simulation (bladder/rectal filling, weight change, tumor shrinkage) in a way the original margin didn't anticipate.
- **First question:** "Is this a one-time setup variance or the start of a systematic anatomic trend?"
- **Data to pull:** cone-beam CT overlay against planning CT, shift log across the first 3–5 fractions.

### Rectum V70 ≥20% or bladder V65 ≥50% not flagged before physician sign-off
- **Usually means:** the plan was evaluated on a summary DVH report without a line-by-line constraint check against the site's protocol table.
- **First question:** "Walk me through which constraints on the protocol table this plan actually meets."
- **Data to pull:** the completed site-specific constraint table (see `references/artifacts.md`), not just the DVH screenshot.

### Independent MU/dose check differs from TPS by >3–5%
- **Usually means:** a beam-modeling error, an incorrect field/arc parameter transcribed between systems, or a tissue-heterogeneity calculation mismatch between the primary and secondary algorithms.
- **First question:** "Which specific field or arc drives the discrepancy — is it uniform across the plan or concentrated in one beam?"
- **Data to pull:** per-beam MU comparison (not just plan total), heterogeneity-correction settings on both calculation engines.

### No collision check documented for non-coplanar or extreme-couch-angle beams
- **Usually means:** the geometry was optimized purely in the TPS's virtual room without confirming it against the actual linac/couch/immobilization hardware.
- **First question:** "Has anyone driven this exact gantry/couch/collimator combination on this machine with this immobilization device?"
- **Data to pull:** vendor-published collision zone diagrams for the specific linac model, physics sign-off on non-standard geometry.

### Mobile thoracic/upper-abdominal target with no 4D-CT or motion-management workflow
- **Usually means:** the target's respiratory excursion was estimated rather than measured, risking a margin sized for typical motion that misses outlier breathing cycles.
- **First question:** "What was the measured excursion on 4D-CT, and does the margin actually cover it?"
- **Data to pull:** 4D-CT MIP/ITV overlay, excursion measurement in each axis.

### Bolus omitted or under-specified on a superficial target near a scar or skin surface
- **Usually means:** the plan was optimized for deep coverage without re-checking the build-up-region dose at a site where skin/scar involvement matters clinically.
- **First question:** "Does the prescribing intent include the skin surface, and does this beam arrangement actually deliver dose there without bolus?"
- **Data to pull:** dose profile through the build-up region at the scar/skin location, bolus thickness and placement instructions on the directive.

### Low-dose bath from VMAT modulation ignored because the high-dose region looks clean
- **Usually means:** the plan was evaluated only against the near-target DVH, missing an integral-dose comparison against a simpler technique — most consequential in pediatric or young-adult patients.
- **First question:** "What's the total-body or contralateral-organ integral dose compared to a static-field alternative?"
- **Data to pull:** whole-body DVH or low-dose-volume metrics (e.g., V5, V10) alongside the near-target DVH.

### Same-day physician sign-off on a plan with a documented coverage/constraint trade, with no written rationale in the chart
- **Usually means:** the tradeoff was discussed verbally but never captured, leaving no record of what was accepted and why if outcomes are reviewed later.
- **First question:** "Where is the written comparison of the alternatives the physician was choosing between?"
- **Data to pull:** the plan directive's tradeoff note (see `references/artifacts.md` template) and the chart sign-off entry.
