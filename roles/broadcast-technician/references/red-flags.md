# Red Flags

### VSWR above 1.5:1 on a transmission line that was under 1.2:1 the prior shift
- **Usually means:** Ice, water intrusion, or physical damage on the antenna/line (environmental, gradual); second most likely is a connector or component failure (step-change, not weather-correlated).
- **First question:** Did this rise gradually with a weather event, or appear as a sudden step change?
- **Data to pull:** Remote-control telemetry log for the last 6–12 hours, local weather/precipitation history, and the previous maintenance/inspection date for the affected line.

### A specific commercial spot or promo is 3+ LU louder than program average despite a compliant dialnorm tag
- **Usually means:** Ad-insertion or processing chain re-normalized the audio after the tag was written (metadata/essence mismatch); second most likely is a splice from a source encoded to a different loudness standard.
- **First question:** Does the file's embedded metadata match what a direct LKFS measurement of the delivered audio actually shows?
- **Data to pull:** The spot's traffic/ad-server ingest log, its embedded loudness metadata, and a fresh integrated-LKFS measurement of the as-aired audio.

### EAS decoder shows no heartbeat/status update for more than one polling interval
- **Usually means:** Network or serial connection to the decoder dropped (most common); second most likely is the decoder itself hung or lost power.
- **First question:** Is this decoder-specific, or are other remote-control-monitored devices on the same network path also silent?
- **Data to pull:** Remote-control system connectivity log, decoder's own internal test log (once reachable), and the timestamp of the last successfully logged RWT/RMT.

### Dead-air / silence-detect alarm fires for more than ~10 seconds during a live segment
- **Usually means:** Upstream source loss (studio audio path, satellite/network feed) rather than a local transmitter fault; second most likely is an automation-to-transmitter path failure.
- **First question:** Is the on-air monitor confirming actual silence, or is this a false trigger from the silence-detect threshold itself?
- **Data to pull:** On-air audio monitor recording, automation as-run log around the alarm timestamp, and upstream source health (satellite receiver lock status, network feed status).

### Closed captions drop out on one platform (OTA) but not another (cable/streaming), or vice versa
- **Usually means:** The dropout is downstream-specific — a distribution-side encoder or pass-through issue, not a captioning-source failure, since a source-side failure would typically affect all outputs.
- **First question:** Is the caption data present and intact at the point it leaves master control, before any distribution-specific processing?
- **Data to pull:** Caption data capture at the master-control output, and the affected distribution path's own encoder/pass-through logs.

### Generator fails to reach full transfer load within the expected time during a weekly exercise test
- **Usually means:** Fuel delivery or battery-start issue (most common in cold weather); second most likely is a transfer-switch relay fault.
- **First question:** Did the generator crank and reach idle, or fail to start at all?
- **Data to pull:** Generator run-log (start time, time-to-load, fuel level before/after), ambient temperature at test time, and last fuel/battery service date.

### Reflected power alarm clears itself without any dispatched intervention
- **Usually means:** An environmental cause (ice, condensation) that resolved on its own — not evidence the underlying line/antenna is fine going forward, since the same cause will likely recur under the same conditions.
- **First question:** What changed in the weather or ambient conditions between the alarm firing and it clearing?
- **Data to pull:** Weather history across the alarm window and the historical alarm log for the same line under similar prior conditions.

### Viewer complaints about loudness cluster around a specific time slot rather than a specific advertiser
- **Usually means:** A program-side processing or automation transition issue (e.g., a loudness-processor bypass during a specific playout chain segment) rather than an individual spot's metadata problem.
- **First question:** Does the complaint window correlate with a specific automation event (program-to-break transition, source switch) rather than a specific piece of content?
- **Data to pull:** Automation as-run log for the complaint window and an LKFS trace across the full transition, not just the flagged segment.

### Remote-control system shows all parameters "in range" but the on-air signal has a visible/audible defect
- **Usually means:** The defect is on a signal path or parameter the remote-control system doesn't sample (e.g., a downstream splice, a caption stream, or a secondary audio program) — the green board reflects only what's instrumented.
- **First question:** What, specifically, does each green indicator measure, and does the reported defect sit inside or outside that instrumented path?
- **Data to pull:** The remote-control system's monitored-point list/configuration, and a manual observation of the actual on-air output (waveform monitor, LKFS meter, caption decoder) at the point closest to what viewers receive.
