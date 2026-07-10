# Precision Agriculture Playbook

Operational checklists with concrete steps and thresholds. Defaults, not laws — deviate consciously and log why.

## 1. Yield monitor calibration protocol

**Pre-calibration.** Clean and visually inspect the mass-flow sensor plate and moisture sensor cell. Check the grain cart or wagon scale is a certified weight — a calibration built against an uncertified scale bakes the scale's error into every yield map for the season. Calibrate the hand-held moisture tester against the same grain type being harvested that day.

**Mass-flow calibration — run multiple loads, not one.**
1. Harvest at least 3 separate calibration loads, each a minimum of 3,000 lb (~50+ bu corn), at different mass-flow rates — target speeds of roughly 1, 2, 3, and up to 4 mph if normal harvest speed is ~3.5 mph, so the calibration curve spans the range the combine will actually run.
2. Weigh each load on the certified scale; enter the true weight against the monitor's recorded weight for that load.
3. If the monitor's error against the certified weight exceeds 3% on any load after entering all calibration points, do not accept the calibration — check for plugged elevator, worn paddles, or a mis-seated sensor before re-running.

**Moisture calibration.**
1. Pull a grain sample per load and determine moisture with the calibrated hand-held meter.
2. Corn harvested above 20% moisture needs **recalibration every 2.5 percentage points of moisture change** to hold yield-monitor error under 5% — build this into the harvest-day schedule, not as an exception.
3. Re-verify moisture calibration at least once per day even without a 2.5-point swing; ambient humidity and grain temperature drift the sensor independent of stored grain moisture.

## 2. Soil sampling and management-zone decision

| Situation | Method | Density / cost |
|---|---|---|
| No multi-year yield history, no ECa survey available | Grid sampling | 2.5-acre grid baseline (≈$6.30/ac); 1.0-acre grid where budget allows and variability is high — best accuracy-to-cost ratio in the research record |
| ≥3 years yield-stability data + ECa or imagery available | Zone (management-zone) sampling | 2–3 composite samples per zone, zone count driven by how many distinct productivity classes the layered data actually shows (typically 3–5 for a quarter-section field) |
| Budget-constrained, flat topography, historically uniform field | Coarser grid (3-acre) or single composite | Accept the accuracy tradeoff explicitly in the file notes — do not silently downgrade a field that has shown variability before |

**Zone-building sequence:**
1. Pull 3+ years of cleaned yield data; classify into stability classes (consistently high, consistently low, variable).
2. Overlay ECa survey (or grid soil-test results if no ECa available) — texture and CEC differences that don't show up in a single yield year often explain multi-year stability patterns.
3. Overlay NDVI or multispectral imagery from at least one representative growing-season pass — canopy vigor differences confirm or contradict the yield/ECa read.
4. Where two of three layers agree on a boundary, treat it as a zone edge; where all three disagree, treat that area as unresolved and either grid-sample it directly or flag it for a walked field check before finalizing.
5. Field-truth: walk or drive the proposed boundaries against known compaction, drainage, or soil-type breaks the grower can point to. A zone boundary that runs straight through a known tile line or terrace with no agronomic reason is a data artifact, not a zone.

## 3. Prescription / rate-file build and validation checklist

1. **Confirm the agronomic rate decision is signed off** by the agronomist or grower of record before building any file — the technician builds what's approved, not a best guess.
2. **Match the file format to the controller**, not the software default: ISO-XML (ISO 11783-10) for ISOBUS-compliant terminals, proprietary shapefile/format exports for legacy or single-brand systems. Confirm the controller's supported ISO-XML version before export — a file built to a newer version than the terminal supports fails silently or displays "unsupported format" at the worst time.
3. **Set headland/boundary buffers** to match actual implement width and turn radius, not the field boundary as surveyed — a rate file with no headland buffer applies variable rate through the turn, producing the same artifacts the yield-data cleaning pass exists to remove on the way out.
4. **Test-load the file on the actual display/controller** before the field day, ideally on the same firmware version as the machine that will run it. A file that opens in desktop software but fails on the cab display is a common, entirely preventable failure.
5. **Confirm the product/rate table inside the file matches the physical product** being loaded (formulation, density, unit) — a rate file built in lb/ac loaded against a controller expecting gal/ac silently misapplies by the density conversion factor.
6. **Brief the operator** on what to expect: where rate changes occur, any zones the controller should hold minimum/maximum caps, and what an obviously-wrong on-screen rate should trigger (stop and call, not "trust the computer").

## 4. Positioning accuracy by task

| Task | Minimum accuracy tier | Why |
|---|---|---|
| Field boundary / coverage mapping, record-keeping | WAAS/SBAS, sub-meter | Sufficient for acreage and as-applied logging; RTK is overspend here |
| Auto-steer, pass-to-pass guidance | RTK, 1–2 cm pass-to-pass | ±2.5 cm cross-track accuracy is the standard auto-steer holds; WAAS-grade drift reintroduces the overlap/skip problem auto-steer exists to remove |
| Variable-rate application, planting population changes | RTK, cm-level, fixed (not float) | Rate-change resolution below the row requires a stable RTK fix; a float or autonomous solution mid-pass degrades to multi-meter accuracy invisibly on the display |
| Multi-year zone-boundary work | RTK preferred, WAAS acceptable if consistent year to year | Consistency across years matters more than absolute accuracy for stability-zone overlay work, but switching correction tiers between years introduces a false boundary shift |

## 5. Yield-map / as-applied data cleaning triage

Run in this order — most artifacts are removed by the first two passes:

1. **Header status filter.** Drop points recorded while the header is not in the working position (raised, or lowered but not engaged) — the single largest source of false zero/low-yield points, concentrated at headlands and end-of-row stops.
2. **GPS-drift duplicates.** Remove co-located points recorded during stop-and-go or slow-turn segments where the GPS reports the same position repeatedly — these inflate point density in headlands without adding real yield information.
3. **Speed-change outliers.** Flag points where the combine abruptly accelerated (falsely low yield, mass hasn't caught up to the sensor) or decelerated (falsely high yield, mass lingering past the point of actual cutting) — cross-check against the machine's speed log, not the yield value alone.
4. **Frequency-distribution outliers.** After the first three passes, run a statistical outlier check (values beyond ~3 standard deviations from the local neighborhood mean) to catch remaining sensor glitches — this pass should remove a small fraction of remaining points; if it's removing a large share, the calibration or the first three passes need review, not a more aggressive filter.
5. **Visual pass.** Look at the cleaned map before delivering it. Automated filters catch known artifact signatures; they don't catch every anomaly, and a technician who ships without looking ships whatever the algorithm missed.
