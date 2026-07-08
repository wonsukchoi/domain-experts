# Red flags

Smell tests an energy engineer catches on a first pass over an audit report, an ECM savings proposal, or an M&V plan.

### Savings quoted as a percentage of the whole utility bill, not the isolated end use the measure actually touches

- **Usually means:** the efficiency-rating jump was applied to the wrong denominator, typically inflating claimed savings by counting lighting, plug load, or fan energy the measure never affects.
- **First question:** what fraction of the baseline bill is this specific end use, and does the audit have a submetered or DOE-2/eQuest breakdown to support that fraction?
- **Data to pull:** end-use breakdown from the audit report, any submetering data for the affected system.

### SEER quoted for equipment rated at or above 65,000 Btu/hr (about 5.5 tons)

- **Usually means:** a metric mismatch — AHRI 210/240's SEER test scope doesn't cover equipment this size; the vendor is quoting a headline number that doesn't apply to the unit being sold.
- **First question:** what's the AHRI 340/360 IEER rating on the certified performance data sheet?
- **Data to pull:** AHRI-certified directory listing or manufacturer submittal for the specific model.

### Degree-days used at the default 65°F base with no balance-point check on a high-internal-load or tightly-sealed building

- **Usually means:** the calculated heating and cooling split doesn't match the building's actual thermal behavior, typically overstating heating savings and understating cooling savings.
- **First question:** what is the building's measured or estimated balance-point temperature, and how far does it sit from 65°F?
- **Data to pull:** hourly interval billing data or BAS trend data to back out the balance point empirically.

### Audit report shows no baseline regression statistic (R², or an equivalent goodness-of-fit) against a driving variable

- **Usually means:** the savings claim isn't weather- or production-normalized, so a post-installation comparison against raw bills will confound the measure's effect with normal year-to-year variance.
- **First question:** what is the R² of the baseline model, and what independent variable (degree-days, production units) was it regressed against?
- **Data to pull:** 12-24 months of monthly or interval billing data, the regression model and its fit statistics.

### ECMs of very different measure life ranked and funded by simple payback alone

- **Usually means:** capital is being allocated toward short-payback measures that may still destroy value on a discounted basis, while longer-payback measures with much longer service life are passed over.
- **First question:** what is each measure's SIR at the organization's discount rate, computed over its own useful life, not a common horizon?
- **Data to pull:** DOE/ASHRAE measure-life tables, the capital plan's stated discount rate, per-measure cash flow.

### M&V plan is written or finalized after construction is already complete

- **Usually means:** no comparable pre-retrofit baseline data exists at the metering granularity the M&V plan now needs, undermining any post-installation savings claim.
- **First question:** is there at least 12 months of pre-retrofit interval or billing data at the same granularity the M&V metering will use?
- **Data to pull:** pre-installation interval/AMI data or monthly billing history, dated before the retrofit's construction start.

### Nameplate efficiency used as the baseline for equipment more than 5-7 years old with no field verification

- **Usually means:** compressor, coil, or combustion efficiency degradation isn't reflected in the baseline, which can push the calculated savings in either direction depending on whether the baseline or the retrofit case used the stale number.
- **First question:** has a field efficiency test (portable power meter, psychrometric measurement, combustion analyzer) been run on the existing equipment recently?
- **Data to pull:** field test readout and date, equipment run-hours or cycle count since last major service.

### Multiple ECMs in the same space or zone analyzed with independently-summed savings

- **Usually means:** interactive effects (a lighting retrofit's reduced internal heat gain lowering the cooling load) weren't sequenced into the HVAC savings calculation, double-counting the shared portion.
- **First question:** was the HVAC savings recalculated using the post-lighting-retrofit internal gain, or run against the original baseline internal gain?
- **Data to pull:** the model run order and internal-gain assumptions for each ECM in the bundle.

### 179D tax deduction or utility incentive claimed against a baseline model that doesn't match the program's required ASHRAE 90.1 edition or climate zone

- **Usually means:** the modeled savings percentage isn't calculated against the reference the program actually requires, risking disqualification or a clawback.
- **First question:** which 90.1 edition and climate zone does the specific incentive program's implementation manual specify?
- **Data to pull:** the program's implementation manual, the baseline model's input file and stated code edition.

### ESPC guaranteed savings level set equal to, not below, the engineering-predicted savings

- **Usually means:** no margin exists for normal weather or occupancy variance, making a contractual shortfall and true-up payment likely in a below-average year even with a correctly performing retrofit.
- **First question:** what stipulated adjustment mechanism exists in the M&V plan for weather or occupancy deviation from the baseline model's assumptions?
- **Data to pull:** the guarantee schedule, the M&V plan's stipulated-vs-measured parameter list.

### Cooling or heating savings calculated with standard degree-days on a building with unoccupied setback hours not reflected in the calculation

- **Usually means:** the degree-day method assumes continuous conditioning to the design setpoint, overstating savings on a building that sets back significantly during unoccupied hours.
- **First question:** does the model separately account for setback-period run-hours, or apply the full 24 hr/day degree-day assumption regardless of schedule?
- **Data to pull:** BAS schedule export or thermostat setpoint log covering occupied and unoccupied periods.

### IPMVP option selected doesn't match the ECM's isolatability (e.g., whole-facility Option C used for a single lighting retrofit in a building with many other coincident changes)

- **Usually means:** the M&V signal for the specific measure will be swamped by unrelated whole-facility noise, producing an inconclusive or misleading result.
- **First question:** can the ECM's key parameter be isolated with dedicated metering (Option A or B) instead of relying on the whole-facility meter?
- **Data to pull:** a submetering feasibility assessment for the specific measure's circuit or system.
