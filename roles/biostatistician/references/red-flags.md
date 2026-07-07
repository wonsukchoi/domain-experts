# Red Flags

### Per-protocol analysis presented as the primary result in a superiority trial
- **Usually means:** dropout differed by arm and per-protocol excludes the unfavorable cases, inflating the apparent treatment effect; second most likely — a genuine misunderstanding of when per-protocol is appropriate (non-inferiority designs, not superiority).
- **First question:** how does the dropout rate and reason compare between arms, and was ITT run and reported alongside?
- **Data to pull:** ITT vs. per-protocol result side by side, dropout counts and reasons by arm.

### Primary endpoint differs between the registered protocol and the final study report
- **Usually means:** the originally specified primary endpoint didn't show the desired effect and a secondary endpoint that did was promoted; second most likely — a genuine, properly documented protocol amendment made before unblinding.
- **First question:** is there a dated protocol amendment or registry update showing this change was made before database lock?
- **Data to pull:** clinical trial registry version history (e.g. ClinicalTrials.gov protocol versions), SAP version history with sign-off dates.

### Single hazard ratio reported with visibly crossing or diverging Kaplan-Meier curves
- **Usually means:** the proportional-hazards assumption is violated and a single averaged hazard ratio is masking a time-varying effect; second most likely — the assumption wasn't checked at all.
- **First question:** was the proportional-hazards assumption tested (e.g. Schoenfeld residuals), and if violated, was an alternative (RMST, time-varying model) reported?
- **Data to pull:** the Kaplan-Meier plot itself, Schoenfeld residual test output.

### DSMB members have direct reporting or financial relationship to the sponsor's efficacy team
- **Usually means:** the independence the DSMB structure exists to provide is compromised, risking informal information flow that enables endpoint or population switching; second most likely — a disclosed but improperly managed conflict.
- **First question:** what is each DSMB member's relationship to the sponsor, and is there a documented independence charter?
- **Data to pull:** DSMB charter, member conflict-of-interest disclosures.

### Safety signal with wide confidence interval dismissed as "not significant" at an early interim look
- **Usually means:** the review is applying a confirmatory-trial significance standard to a small-sample safety monitoring context, where clinical plausibility and magnitude matter more than crossing a p<0.05 threshold; second most likely — a legitimately underpowered false alarm.
- **First question:** is the point estimate and direction clinically plausible given the drug's mechanism, independent of the interval width?
- **Data to pull:** case-level adjudication of the events in question, mechanism-of-action literature for plausibility.

### More than 3 secondary endpoints tested at nominal alpha with no gatekeeping structure
- **Usually means:** the trial-wide false-positive rate across the endpoint family is uncontrolled and understated in the reported p-values; second most likely — a gatekeeping structure exists but wasn't applied consistently across all secondaries.
- **First question:** is there a pre-specified testing hierarchy or alpha allocation across the primary and all secondaries?
- **Data to pull:** the SAP's multiplicity section, full list of endpoints tested (including any not in the final report).

### Missing-data rate over 10% on the primary endpoint analyzed via complete-case only
- **Usually means:** the missingness mechanism (often differential dropout by arm, or dropout correlated with worsening condition) wasn't tested before defaulting to complete-case; second most likely — MMRM or multiple imputation was run but only complete-case was reported as primary.
- **First question:** does dropout rate or reason differ meaningfully by arm, and was a missing-at-random-aware method (MMRM, multiple imputation) run as a sensitivity check?
- **Data to pull:** missingness rate and reason by arm, sensitivity analysis results under the alternative method.

### Non-inferiority margin set without reference to the historical effect size of the active comparator
- **Usually means:** the margin was chosen to make an underpowered or lower-effect-size study "pass" rather than derived from clinically and statistically justified precedent; second most likely — a genuine but undocumented clinical judgment call.
- **First question:** what historical trial(s) and effect size justify this specific margin?
- **Data to pull:** the margin's justification section in the protocol/SAP, cited historical trial data.
