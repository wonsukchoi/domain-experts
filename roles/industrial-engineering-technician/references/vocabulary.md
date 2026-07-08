# Vocabulary

### Observed time (OT)
The raw average of the retained stopwatch readings for an element, before any rating or allowance is applied.
**In use:** "OT on E2 came in at 9.10 seconds across 20 retained cycles."
**Common misuse:** treating OT as the standard time and quoting it directly to a supervisor or into a rate table — it hasn't been rated or allowanced yet.

### Normal time (NT)
Observed time adjusted by the rating factor to reflect a defined "normal" pace: NT = OT × rating.
**In use:** "E2 rated 95, so NT is 9.10 × 0.95, or 8.65 seconds."
**Common misuse:** confusing normal time with standard time — NT still has no allowance in it and isn't ready to schedule against.

### Standard time (ST)
Normal time plus the PFD allowance: ST = NT × (1 + allowance). The number the line is actually scheduled and paid against.
**In use:** "Standard time for the whole cycle is 17.85 seconds NT times 1.33, or 23.74 seconds."
**Common misuse:** calling any of OT, NT, or a vendor-quoted cycle time "the standard" interchangeably — they're three different numbers with three different uses.

### Rating (leveling)
A percentage judgment of how the observed operator's pace compares to a defined normal pace, applied per element (except machine-paced elements, locked at 100).
**In use:** "Rated E1 at 100, straight pace — no adjustment needed."
**Common misuse:** applying one rating to an entire multi-element cycle instead of judging pace element by element, especially where one element is machine-paced and shouldn't be rated at all.

### PFD allowance (Personal, Fatigue, Delay)
The percentage added to normal time to account for personal needs, fatigue recovery, and unavoidable delay — sourced from a table (e.g., ILO) as a starting estimate, validated by work sampling for a specific job.
**In use:** "Book allowance was 15%; work sampling measured 32.7%, so we're updating to a 33% working allowance."
**Common misuse:** treating the table value as permanent instead of an estimate to be checked, especially after a process or ergonomics change.

### Foreign element
An irregular occurrence during a time study — a jam, an interruption, a dropped part — that is not part of the normal work cycle and gets logged and excluded by rule, not by feel.
**In use:** "Logged cycle 7 as a foreign element — tape-gun jam, cleared by the tech — and re-timed it as cycle 21."
**Common misuse:** using "foreign element" as a catch-all excuse to drop any inconvenient reading without a documented cause or threshold.

### Work sampling
A statistical technique that estimates the percentage of time spent on defined activity categories from a large number of randomly timed instantaneous observations, rather than continuous stopwatch timing.
**In use:** "Sized the work-sampling study at n=547 for 95% confidence and ±4% precision off a 35% pilot estimate."
**Common misuse:** taking observations on a convenient schedule (every hour on the hour, or only in the morning) and calling it random — the method's validity depends on the sampling actually being random across the full observation window.

### Continuous timing method
A stopwatch technique where the watch runs without resetting between elements; each element's time is derived by subtracting the cumulative reading at the start of the element from the reading at its end.
**In use:** "Ran continuous timing on the 3-element cycle since it's under a minute total."
**Common misuse:** confusing continuous timing's cumulative subtraction with snapback timing's direct per-element read — they use different raw data and different error characteristics.

### Snapback timing
A stopwatch technique that resets to zero at the end of each element, reading each element's time directly.
**In use:** "Snapback works fine here — each element runs 20+ seconds, so read error is a small fraction of the reading."
**Common misuse:** using snapback on very short elements (a few seconds), where the reset action itself introduces error large relative to the element being timed.

### Minimum-cycles check (N')
A formula (e.g., Niebel's N' = [(40√(NΣx² − (Σx)²))/Σx]²) that computes, from a pilot sample's actual variance, how many cycles a time study needs to hit a stated confidence and precision.
**In use:** "N' came back at 15 for the noisiest element; we'd already run 20, so the study clears it."
**Common misuse:** skipping the check entirely and defaulting to a fixed cycle count regardless of how variable the element actually turned out to be.

### Confidence interval / precision
The range around a sample statistic (a mean or a percentage) within which the true value is expected to fall at a stated confidence level; precision is the interval's half-width.
**In use:** "32.7% away-time, 95% CI ±3.93%, so the true figure is very likely between 28.8% and 36.6%."
**Common misuse:** reporting the point estimate alone and letting a reader assume it's exact, or confusing "95% confidence" with "95% of observations."

### Predetermined time system (MTM / MOST)
A method that builds a task's normal time from tabulated times for elemental motions (reach, grasp, move) rather than from a physical stopwatch study — usable before a job physically exists.
**In use:** "Job isn't running yet, so we cross-checked the proposed cycle with an MTM-1 breakdown instead of a stopwatch study."
**Common misuse:** treating an MTM estimate as equally authoritative as a validated physical time study once the job is actually running and can be timed directly.

### Line balance efficiency
Total work content divided by (number of stations × bottleneck cycle time) — a measure of how evenly work is spread across stations, not a measure of throughput.
**In use:** "Efficiency reads 100% at 3 stations, but the bottleneck cycle time — and therefore throughput — didn't change from the 4-station layout."
**Common misuse:** treating a higher balance-efficiency number as automatically meaning higher output; it measures labor utilization across stations, not units per hour.

### Takt time
Available production time divided by customer demand — the pace the line must hold to meet demand, distinct from any individual station's cycle time.
**In use:** "St.3 re-timed at 74.0 seconds, which is now over the line's 67.5-second takt, not just over its own 65-second standard."
**Common misuse:** using "takt time" and "cycle time" interchangeably — takt is a demand-derived target; cycle time is what a station or operator actually measures at.
