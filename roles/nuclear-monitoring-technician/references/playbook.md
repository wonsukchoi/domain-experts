# Playbook

## Contamination smear survey conversion (filled example)

Equipment leaving an RCA, gas-flow proportional counter, 100 cm2 smear template, 2π efficiency 34% for the beta-gamma mix present, background check current at 40 cpm.

| Step | Value |
|---|---|
| Gross count (1 min) | 620 cpm |
| Background | 40 cpm |
| Net count rate | 620 − 40 = 580 cpm |
| Efficiency (2π, beta-gamma) | 34% (0.34) |
| Corrected activity | 580 ÷ 0.34 = 1,706 dpm/100cm2 |
| Removable action level | 1,000 dpm/100cm2 |
| Result | Exceeds action level by 706 dpm/100cm2 (71% over) — held, decon required |

**Second item, same instrument, for comparison:** gross count 210 cpm, same 40 cpm background, same 0.34 efficiency.
Net = 210 − 40 = 170 cpm. Corrected = 170 ÷ 0.34 = 500 dpm/100cm2. Below the 1,000 dpm/100cm2 action level — released for unrestricted use, logged with the corrected value (not the raw 210 cpm) on the survey record.

## Minimum detectable activity (MDA) check (filled example)

Same counter, background 40 cpm, 1-minute count, 34% efficiency. Using the Currie formula for net count-rate MDA at this count time:

| Quantity | Value |
|---|---|
| Background count rate (Rb) | 40 cpm |
| Count time (t) | 1 min |
| Background counts (B = Rb × t) | 40 |
| σ_B (√B) | 6.32 |
| MDA (net cpm) = 2.71 + 4.65 × σ_B | 2.71 + 4.65 × 6.32 = 32.1 cpm |
| MDA in dpm/100cm2 = MDA(cpm) ÷ efficiency | 32.1 ÷ 0.34 = 94.4 dpm/100cm2 |

**Applied check:** MDA of 94.4 dpm/100cm2 is well below the 1,000 dpm/100cm2 action level, so a 1-minute count on this instrument is adequate to reliably distinguish "clean" from "over the action level." If the same calculation instead produced an MDA above 1,000 dpm/100cm2 (e.g., a lower-efficiency instrument or shorter count time), a "not detected" result on that setup would not be usable evidence of compliance — count time would need to increase, or a more efficient instrument substituted, before survey results against that action level are valid.

## Stay-time calculation from a survey map (filled example)

Job: replace a valve in an area with a non-uniform dose-rate field per the current radiological survey map. RWP lists a single estimated average of 40 mrem/hr for the general area. The survey map shows a 150 mrem/hr hot spot directly at the valve flange, where roughly 10 minutes of the job will actually be spent; the remaining work happens in the surrounding 30 mrem/hr general field. Job dose budget: 100 mrem.

| Approach | Calculation | Result |
|---|---|---|
| Naive (RWP average only) | 100 mrem ÷ 40 mrem/hr | 150 minutes allowed, treated as a flat budget |
| Correct (survey-map-based) | Hot spot: 150 mrem/hr × (10/60 hr) = 25 mrem. Remaining budget: 100 − 25 = 75 mrem. General field time: 75 mrem ÷ 30 mrem/hr = 150 min | 10 min at the flange + 150 min in the general field = 160 min total, with only 25 mrem of the 100 mrem budget spent at the hot spot |

**Applied check:** the naive average-based budget doesn't reserve dose specifically for the hot-spot portion of the job — a worker following it could spend more than 10 minutes at the flange and consume the entire 100 mrem budget well before the valve work is finished, forcing an unplanned mid-job swap. The survey-map-based calculation allocates dose to where the job actually happens, not to a single blended number.
