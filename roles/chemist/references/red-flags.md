# Chemist — Red Flags

### Reported result falls between LOD and LOQ but is stated as a number
- **Usually means:** analyst or software defaulted to reporting the raw calculated value instead of applying the "detected, below LOQ" convention.
- **First question:** is this value inside the validated LOQ, or below it?
- **Data to pull:** the method's validated LOD/LOQ from the validation report; compare against the reported value.

### Method validated only on neat reference standards, no matrix spike-recovery study
- **Usually means:** validation was rushed to meet a timeline, or the method was adapted from a compendial procedure without matrix-specific verification.
- **First question:** has this method ever been run against the actual production/real-sample matrix?
- **Data to pull:** the validation protocol's sample list — standards only, or spiked matrix included.

### Peak-purity angle close to or exceeding threshold angle on a "specific" method
- **Usually means:** a co-eluting compound (degradant, impurity, or matrix component) is hiding under the peak of interest.
- **First question:** has this been checked against a forced-degradation or stressed sample, not just a fresh standard?
- **Data to pull:** PDA purity-angle/threshold-angle report; forced-degradation chromatogram overlay.

### Isolated yield >15 percentage points below in-process conversion %
- **Usually means:** workup or purification loss, not incomplete reaction — most commonly emulsion/incomplete extraction or co-eluting fractions discarded during purification.
- **First question:** what was the in-process HPLC conversion versus the final isolated mass — where's the gap?
- **Data to pull:** in-process HPLC/TLC conversion data; workup and purification recovery logs.

### OOS result retested without a documented root-cause investigation
- **Usually means:** time pressure to release/ship overrode investigation discipline — the single most common data-integrity audit finding.
- **First question:** was an investigation opened and root cause documented before any retest?
- **Data to pull:** the OOS investigation record; sequence log showing order of retest vs. investigation sign-off.

### Method %RSD passes but recovery is consistently 90–95% (not 98–102%) across multiple runs
- **Usually means:** a systematic bias (incomplete extraction, matrix suppression in MS detection, or a calibration-curve intercept issue), not random error — precision hides bias.
- **First question:** is the bias consistent in direction and magnitude across runs?
- **Data to pull:** recovery data across all validation runs, plotted by run date/analyst/instrument.

### Calibration curve R² reported without checking residuals or range
- **Usually means:** a high R² can mask a curved (non-linear) relationship if only endpoints are weighted, or the reportable range extends past the highest calibrator.
- **First question:** were unknowns quantified within the bracketed calibration range, or extrapolated?
- **Data to pull:** calibration curve residual plot; unknown sample concentrations vs. calibration range bounds.

### Structure confirmed by a single spectroscopic method (e.g., NMR only, no MS)
- **Usually means:** time or sample-quantity pressure skipped orthogonal confirmation.
- **First question:** does a second, independent method (different physical principle) agree?
- **Data to pull:** full characterization package — NMR, MS, IR as applicable — not just the fastest one run.

### Stability sample assay shows a new peak growing over time under a "validated" method
- **Usually means:** the method wasn't confirmed stability-indicating before the program started, or a degradant is co-eluting with the main peak (masked, not absent).
- **First question:** was the method's specificity confirmed against forced-degradation samples before the first real stability pull?
- **Data to pull:** original method-validation specificity data; current stability chromatogram overlaid against t=0.
