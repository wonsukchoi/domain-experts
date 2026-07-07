# Playbook

Filled separation-minima references and checklists, per FAA Order JO 7110.65 unless otherwise noted. These are the numbers a controller applies directly, not descriptions of them — adapt to facility letters of agreement and local procedures, which can be more restrictive than the order's baseline.

## 1. Radar separation minima (by environment)

| Environment | Lateral minimum | Notes |
|---|---|---|
| En route (Class A/E, radar, below FL600) | 5 NM | Standard en route radar minimum; ARTCC sectors. |
| Terminal (radar, within ~40 NM of antenna) | 3 NM | Standard terminal radar minimum; TRACON/approach control. |
| Terminal, same final approach course | 2.5 NM | Only when the trailing aircraft is no heavier than the leading aircraft's wake category, both are on the same ILS/PAR course, and the position is continuously radar-identified or visually confirmed by tower — reduced minimum, not a default. |

| Vertical minimum | Applies | Notes |
|---|---|---|
| 1,000 ft | Surface up to FL290; FL290 through FL410 in domestic RVSM airspace | RVSM (effective Jan 2005) is what allows 1,000 ft above FL290 — non-RVSM-approved aircraft are excluded from that band and require 2,000 ft there instead. |
| 2,000 ft | Above FL410; anywhere non-RVSM aircraft operate above FL290 | Legacy/non-equipped-aircraft minimum. |

## 2. Non-radar (procedural) separation minima

| Type | Minimum | Notes |
|---|---|---|
| Longitudinal, time-based | 10 minutes | Baseline same-course, same-altitude procedural minimum. |
| Longitudinal, Mach Number Technique | 5 minutes | Reduced minimum for same-direction turbojets maintaining assigned Mach, once established. |
| Longitudinal, distance-based (DME/RNAV) | 20 NM | Substitutes for time separation when both aircraft can report distance from a common reference. |

Non-radar minima are larger than radar minima across the board because there's no independent scope check on either aircraft's actual position — the extra distance/time buys margin against navigation and reporting error that radar surveillance would otherwise catch directly.

## 3. Wake-turbulence separation — same runway or on approach (legacy weight categories)

Distance required between the **leading** aircraft (rows) and the **trailing** aircraft (columns), arrival stream:

| Leading \ Trailing | Heavy | Large | Small |
|---|---|---|---|
| **Super** | 6 NM | 7 NM | 8 NM |
| **Heavy** | 4 NM | 5 NM | 6 NM |
| **Large** | — (standard 3 NM applies) | — | 4 NM |
| **Small** | — (standard 3 NM applies) | — | — (standard 3 NM applies) |

Reading the table: a Small aircraft trailing a Heavy needs 6 NM — double the generic 3 NM terminal radar minimum — because wake-vortex strength scales with the *generating* (leading) aircraft's weight, not the trailing aircraft's. A Heavy trailing a Small needs only the standard 3 NM; the hazard is one-directional.

**Departure wake-turbulence separation (time-based):** 2 minutes required for a Small or Large departing behind a Heavy or Super from the same threshold, an intersecting runway, or a crossing departure path — unless the required distance-based separation (e.g., ≥6 NM airborne) is achieved by other means instead.

**RECAT note:** facilities running the RECAT wake-recategorization program replace these legacy Heavy/Large/Small distances with finer weight/wingspan-based group pairings (typically smaller distances for many pairings). Apply RECAT minima only at RECAT-equipped facilities — using RECAT numbers at a legacy-category facility understates required separation.

## 4. Read-back required-elements checklist

A controller actively parses the pilot's read-back against every element below before releasing the frequency; a partial or garbled read-back on any of these triggers an immediate re-issue and re-confirm, not a "close enough":

- [ ] Altitude assignments (climb/descend/maintain)
- [ ] Heading assignments (vectors)
- [ ] Speed assignments
- [ ] Runway assignments — takeoff, landing, and taxi clearances
- [ ] Hold-short instructions (runway or taxiway)
- [ ] Transponder code assignments
- [ ] Clearance limits and route amendments
- [ ] Frequency changes, confirmed by the next facility establishing contact

## 5. Loss-of-separation immediate-action sequence

When projected or actual separation falls below the required minimum:

1. **Issue immediate corrective instruction** (turn, climb, or descend) to re-establish the minimum first — before any notification or documentation step.
2. **Confirm re-establishment** by re-projecting the new geometry within the next scan cycle; don't assume the correction worked without checking.
3. **Notify the facility/sector supervisor immediately**, stating the two callsigns and the approximate closest distance/altitude achieved.
4. **Preserve radar data and voice tapes** for the event window — this happens before any informal discussion of what occurred.
5. **File the mandatory occurrence report** (or route through ATSAP if the event qualifies for voluntary self-disclosure); the event is subsequently categorized by severity (how much of the required minimum was lost, and how much reaction time was available) — a 4.5 NM event against a 6 NM wake minimum is treated differently from a 0.5 NM event against the same minimum, even though both are reportable losses of separation.
