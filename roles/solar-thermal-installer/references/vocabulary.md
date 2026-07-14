# Vocabulary

Terms generalists conflate that solar thermal installers keep sharply separate. Each: definition, a sentence a practitioner would actually say using it, and the common misuse.

## Stagnation temperature

The temperature a collector reaches with no fluid flow and full sun — commonly 250–400°F for flat-plate collectors, higher for evacuated-tube — the condition every closed loop in the system has to survive, not avoid.

*Practitioner usage:* "The tank being oversized doesn't mean we skip the stagnation check — it just means stagnation happens on fewer days, not zero."

*Common misuse:* treating stagnation as a rare fault condition instead of a routine one that a correctly designed system is built to survive on a normal basis.

## Solar fraction

The percentage of a household's annual water-heating energy load supplied by the solar system, with the remainder from backup (gas, electric, or heat-pump water heater). A typical residential SWH system targets 50–70% solar fraction, not 100%.

*Practitioner usage:* "We're sizing for a 60% solar fraction here — the backup heater still carries the load on cloudy stretches, this system was never meant to replace it."

*Common misuse:* selling or designing toward "100% solar hot water," which usually means an oversized, uneconomical array chasing the last, cloudiest fraction of the load.

## Drainback vs. pressurized glycol

**Drainback** systems use plain water and gravity: when the pump stops, the collector loop drains into an indoor reservoir, removing both freeze risk and glycol-degradation risk. **Pressurized glycol** systems keep a closed, pressurized loop of glycol/water mixture in the collector at all times, protected by concentration rather than by draining.

*Practitioner usage:* "This roof pitches the collector loop clean back to the mechanical room, so we went drainback — no glycol to test or replace ten years from now."

*Common misuse:* assuming any closed loop with antifreeze in it is "basically the same" as drainback, missing that drainback eliminates the freeze-margin and fluid-degradation questions entirely rather than managing them.

## Double-wall vs. single-wall heat exchanger

A **double-wall** heat exchanger has a vented or monitored air gap between the two fluid paths, so a leak in either wall is visible and can't directly mix glycol into potable water. A **single-wall** exchanger has one boundary between the two fluids — a single failure point.

*Practitioner usage:* "Code here requires double-wall for this fluid — a single-wall brazed plate doesn't clear the potable-water separation requirement without a documented variance."

*Common misuse:* assuming "food-grade" glycol automatically qualifies a single-wall exchanger under code, without checking the specific AHJ's adopted requirement.

## SRCC OG-100 vs. OG-300

**OG-100** certifies an individual collector's thermal performance (the basis for rated Btu output figures). **OG-300** certifies a whole system — collector, tank, and controls as a matched set — and is what most tax-credit and rebate programs actually require documentation against.

*Practitioner usage:* "The collector's OG-100 rated, sure, but the rebate paperwork needs the whole system's OG-300 certificate, and that means the tank and controller match the certified combination too."

*Common misuse:* citing an OG-100 collector rating as sufficient proof of incentive eligibility when the program requires an OG-300 whole-system match.

## Differential controller deadband (ON/OFF differential)

The temperature gap between the collector and tank sensors that triggers the pump ON, and the smaller gap at which it triggers OFF — set apart deliberately to prevent the pump from cycling every time cloud cover nudges the collector temperature.

*Practitioner usage:* "We've got it set at 10°F on, 4°F off — tight enough to catch real solar gain, wide enough it's not clicking on and off every time a cloud passes."

*Common misuse:* setting ON and OFF differentials close together "to capture every bit of sun," which produces rapid pump cycling instead of more delivered heat.

## Aperture area vs. gross area

**Aperture area** is the actual glazed or absorbing surface SRCC uses to rate collector output — the number that governs sizing calculations. **Gross area** is the collector's full panel footprint including frame, always larger than aperture area.

*Practitioner usage:* "Size storage off the aperture area on the OG-100 label, not the panel's overall dimensions — the frame doesn't collect anything."

*Common misuse:* using a collector's gross panel dimensions in a sizing calculation, which overstates the effective collecting area and skews storage and solar-fraction numbers.

## Freeze point vs. burst protection

**Freeze point** is the temperature at which a glycol mixture begins forming ice crystals (slush). **Burst protection** is the lower temperature at which the mixture, even partially frozen, hasn't expanded enough to rupture piping or the collector — typically well below the freeze point for a given concentration.

*Practitioner usage:* "This mix's freeze point is −28°F, and its burst protection goes lower than that — but we still design to the freeze point with margin, not to burst protection, because slush ice can still restrict flow and damage a pump."

*Common misuse:* citing a fluid's burst-protection temperature as the design freeze-protection number, which understates the temperature at which the system actually stops functioning correctly.

## Tempering valve (thermostatic mixing valve)

A valve at the storage tank's hot outlet that blends hot tank water with cold supply to deliver a fixed output temperature, regardless of how hot the tank itself runs on a given day.

*Practitioner usage:* "Tank can hit 180°F on a big solar day — the tempering valve is what keeps the fixture at 120°F regardless."

*Common misuse:* treating the tank's thermostat or high-limit setting as equivalent to a tempering valve — a solar tank's temperature swings with solar gain in a way a gas or electric water heater's setpoint doesn't.

## Steamback

The event where a stagnating closed-loop collector boils its fluid and vapor pressure pushes the remaining liquid back down into the piping and expansion tank — a normal, designed-for occurrence in a correctly sized pressurized-glycol system, a relief-valve-dumping failure in an undersized one.

*Practitioner usage:* "This system's expansion tank is sized to absorb a steamback event without lifting the relief valve — that's the whole point of the 10%-of-fluid-volume acceptance calculation."

*Common misuse:* treating any steamback event as evidence of a system fault, when a correctly sized system is designed to steamback without relieving fluid.

## Expansion tank acceptance volume vs. total volume

**Acceptance volume** is the actual usable expansion capacity a pre-charged diaphragm expansion tank delivers before the diaphragm bottoms out — commonly 40–50% of the tank's rated total volume, not the whole nameplate figure.

*Practitioner usage:* "Don't spec off the '2-gallon' label — pull the acceptance-volume spec, because that's closer to 0.9 gallons of usable expansion, not 2."

*Common misuse:* sizing an expansion tank off its total rated volume instead of its (smaller) rated acceptance volume, which under-delivers the margin the calculation assumed.

## Collector loop vs. potable loop

The **collector loop** (or primary loop) circulates the heat-transfer fluid — water or glycol — between the collector and the heat exchanger. The **potable loop** (or secondary loop) is the actual drinking-water path through the storage tank and out to fixtures. The heat exchanger is the only point where the two loops meet, and code governs how completely they're allowed to be separated there.

*Practitioner usage:* "Pressure-test the collector loop separately from the potable side before you ever fill the tank — you want to know a leak's location before the two loops are both live."

*Common misuse:* referring to "the system" as one loop when troubleshooting, obscuring which side (collector or potable) a pressure or temperature anomaly is actually on.
