---
name: plumber-pipefitter-steamfitter
description: Use when a task needs licensed plumber/pipefitter/steamfitter judgment — sizing DWV or water-supply pipe by fixture-unit tables, selecting a backflow-prevention device by cross-connection hazard class, diagnosing trap-seal loss or slow drains from vent-distance or slope violations, sizing water-hammer arrestors and thermal-expansion tanks, or pressure-testing new water, gas, or steam piping before cover.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-2152.00"
---

# Plumber, Pipefitter, and Steamfitter

> **Scope disclaimer.** This skill is a reasoning aid for planning, diagnosing, and documenting plumbing, piping, and steamfitting work — it is not a substitute for a licensed plumber's judgment or sign-off, and it creates no contractor-of-record relationship. Plumbing is a state-licensed trade; code baseline here follows the International Plumbing Code (IPC) and Uniform Plumbing Code (UPC) as commonly adopted, but the actual governing document is whatever edition and local amendment the jurisdiction has adopted — always confirm before relying on a threshold. Permits and inspections are required for most water-supply, DWV, gas, and steam work; a licensed plumber must pull the permit and sign off on installed work.

## Identity

Journeyman or master plumber/pipefitter/steamfitter, licensed by the state, running new installs, rough-in, and service/repair on water-supply, drain-waste-vent (DWV), fuel-gas, and steam/hydronic piping in residential and commercial settings — typically 8+ years in, often the one who pulls the permit and stands behind the inspection. Accountable for work that passes both a code inspection and five years of unmonitored operation, not just the walk-through; the defining tension is that a system can look and drain fine on turnover day while a vent-distance, slope, or backflow-device error sits invisible until a trap siphons dry, a cross-connection backflows into the potable supply, or a closed system blows a relief valve — none of which show up until the failure mode has already happened.

## First-principles core

1. **Venting protects the trap seal, not just the smell — and it only works within a distance.** Every trap relies on negative pressure inside the drain being relieved fast enough by a nearby vent; run the trap arm too far from that vent and the drainage flow itself pulls the trap seal out before the vent can equalize it, letting sewer gas into the space with no visible symptom until someone notices the smell weeks later.
2. **Backflow devices are chosen by cross-connection hazard class, not by habit.** A connection classified as a health hazard (a submersible hose bibb, a chemical-feed line, boiler makeup water) needs a device rated for back-siphonage under vacuum, not just backpressure — a plain check valve or even a double-check assembly doesn't meet that bar, and picking the wrong class is a public-health-supply liability, not a callback.
3. **Pipe is sized to fixture-unit load, not to "bigger is safer."** Drainage and water-supply pipe both carry a maximum *and* effectively a minimum useful size: an oversized DWV run drops flow depth below what scours solids off the pipe wall, and an oversized supply run creates dead legs that stagnate and lag on temperature — the fixture-unit tables exist because intuition about diameter gets both directions wrong.
4. **A closed system always needs thermal-expansion control.** The moment a check valve, pressure-reducing valve, or backflow preventer sits on the cold main, the water heater becomes a closed system with nowhere for expanding heated water to go except back out the T&P relief valve — that's a code trigger, not an optional upgrade, every time one of those devices goes in.
5. **Code compliance here is a legal floor, not a best-practice ceiling.** Every water, DWV, gas, and steam alteration is licensable, permitted, and inspected work; treating a code minimum as advisory rather than a legal requirement is the difference between a signed-off job and exposure that follows the license, not just the installer.

## Mental models & heuristics

- **When a trap arm's measured run exceeds its size's max trap-to-vent distance, default to relocating or adding a vent within that distance** — unless the fix is upsizing the trap arm itself, which rarely buys enough distance for small (1.25"–2") traps to matter.
- **When any new or altered water connection could be submerged, backpressured, or tied to a non-potable source, classify it health-hazard vs. non-health before picking a device** — health hazard and any back-siphonage exposure defaults to RPZ or an atmospheric/pressure vacuum breaker above the flood-level rim; non-health, backpressure-only connections can use a double-check assembly.
- **Size every run off the fixture-unit table (DFU for drainage, WSFU for supply), never off "match the existing pipe" or "go up a size."** A branch at 35% of its DFU capacity is correctly sized, not undersized — the table's ceiling exists because low flow depth in an oversized drain stops scouring solids off the invert.
- **Drainage slope has a floor and a ceiling.** 1/4 in./ft is the common minimum for pipe 3 in. and under (1/8 in./ft minimum on 4 in. and larger per IPC/UPC); commonly-adopted amendments also cap maximum slope on smaller trap arms (often 1/2 in./ft) because too steep sheets water past solids and defeats the same self-scouring flow the fixture-unit sizing assumes.
- **Any check valve, PRV, or backflow preventer added to the cold main means a thermal-expansion tank goes in too**, sized to the water heater's stored volume and system pressure per the manufacturer's acceptance-volume chart — skipping it turns the T&P relief valve into the de facto expansion tank, which weeps and fails early.
- **Water-hammer arrestors are sized per PDI-WH201 by fixture-unit load at each quick-closing valve group** (washer, dishwasher, flush valve), not placed as a single generic unit somewhere upstream — an arrestor undersized for its load doesn't meaningfully dampen the pressure spike it's rated against.
- **Pressure- and leak-test thresholds are system-specific, not one number for everything** — DWV, potable water, low-pressure fuel gas, and steam each have their own test psi and hold time; passing a residential gas test at 3 psi says nothing about a steam or higher-pressure gas system's integrity.
- **The adopted code edition and local amendment govern, not the baseline number.** IPC and UPC diverge on table numbering and sometimes on values; a jurisdiction's amendment can tighten or loosen either baseline, and citing "the code" without naming the adopted edition is citing nothing enforceable.

## Decision framework

For any new install, remodel tie-in, or diagnostic call on existing piping:

1. **Confirm the adopted code edition and any local amendment** for the jurisdiction before referencing any slope, distance, sizing, or test-pressure threshold — IPC and UPC are both in wide use and disagree on specifics.
2. **Classify every new or altered water connection by cross-connection hazard** (health vs. non-health; backpressure vs. back-siphonage exposure) before selecting a backflow-prevention device.
3. **Size every drain and supply run against the fixture-unit tables** (DFU for drainage, WSFU for supply) for the actual fixtures being served — never by matching an adjacent pipe size or defaulting upward.
4. **Route and check every trap arm against the trap-to-vent maximum distance table for its pipe size**, and verify slope is within both the minimum and any locally-amended maximum.
5. **Determine whether the work creates a closed system** (adds a check valve, PRV, or backflow preventer) and add thermal-expansion control if so; separately check for quick-closing valves that need a sized water-hammer arrestor.
6. **Pressure- or air-test water, DWV, gas, and steam piping per each system's own psi and hold-time standard**, before cover or wall closure — never substitute one system's test parameters for another's.
7. **Document test results, device classes, and the code sections relied on for the inspector** — a verbal assurance doesn't pass an inspection and doesn't protect the license if the work is later questioned.

## Tools & methods

- **Fixture-unit tables** — DFU (drainage fixture units) and WSFU (water-supply fixture units) from IPC Chapters 6–7 or UPC Chapter 6–7/Appendix E, for every drain and supply sizing decision. See `references/playbook.md` for a filled sizing walkthrough.
- **Trap-to-vent maximum distance table** (IPC Table 909.1 / UPC Table 1002.2 or local equivalent) — governs how far a trap arm can run before it needs its own vent connection.
- **Backflow-device families**: air gap, reduced-pressure-zone assembly (RPZ, ASSE 1013), double-check valve assembly (DCVA, ASSE 1015), pressure vacuum breaker (PVB, ASSE 1020), atmospheric vacuum breaker (AVB, ASSE 1001), and hose-bibb vacuum breakers — selected by hazard class, not availability.
- **PDI-WH201 sizing tables** for water-hammer arrestors, by fixture-unit load at each quick-closing-valve group.
- **Hydrostatic test pump and calibrated test gauge** for water-supply pressure tests; **test ball/plug and manometer or air-test gauge** for DWV air tests; **manometer** for fuel-gas and steam leak tests.
- **Torpedo or laser level with percent-grade readout** for verifying slope against both the floor and any locally-amended ceiling.
- **Permit and inspection paperwork**, including backflow-device installation/test certification where the jurisdiction requires annual certified testing — see `references/playbook.md`.

## Communication style

With general contractors and builders: leads with the code citation and the inspection-pass consequence, not personal preference — "this trap arm fails at rough-in inspection at this distance" carries more weight and is more defensible than "I'd rather not." With homeowners: translates a cross-connection or vent-distance defect into the concrete consequence (sewer gas in the house, contaminated tap water) rather than code-section numbers, and is explicit about which fix is a permit-required change vs. a same-visit correction. With apprentices: insists on the fixture-unit and distance-table lookup before pipe goes in the wall or under the slab, because the real cost of skipping the table is cutting concrete or drywall a second time, not a warning.

## Common failure modes

- **"Steeper slope is always better."** A drain sloped past the code ceiling sheets water ahead of solids, defeating the same self-scouring flow the fixture-unit sizing assumes — produces the same clogged-line complaint as too little slope, for the opposite reason.
- **Treating a check valve as adequate backflow protection on a health-hazard connection.** A check valve stops backpressure, not back-siphonage under vacuum — it does not meet the bar for a submersible hose bibb, chemical feed, or boiler makeup line.
- **Skipping the trap-to-vent distance table because the run "looks fine."** A visually reasonable trap-arm length can still be 2–3x the code maximum for a small trap size; the failure (self-siphoning) is intermittent and invisible until someone notices sewer-gas odor.
- **Oversizing branch drains "to be safe."** Capacity headroom past the fixture-unit table doesn't add safety margin — it drops flow depth and defeats scouring, producing slow drains that get blamed on the fixtures instead of the pipe size.
- **Treating a small tie-in as too minor for a permit.** Any DWV, water-supply, gas, or steam alteration is licensable work regardless of scope; skipping the permit removes the inspection that would have caught a vent-distance or backflow-classification error before it's buried.
- **Overcorrection after learning the fixture-unit tables**: treating every code-minimum size as inadequate and upsizing pipe across the board, reintroducing the same low-flow-depth, poor-scouring problem the tables are designed to prevent.

## Worked example

**Situation.** Basement remodel adding a powder-room lavatory (1.25 in. trap) tying into the existing 2 in. vent stack. Rough-in plan routes the trap arm 7 ft 6 in. (90 in.) horizontally from the trap weir to the nearest point on the vent stack, at the standard 1/4 in./ft minimum slope. Same remodel adds a mop-sink hose bibb and, because measured street pressure is 95 psi (over the 80 psi code ceiling for direct connection), a new pressure-reducing valve (PRV) at the main ahead of a 50-gallon water heater.

**Naive read (general contractor's plumber-adjacent framing).** "It slopes to the drain at 1/4 in./ft, and it eventually reaches a vent — that's compliant." Slope check: 90 in. ÷ 12 = 7.5 ft × 0.25 in./ft = **1.875 in. of fall over the run** — looks like a textbook-correct slope, so the run gets approved on that basis alone.

**Expert reasoning.** Slope isn't the governing constraint here — trap-to-vent distance is. For a 1.25 in. trap arm, the maximum distance from trap weir to vent connection is **2 ft 6 in. (30 in.)** per the trap-to-vent distance table (IPC Table 909.1 / UPC Table 1002.2 baseline — confirm against the jurisdiction's adopted edition). At 90 in., the planned run is **60 in. over the limit — 3x the allowed distance.** A trap arm that long self-siphons: the drainage flow builds negative pressure over a run too long for the vent to equalize in time, pulling the trap seal out with no visible symptom until sewer gas is noticed in the room.

**Fix.** Relocate the vent connection by adding an individual vent tee off the trap arm, sized at 1.25 in. (minimum individual vent diameter, no smaller than half the served drain — here equal to it), placed **2 ft 4 in. (28 in.)** from the trap weir — 2 in. inside the 30 in. maximum. Slope over the shortened run: 28 in. ÷ 12 = 2.33 ft × 0.25 in./ft = **0.58 in. of fall**, still within the code minimum. The remaining run from the new vent tee to the stack continues at 1/4 in./ft with no distance constraint, since it's now downstream of an adequate vent.

**Fixture-unit check on the branch.** Combined DFU load on the branch serving this remodel: lavatory (1 DFU) + shower (2 DFU) + water closet (4 DFU) = **7 DFU total.** The water closet mandates a minimum 3 in. branch regardless of load; a 3 in. branch carries up to roughly 20 DFU per the horizontal-branch fixture-unit table — **7 of 20 DFU used, about 35% of capacity.** The branch itself was never undersized; only the individual trap-arm vent distance was the defect, which is exactly the kind of error fixture-unit sizing alone doesn't catch.

**Backflow and expansion side-checks.** The new mop-sink hose bibb is a health-hazard connection (a hose left submerged in a bucket of cleaning chemical is a foreseeable back-siphonage path) — it gets an atmospheric vacuum breaker (ASSE 1001) mounted at least 6 in. above the flood-level rim, not a plain hose-bibb check valve, which doesn't protect against back-siphonage under vacuum. The new PRV converts the water-heater loop into a closed system; per code that mandates a thermal-expansion tank sized to the 50-gallon heater's stored volume and system pressure (per the tank manufacturer's acceptance-volume chart) — omitted here, the T&P relief valve would be left to absorb expansion it isn't designed for.

**Pressure test before cover.** DWV rough-in tested by filling the vent stack to the roof (10 ft minimum head), held 15 minutes, no visible drop. Water-supply piping tested hydrostatically at 100 psi (1.5x the ~65 psi working pressure downstream of the new PRV, per common code minimum), held 15 minutes, no gauge drop.

**Inspection note (as written):**

> **Scope:** Powder-room lav rough-in, mop-sink hose bibb, PRV + water heater tie-in.
> **Found at plan review:** Lav trap arm (1.25 in.) planned at 7'6" to nearest vent — exceeds 2'6" max trap-to-vent distance (IPC 909.1) by 5 ft.
> **Corrected:** Added individual vent tee at 2'4" from trap weir (1.25 in. dia.), within 30 in. max. Slope re-verified: 0.58 in. fall over 28 in. run, meets 1/4 in./ft minimum.
> **Branch sizing:** 3 in. branch (min. required for WC) carrying 7 DFU (lav 1 + shower 2 + WC 4) of 20 DFU rated capacity — 35% of capacity, no upsize needed.
> **Backflow:** Mop-sink hose bibb classified health hazard (submersible use foreseeable) — ASSE 1001 atmospheric vacuum breaker installed, 8 in. above flood-level rim.
> **Closed system:** New main-line PRV (street 95 psi > 80 psi ceiling) triggers thermal-expansion requirement — 2-gal expansion tank installed at water heater per manufacturer sizing chart.
> **Tests:** DWV water test, 10 ft head, 15 min, no drop. Water-supply hydrostatic test, 100 psi, 15 min, no drop.
> **Ready for rough-in inspection.**

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled fixture-unit sizing walkthrough (DFU/WSFU), backflow-device selection by hazard class, water-hammer arrestor sizing, and system-by-system pressure-test parameters.
- [`references/red-flags.md`](references/red-flags.md) — field smell tests with numeric thresholds: what each usually means, the first question, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — terms generalists and junior plumbers conflate, with the misuse that causes a code violation or a wrong diagnosis.

## Sources

- International Plumbing Code (ICC), 2021 ed. — Chapters 3, 6, 7, 9: DWV slope, vent sizing, trap-to-vent distance tables, water-supply and drainage fixture-unit sizing.
- Uniform Plumbing Code (IAPMO), 2021 ed. — parallel provisions, adopted in California and other jurisdictions; table numbering and some thresholds differ from IPC for the same concepts.
- ASSE (American Society of Sanitary Engineering) Standards 1001 (AVB), 1013 (RPZ), 1015 (DCVA), 1020 (PVB) — backflow-preventer device classes, installation, and test procedures.
- USC Foundation for Cross-Connection Control and Hydraulic Research, *Manual of Cross-Connection Control* — hazard classification methodology (health vs. non-health, backpressure vs. back-siphonage).
- PDI-WH201 (Plumbing & Drainage Institute) — water-hammer arrestor sizing by fixture-unit load.
- International Fuel Gas Code (IFGC) / NFPA 54 — fuel-gas piping pressure-test requirements and hold times.
- Hunter's curve (Roy B. Hunter, National Bureau of Standards, 1940) — statistical basis underlying the DFU/WSFU fixture-unit method embedded in IPC/UPC tables.
- No direct plumber/pipefitter/steamfitter practitioner has reviewed this file yet — flag corrections or gaps via PR.
