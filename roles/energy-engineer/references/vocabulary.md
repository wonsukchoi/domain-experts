# Vocabulary

Terms generalists flatten together that an energy engineer keeps sharply separate — the value is in the misuse, not the definition.

## SEER vs. EER

**SEER** (Seasonal Energy Efficiency Ratio) is a part-load-weighted average across a defined set of temperature bins over a cooling season, per AHRI 210/240, and only applies to unitary equipment under 65,000 Btu/hr. **EER** is a single full-load rating at one fixed design condition (95°F outdoor / 80°F indoor), applicable to any DX cooling equipment regardless of size.

**In use:** "We can't put this 25-ton unit's IEER next to that old unit's nameplate EER and call it apples to apples without converting one side."

**Common misuse:** treating SEER and EER as interchangeable or directly comparable numbers because they're both "efficiency ratings," when they're measured under different conditions and, for larger equipment, under different standards entirely.

## IEER / IPLV

Integrated Energy Efficiency Ratio (AHRI 340/360) — a weighted average of EER measured at four load points (100/75/50/25%), replacing the older IPLV metric for commercial unitary equipment. Built specifically for equipment that spends most of its operating hours below full load.

**In use:** "The spec sheet's headline SEER-equivalent number is marketing; the AHRI-certified IEER is 12.6, and that's the number that predicts actual part-load field energy use."

**Common misuse:** accepting a vendor-quoted "SEER-equivalent" figure for large commercial equipment instead of asking for the AHRI 340/360-certified IEER, which is frequently lower than the marketing number implies.

## COP (Coefficient of Performance)

The dimensionless ratio of useful output to energy input, both expressed in matching units (typically kW/kW), used for chillers (AHRI 550/590) and heat pumps in heating mode. Convertible to EER via EER = COP x 3.412, and to kW/ton via kW/ton = 3.517 / COP.

**In use:** "The chiller's 0.62 kW/ton spec converts to a COP of 5.67 — use that to benchmark against the plant's other chillers on a common basis."

**Common misuse:** quoting COP and EER as if they're the same number without applying the 3.412 conversion factor, or comparing a chiller's COP directly against a packaged DX unit's EER without converting either.

## Degree day and balance point

A **degree day** is the integral, over a period, of the difference between a base temperature (commonly 65°F) and the average daily outdoor temperature — heating degree days (HDD) below the base, cooling degree days (CDD) above it. The **balance point** is the outdoor temperature at which a specific building's internal and solar heat gains exactly offset its heat loss, and it is not always 65°F — high-internal-load or tightly-sealed buildings have a lower true balance point.

**In use:** "This building's internal loads push the balance point down to about 58°F — recompute HDD at that base before running the envelope calc, or the heating savings estimate will run high."

**Common misuse:** using the standard 65°F base as a universal default without checking whether the specific building's balance point actually sits near it.

## ASHRAE audit Level 1 / 2 / 3

A graduated scope defined by ASHRAE's *Procedures for Commercial Building Energy Audits*: Level 1 is a walkthrough with utility-bill analysis (+/-30-50% accuracy, screening use only); Level 2 is a detailed survey with an end-use breakdown and ECM-by-ECM analysis (+/-15-25%, standard basis for a capital decision); Level 3 is investment-grade, calibrated-simulation analysis (+/-10%, required for ESPC-guaranteed contracts).

**In use:** "This is a Level 1 walkthrough — fine for deciding which of the five buildings gets a Level 2 next year, not fine for signing a capital request."

**Common misuse:** citing a Level 1 walkthrough's rough savings estimates as if they carry Level 2 or 3 accuracy when requesting capital approval.

## Simple payback vs. savings-to-investment ratio (SIR)

**Simple payback** is installed cost divided by annual savings, in years, with no discounting and no reference to the measure's actual service life. **SIR** is the present value of the measure's savings over its own useful life, at a stated discount rate, divided by installed cost — a measure with SIR below 1.0 destroys value over its life even if its simple payback looks reasonable.

**In use:** "Its payback is 16 years against a 15-year service life — check the SIR before this goes on the approved list, because that combination is a value-negative measure at any positive discount rate."

**Common misuse:** ranking a capital plan by payback alone, which ignores that different measures have very different useful lives and silently funds the ones whose payback nearly exhausts their own service life.

## IPMVP Option A / B / C / D

The Efficiency Valuation Organization's four measurement and verification approaches: **A** (retrofit isolation, key parameter measured, rest stipulated), **B** (retrofit isolation, all parameters measured), **C** (whole-facility utility-meter regression), **D** (calibrated simulation). Selected by whether the measure can be isolated with dedicated metering, not by audit-template default.

**In use:** "This RTU has a variable load profile, so we're on Option B with continuous submetering, not Option A with a stipulated runtime assumption."

**Common misuse:** defaulting to whole-facility Option C for a single, easily-isolated measure, burying a real but small signal in unrelated whole-building noise instead of isolating it directly.

## M&V baseline vs. code baseline

The **M&V baseline** is the specific building's own pre-retrofit energy performance, established from its actual utility data and used to measure real savings against itself. The **code baseline** (commonly ASHRAE 90.1 at a stated edition and climate zone) is a hypothetical minimally-compliant building used for incentive, tax-deduction (179D), or code-compliance percentage-better-than-code claims. They answer different questions and are not interchangeable.

**In use:** "The utility incentive wants percent-better-than-90.1-2019 for climate zone 3A — that's the code baseline, separate from the M&V baseline we're using to true up the ESPC guarantee."

**Common misuse:** using the M&V baseline (this building's actual historical performance) when a program specifically requires the code baseline, or vice versa, disqualifying the claim.

## AFUE

Annual Fuel Utilization Efficiency — the fraction of fuel energy input converted to delivered heat over a year for a furnace or boiler, accounting for cycling and standby losses beyond the steady-state combustion efficiency. Distinguishes the input (fuel purchased) from the output (heat actually delivered to the space).

**In use:** "The envelope calc gives us delivered heat saved in therms — divide by AFUE to get the actual gas input reduction on the meter."

**Common misuse:** treating a degree-day calculation's delivered-heat result as directly equal to the metered fuel savings, skipping the AFUE division that converts delivered heat back to fuel input.

## ESPC and guaranteed savings true-up

An **Energy Savings Performance Contract (ESPC)** ties an ESCO's compensation to a contractually guaranteed savings level, verified by an agreed M&V plan; a **true-up** is the reconciliation payment (typically ESCO to owner) when measured savings fall short of the guarantee, computed as the shortfall quantity times the applicable rate.

**In use:** "Measured savings came in 5.2% below the guarantee this year — that's a $2,472 true-up owed under the contract's annual reconciliation clause."

**Common misuse:** treating "guaranteed savings" as a marketing phrase rather than a contractual figure with a specific M&V method and true-up formula attached — without both, "guaranteed" isn't enforceable.

## Demand savings vs. energy savings

**Demand savings** (kW) is a reduction in peak instantaneous power draw, which affects demand charges on a utility bill. **Energy savings** (kWh) is a reduction in total consumption over time, which affects the volumetric energy charge. A measure can produce one without the other — a load-shifting or peak-shaving control strategy can cut demand charges with little or no change in total kWh consumed.

**In use:** "This isn't an energy-savings measure — it's shifting the chiller's run schedule to shave the peak, which hits the demand charge line, not the kWh line."

**Common misuse:** presenting a demand-only measure's dollar impact as if it came from reduced energy consumption, or sizing an M&V plan to track kWh when the actual financial benefit is on the demand-charge line.
