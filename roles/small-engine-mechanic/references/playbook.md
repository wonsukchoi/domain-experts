# Playbook

Filled reference material: oil-mix ratio and consequence tables, the float-vs-diaphragm carburetor spec comparison, spark plug gap reference, the ethanol-degradation timeline, and the seasonal staffing/stocking worksheet.

## 1. Two-stroke oil-mix ratio reference and consequence table

| Category | Typical spec ratio | Oil per 1 US gal (128 oz) | If mixed richer than spec (excess oil) | If mixed leaner than spec (deficient oil) |
|---|---|---|---|---|
| Modern handheld, synthetic-oil-rated (current Stihl, Husqvarna, Echo lines) | 50:1 | 2.6 oz | Smoke, spark plug and combustion-chamber carbon fouling, spark arrestor screen loading — recoverable with cleaning | Inadequate lubrication — piston/cylinder scoring, possible seizure within one tank; often requires a rebuild |
| Older/mid-era handheld (many 1990s–2000s units, some Poulan/Craftsman) | 40:1 | 3.2 oz | Same as above | Same as above |
| Vintage two-stroke (pre-1990s, some Homelite and early chainsaw lines) | 32:1, some as rich as 16:1–25:1 on very old designs | 4–8 oz | Same as above | Same as above |

**Consequence asymmetry, always stated to the customer this way:** running rich is a cleanup job; running lean is a rebuild-or-replace conversation. When in doubt about a customer's mix history, treat the possibility of a lean mix as the more urgent thing to rule out first, before quoting anything for a "just smokes" complaint.

**Mix-math check, worked in oz (the arithmetic to actually do at intake):** oil bottle rated oz ÷ actual fuel oz mixed = actual ratio. Example: a 3.2 oz bottle (rated for 1 gal at 40:1) used with 64 oz (0.5 gal) of gas gives 64 / 3.2 = 20:1 — half the spec'd dilution, i.e., double the oil concentration.

## 2. Float-type vs. diaphragm-type carburetor comparison

| Type | Common application | Level/height mechanism | Typical spec | Primary failure mode |
|---|---|---|---|---|
| Float-type (Briggs & Stratton Flo-Jet, Tecumseh) | 4-stroke walk-behind mowers, tillers | Float level measured with a gauge tool, carb body inverted | Commonly in the 11/64–13/64 in range depending on platform — confirm against the specific service manual before adjusting | Float level set high, or a worn/leaking needle and seat, floods the bowl and causes fuel weeping or a rich idle independent of jet size |
| Diaphragm-type (Walbro, Zama) | 2-stroke handhelds (trimmers, blowers, chainsaws) | Metering lever height measured against the carb body's gasket surface, no float or bowl present | Commonly flush to roughly 0.010 in of the gasket surface — confirm the exact figure per model, some Walbro specs call for slightly below flush | Lever height out of spec floods or leans the metering circuit; separately, the fuel-pump and metering diaphragms harden or tear from ethanol exposure over roughly 1–2 seasons even when the lever height is correct |

**Always confirm architecture before opening a carb** — a float-level gauge produces no meaningful reading on a diaphragm carb, and a metering-lever check has nothing to measure on a float carb; applying the wrong spec wastes the diagnostic step.

## 3. Spark plug gap reference

| Common small-engine plug | Typical gap spec |
|---|---|
| Champion RCJ6Y / RCJ7Y (common 2-stroke handheld fitment) | 0.025 in (0.635 mm) |
| Briggs & Stratton 4-stroke (common walk-behind mower platforms) | 0.030 in (0.75 mm) |
| NGK small-engine equivalents | 0.020–0.030 in, model-dependent — confirm per engine before gapping |

A plug gapped tighter than spec with oily, wet fouling is a symptom of a rich mix ratio or excess oil, not a defective plug — replacing the plug alone without correcting the mix produces the same fouling again within one tank.

## 4. Ethanol-blend fuel degradation timeline (no stabilizer added)

| Storage duration | Expected condition |
|---|---|
| Under 30 days | Minimal degradation; low risk per OPEI storage guidance |
| 30–90 days | Early varnish formation begins in the smallest fixed passages (idle/fixed jet); fuel may still look and smell normal |
| 3–6 months (typical single off-season layup) | Varnish commonly clogs the idle circuit; phase-separation risk rises with any moisture exposure in the tank |
| 6+ months | High likelihood of gum/varnish requiring carb disassembly to clear; rubber fuel lines and diaphragms may show swelling or hardening on top of the varnish issue |

**"The fuel looks fine" is not a data point that rules out varnish** — deposits form in the idle jet well before the bulk fuel in the tank shows visible discoloration or a separated layer.

## 5. Seasonal staffing and parts-stocking worksheet

Reconciling example comparing two seasonal-only hires against one cross-trained year-round tech, both models covering the spring mower rush (March–June) and the fall/winter snowblower rush (October–January), each roughly 173 paid hours/month:

| | Two seasonal-only hires | One cross-trained year-round tech |
|---|---|---|
| Spring mower coverage | 4 mo × 173 hr × $22/hr = $15,224 | included below |
| Fall/winter snowblower coverage | 4 mo × 173 hr × $22/hr = $15,224 | included below |
| Year-round coverage | 12 mo × 173 hr × $24/hr = $49,824 | |
| **Total labor cost** | **$30,448** | **$49,824** |
| Coverage of the ~5 off-peak months (Feb, Jul–Sep) | None — no dedicated tech scheduled | Covered — bench shifts to handheld 2-stroke repairs, sharpening, and off-season tune-ups |

**Reconciling arithmetic:** $49,824 − $30,448 = **$19,376 more per year** for the cross-trained model. That premium is worth paying only if the shop's own off-peak ticket volume (the ~5 months with no dedicated seasonal tech under the two-hire model) generates more than $19,376 in gross margin annually — a number to check against the shop's own point-of-sale history before committing to either staffing model, not a rule to apply blind.

**Parts-ordering lead time, same logic applied to inventory:** place mower carb kit and belt orders by early January for the March rush; place shear pin and scraper bar orders by early July for the October rush. Ordering against the current bench's slow-season volume instead of the coming season's forecast is the most common stocking mistake — by the time the season's volume shows up on the bench, the distributor is back-ordered on the same parts every other shop just reordered.
