# Red Flags

### QC check standard stays within spec but shows 6+ consecutive points trending one direction
- **Usually means:** a reagent, titrant, or reference standard degrading in place; second most likely: an aging consumable (lamp, column, electrode) drifting the instrument response.
- **First question:** when was this reagent/standard/consumable last verified, replaced, or restandardized?
- **Data to pull:** control-chart history for the last 20+ points, reagent/standard prep and lot log, consumable install date.

### Balance, pH meter, or other calibration check drifts by more than half the SOP tolerance over 3 consecutive days
- **Usually means:** instrument needs service; second most likely: an environmental change (HVAC, vibration, humidity) at the bench location.
- **First question:** has anything changed at this bench (location, HVAC setting, nearby equipment) in the last week?
- **Data to pull:** calibration check log, facilities work-order history for the area.

### A result near the method's LOQ is reported as a discrete quantitative value
- **Usually means:** pressure to report a number rather than "detected, below LOQ"; occasionally a genuine misunderstanding of the method's validated range.
- **First question:** is this signal above the method's validated LOQ, not just above the LOD?
- **Data to pull:** method validation LOQ/LOD, raw signal-to-noise for this specific run.

### Reagent or standard bottle in active use has no prep date, expiration, or analyst initials
- **Usually means:** labeling SOP skipped under workload pressure; less commonly, a mislabeled or swapped container.
- **First question:** who prepared this, and can they confirm what's actually in it?
- **Data to pull:** reagent prep logbook, SOP-defined shelf-life table for this reagent class.

### An OOS result is retested immediately with no documented root-cause investigation, and the passing retest is reported as final
- **Usually means:** a data-integrity shortcut under deadline pressure; occasionally a genuine gap in OOS-procedure training.
- **First question:** was a root cause for the first failure identified and documented before the retest was authorized?
- **Data to pull:** OOS investigation form, instrument/standard check history for the original run.

### Chain-of-custody form shows a gap of several hours between sample collection/receipt and login with no noted reason
- **Usually means:** a workflow bottleneck (backlog at intake); occasionally an actual custody breach.
- **First question:** where was the sample, physically, during the gap?
- **Data to pull:** COC form, sample receipt log, building/badge access log if available.

### Incompatible chemicals found stored in the same secondary containment or adjacent shelf
- **Usually means:** storage was reorganized alphabetically or for shelf-space convenience rather than by hazard class.
- **First question:** who last reorganized this cabinet or shelf, and against what reference?
- **Data to pull:** SDS Section 7/10 for each chemical involved, the site's storage compatibility chart.

### One analyst's replicate precision is consistently tighter than the method's validated %RSD across many different analytes
- **Usually means:** results being copied, rounded, or partially transcribed rather than independently measured; less commonly, genuinely exceptional technique on a well-controlled method.
- **First question:** can the raw instrument data for each individual replicate be pulled and compared independently?
- **Data to pull:** raw chromatograms/spectra or instrument audit trail, replicate-level (not summarized) data.

### Hazardous waste container has no accumulation start date, or the date is more than 90 days old
- **Usually means:** the RCRA satellite/90-day accumulation limit has been missed, most often because the container wasn't dated when waste generation started.
- **First question:** when did this specific waste stream actually begin accumulating in this container?
- **Data to pull:** waste log, manifest records, EHS accumulation-area inspection log.

### A method blank shows a detectable signal above the method detection limit (MDL)
- **Usually means:** carryover from a high-concentration sample or standard run immediately before it; second most likely: contaminated reagent or glassware.
- **First question:** what ran immediately before this blank in the sequence?
- **Data to pull:** instrument run-sequence log, blank/carryover history for this method.

### A calibration curve passes the R² acceptance criterion (e.g., >0.995) but the residuals show a systematic pattern rather than random scatter
- **Usually means:** a non-linear response near one end of the calibration range being forced into a linear fit, often driven by the highest or lowest standard.
- **First question:** does removing the extreme calibration point change the fit meaningfully?
- **Data to pull:** residual plot, back-calculated concentration for each individual calibration standard.

### A technician overrides or works around an SOP step "because it obviously doesn't matter for this sample"
- **Usually means:** a genuine method limitation the SOP hasn't caught up to; equally often, a shortcut that will surface as an unexplained deviation later.
- **First question:** has this been raised with the chemist/QA and documented as a deviation, or just done silently?
- **Data to pull:** deviation log, SOP revision history for this step.
