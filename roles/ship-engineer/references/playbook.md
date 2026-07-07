# Ship Engineer — Playbook

## Cooling/lube-oil trend worksheet (filled example)

Read the trend across at least three successive readings, not a single snapshot against the alarm setpoint.

| Time | JCW temp (°C) | Δ from prior | SW pump discharge pressure (bar) | Δ from prior |
|---|---|---|---|---|
| 0200 | 82 | — | 2.2 | — |
| 0205 | 86 | +4 | 1.8 | −0.4 |
| 0210 | 88 (alarm) | +2 | 1.4 | −0.4 |

- **Rate of climb:** (88 − 82) / 10 min = 0.6°C/min.
- **Time to shutdown setpoint (95°C):** (95 − 88) / 0.6 = 11.7 min if the trend continues unaddressed.
- **Root-cause signal:** SW pump discharge pressure has fallen 2.2 → 1.4 bar (a 36% drop) against a normal band of 2.0–2.4 bar — the cooling-water supply side, not the engine, is the primary fault; treat the temperature rise as a symptom.
- **Action threshold:** cut in the standby SW pump and strainer as soon as the trend projects a threshold crossing inside the next 15 minutes — do not wait for the 95°C shutdown to make the decision for you.
- **Confirm the fix worked:** re-plot after switching pumps. Temperature should stabilize or fall within 2–3 readings (roughly 10–15 minutes); if it keeps climbing, the fault is downstream of the pump (fouled cooler, closed valve) and requires further isolation, not another pump swap.

## CO2 muster-verification checklist (filled example)

Before authorizing a fixed CO2 release into any machinery space, complete every line — do not skip ahead because the fire looks urgent.

| Step | Action | Example result |
|---|---|---|
| 1 | Pull the current watch/duty roster for the affected space | 2/E + 1 oiler expected in engine room |
| 2 | Sound local space-evacuation alarm, direct all hands to muster stations | Sounded 0215:30 |
| 3 | Take headcount at each muster station and reconcile against roster | 2/E confirmed at CO2 station 0216; oiler unaccounted |
| 4 | If any expected person is unconfirmed, HOLD release and actively locate them | Oiler traced to shaft alley via sound-powered phone, confirmed clear via bridge 0217:30 |
| 5 | Confirm ventilation/dampers closed and fuel quick-closing valves shut | Confirmed 0217:45 |
| 6 | Sound the mandatory pre-discharge alarm (audible, distinct from the fire alarm, minimum duration per SOLAS Ch II-2 Reg 10) | Sounded 0218:00 |
| 7 | Only after steps 1–6 reconcile, operate the release | Released 0218:20 |

A release attempted at step 3 — before the oiler was located — would have flooded an occupied space. The 90-second hold between the fire alarm (0215) and the actual release (0218:20) is the correct outcome, not a delay to be minimized next time.

## Black-start / stepped-load worksheet (filled example)

Total blackout, dead-ship condition. Emergency generator: 100 kW rated. Main auxiliary generator (DG1) being black-started: 500 kW rated.

**Phase 1 — emergency generator pickup (must be online within 45 seconds of main power loss per SOLAS Ch II-1 Reg 42/43):**

| Load | kW | Cumulative kW | % of 100 kW emergency capacity |
|---|---|---|---|
| Emergency lighting | 5 | 5 | 5% |
| Steering gear hydraulic pump | 30 | 35 | 35% |
| Emergency fire pump | 45 | 80 | 80% |

80 kW of 100 kW capacity leaves 20 kW (20%) of margin — enough for radio/navigation loads but not enough to add propulsion auxiliaries; those wait for DG1.

**Phase 2 — DG1 black-start and stepped load restoration (500 kW rated):**

| Step | Load added | kW | Cumulative kW | Cumulative % of rated capacity | Check before next step |
|---|---|---|---|---|---|
| 1 | Engine-room blowers, FO/LO service pumps | 150 | 150 | 30% | Frequency/voltage stable for ≥2 min |
| 2 | Steering gear + navigation transferred from emergency bus | 50 | 200 | 40% | Frequency/voltage stable for ≥2 min |
| 3 | Remaining propulsion auxiliaries + accommodation | 300 | 500 | 100% | Full load confirmed stable |

Rule of thumb: no single step exceeds roughly 40% of rated capacity on a cold-started generator — a bigger single step risks a frequency/voltage dip severe enough to trip the breaker and re-blackout the vessel, discarding the recovery already made.

## OCM / Oil Record Book worked entry (filled example)

| Item | Value |
|---|---|
| OCM reading, bilge holding tank sample | 22 ppm |
| MARPOL Annex I, Reg 14 discharge limit | 15 ppm |
| Holding tank capacity | 12 m³ |
| Holding tank level at time of reading | 9.5 m³ (79%) |
| Bilge accumulation rate (this vessel, current condition) | ~0.3 m³/day |
| Days to next port | 2 |
| Projected level at arrival | 9.5 + (0.3 × 2) = 10.1 m³ |
| Margin against capacity | 12 − 10.1 = 1.9 m³ |

Because 22 ppm exceeds the 15 ppm limit, no discharge is authorized regardless of how close the reading is to the line. Because the projected holding-tank level at arrival (10.1 m³) stays under capacity (12 m³) with 1.9 m³ to spare, holding the water rather than discharging it is the feasible option — the arithmetic, not a general sense of caution, is what makes "hold" the correct call here rather than an overcautious one. Oil Record Book Part I entry is written the same watch: sample result, limit cited, tank levels, corrective action (coalescer replacement) scheduled, and shoreside disposal arranged as the fallback if a compliant sample isn't achieved before arrival.
