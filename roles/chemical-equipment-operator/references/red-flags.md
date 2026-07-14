# Red flags

### Reactor temperature rising faster than expected during a reagent addition, after previously tracking normally
- **Usually means:** heat generation beginning to outpace cooling capacity — an early signature of thermal runaway risk, not a value to push through.
- **First question:** is this a stable elevated reading, or an actively rising excursion?
- **Data to pull:** temperature trend over the addition period (not just the current point value), addition rate log, cooling system status.

### A reagent addition continued per a fixed schedule despite an out-of-spec temperature reading
- **Usually means:** the addition rate control is being driven by elapsed time/volume rather than by actual reactor response.
- **First question:** is addition rate currently being adjusted based on real-time temperature, or following the original fixed schedule regardless?
- **Data to pull:** addition rate log against temperature trend, batch record's specified control method.

### A batch record showing a step performed out of its specified sequence
- **Usually means:** a procedural error or a deliberate reordering assumed to be equivalent — the actual chemical consequence needs verification either way.
- **First question:** has this specific reordering been chemically evaluated, or assumed to be fine because the final mixture "looks the same"?
- **Data to pull:** the batch record's specified sequence, process chemistry guidance on this reaction's sequence sensitivity.

### A batch passing visual/physical inspection despite a documented process deviation
- **Usually means:** an appearance-based check that doesn't verify the specific chemical consequence (impurity profile, yield, purity) a deviation could cause.
- **First question:** has an analytical test appropriate to this specific deviation type been run, or only a visual/physical check?
- **Data to pull:** the deviation type and its known/possible chemical consequences, analytical test results if performed.

### Equipment being opened or serviced without a completed lockout/tagout, because it "looks empty"
- **Usually means:** residual hazard (vapor space, unpurged line segment, stored pressure) hasn't been ruled out, only assumed absent based on appearance.
- **First question:** has this equipment been formally purged/verified per LOTO procedure, or just visually assessed?
- **Data to pull:** LOTO checklist status for this equipment, purge/verification record.

### Secondary containment or spill response equipment not verified on its scheduled interval
- **Usually means:** a readiness gap exists that won't be discovered until an actual release, when it's too late to address.
- **First question:** when was this containment system or spill kit last verified, and is it within its required check interval?
- **Data to pull:** containment/spill kit inspection log, required verification interval.

### A cooling system alarm or capacity limit approached during a reaction that historically ran with comfortable margin
- **Usually means:** either a change in reaction conditions (concentration, ambient temperature, feedstock purity) or a degrading cooling system component.
- **First question:** has anything about this batch's conditions changed from the historical baseline, or has cooling system performance itself degraded?
- **Data to pull:** batch conditions vs. historical baseline, cooling system maintenance/performance log.

### A reagent substitution or supplier change with no re-verification of addition rate/temperature behavior
- **Usually means:** the new reagent's reaction kinetics may differ from the characterized original, invalidating the existing addition-rate schedule's safety margin.
- **First question:** has this specific substitution been evaluated for its exotherm/reaction-rate behavior, or assumed equivalent to the original reagent?
- **Data to pull:** the substitution's technical data sheet, any qualification testing performed for this change.

### A near-miss (a close-call temperature excursion, a stopped addition) not documented in the batch record
- **Usually means:** the event was resolved operationally but the record doesn't reflect what actually happened, losing the learning opportunity and the traceability.
- **First question:** does the batch record capture the excursion, the action taken, and the resolution, or just the final "batch complete" status?
- **Data to pull:** the batch record's deviation section, shift log notes for the relevant period.

### A standard operating procedure followed without recent verification that reagent purity/concentration still matches its original characterization
- **Usually means:** feedstock or reagent quality drift could change reaction behavior even when the procedure itself hasn't changed.
- **First question:** does current reagent lot data match the specification the procedure was originally validated against?
- **Data to pull:** current reagent lot certificate of analysis, the procedure's original validation basis.
