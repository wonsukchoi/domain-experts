# Playbook

Filled formulas, thresholds, and workflows a land surveyor runs against. Verify against the governing state board's current minimum standards and the client's title commitment — these are commonly applied patterns and named national standards, not a substitute for the state-specific rule in front of you.

## 1. Deed and title research workflow (run before field work)

| Step | Source | What to pull |
|---|---|---|
| 1 | Client's deed | Legal description, reference to prior plat/survey, grantor/grantee chain |
| 2 | Title commitment (if insured transaction) | Schedule A (vesting), Schedule B-II exceptions (easements, prior reservations) |
| 3 | County recorder / register of deeds | Adjoining owners' deeds for the shared line(s), any recorded boundary-line agreements |
| 4 | Prior recorded plats/surveys | Record monuments, bearings, distances, and area for this and adjoining parcels |
| 5 | County GIS parcel viewer | Sanity-check parcel shape and area against the record; flag gross mismatches before the field visit |
| 6 | BLM GLO records (PLSS land only) | Original General Land Office plat and field notes for the governing section |

**Rule:** don't schedule the field crew until steps 1–4 are reconciled — a title exception or an adjoiner's conflicting call found after monuments are set converts a research problem into a liability event.

## 2. Boundary evidence hierarchy (BLM Manual of Surveying Instructions, 2009)

1. Found, undisturbed **original** monuments (set by the surveyor who created the boundary).
2. **Obliterated** monuments — no longer found, but whose original position is provable by reliable secondary evidence (witness trees, references in adjoining surveys, testimony).
3. **Lost** corners — position not provable by any direct evidence — restored by proportionate measurement.
4. Record **courses and distances** — used to compute a position only when no monument evidence (1–3) exists.

**Rule:** a found monument consistent with its era and undisturbed condition outranks any record bearing/distance, even if the record and the monument disagree by a measurable amount — the record describes where the corner was, not where it should be.

## 3. Proportionate measurement (restoring a lost PLSS corner)

- **Single proportion**: used for a lost corner on the **outer boundary** of the township/section, using only the record distance along that one line between the two nearest found corners.
- **Double proportion**: used for a lost **interior** corner, using record distances on both the line and the intersecting line between the four nearest found corners (the "controlling corners").

*Formula (single proportion, one axis): new position = found corner A + (record distance A→lost / (record distance A→lost + record distance lost→B)) × (measured distance A→B).*

*Example: Section corner lost. Found corners 2 miles apart on the section line (record). Measured distance between found corners = 10,562.4 ft (vs. record 10,560.0 ft — a 2.4 ft excess distributed proportionally). Lost corner sits at record midpoint (5,280.0 ft from each). Proportional distance = 5,280.0/10,560.0 × 10,562.4 = 5,281.2 ft from the western found corner — not the raw record 5,280.0 ft, because the era's measurement excess is distributed across the whole line, not dumped at the restored corner.*

**Rule:** never restore a lost interior corner using single proportion (one line only) — it ignores the intersecting line's evidence and understates the actual restored position's uncertainty.

## 4. Traverse angular closure

**Allowable misclosure (commonly applied third-order field rule): C√n**, where C = instrument's angular reading capability (commonly 5"–10" for a modern robotic total station) and n = number of angles.

*Example: 5"-instrument, n = 4 angles → allowable = 10"√4 = 20" (using the commonly applied 10"×C-multiple field convention; consult the governing state standard for the exact multiplier it specifies).*

**Distribution:** if within tolerance, distribute the misclosure across angles, weighting larger corrections toward angles with the shortest sight distances or poorest geometry (they carry the most measurement uncertainty) — never distribute equally without considering geometry.

## 5. Traverse linear closure and precision ratio

**Latitude (Lat) = Distance × cos(bearing angle from north). Departure (Dep) = Distance × sin(bearing angle from north).** North and east are positive.

**Linear misclosure = √(ΣLat² + ΣDep²). Precision ratio = Perimeter / Linear misclosure, expressed as 1:N.**

| Survey classification (commonly applied pattern) | Typical minimum precision ratio |
|---|---|
| Rural/agricultural boundary retracement | 1:7,500 |
| Suburban/platted-subdivision boundary retracement | 1:10,000 |
| ALTA/NSPS commercial or high-value survey | 1:15,000 or tighter |
| Control traverse feeding an ALTA/NSPS survey | 1:20,000+ (Second Order Class II or better) |

**Rule:** verify the exact ratio against the governing state board's minimum standards for the classification in use — the table above reflects a commonly cited pattern, not a single national number.

## 6. Compass Rule (Bowditch) adjustment

**Latitude correction for a course = −(ΣLat) × (course length / perimeter). Departure correction for a course = −(ΣDep) × (course length / perimeter).**

*Example: ΣLat = −0.10 ft, ΣDep = +0.04 ft, perimeter = 999.95 ft, course AB = 300.00 ft. Lat correction to AB = +0.10 × 300.00/999.95 = +0.030 ft. Dep correction to AB = −0.04 × 300.00/999.95 = −0.012 ft. Repeat per course; corrections sum exactly to −ΣLat and −ΣDep, forcing the adjusted figure to close at (0, 0).*

**Rule:** Compass Rule assumes distance and angle measurements carry comparable proportional error — for a traverse with one clearly weaker course (short sight, obstructed line, disturbed monument), re-observe that course instead of letting the proportional adjustment mask it.

## 7. Area by coordinates (shoelace / DMD method)

**Area = |Σ(x_i × y_{i+1} − x_{i+1} × y_i)| / 2**, using adjusted (Easting, Northing) coordinates walked in order around the closed figure; divide by 43,560 for acres.

*Example: closed quadrilateral coordinates (Easting, Northing) A(0,0), B(212.11,212.15), C(353.53,70.75), D(141.44,−141.42). Shoelace sum = −119,997.7 (absolute value); Area = 59,998.8 sq ft = 1.377 ac.*

**Rule:** compare the computed closed-traverse area against the record deed's stated acreage — variance under roughly 2% is normal rounding; anything larger is a finding to investigate, not a number to quietly overwrite.

## 8. ALTA/NSPS positional uncertainty check

**Maximum allowable positional uncertainty (95% confidence) = 0.07 ft + 50 ppm × distance to the nearest related monument or corner.**

*Example: 300 ft line → 0.07 + (300 × 0.00005) = 0.07 + 0.015 = 0.085 ft allowed at that corner.*

**Rule:** this is a per-corner positional check, distinct from the traverse's overall linear precision ratio (Section 5) — a survey can pass one and fail the other; both are checked independently, and both must pass for an ALTA/NSPS certification.

## 9. ALTA/NSPS Table A items — common sourcing requirements

| Item | What it certifies | Required source |
|---|---|---|
| 1 | Monuments at all major corners | Field-set or recovered, per survey |
| 6(a)/(b) | Zoning setbacks/classification | Current municipal zoning letter or ordinance, dated |
| 7(c) | Flood zone designation | Current effective FEMA FIRM panel number and date, not a cached lookup |
| 8 | Substantial features (fences, walls) observed | Field-located, shown on the plat |
| 11 | Utility locations | Current locate ticket (e.g., 811) or as-built record, not a client sketch |
| 16 | Evidence of recent earth-moving/construction | Field observation, dated to the survey date |

**Rule:** certify only the items actually performed with a named, dated source — an unlisted or generically sourced Table A item is an unverified guess wearing a certification.
