# Biomedical Engineer — Red Flags

### Design input written as an adjective ("robust," "reliable," "user-friendly") with no numeric acceptance criterion
- **Usually means:** the requirement was copied from a marketing or user-needs document without engineering translation, or the team is deferring a hard spec decision.
- **First question:** "What bench or clinical test would pass or fail against this exact wording?"
- **Data to pull:** the design input specification document and its linked verification protocol (if none exists, the input is untestable as written).

### Design FMEA severity scored from the engineering team's perspective, not worst-realistic patient harm
- **Usually means:** severity is being anchored to "how often engineering thinks this happens" (an occurrence concept) rather than "how bad is the worst credible outcome."
- **First question:** "If this failure mode occurred in the least favorable realistic patient/use scenario, what's the clinical consequence?"
- **Data to pull:** the risk management file's severity scale definitions and any adverse-event or complaint data for comparable failure modes on predicate devices.

### RPN above the program's stated threshold with no assigned mitigation owner or target date
- **Usually means:** the FMEA was completed as a documentation exercise rather than a live risk-management tool.
- **First question:** "Who owns closing this, and by when?"
- **Data to pull:** the FMEA action-item log and its closure status as of the last design review.

### Traceability matrix row with an empty verification AND validation column
- **Usually means:** either the requirement is untested (real gap) or it's a non-testable requirement that should have been reclassified or retired, not left dangling.
- **First question:** "Is this requirement verification-only, validation-only, or genuinely untested?"
- **Data to pull:** the traceability matrix and the design input's classification tag.

### Summative usability validation study with fewer than 15 representative users per critical-task user group
- **Usually means:** the study was scoped to a convenience sample rather than FDA human-factors guidance sample-size expectations.
- **First question:** "What's the basis for this sample size against the critical task list?"
- **Data to pull:** the use-related risk analysis's critical task list and the study protocol's stated statistical justification.

### Biocompatibility test battery unchanged after a patient-contacting material substitution
- **Usually means:** someone assumed "same category of material" is equivalent to "same tested material" — a common and expensive assumption.
- **First question:** "Has the new material's chemical composition and leachable profile been compared to the originally tested material?"
- **Data to pull:** material data sheets (old vs. new) and the biocompatibility risk assessment addendum, if one exists.

### Third-party or legacy software component ("SOUP") integrated with no documented risk assessment
- **Usually means:** the team is treating "it's been used elsewhere" as equivalent to "it's been characterized for this use."
- **First question:** "What edge-case or off-nominal input behavior has actually been characterized for this component in this context?"
- **Data to pull:** the SOUP risk assessment (if one exists) and the component's own test/validation documentation from its origin.

### Design change made after verification testing started, with no documented impact assessment
- **Usually means:** schedule pressure is overriding change control — the change felt small enough to "just make."
- **First question:** "Which verification and validation activities does this change actually touch?"
- **Data to pull:** the change request record and the re-verification/re-validation scope decision tied to it.

### Design History File shows only final-state documents, no versioned change rationale
- **Usually means:** the DHF was assembled retroactively for an audit rather than maintained live through development.
- **First question:** "Why did this design input or output change between this version and the last?"
- **Data to pull:** version history / redline documents for the design input or output in question.

### Process capability (Cpk) for a critical dimension below 1.33 discovered at first-article inspection, not at design
- **Usually means:** the design tolerance was set without checking it against the actual manufacturing process capability.
- **First question:** "Was Cpk for this dimension checked against this process before or after the tolerance was finalized?"
- **Data to pull:** first-article inspection data and the design transfer process-capability study.

### Post-market complaint pattern matches a failure mode the FMEA scored as low-occurrence
- **Usually means:** the occurrence estimate was based on bench data that didn't represent real-world use conditions.
- **First question:** "What's different between the bench test conditions and the reported field-use conditions?"
- **Data to pull:** complaint/CAPA records for the failure mode and the original bench protocol's use-condition assumptions.

### Predicate or prior-generation device cited as justification for skipping a verification test
- **Usually means:** someone is treating "similar" as "identical" to avoid re-running a test on a schedule-critical path.
- **First question:** "What specifically differs between this design and the predicate that could affect this test's outcome?"
- **Data to pull:** the design comparison table between current device and the cited predicate/prior generation.
