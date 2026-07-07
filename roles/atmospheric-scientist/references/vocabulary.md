# Atmospheric Scientist — Vocabulary

### CAPE (Convective Available Potential Energy)
A measure (J/kg) of the energy available to a rising air parcel if it becomes buoyant relative to its environment — the fuel for thunderstorm updrafts.
**In use:** "SBCAPE is running 2500 J/kg by 3 PM, so we've got plenty of instability if a trigger shows up."
**Common misuse:** treating high CAPE alone as sufficient for severe weather — without shear to organize the updraft, high-CAPE environments often just produce disorganized, short-lived cells.

### Bulk shear
The vector difference in wind speed and direction between two altitudes (commonly 0-6 km) — organizes storms into long-lived, rotating structures rather than pulse cells.
**In use:** "0-6km shear is 45 kt, that's enough to support supercells if CAPE cooperates."
**Common misuse:** conflating shear with wind speed generally — shear is specifically the *change* with height, not the surface wind.

### Reliability diagram
A verification plot comparing forecast probability bins against the observed frequency of the event in each bin, used to calibrate raw model output.
**In use:** "Pull the reliability diagram before you quote that 70% — last season it verified closer to 55."
**Common misuse:** assuming any single model's ensemble output is already calibrated out of the box — most raw ensemble products are overconfident (too sharp) without a season of local verification behind them.

### Brier score
A verification metric scoring the accuracy of probabilistic forecasts — mean squared error between forecast probability and the binary outcome (0 or 1), lower is better.
**In use:** "Our Brier score for this parameter dropped from 0.19 to 0.14 after we started calibrating against the reliability table."
**Common misuse:** comparing Brier scores across different base rates without decomposing into reliability/resolution/uncertainty components — a low base-rate event can produce a deceptively low Brier score even from a poor forecast.

### POD (Probability of Detection)
Fraction of actual events that were correctly warned — hits / (hits + misses).
**In use:** "Seasonal POD for tornado warnings is running 78%, in line with the national average."
**Common misuse:** optimizing POD alone, which trivially reaches 100% by warning everything — must be read alongside FAR.

### FAR (False Alarm Ratio)
Fraction of issued warnings that did not verify — false alarms / (hits + false alarms).
**In use:** "FAR crept up to 55% this quarter, we may be warning too aggressively on marginal signatures."
**Common misuse:** treating any nonzero FAR as a failure — a well-calibrated warning system for a life-safety hazard accepts a structurally higher FAR because the cost of a miss vastly exceeds the cost of a false alarm.

### CSI (Critical Success Index)
A combined verification metric — hits / (hits + misses + false alarms) — that penalizes both misses and false alarms simultaneously.
**In use:** "CSI for this warning type sits around 0.35, which is typical for tornado warnings nationally."
**Common misuse:** expecting CSI values near 1.0 — for rare, hard-to-detect events like tornadoes, CSI in the 0.3-0.4 range is normal and does not indicate poor forecasting.

### Ensemble spread
The range of outcomes across an ensemble's individual members, representing the model's estimate of forecast uncertainty at that point in time.
**In use:** "Spread has widened a lot on days 5-7, so I'm not going to commit to a categorical forecast that far out."
**Common misuse:** reading narrow spread as high confidence when it can also result from all members sharing the same systematic bias (correlated error, not genuine agreement).

### Watch vs. Warning vs. Advisory
A watch means conditions are favorable for a hazard to develop over a broad area/time window; a warning means the hazard is occurring or imminent at a specific location; an advisory covers a less-severe but still hazardous condition.
**In use:** "We're in a watch right now, but that cell 20 miles out just went warning-criteria on radar."
**Common misuse:** using "warning" colloquially for any weather alert — the tiered system carries specific, calibrated meaning about certainty and timing that gets lost when flattened.

### TVS (Tornado Vortex Signature)
A radar-detected rotational velocity signature associated with a developing or ongoing tornado, derived from Doppler velocity data.
**In use:** "TVS just showed up on the 3-degree tilt, rotational velocity 55 kt — that's warning criteria."
**Common misuse:** treating a TVS as visual confirmation of a tornado — it is a radar-inferred rotation signature, not a direct observation; ground truth (spotter, damage survey) is a separate confirmation step.

### Nowcasting
Very-short-range forecasting (0-2 hours) based primarily on extrapolating current observed trends (radar, satellite) rather than numerical model output.
**In use:** "Models have busted on this cell's track, we're nowcasting off radar motion vectors now."
**Common misuse:** conflating nowcasting with model forecasting generally — nowcasting explicitly de-emphasizes model guidance in favor of observed trend extrapolation once the model has diverged from reality.

### Skill score
A general class of metrics expressing forecast performance relative to a reference baseline (climatology or persistence), scaled so 0 = no better than baseline, 1 = perfect.
**In use:** "Skill score against climatology was 0.42 for this event — solidly skillful, not just lucky."
**Common misuse:** quoting raw accuracy (e.g., "we were right 80% of the time") without the baseline comparison — 80% accuracy on an event that occurs 85% of the time climatologically is a negative-skill forecast.

### Categorical outlook (Marginal/Slight/Enhanced/Moderate/High)
SPC's tiered risk communication scale for convective outlooks, each tier corresponding to a range of calibrated probabilities and expected coverage/intensity.
**In use:** "We're in an Enhanced risk today, which corresponds to the 30-45% probability corridor with a reasonable chance of a couple of intense storms."
**Common misuse:** treating the tier name as the complete forecast — it is shorthand layered on top of the actual percentage and corridor, not a replacement for them.
