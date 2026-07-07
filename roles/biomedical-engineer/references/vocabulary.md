# Biomedical Engineer — Vocabulary

### Design input
A documented, testable requirement describing what the device must do, derived from user needs — the "what," stated so a verification test can pass or fail against it.
**In use:** "That's not a design input yet — 'reliable delivery' doesn't produce a pass/fail test, give me a cycle count and a failure-rate threshold."
**Common misuse:** Treating a marketing claim or user-needs statement as if it were already a design input without translating it into testable form.

### Design output
The actual engineering artifact (drawing, spec, software, material selection) that implements a design input.
**In use:** "The strain-relief collar drawing is the design output for the occlusion-reduction input — it needs its own verification record."
**Common misuse:** Confusing design output with design input — calling a drawing a "requirement."

### Design verification
Confirming the design outputs meet the design inputs — bench/lab testing against acceptance criteria, answering "did we build it right."
**In use:** "Verification passed on the pressure sensor's 15-minute detection floor; that doesn't tell us anything about validation yet."
**Common misuse:** Treating a passed verification suite as proof the device is safe or usable — it only proves the outputs match the inputs, not that the inputs were correct.

### Design validation
Confirming the finished device meets the user needs in the actual (or realistically simulated) use environment — answering "did we build the right thing."
**In use:** "We need a simulated-use validation study, not another bench verification run, to answer whether patients can actually wear this for 7 days without occlusion."
**Common misuse:** Using "validation" and "verification" interchangeably; they answer different questions and neither substitutes for the other.

### Design History File (DHF)
The compiled record of the entire design process — inputs, outputs, reviews, verification, validation, risk management, and the rationale behind changes — required under 21 CFR 820.30(j).
**In use:** "The DHF needs to show why we changed the seal material, not just that we changed it."
**Common misuse:** Confusing the DHF (the design process record) with the Device Master Record (the manufacturing instructions) — they serve different audiences and audit purposes.

### Device Master Record (DMR)
The compiled set of manufacturing specifications, procedures, and quality-assurance requirements needed to build the device consistently.
**In use:** "The DMR needs the updated torque spec before this goes to the line."
**Common misuse:** Treating the DMR as interchangeable with the DHF — DMR is "how to build it," DHF is "why it's designed this way."

### Design Failure Mode and Effects Analysis (DFMEA)
A structured risk analysis scoring each credible failure mode on severity, occurrence, and detection to compute a Risk Priority Number (RPN) and prioritize mitigation.
**In use:** "This failure mode scores severity 8 regardless of RPN — that trips the mandatory-review rule on its own."
**Common misuse:** Treating RPN as the sole risk metric and ignoring a severity-floor rule that some programs apply regardless of the multiplied score.

### Risk Priority Number (RPN)
Severity × Occurrence × Detection, used to rank and prioritize failure modes for mitigation within a DFMEA.
**In use:** "Post-mitigation RPN dropped from 96 to 32 — still needs documented disposition since severity alone crossed the mandatory-review threshold."
**Common misuse:** Comparing RPNs across programs or products as if the scale were universal — severity/occurrence/detection scoring criteria are program-specific and not directly comparable.

### Use error
A user action or lack of action, during use of the device, that produces a different result than intended by the manufacturer or expected by the user — treated as a design output under IEC 62366, not a user failing.
**In use:** "That's a use error, not a training gap — the fix is a design or labeling change, not a slide deck."
**Common misuse:** Calling a foreseeable use error "user error" and closing it with a training recommendation instead of a design change.

### Critical task
A user task that, if performed incorrectly or not performed, could cause serious harm — the focus of summative usability validation.
**In use:** "Occlusion-alarm acknowledgment is a critical task; that's why it needs the full 15-user validation, not a convenience sample."
**Common misuse:** Applying uniform sample sizes across all tasks instead of concentrating validation rigor on the tasks flagged critical by the use-related risk analysis.

### SOUP (Software of Unknown Provenance)
A software component (often third-party or legacy) integrated into a device without full development-process documentation available to the integrating team.
**In use:** "That library is SOUP for us — we need a risk-based verification wrapper since we can't see its unit test coverage."
**Common misuse:** Assuming a widely-used or previously-shipped software component is automatically "already validated" for a new use context.

### Biocompatibility
The property of a material not producing an adverse biological response when in contact with the body, evaluated per ISO 10993 based on contact type and duration.
**In use:** "The adhesive substitution re-triggers the biocompatibility battery — same category doesn't mean same tested material."
**Common misuse:** Assuming a material change within the "same category" (e.g., another medical-grade adhesive) doesn't require re-testing.

### Process capability index (Cpk)
A statistical measure of how well a manufacturing process can hold a design tolerance, relative to the spread and centering of the process distribution.
**In use:** "Cpk on this dimension is 1.1 — below our 1.33 target, so either loosen the tolerance or tighten the process before transfer."
**Common misuse:** Setting a design tolerance without checking it against Cpk data from the actual manufacturing process, discovering the mismatch only at first-article inspection.

### Design transfer
The formal handoff of a design from R&D to manufacturing, including process validation and confirmation that production processes can reliably reproduce the verified/validated design.
**In use:** "We can't transfer this design until process validation shows Cpk ≥ 1.33 on the critical-to-quality dimensions."
**Common misuse:** Treating design transfer as an administrative handoff rather than a gated activity requiring its own verification (process validation) evidence.

### As Low As Reasonably Practicable (ALARP)
A risk-acceptability principle: a residual risk is acceptable if reducing it further would require effort, cost, or design compromise grossly disproportionate to the risk reduction gained.
**In use:** "Residual risk is disposed ALARP — no lower-risk delivery-line routing exists without redesigning the whole wear-mechanism."
**Common misuse:** Invoking ALARP to close out a risk without documenting what alternative mitigations were actually considered and why they were rejected.
