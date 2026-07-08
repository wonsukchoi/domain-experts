# Vocabulary

Terms generalists flatten together that a solar energy systems engineer keeps sharply separate — the value is in the misuse, not the definition.

## Voc vs. Vmp

**Voc** (open-circuit voltage) is the voltage across a module or string with no current flowing — the value that governs the NEC 690.7 cold-temperature maximum-voltage calculation. **Vmp** (voltage at maximum power) is the operating voltage under load at the module's maximum power point — the value that governs whether a string sits inside the inverter's MPPT window.

**In use:** "Size the string length off cold-temperature Voc for the code-compliance ceiling, then separately check hot-temperature Vmp against the inverter's MPPT window — they're two different checks with two different failure modes."

**Common misuse:** running only the Voc check and assuming a string that clears 690.7 automatically sits inside the inverter's MPPT operating window, or vice versa.

## Temperature coefficient

The rate a module's electrical parameter (Voc, Vmp, Isc, or Pmax) changes per degree Celsius away from the 25°C STC test condition, expressed in %/°C. Voc and Vmp coefficients are negative (voltage falls as temperature rises); Isc's coefficient is small and positive.

**In use:** "This module's Voc coefficient is -0.27%/°C — at -18°C site design low, that's 43 degrees below STC, so Voc rises about 11.6% over the nameplate 49.5 V."

**Common misuse:** applying a single "typical crystalline silicon" coefficient from memory instead of the specific certified module datasheet value, or applying the Pmax coefficient where the Voc-specific coefficient is required for a 690.7 calculation.

## DC/AC ratio (ILR, inverter load ratio)

The array's nameplate DC capacity (kWdc) divided by the inverter's AC nameplate rating (kWac). A ratio above 1.0 intentionally oversizes the DC array relative to the inverter to capture more of the inverter's operating hours at partial irradiance, at the cost of some clipped energy during peak-irradiance hours.

**In use:** "We're at a 1.25 DC/AC ratio for this fixed-tilt site — inside the normal 1.2-1.3 band, with clipping loss under 2% per the 8760 sim."

**Common misuse:** treating any ratio above 1.0 as an oversizing error rather than a deliberate, climate-dependent design choice with its own optimum.

## Clipping

Energy lost when the array's DC output at a given moment exceeds the inverter's AC power rating, so the inverter caps ("clips") its output at nameplate rather than converting the full available DC power. Concentrated in a small number of midday, high-irradiance hours, not spread evenly across the year.

**In use:** "The 1.4 ratio candidate clips almost 5% of gross DC energy in summer, versus 1.6% at 1.25 — that's the trade the DC/AC comparison table needs to show."

**Common misuse:** estimating clipping loss as a flat annual percentage instead of running an hourly simulation, which misses that clipping is a threshold effect, not a linear one.

## Performance ratio (PR)

The ratio of actual (or modeled) AC energy delivered to the theoretical energy the array's nameplate DC capacity would produce at the site's reference irradiance with zero losses. The single number that captures the full multiplicative loss stack — temperature, soiling, shading, mismatch, wiring, inverter, and availability.

**In use:** "The corrected PR comes out to 0.85 — that's the number the financing model should use, not the nameplate-times-peak-sun-hours figure."

**Common misuse:** confusing PR with capacity factor (which is normalized to the site's actual irradiance, not a full loss accounting) or skipping the PR calculation entirely and reporting the unloss-adjusted nameplate estimate.

## Capacity factor vs. performance ratio

**Capacity factor** is annual AC energy delivered divided by (AC nameplate capacity x 8,760 hours) — a measure of how much of the inverter's theoretical maximum annual output the plant actually achieves, driven mostly by the site's irradiance resource. **PR** is annual AC energy divided by the loss-free theoretical output at the *site's actual measured irradiance* — a measure of system efficiency independent of how sunny the site is.

**In use:** "Two sites can have very different capacity factors because one gets more sun, but similar performance ratios if both systems are equally well-designed."

**Common misuse:** using capacity factor to judge system design quality, when a low capacity factor may simply reflect a cloudier site rather than a worse design — PR is the design-quality metric.

## Light-induced degradation (LID) vs. warranty degradation

**LID** is a one-time power loss (commonly 1-3% for crystalline silicon, less for PERC/passivated-cell technologies) that occurs in the first weeks to months of a module's light exposure. **Warranty degradation** is the ongoing, roughly linear annual output decline (commonly ~0.4-0.5%/yr for tier-1 crystalline modules) that continues for the module's service life, per the manufacturer's power warranty schedule.

**In use:** "Apply LID once as a first-year step, then the 0.45%/yr linear degradation every year after — don't apply the linear rate to year 1 on top of LID, that double-counts."

**Common misuse:** treating LID and annual warranty degradation as the same phenomenon, or applying only one of the two to a multi-year yield model.

## P50 / P90 / P99 exceedance probability

Statistical confidence levels on a modeled annual yield: **P50** is the median-case estimate (50% chance actual output exceeds it, 50% chance it falls short); **P90** is the value actual output is expected to exceed 90% of the time (a more conservative number used for debt sizing); **P99** is used for the most conservative senior-debt coverage cases.

**In use:** "The lender's debt-sizing model wants P90, not P50 — pull that value from the same weather-year Monte Carlo run instead of quoting the median case."

**Common misuse:** presenting a single P50 number to a financing counterparty as if it were the number they should underwrite against, when debt sizing typically requires the more conservative P90 or P99 basis.

## Source circuit vs. output circuit

The **PV source circuit** carries DC current from a string (or parallel strings) of modules to a combiner or the inverter's DC input, sized per NEC 690.8 off module-level Isc. The **PV output circuit** carries DC current downstream of a combiner, sized off the combined current of all parallel source circuits feeding it — using module-level Isc for output-circuit sizing undersizes the conductor.

**In use:** "That combiner output feeds six parallel strings — size the output circuit conductor off six times per-string Isc x 1.5625, not off a single string's current."

**Common misuse:** applying source-circuit (single-string) ampacity figures to an output circuit that actually carries the combined current of multiple parallel strings.

## MPPT window

The inverter's operating voltage range within which its maximum-power-point-tracking algorithm can find and hold the array's maximum power point. A string sized correctly for the NEC 690.7 cold-temperature voltage ceiling can still fail if its hot-temperature Vmp falls below the MPPT window's minimum.

**In use:** "The cold-temp check clears the 1,000 V ceiling, but confirm the hot-temp Vmp doesn't drop below the inverter's 250 V MPPT floor on a short string in a hot climate."

**Common misuse:** running only the cold-temperature maximum-voltage check and skipping the separate hot-temperature minimum-voltage check against the MPPT window's lower bound.

## Module mismatch

Power loss from small manufacturing variances between modules connected in series or parallel — a string's current is limited by its lowest-current module, so even modules within the same power bin produce slightly less combined output than the sum of their individual rated outputs.

**In use:** "Budget 1-2% for mismatch on top of LID in the loss stack, even with modules from the same production batch and power bin."

**Common misuse:** omitting mismatch loss from the PR loss stack because all modules carry the same nameplate rating, ignoring that nameplate ratings tolerate a manufacturing bin range.
