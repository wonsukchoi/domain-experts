# Wind farm operations working vocabulary

Terms a wind energy operations manager uses precisely and a generalist blurs together. Format: definition → how a practitioner says it → common misuse.

**Time-based availability vs. energy-based (production) availability** — Time-based availability is the percentage of time a turbine is mechanically ready to operate, the metric most O&M contracts guarantee. Energy-based availability compares actual production to wind-resource-adjusted expected production, capturing curtailment and underperformance that time-based availability doesn't measure.
In use: "The contractor's 97.8% time-based number meets the guarantee, but that tells us nothing about the 14.8% energy-based shortfall — those are two different questions."
Misuse: treating a met time-based availability guarantee as proof there's no production problem, when curtailment and turbine underperformance are invisible to that specific metric.

**Curtailment (and reason codes)** — A deliberate reduction in a turbine's output below what wind conditions would otherwise allow, for reasons including grid-operator directive, noise ordinance, negative electricity pricing, or wildlife protection windows — each with different PPA compensation implications.
In use: "Log the reason code at the time of the event — 'other' isn't a reason code, it's a compensation claim we can't file later."
Misuse: logging curtailment events without a specific reason code, which makes it impossible to later determine which events were compensable under the PPA.

**Power purchase agreement (PPA) curtailment compensation clause** — Contract language specifying whether and how much the offtaker compensates the generator for output lost to grid-operator-directed curtailment, distinct from curtailment the generator chooses for its own reasons (economic or regulatory).
In use: "The 210 turbine-hours of grid-directed curtailment qualify under our PPA's compensation clause at $45/MWh — that's a claim to file, not a loss to write off."
Misuse: assuming all curtailment is uncompensated by default, without checking whether the specific reason code matches a clause the PPA actually compensates.

**Full-service vs. unbundled O&M/warranty agreement** — A full-service agreement has the OEM assume major-component failure risk (at a premium price) for the contract term. An unbundled agreement covers routine maintenance only, leaving the owner exposed to the full cost of a major component failure.
In use: "We're on an unbundled agreement past year 5 — that gearbox failure is coming out of our budget, not the OEM's, unless the manufacturing-defect exclusion applies."
Misuse: assuming warranty coverage continues at the same scope throughout a turbine's operating life without checking the specific agreement's term and component list, which often narrows or expires well before the turbine's full service life.

**Condition monitoring system (CMS)** — Sensors and analytics (vibration, oil particulate analysis, temperature trending) that track a component's degradation over time, distinct from SCADA, which primarily reports operational status and production data in real time.
In use: "CMS flagged rising particulate count on that gearbox three weeks before the trip — we had the lead time to schedule a swap instead of an emergency mobilization."
Misuse: treating CMS data as informational only, reviewed after a failure rather than acted on as a leading indicator before the failure occurs.

**Predictive vs. reactive maintenance** — Predictive maintenance acts on CMS/SCADA trend data to schedule a repair before failure; reactive maintenance responds only after an unplanned trip or failure has already occurred, which typically costs more in crane mobilization and lost production.
In use: "This gearbox swap was predictive — scheduled around a low-wind week. The one last quarter was reactive, an emergency crane mobilization during peak production season."
Misuse: measuring maintenance program success by total maintenance spend alone, without distinguishing the (cheaper) predictive share from the (expensive) reactive share.

**Logistics lead time (major components)** — The time between ordering a replacement major component (main bearing, gearbox, blade bearing) and its arrival on-site, commonly 6–12 weeks for these parts, which drives the case for pre-stocking versus order-on-failure.
In use: "A gearbox failure with no regional stock means 8-10 weeks of downtime just waiting on the part — that's the number that justifies pre-stocking one regionally."
Misuse: applying a single stocking policy to every component regardless of its individual lead time and failure probability, rather than evaluating each component against the stocking-decision threshold.

**Power curve (turbine performance)** — The manufacturer-specified relationship between wind speed and expected power output for a given turbine model, used as the baseline to detect underperformance independent of whether the wind resource itself was as forecast.
In use: "Comparing SCADA output against the power curve for the actual observed wind speed — not the forecast — tells us if this is a turbine problem or a wind problem."
Misuse: comparing actual production only against a pre-season resource forecast, which conflates "the wind was different than predicted" with "the turbine underperformed for the wind it actually got" — two different problems requiring different fixes.

**Wake effect / soiling / yaw misalignment (underperformance causes)** — Wake effect is production loss from turbines shadowing each other's wind resource; soiling is reduced aerodynamic efficiency from blade surface buildup (dirt, insects, ice); yaw misalignment is the turbine's rotor not tracking directly into the wind, both cutting energy capture below the power curve's prediction.
In use: "The power-curve gap is consistent across the whole west row — check for wake effect first before assuming individual turbine soiling."
Misuse: attributing any power-curve shortfall to "the wind year" without checking these specific, fixable mechanical/aerodynamic causes first.

**Liquidated damages (O&M contract)** — A pre-agreed financial penalty an O&M contractor owes the owner when time-based availability falls below the contractual guarantee, calculated per the contract's specified formula rather than actual damages proven case by case.
In use: "Availability came in at 95.2% against a 97% guarantee — liquidated damages apply per the contract formula, no need to prove actual lost revenue separately."
Misuse: assuming liquidated damages apply automatically to any production shortfall, when the clause is specifically tied to the time-based availability metric, not energy-based production.
