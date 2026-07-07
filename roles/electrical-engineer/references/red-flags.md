# Red flags — what a power-systems electrical engineer notices instantly

Smell tests with thresholds. Any one can be innocent; two or three together in the same study or drawing package is a pattern worth stopping the review for.

### Arc-flash study reports incident energy only at 100% bolted fault current, with no reduced-current case shown
- **Usually means:** the analyst ran the software's default single-point calculation and never checked the arcing-current range NFPA 70E requires — exactly the gap that hides a reduced-current scenario dropping below a breaker's instantaneous pickup.
- **First question:** "What's the incident energy at 85% and at the code-required lower bound, and does either exceed the 100% case?"
- **Data to pull:** the protective device's time-current curve and the incident-energy result at each required arcing-current percentage.

### Short-circuit study uses transformer nameplate %Z only, with no utility source impedance in the model
- **Usually means:** the "infinite bus" assumption was applied without checking whether it's justified — safe for breaker AIC sizing, but it can meaningfully shift the reduced-current arc-flash result if the utility feed isn't overwhelmingly strong.
- **First question:** "What's the utility's available fault current and X/R at the service point, and is it in the impedance model?"
- **Data to pull:** the utility fault-current letter or interconnection data, and the per-unit or ohmic impedance diagram showing where it enters the model.

### Breaker or fuse selected by ampacity/continuous rating with no interrupting (AIC) rating stated against the calculated fault current
- **Usually means:** the device sizing exercise stopped at "will it carry the load" and never checked "can it survive clearing the fault" — a code violation and a safety hazard if the AIC rating is below the available fault current at that location.
- **First question:** "What's the calculated available fault current at this device, and is it below the device's interrupting rating with margin?"
- **Data to pull:** the short-circuit study's bus-by-bus fault-current table and the device's nameplate AIC rating.

### Protective-device coordination checked only at each device's own rated current, not at the maximum through-fault current
- **Usually means:** the coordination plot was read at a convenient reference point rather than at the actual fault magnitude the devices will see — curves that look separated near rated current can converge or cross at real fault levels.
- **First question:** "What's the coordination margin at the maximum through-fault current at this bus, not at rated current?"
- **Data to pull:** the TCC overlay plot with the actual through-fault current marked, and the resulting time separation at that point.

### Service or feeder sized from summed nameplate connected load with no demand-factor table applied
- **Usually means:** the designer treated "add up every nameplate" as conservative, missing that the code's demand tables exist specifically because coincident load is lower — this oversizes equipment cost and lead time without a corresponding safety benefit.
- **First question:** "Which NEC 220 demand factor was applied to this load category, and what's the resulting demand VA versus the raw connected VA?"
- **Data to pull:** the load-calc worksheet showing connected VA, the applicable demand factor, and the resulting demand VA per category.

### Voltage drop calculation absent on a long feeder run (>100 ft) or a run feeding sensitive equipment (VFDs, electronics)
- **Usually means:** voltage drop was assumed acceptable without calculation because the conductor "looked adequately sized" for ampacity — ampacity and voltage-drop sizing are independent checks, and a conductor can pass one and fail the other on a long run.
- **First question:** "What's the calculated voltage drop on this run at full load, and does it clear the design target?"
- **Data to pull:** the conductor length, size, load current, and the resulting %drop calculation.

### Power-factor correction sized to "improve the meter reading" with no target PF or kVAR calculation shown
- **Usually means:** capacitors were added incrementally until the utility bill's PF penalty stopped, without a calculated target — this risks overcorrection into a leading power factor or resonance with harmonic-producing loads on the same system.
- **First question:** "What's the target PF and the kVAR calculation behind this bank size, and has harmonic content on this bus been checked?"
- **Data to pull:** the kW/PF billing data and the kVAR = kW × (tanθ1 − tanθ2) calculation used to size the bank.

### Equipment grounding conductor sized by scaling proportionally to the ungrounded conductor instead of reading the grounding table directly
- **Usually means:** the designer assumed a fixed ratio between phase conductor and ground conductor size, which holds at small sizes but diverges from the code's grounding table at larger conductor sizes.
- **First question:** "Was the grounding conductor size read directly from the table at this overcurrent device rating, or scaled from the phase conductor?"
- **Data to pull:** the overcurrent device rating and the grounding-conductor table entry at that rating.

### Arc-flash label date or system configuration doesn't match the current one-line diagram
- **Usually means:** an upstream change (transformer replacement, breaker setting change, new distributed generation) happened after the study, and the label was never revalidated — the posted PPE category may no longer reflect actual incident energy.
- **First question:** "Has anything upstream of this panel changed since the study date on the label, and has it been re-run?"
- **Data to pull:** the label's study date, the current one-line diagram, and a change log for the upstream equipment.
