# Red flags

Smell tests a senior mechanic catches on the first pass through the route data or a repair request. Format for each: what it usually means, the first question to ask, and the data to pull before committing to a repair plan.

## 1. Overall vibration velocity crosses from Zone B into Zone C in under 60 days

**Usually means:** an active, worsening mechanical fault (misalignment, developing bearing defect, or loosening mount) rather than the slow drift of normal wear — a fast zone crossing has a materially shorter time-to-failure than a slow one at the same absolute reading.

**First question:** "What did the spectrum look like at the last two readings, not just the overall number?"

**Data to pull:** overall velocity trend for 6 months, FFT spectra from the last two route visits, bearing/motor temperature trend over the same window.

## 2. 2X running-speed peak amplitude exceeds the 1X peak, with an axial component present

**Usually means:** angular misalignment at a coupling, not imbalance or a bearing defect — imbalance shows as a clean 1X-dominant radial peak with little axial content.

**First question:** "When was this coupling last laser-aligned, and what was the measured offset?"

**Data to pull:** laser alignment history for the coupling, current offset/angularity measurement, soft-foot check results.

## 3. Discrete BPFO/BPFI peaks with sidebands at 1X spacing, amplitude rising month over month

**Usually means:** an advancing bearing defect (stage 2–3) on the specific race the frequency maps to — the rate of amplitude rise, not just its presence, sets urgency.

**First question:** "How fast is this amplitude rising relative to the last two readings, and does the asset's criticality justify replacing before the next scheduled window?"

**Data to pull:** bearing-specific defect frequencies from the manufacturer data sheet, amplitude trend at that frequency, thermal reading at the bearing housing.

## 4. Bearing housing temperature rises more than 10–15°C over its own established baseline

**Usually means:** lubrication breakdown, contamination, or advancing mechanical distress — not ambient/seasonal drift, which moves the whole plant's baseline together rather than one bearing relative to its neighbors.

**First question:** "Is this bearing hotter relative to its own baseline, or is the whole line running hot today?"

**Data to pull:** thermography trend for that specific bearing, ambient temperature log, lubrication schedule and last relube date, oil/grease sample if accessible.

## 5. ISO 4406 particle count or PQ index jumps two codes or more between quarterly oil samples

**Usually means:** a contamination ingress path opened (seal failure, breather issue) or active gear/bearing wear generating metal debris — either way, it typically precedes a vibration-detectable fault by 30–60 days on gearboxes.

**First question:** "Is this a contamination signature (dirt/water) or a wear-metal signature (iron, chromium, copper), and which components do those metals map to?"

**Data to pull:** full oil lab report (viscosity, TAN/TBN, spectroscopy, particle count, ferrography if ordered), seal and breather inspection history, last oil change/top-off date.

## 6. Same failure mode recurs on the same asset within 90 days of a repair

**Usually means:** the prior repair replaced the failed part without correcting the mechanical root cause — misalignment, imbalance, or a load/design mismatch is still present and will produce the next failure on a similar timeline.

**First question:** "What was documented as the root cause on the last work order, and was it actually corrected or just the part?"

**Data to pull:** the prior work order's root-cause field, post-repair alignment/balance verification records (or their absence), load calculation if one was done.

## 7. A LOTO group lockout is used routinely for single-crew jobs instead of individual locks

**Usually means:** a shortcut around 1910.147's individual-lock requirement that works fine until a crew member leaves the job mid-task without notice — the group box protects the group's convenience, not the individual doing the hands-on work at that moment.

**First question:** "Who is physically on this equipment right now, and does each of them have their own lock on the box or the isolation point?"

**Data to pull:** LOTO procedure for this asset, group lockout log, date of the last annual periodic inspection required under 1910.147(c)(6).

## 8. A PM interval has never changed since commissioning despite years of failure history

**Usually means:** the plant is running the vendor's generic default rather than an interval derived from this fleet's demonstrated MTBF — the default is calibrated for an unknown environment, not this one.

**First question:** "What's the demonstrated MTBF for this asset class in this plant, and does the current interval reflect it?"

**Data to pull:** CMMS failure history for the asset class over 24+ months, current PM interval and its source (vendor manual vs. internal MTBF calculation).

## 9. A "better" replacement bearing is requested after a second failure on the same position

**Usually means:** the load or alignment condition at that position exceeds the original design assumption, and a heavier-duty bearing will fail on the same accelerated timeline unless the load itself is corrected — bearing life scales with load cubed, so the fix is rarely just a bigger part number.

**First question:** "Has anyone recalculated the actual radial/axial load at this position against the design assumption, or are we assuming the original spec was right?"

**Data to pull:** original bearing selection calculation (C, P, L10), current alignment measurement, any process change (belt tension, coupling type, load increase) since commissioning.

## 10. PM/inspection labor cost on an asset exceeds a meaningful share of its replacement value annually, with no failure history to justify it

**Usually means:** the asset is being monitored or serviced at an intensity set by habit or a blanket policy rather than by its actual criticality — attention that would be better spent on a higher-consequence asset.

**First question:** "What's this asset's downtime-cost-times-failure-probability criticality score, and does it actually belong in the condition-monitored tier?"

**Data to pull:** annual PM/PdM labor hours and cost for the asset, replacement value, criticality ranking versus other assets on the same line.
