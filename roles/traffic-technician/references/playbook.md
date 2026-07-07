# Playbook

Filled worksheets a traffic technician actually runs, not descriptions of them — swap in the geometry, speed, and count data for the intersection in front of you.

## 1. Yellow change interval worksheet (ITE/Kell formula)

Y = t + v / (2a + 64.4G), where t = perception-reaction time (1.0 s, ITE-recommended constant), a = deceleration rate (10 ft/s², ITE-recommended comfortable stop), v = 85th-percentile approach speed in ft/s (mph × 1.467), G = grade as a decimal (+ uphill, − downhill).

Example — level approach, 45 mph: v = 45 × 1.467 = 66.0 ft/s.
Y = 1.0 + 66.0/(2×10 + 64.4×0) = 1.0 + 66.0/20 = 1.0 + 3.30 = 4.30 → round up to 4.3 s.

Example — same approach speed, 3% downgrade (G = −0.03): Y = 1.0 + 66.0/(20 + 64.4×(−0.03)) = 1.0 + 66.0/(20 − 1.932) = 1.0 + 66.0/18.068 = 1.0 + 3.653 = 4.65 → round up to 4.7 s.
Downhill grades reduce the effective deceleration term, which is why the same approach speed needs more yellow time going downhill than on the level.

Always round the computed value up to the next 0.1 s — never down, and never truncate to the nearest whole second on a signal controller that supports tenths.

## 2. All-red clearance interval worksheet

AR = (W + L) / v, where W = clearance path width in ft (stop bar to the far side of the last conflicting lane or crosswalk, whichever is farther), L = design vehicle length in ft (20 ft passenger car; 40–60 ft for a WB-50 semi if truck volume is material), v = the same 85th-percentile approach speed used for yellow, in ft/s.

Example — 6-lane cross street plus far crosswalk, W = 72 ft, L = 20 ft (passenger car), v = 66.0 ft/s (45 mph): AR = (72+20)/66.0 = 92/66.0 = 1.394 → round up to 1.4 s.

Truck-adjusted example, same intersection, L = 60 ft (WB-50 semi, truck share on this approach measured at 12% of ADT): AR = (72+60)/66.0 = 132/66.0 = 2.0 s.
When truck share on an approach exceeds roughly 10% of ADT, compute all-red off the truck length, not the passenger-car default — the passenger-car clearance interval strands the tail of a longer vehicle in the intersection.

## 3. MUTCD Chapter 4C signal-warrant determination worksheet

Commonly cited 100%-column thresholds for urban approaches with 2 or more lanes each direction — confirm exact figures against the current MUTCD edition and any state supplement before certifying a determination. A 70% factor applies where the major-street 85th-percentile speed exceeds 40 mph or the intersection sits in an isolated community under 10,000 population.

| Warrant | Major street, 8-hr volume (both approaches) | Minor street, 8-hr volume (highest approach) |
|---|---|---|
| 1A — Minimum Vehicular Volume | ≥600 vph, each of 8 hrs | ≥200 vph, each of the same 8 hrs |
| 1B — Interruption of Continuous Traffic | ≥900 vph, each of 8 hrs | ≥100 vph, each of the same 8 hrs |
| 3 — Peak Hour (unusual-case use only) | n/a (combined volume/delay chart) | ≥100 vph for 1 hr, plus minor-street approach delay ≥4 vehicle-hours |

Example determination — Oak St & 12th Ave, 2-lane approaches both streets, 8-hour classification count: major-street volumes ranged 610–780 vph across the 8-hour study window; minor-street highest approach ranged 140–175 vph.
- Warrant 1A needs minor ≥200 vph for a 2+-lane approach — measured max of 175 vph fails.
- Warrant 1B needs major ≥900 vph — measured max of 780 vph fails.
- Determination: no warrant met on this count. Recommend re-count in 12 months, or immediately after the adjacent development under construction opens and adds trips, rather than installing a signal now.

## 4. Pedestrian walk/clearance interval worksheet

Pedestrian clearance (flashing DON'T WALK) interval = crossing distance ÷ walking speed. Walking speed default = 3.0 ft/s (MUTCD 11th ed./PROWAG-aligned general assumption); use a documented slower speed (e.g., 2.8 ft/s) where the crossing serves a population skewing toward the accessible/slower end — senior housing, hospital frontage, assisted-living facility. Minimum WALK interval = 7 s; do not reduce below this without a documented pedestrian-volume/engineering-study justification.

Example — 6-lane arterial crossing, general population: crossing distance = 54 ft. Clearance = 54/3.0 = 18.0 s. Minimum total pedestrian phase = 7 + 18.0 = 25.0 s.

Example — crossing at a senior-center frontage, documented slower walking speed 2.8 ft/s: crossing distance = 48 ft. Clearance = 48/2.8 = 17.14 → round up to 17.2 s. Minimum total pedestrian phase = 7 + 17.2 = 24.2 s. Compare against the vehicle phase it rides on (22 s green + 4.5 s change interval = 26.5 s total): 26.5 s clears the 24.2 s floor with 2.3 s margin — no timing change needed, but the push button dates to the original installation and should be flagged for an APS upgrade audit regardless.

## 5. Corridor coordination worksheet — cycle length and offsets

Webster optimal cycle length: C₀ = (1.5L + 5) / (1 − Y), where L = total startup lost time per cycle (s) and Y = sum of critical volume/saturation-flow ratios across the phases.

Example — 4-phase signal, lost time ≈ 3 s/phase × 4 phases → L = 12 s. Critical flow ratios: Y1 = 0.28, Y2 = 0.19, Y3 = 0.15, Y4 = 0.12 → ΣY = 0.74.
C₀ = (1.5×12 + 5) / (1 − 0.74) = (18+5)/0.26 = 23/0.26 = 88.5 → round to a 90 s cycle for corridor-wide use.
If the corridor is currently running a 100 s cycle, the 90 s optimum flags roughly 10 s/cycle of unnecessary delay being carried by every vehicle at every signal on the route — a case for reducing the coordinated cycle, not evidence that the longer cycle is the "safer" choice.

Offset calculation: adjacent signal 700 ft downstream, target progression speed 35 mph = 51.3 ft/s. Ideal offset = distance ÷ speed = 700/51.3 = 13.65 → program 14 s (round to the controller's whole-second resolution).

Ripple rule: if an upstream signal's phase split changes by Δt seconds for any reason (a clearance-interval fix, a pedestrian-minimum adjustment), every downstream offset in the coordinated group must shift by the same Δt to preserve the band. Example: the through-phase clearance fix above added 0.7 s to signal 4's cycle reference point; signal 5's offset moves from 14 s to 14 − 0.7 ≈ 13.3 s → program 13 s, not left unchanged.
