# Wind farm operations playbook

Filled worksheets for the four recurring operations decisions: availability decomposition, curtailment/PPA reconciliation, spare-parts stocking, and warranty triage.

## 1. Availability and production decomposition model

```
Resource-adjusted expected production = Σ (turbine power curve applied to met-tower wind speed/direction data, per hour, per turbine)

Time-based availability = (turbine-hours ready to operate) / (total turbine-hours in period)
Energy-based (production) availability = actual production / resource-adjusted expected production

Example, this quarter:
  Actual production: 92,000 MWh
  Resource-adjusted expected: 108,000 MWh
  Energy-based shortfall: 16,000 MWh (14.8%)
  Reported time-based availability: 97.8% (meets 97% contractual guarantee)
```

Rule: a time-based availability figure meeting its guarantee does NOT mean the energy-based shortfall is explained — always decompose the energy-based gap into curtailment categories before accepting a "resource variance" conclusion.

## 2. Curtailment reason-code log and PPA reconciliation

| Reason code | Turbine-hours | Avg output during event | Lost/foregone MWh | PPA treatment |
|---|---|---|---|---|
| Grid-operator directive | 210 | 1.8 MW | 378 | Compensable — file claim at PPA curtailment rate |
| Noise ordinance (nighttime) | 620 | 1.8 MW | 1,116 | Uncompensated — contractual operating limitation |
| Negative-price economic curtailment (self-directed) | 380 | 1.8 MW | 684 | Not a loss — avoided negative-price exposure |
| Avian/bat seasonal restriction | 0 (out of season this quarter) | — | 0 | Uncompensated — permit condition |
| Planned maintenance | 340 | 1.8 MW | 612 | Uncompensated — scheduled, excluded from availability guarantee per contract |
| **Unexplained (requires investigation)** | — | — | **13,822** | Pending SCADA-vs-power-curve verification study |

Rule: every curtailment event gets a reason code at the time it's logged, not reconstructed later — reconstructing after the fact is how a compensable grid-directed event ends up miscoded as "other" and the claim window lapses.

## 3. Spare parts stocking plan (by failure probability × lead time)

| Component | Annual failure probability (fleet-wide) | Logistics lead time | Stocking decision |
|---|---|---|---|
| Main bearing | 3-5% | 10-12 weeks | Stock 1 regionally per 20 turbines |
| Gearbox | 2-4% | 8-10 weeks | Stock 1 regionally per 30 turbines, or confirm OEM exchange-unit program |
| Blade bearing (pitch) | 4-6% | 6-8 weeks | Stock 1 on-site per 15 turbines |
| Generator | 1-2% | 8-10 weeks | Order-on-failure acceptable given lower probability, confirm expedited-freight terms in advance |
| Converter/control electronics | 5-8% | 2-4 weeks | Order-on-failure acceptable — short lead time doesn't justify pre-stocking cost |

Decision rule: pre-stock when (failure probability × average lost-production-value per day of downtime × lead-time days) exceeds the carrying cost of holding the part — components with both meaningful failure probability and long lead time (main bearing, gearbox, blade bearing) clear this bar; short-lead-time components usually don't.

## 4. Warranty/service-agreement triage checklist

```
Failure detected: <component, turbine ID, date>
Service agreement type: <full-service OEM / unbundled / expired>
Coverage check:
  - Is this component/failure mode explicitly covered? <yes/no/ambiguous>
  - Is the turbine within the coverage window (age, operating hours)? <yes/no>
  - Does the failure mode qualify (manufacturing defect vs. external damage vs. normal wear)? <check exclusions>
Decision: <file OEM warranty claim / authorize owner-funded repair / dispute pending further review>
Evidence attached: <SCADA data, CMS trend history, maintenance log>
```

Rule: never authorize a major-component repair (gearbox, blade, generator) without completing this checklist first — the cost difference between a warrantied and owner-funded gearbox replacement alone commonly exceeds $250,000–$400,000 per turbine.
