# Red Flags

### ALD/CVD step coverage below 95% on a feature past 100:1 aspect ratio
- **Usually means:** precursor starvation at depth from insufficient pulse or purge time, breaking the self-limiting surface reaction; second most likely is a contaminated or degraded precursor source reducing effective reactivity before it reaches the bottom of the feature.
- **First question:** what's the bottom-to-top thickness ratio at the deepest measured point, and does it fall outside the >95% step-coverage spec for this aspect ratio?
- **Data to pull:** CD-AFM or CD-SEM readings at top, mid, and bottom of the feature for the lot in question, plus the pulse/purge timing log for the run.

### CD metrology reading drifts outside calibrated uncertainty (<1 nm) with no corresponding process change
- **Usually means:** CD-AFM tip wear or deformation (tips run ~10 nm radius and degrade with use); second most likely is a real process shift coinciding with a tool PM or precursor lot change.
- **First question:** when was this tip last calibrated, and how many scans has it logged since?
- **Data to pull:** tip calibration and usage history, and the deposition/etch process log for the same time window.

### Defect density rises from ~0.01 to ~0.05 defects/cm² between pilot and scale-up runs
- **Usually means:** a contamination source introduced at scale (particle counts, handling, or a cleanroom class mismatch for the process step) that wasn't present at pilot volume; second most likely is a tool-to-tool variation the pilot single-tool run never exposed.
- **First question:** does the yield curve show the expected nonlinear collapse (e.g., ~70% to ~12% test yield) at this defect density, or is yield holding — meaning the defect count itself may be miscounted?
- **Data to pull:** particle-count logs per ISO 14644-1 class for the affected process step, and lot-level yield data before and after the defect-density jump.

### Nanomaterial exposure control plan cites a PEL instead of a NIOSH REL
- **Usually means:** whoever wrote the plan assumed OSHA has a codified nanomaterial-specific limit and copied the wrong document type; second most likely is the plan was copied from a bulk-material SDS that doesn't apply at the nanoscale.
- **First question:** which specific NIOSH REL (or equivalent advisory limit) applies to this material's form factor, and is it being enforced as the ceiling rather than treated as optional guidance?
- **Data to pull:** the material's SDS, NIOSH's engineered-nanomaterial sampling technical report entry for this substance class, and the site's current exposure sampling results.

### MEMS/NEMS structure shows collapsed or stuck features after wet release
- **Usually means:** stiction from capillary forces dominating at nanoscale during liquid-vapor interface drying; second most likely is a SAM coating that wasn't applied or didn't fully react before drying.
- **First question:** was supercritical CO2 critical-point drying used, or did the release go through a standard liquid-vapor evaporation step?
- **Data to pull:** the release process recipe (drying method and SAM chemistry used, if any) and SEM images of the collapsed structures.

### Nanoimprint overlay exceeds ~10 nm 3-sigma spec on a production run
- **Usually means:** template field-corner deformation accumulating over repeated imprint cycles; second most likely is thermal drift in the imprint tool between calibration checks.
- **First question:** how many imprint cycles has this specific template run since its last inspection, and is the overlay error concentrated at field corners?
- **Data to pull:** template imprint-cycle count and inspection history, and the overlay metrology map (not just the summary 3-sigma number) for the affected lot.

### A nanomaterial pitch leads with a lab-batch result and no batch-to-batch reproducibility data
- **Usually means:** the material is still lab-stage, not manufacturing-ready, and crystal-structure quality or dispersion stability hasn't been characterized across multiple batches; second most likely is the pitch deliberately omits reproducibility data because it's poor.
- **First question:** how many independent batches have been characterized, and what's the variance in the key property (particle size, dispersion, crystal quality) across them?
- **Data to pull:** batch-to-batch characterization records (not the single headline batch) and any existing scale-up attempt history.

### Biomedical nanoparticle delivery design is justified by EPR accumulation alone (no benchmark against the ~0.7% median)
- **Usually means:** the design assumes passive tumor accumulation without accounting for the literature median of well under 1% systemic delivery via EPR; second most likely is the design was carried over from an older framework without revisiting active-targeting mechanisms.
- **First question:** what fraction of administered dose is the design targeting to reach the tumor, and is that number benchmarked against EPR-only literature or against active-targeting data?
- **Data to pull:** the biodistribution study data (if any exists) and the targeting-ligand specification, if the design includes one.

### A production-volume lithography choice is e-beam
- **Usually means:** the process was locked in during R&D and never re-evaluated for the target volume, since e-beam's serial write time (hours per die) makes it a throughput mismatch at production scale; second most likely is the target volume estimate itself changed after the technique was chosen.
- **First question:** what's the current target volume, and was the lithography technique re-scored against DUV or NIL at that volume?
- **Data to pull:** the current volume forecast and the original technique-selection memo's stated assumptions.

### A process deviation is reported without a stated root-cause hypothesis
- **Usually means:** the measurement was taken and flagged as out-of-spec, but no one has yet distinguished instrument error from a real process shift; second most likely is time pressure pushed the lot toward a release decision before triage happened.
- **First question:** has the metrology uncertainty been compared against the size of the measured gap to rule out (or in) instrument error?
- **Data to pull:** the calibrated uncertainty spec for the metrology tool used, and the raw measurement set (not just the pass/fail summary).

### A nanoparticle or nanomaterial characterization report doesn't specify nano-object, nanoparticle, or nanoplate/nanofibre classification
- **Usually means:** whoever wrote the report is using "nanoparticle" as a generic catch-all term rather than the ISO dimensionality-based classification, which changes which exposure and characterization protocol applies; second most likely is the material genuinely wasn't characterized for shape/dimensionality.
- **First question:** what are the material's dimensions in all three axes, and does that place it in the nanoparticle, nanoplate/nanofibre, or nano-object category per ISO/TS 27687?
- **Data to pull:** TEM or SEM images with dimensional measurements across all three axes.
