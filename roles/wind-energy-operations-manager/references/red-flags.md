# Red flags — signals a wind energy operations manager notices instantly

Smell tests with thresholds. Any one alone can have an innocent explanation; two or more together on the same turbine, quarter, or contractor is a pattern worth an immediate review.

### Time-based availability meets the contractual guarantee while energy-based production shows a double-digit percentage shortfall
- **Usually means:** curtailment or turbine underperformance is masked by an availability metric that only measures whether the turbine was mechanically ready, not whether it actually produced — the "met the guarantee" framing can hide a large unexplained gap.
- **First question:** "Decompose the shortfall — how much is curtailment by reason code, and how much is left unexplained after that?"
- **Data to pull:** time-based availability report, resource-adjusted expected production, curtailment log by reason code (see `references/playbook.md` §2).

### Curtailment events logged under a generic "other" reason code at a meaningful rate
- **Usually means:** compensable grid-operator-directed curtailment is likely being miscoded and going unclaimed under the PPA, since "other" doesn't map to any specific compensation clause.
- **First question:** "Pull the underlying grid-operator or dispatch instructions for these 'other'-coded events — do any match a compensable curtailment directive?"
- **Data to pull:** curtailment log with reason codes, grid-operator dispatch instruction records for the period, PPA curtailment-compensation clause language.

### A major component failure repaired and invoiced before the warranty/service-agreement scope was checked
- **Usually means:** the owner may have paid out-of-pocket for a failure that should have been an OEM warranty claim, or vice versa — a claim was never filed because no one checked coverage before authorizing the repair.
- **First question:** "Was the warranty triage checklist completed before this repair was authorized, and where's the coverage determination documented?"
- **Data to pull:** service agreement/warranty terms for the affected component, repair authorization date versus coverage-check documentation, SCADA/CMS evidence supporting the failure mode classification.

### CMS/SCADA trend data showing a gradual drift (rising vibration, oil particulate count) with no maintenance action taken before an unplanned trip occurred
- **Usually means:** the maintenance program is reactive rather than predictive — the data existed to catch this before it became an unplanned, more expensive event.
- **First question:** "How many weeks of trend data preceded this trip, and was there an alert threshold that should have triggered action earlier?"
- **Data to pull:** CMS historical trend data for the affected component, alert threshold configuration and history, maintenance ticket timeline versus trend-alert timeline.

### O&M spend increasing quarter over quarter while time-based availability is already above ~97%
- **Usually means:** the program may be chasing marginal availability gains past the point where the marginal O&M cost exceeds the marginal revenue those gains protect.
- **First question:** "What's the specific failure mode or component driving this spend increase, and what's its marginal cost per availability percentage point recovered?"
- **Data to pull:** O&M spend trend by category, availability trend, marginal-cost model (see `references/playbook.md` §1 framing applied to spend).

### A long-lead-time component (main bearing, gearbox, blade bearing) with zero regional or on-site spare stock
- **Usually means:** an unplanned failure on this component will incur the full 8–12 week logistics lead time as unplanned downtime, disproportionately costly if it falls during a high-wind-production season.
- **First question:** "What's this component's fleet-wide failure probability and lead time, and has it cleared the stocking decision threshold?"
- **Data to pull:** spare-parts stocking plan (see `references/playbook.md` §3), current inventory levels, historical failure rate for this component across the fleet.

### Negative electricity pricing hours with no corresponding self-directed curtailment logged
- **Usually means:** the farm may be selling into negative-price periods without an active decision to curtail, generating revenue-negative production that a properly logged economic curtailment would have avoided.
- **First question:** "For the negative-pricing hours this period, were turbines actively curtailed, or did they continue producing by default?"
- **Data to pull:** wholesale market pricing data for the period, turbine production log during negative-price hours, curtailment decision log (or its absence).

### A specific turbine or group of turbines showing a persistent power-curve shortfall (actual output below the manufacturer power curve for the observed wind speed) across multiple quarters
- **Usually means:** a physical degradation issue (blade soiling, yaw misalignment, icing not accounted for) rather than normal wind-resource variance — and it compounds each quarter left uninvestigated.
- **First question:** "Has a per-turbine SCADA-vs-power-curve comparison been run, or is the shortfall still being attributed to 'the wind year' without verification?"
- **Data to pull:** turbine-level SCADA production data, manufacturer power curve, wind speed/direction data at hub height, yaw-alignment logs.
