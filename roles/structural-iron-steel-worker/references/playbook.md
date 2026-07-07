# Playbook

Filled thresholds and sequences a structural ironworker actually runs against. Verify against the site-specific erection plan and the connection drawing in front of you — these are the regulatory/standard floors, not a substitute for the project's engineered detail.

## 1. Fall-protection height bands (29 CFR 1926.760)

| Elevation above lower level | General worker | Connector |
|---|---|---|
| ≤ 15 ft | No Subpart R fall-protection trigger (site policy may still require it) | Same |
| > 15 ft up to 30 ft (or two stories, whichever is less) | Guardrail, safety net, PFAS, positioning device, or fall restraint required | May work without tie-off **only if** fall-protection equipment is provided and the site-specific erection plan addresses connector procedures |
| > 30 ft (or two stories, whichever is less) | Full conventional fall protection required | Full conventional fall protection required — connector exemption ends here regardless of role |

**Rule:** the exemption band is conditional (equipment provided, plan in place), not a blanket pass — and it has a hard ceiling at 30 ft/two stories that applies no matter who's on the beam.

**Anchorage for PFAS/positioning devices:** independent anchorage rated to support at least 5,000 lb per attached employee, or engineered and maintained under a qualified person's supervision with a safety factor of at least 2 (1926.502(d)(15)). Never anchor to a member that hasn't been confirmed to meet one of those two standards.

## 2. Minimum bolts before hoist-line release (1926.754(c)(1))

- **Baseline:** at least 2 bolts per connection, same size and strength as shown in the erection drawings, drawn up wrench-tight (or the equivalent), before the load is released from the hoisting line.
- **Cantilevered or eccentric connections:** a competent person determines whether more than 2 bolts are required for stability before release — if so, that number governs, not the 2-bolt baseline.
- **Wrench-tight / snug-tight, defined:** the tightness attained by the full effort of an ironworker using an ordinary spud wrench, or the equivalent effort from a few impacts of an impact wrench, bringing the connected plies into firm contact. This is a distinct, earlier state than final pretension — see §3.

## 3. Bolt pretensioning methods and acceptance criteria (RCSC Specification)

| Method | How it works | Acceptance criterion |
|---|---|---|
| **Turn-of-nut** | Snug-tight, match-mark nut-to-bolt-and-ply, rotate a specified additional amount | Rotation per Table 8.1 by bolt length/diameter ratio (below); tolerance +30° for rotations ≤1/2 turn, +45° for rotations >1/2 turn up to 3/4 turn |
| **Calibrated wrench** | Torque wrench set to produce the required tension, verified daily | Wrench calibrated on a tension-measuring device (e.g. Skidmore-Wilhelm) for the actual bolt/washer/nut lot in use, minimum 3 bolts of each diameter and grade tested before use each shift |
| **Direct-tension-indicator (DTI) washer** | Washer with domed protrusions compresses as tension is applied | 0.005 in feeler gauge refused entry (i.e., gap ≤ 0.005 in) at not fewer than 5 of 8 protrusions on a standard DTI washer |
| **Twist-off (TC) bolt** | Splined tip shears off at a factory-set tension when torqued | Spline shear-off confirms tension — visually verify splined end has sheared on every bolt |

**Turn-of-nut rotation table (RCSC Table 8.1), by bolt length relative to diameter (d):**

| Bolt length | Required rotation past snug-tight |
|---|---|
| ≤ 4d | 1/3 turn (120°) |
| > 4d and ≤ 8d | 1/2 turn (180°) |
| > 8d and ≤ 12d | 2/3 turn (240°) |

*Example: 7/8 in bolt, 3 in length. 4d = 4 × 0.875 = 3.5 in. 3 in ≤ 3.5 in → 1/3 turn (120°) required, accept up to 150° (120° + 30° tolerance).*

**Rule:** the method used has to match what the connection drawing specifies (bearing-type snug-tight only, or pretensioned via one of the four methods above) — running extra impact-wrench hits past snug is not a substitute for any of these and doesn't create a verifiable record.

## 4. Slip-critical vs. bearing-type joints

- **Bearing-type (snug-tight only):** most common on beam/column shear connections not subject to load reversal or vibration; snug-tight per §2 is the finished state, no further pretensioning method required unless the drawing says otherwise.
- **Slip-critical (fully pretensioned, faying surface treatment specified):** required where the connection can't be allowed to slip under service load — moment connections, connections subject to fatigue or load reversal, connections in the seismic or wind lateral system. Requires one of the four pretensioning methods in §3 plus the specified faying-surface class (e.g., Class A, unpainted clean mill scale, or Class B, blast-cleaned).
- **Rule:** check the connection drawing's designation before defaulting to either state — over-pretensioning a bearing-type joint wastes crew time, under-pretensioning a slip-critical joint leaves a connection that can slip under its actual service load.

## 5. Column anchorage (1926.755)

- Minimum **4 anchor rods** per column.
- Column anchor-rod assembly (rods, base-plate weld, and column foundation) must be designed to resist a minimum eccentric gravity load of **300 lb located 18 in from the extreme outer face of the column**, in each direction, at the top of the column shaft — this is the load a connector standing and working on top of an unbraced column imposes.
- Rods that have been field-burned or enlarged to force a fit are a fabrication nonconformance, not a field fix — flag, don't grind.

## 6. Temporary bracing / guy-wire status tracking

Track per bay, not per building:

1. **Erected, snug/pinned only** — bare steel up, minimum-bolt release satisfied, no pretensioning done yet. Temporary guys/bracing are load-bearing for this bay.
2. **Bolted up, pretensioned** — all specified connections in the bay brought to final method and verified per §3.
3. **Permanent lateral system complete** — diaphragm (deck welds, e.g. puddle welds) and/or permanent bracing for that portion installed and verified per the erection plan.

**Rule:** temporary guys/bracing for a bay are struck only once state 3 is confirmed for that bay — not when the bay visually resembles a finished one. A deck that's 60% welded (e.g. 18 of 30 required puddle welds) is not carrying diaphragm load; treat it as state 2 until the erection plan's completion criterion for that bay is met.

## 7. Controlled decking zone (CDZ) limits (1926.760(c))

- Maximum size: **90 ft wide by 90 ft deep from the leading edge**, in any direction.
- Maximum unsecured decking within the zone: **3,000 sq ft**.
- Control line placed **not less than 6 ft nor more than 90 ft** from the leading edge, clearly marked.
- Only workers performing leading-edge decking or connecting work, who have completed CDZ-specific training, may work inside the zone without individual fall arrest.
- **Rule:** these are ceilings, not targets — a CDZ sized to the full floor plate, or unsecured decking past 3,000 sq ft, is an unprotected exposure with no regulatory limit anymore, not an efficiency gain.

## 8. Double connections (1926.757)

Where two members frame into opposite sides of the same column web or bracket at the same elevation, standard bolt patterns can leave no wrench clearance for the second connection. Resolve per the connection drawing's specified method — typically:

- A seat or clip angle that lets the second member land and be bolted without reaching behind the first.
- A blind-bolting fastener or erection aid specified for that exact clearance conflict.

**Rule:** never force bolts in blind from below with no specified clearance solution — if the drawing doesn't show one and the field can't make the standard pattern work, that's an RFI, not an improvisation.
