# Vocabulary

Terms generalists and new reps blur together that a practitioner keeps sharply separate.

## Net metering (NEM) vs. net billing (NEM 3.0)

**Net metering** credits exported solar at (or near) the retail rate — a kWh sent to the grid at noon offsets a kWh bought back at 7pm at the same price. **Net billing** (California's NEM 3.0 and similar successor tariffs elsewhere) credits exports at an avoided-cost rate that floats with wholesale/grid-value conditions and is typically a fraction of retail, especially in high-solar midday hours.

**In use:** "This site's still on legacy NEM 2.0, so full offset makes sense — don't apply the net-billing sizing logic here."

**Common misuse:** using "net metering" as a generic catch-all for any export compensation program, which hides the fact that the economics (and therefore the right system size) are completely different under net billing.

## Avoided Cost Calculator (ACC)

The CPUC-approved methodology (and analogous tools in other net-billing jurisdictions) that sets the dollar value of exported solar under net billing, varying by hour and month based on the grid's marginal cost/value at that time.

**In use:** "Pull the current ACC rate for this export hour before you model self-consumption value — it's not a flat number."

**Common misuse:** treating the ACC export rate as if it equals the retail rate, or as a single flat number instead of a value that moves by hour and season.

## Dealer fee

A fee, commonly 15–30% of system cost, that a solar loan or sales financing product charges the installer/dealer and that gets folded into the loan principal or interest rate rather than itemized as a line item the customer sees.

**In use:** "The 0.99% loan looks cheap, but the dealer fee on it is higher than the 5.99% option's — compare cash-price-equivalent, not APR."

**Common misuse:** assuming a lower advertised APR means a lower total cost; the dealer fee, not the rate, often drives the real cost difference between loan products.

## PPA vs. lease vs. loan

**PPA** (power purchase agreement): customer pays per kWh produced, doesn't own the system. **Lease**: customer pays a fixed (usually escalating) rent for the equipment, doesn't own it. **Loan**: customer owns the system from day one and finances the purchase. Ownership determines who keeps the tax credit and who bears production risk.

**In use:** "On a PPA, a bad shading estimate is the provider's risk, not yours — but you also never touch the tax credit."

**Common misuse:** describing lease/PPA as "basically the same as owning" — ownership status changes credit eligibility, resale handling, and escalation exposure.

## ITC vs. MACRS depreciation

**ITC** (Investment Tax Credit, IRC §48/§48E for commercial, §25D for residential) is a direct tax credit against the system's cost. **MACRS** (Modified Accelerated Cost Recovery System) is a separate commercial-only depreciation benefit that lets a business write off the system's depreciable basis over an accelerated schedule — stacking on top of, not instead of, the ITC.

**In use:** "On the commercial deal, model the ITC and the five-year MACRS schedule together — the depreciation benefit alone is often worth more than the credit for a business with tax appetite."

**Common misuse:** applying MACRS logic to a residential deal (§25D has no depreciation component) or assuming the two benefits are mutually exclusive alternatives rather than stackable.

## Interconnection / Permission to Operate (PTO)

**Interconnection** is the utility approval process (e.g., Rule 21 in California, or the applicable IREC Model Interconnection Procedures elsewhere) required before a grid-tied system can be energized. **PTO** is the utility's final authorization to turn the system on — savings don't start until PTO is issued, regardless of install completion date.

**In use:** "Installation's done, but we're still pre-PTO — don't count savings for this customer until the utility signs off."

**Common misuse:** telling a customer their savings begin at install completion instead of at PTO, which can lag installation by weeks to months depending on the utility's queue.

## Derate factor / system losses

The cumulative set of real-world efficiency losses (inverter conversion, wiring, soiling, shading, connections) subtracted from a system's theoretical nameplate output to produce a realistic production estimate — distinct from panel degradation, which is a separate year-over-year decline.

**In use:** "Nameplate is 9kW DC, but after the derate stack we're modeling 78% of that as usable AC production in year one."

**Common misuse:** quoting nameplate wattage times a flat national irradiance number as if it were the production estimate, skipping the derate stack entirely.

## Degradation rate

The annual decline in a panel's output capacity over its lifespan, industry-standard modeled at roughly 0.5%/yr (per NREL/manufacturer warranty data), compounding over a 25–30-year system life.

**In use:** "Year-25 production in this model is about 88% of year-1, using the standard 0.5%/yr degradation curve."

**Common misuse:** omitting degradation from a multi-year savings projection, which overstates cumulative lifetime savings, especially past year 15.

## Time-of-Use (TOU) rate

A utility rate structure where the price per kWh varies by the hour of day and sometimes season, with a defined peak window (commonly 4–9pm in much of the western US) priced well above off-peak hours.

**In use:** "Their peak window is 4–9pm — that's exactly when the battery should be discharging, not exporting midday solar at the off-peak export rate."

**Common misuse:** modeling savings against a single blended average rate when the customer is actually on a TOU schedule, which misses the value (or cost) concentrated in the peak window.

## Self-consumption ratio

The share of a system's total production that is used on-site in real time (directly or via battery-shifting) rather than exported to the grid — the key variable that determines real savings under a devalued export tariff.

**In use:** "Adding the battery took self-consumption from about 35% to about 90% on this deal — that's most of the payback improvement, not the panel count."

**Common misuse:** treating offset percentage (production ÷ usage, annualized) as if it were the same thing as self-consumption ratio — a system can have 127% offset and a 35% self-consumption ratio at the same time.

## True-up

Under legacy annual net-metering programs, the once-a-year reconciliation where the utility settles the customer's net kWh position (banked credits vs. draws) and bills or credits the difference — distinct from net billing's near-real-time hourly/monthly export valuation.

**In use:** "This account's still on an annual true-up cycle — don't judge the deal off a single month's bill, pull the full 12-month cycle."

**Common misuse:** applying true-up logic (annual netting at full value) to a net-billing account, where the export value is set per-interval, not netted annually at retail.
