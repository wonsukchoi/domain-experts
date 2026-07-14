# Red flags

### Rate regulation verified in only one position at room temperature
- **Usually means:** position- and temperature-dependent rate variation hasn't been checked, and the device could fail spec in orientations or conditions it will actually experience.
- **First question:** has the device been tested across all specified positions and the full temperature range, or only a single convenient bench condition?
- **Data to pull:** multi-position/temperature test data if performed, the device's specified testing positions and temperature range.

### Lubrication applied using a single generalized oil/amount across all components
- **Usually means:** component-specific lubrication requirements (type, viscosity, amount, location) may not have been followed.
- **First question:** does the lubrication applied match the specific type/amount/location called for at each individual component?
- **Data to pull:** the assembly specification's lubrication requirements per component, actual lubrication applied.

### Assembly performed outside a controlled-cleanliness environment or with visible contamination risk
- **Usually means:** dust or debris contamination could affect rate performance, treated as equivalent in seriousness to a dimensional error.
- **First question:** were the required cleanliness/environmental conditions maintained throughout assembly?
- **Data to pull:** environmental monitoring data if available, visual inspection for contamination.

### Components assembled out of the specified sequence
- **Usually means:** access needed for adjustment or testing of an earlier-installed component may now be obscured.
- **First question:** does the actual assembly order match the specified sequence, or was it altered for convenience?
- **Data to pull:** the specified assembly sequence, actual order followed.

### A rate deviation discovered only at final test, with no intermediate checkpoint verification performed
- **Usually means:** an issue that could have been caught earlier and cheaply now requires disassembly, risking new contamination or misalignment.
- **First question:** were intermediate checkpoints performed during assembly, or was verification deferred entirely to final test?
- **Data to pull:** checkpoint verification records if any exist, assembly stage at which the issue was found.

### A device passing rate spec in most tested positions but failing in one or two specific orientations
- **Usually means:** a position-dependent issue (balance/escapement sensitivity to that specific orientation) requiring further regulation, not a random or intermittent fault.
- **First question:** does the failure correlate consistently with a specific position, or does it appear randomly?
- **Data to pull:** position-by-position rate data, repeat testing in the failing position to confirm consistency.

### A device passing rate spec at room temperature but failing at a specified temperature extreme
- **Usually means:** excess temperature sensitivity, potentially from a hairspring material/attachment issue, not caught by room-temperature-only testing.
- **First question:** has the device been tested at both specified temperature extremes, not just ambient/room temperature?
- **Data to pull:** temperature-range test data, hairspring specification/material if relevant to the investigation.

### A recurring rate issue across multiple units from the same assembly batch or component lot
- **Usually means:** a systematic cause (a component lot issue, a lubrication batch problem, a training gap) rather than isolated unit-to-unit variation.
- **First question:** do multiple units share a common component lot, lubrication batch, or assembly technician/step?
- **Data to pull:** batch/lot traceability data, rate deviation pattern across affected units.

### A device disassembled to diagnose an internal issue without a plan to re-verify cleanliness and lubrication after reassembly
- **Usually means:** the disassembly/diagnosis process itself risks introducing new contamination or lubrication issues that need re-checking.
- **First question:** is there a plan to re-verify cleanliness and lubrication specifically for the areas disturbed during diagnosis?
- **Data to pull:** the diagnosis/rework plan, post-rework verification record.

### A rate specification's testing positions or temperature range not clearly documented for a specific device type
- **Usually means:** without documented required conditions, testing may default to whatever's convenient rather than what the device actually needs verified.
- **First question:** does a clear specification exist for this device's required testing positions and temperature range?
- **Data to pull:** the device's design/quality specification for rate testing requirements.
