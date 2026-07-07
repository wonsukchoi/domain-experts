# Playbook

Filled walkthroughs for the four places this trade gets shortcut: fixture-unit sizing, backflow-device selection, water-hammer arrestor sizing, and system-by-system pressure testing. Numbers are worked examples to adapt, not universal constants — always check the jurisdiction's adopted code edition and any local amendment.

## 1. Fixture-unit sizing (DFU for drainage, WSFU for supply)

**Drainage fixture units (DFU), common baseline values:**

| Fixture | DFU |
|---|---|
| Lavatory | 1 |
| Bathtub / shower stall | 2 |
| Kitchen sink (with disposal) | 2 |
| Water closet (tank type) | 4 |
| Water closet (flushometer) | 6 |
| Floor drain (2 in.) | 3 |

**Horizontal branch and building-drain capacity by pipe size (illustrative — verify against the adopted table):**

| Pipe size | Max DFU, horizontal branch | Max DFU, building drain at 1/4 in./ft |
|---|---|---|
| 1-1/2 in. | 3 | — |
| 2 in. | 6 | 21 |
| 3 in. | 20 (no water closets under 3 in.) | 42 |
| 4 in. | 160 | 216 |

**Worked sizing example:** A remodel adds a lavatory (1 DFU) + shower (2 DFU) + water closet, tank type (4 DFU) = **7 DFU total**. The water closet alone mandates a minimum 3 in. branch regardless of load. At 20 DFU capacity for a 3 in. branch, 7 DFU is **35% utilized** — correctly sized, not a candidate for upsizing.

**Water-supply fixture units (WSFU), common baseline values (private/residential):**

| Fixture | WSFU (cold) |
|---|---|
| Lavatory | 0.5 |
| Bathtub | 1.0 |
| Shower stall | 1.0 |
| Water closet (tank, 1.6 gpf) | 2.2 |
| Kitchen sink | 1.0 |
| Hose bibb | 2.5 |

**Worked example:** A 3-bathroom house totals roughly 18 WSFU (2 full baths at ~6 WSFU each + a powder room at ~1.5 WSFU + kitchen/laundry at ~4.5 WSFU). At 18 WSFU and a typical 40–50 psi supply pressure with a 40 ft run, the supply-pipe sizing curve calls for a **3/4 in. main** with 1/2 in. branches to individual fixtures — a 1 in. main sized "to be safe" past the curve's requirement adds a dead-leg volume that lags temperature response at every fixture without improving flow.

## 2. Trap-to-vent maximum distance (illustrative baseline — confirm against IPC Table 909.1 / UPC Table 1002.2)

| Trap arm (drain) size | Max distance, trap weir to vent |
|---|---|
| 1-1/4 in. | 2 ft 6 in. |
| 1-1/2 in. | 3 ft 6 in. |
| 2 in. | 5 ft 0 in. |
| 3 in. | 6 ft 0 in. |
| 4 in. | 10 ft 0 in. |

**Rule:** measure the actual horizontal (plus any allowed vertical) run from the trap weir to the vent connection before finalizing rough-in — a run that clears the *slope* minimum can still exceed this *distance* maximum, which is the more common miss. Individual vent minimum diameter is the smaller of half the served drain's diameter or 1.25 in., whichever is larger in practice.

## 3. Backflow-device selection by cross-connection hazard class

| Connection example | Hazard class | Exposure | Device |
|---|---|---|---|
| Irrigation system tied to potable main | Non-health (pollutant) | Backpressure only | Double-check valve assembly (DCVA, ASSE 1015) |
| Boiler makeup water | Health hazard (chemical treatment) | Backpressure and back-siphonage | Reduced-pressure-zone assembly (RPZ, ASSE 1013) |
| Hose bibb / mop sink, hose can be submerged | Health hazard (foreseeable submersion) | Back-siphonage under vacuum | Atmospheric vacuum breaker (AVB, ASSE 1001) or hose-bibb vacuum breaker, min. 6 in. above flood-level rim |
| Fire sprinkler system with no chemical additive | Non-health | Backpressure only | Double-check assembly, or per local fire-code amendment |
| Chemical dispensing / commercial dishwasher | Health hazard | Back-siphonage and backpressure | Air gap (preferred) or RPZ |

**Decision rule:** classify hazard first (health vs. non-health), then classify exposure (backpressure-only vs. back-siphonage-possible). A device rated only for backpressure (DCVA) never substitutes for one rated for back-siphonage (AVB/PVB/RPZ) on a health-hazard connection — this is a device-class mismatch, not a matter of degree.

## 4. Water-hammer arrestor sizing (PDI-WH201, fixture-unit load method)

| Fixture-unit load at the valve group | PDI-WH201 arrestor size |
|---|---|
| 1–11 (single washer or dishwasher) | AA |
| 12–32 | A |
| 33–60 | B |
| 61–113 | C |
| 114–154 | D |
| 155–330 | E |
| 331–450 | F |

**Placement rule:** install as close as possible to the quick-closing valve(s) generating the hammer (washing machine box, dishwasher branch, flush valve), not centrally on the main — arrestor effectiveness drops off sharply with distance from the valve because the pressure wave has already reflected before reaching a distant arrestor.

## 5. Thermal expansion — closed-system trigger and sizing

**Trigger:** any check valve, pressure-reducing valve (PRV), or backflow preventer on the cold main converts the water heater into a closed system — code requires expansion control the moment one of these devices is present, not as a discretionary upgrade.

**Worked sizing example:** 50-gallon water heater, system operating pressure 80 psi (post-PRV). Per a typical expansion-tank manufacturer's chart, a 50-gallon heater at 80 psi requires roughly a **2-gallon acceptance-volume tank** (tank total volume larger; acceptance volume is the usable expansion space at that pre-charge and system pressure). Undersizing the tank (e.g., installing a 2-gallon nominal tank rated for only 40 psi systems) leaves the T&P relief valve to absorb the excess, producing intermittent weeping that gets misdiagnosed as a bad relief valve rather than an undersized expansion tank.

## 6. Pressure- and leak-test parameters by system (illustrative baseline — verify against adopted code edition)

| System | Test method | Test pressure | Hold time | Pass criterion |
|---|---|---|---|---|
| DWV (water test) | Fill to 10 ft head (or to roof via vent) | 10 ft head minimum | 15 min | No visible leakage, no drop |
| DWV (air test alternative) | Air test ball/plug | 5 psi | 15 min | No drop greater than 0.1 psi |
| Potable water supply | Hydrostatic | Working pressure or 1.5x working pressure, whichever code specifies | 15 min | No gauge drop |
| Low-pressure fuel gas (residential) | Air/manometer | 3 psi minimum (systems under 3.5 in. w.c. operating) | 10 min minimum, varies by piping volume | No perceptible pressure loss |
| Higher-pressure gas / steam | Air or inert gas | 1.5x working pressure or higher per code class | Per code, typically longer than low-pressure test | No perceptible pressure loss |

**Rule:** never apply one system's test parameters to another — a low-pressure residential gas test at 3 psi for 10 minutes says nothing about the integrity of a steam system or a higher-pressure gas class, which test at a multiple of their own working pressure, not a flat number borrowed from the residential case.
