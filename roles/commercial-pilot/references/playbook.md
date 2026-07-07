# Commercial Pilot Playbook

Filled worksheets and reference tables for the calculations the SKILL.md decision framework calls for. Numbers below are illustrative, self-consistent examples in the shape of a Caravan-class single-engine turbine — always substitute the current aircraft's actual AFM/POH and W&B data.

## 1. Density altitude quick-reference table

Pressure altitude (PA) = field elevation + (29.92 − altimeter setting) × 1,000. Density altitude (DA) ≈ PA + 120 × (OAT °C − ISA temp at PA), where ISA temp = 15°C − 2°C per 1,000 ft of PA.

| Field elevation | Altimeter | OAT | PA | ISA temp at PA | DA |
|---|---|---|---|---|---|
| 1,000 ft | 29.92 | 25°C | 1,000 ft | 13.0°C | 1,000 + 120×12.0 = 2,440 ft |
| 3,000 ft | 30.05 | 30°C | 2,870 ft | 9.3°C | 2,870 + 120×20.7 = 5,354 ft |
| 6,500 ft | 30.10 | 30°C | 6,320 ft | 2.4°C | 6,320 + 120×27.6 = 9,632 ft |
| 6,500 ft | 30.10 | 34°C | 6,320 ft | 2.4°C | 6,320 + 120×31.6 = 10,112 ft |
| 9,927 ft | 30.00 | 20°C | 9,905 ft | -4.8°C | 9,905 + 120×24.8 = 12,881 ft |

Rule of thumb this table demonstrates: at high-elevation fields, a single-digit temperature swing (30°C → 34°C) moves DA by roughly 500 ft on its own — recompute rather than reuse a morning number for an afternoon departure.

## 2. Weight and balance worked worksheet

Scenario: Caravan-class aircraft, passenger charter, basic empty weight 5,240 lb / arm 172.5 in.

| Item | Weight (lb) | Arm (in) | Moment (in-lb) |
|---|---|---|---|
| Basic empty weight | 5,240 | 172.5 | 904,140 |
| Pilot | 200 | 140.0 | 28,000 |
| Front passenger | 170 | 140.0 | 23,800 |
| Middle-row passengers (3) | 480 | 180.0 | 86,400 |
| Aft-row passengers (2) | 340 | 214.0 | 72,760 |
| Baggage/cargo | 150 | 240.0 | 36,000 |
| Fuel, planned load | 1,000 | 197.0 | 197,000 |
| **Takeoff total** | **7,580** | | **1,348,100** |

Takeoff CG = 1,348,100 ÷ 7,580 = **177.9 in**. Example envelope at 7,580 lb: 173.0–182.0 in → within envelope, 4.1 in margin to aft limit, 4.9 in to forward limit.

Recheck at estimated landing weight (400 lb fuel burned, arm 197.0):

| | Weight (lb) | Moment (in-lb) |
|---|---|---|
| Takeoff | 7,580 | 1,348,100 |
| Less fuel burned | −400 | −78,800 |
| **Landing total** | **7,180** | **1,269,300** |

Landing CG = 1,269,300 ÷ 7,180 = **176.8 in**. Fuel arm (197.0) sits aft of the running CG, so burning it moves CG forward — confirm the *landing*-weight envelope (example: 172.0–180.0 in at 7,180 lb) separately from the takeoff-weight envelope; a load that's fine at brake release is not automatically fine in the flare.

**Load-change rule:** any manifest change after this worksheet is finalized (extra cargo, reassigned seating) requires rerunning both rows, not just adding the new weight to the total — arm, not just weight, is what moves CG.

## 3. Go/no-go decision points by phase of flight

| Phase | Trigger | Action if triggered |
|---|---|---|
| Preflight/planning | Forecast ceiling/vis at ETA ±1 hr below personal minimum, or AFM-distance margin <20% at actual DA/weight | No-go, or replan: lighter load, later/earlier departure, different runway |
| Before engine start | Fuel plan doesn't cover reserve + one full missed approach/hold above regulatory floor | Add fuel or reduce payload before pushback |
| Line up for takeoff | Crosswind component (gust-adjusted, not steady) at or above personal crosswind minimum | Hold for a lull, request runway change, or divert |
| Climb-out | Actual climb rate materially below chart-predicted rate for this DA/weight in the first 500 ft | Do not continue climb-out over terrain requiring book performance; consider return |
| Cruise/en route | Fuel remaining at a named checkpoint below reserve + 30-min contingency | Divert to the pre-briefed alternate now, not at destination |
| Descent/approach | Reported ceiling/vis below personal (not just legal) approach minimums, or a worsening trend on the last two METARs | Execute the pre-briefed missed-approach/alternate plan; don't renegotiate the trigger in the moment |

## 4. Personal minimums card (filled example)

| Category | Legal minimum | This pilot's personal minimum |
|---|---|---|
| Day VFR ceiling/visibility | Class E: 1,000 ft / 3 sm | 1,500 ft / 5 sm |
| Night VFR ceiling/visibility | Same as day | 3,000 ft / 8 sm |
| IFR approach minimums | Published minima | Published + 200 ft / +½ sm (waived only at home airport with 50+ logged approaches) |
| Crosswind component | Max demonstrated 20 kt (example type) | 15 kt steady; 12 kt if gust spread >8 kt |
| Runway margin | Any length ≥ AFM total distance | AFM total distance × 1.5 |
| Fuel on landing | 45 min IFR / 30–45 min VFR | Regulatory reserve + 30 min contingency |
| Duty day | Part 135 example limit: 14 hr | Personal stop at 12 hr if more than one leg remains |

## 5. Fuel planning worksheet (filled example)

| Leg | Planned burn | Reserve required | Contingency | Total required | Fuel loaded | Margin |
|---|---|---|---|---|---|---|
| KXYZ–KABC | 210 lb (1.5 hr @ 140 lb/hr) | 105 lb (45 min IFR) | 70 lb (30 min) | 385 lb | 450 lb | +65 lb (17%) |
| KABC–KXYZ (return) | 245 lb (1.75 hr @ 140 lb/hr, headwind added) | 105 lb | 70 lb | 420 lb | 450 lb | +30 lb (7%) — below the 15% target; add fuel or trim payload before this leg, not after |
