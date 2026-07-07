# Chemical Engineer — Artifacts

## Mass/energy balance worksheet (reactor node)

| Stream | Component | Flow (kg/h) | Temp (°C) | Notes |
|---|---|---|---|---|
| In-1 | Reagent A | 1,200 | 20 | Fed continuously |
| In-2 | Solvent | 3,400 | 20 | Recycle from Column C-101 |
| In-3 | Reagent B | 640 | 20 | Metered addition |
| Out-1 | Product stream | 4,980 | 45 | To separation |
| Out-2 | Vent (light ends) | 260 | 45 | To scrubber |
| **Balance check** | — | In: 5,240 / Out: 5,240 | — | **DOF = 0, closes to 0.0%** |

DOF count for this node: 5 unknowns (Out-1 flow/composition, Out-2 flow/composition, reactor temp) minus 5 independent equations (2 component balances, 1 energy balance, 2 measured feed compositions) = 0. If any feed composition is unmeasured, DOF becomes 1 — stop and instrument before solving.

## HAZOP worksheet (excerpt, one node)

| Node | Deviation | Cause | Consequence | Safeguard | Action |
|---|---|---|---|---|---|
| Reactor R-101 feed line | More flow (Reagent A) | Control valve fails open | Stoichiometric excess → uncontrolled exotherm | High-flow alarm + independent high-temp interlock (SIS) | Verify interlock trip setpoint is 15°C below adiabatic runaway onset; confirm annual proof-test schedule |
| Reactor R-101 feed line | No flow (Solvent) | Pump trip | Loss of dilution → concentration-driven exotherm | Low-flow interlock trips feed of Reagent A | Confirm interlock uses independent flow transmitter, not shared with BPCS indication |
| Reactor R-101 | More pressure | Cooling failure + continued reaction | Overpressure, potential relief lift | Relief valve (fire + runaway case, API 521) | Recompute relief load for runaway case per DIERS two-phase methodology; confirm not sized on fire case alone |

## LOPA scenario table (excerpt)

| Scenario | Initiating cause freq (per yr) | Consequence severity | Independent protection layers | PFD each | Mitigated frequency | Target | Gap? |
|---|---|---|---|---|---|---|---|
| Reactor overpressure from cooling-water loss | 0.1 | Major (relief discharge, potential injury) | BPCS high-temp alarm + operator response (PFD 0.1); SIS high-temp trip (PFD 0.01); relief valve (PFD 0.01) | — | 0.1 × 0.1 × 0.01 × 0.01 = 1×10⁻⁶ /yr | ≤1×10⁻⁵ /yr | No gap |
| Reactor overpressure from cooling-water loss (if BPCS alarm and SIS trip share one temp transmitter) | 0.1 | Major | BPCS alarm + SIS trip **not independent** (shared sensor, PFD counts once at 0.1) + relief (0.01) | — | 0.1 × 0.1 × 0.01 = 1×10⁻⁴ /yr | ≤1×10⁻⁵ /yr | **Gap — 10x over target** |

The second row is the standard trap: two logically distinct alarms sharing one transmitter give only one layer's worth of risk reduction, not two.
