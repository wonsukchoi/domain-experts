### Line efficiency below 75% on a newly balanced line
- **Usually means:** task-to-station assignment ignores precedence-driven idle time, or the takt/demand number feeding the balance is stale.
- **First question:** what's the theoretical minimum station count from total work content ÷ takt, and how does it compare to the current station count?
- **Data to pull:** line-balance worksheet, current takt calculation, demand forecast used.

### WIP in front of one station running 2x+ the line's normal buffer
- **Usually means:** that station is the real bottleneck regardless of where the complaints are loudest.
- **First question:** what's this station's cycle time versus takt, measured today, not from the original balance study?
- **Data to pull:** WIP count log by station, current station cycle times.

### Standard time set from a single observed cycle (n=1)
- **Usually means:** no rating factor or PFD allowance was applied — the "standard" is one operator's one day.
- **First question:** what rating factor and allowance percentage were used, and how many cycles were observed?
- **Data to pull:** original time-study raw sheet.

### Changeover time exceeding 10% of available shift time
- **Usually means:** SMED (internal-to-external conversion) has never been applied to this changeover.
- **First question:** how many changeovers per shift, and what's the current internal vs. external split?
- **Data to pull:** changeover log with step-by-step timing.

### Actual output running 10-15% below rated capacity with no line change
- **Usually means:** allowances were underestimated at design time, or unplanned downtime isn't being captured in the standard.
- **First question:** what does the OEE breakdown show — is the gap in availability, performance, or quality?
- **Data to pull:** OEE dashboard, downtime log.

### Operator travel exceeding 40% of observed cycle time
- **Usually means:** the facility layout wasn't designed from a relationship chart — proximity was decided by habit or available floor space.
- **First question:** what does a spaghetti diagram of one full cycle show?
- **Data to pull:** travel-distance/spaghetti diagram, current layout drawing.

### Learning-curve assumption unrevisited after 3+ months of production
- **Usually means:** the labor standard is now stale — either overstated (costing looks worse than reality) or understated (operators can't hit it and get blamed).
- **First question:** what does actual cumulative-average labor hours per unit look like against the assumed curve?
- **Data to pull:** labor-hours-per-unit trend by month since launch.

### Automation payback claimed under 12 months with no stated utilization assumption
- **Usually means:** the vendor's payback model assumes continuous, downtime-free operation.
- **First question:** what utilization rate and changeover allowance did the payback calculation assume?
- **Data to pull:** vendor capital proposal, current line OEE for comparison.

### Bottleneck relieved but total line throughput didn't move
- **Usually means:** the constraint shifted to a new station and was never re-identified (Theory of Constraints' "elevate, then repeat" step was skipped).
- **First question:** which station now has the largest WIP buildup?
- **Data to pull:** updated WIP-by-station log, post-change throughput data.

### Ergonomic lifting index above 1.0 at a manual station
- **Usually means:** the task was rate-increased or redesigned without an ergonomic reassessment.
- **First question:** what's the current NIOSH lifting index or RULA score at that station?
- **Data to pull:** ergonomic assessment, injury/near-miss log for that station.

### Value-added touch time under 30% of total process time
- **Usually means:** a large share of the "standard" is motion, waiting, or handling that a value stream map would expose as non-value-add.
- **First question:** what does a current-state value stream map show for touch time versus wait time?
- **Data to pull:** value stream map with time splits.

### Operators pacing to feel rather than a posted takt
- **Usually means:** there's no visual takt or andon system at the line, so the standard exists on paper but not on the floor.
- **First question:** is takt time posted and visible at each station right now?
- **Data to pull:** photo/audit of current visual management at the line.
