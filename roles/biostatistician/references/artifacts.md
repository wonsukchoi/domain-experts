# Artifacts

Filled skeletons. Populate bracketed fields; structure and thresholds are the reusable part.

## Statistical Analysis Plan (SAP) skeleton — clinical trial

```
Trial: [name/ID]
Phase: [I / II / III / IV]
Estimand: [treatment policy / hypothetical / composite / while-on-treatment strategy] for [population], accounting for intercurrent events: [dropout, rescue medication, death — specify handling for each]
Primary endpoint: [name], analyzed via [method, e.g. Cox proportional hazards], population = [ITT]
Key secondary endpoints (ordered, gatekeeping): 
  1. [endpoint] — tested only if primary succeeds
  2. [endpoint] — tested only if #1 succeeds
  3. [endpoint] — tested only if #2 succeeds
Sample size: [N per arm], power [___%], based on detecting [effect size] via [test], assuming [event rate/variance assumption]
Interim analyses: [count and timing], efficacy boundary = [method, e.g. O'Brien-Fleming], safety review = [independent DSMB, separate mandate]
Analysis populations: ITT (primary), per-protocol (sensitivity), as-treated (sensitivity) — deviations from ITT criteria: [list]
Missing data / censoring: [MMRM for repeated measures / Kaplan-Meier + Cox for time-to-event], sensitivity analysis under [alternative assumption]
Subgroup analyses: [list], explicitly labeled exploratory unless pre-specified as confirmatory with its own multiplicity allocation
```

## DSMB interim report skeleton

```
Meeting: [scheduled / ad hoc — trigger reason if ad hoc]
Data cutoff: [date], [N] patients enrolled, [N] events accrued ([X%] of target)
Efficacy summary: [point estimate, CI] vs. pre-specified boundary [value] — boundary crossed: [yes/no]
Safety summary:
  Serious adverse events: [N (rate) treatment] vs. [N (rate) control], [event of specific interest]: HR [value], 95% CI [___, ___]
  Clinical assessment: [plausibility given mechanism, consistency of direction/magnitude with prior data]
Recommendation: [continue as planned / continue with modification / ad hoc adjudication requested / stop for efficacy / stop for futility / stop for safety]
Basis: [statistical boundary crossed and/or clinical judgment rationale — state which]
Next scheduled review: [date/event trigger]
```

## Survival analysis output shell

```
Endpoint: [time to event name]
Population: [N per arm], [N] events, [N] censored per arm
Median time-to-event (Kaplan-Meier): [value, 95% CI] treatment vs. [value, 95% CI] control
Log-rank test: p = [value]
Cox model hazard ratio (adjusted for [covariates]): [value], 95% CI [___, ___], p = [value]
Proportional hazards assumption check (Schoenfeld residuals): [assumption holds / violated — if violated, report RMST or time-varying model instead]
Restricted mean survival time at [time horizon] (if PH assumption violated): [value] treatment vs. [value] control, difference [value], 95% CI [___, ___]
```

## Multiplicity gatekeeping order (example structure)

| Order | Endpoint | Tested only if | Alpha allocated |
|---|---|---|---|
| 1 | Primary (e.g. time to major bleeding) | Always tested first | Full α (e.g. 0.05, minus interim spend) |
| 2 | Key secondary 1 (e.g. stroke reduction) | Endpoint 1 succeeds | Inherits α from #1 (closed testing) |
| 3 | Key secondary 2 (e.g. all-cause mortality) | Endpoint 2 succeeds | Inherits α from #2 |
| 4+ | Remaining secondaries / exploratory | Independent of above | Reported descriptively, not confirmatory |
