# Red flags

### Alloy addition calculated assuming 100% recovery rather than the furnace's established recovery rate for that element
- **Usually means:** the melt will land short of target chemistry by a predictable, calculable amount.
- **First question:** what recovery rate is actually being applied to this addition calculation, versus this furnace's documented rate for this element?
- **Data to pull:** addition calculation basis (recovery rate assumed) compared against the furnace's documented recovery rate for that element.

### Alloy addition amounts reused from a prior heat without recalculating from the current heat's actual sample assay and melt weight
- **Usually means:** off-target chemistry when charge or scrap composition differs between heats.
- **First question:** what does the current heat's actual assay and weight show versus what was charged?
- **Data to pull:** current heat's actual assay/weight compared against the addition amounts actually charged.

### Slag basicity/practice not adjusted for the specific refining reaction required for this heat's chemistry targets
- **Usually means:** the target impurity won't actually be removed regardless of time or temperature, since slag chemistry — not just its presence — governs the reaction.
- **First question:** does the measured slag basicity actually meet the requirement for the specific refining reaction targeted?
- **Data to pull:** slag basicity measurement compared against the requirement for the specific refining reaction targeted.

### Tap proceeds based on time-in-furnace or visual judgment rather than a verified actual melt temperature
- **Usually means:** risk of premature solidification during transfer or pouring (too cold), or excess refractory wear and gas pickup (too hot).
- **First question:** what does the actual measured tap temperature show versus the target for this specific alloy and process?
- **Data to pull:** measured tap temperature compared against the target temperature for this specific alloy and downstream process.

### A chemistry-adjustment decision is made from a sample assay without accounting for elapsed time or further melting since that sample was pulled
- **Usually means:** the addition is calculated against a chemistry that may no longer represent the melt's actual current state.
- **First question:** how much time elapsed between the sample and the addition, and did further charge melting occur in between?
- **Data to pull:** sample timestamp compared against time of addition, and whether further charge melting occurred in between.

### Final chemistry consistently lands off-target in the same direction for a specific element across multiple heats
- **Usually means:** the assumed recovery rate itself is miscalibrated for current furnace practice, not random heat-to-heat variation.
- **First question:** does the deviation trend correlate with the recovery rate currently assumed in addition calculations?
- **Data to pull:** final chemistry deviation trend for that element compared against the recovery rate currently assumed.

### A heat record doesn't document the actual recovery rate/addition calculation basis used, only the final addition amount
- **Usually means:** a later investigation into a chemistry miss can't determine whether the calculation itself or an execution error was the cause.
- **First question:** does the heat record capture the required fields — initial assay, target, recovery rate assumed, addition calculated, final assay?
- **Data to pull:** heat record documentation completeness compared against the standard required fields.
