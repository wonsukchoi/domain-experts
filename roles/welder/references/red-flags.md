# Red flags

### Actual heat input computed from as-run parameters falls outside the WPS-qualified range, even though the bead passes visual inspection
- **Usually means:** travel speed or amperage drifted from the qualified parameters during the pass.
- **First question:** what were the actual as-run amps, volts, and travel speed versus the WPS's qualified range?
- **Data to pull:** the welder's data log or traveler entry for that specific joint.

### Preheat not verified or recorded before striking an arc on a high-carbon-equivalent or thick joint
- **Usually means:** hydrogen-cracking risk is unmanaged for that joint.
- **First question:** what carbon-equivalent and thickness combination does this joint's WPS actually require preheat for?
- **Data to pull:** the material certification (for CE calculation) and the WPS preheat table.

### Same defect type recurs at the same point in every weld pass
- **Usually means:** a specific technique or parameter issue at that point — arc-strike method, travel-speed ramp-up — not random variation.
- **First question:** what's different about the technique or setup specifically at that point in each pass?
- **Data to pull:** the weld log noting defect type and location by pass number.

### Measured distortion or warp after welding exceeds the project's tolerance
- **Usually means:** the weld sequence wasn't planned for heat balance on that joint geometry.
- **First question:** what sequence — continuous or backstep/skip — was actually used?
- **Data to pull:** the planned weld sequence compared against what was actually run.

### Interpass temperature exceeds the WPS maximum on a multi-pass weld
- **Usually means:** insufficient cooling time between passes, raising the risk of grain coarsening and reduced toughness.
- **First question:** how long was the actual dwell time between passes versus what the WPS requires?
- **Data to pull:** the interpass temperature log recorded per pass.

### Filler metal lot or certification doesn't match what the WPS specifies
- **Usually means:** a substitution happened without engineering approval.
- **First question:** who approved using this filler metal lot instead of the one called out in the WPS?
- **Data to pull:** the filler metal certification paperwork compared against the WPS callout.

### NDT (radiographic or ultrasonic) rejects a weld that passed visual inspection
- **Usually means:** a subsurface defect — lack of fusion, internal porosity — invisible from the outside.
- **First question:** what specific defect type, size, and location did the NDT report identify?
- **Data to pull:** the NDT report's defect classification, size, and location detail.
