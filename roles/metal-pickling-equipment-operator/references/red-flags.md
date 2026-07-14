# Red flags

### Post-pickling bake started later than the specified timing window for embrittlement-susceptible material
- **Usually means:** a nonconformance exists independent of whether the bake itself is later performed correctly.
- **First question:** does the material's specification set a maximum time between pickling and bake start, and was that window met?
- **Data to pull:** pickling completion timestamp, bake start timestamp, material's specified timing window.

### Pickling time extended beyond spec "to make sure" scale is fully removed
- **Usually means:** risk of overpickling — base metal attack — once scale removal is already complete.
- **First question:** has surface condition been checked against the process's actual endpoint standard, or is time simply being extended as a precaution?
- **Data to pull:** actual pickling time used, surface inspection result, process's specified time range.

### Acid bath in use for an extended period without a recent titration or concentration check
- **Usually means:** actual bath concentration may have drifted from original makeup due to iron buildup or drag-in dilution.
- **First question:** when was this bath's concentration last verified, and does current usage volume suggest it may have drifted?
- **Data to pull:** bath concentration check log, volume of material processed since last verification.

### A part released to the next process step based on visual rinse appearance alone
- **Usually means:** acid or residue carryover hasn't been directly verified and could be present without visual evidence.
- **First question:** has a pH or conductivity check been performed on this rinse, or only a visual inspection?
- **Data to pull:** rinse verification test result, visual inspection notes.

### A material grade change on the pickling line without re-verifying pickling parameters or embrittlement sensitivity
- **Usually means:** settings validated for a previous material may not be appropriate for the new one.
- **First question:** does the new material's specification match the prior material's pickling time/concentration/embrittlement classification, or does it differ?
- **Data to pull:** current and prior material specifications, current line settings.

### A part or batch showing pitting or surface roughness after pickling
- **Usually means:** overpickling — base metal attack after scale removal was already complete.
- **First question:** does actual pickling time/concentration exceed the specified range for this material?
- **Data to pull:** actual process parameters used, material specification's allowable range.

### Embrittlement-susceptible material processed without a documented baking step
- **Usually means:** the required de-embrittlement treatment may have been skipped, whether due to a process gap or a misclassification of the material's susceptibility.
- **First question:** does this material's classification require baking, and does the batch record show it was performed?
- **Data to pull:** material hardness/susceptibility classification, batch processing record for baking step.

### A shift handoff not specifying pickling completion time for a batch pending baking
- **Usually means:** the incoming shift lacks the information needed to track the critical pickling-to-bake timing window.
- **First question:** does the handoff record include pickling completion timestamp for any batch awaiting baking?
- **Data to pull:** shift handoff record, batch status for any pending baking.

### Acid handling or spent bath disposal performed outside the facility's documented procedure
- **Usually means:** a compliance requirement is being treated as flexible rather than fixed, creating regulatory and safety exposure.
- **First question:** does the actual handling/disposal method match the documented, regulatory-compliant procedure?
- **Data to pull:** the facility's documented procedure, actual method used.

### A hydrogen embrittlement failure (a fastener or part cracking) discovered after a delay following installation/service
- **Usually means:** a delayed-failure signature consistent with embrittlement — worth checking whether the part's pickling-to-bake timing was within spec.
- **First question:** does this part's processing record show pickling and baking timestamps, and were they within the required window?
- **Data to pull:** the specific part's batch/processing record, timing data if available.
