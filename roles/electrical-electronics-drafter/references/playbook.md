# Playbook

Filled tables and formulas an electrical/electronics drafter runs against. Verify against the code edition and project standard in force — these are commonly applied 2023 NEC and IPC-2221 values, not a substitute for the project's specific standard in front of you.

## 1. Conductor ampacity (NEC Table 310.16, copper, subset)

| AWG/kcmil | 60°C col. | 75°C col. | 90°C col. (THHN) |
|---|---|---|---|
| 14 | 15A | 20A | 25A |
| 12 | 20A | 25A | 30A |
| 10 | 30A | 35A | 40A |
| 8 | 40A | 50A | 55A |
| 6 | 55A | 65A | 75A |
| 4 | 70A | 85A | 95A |
| 2 | 95A | 115A | 130A |
| 1/0 | 125A | 150A | 170A |

**Rule (110.14(C)):** the applicable column is the *lowest* temperature rating among the conductor insulation, the termination it lands on, and the equipment it's listed with — not automatically the insulation's own rating. Most breakers, starters, and terminal blocks rated ≤100A are dual-listed 60/75°C; equipment >100A is typically 75°C. Only use the 90°C column when every termination in the circuit is separately listed for 90°C.

*Example: 10 AWG THHN (90°C rated 40A) landing on a starter terminal rated 75°C max is limited to 35A, not 40A — see SKILL.md worked example.*

## 2. Continuous-load conductor sizing (210.19(A)(1) / 430.22)

**Minimum conductor ampacity = 125% x continuous load current**, unless the conductor and its termination/OCPD are both listed for 100% continuous duty.

*Example: 21A motor FLC x 1.25 = 26.25A minimum branch-circuit ampacity.*

## 3. Motor full-load current (NEC Table 430.250, 3-phase, subset)

| HP | 208V | 230V | 460V |
|---|---|---|---|
| 5 | 16.7A | 15.2A | 7.6A |
| 7.5 | 24.2A | 22A | 11A |
| 10 | 30.8A | 28A | 14A |
| 15 | 46.2A | 42A | 21A |
| 20 | 59.4A | 54A | 27A |
| 25 | 74.8A | 68A | 34A |

**Rule:** use the FLC from this table for branch-circuit, feeder, and overload sizing — never the motor nameplate's FLA, which reflects that specific motor's actual rated performance and is used only for overload-relay selection cross-check, not for conductor ampacity math.

## 4. Motor overload and short-circuit/ground-fault protection

| Protection type | Code section | Max multiplier of FLC |
|---|---|---|
| Overload (SF ≥1.15 or temp rise ≤40°C) | 430.32(A)(1) | 125% |
| Overload (SF <1.15) | 430.32(A)(1) | 115% |
| Inverse-time breaker, short-circuit/ground-fault | Table 430.52 | 250% (max, non-time-delay fuse 300%, time-delay fuse 175%) |

**Rule:** if the calculated maximum doesn't match a standard OCPD size, round up to the next standard size per 240.6(A) and 430.52(C)(1) Exception 1 — never round down, and never treat the overload percentage and the short-circuit percentage as the same calculation; they protect against different fault modes from two different table lookups.

*Example: 15 HP/460V motor, FLC 21A. Overload: 21 x 1.25 = 26.25A (set at nearest standard heater/trip, 27A). Short-circuit/ground-fault, inverse-time breaker: 21 x 2.50 = 52.5A → next standard size 60A.*

## 5. Equipment grounding conductor sizing (Table 250.122, copper, subset)

| Rating of OCPD ahead of the equipment | Min. copper EGC |
|---|---|
| 20A | 12 AWG |
| 30A–60A | 10 AWG |
| 100A | 8 AWG |
| 200A | 6 AWG |

**Rule:** EGC size is keyed to the OCPD's rating, not to the ampacity-derived phase conductor size — the two calculations can land on the same wire size by coincidence (as in the 60A/10 AWG worked example) but diverge as soon as the OCPD rating changes without the phase conductor changing, or vice versa.

## 6. Conduit fill (Chapter 9 Tables 1, 4, 5)

**Table 1 fill percentage by conductor count:** 1 conductor = 53%, 2 conductors = 31%, over 2 conductors = 40%.

**Table 4 — EMT internal area at 40% fill (subset):**

| Trade size | Total internal area | 40% fill area |
|---|---|---|
| 1/2" | 0.304 in² | 0.122 in² |
| 3/4" | 0.533 in² | 0.213 in² |
| 1" | 0.864 in² | 0.346 in² |

**Table 5 — THHN conductor area (subset):**

| AWG | Area |
|---|---|
| 12 | 0.0133 in² |
| 10 | 0.0211 in² |
| 8 | 0.0366 in² |
| 6 | 0.0507 in² |

*Example: 3 x 10 AWG THHN phase conductors + 1 x 10 AWG Cu EGC = 4 x 0.0211 = 0.0844 in², against 1/2" EMT's 0.122 in² 40%-fill allowance — fits with 0.0376 in² spare.*

**Rule:** count every conductor in the raceway (including the EGC) for the fill percentage lookup in Table 1, but exclude the EGC and any balanced neutral when counting current-carrying conductors for the Table 310.15(C)(1) ampacity adjustment factor (per 310.15(E)) — the two conductor counts serve different calculations and are not the same number.

## 7. Table 310.15(C)(1) adjustment factor for bundled current-carrying conductors

| Number of CCCs in raceway | Adjustment factor |
|---|---|
| 4–6 | 80% |
| 7–9 | 70% |
| 10–20 | 50% |

**Rule:** apply this factor to the temperature-column ampacity *before* comparing to the load, only when 4 or more current-carrying conductors share the raceway. 3 or fewer CCCs: no adjustment.

## 8. One-line vs. elementary (three-line) diagram — content comparison

| Element | One-line diagram | Elementary (three-line) diagram |
|---|---|---|
| Phase conductors | Single line represents all phases | Each phase (L1/L2/L3) drawn separately |
| Control/relay logic | Omitted | Full ladder logic, rungs numbered |
| OCPD rating | Shown as a callout | Shown plus terminal-level detail |
| Wire numbers | Not applicable (system-level view) | Assigned per net/segment, cross-referenced to panel wiring |
| Primary audience | System coordination, utility interface, short-circuit studies | Panel builder, field technician, troubleshooting |

**Rule:** never add control-relay logic to a one-line (it stops being a coordination-scale drawing) and never issue a one-line as the sole wiring reference for a circuit with control logic — the elementary diagram is the buildable document for anything beyond the main power path.

## 9. PCB trace width and current-carrying capacity (IPC-2221, external layer, 10°C rise, subset)

| Trace width | 1 oz copper | 2 oz copper |
|---|---|---|
| 10 mil | ~0.6A | ~1.0A |
| 20 mil | ~1.1A | ~1.7A |
| 50 mil | ~2.0A | ~3.0A |
| 100 mil | ~3.0A | ~4.7A |

**Rule:** these are external-layer values at a conservative 10°C rise — internal-layer traces carry roughly half the current of an external trace at the same width and rise, because internal layers dissipate heat less efficiently through the board. Confirm which layer a power trace routes on before sizing it off this table, and confirm copper weight from the fab's stack-up spec, not an assumption.

**Rule (controlled impedance):** for any net where the design calls out a target impedance (differential pairs, high-speed single-ended), trace width is set from the stack-up's impedance calculation (dielectric height, dielectric constant, copper weight), not from this current table — current capacity on those nets is a secondary check, not the sizing driver.
