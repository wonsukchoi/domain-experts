# Structural firefighting playbook — filled sequences

Executable sequences with real numbers, not descriptions of sequences. Scenario used throughout: Engine 7, 2,400 sq ft single-story residence, built 2006 (engineered I-joist construction), reported child trapped, first-arriving four-person crew.

## 1. Size-up checklist (compressed COAL WAS WEALTH, transmitted as the initial report)

| Factor | This incident | Why it matters here |
|---|---|---|
| Construction | 2006, engineered I-joist roof/floor | Collapse clock measured in single-digit minutes once the cavity is involved, not the 18+ min of legacy dimensional lumber |
| Occupancy | Single-family residential | One likely floor plan pattern (bedrooms toward rear/sides), not a compartmentalized commercial layout |
| Life hazard | 1 reported, Bravo-side bedroom, unconfirmed | Drives the offensive call and the VEIS assignment before a full 360 is complete |
| Smoke | Light gray, moderate velocity, Bravo side only | Pre-flashover, no backdraft indicators — supports entry now, not a wait-and-vent-first call |
| Water supply | Hydrant 400 ft from scene, engine tank 500 gal | Tank water covers the first ~3–4 min of flow at target gpm; hydrant line must be established inside that window |
| Exposures | Detached homes, ~15 ft setback both sides | Low exposure priority this arrival; revisit if fire vents through the roof |
| Time | Dispatched 14:32, on scene 14:36, fire duration before call unknown | Unknown pre-arrival burn time is treated as "assume closer to flashover than comfortable," not "assume early-stage" |

Rule: if any two of {engineered/lightweight construction, smoke condition worsening, unknown fire duration >10 min} are true together, tighten the SCBA trigger point and shorten the reassessment interval from 5 minutes to 3.

## 2. Strategy decision matrix

| Condition | Call | Action |
|---|---|---|
| Tenable smoke/heat + viable rescue reported or confirmed | **Offensive** | Commit interior crew to rescue/attack; two-in/two-out rescue exception applies for the initial entry only |
| Marginal tenability, no confirmed rescue, quick exterior hit could improve conditions | **Transitional** | Brief exterior knockdown (15–30 sec) from a position that won't push the flow path toward any occupant or interior crew, then reassess for offensive |
| Heavy fire >50% structural involvement, collapse indicators present, or no viable rescue possible | **Defensive** | Withdraw/stay exterior, establish collapse zone at 1–1.5× building height, exterior streams only |

Re-test cadence: every 3–5 minutes, or immediately on any of — smoke color/velocity change, a reported mayday, confirmed additional victims, or visible structural sag/cracking.

## 3. SCBA air-budget worksheet (rule of thirds, working exertion)

```
Cylinder rating:            4,500 psi, 30-min NFPA-rated (resting rate)
Working-exertion yield:     ~13–15 min actual (roughly half of rated,
                             per elevated heart rate / heat stress)
Budget used for planning:   13.5 min (conservative end of range)

Step 1 — first third (reach objective):     13.5 / 3 = 4.5 min
Step 2 — second third (perform task):       13.5 / 3 = 4.5 min
Step 3 — last third (exit + margin):        13.5 / 3 = 4.5 min

Trigger to abort task and turn to exit: low-air alarm (25% remaining,
~1,125 psi) OR elapsed time exceeds 9 min (end of second third),
whichever comes first.
```

FF Diaz's actual consumption against this budget:

```
14:37:30  Mask on, air start
14:38:00–14:39:00  (1.0 min) Force Bravo window, vent, isolate re-entry point
14:39:00–14:43:00  (4.0 min) Search bedroom + closet, locate victim at 14:42
14:43:00–14:45:00  (2.0 min) Extract via window to staged EMS
----------------------------------------------------------------
Total elapsed:      7.5 min against a 13.5-min budget (~55% consumed)
Margin remaining:   ~6 min — task completed inside the planned two-thirds,
                     not against the low-air alarm
```

## 4. Coordinated attack / VEIS timing sequence

1. **T+0** (14:37:00) — Strategy called offensive, tasks split: search team to VEIS, attack team to stretch and charge a line.
2. **T+30s** — Attack team masks up, begins stretching 1¾" line (200 ft, target flow below).
3. **T+90s** — Search team forces the reported-victim-side window; door/window on the attack side (Alpha) held **vent-limited** — cracked only enough to feed the hose — until water is confirmed flowing.
4. **T+2:00** — Search team enters through the window and immediately **isolates** (closes the bedroom door) before proceeding — this is the step that prevents the flow path from connecting the search area to whatever the attack team's entry does next.
5. **T+2:30–3:00** — Attack line charged and confirmed at the pump; only now does the attack team fully open the Alpha entry point and advance.
6. **Rule:** never let a second opening (search team's window, a failed window, a second door) exist simultaneously with the attack entry unless water is already flowing through the attack opening — two unlinked openings before knockdown is the uncoordinated-flow-path condition tied to accelerated heat release.

## 5. Needed fire flow (rough planning formula, NFA method)

```
Needed fire flow (gpm) = (Length × Width) / 3, adjusted for % involvement

This structure: 2,400 sq ft ÷ 3 = 800 gpm if fully involved
Actual involvement at arrival: ~15% (one room/corner) → 800 × 0.15 ≈ 120 gpm
```

Tank water check: 500 gal ÷ 120 gpm ≈ 4.2 minutes of flow before the hydrant supply must be established — Engineer Ortiz lays in from the 400 ft hydrant immediately on arrival rather than waiting to see if tank water is enough, because 4.2 minutes is inside the length of the search-and-attack operation, not a comfortable margin past it.

## 6. Mayday / LUNAR protocol

1. Firefighter in trouble transmits "Mayday, Mayday, Mayday" on the tactical channel.
2. Command immediately clears all non-mayday radio traffic on that channel.
3. Firefighter (or last crew member with contact) transmits LUNAR:
   - **L**ocation — division/room/last known point
   - **U**nit — company/unit designation
   - **N**ame — the firefighter's name
   - **A**ssignment — what they were doing when trouble started
   - **R**esources needed — air, extraction tools, hoseline, additional RIT
4. Command activates and directs the staged RIT/FAST crew to the reported location; a second RIT is requested if the first is committed.
5. All other crews not directly supporting the mayday continue their assigned tasks unless redirected — a mayday does not automatically abandon fire attack, because an uncontrolled fire can create a second mayday.
6. PAR (personnel accountability report) is taken for every other crew on scene immediately after the mayday is declared, confirming no second incident is developing unnoticed.
