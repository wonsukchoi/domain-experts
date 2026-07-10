# Red Flags

Smell tests for yield data, prescriptions, and equipment behavior. Format per flag: what it usually means, the first question to ask, the check to run.

## Moisture reading swings more than 2.5 percentage points intraday with no recalibration logged

- **Usually means:** the moisture sensor has drifted with ambient humidity or grain temperature and the yield map is now carrying compounding error across every point since the last calibration.
- **First question:** "When was moisture last checked against the hand-held meter today, and against what grain sample?"
- **Data to pull:** the monitor's calibration log timestamps versus the harvest log's moisture readings for the day; flag any span exceeding 2.5 points without a logged recalibration.

## Header-on yield points reading at or near zero across more than a thin headland band

- **Usually means:** header-height/status logic isn't filtering turn and deceleration segments, so headland artifacts are bleeding into the interior of the field rather than being confined to the border.
- **First question:** "Is the header status sensor triggering on actual header position, or on a timer/lever proxy?"
- **Data to pull:** raw point map colored by header status; compare the near-zero zone's footprint against the implement's known turn radius.

## RTK correction status drops to float or autonomous mid-pass

- **Usually means:** a base-station dropout, NTRIP connectivity gap, or obstruction (tree line, structure) degraded the fix from centimeter to multi-meter accuracy without any visible change on the display.
- **First question:** "What was the fix-status log during the affected pass, not just the current status?"
- **Data to pull:** correction-status log for the session; cross-reference against the rate or guidance file's timestamp range and exclude or re-flag affected segments.

## As-applied rate deviates from the prescription by more than 10% average within a zone

- **Usually means:** a controller lag on rate change, a boom/section-width mismatch, or the prescription file's zone boundaries didn't align with the controller's actual response time at operating speed.
- **First question:** "Is the deviation systematic in one direction (controller under- or over-shooting) or random (a data or GPS issue)?"
- **Data to pull:** as-applied log against the intended rate file, zone by zone, plotted against ground speed to check for a speed-dependent lag pattern.

## Prescription file fails to load or the controller reports an unsupported format

- **Usually means:** the file was exported to a newer ISO-XML version than the terminal firmware supports, or the wrong file type was exported for that brand's controller.
- **First question:** "What ISO-XML version does this terminal's firmware actually support, and does the export match it?"
- **Data to pull:** terminal firmware version and its documented supported ISO-XML/task-file version; re-export at the matching version rather than troubleshooting the terminal first.

## Management zones built from a single data layer

- **Usually means:** the zone map reflects one growing season's weather pattern (if yield-only) or one snapshot of canopy vigor (if imagery-only) rather than a persistent, multi-cause productivity difference.
- **First question:** "What years and layers actually went into this boundary — one season of yield, or yield plus ECa plus imagery agreeing?"
- **Data to pull:** the source-layer metadata for the zone file; if only one layer and one year, treat the zones as provisional and recommend a second layer before capital-intensive variable-rate decisions ride on them.

## Zone boundary runs exactly along an equipment path or field access road

- **Usually means:** the "zone" is an artifact of how the field was worked (compaction from repeated equipment travel, or a sampling path bias) rather than a real soil or productivity difference.
- **First question:** "Does this boundary correspond to a known drainage, texture, or compaction feature, or just to where equipment turns?"
- **Data to pull:** aerial imagery of historical traffic patterns overlaid on the proposed zone boundary.

## Grid or zone soil-sample coefficient of variation is high within a single supposed zone

- **Usually means:** the zone was drawn too coarse, merging areas that don't actually behave the same, or the zone-building layers disagreed and got averaged instead of resolved.
- **First question:** "Which layer disagreed inside this zone — was it flagged as unresolved during the build, or assumed uniform?"
- **Data to pull:** per-sample-point results within the zone plotted spatially; a real internal gradient (not just lab noise) means the zone needs splitting.

## Auto-steer cross-track error sustained above roughly 2.5 cm on RTK-fixed guidance

- **Usually means:** either the fix has quietly degraded (see float/autonomous flag above) or a mechanical issue (wheel slip, hydraulic valve calibration, worn steering components) is preventing the system from holding the line it's receiving.
- **First question:** "Is the correction status still showing a full RTK fix during the drift, or has it degraded?"
- **Data to pull:** correction-status log alongside the cross-track error log for the same window — separates a positioning problem from a mechanical one.

## A rate or product decision was made without a named agronomist or grower sign-off in the file notes

- **Usually means:** the technician (or the software's default) picked the rate, which moves an agronomic and liability decision onto a role that doesn't own it.
- **First question:** "Whose rate is this, and is that approval documented anywhere the file references?"
- **Data to pull:** the prescription file's metadata or accompanying memo for a named sign-off; if absent, route back before building the final file.
