# Nanotechnology Engineering Technician — Red Flags

### Carbon nanotube/nanofiber air sample reported as "pass" at or near the 1 µg/m³ REL with no mention of the method's detection limit
- **Usually means:** the sample is being treated as proof of safety rather than "not detected at the floor of what the instrument can measure" — the REL itself is instrument-limited, not toxicologically derived.
- **First question:** what was the method's limit of detection relative to the reported value, and was that margin stated in the report or omitted?
- **Data to pull:** the NIOSH-method air sampling report with LOD, sample volume, and analyte mass, not just the final µg/m³ figure.

### TiO2 exposure assessed against the 2.4 mg/m³ fine-particle REL instead of the 0.3 mg/m³ nanoscale/ultrafine REL
- **Usually means:** the material was classified by chemical label (TiO2) rather than by particle size, missing the 8x-stricter limit that applies once the same compound is in nanoscale form.
- **First question:** what particle-size data (not just the SDS chemical name) was used to select which REL applies?
- **Data to pull:** particle-size distribution or manufacturer spec sheet for the material batch in use, cross-checked against the REL selected in the exposure report.

### Cleanroom garment issued or reused with no lot record showing surface resistivity inside the 10^5–10^11 ohms/sq dissipative band
- **Usually means:** gowning stock was replenished or a non-standard garment substituted without checking fabric spec, leaving a garment that can generate the static charge it's meant to suppress.
- **First question:** does the garment lot's spec sheet or incoming-QC record show a measured resistivity inside 10^5–10^11 ohms/sq, or was dissipative construction assumed from appearance/brand?
- **Data to pull:** garment vendor spec sheet or incoming-QC resistivity measurement for the lot in use.

### Wrist-strap or ESD-grounding check skipped or logged as "N/A" before touching a run
- **Usually means:** the badge/PPE checklist step was treated as a formality rather than a yield-relevant control, especially likely if the technician has run the same tool recently without incident.
- **First question:** was the grounding check performed and logged for this specific run, or copied forward from a prior shift's log?
- **Data to pull:** the tool's daily ESD-check log with timestamps matching the run in question.

### SC1 bath temperature logged outside the 55–75°C controlled-etch band for an exposure over 60 minutes
- **Usually means:** the bath was run at the nominal 80°C spec point on the assumption that "on-spec" and "tightly controlled" are the same thing, without accounting for the tighter band required for long exposures.
- **First question:** what was the exposure duration, and does the logged temperature fall inside 55–75°C for that duration?
- **Data to pull:** bath temperature log at set intervals through the full exposure, not a single start-of-run reading.

### Wet-chemistry ratio (e.g., SC1 at 1:4:20) has any single reagent's dispensed volume off the target ratio by more than ±10%, without a logged deviation
- **Usually means:** chemistry was mixed "close enough" from memory or a partially-empty reagent bottle, on the assumption that a slightly off ratio doesn't matter at this scale.
- **First question:** was the actual dispensed volume of each reagent recorded and checked against ±10% of its target-ratio volume, or only the target ratio from the recipe sheet?
- **Data to pull:** dispense log or scale/flow-meter readout for each reagent in the batch.

### AFM image resolution degrading progressively across a run with no probe-hour tracking
- **Usually means:** tip radius has worn past its manufacturer spec (e.g., beyond ~8 nm for a ScanAsyst probe rated at 2 nm nominal) and the degradation is being attributed to the sample or process instead of the consumable.
- **First question:** how many scan-hours are on the current probe, and does the resolution loss track probe hours or sample changes?
- **Data to pull:** probe usage log (hours or scan count since installation) against the manufacturer's tip-radius spec.

### ALD growth-per-cycle at an in-line checkpoint has moved more than ~10% from its qualified nominal rate
- **Usually means:** precursor delivery (bubbler level, valve, purge line) is degrading mid-run; second most likely, the witness-wafer metrology itself has drifted (calibration or contamination).
- **First question:** has a short verification sub-run been executed to confirm the new rate is stable, or is the disposition being decided off the single checkpoint reading?
- **Data to pull:** full cycle-by-cycle or checkpoint-by-checkpoint GPC history for the run, plus the verification sub-run result if one exists.

### Remaining process cycles/time recalculated using the original nominal rate after a confirmed drift
- **Usually means:** the technician (or a review step) reverted to the qualified spec number because it's "the number on the recipe sheet," rather than projecting forward on the last-confirmed measured rate.
- **First question:** which rate — nominal or last-measured — was used to compute the remaining cycles/time in the current plan?
- **Data to pull:** the disposition log showing which rate fed the remaining-cycle calculation, alongside the raw checkpoint measurements.

### Particle counter check for an ISO-classified bay is more than 6 months old (ISO Class ≤5) or 12 months old (ISO Class >5) per ISO 14644-2's maximum retest interval, yet the bay is still logged as in-class
- **Usually means:** the posted classification is being trusted indefinitely rather than re-verified on the ISO 14644-2 schedule, often because no excursion has been visibly obvious.
- **First question:** when was the bay's classification last verified by an actual particle count, and does that date fall inside the 6-month (ISO ≤5) or 12-month (ISO >5) retest interval?
- **Data to pull:** particle-counter logs for the bay (e.g., ISO 5 threshold of ≤3,520 particles/m³ at ≥0.5 µm) with timestamps.

### Exposure limit used in a report has no OSHA PEL and the report doesn't flag it as a recommendation rather than an enforceable standard
- **Usually means:** a NIOSH REL or vendor SDS limit was applied as if it carried regulatory force, which overstates the certainty of the safety call to whoever reads the report downstream.
- **First question:** does the report explicitly state that the limit used is a REL/SDS recommendation, not an OSHA-enforceable PEL?
- **Data to pull:** the exposure assessment report's stated limit and its citation (OSHA PEL vs. NIOSH REL vs. SDS-stated value).

### A process deviation was corrected in real time but never entered in the process log
- **Usually means:** the technician judged the correction too minor to document, but a downstream reviewer (or the next shift) has no way to distinguish an undocumented fix from an undetected excursion.
- **First question:** is there any log entry — even a one-line note — for the moment the reading went out of tolerance and what was done about it?
- **Data to pull:** the run's full process log cross-referenced against the raw metrology trace for gaps where an out-of-band reading has no corresponding entry.
