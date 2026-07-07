# Astronomer — Red Flags

### Reported SNR scales linearly with claimed exposure-time increase (e.g. "doubled exposure, doubled SNR")
- **Usually means:** a source-noise-only mental model that ignores background/read noise, or an outright arithmetic error — SNR scales as √t in the noise-dominated regime, not t.
- **First question:** what's the dominant noise term at this target's flux level — source, sky, or read noise?
- **Data to pull:** the exposure-time-calculator output or the raw count-rate breakdown by term.

### Photometric scatter between nights exceeds the photon-noise-predicted error by more than ~3x
- **Usually means:** an uncorrected systematic — flat-fielding residual, differential extinction, unstable transparency — not photon noise.
- **First question:** was differential photometry against local reference stars used, or absolute calibration only?
- **Data to pull:** the reference-star light curve from the same field and night.

### A reported magnitude is given without its zero-point uncertainty
- **Usually means:** the calibration step was treated as a fixed constant rather than a measured quantity with its own error.
- **First question:** what standard-star field and what night's conditions were used to solve the zero point?
- **Data to pull:** the standard-star fit residuals from the photometric solution.

### A target below the detection threshold is simply absent from the results table
- **Usually means:** analysis stopped at "below SNR threshold" without computing the flux upper limit that still constrains the model.
- **First question:** what's the 3σ upper limit at this target's coordinates?
- **Data to pull:** the local background RMS at the source position.

### A telescope-time request has no stated target SNR or ETC output attached
- **Usually means:** the proposal was written science-first without the feasibility math, and is likely to be judged unfeasible-to-evaluate by a review panel.
- **First question:** what specific measurement (SNR, precision) does the requested time achieve?
- **Data to pull:** the ETC run for this instrument/target combination.

### A single planned integration exceeds ~30 minutes in unstable seeing or tracking conditions
- **Usually means:** no sub-exposure or cosmic-ray-rejection strategy, risking loss of the entire integration to one bad frame or tracking drift.
- **First question:** how will cosmic rays and tracking drift be handled across the integration?
- **Data to pull:** the guiding/tracking log or the planned sub-exposure count.

### Claimed precision below ~1% (e.g. a transit depth, a radial-velocity amplitude) with no stated systematic-error budget
- **Usually means:** a statistics-only error bar that misses the systematic floor, which usually dominates at that precision level.
- **First question:** what's the known systematic floor for this technique and instrument combination?
- **Data to pull:** prior calibration or standard-star repeatability data for the instrument.

### Sky background estimated from a small annulus in a visibly crowded field
- **Usually means:** the background estimate is contaminated by flux from a neighboring source, biasing the photometry.
- **First question:** is the field crowded enough that the local background annulus could contain another source?
- **Data to pull:** a finder chart or a deeper reference image of the field.

### Spectroscopic wavelength solution not checked against known reference lines after reduction
- **Usually means:** an unverified wavelength calibration, which silently shifts every derived redshift or velocity by the same offset.
- **First question:** what's the residual, in pixels or km/s, between the fitted solution and known reference lines?
- **Data to pull:** the arc-lamp or sky-line residual plot.

### A claimed detection sits at SNR 3–5 with no independent confirming observation
- **Usually means:** a plausible statistical fluctuation rather than a real signal, especially if many pixels, epochs, or targets were searched (the look-elsewhere effect).
- **First question:** how many independent trials were searched, and has that been accounted for in the significance?
- **Data to pull:** the full search parameter space (pixel count, epoch count, target count).
