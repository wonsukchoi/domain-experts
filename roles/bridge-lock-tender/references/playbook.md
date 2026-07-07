# Playbook

Filled sequences a tender runs, with the numbers that make them safe rather than merely fast. Adapt the specific timings to the structure's own certified interlock timing and the lock's certified valve schedule — these are worked examples, not universal constants.

## 1. Lock-chamber lockage: fill sequence (upbound vessel, lift lock)

**Structure profile used for this example:** chamber 600 ft × 84 ft, lift 18 ft (low pool to high pool), two culvert valves per gate end, gravity-fed (no pumps).

**Sequence:**

1. **Vessel enters chamber, clears near (downstream) gates by at least the fender-line marker.** Do not close gates until the stern is confirmed past the marker — a stern still in the approach turns the next step's turbulence into a strike hazard.
2. **Close downstream miter gates.** Confirm seated (gate-seal indicator or visual check of the miter point) before touching a valve.
3. **Stage the upstream filling valves open in increments, not full-open:**

   | Stage | Valve opening | Elapsed time | Head differential remaining |
   |---|---|---|---|
   | 1 | 10% | 0:00–1:30 | 18 ft → ~16 ft |
   | 2 | 25% | 1:30–3:30 | ~16 ft → ~11 ft |
   | 3 | 50% | 3:30–6:00 | ~11 ft → ~5 ft |
   | 4 | 100% | 6:00–8:30 | ~5 ft → 0 ft (equalized) |

   Full-open at Stage 1 instead of 10% is the single most common shortcut that causes surge damage — the head differential is largest at the start, so that's exactly when the flow needs to be smallest.

4. **Watch the staff gauge boards on both chamber walls, not a timer, for the actual equalization point.** The table above is a planning estimate; a slower fill (silted culverts, colder water density effects) is normal and the gauge, not the clock, decides when Step 5 is safe.
5. **Once gauges read level (0 ft differential), open upstream gates.** Vessel proceeds. Log actual fill time against the ~8:30 estimate; a fill running more than ~50% over estimate is a maintenance flag, not just a delay to log.

**Downbound (emptying) sequence is the mirror image**, staged the same way through the downstream valves, gauges again deciding the release point — never assume emptying the same lift takes the same time as filling it; outflow geometry and any downstream vessel wake can slow it.

## 2. Bridge opening: interlock cycle timing table

| Step | Action | Typical duration | Confirmed by |
|---|---|---|---|
| 1 | Traffic gates begin lowering | 10–15 sec | Gate-down limit switch |
| 2 | Warning lights/bell cycle (gates fully down) | minimum 20 sec | Timer + gate-down switch both true |
| 3 | Interlock releases span-lift command | instant | Both switches confirmed |
| 4 | Span lift to full/logged clearance | 60–120 sec (span-size dependent) | Span-up limit switch |
| 5 | Vessel transit | (tow length ÷ speed) | VHF confirmation from vessel |
| 6 | Span lower | 60–120 sec | Span-seated limit switch |
| 7 | Traffic gates release | 10 sec | Gate-up limit switch |

**Rule that never bends:** step 3 does not fire on a visual "looks down" — only on both limit switches. If either switch fails to confirm within roughly 2× its typical duration, treat the gate as still up, re-cycle, and do not attempt a manual override without a documented maintenance bypass procedure and a second qualified person present.

## 3. Schedule-exception check (worksheet, filled example)

Run this before refusing any opening inside a posted restricted window.

```
STRUCTURE: [bridge name], governed by 33 CFR 117.[section]
POSTED RESTRICTION: No openings 1600–1800 weekdays, recreational traffic
EXCEPTION LIST (from the section text):
  [x] Vessels engaged in commerce, ≥2 hr advance notice given
  [ ] Public vessels (Coast Guard, law enforcement, fire/rescue)
  [ ] Documented emergency
REQUEST RECEIVED: 1345, tow "Ellen Marsh," requested passage 1715
NOTICE GIVEN: 3h30m (exceeds 2h minimum) → EXCEPTION MET
DECISION: Opening required at 1715 despite restricted window.
LOG REASON CODE: SCHED-EXC-COMMERCIAL-NOTICE
```

A worksheet with every box unchecked and a refusal logged anyway is the tell that the schedule was applied as absolute — pull the section text and re-check before the refusal stands.

## 4. Vessel queue consolidation (multiple requests, one span cycle)

When two or more vessels request passage within a window shorter than one full interlock cycle (roughly 5 minutes end-to-end per the table in section 2):

1. Acknowledge each request individually on VHF with an estimated single opening time.
2. Hold the span open through the full queue rather than cycling down and back up between vessels — cycling down and up again costs a full extra 10–15 sec gate-down, 20 sec warning cycle, and 10 sec gate-release for no safety benefit.
3. Confirm each vessel has cleared before starting the close sequence; the last vessel through, not the first, sets the close timing.
4. Log all vessels under the one opening event with individual clearance timestamps — a single opening serving three vessels should show as one event with three transit confirmations, not three separate logged openings.
