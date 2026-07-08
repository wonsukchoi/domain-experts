# Red flags

### DR angle pair disagrees by more than ~2x the instrument's stated accuracy (e.g., >10" on a 5"-reading instrument)
- **Usually means:** the backsight target was misidentified between faces, the tribrach or tripod shifted between the Direct and Reverse pointing, or the instrument needs a collimation check.
- **First question:** did the crew re-point on the exact same target both times, or was a different part of the prism/target sighted?
- **Data to pull:** the raw Direct and Reverse readings from the data collector, and the instrument's last calibration/collimation check date.

### RTK shows fixed but PDOP is above ~4 or the epoch count logged is under 5
- **Usually means:** satellite geometry is momentarily weak (partial sky obstruction, low satellite count) even though the ambiguity resolver reports fixed — the fix can be real but imprecise.
- **First question:** what does the sky view look like at this exact point, and has the PDOP been trending down or up over the last minute?
- **Data to pull:** the data collector's live PDOP/satellite-count log for the occupation, not just the final logged value.

### Float solution logged as a final control-quality point
- **Usually means:** schedule pressure or an unfamiliar receiver skipped the wait for ambiguity resolution, or the site's sky obstruction genuinely won't resolve to fixed from this location.
- **First question:** has the crew tried a different physical location, a longer occupation, or a different correction source (network vs. single base) before accepting float?
- **Data to pull:** the occupation log showing fix-type history for that point, and whether a fixed alternative point nearby exists.

### Traverse or level loop closes within tolerance but one leg's individual residual is 3x+ the others
- **Usually means:** a single blunder (wrong prism constant, misread rod, transposed digits) that happens to be offset by compensating error elsewhere in the loop.
- **First question:** which single course or setup, if re-observed, would change the closure the most?
- **Data to pull:** the per-course or per-setup residual breakdown, not just the final aggregate closure number.

### Backsight and foresight distances at one leveling setup differ by more than ~10 m
- **Usually means:** the instrument operator didn't balance the setup (common when a turning point is placed for convenience rather than geometry), letting collimation or curvature-and-refraction error leak into that shot.
- **First question:** was this setup's turning point chosen for line-of-sight balance or just for a flat, convenient spot?
- **Data to pull:** the field log's paced or measured BS/FS distances for that specific setup.

### Stakeout offset exceeds the task's tolerance but the hub was set anyway
- **Usually means:** the check was skipped or treated as advisory rather than a gate, often under time pressure near end of day.
- **First question:** was the offset actually computed and compared to a stated tolerance, or eyeballed as "close"?
- **Data to pull:** the data collector's stakeout report for that point, showing the design-vs-measured comparison at the moment the hub was set.

### Field notes missing the antenna height measurement method or the DR pair for a control point
- **Usually means:** the crew recorded a number but not how it was obtained, making the observation unverifiable later even if the number itself is correct.
- **First question:** can this specific shot be reconstructed and re-checked from the notes alone, or does it depend on someone's memory of the day?
- **Data to pull:** the field book or digital note entry for that point ID.

### Instrument or rod height not independently checked at setup
- **Usually means:** a single measured height (often eyeballed or estimated) was accepted without a second check, so any transcription or measurement error propagates through every shot from that setup.
- **First question:** was the height measured twice, and did the two measurements agree?
- **Data to pull:** the setup log's height entries and method (e.g., slant to a marked point vs. vertical to a fixed reference).

### Prism constant on the data collector doesn't match the reflector actually in use
- **Usually means:** a crew swapped reflectors (different manufacturer or type) mid-day without updating the instrument's prism-constant setting, introducing a small but systematic distance error across every subsequent shot.
- **First question:** what reflector is physically on the pole right now, and does its stamped constant match the collector's active setting?
- **Data to pull:** the reflector's manufacturer constant and the data collector's current prism-constant configuration.

### A control-feeding point has only one observation with no independent check
- **Usually means:** time pressure skipped the redundancy step for a shot the crew assumed was routine.
- **First question:** is there any second, independent observation — a repeat RTK occupation, a DR pair, a crosscheck from another control point — this value can be compared against?
- **Data to pull:** the point's observation history in the data collector; count of independent shots behind it.

### Found monument or occupation line doesn't match the expected description or position
- **Usually means:** the record is wrong, the monument was disturbed or replaced, or the crew is at the wrong point entirely.
- **First question:** does the physical evidence match the record well enough that a licensed surveyor should look at this before the crew proceeds?
- **Data to pull:** the monument's physical description, condition, and position as found, photographed, and compared to the record call — routed to the party chief, not resolved on-site.

### EDM distance on a long or precision shot has no atmospheric (ppm) correction applied
- **Usually means:** the instrument's temperature/pressure settings were left at default rather than updated for actual field conditions, introducing a small systematic distance error that grows with shot length.
- **First question:** when was the instrument's atmospheric correction last updated today, and against what temperature/pressure reading?
- **Data to pull:** the instrument's current ppm/atmospheric setting and the field-recorded temperature and pressure at the time of the shot.
