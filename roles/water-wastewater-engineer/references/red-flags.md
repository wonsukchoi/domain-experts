# Red flags

### Pump starts exceeding 6/hour on a SCADA run-log for a station rated ≤15 hp
- **Usually means:** wet well active storage is undersized relative to the pump's cycling formula (inflow drifting near Qp/2, the worst-case condition), or a level-control/check-valve fault is causing rapid re-trigger.
- **First question:** what's the pump's rated capacity (Qp) versus the current average inflow — is inflow sitting near half of Qp?
- **Data to pull:** SCADA pump-run event log (start/stop timestamps), wet-well level trend over the same window.

### CT compliance log shows a residual and a "contact time" but no documented baffling factor or tracer study
- **Usually means:** the CT credit was computed from theoretical detention time (V/Q) instead of T10, overstating inactivation credit — a defensible-looking number that isn't actually the regulatory-required calc.
- **First question:** has this specific clearwell or contact basin ever had a tracer study, or is the baffling factor an assumed default?
- **Data to pull:** original design report's CT methodology, or the primacy agency's on-file CT compliance determination.

### Force main velocity below 2 ft/s at normal (not peak) operating flow
- **Usually means:** the main was sized for a future population that hasn't materialized yet, or the station is running well below its original design capacity.
- **First question:** what population/flow was this force main originally sized for, versus current actual average flow?
- **Data to pull:** original design report's flow projection, current SCADA flow trend, any odor/corrosion complaint history along the alignment.

### Secondary clarifier reported as "passing" using average-day flow only
- **Usually means:** the SOR/weir-loading check was never run at peak hourly flow, where most clarifier failures (solids carryover, floc breakup) actually occur.
- **First question:** what's the SOR at peak hourly flow, not just average day?
- **Data to pull:** peak-hour flow record (SCADA or permit DMR), clarifier surface area, current effluent TSS during high-flow events.

### Dewatering cake solids below the typical range for the specified technology (e.g., belt press cake <15% TS)
- **Usually means:** inadequate polymer dose, poor feed sludge conditioning, or a mechanical issue (belt tension, feed rate too high for the press's rated hydraulic capacity).
- **First question:** what's the polymer dose (lb active/dry ton) relative to the vendor's design range, and has feed sludge concentration changed?
- **Data to pull:** polymer feed rate log, feed sludge TS%, jar-test or bench-scale polymer optimization data if available.

### Chemical feed pump can't reach its rated minimum flow at the plant's actual minimum-hour demand
- **Usually means:** the feed pump was sized only for maximum-day dose, without checking turndown ratio against minimum-hour flow — risking an overdose (chemical cost, taste/odor, or a compliance parameter like pH) during low-demand periods.
- **First question:** what's the pump's specified turndown ratio, and what dose rate does minimum-hour flow actually require?
- **Data to pull:** pump manufacturer turndown spec, minimum-hour flow record, chemical feed SCADA trend during overnight/low-demand hours.

### A compliance parameter (turbidity, CT, effluent BOD/TSS) passes on monthly average but exceeds the limit during at least one recorded instantaneous or daily reading
- **Usually means:** the design or operating setpoint was tuned to the averaging period the permit reports, not the instantaneous/daily limit the same permit also carries — most SDWA and NPDES permits carry both.
- **First question:** does this permit have a separate instantaneous-maximum or daily-maximum limit in addition to the monthly average, and what's the highest single reading in the period?
- **Data to pull:** full compliance monitoring report (not just the summary average), permit's limit table showing all averaging periods.

### Filter hydraulic loading rate calculated using total installed filter area, not area actually in service
- **Usually means:** the calc didn't account for at least one filter being offline for backwash (N-1 redundancy), understating the real per-filter loading during normal cyclic operation.
- **First question:** how many filters does the plant actually run simultaneously during a normal backwash cycle?
- **Data to pull:** filter backwash SCADA log or operator log showing typical filters-in-service count.

### Digester volatile-solids destruction consistently below ~35%
- **Usually means:** underloading, temperature control failure, hydraulic retention time too short for the feed characteristics, or a toxicity event (e.g., industrial slug load).
- **First question:** what's the digester's operating temperature and hydraulic retention time versus its design values?
- **Data to pull:** digester temperature trend, feed/discharge VS lab data, industrial pretreatment discharge records for the same period.

### Lift station bypass or high-level alarm events correlating with wet-weather (rain) events
- **Usually means:** inflow/infiltration (I&I) into the collection system is exceeding the station's firm pumping capacity during storms — a collection-system problem surfacing at the pump station, not a pump station design defect by itself.
- **First question:** does the alarm timing correlate with rainfall records, and what's the station's firm capacity versus the estimated peak wet-weather flow?
- **Data to pull:** SCADA alarm log timestamps cross-referenced against local rain gauge data, most recent I&I study if one exists for the tributary sewershed.
