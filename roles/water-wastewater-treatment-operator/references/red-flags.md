# Red flags

### Free chlorine residual <0.2 mg/L at a distribution-system endpoint
- **Usually means:** low demand/dead-end main allowing decay, or a recent main break/repair introducing contamination risk; second most likely is a booster/rechlorination station offline.
- **First question:** is this a single endpoint or a spreading pattern across the pressure zone?
- **Data to pull:** distribution residual monitoring log for the past 7 days, work-order history for that main segment, booster station run status.

### Effluent BOD5 or TSS at ≥80% of the NPDES 30-day average limit on any single sample
- **Usually means:** organic/hydraulic overload from I/I or an industrial slug, or a wasting-rate mismatch letting MLSS drift out of the functional F:M band.
- **First question:** has influent flow or BOD load moved outside its normal range in the same window?
- **Data to pull:** influent flow and BOD/TSS trend, current MLSS and computed F:M, industrial pretreatment discharge log.

### MLSS dropping more than 15% between consecutive daily samples with wasting rate unchanged
- **Usually means:** hydraulic washout from a flow event exceeding clarifier or aeration detention capacity; second most likely is a clarifier solids-blanket failure sending solids over the weir.
- **First question:** did influent flow spike in the same window, and by how much relative to design capacity?
- **Data to pull:** influent flow hydrograph, clarifier sludge-blanket depth log, wasting pump run log.

### Turbidity combined filter effluent >0.3 NTU in more than 5% of samples in a month
- **Usually means:** coagulant underdose relative to a shift in raw-water turbidity/alkalinity, or a filter approaching its run-length limit (media fouling, mudball formation).
- **First question:** when was the last jar test run against current raw-water conditions?
- **Data to pull:** raw-water turbidity/pH/alkalinity trend, filter run-time-since-backwash log, most recent jar test results.

### CT value calculated below the required log-inactivation target for the current flow
- **Usually means:** peak instantaneous flow (not average) wasn't used in the T term, or clearwell/contact-basin detention time has shortened due to short-circuiting or a lowered water level.
- **First question:** was the CT calculation run against peak hour flow or average daily flow?
- **Data to pull:** peak-flow SCADA log for the compliance period, clearwell level trend, most recent tracer study if one exists.

### DO in an aeration basin below 1.0 mg/L for more than 2 hours
- **Usually means:** blower or diffuser fault, or an organic load spike consuming oxygen faster than aeration capacity supplies it.
- **First question:** did the alarm coincide with a rain event or a known industrial discharge schedule?
- **Data to pull:** blower run status and amperage, influent flow/BOD trend, diffuser cleaning/inspection history.

### F:M ratio above 0.5 lb BOD/lb MLSS/day for a conventional activated-sludge system
- **Usually means:** organic overload outpacing biomass inventory, commonly from a hydraulic surge diluting MLSS faster than it's replenished.
- **First question:** was the MLSS sample taken during or shortly after a flow surge?
- **Data to pull:** SVI/settleometer result to confirm true biomass condition, wasting-rate log, influent BOD trend.

### SVI trending above 150 mL/g over consecutive days
- **Usually means:** filamentous bulking (often low F:M, low DO, or septic influent) reducing clarifier settling and risking solids carryover to the effluent.
- **First question:** has DO or F:M drifted outside its normal band in the prior week?
- **Data to pull:** DO trend log, F:M trend, microscopic exam results if available.

### A single grab sample exceeding a permit limit that is defined only as a 7-day or 30-day average
- **Usually means:** not itself a violation, but an early signal that the averaging-period limit is at risk if the condition persists.
- **First question:** how many more samples remain in the current averaging period, and at what value would the average breach the limit?
- **Data to pull:** all samples already logged in the current averaging period, permit's exact averaging-period definition.

### Biosolids fecal coliform result above 2,000,000 MPN/g dry weight (Class B threshold, 40 CFR 503.32)
- **Usually means:** an interruption in the stabilization process (digestion time/temperature shortfall, lime dose miscalculation) rather than a sampling error.
- **First question:** did digester temperature or retention time drop below spec in the batch this sample represents?
- **Data to pull:** digester temperature/retention-time log for the batch, stabilization process control records.

### Distribution system pressure dropping below 20 psi anywhere in the system
- **Usually means:** a main break or major leak creating a backflow/contamination risk under SDWA's distribution-system pressure requirement.
- **First question:** is there a confirmed main break, or is this a pump station or elevated-tank level issue?
- **Data to pull:** SCADA pressure zone map, pump station run status, tank level trend.
