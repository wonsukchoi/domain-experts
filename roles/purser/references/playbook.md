# Playbook

Filled worksheets and step sequences a purser runs before and during a trip. Numbers are worked examples — recompute against the actual manifest each time.

## 1. Crew-complement worksheet (14 CFR 121.391)

Formula by passenger seating capacity:

| Seating capacity | Required flight attendants |
|---|---|
| 10–19 passengers (payload >7,500 lb) or 20–50 (payload ≤7,500 lb) | 1 |
| 51–100 | 2 |
| 101+ | 2 + 1 per unit (or part of a unit) of 50 seats above 100 |

Worked rows:

| Aircraft config | Seats | Calculation | Required FAs |
|---|---|---|---|
| Regional jet | 76 | Flat tier | 2 |
| Narrowbody, standard | 128 | 2 + ⌈28/50⌉ = 2+1 | 3 |
| Narrowbody, high-density | 189 | 2 + ⌈89/50⌉ = 2+2 | 4 |
| Widebody | 293 | 2 + ⌈193/50⌉ = 2+4 | 6 |

**Trigger to rerun this worksheet:** any equipment/gauge swap on a flight number, any last-minute seat-block change (e.g., a cabin reconfigured for a charter), or a crew sheet inherited from a prior day's assignment for the "same" flight number.

## 2. Duty/rest legality check (14 CFR 121.467)

Step sequence for each crew member joining the trip, especially reserves and reassignments:

1. Pull the crew member's actual duty log — not a verbal confirmation — for the timestamp their most recent duty period ended.
2. Determine the length of that prior duty period: ≤14 hours requires ≥10 consecutive hours rest; >14–20 hours requires ≥12 consecutive hours rest.
3. Compute elapsed rest as of this trip's report time: report time − prior duty end time.
4. Compare elapsed rest to the required floor. Margin under ~30 minutes: treat as a scheduling problem, not a rounding error — flag to crew scheduling before boarding close.
5. If short of the floor: request either (a) a report-time push sufficient to clear the floor, or (b) a substitute crew member whose rest already clears it. Prefer (b) when it avoids a schedule delay and a legal substitute is available.

Worked table:

| Crew member | Prior duty ended | Duty length | Required rest | Report time | Elapsed rest | Legal? |
|---|---|---|---|---|---|---|
| FA S (reserve) | 06:00 | 8 hrs | 10:00 | 15:30 | 9.5 hrs | No — 0.5 hr short |
| FA T (reserve) | 20:00 (prior day) | 9 hrs | 10:00 | 15:30 | 19.5 hrs | Yes |

## 3. Pre-flight briefing agenda (filled example, 189-seat aircraft, 4-person crew)

1. **Crew introductions and door/position assignments** — confirm who's on which door, who's aisle-chair trained if needed today.
2. **Today's manifest specifics**: 1 lap infant (seat 14C), 1 wheelchair passenger requiring an aisle-chair transfer at 22A, no unaccompanied minors, no known security flags from the gate.
3. **Weather/turbulence expectation**: moderate chop forecast climbing through FL180–FL240; seatbelt sign policy for that segment.
4. **Safety equipment check**: confirm each door team has verified slide/raft armed status, oxygen bottle pressure, and defibrillator/first-aid kit seal intact.
5. **New-to-type or first-trip-together flags**: FA T is current on this aircraft type but flying her first trip with this specific crew — pair her door assignment with an experienced crew member on the adjacent exit.
6. **Sterile cockpit reminder**: no non-essential cabin calls below 10,000 feet or during the forecast turbulence segment; urgent-contact protocol is three chimes.
7. **Questions/safety review**: each crew member states their exit's evacuation command and equipment location aloud.

## 4. ASAP/irregularity report (filled example)

> **Report type:** ASAP — non-punitive
> **Flight:** 482, [date]
> **Reporter:** Purser
> **What happened:** During boarding, door 2L was armed before the cross-check call was completed with door 2R; caught and corrected before push-back by the purser's walk-through, no injury or incident.
> **Conditions:** Short 35-minute turn time before this leg; door team included one crew member on her first trip with this aircraft type.
> **Contributing factors noted:** Cross-check call sequence not verbally confirmed between doors before the arming step; time pressure from the short turn.
> **Immediate action taken:** Door team briefed on cross-check sequence before next leg; no discipline action.
> **Recommendation:** Flag short-turn pairings with a first-trip crew member for an extra cross-check verification step in the pre-departure flow.

## 5. Sterile-cockpit contact protocol (below 10,000 ft / critical phases)

| Situation | Contact allowed? | Method |
|---|---|---|
| Routine cabin service question | No | Hold until above 10,000 ft |
| Passenger requesting a seatbelt-sign exception | No | Hold |
| Medical emergency in progress | Yes | Designated urgent-contact chime pattern, then verbal report |
| Security concern (suspicious behavior, threat indication) | Yes | Designated urgent-contact chime pattern, then verbal report |
| Smoke/fire indication in the cabin | Yes | Designated urgent-contact chime pattern, immediate verbal report |
| Fuel/mechanical concern visible from cabin (unrelated to the above) | Yes, if immediate safety relevance | Designated urgent-contact chime pattern |
