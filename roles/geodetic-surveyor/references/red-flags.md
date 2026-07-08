# Red flags

### OPUS peak-to-peak scatter between independent sessions exceeds ~3 cm horizontal / 6 cm vertical
- **Usually means:** multipath at the site (metal roofing, chain-link fence, water nearby), or an unrecorded antenna-height/setup change between sessions.
- **First question:** did anything about the setup — tripod, antenna, height measurement point — change between the two sessions?
- **Data to pull:** the raw OPUS solution reports for both sessions side by side, plus the field log's antenna-height entries.

### A single, unrepeated static session used as final control for 2nd-order-or-better work
- **Usually means:** schedule pressure skipped the redundancy step, or the crew doesn't distinguish "long session" from "independent check."
- **First question:** is there any independent observation — a second session, a different day, a different baseline set — that this result can be checked against?
- **Data to pull:** the project's session log; count of independent sessions per station.

### Minimally-constrained adjustment residual on one baseline is 3x+ larger than the rest
- **Usually means:** a blunder — mistyped antenna height, wrong antenna reference point selected in software, or a genuinely bad control mark.
- **First question:** which single input (antenna height, control coordinate, observation) is common to just that baseline and no others?
- **Data to pull:** the minimally-constrained adjustment's residual table and the raw field log for that baseline's session.

### Control mark's NGS datasheet superseded/adjustment date predates the 2011 National Adjustment
- **Usually means:** the mark's published coordinate is on an older NAD83 realization and needs an explicit time-transformation before being combined with post-2011 marks.
- **First question:** what realization and epoch is this mark actually published in, versus what the rest of the network is using?
- **Data to pull:** the NGS datasheet's history section (PID lookup) showing prior adjustments and superseded values.

### Antenna height recorded as a rounded field estimate rather than measured to the specified reference point
- **Usually means:** the crew measured to a convenient point (base of antenna, tripod leg) instead of the antenna reference point (ARP) or slant-height point the receiver model requires.
- **First question:** which specific point on the antenna does this receiver's firmware assume the recorded height is measured to?
- **Data to pull:** the receiver manufacturer's antenna calibration sheet and the field log's height entries (method: vertical vs. slant).

### RTK-only positions submitted or referenced as project geodetic control
- **Usually means:** confusion between mapping-grade convenience (RTK, cm-level but single-base-dependent) and geodetic-grade control (static, network-adjusted, independently checked).
- **First question:** what is the RTK base tied to, and has that base's own coordinate been independently verified?
- **Data to pull:** the RTK base station's source coordinate and its provenance (published NSRS mark vs. arbitrary autonomous position).

### Ellipsoidal height reported or used with no geoid model named
- **Usually means:** the deliverable conflated GNSS height (h) with orthometric elevation (H) — a regionally-varying error that can exceed a meter.
- **First question:** was a geoid model applied at all, and if so, which one and what version?
- **Data to pull:** the processing report's height fields (h, N, H) and the geoid model name/version used.

### Baseline to nearest usable CORS or control mark exceeds ~50-75 km with no intermediate station
- **Usually means:** weak network geometry — long, sparse baselines degrade precision and remove the network's ability to cross-check itself.
- **First question:** is there a closer CORS, campaign mark, or densification point that could shorten this baseline or add a check?
- **Data to pull:** a baseline-length table for the whole network, sorted longest to shortest.

### Independent loop misclosure exceeds the allowable for the stated order/class
- **Usually means:** a blunder somewhere in the loop (bad antenna height, misidentified point, processing error), not generic "noise."
- **First question:** which single baseline in the loop, if removed, brings the misclosure back under tolerance?
- **Data to pull:** the loop-closure report and the individual baseline vectors making up that loop.

### Delivered coordinate has no stated datum, reference frame, or epoch
- **Usually means:** the deliverable was written for internal use and never adapted for the accuracy standard actually required, or the author doesn't distinguish "WGS84" (a family of realizations) from a specific epoch.
- **First question:** what document or template produced this deliverable, and does it have a frame/epoch field that was left blank?
- **Data to pull:** the project's coordinate deliverable template and the processing software's stated output frame/epoch.

### Vertical control mixes NGVD29-referenced values with NAVD88 values without conversion
- **Usually means:** older benchmark data was pulled into a new project without running it through the appropriate vertical datum conversion.
- **First question:** which specific benchmarks in this dataset predate NAVD88, and have they been converted?
- **Data to pull:** the benchmark list with original datum tags, and the conversion tool/grid used (e.g., VERTCON or the current NGS tool).

### Project spans a known active-deformation area (near a fault zone, subsidence area, or recent significant seismic event) with no epoch-motion correction
- **Usually means:** the adjustment assumed a static frame where local ground motion since the reference epoch is large enough to matter.
- **First question:** what is the known or estimated local displacement since the control's reference epoch, and does it exceed the project's accuracy tolerance?
- **Data to pull:** NGS velocity model output (e.g., HTDP) or regional deformation monitoring data for the site's coordinates.
