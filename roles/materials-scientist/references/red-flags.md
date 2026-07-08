# Red flags

Smell tests a materials scientist catches on a first pass over an XRD pattern, a DSC/TGA scan, a composite-modeling result, or a new-material claim.

### XRD peak reported as "shifted" with no comment on whether its width also changed

- **Usually means:** the analyst read the peak-position change (lattice/chemistry effect) without checking whether broadening (size/strain effect) is also present, risking a size or strain contribution being folded into a lattice-parameter or composition conclusion.
- **First question:** did the FWHM change between the two patterns being compared, and if so, has size/strain broadening been deconvolved (Williamson-Hall) before the shift is interpreted as purely a lattice-spacing change?
- **Data to pull:** the raw diffractograms overlaid, peak position and FWHM for both patterns, and any prior Williamson-Hall or Rietveld analysis on file.

### Crystallite size (Scherrer) reported with no instrumental broadening correction

- **Usually means:** the measured FWHM includes the diffractometer's own instrumental broadening (from slit width, wavelength dispersion), which inflates the apparent broadening and understates the true crystallite size — especially significant when true size exceeds roughly 100-150 nm, where instrumental broadening can be a comparable fraction of the total.
- **First question:** was the instrumental FWHM (from a standard reference material, e.g., NIST SRM 660 LaB6) subtracted or deconvolved from the raw FWHM before applying Scherrer?
- **Data to pull:** the instrument calibration file/standard scan, raw vs. corrected FWHM, and the Scherrer K-value assumed (0.89-0.94 depending on crystallite shape assumption).

### DSC %crystallinity computed with an uncited or unverified ΔH(100%) reference value

- **Usually means:** the "100% crystalline" enthalpy of fusion used as the denominator is itself a modeled or extrapolated literature value specific to a polymorph and measurement method, not a universal constant — swapping the reference source changes every reported crystallinity number without changing anything about the sample.
- **First question:** which literature source and polymorph does the ΔH(100%) value trace to, and is the same value being used consistently across every sample in the comparison?
- **Data to pull:** the DSC thermogram, the ΔHm and ΔHcc integration regions used, and the cited source for the reference enthalpy.

### First-heat DSC scan used to report an "intrinsic" thermal property

- **Usually means:** a first heating scan carries the sample's processing/thermal history (residual stress, prior crystallization state), which a standard second-heat scan (after a controlled cool) erases — reporting a first-heat Tg or Tm as a material-intrinsic property conflates history with intrinsic behavior.
- **First question:** was this from a first heat or a second heat, and if first heat, is the comparison being made against another sample's first heat (consistent) or second heat (not consistent)?
- **Data to pull:** the full DSC program (heat/cool/heat cycle, rates), and confirmation of which heating cycle the reported transition came from.

### Composite property model run with an idealized structural input (assumed full exfoliation, assumed perfect alignment) rather than a measured one

- **Usually means:** the model's algebra is correct but its aspect-ratio, orientation, or volume-fraction input was taken from the formulation recipe rather than from actual structural characterization (XRD, TEM), producing a confidently wrong prediction.
- **First question:** does the structural characterization (XRD gallery spacing, TEM image) actually support the assumed structural state the model used, or does it show an intermediate state (intercalated, partially aligned, agglomerated)?
- **Data to pull:** the model's input parameters and their source, the XRD/TEM data on the same sample, and the measured property being compared against the prediction.

### A "reproducible" new synthesis route reported from fewer than 3 independent batches

- **Usually means:** batch-to-batch scatter in a newly developed synthesis is routinely large enough that a two-batch agreement can be coincidence rather than genuine reproducibility, and a real outlier batch hasn't yet been seen.
- **First question:** how many independent batches (not aliquots of one batch) were run, and what is the batch-to-batch standard deviation on the key property?
- **Data to pull:** the batch log with synthesis dates/conditions, and the property measurement for each independent batch, not just the reported mean.

### Property change reported without a converging second characterization technique

- **Usually means:** the reported mechanism (reinforcement, crystallinity, interfacial adhesion) is a plausible story fit to a single number, not a structurally confirmed cause — several mechanisms can produce the same property delta.
- **First question:** what second, independent technique (microscopy, a different diffraction reflection, spectroscopy) was checked, and does it point at the same structural change as the proposed mechanism?
- **Data to pull:** the full characterization set run on the sample (not just the property test), and whether any of it was actually reviewed before the mechanism was written up.

### TGA weight-loss step near 80-150°C interpreted as decomposition

- **Usually means:** a mass loss in this range is almost always adsorbed moisture or residual solvent leaving the sample, not thermal decomposition of the material itself, which for most organic/polymeric systems doesn't onset until well above 200°C.
- **First question:** was the sample dried or pre-conditioned before the TGA run, and does the weight-loss step correspond to a known solvent/water boiling range rather than a decomposition-consistent temperature for this material class?
- **Data to pull:** the TGA thermogram with derivative (DTG) curve, sample drying/storage history, and a comparison decomposition onset from literature for the material class.

### XRD relative peak intensities used for quantitative phase fraction without checking for preferred orientation

- **Usually means:** platy, needle-like, or otherwise anisotropic crystallites can pack with a preferred orientation on the sample holder, systematically over- or under-representing certain reflections relative to a random-powder reference pattern, which biases a simple intensity-ratio phase-fraction estimate.
- **First question:** does the sample's crystallite morphology (from microscopy) suggest a shape prone to preferred orientation, and was a Rietveld refinement with a texture/preferred-orientation correction used instead of a raw intensity-ratio method?
- **Data to pull:** microscopy images of crystallite morphology, the raw vs. Rietveld-refined phase fractions, and the preferred-orientation correction parameters if refined.

### Tg reported with no stated determination method (onset, midpoint, half-height, or inflection)

- **Usually means:** these four conventions for reading a glass transition off a DSC curve can differ by several degrees C on the same thermogram, and comparing Tg values across sources or samples without matching methods produces an apparent shift that is a methodology artifact, not a real transition change.
- **First question:** which convention (onset, midpoint/half-height, or inflection point) was used to read Tg, and was the same convention applied to every sample being compared?
- **Data to pull:** the raw DSC curve with the determination method marked, and the stated method for any literature value being compared against.
