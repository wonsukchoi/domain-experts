# Red flags

### System frequency below 59.95 Hz for more than 1 minute (not a transient dip)
- **Usually means:** a generation trip or sudden load increase exceeding the interconnection's available primary frequency response; second most likely is a metering/PMU fault at the reporting point.
- **First question:** does a second frequency source (a neighboring BA's reading, a different PMU) confirm the deviation?
- **Data to pull:** interconnection-wide frequency trend, recent generator trip alarms, ACE trend for the same window.

### ACE outside the Control Performance Standard limits for more than 30 consecutive minutes
- **Usually means:** AGC is under-responding to a sustained imbalance, commonly because available regulating capacity is exhausted or a unit on AGC has gone unresponsive.
- **First question:** is every unit assigned to AGC actually following its regulation signal?
- **Data to pull:** AGC unit-by-unit response log, regulating reserve capacity remaining, ACE trend.

### Spinning reserve below the N-1 (largest single contingency) requirement
- **Usually means:** reserve was recently deployed to cover a contingency or an economic dispatch decision reduced online regulating capacity without checking the reserve floor first.
- **First question:** was reserve consumed by a real event, or reduced by a dispatch decision?
- **Data to pull:** reserve capacity trend for the past 4 hours, dispatch log, any recent contingency events.

### Bus voltage below 95% of nominal on a heavily loaded transmission path
- **Usually means:** insufficient local reactive power support (capacitor banks offline, generator AVR at its VAR limit) relative to real power flow on that path.
- **First question:** are the capacitor banks and generator VAR sources on that path all in service and within limits?
- **Data to pull:** reactive power flow and VAR reserve on the path, capacitor bank status, generator AVR limit status.

### Voltage declining while real power transfer on the same path is increasing
- **Usually means:** the path is approaching voltage collapse — the classic signature of a reactive-power-starved corridor being pushed with more real power.
- **First question:** can real power transfer on this path be reduced or rerouted while reactive support is added?
- **Data to pull:** P-V (nose) curve position if available, reactive reserve margin, line loading relative to thermal and voltage-stability limits.

### Tie-line interchange deviating from schedule on one specific path while others match
- **Usually means:** a metering error or a scheduling discrepancy isolated to that path, not a system-wide imbalance.
- **First question:** does the counterparty balancing authority's metering agree with this reading?
- **Data to pull:** tie-line meter readings from both sides, current interchange schedule, e-Tag records.

### Two or more generation units on the same fuel source or transmission corridor trending toward derates simultaneously
- **Usually means:** a common-mode risk (fuel supply constraint, extreme weather, a shared transmission path approaching its limit) rather than independent unit issues.
- **First question:** what do these units or paths share in common that could explain simultaneous stress?
- **Data to pull:** fuel supply status, weather forecast for the affected units' locations, shared transmission path loading.

### Frequency approaching 59.5 Hz (first UFLS stage under PRC-006)
- **Usually means:** every prior response stage (AGC, spinning reserve, fast-start capacity, emergency purchases) has been exhausted or was insufficient — this is the last stage before automatic load shed engages.
- **First question:** has emergency energy assistance from neighboring balancing authorities been requested?
- **Data to pull:** full escalation-ladder status (what's been deployed, what remains), neighboring BA emergency assistance availability.

### Reserve restoration not completed within the balancing authority's internal restoration target after a Reportable Balancing Contingency Event
- **Usually means:** fast-start capacity failed to come online as scheduled, or a second event consumed reserve before the first restoration completed.
- **First question:** did the committed fast-start unit reach full output on schedule?
- **Data to pull:** fast-start unit commitment and output log, reserve capacity trend since the event, any overlapping second event.

### A single telemetry point driving an escalation decision with no corroborating source checked
- **Usually means:** the point is legitimate, but it hasn't been verified — a bad PMU, a stuck meter, or a communication fault can produce a reading indistinguishable from a real event until cross-checked.
- **First question:** has this reading been confirmed against the state estimator or a second independent source?
- **Data to pull:** state estimator solution for the same point, adjacent telemetry points, that point's recent data-quality history.
