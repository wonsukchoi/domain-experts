# Vocabulary

Terms generalists flatten together that a petroleum engineer keeps sharply separate — the value is in the misuse, not the definition.

## Nominal decline rate vs. effective (secant) decline rate

**Nominal** decline rate (Di) is the continuous, instantaneous exponential rate used inside the Arps equations. **Effective (secant)** decline rate is the actual observed percentage drop in rate over a full year, always numerically smaller than the nominal rate at the same underlying decline.

**In use:** "Nominal Di is 65%/yr in the model, but the effective annual decline you'd actually observe is closer to 48% — don't quote the nominal number as if it's the year-over-year drop."

**Common misuse:** reporting the nominal decline rate as if it were the directly observable year-over-year percentage decline, overstating how fast the well appears to be falling.

## EUR vs. reserves vs. resources

**EUR** (estimated ultimate recovery) is a well's total lifetime recoverable volume (already produced plus remaining), with no price or category qualifier. **Reserves** are the economically recoverable, price- and technology-qualified portion of EUR, categorized 1P/2P/3P under SPE-PRMS. **Resources** is the broader term including contingent and prospective volumes not yet meeting the reserves threshold.

**In use:** "EUR on this well is 1.8 MMbbl — the 1P reserves booked against it are lower, because only the direct-offset-supported portion clears the reasonable-certainty bar."

**Common misuse:** calling a raw decline-curve EUR figure "proved reserves" without running it through the category and price-deck tests reserves actually require.

## OOIP/OGIP vs. recoverable reserves

**OOIP/OGIP** (original oil/gas in place) is the total volumetric hydrocarbon volume in the reservoir, before any recovery mechanism is applied. **Recoverable reserves** = OOIP/OGIP x recovery factor, where the recovery factor depends on drive mechanism and development plan.

**In use:** "OOIP is 42 MMbbl, but at a 22% primary recovery factor for this solution-gas-drive reservoir, recoverable is only about 9.2 MMbbl."

**Common misuse:** quoting an in-place volume as if it were the recoverable number, skipping the recovery-factor step entirely.

## Skin factor

A dimensionless term added to the radial-flow pressure equation representing near-wellbore flow restriction (positive skin, e.g., formation damage) or enhancement (negative skin, e.g., a successful fracture stimulation), separate from the reservoir's bulk permeability.

**In use:** "Buildup test shows skin of +8 — the low rate isn't a permeability problem, it's near-wellbore damage that an acid job could remove."

**Common misuse:** assuming a well producing below its expected rate must sit in a lower-permeability part of the reservoir, without running a pressure transient test to isolate skin from permeability.

## Bubble point pressure

The pressure at which the first bubble of gas comes out of solution from an undersaturated oil as pressure declines; below this pressure, flow in the reservoir is two-phase (oil and free gas).

**In use:** "Reservoir pressure is still above bubble point at this stage, so we're on the straight-line PI, not Vogel's curve, for the IPR."

**Common misuse:** applying Vogel's IPR equation (derived for two-phase, below-bubble-point flow) to a well still producing single-phase above bubble point, where a straight-line productivity index is the correct model.

## Productivity index (PI) vs. inflow performance relationship (IPR)

**PI** is a single ratio, J = q/(Pr-Pwf), valid for single-phase flow above bubble point where the relationship between rate and drawdown is linear. **IPR** is the full, generally nonlinear curve (e.g., Vogel's equation below bubble point) that PI reduces to as a special case.

**In use:** "PI held constant only works above bubble point — once we're below it, the IPR curve flattens at high drawdown and a constant-PI extrapolation overstates rate."

**Common misuse:** extrapolating a constant PI to high-drawdown, below-bubble-point conditions where the true IPR curve is nonlinear.

## Voidage replacement ratio (VRR)

The ratio of reservoir-barrel fluid injected to reservoir-barrel fluid produced (oil+water+gas, all at reservoir conditions) over the same period in a waterflood or pressure-maintenance project.

**In use:** "VRR has been running 0.91 for three months straight — injection isn't keeping pace with voidage, and we should expect a pressure decline unless injectivity improves."

**Common misuse:** comparing surface injection and production volumes directly (stock-tank barrels) instead of converting each to reservoir barrels via formation volume factor before computing the ratio.

## Design factor vs. rated (catalog) pressure

The **rated (catalog) burst/collapse pressure** is the API/ISO nameplate value for new pipe at zero axial load. The **design factor** is a safety multiplier (commonly 1.10-1.125 for burst, similar range for collapse) applied on top of that rating to set the actual maximum working pressure used in design.

**In use:** "Catalog burst is 7,738 psi; at a 1.10 design factor the working limit we design to is 7,035 psi, not the nameplate number."

**Common misuse:** treating the API catalog rating itself as the safe maximum working pressure, skipping the design factor.

## Triaxial (von Mises) stress vs. uniaxial burst/collapse rating

The **uniaxial rating** (API burst or collapse pressure) assumes zero axial load. **Triaxial (von Mises) stress** combines the actual axial (tension/compression), radial, and tangential (hoop) stress components at the pipe wall into a single equivalent stress compared against yield — the governing check for a landed string that is never actually at zero axial load.

**In use:** "Burst and collapse individually check out, but the triaxial check at this string's actual axial tension shows a design factor below minimum — that's the real governing case."

**Common misuse:** checking burst and collapse independently against the catalog rating and treating a pass on both as sufficient, ignoring how axial load reduces the effective rating in combined loading.

## Working interest (WI) vs. net revenue interest (NRI)

**WI** is a party's share of a well's costs and gross production before royalty is deducted. **NRI** is that same party's share of production after royalty and other burdens are deducted — NRI = WI x (1 - total royalty/burden fraction).

**In use:** "WI is 75%, but with a 20% royalty burden the NRI is 60% — revenue runs off NRI, costs run off WI."

**Common misuse:** applying the working interest percentage directly to a revenue calculation instead of converting to net revenue interest first.

## Type curve vs. decline curve

A **type curve** is a normalized or dimensionless curve family (often built from analytical or numerical models, or a basin-wide statistical fit) used to forecast a well before it has enough of its own production history. A **decline curve** is the well-specific Arps fit to that well's own actual production data.

**In use:** "We're using the basin type curve for the first six months since this well doesn't have stabilized data yet — once it does, we switch to a well-specific decline fit."

**Common misuse:** continuing to rely on a basin type curve's EUR for a specific well's booked reserves well after enough well-specific data exists to fit and use its own decline curve.

## Rate transient analysis (RTA) vs. decline curve analysis (DCA)

**DCA** is a purely empirical fit of rate vs. time (Arps and its variants), with no direct link to reservoir or fluid properties. **RTA** incorporates flowing pressure data along with reservoir and fluid properties to estimate permeability and drainage area, giving the decline a physical basis.

**In use:** "DCA gives us a b of 1.3, but RTA on the same well backs out a permeability and drainage area consistent with that behavior being transient, not boundary-dominated yet."

**Common misuse:** treating a DCA-fitted b-exponent as a physically meaningful, fixed reservoir property rather than a curve-fit result that RTA can confirm or contradict.

## Terminal (minimum) decline rate, Dmin

The floor exponential decline rate applied once a hyperbolic decline's instantaneous secant decline falls to it; the forecast switches from hyperbolic to exponential decline at that point to keep EUR finite.

**In use:** "Once secant decline hits our 8%/yr Dmin, we switch this well's forecast to exponential — that's what keeps the tail from running to an unphysical well life."

**Common misuse:** omitting a terminal decline rate entirely and extrapolating a hyperbolic (especially b>=1) fit all the way to the economic limit, producing an unbounded or unrealistically large EUR.
