# Physicist — Vocabulary

### Systematic error (systematic uncertainty)
An error source that biases a measurement in a consistent direction and doesn't shrink with more repeated measurements — miscalibration, an unaccounted physical effect, or an instrument offset.
**In use:** "Once we beat down the statistical error, the amplitude-correction systematic dominated the budget."
**Common misuse:** treated as interchangeable with statistical error, or ignored entirely once statistics look small — a systematic doesn't average away no matter how many trials are run.

### Statistical error (statistical uncertainty)
The uncertainty arising from random fluctuation in a finite number of measurements; shrinks as 1/√N with more independent trials.
**In use:** "Statistical error on the mean was 0.000716 s after 20 trials."
**Common misuse:** quoted as the total uncertainty when a systematic term is comparable or larger, understating the real error.

### Chi-squared (χ²) / reduced chi-squared (χ²/dof)
A statistic measuring how well a model fits data given the assumed uncertainties; reduced chi-squared divides by degrees of freedom and should be near 1 for a correctly modeled fit with correctly estimated errors.
**In use:** "χ²/dof came out to 0.96 — the timing-error assumption checks out."
**Common misuse:** treating a very low χ²/dof as evidence of an excellent fit, when it usually signals overestimated error bars.

### Blind analysis
An analysis discipline where the signal region is masked and all cuts/model choices are frozen before it's unmasked, to prevent unconscious tuning toward a desired result.
**In use:** "We kept the [124,126] GeV window blinded until the background model was frozen."
**Common misuse:** assuming blinding is only for particle physics — any search for a small or borderline effect benefits from it, and skipping it "because we're careful" is exactly the failure mode it exists to prevent.

### Error propagation
The process of computing the uncertainty on a derived quantity from the uncertainties on its inputs, via quadrature (independent errors) or full covariance (correlated errors).
**In use:** "We propagated the length and timing uncertainties through g = 4π²L/T² using quadrature, since they're independent."
**Common misuse:** applying quadrature to inputs that share a calibration source, which understates the true combined error.

### Look-elsewhere effect
The inflation of apparent statistical significance that occurs when a search is performed over many possible locations, bins, or hypotheses, increasing the chance of a spurious excess somewhere.
**In use:** "The local significance was 4σ, but after the look-elsewhere correction across the full mass range it dropped to 2.5σ."
**Common misuse:** quoting only the local significance of the most striking bin without correcting for how many bins were scanned to find it.

### Significance (sigma, σ)
A measure of how many standard deviations an observed result is from a null-hypothesis expectation, under a stated statistical model.
**In use:** "The excess sits at 3.1σ relative to the background-only model."
**Common misuse:** treating sigma as a standalone quality signal without stating what null hypothesis and background model it's measured against — the same data can yield different sigma values under different background assumptions.

### Calibration standard
A reference measurement or object with a known, traceable value used to establish or verify an instrument's accuracy.
**In use:** "The length was checked against a NIST-traceable gauge block before each run."
**Common misuse:** assuming a one-time calibration remains valid indefinitely, ignoring drift after hardware or environmental changes.

### Degrees of freedom (dof)
The number of independent data points minus the number of parameters fit to the data; used to normalize χ² for a meaningful fit-quality comparison.
**In use:** "20 trials, one fitted parameter (the mean), gives 19 degrees of freedom."
**Common misuse:** using the raw number of data points instead of subtracting fitted parameters, which biases the reduced-χ² interpretation.

### Covariance matrix / correlation coefficient
A matrix (or pairwise coefficient) describing how two or more uncertain quantities vary together; needed for correct error propagation when inputs aren't independent.
**In use:** "The fit parameters had a correlation coefficient of 0.8, so we can't read off their individual errors as if they were independent."
**Common misuse:** reporting individual parameter uncertainties from a correlated fit without noting the correlation, which misleads anyone combining them further.

### Confidence interval
A range constructed by a procedure that, over repeated experiments, would contain the true value a stated fraction of the time (e.g., 95%) — a frequentist statement about the procedure, not a probability statement about the true value itself.
**In use:** "The 95% confidence interval on the coupling constant is [0.42, 0.51]."
**Common misuse:** interpreting a 95% confidence interval as "95% probability the true value is in this range" — that's a credible interval (Bayesian), a related but distinct concept.

### Null result / upper limit
A measurement that finds no statistically significant signal, reported as a bound on how large the effect could be given the data, rather than as an absence of any result.
**In use:** "We set a 95% CL upper limit of 3.8 events on the signal yield."
**Common misuse:** treating a null result as a failed experiment rather than a complete, publishable measurement of an upper bound.

### Dimensional analysis
Checking that the units on both sides of an equation, or through a derivation, are consistent — a fast, free error check independent of the numerical arithmetic.
**In use:** "Dimensional analysis on the derived formula showed it came out in units of energy per volume, not energy — caught the missing factor before we trusted the number."
**Common misuse:** skipped as "too basic to bother with," when it's precisely the basic check that catches a large share of algebra mistakes before data is trusted.

### Precision vs. accuracy
Precision is how reproducible repeated measurements are (small statistical scatter); accuracy is how close the measured value is to the true value (small systematic bias). A measurement can be highly precise and inaccurate at the same time.
**In use:** "The timing was precise to 0.04% but inaccurate by 0.23% until the amplitude correction was applied."
**Common misuse:** using "precision" and "accuracy" interchangeably, when a tight statistical spread says nothing about whether a systematic bias is present.
