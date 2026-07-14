# Playbook

## Driving log format (filled example)

Pile 7, HP14x89, Pier P2, hammer: single-acting diesel, ram weight 6,600 lb, rated stroke 10.0 ft.

| Depth (ft) | Blows/ft | Stroke (ft) | Delivered energy (ft-lb) | Notes |
|---|---|---|---|---|
| 0–10 | 8 | 6.0 (warm-up) | 39,600 | Hammer warming up; not yet at rated stroke |
| 10–20 | 14 | 7.5 | 49,500 | Loose fill/upper sand |
| 20–30 | 22 | 8.0 | 52,800 | Medium-dense sand |
| 30–40 | 28 | 8.0 | 52,800 | Consistent |
| 40–50 | 31 | 8.0 | 52,800 | Consistent |
| 50–58 | 36 (this ft) | 8.0 | 52,800 | Below 72 bpf bearing-graph floor at planned tip — continue |
| 58–61 | 96 (this ft) | 8.0 | 52,800 | Within 72–108 bpf predicted range — stop, flag for PDA |

Delivered energy = ram weight (6,600 lb) × observed stroke (ft). Compare against the wave-equation analysis's assumed energy (52,800 ft-lb at 80% of 66,000 ft-lb rated) before attributing a low blow count to soil rather than hammer performance.

## Bearing-graph reading procedure

1. Confirm which bearing graph applies: hammer model and energy setting, cushion type/condition, pile section, and the soil-resistance distribution assumption must all match the pile being driven — a new hammer, a cushion change, or a different pile section requires a re-run, not a reused graph.
2. At each recorded blow count, read the corresponding nominal resistance off the graph's curve (not a straight-line interpolation between two arbitrary points — use the graph as supplied by the geotechnical engineer, which is already the analysis output).
3. Compare the read resistance to the contract's required nominal resistance (design load × factor of safety, or the stated ultimate resistance directly).
4. If below required resistance at planned tip elevation: continue driving (unless the depth already exceeds a maximum specified in the contract, in which case stop and escalate to the geotechnical engineer — do not drive past a contract-stated maximum depth without engineering sign-off).
5. If at or above required resistance: stop driving; log final blow count, depth, and stroke; flag pile for any restrike or dynamic-test requirement.
6. If blow count spikes far above the graph's range at a depth well above the anticipated bearing stratum: stop driving immediately; treat as probable obstruction per the obstruction-response sequence below, not as early refusal.

## Obstruction-response sequence (preference order)

1. **Verify against records** — check the boring log at or near this pile location and any obstruction history from adjacent piles in the same footing/pier before assuming it's an obstruction rather than a genuinely shallow bearing layer (rare but possible if the boring was offset from the actual pile location).
2. **Attempt to drive through** if the obstruction is thin/isolated (single cobble-scale) and the pile section and hammer energy are adequate per the geotechnical engineer's guidance — log blow count through the event; resistance should drop back toward the pre-obstruction trend once through.
3. **Predrill or spud through** if driving-through attempts fail or risk pile damage — predrill to a depth just above the obstruction, or use a spud/mandrel to break it up, then resume normal driving.
4. **Relocate the pile** a short distance (within the tolerance the structural engineer allows for the footing) if predrilling/spudding isn't practical, with the relocation and any resulting eccentricity documented and reviewed by the structural engineer.
5. **Escalate for a design change** (larger footing, additional pile, alternate foundation type at this location) only after the above options are exhausted or ruled out by the engineer of record — this is the highest-cost, highest-schedule-impact option and is a last resort, not a first response to an obstruction.

## Restrike wait-time table by soil type (representative — verify against the project geotechnical report)

| Predominant soil at pile tip | Expected behavior | Typical restrike wait | What to watch for |
|---|---|---|---|
| Saturated soft-to-stiff clay, clayey silt | Setup (capacity gain) | 24 hours minimum; several days to 1–2 weeks for thick, plastic clay | Restrike blow count higher than end-of-drive; use it to confirm/upgrade capacity, not to shorten the wait |
| Loose-to-medium-dense clean sand or gravel | Minimal time-dependent change | Often none required beyond a short confirmation restrike | Blow count roughly stable end-of-drive to restrike |
| Dense fine sand, silt, or silty sand | Relaxation risk | Restrike as soon as practical (hours), then again if the first restrike shows a drop | Restrike blow count lower than end-of-drive — take the lower number as governing |
| Weathered or fractured rock | Relaxation risk | Restrike within 24 hours | Same as above — don't rely on end-of-drive alone |
| Mixed/interbedded profile | Depends on which stratum governs tip resistance | Follow the geotechnical engineer's soil-specific recommendation for the governing stratum | Confirm which layer the analysis attributes most resistance to before picking a wait time |

## Pile group driving-sequence template (tight-spacing groups, center-to-center under ~3 pile diameters)

1. Identify the group's geometric center and any batter piles (batter piles typically driven last, after vertical piles establish the group geometry, unless the engineer specifies otherwise).
2. Drive from the center of the group outward in rings, or per the geotechnical engineer's explicit sequence drawing if one is provided — never in installation-convenient (e.g., left-to-right) order on a tight group without checking the specified sequence first.
3. After each ring, survey previously driven piles in the group for heave (vertical movement) and lateral displacement against the pre-drive baseline survey.
4. If heave on any pile exceeds the project's stated tolerance (commonly on the order of a few tenths of an inch to a half inch — confirm the project-specific number), flag that pile for re-driving to restore penetration and re-verify capacity before proceeding with the remaining ring.
5. Complete the group; final survey and driving log become part of the as-built record before the pile cap is formed and poured — once concrete is placed, heave correction is no longer an option.
