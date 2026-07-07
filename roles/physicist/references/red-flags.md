# Physicist — Red Flags

### χ²/dof far from 1 (roughly <0.5 or >2, dof-dependent)
- **Usually means:** below the range — quoted per-point uncertainties are overestimated, or errors are correlated when the fit assumed independence; above the range — errors are underestimated or the model is wrong.
- **First question:** are the quoted per-point uncertainties validated by repeat measurements, or just assumed from instrument specs?
- **Data to pull:** raw residuals vs. fit, per-point error derivation, correlation matrix among data points.

### A "discovery"-level result that only emerged after cuts were tuned looking at the signal region
- **Usually means:** look-elsewhere effect or unconscious bias from an unblinded analysis, not a real effect.
- **First question:** were the analysis cuts frozen before the signal region was unmasked?
- **Data to pull:** analysis log with cut-freeze timestamp, blind-analysis protocol document.

### Statistical error much smaller than a known systematic floor, with no stated systematic budget
- **Usually means:** systematics were computed but not clearly separated in the report, or were never estimated.
- **First question:** what's the leading systematic term and how was it derived?
- **Data to pull:** error-budget table, calibration-run data.

### Combined uncertainty computed by simple quadrature when inputs share a calibration standard
- **Usually means:** correlated errors treated as independent, understating the true combined uncertainty.
- **First question:** do any of the combined measurements share an instrument, calibration reference, or environmental condition?
- **Data to pull:** covariance matrix or correlation coefficients between the input measurements.

### A derived formula's result carries the wrong units, or units were never checked
- **Usually means:** an algebra error upstream that dimensional analysis would have caught immediately.
- **First question:** does every term in the derivation collapse to the expected units?
- **Data to pull:** full derivation with units carried through each step.

### "N-sigma significance" reported without stating the null hypothesis or background model
- **Usually means:** significance is only meaningful relative to a specific background model — an ill-defined null inflates the apparent significance.
- **First question:** what exactly is the null hypothesis being rejected, and what's its own uncertainty?
- **Data to pull:** background-model assumptions and their uncertainty.

### A fit converges to a parameter value at or very near a physical boundary (e.g., zero)
- **Usually means:** the fit is degenerate or the model is misspecified — not that the true value sits at the boundary.
- **First question:** what does the profile likelihood or χ² surface look like near the boundary?
- **Data to pull:** profile likelihood scan, parameter correlation matrix.

### Two independent measurements of the same quantity disagree beyond their combined quoted uncertainty
- **Usually means:** at least one has an underestimated systematic — assume this before assuming a real anomaly.
- **First question:** do the two measurements share a common systematic source (same calibration lab, same detector type)?
- **Data to pull:** independent systematic-error breakdowns for both measurements.

### A control or calibration run wasn't repeated after a hardware or software change mid-experiment
- **Usually means:** drift between the calibration and the affected data-taking period is unaccounted for.
- **First question:** when was the apparatus last calibrated relative to the data run in question?
- **Data to pull:** calibration-log timestamps vs. data-run timestamps.

### Signal-to-noise fails to improve as √N with more averaging (or improves faster than √N)
- **Usually means:** departure from the expected noise-averaging law signals a systematic (drift, 1/f noise) the simple statistical model doesn't capture.
- **First question:** is the noise white (uncorrelated) across averaged samples, or does it show low-frequency drift?
- **Data to pull:** Allan variance or noise power spectrum of the raw signal.
