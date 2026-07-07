# Astronomer — Vocabulary

### Signal-to-noise ratio (SNR)
The ratio of a measured signal to the noise (uncertainty) in that measurement.
**In use:** "We need SNR ≥ 10 for a secure detection, SNR ≥ 30 to characterize the line profile."
**Common misuse:** treating SNR as scaling linearly with exposure time, when in the noise-dominated regime it scales as the square root of integration time.

### Zero point
The magnitude that corresponds to one count (or one count per second) in a given instrument's photometric system, derived by observing standard stars of known magnitude.
**In use:** "Tonight's zero point came out 0.03 mag fainter than the archival value — thin cirrus, most likely."
**Common misuse:** treating the zero point as a fixed instrument constant rather than a quantity that must be re-solved each night, since it depends on atmospheric transparency.

### Differential photometry
Measuring a target's brightness relative to one or more reference stars in the same field and exposure, rather than against an absolute calibration.
**In use:** "The transit light curve is differential against three comparison stars within 30 arcsec of the target."
**Common misuse:** comparing absolute (non-differential) photometry across nights and attributing the resulting scatter to target variability, when it's actually uncorrected night-to-night calibration drift.

### Flat field
A calibration frame (typically from a uniformly illuminated source) used to correct pixel-to-pixel sensitivity variation across a detector.
**In use:** "The residual gradient after flat-fielding is under 1%, so it's not driving the photometric scatter."
**Common misuse:** treating flat-fielding as a fully solved, zero-residual correction, when an imperfect flat is a common source of the systematic floor in precision photometry.

### Dark current
Thermally generated electrons accumulating in a detector pixel independent of incoming light, which must be subtracted using a dark calibration frame.
**In use:** "Dark current is negligible at our operating temperature, so it drops out of the noise budget."
**Common misuse:** assuming dark current is always negligible without checking the detector's actual operating temperature and specification.

### Read noise
The noise added to a pixel's value by the electronics reading it out, independent of exposure time or flux level.
**In use:** "At this flux level we're read-noise-limited, so a longer single exposure helps more than splitting it."
**Common misuse:** ignoring read noise entirely in a hand-calculated SNR estimate, which underestimates required exposure time for faint, short-exposure cases.

### Point spread function (PSF)
The two-dimensional pattern a true point source (like a star) produces on the detector, shaped by the telescope optics and atmospheric seeing.
**In use:** "PSF photometry outperforms simple aperture photometry in this crowded field."
**Common misuse:** conflating the PSF with "seeing" alone — the PSF also includes telescope diffraction and optical aberrations, not atmospheric blurring only.

### Seeing
The blurring of a point source's image caused by atmospheric turbulence, usually quoted as a full-width-half-maximum (FWHM) in arcseconds.
**In use:** "Seeing was 1.8 arcsec most of the night, so we widened the photometric aperture accordingly."
**Common misuse:** using "seeing" and "PSF" interchangeably — seeing is one contributor to the PSF, not the whole of it.

### Aperture photometry vs. PSF photometry
Two flux-extraction methods: aperture photometry sums counts within a fixed radius around a source; PSF photometry fits a model point-spread function to the source.
**In use:** "Switch to PSF photometry once source density gets high enough that apertures start overlapping."
**Common misuse:** defaulting to aperture photometry in a crowded field where overlapping sources bias the aperture sums, when PSF fitting would separate them.

### Systematic error
An error that does not shrink with more data because it comes from a fixed, uncorrected bias in the measurement process, as opposed to random statistical noise.
**In use:** "We're systematic-limited at 0.15% — another ten nights of data won't move that number."
**Common misuse:** assuming that adding more integration time or more nights of data always improves precision, when past a certain point the systematic floor is what's limiting, not statistics.

### Statistical error
Random measurement noise (e.g. photon-counting noise) that decreases as more independent measurements are combined, typically as 1/√N.
**In use:** "The statistical error on the transit depth is already down to 0.03% with this many bins — systematics dominate the total now."
**Common misuse:** reporting only the statistical error as "the uncertainty," omitting the systematic term entirely.

### Upper limit
The maximum flux a non-detected source could have and still be consistent with the data, usually quoted at a stated confidence level (e.g. 3σ).
**In use:** "We report a 3σ upper limit of 2.1 μJy at the source position."
**Common misuse:** omitting non-detections from a results table instead of reporting their upper limits, discarding information the detections alone don't carry.

### Look-elsewhere effect
The increased chance of a false-positive-looking detection when many independent trials (pixels, epochs, targets) are searched, inflating the apparent significance of a marginal signal.
**In use:** "At SNR 4 across 10,000 independent pixels, the look-elsewhere-corrected significance is much lower than it looks."
**Common misuse:** quoting the per-trial significance of a marginal detection without correcting for how many trials were actually searched.

### Standard star
A star with a precisely known, previously calibrated magnitude or flux, used to anchor an instrument's photometric or spectroscopic calibration to a physical scale.
**In use:** "We bracketed the science exposures with standard-star observations at two airmasses to solve for the extinction coefficient."
**Common misuse:** using a single standard-star observation at one airmass to calibrate an entire night, without characterizing how extinction changes with airmass.

### Photometric night
An observing night with stable, well-characterized atmospheric transparency (no significant cloud), allowing an absolute flux calibration to be trusted.
**In use:** "Tonight wasn't photometric — stick to differential photometry, don't try to publish an absolute zero point from it."
**Common misuse:** assuming any night without visible clouds is photometric, when thin, hard-to-see cirrus can still shift the effective zero point.

### Exposure-time calculator (ETC)
Instrument-specific software that predicts achievable SNR for a given target brightness and exposure time (or vice versa), incorporating that instrument's actual throughput, background, and noise characteristics.
**In use:** "Run it through the ETC before you commit to that exposure time in the proposal."
**Common misuse:** substituting a generic textbook photon-noise formula for the instrument's own ETC, missing detector- and site-specific terms the ETC already accounts for.
