# Red flags

### Mash pH reads outside 5.2–5.6 at room temperature
- **Usually means:** water chemistry drift (alkalinity creep from a source-water change) or a grain-bill swap that wasn't re-salted for; second most likely is a miscalibrated or unslope-corrected pH meter.
- **First question:** was this reading taken at room temperature, or mash temperature with a correction applied?
- **Data to pull:** water report for the batch's brew date, grain bill and salt additions logged for the batch, meter calibration log.

### VDK (diacetyl) reads above 0.05 ppm on a lager at day 8–10
- **Usually means:** batch was pulled toward cold crash on an ale-tolerance chart (0.10–0.40 ppm) misapplied to a lager, or fermentation was cut short before yeast finished reabsorbing diacetyl.
- **First question:** which style's threshold was used to judge this reading — is this batch actually a lager or an ale?
- **Data to pull:** GC readout with style tag, fermentation temperature log, day-9 gravity trend.

### Dissolved oxygen at packaging exceeds 50 ppb
- **Usually means:** a transfer or filler seal is drawing air, or CO2 purge/counter-pressure filling isn't fully displacing headspace oxygen; second most likely is a worn check valve on the bright-tank side.
- **First question:** is this reading hot-side or cold-side, and at which specific checkpoint in the line?
- **Data to pull:** DO meter log by checkpoint (post-fermentation, pre-fill, post-fill), filler maintenance log, gas panel purge settings for the run.

### Kettle/whirlpool wort temperature exceeds 80°F/27°C pre-boil
- **Usually means:** underback or mash-out transfer is running hot, exposing wort to hot-side oxidation before the boil even starts.
- **First question:** at which transfer step did the wort cross 80°F, and was it aerated at that point?
- **Data to pull:** brewhouse temperature log by transfer stage, timestamped against the aeration/oxygenation step.

### ABV lands outside ±0.3% of the label claim
- **Usually means:** original or final gravity reading was off (hydrometer/refractometer miscalibration), or a fermentation stall/over-attenuation shifted the real attenuation from the recipe target.
- **First question:** does the OG/FG pair on file reconcile arithmetically to the tested ABV, or is one of those readings the outlier?
- **Data to pull:** OG/FG log for the batch, instrument calibration record, TTB formula on file for that label.

### Pasteurization log shows a run below 140°F
- **Usually means:** a tunnel pasteurizer temperature drop mid-run (steam pressure loss, conveyor speed change) or a probe placement that isn't reading the coldest point in the can/bottle.
- **First question:** was 140°F held for the full validated dwell time, or just touched at the peak?
- **Data to pull:** pasteurizer time-temperature chart for the run, probe calibration record, HACCP CCP log for that batch.

### Milling-consistency SPC chart shows two of three points beyond 2-sigma
- **Usually means:** roller-gap drift on the mill, or a malt-lot change with different kernel size that the gap wasn't reset for.
- **First question:** has the roller gap been checked and re-set against spec since the last malt-lot changeover?
- **Data to pull:** SPC control chart for the milling run, malt lot numbers for the period, roller-gap maintenance log.

### Yeast pitch rate calculated below 0.75M cells/mL per °Plato (ale) or 1.5M (lager)
- **Usually means:** cell-count estimate from an aging or under-propagated starter is stale, or a fresh lab-culture pitch was scaled down without confirming the culture is actually fresh enough to justify the halved rate.
- **First question:** was this pitch rate calculated from a same-day viability count or an assumed number from the prior batch?
- **Data to pull:** hemacytometer/methylene-blue viability count for the pitch, starter/propagation log, wort gravity at pitch.

### Off-flavor or contamination report surfaces after packaging on a dated run
- **Usually means:** infection introduced at a transfer point (tank, hose, filler) rather than in the fermentor itself, especially if only some dated runs are affected and not the whole batch.
- **First question:** which specific tanks, transfer lines, and filler runs does the affected date range trace back to?
- **Data to pull:** batch/lot records for the affected date range, transfer-line cleaning/sanitation log, membrane-filtration spoilage-organism test results.

### A batch is held past its scheduled release for a second consecutive time with no failing retest on file
- **Usually means:** the hold is being applied by habit after an earlier QC scare rather than against this batch's own test result — an overcorrection, not a real failure.
- **First question:** what specific test result on this batch, not a prior one, is out of spec right now?
- **Data to pull:** this batch's own release-test results against its style threshold, hold log with stated reason for each prior hold.

### Working-forum or unverified source is the only backing for a QC cutoff being applied
- **Usually means:** the threshold in use has no traceable published source and no local validation against this house's yeast and process. [heuristic — reflects practitioner-forum consensus, not one authoritative number]
- **First question:** does this threshold trace to a named method or standard (ASBC, TTB, HACCP), or only to an unverified forum consensus?
- **Data to pull:** source citation for the threshold as documented in the SOP, any local validation data comparing it against this house's actual batches.
