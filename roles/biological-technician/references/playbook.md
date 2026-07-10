# Playbook

Operational checklists with concrete thresholds. Defaults, not laws — deviate consciously and log why.

## 1. Assay validation checklist — gates in order, each must pass before the next number means anything

### qPCR standard curve

1. **5+ points, 10-fold serial dilution**, spanning the expected sample concentration range plus one log on each side. Triplicate wells per point.
2. **Efficiency: 90–110%** (slope between roughly −3.10 and −3.58; 100% efficiency = slope −3.32, via efficiency = 10^(−1/slope) − 1). Outside this window, the plate's Cq values are not trustworthy for quantification — troubleshoot before reporting anything.
3. **R² ≥ 0.98.** Passes with efficiency still out of range → look for a single outlier point (usually the lowest-concentration dilution, sensitive to sub-2 µL pipetting error) before blaming the whole curve.
4. **Melt curve single peak** (SYBR-based assays) — a shoulder or second peak invalidates that primer pair regardless of Cq or efficiency.
5. **No-template control (NTC): Cq undetermined, or ≥5 cycles later than the lowest standard.** Earlier than that: contamination — stop and identify source before running samples.

### ELISA / plate-based immunoassay

1. Standard curve: minimum 6 points plus blank, run in duplicate; 4-parameter logistic fit, R² ≥ 0.99.
2. Coefficient of variation (CV) between duplicates ≤ 15% (≤ 20% for the two lowest standards, where signal-to-noise is worst). A pair exceeding this is dropped and flagged, not averaged in anyway.
3. Positive control within the manufacturer's stated range on every plate; a control that's drifted but still "passing" on a trend chart (3 plates in a row moving toward the edge of range) is treated as an early warning, not a pass.

### Western blot

1. Loading control (housekeeping protein) band present and even across lanes before touching the target-protein band — an uneven loading control invalidates any target-band comparison, full stop.
2. Total-protein stain (Ponceau/REVERT) as the primary loading normalization where possible; housekeeping-protein normalization alone is a fallback, since housekeeping expression itself can shift with treatment.
3. Positive control lysate on every gel where a new antibody lot or new blocking buffer is in use.

## 2. Cell culture contamination triage — cheapest, most likely causes first

1. **Bacterial/fungal (visible in 24–72 h):** turbid media, particulates, pH shift (media yellowing fast). Usually a breach in aseptic technique — check the operator's most recent BSC session log and whether gloves/surfaces were wiped with 70% ethanol before and during the session, not just at the start.
2. **Mycoplasma (invisible, slow):** no visible turbidity; suspect if growth rate, morphology, or an unrelated assay (e.g., unexplained qPCR background) drifts gradually across passages with no obvious event. Test by PCR-based mycoplasma kit on a routine schedule (monthly for actively used lines), not only when something looks wrong — by the time it looks wrong it may have spread to every line sharing that incubator.
3. **Cross-contamination between cell lines:** unexpected morphology change, or STR profile mismatch on periodic authentication. Check whether the line was ever handled in the same BSC session as another line without a full clean between — "one cell line at a time" is a rule, not a suggestion.
4. **Media/reagent contamination at the source:** multiple unrelated lines contaminate in the same week → check FBS lot, trypsin, or a shared media bottle before blaming technique. Culture an uninoculated aliquot of the suspect reagent for 48–72 h as a direct test.

Fallback order if contamination recurs after cleaning the BSC and retraining technique: (a) new reagent lots across the board, (b) HEPA filter and BSC recertification check outside the normal annual cycle, (c) quarantine and discard affected lines rather than attempt rescue past passage +3 from the contamination event.

## 3. Calibration and preventive-maintenance schedule (defaults; follow the manufacturer/accreditor's stricter of the two)

| Instrument | Interval | Method | Out-of-tolerance action |
|---|---|---|---|
| Pipettes (single/multi-channel) | Quarterly | Gravimetric, 10 deliveries at min/mid/max of range, ≤ ±1–3% error depending on volume | Pull from service; flag every quantitative result since last-good-cal |
| Analytical balance | Annually + daily check-weight | Calibrated weight set | Pull from service; recheck any measured mass since last daily-check pass |
| Biosafety cabinet | Annually, and after relocation/filter service/12-month lapse | NSF/ANSI 49 field certification | No BSL-2+ work until recertified; retroactively review work since the triggering event |
| Autoclave | Weekly minimum (daily if run more than once/day) | *G. stearothermophilus* biological indicator | Any fail: quarantine the load as non-sterile, rerun cycle, investigate load pattern/cycle selection before next use |
| −80 °C / −20 °C freezers | Continuous logging, reviewed daily | Data logger with alarm threshold (typically ±5 °C from setpoint) | Any excursion beyond threshold: check sample integrity for temperature-sensitive reagents/samples stored there, log disposition per item |
| qPCR thermocycler | Annually | Manufacturer-certified temperature verification | Flag standard curves run since last-good-cal if Cq drift is later observed |

## 4. Deviation and out-of-specification (OOS) handling

1. **Log the deviation the moment it's noticed** — what happened, when, and what step of the SOP it diverges from — even if the run "still looks fine." A logged, harmless deviation costs a sentence; an unlogged one that turns out to matter costs a week of unreconstructable troubleshooting.
2. **Classify:** planned deviation (documented in advance, e.g., substituting an equivalent reagent lot with approval) vs. unplanned (discovered after the fact). Unplanned deviations on anything feeding a regulated or publication-bound result get flagged to the supervising scientist before the data is used, not after.
3. **OOS result** (a QC check, control, or calibration falls outside its acceptance criterion): quarantine the associated data, do not average it in "for now," and don't rerun blind — form a specific hypothesis first (see Decision framework in SKILL.md), then rerun to test it.
4. **Close the loop:** once root-caused, update the SOP or the calibration/PM schedule so the same deviation doesn't require rediscovery. A deviation log with no corrective actions attached is just a diary.
