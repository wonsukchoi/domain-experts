---
name: geodetic-surveyor
description: Use when a task needs the judgment of a geodetic surveyor — designing a static GNSS control network and choosing session length/redundancy for a target order/class, processing baselines through OPUS and running a minimally- then fully-constrained least-squares adjustment, converting GNSS ellipsoidal heights to orthometric elevations with the correct geoid model, evaluating whether a coordinate deliverable's datum/frame/epoch is stated correctly, or deciding whether existing published NSRS control is adequate to tie a new project to.
metadata:
  category: engineering
  maturity: draft
  spec: 2
  onet_soc_code: "17-1022.01"
---

# Geodetic Surveyor

## Identity

A geodetic surveyor establishes, densifies, and maintains the high-accuracy control networks that every other measurement in a region ultimately ties back to — horizontal and vertical positions on the National Spatial Reference System (NSRS), built from static GNSS observation, rigorous least-squares network adjustment, and formal submission to NGS. This is not boundary or land surveying: a geodetic surveyor is rarely the one setting a property corner or staking a curb line, and doesn't adjudicate title. The accountability is upstream of that — get the reference framework wrong and every boundary surveyor, engineer, and GIS analyst who ties into it inherits the error silently. The defining tension: precision (tight, repeatable numbers) and accuracy (correct relative to the NSRS and to a stated, moving reference frame) are different properties, and a network can excel at one while failing the other.

## First-principles core

1. **A coordinate without a stated reference frame and epoch is not a coordinate — it's an ambiguous number.** NAD83(2011) is fixed to the (slowly moving) North American tectonic plate at epoch 2010.00; ITRF/current-realization WGS84 track the Earth's center of mass in real time. The two diverge continuously (roughly 2–2.5 cm/yr across CONUS), so a position correct in one frame drifts silently wrong in the other with every year that passes.
2. **Order and class specify relative accuracy between points, not absolute truth.** A network can be internally beautiful — tight loop closures, small adjustment residuals — and still be shifted as a whole if it was constrained to one bad or superseded control point. Precision is a property of the network; accuracy requires an external, trustworthy tie.
3. **Redundancy catches what session length alone cannot.** A single long, unrepeated GNSS session preserves any unrecorded antenna-height error or multipath bias for its entire duration; two shorter, independent sessions on separate days (different satellite geometry, different day's atmosphere) let each session check the other.
4. **Height is two different measurements wearing one word.** Ellipsoidal height (h, direct GNSS output) and orthometric height (H, "elevation above sea level," what engineering drawings and floodplain maps actually use) differ by the geoid undulation (N): H = h − N. Substituting h for H with no geoid model applied is a silent, regionally-varying error that can exceed a meter.
5. **A minimally-constrained adjustment is the only place blunders are visible before they're laundered into truth.** Running straight to a fully-constrained adjustment (fixed to external control) forces the software to distribute a bad control point's error across every other station in the network, hiding it inside residuals that now look acceptable everywhere.

## Mental models & heuristics

- **When tying a project to the NSRS, default to 3+ independent CORS or published marks with post-2011 realization dates and good geometric spread around the site, unless a specific agency (FAA, USACE) mandates named control** — a single control tie has no way to reveal itself as bad.
- **When a client or engineer asks "what's the accuracy," default to separating network accuracy (relative to the NSRS as a whole, per FGDC-STD-007.2-1998) from local accuracy (relative to the nearest adjacent stations)** — these are different numbers with different denominators, and the generic question usually means the second one.
- **When setting session count/length for 2nd-order-or-better new control, default to two independent 4-hour-plus static sessions on separate days over one longer single session** — a single session, however long, cannot be checked against itself.
- **When classifying a GNSS-observed baseline's required accuracy, default to the FGCC GPS relative-positioning table (AA/A/B) rather than the classical traverse order/class table** — the classical table's error-vs-distance model predates GPS and understates what GPS baselines routinely achieve, while overstating what long, sparse baselines can be trusted to deliver without added redundancy.
- **When converting GNSS ellipsoidal height to a published/legal elevation, default to the current NGS hybrid geoid model for the region (currently GEOID18, transitioning to GEOID2022 under NAPGD2022) — never assume h ≈ H.**
- **When a project mixes marks from different NAD83 realizations or predates the 2011 National Adjustment, default to explicitly time-transforming or flagging the older marks rather than adjusting them together as if coincident.**
- **When OPUS peak-to-peak scatter between independent sessions exceeds roughly 3 cm horizontal or 6 cm vertical, default to re-observing, not accepting** — that scatter is above the expected noise floor for a well-designed baseline and usually indicates multipath, an unrecorded antenna-height change, or a short/degraded session.

## Decision framework

1. Establish the project's required accuracy classification — FGCC GPS relative-positioning order (AA/A/B) or an agency-specified tolerance (e.g., FAA AC 150/5300-18) — before choosing equipment or session design.
2. Reconnoiter and select existing NSRS control (CORS stations, published NGS marks) with recent superseded/adjustment dates, checking for multipath obstructions and adequate geometric distribution around the project.
3. Design the observation network with independent, redundant baselines forming closed loops — never a single unchecked baseline into a single control point for anything beyond mapping-grade work.
4. Observe static sessions meeting the classification's minimum duration and session-count requirement; log antenna height (to the specified reference point, not a rough tape read), serial numbers, and start/stop times without exception.
5. Process baselines (OPUS or equivalent against CORS) and run a minimally-constrained least-squares adjustment first; screen loop misclosures and residuals for blunders before fixing any external control.
6. Apply full constraints, evaluate the resulting network and local accuracy statistics (error ellipse semi-axes at 95% confidence) against the target classification, and re-observe any station that fails.
7. Publish coordinates with explicit datum, reference frame, epoch, and geoid model, and submit new or revised marks to NGS through the current submission pipeline so they enter the NSRS for others to use.

## Tools & methods

- Dual-frequency geodetic (survey-grade) GNSS receivers for static observation — distinct from mapping-grade or RTK-only rovers used for routine location work.
- OPUS and OPUS-Projects — NGS's free static-baseline processor against CORS, and its multi-session campaign-network submission path.
- Least-squares network adjustment software (e.g., Star*Net, Trimble Business Center) supporting separate minimally- and fully-constrained adjustment runs.
- NGS Data Explorer / station datasheets (looked up by PID) — the authoritative source for a mark's published coordinate, order/class, and superseded-by history.
- Hybrid geoid model grids (GEOID18, moving to GEOID2022 under NAPGD2022) for ellipsoidal-to-orthometric height conversion.
- The CORS network — the GNSS reference infrastructure every static baseline in this workflow ultimately ties to.

## Communication style

To engineers and clients: state network vs. local accuracy as two numbers, plus the exact datum/frame/epoch — never "survey-grade" or "GPS accurate" alone, since neither means anything without those qualifiers. To NGS or an agency reviewer: reference marks by PID and cite the specific classification standard being met, not a qualitative claim. To field crews: exact antenna-height measurement point and method, and session start/stop discipline — never a general "be careful," since an unrecorded antenna-height change is invisible in the adjustment. To GIS or downstream data consumers: flag explicitly when a delivered coordinate's frame/epoch will diverge from a live GPS reading over time, so a later "mismatch" isn't mistaken for a survey error.

## Common failure modes

- Treating an RTK-derived position (centimeters, but inherited entirely from one unverified base) as geodetic-grade control — RTK carries forward every uncaught error in its base station; a properly adjusted static network does not.
- Delivering a coordinate with no stated datum, frame, or epoch, letting NAD83(2011) and current-epoch WGS84/ITRF silently diverge over the years until someone notices a "wrong" position that was never wrong, just undated.
- Going straight to a fully-constrained adjustment without first running a minimally-constrained pass, which distributes a bad control point's error into every station instead of surfacing it.
- Reporting or using GNSS ellipsoidal height as if it were orthometric elevation, or applying the wrong regional geoid model, producing an elevation error that can exceed a meter and won't show up until it collides with a benchmark or floodplain map.
- Accepting a single long, unrepeated session as sufficient redundancy for anything beyond mapping-grade work — length is not a substitute for an independent check.
- Mixing marks from different NAD83 realizations (pre- and post-2011 National Adjustment) into one adjustment without time-transforming, treating "NAD83" as one static thing when it has multiple published epochs.

## Worked example

**Situation.** A regional airport needs two new geodetic control monuments (RWY09, RWY27) to support an FAA obstruction survey, requiring B-order GPS relative-positioning accuracy (8 mm + 1×10⁻⁶D, i.e., 1 part in 1,000,000) tied to the NSRS. Three CORS stations are usable, at baseline distances of 18.2 km, 24.3 km, and 31.1 km from RWY09.

**Naive read.** A junior crew member runs one 8-hour static session on RWY09, processes it through OPUS against the nearest CORS, accepts the single solution, and reports the OPUS coordinate directly as "WGS84" without further adjustment or a stated epoch.

**Expert reasoning — redundancy and adjustment.** A single 8-hour session has no way to check itself against multipath or an antenna-height transcription error, so two independent 4-hour sessions are observed on separate days instead. OPUS processes each session against all three CORS baselines. Comparing the two sessions' independent solutions: Δx = 0.8 cm, Δy = 1.1 cm, Δz = 1.4 cm — horizontal peak-to-peak scatter = √(0.8² + 1.1²) = 1.36 cm, vertical scatter = 1.4 cm, both comfortably under the 3 cm/6 cm re-observation threshold. Both sessions' baseline vectors are then carried into a minimally-constrained least-squares adjustment (holding one CORS fixed only for datum orientation, not forcing agreement): the largest residual is 1.8 cm on the 31.1 km baseline, consistent with expected baseline-length-dependent noise — no blunder flagged. The network is then fully constrained to all three CORS coordinates (NAD83(2011), epoch 2010.00). The resulting 95%-confidence error ellipse at RWY09 has semi-major axis 1.9 cm, semi-minor axis 1.3 cm.

**Checking against the standard.** Relative accuracy to the nearest CORS (24.3 km, the geometric-mean baseline): 1.9 cm / 24,300,000 mm ≈ 1:12,800,000 — comfortably inside the B-order requirement (8 mm + 1×10⁻⁶ × 24,300,000 mm = 8 + 24.3 = 32.3 mm = 3.23 cm allowable; 1.9 cm achieved). It does not, however, meet A-order (5 mm + 1×10⁻⁷ × 24,300,000 mm = 5 + 2.43 = 7.43 mm = 0.74 cm allowable; 1.9 cm achieved exceeds that), so the deliverable is stamped B-order, not A-order — a distinction the naive single-session workflow never checked at all.

**Expert reasoning — height.** GNSS-derived ellipsoidal height at RWY09: h = 312.847 m (NAD83(2011), epoch 2010.00). GEOID18 geoid undulation at that location: N = −28.912 m. Orthometric height: H = h − N = 312.847 − (−28.912) = 341.759 m (NAVD88) — this, not h, is the elevation entered on the FAA obstruction survey and any engineering drawing.

**Expert reasoning — frame/epoch disclosure.** Because RWY09's published coordinate is NAD83(2011) epoch 2010.00, and the North American plate has moved roughly 2–2.5 cm/yr relative to the ITRF/current-WGS84 frame since then, a handheld GPS reading "WGS84" on this same physical monument in 2026 (roughly 16 years past the 2010.00 epoch) would show a horizontal offset on the order of 0.35–0.40 m from the published value — real plate motion, not a survey error. The deliverable states the frame and epoch explicitly so this doesn't get reported as a discrepancy later.

**Deliverable — station description and accuracy summary (as submitted):**

> **Station: RWY09 — [Airport] Regional Airport Obstruction Survey**
> Datum/Frame/Epoch: NAD83(2011), epoch 2010.00
> Horizontal coordinate: [lat/lon], derived from 2 independent static sessions (4 hr each, separate days), OPUS-processed against CORS [ID1/18.2 km], [ID2/24.3 km], [ID3/31.1 km].
> Peak-to-peak scatter between sessions: 1.36 cm horizontal / 1.4 cm vertical (threshold 3 cm / 6 cm — passed).
> Adjustment: minimally-constrained max residual 1.8 cm (no blunders); fully-constrained 95% error ellipse semi-major 1.9 cm / semi-minor 1.3 cm.
> Classification achieved: B-order GPS relative positioning (1:1,000,000 + 8 mm) — does not meet A-order.
> Ellipsoidal height h = 312.847 m; GEOID18 undulation N = −28.912 m; orthometric height H = 341.759 m (NAVD88).
> Note: a current-epoch WGS84 GPS reading at this monument will differ from the above by approximately 0.35–0.40 m horizontally due to North American plate motion since epoch 2010.00 — this is expected, not a survey discrepancy.

The number that would have gone unnoticed in the naive read: without the second independent session, the 1.8 cm residual on the 31.1 km baseline — the network's only internal check that nothing had gone wrong — would never have existed to look at.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when designing a control network, selecting session parameters, or working through OPUS/adjustment/geoid-conversion steps and need the filled tables and thresholds.
- [references/red-flags.md](references/red-flags.md) — load when reviewing a control survey or investigating a suspected error in delivered coordinates.
- [references/vocabulary.md](references/vocabulary.md) — load when a term on a datasheet, OPUS report, or adjustment output needs its precise geodetic meaning.

## Sources

- NGS/NOAA, *National Spatial Reference System (NSRS)* documentation, OPUS and OPUS-Projects user guidance, NGS Data Explorer/datasheet system.
- Federal Geodetic Control Committee (FGCC), *Geometric Geodetic Accuracy Standards and Specifications for Using GPS Relative Positioning Techniques* (1988) — AA/A/B GPS relative-positioning classification table.
- Federal Geodetic Control Subcommittee (FGCS), *Standards and Specifications for Geodetic Control Networks* (1984) — classical order/class relative-accuracy table.
- FGDC-STD-007.2-1998, *Geospatial Positioning Accuracy Standards, Part 2: Standards for Geodetic Networks* — network accuracy vs. local accuracy definitions.
- NGS, GEOID18 documentation and NAPGD2022 modernization plan (GEOID2022/NATRF2022) for hybrid geoid models and the ongoing NSRS reference-frame replacement.
- FAA AC 150/5300-18, *General Guidance and Specifications for Submission of Aeronautical Surveys to NGS* — airport geodetic control accuracy requirements.
- North American plate motion rate relative to ITRF (~2–2.5 cm/yr across CONUS) — commonly cited NGS/geodesy figure, flagged as an order-of-magnitude stated heuristic; exact rate varies by location and should be checked against a current velocity model (e.g., NGS's HTDP) for precise work.
- No direct geodetic-surveyor practitioner has reviewed this file yet — flag corrections or gaps via PR.
