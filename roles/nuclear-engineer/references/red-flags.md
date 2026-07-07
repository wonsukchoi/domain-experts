# Nuclear Engineer — red flags

### Safety analysis reports margin <10% on a design-basis acceptance criterion (e.g. peak clad temperature within 10% of the 2,200°F limit)
- **Usually means:** the analysis is using best-estimate rather than the mandated conservative assumptions, or a recent plant change (power uprate, fuel redesign) eroded margin that wasn't re-baselined.
- **First question:** "Is this the design-basis conservative methodology, or a best-estimate result being compared against the conservative limit?"
- **Data to pull:** the analysis-of-record methodology statement and the most recent FSAR amendment affecting this parameter.

### Redundant safety trains share a single power bus, room, or operator action
- **Usually means:** the design credits redundancy on paper that doesn't survive a common-cause event (fire, flood, seismic, single operator error).
- **First question:** "If this specific room floods or this bus de-energizes, does the backup train still function?"
- **Data to pull:** the electrical separation analysis (IEEE 384 compliance) and the fire/flood/seismic hazard analysis for the shared location.

### A proposed change is screened as "no 50.59 evaluation needed" with no written screening record
- **Usually means:** the screening was done informally/from memory rather than against the actual FSAR description, and a genuine margin-of-safety question got missed.
- **First question:** "Where's the written screening — which FSAR section did you check against?"
- **Data to pull:** the FSAR section describing the affected system/function and the site's 50.59 screening form.

### Dose estimate presented only against the regulatory limit, with no ALARA design-objective comparison
- **Usually means:** the analysis stopped at "legal" instead of evaluating cost-effective further reduction, which is what ALARA actually requires.
- **First question:** "What's the ALARA design objective for this area/occupancy, and did we check cost-effectiveness of getting closer to it?"
- **Data to pull:** Appendix I design objectives table and the last ALARA cost-benefit review for a comparable area.

### PRA importance ranking not consulted before a maintenance-interval change
- **Usually means:** the interval change is being justified by cost or historical failure rate alone, missing that a low-failure-rate component can still have high risk-achievement worth.
- **First question:** "What's this component's Fussell-Vesely and RAW in the current plant PRA model?"
- **Data to pull:** the plant PRA importance-ranking output for the specific component, not a system-level summary.

### Fatigue/aging analysis assumes original design-basis load spectrum with no re-evaluation for license renewal or power uprate
- **Usually means:** cumulative usage factor (CUF) tracking wasn't updated after an operational change that increased cycling (e.g. load-following operation).
- **First question:** "Has the CUF calculation been re-run since the plant started load-following / since the uprate?"
- **Data to pull:** the current CUF tracking log against the ASME Section III fatigue design curve assumptions.

### A "best-estimate" thermal-hydraulic result is used to justify a Tech Spec change with no stated uncertainty bound
- **Usually means:** the methodology isn't an NRC-approved realistic method (which requires quantified uncertainty), or the uncertainty analysis was dropped under schedule pressure.
- **First question:** "Is this an NRC-approved best-estimate-plus-uncertainty methodology, and where's the uncertainty quantification?"
- **Data to pull:** the methodology's NRC Safety Evaluation Report (SER) approval letter and the uncertainty propagation results.

### Shielding calculation rounds the required HVL count down instead of up
- **Usually means:** a design error that under-shields — attenuation factor must clear the target, and a fractional HVL (e.g. 9.73) always rounds up to the next whole HVL.
- **First question:** "Did we round the HVL count up or down, and does the post-shield calculated dose rate actually clear the target with the rounded number?"
- **Data to pull:** the shielding calculation showing both the fractional HVL result and the rounded thickness used.

### Outage schedule pressure produces a "will analyze after startup" note on an open safety question
- **Usually means:** "not yet evaluated" is being informally treated as "acceptable for now," which is exactly the conflation that produces a licensing violation.
- **First question:** "Has this been formally dispositioned as acceptable, or is it genuinely still open?"
- **Data to pull:** the open-item/condition-report tracking log and its disposition status, not the verbal schedule commitment.
