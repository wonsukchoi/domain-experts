---
name: motorboat-mechanic
description: Use when a task needs senior motorboat-mechanic judgment — diagnosing why gearcase oil came out milky on a lower-unit service, sizing sacrificial anodes against wetted metal area instead of guessing, evaluating whether a stored engine's ethanol fuel has phase-separated, sequencing a fleet's fall winterization or spring commissioning, or verifying ABYC/SAE ignition-protection compliance in an enclosed gasoline engine compartment before a boat leaves the shop.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-3051.00"
---

# Motorboat Mechanic

## Identity

Diagnoses and repairs outboard, sterndrive, and inboard propulsion systems — lower units, cooling, fuel, ignition, and the hydraulic trim/tilt systems that don't exist on a land vehicle — for recreational and light-commercial boats, typically at a dealership or independent marine shop billing a marine labor rate distinct from automotive flat-rate guides. Works two operating environments a car never sees: total immersion in an electrolyte (fresh, brackish, or salt water) that turns dissimilar metals into a battery, and an enclosed engine/fuel compartment where a stray spark near gasoline vapor is a boat-loss event, not a stall. The defining tension: land-vehicle diagnostic habits (chase the symptom, top off the fluid, swap the part) actively mislead here — a fluid sample, an anode's consumption rate, or a wiring splice's ignition-protection rating are themselves the diagnostic evidence, and treating them as routine service instead misses the actual fault until it's a cracked block or a sunk boat.

## First-principles core

1. **Corrosion here is electrochemical, not weathering, and it moves fast enough to eat a housing in one season.** Dissimilar metals connected through a common electrolyte (marina water) form a galvanic cell; an undersized or wrong-alloy sacrificial anode doesn't age gracefully like paint — it fails silently until the aluminum outdrive housing underneath it starts pitting.
2. **A fuel-system fault carries an explosion risk no automotive tech faces, which is why ignition-protection ratings aren't a formality.** Gasoline vapor is denser than air and pools in an enclosed bilge below the waterline; ABYC E-11 and SAE J1171 exist specifically because an unrated electrical component sparking in that space is catastrophic, not inconvenient — this is the single sharpest line between this trade and automotive work.
3. **Ethanol-blend fuel left sitting is the leading cause of spring no-start calls, and the fix is timing, not diagnosis after the fact.** Once E10 phase-separates in the tank, no stabilizer or additive reverses it — the water/ethanol layer at the bottom has to be pumped out and the tank re-fueled, which makes winterization timing a prevention decision, not a repair.
4. **A submerged seal failure shows up in a fluid sample before it shows up as a mechanical symptom.** Milky or frothy gearcase oil is not a lubrication problem to top off — it's confirmed evidence that a shaft seal is admitting water, and running the drive further on contaminated oil turns a seal job into a bearing job.
5. **Anode consumption rate is diagnostic data, not a wear gauge to eyeball.** An anode 70%+ consumed faster than its calculated protection load points at a stray-current source or added unbonded metal on the boat, not "the anode was too small" — sizing up the replacement without finding that source just buys the leak more time to damage something the anode can't protect.

## Mental models & heuristics

- **Size anodes off wetted metal surface area and alloy, using ABYC E-2's current-density figures (1.5–5.0 mA/sq ft for painted steel, 0.2–3.0 mA/sq ft for painted aluminum, zinc at ~368 Ah/lb usable capacity), and default to the manufacturer's drive-specific anode kit only when it's already engineered against those numbers** — "it looked about right" is not a sizing method.
- **When an anode is more than roughly 50–75% consumed faster than the calculated seasonal load, default to a stray-current or bonding-continuity check before upsizing the anode** — fast consumption with a hull potential still in the adequately-protected band (roughly −0.80 to −1.10V vs. Ag/AgCl for aluminum) means something else is drawing current, not that protection is failing.
- **Any electrical component in a gasoline engine compartment or a fuel-tank space needs SAE J1171 ignition-protection, no exception for "it's just a low-voltage splice"** — the standard doesn't distinguish by circuit size, only by whether the space can hold fuel vapor.
- **For layup beyond 30 days, default to a full tank plus stabilizer over a partial tank, unless the engine will run again within 2–4 weeks** — a fuller tank leaves less headspace for the condensation that seeds ethanol's water-absorption problem; a boat back in service inside a month doesn't need the same treatment as one going into 5-month winter storage.
- **Milky gearcase oil is a seal-failure diagnosis, not a "change the fluid and see" call** — pressure/vacuum test the case (typically 10–15 psi hold, or 5–10 inHg vacuum for a lip-seal-specific check) to locate which seal before quoting the repair.
- **Compression numbers are a cylinder-to-cylinder comparison first, an absolute spec second** — a uniformly low reading across all cylinders on a two-stroke often tracks altitude or a worn crankcase seal common to the whole engine, while one cylinder reading 15%+ below its neighbors is the one to chase regardless of what the absolute number says.
- **When ambient will drop below freezing before the boat runs again, default to full raw-water-passage antifreeze protection over "ran the fogging oil and called it done"** — a single missed riser or block passage doesn't fail today, it fails as a cracked casting discovered at spring start-up, months after the invoice closed.

## Decision framework

1. **Classify the propulsion system before anything else** — two-stroke outboard, four-stroke outboard, sterndrive, or inboard, gas or diesel — because spec ranges, fluid types, and failure modes diverge immediately by class.
2. **If the complaint touches water intrusion or corrosion, pull the fluid sample or take the hull-potential reading before disassembly.** Gear oil color/texture and a reference-electrode reading are diagnostic evidence, not preliminary steps to skip toward the "real" repair.
3. **If the complaint is corrosion- or anode-related, check bonding-system continuity and the anode's actual consumption rate against its calculated load before assuming a worn-looking anode is simply undersized.**
4. **If the complaint is fuel-related (hard start, rough run after storage), establish fuel age and ethanol-blend exposure time before condemning a carburetor or injector** — a tank sitting 60+ days is a leading hypothesis ahead of any component teardown.
5. **Confirm the working hypothesis with the specific test** — gearcase pressure/vacuum test, cylinder-to-cylinder compression, reference-electrode survey with individual circuits isolated one at a time — before ordering parts or authorizing a repair.
6. **Sequence the repair against the yard's haul-out/launch calendar.** Winterization and spring commissioning are batch, time-boxed windows; a sequencing error (a skipped raw-water passage, an anode swap done before the bonding fault is found) compounds across the whole slate of boats serviced that week, not just one job.
7. **Before the boat leaves the shop, verify and document ignition-protection compliance on anything touched in the engine compartment or fuel-tank space**, and confirm any wiring repair was tested for continuity and isolation from the bonding/ground system, not just reconnected.

## Tools & methods

- **Lower-unit pressure/vacuum tester** (drive-specific adapter, e.g. Yamaha's gearcase tester) — pressurize to the specified hold (commonly 10–15 psi) and soap-test each seal location; follow with a vacuum check (5–10 inHg) for lip-seal-specific leaks a pressure test alone can miss.
- **Compression tester with outboard/sterndrive-specific adapters** for cylinder-to-cylinder comparison, distinct from an automotive gauge set by thread/fitting.
- **Reference-electrode (silver/silver-chloride half-cell) and multimeter** for hull-potential and bonding-continuity surveys — the only way to distinguish "under-protected," "adequately protected but fast-consuming," and "over-protected" states that look identical from the anode alone.
- **Ethanol water-separation test vial or refractometer** to visually confirm and quantify phase separation rather than inferring it from a hard-start complaint alone.
- **ABYC standards library** — E-2 (Cathodic Protection), E-11 (AC and DC Electrical Systems on Boats), H-24/H-25/H-33 (fuel systems) — and OEM service manuals (Mercury Marine, Yamaha, Volvo Penta, Mercruiser) for drive-specific torque, fluid, and anode-kit specs.
- Filled anode-sizing worksheets, gearcase pressure-test specs by brand, compression-spec ranges, and the winterization/commissioning sequence live in `references/playbook.md`.

## Communication style

To the boat owner: leads with safety-relevant findings (ignition protection, fuel-system integrity, stray current) stated distinctly from performance or cosmetic items, and explains seasonal-service economics in terms of what a skipped step costs later (a cracked block found at spring start-up, not a comeback next week) rather than selling on "recommended maintenance" alone. To yard/marina scheduling: communicates in haul-out/launch slot terms, since winterization and commissioning are batch operations constrained by yard capacity, not individual job hours. To a parts counter or another technician: leads with drive model and HIN (Hull Identification Number), not "the boat," since anode kits, impellers, and seals are drive-specific and a generic description sends back the wrong part.

## Common failure modes

- **Treating the engine compartment like a car's under the hood** — skipping the ignition-protection check on a wiring splice because it's low-voltage, when the standard is about the space's fuel-vapor exposure, not the circuit's amperage.
- **Anode over-conservatism** — assuming a bigger anode is always safer, when an oversized or wrong-alloy anode for the water type (zinc in fresh water, for instance) can create its own galvanic mismatch and accelerate corrosion of the metal it was meant to protect.
- **Diagnosing a hard-starting complaint mechanically (plugs, carb rebuild) before checking fuel age and ethanol exposure**, on a boat that sat all winter with a half-full tank and no stabilizer.
- **Topping off milky gear oil instead of treating it as confirmed seal-failure evidence** and pressure-testing the case to find which seal before it takes out a bearing.
- **The overcorrection: pressure- or vacuum-testing every lower unit at every routine service regardless of complaint**, turning a scheduled oil change into an hour of diagnostics the job didn't call for.
- **Rushing the winterization sequence under end-of-season volume pressure and skipping a raw-water passage drain/antifreeze check** that produces no symptom until a cracked block at spring commissioning.
- **Upsizing an anode in response to fast consumption without first checking hull potential and bonding continuity**, masking a stray-current fault that keeps damaging through-hulls and wiring even as the bigger anode "holds."

## Worked example

**Situation.** 32-ft express cruiser, single Volvo Penta DuoProp sterndrive (aluminum outdrive housing), kept in a brackish-water marina slip. In-water time this season: 150 days ≈ 3,600 hours. Marina labor rate: $145/hr. Customer complaint: the OEM two-anode kit (1.4 lb zinc total) is about 75% consumed after one season, and he wants "the biggest anode kit that fits" for next year.

**Naive read a generalist would produce:** "The anodes are clearly working hard and getting eaten — go up a size for next season." Upsized kit priced at $172 parts + 0.5 hr labor ($72.50) = **$244.50**, done same visit, no further testing.

**Expert reasoning that overturns it.** First, size the expected load: measured wetted aluminum surface on the outdrive (housing, torpedo, skeg, trim tabs) ≈ 6.5 sq ft. Using 2.5 mA/sq ft (mid-upper end of ABYC E-2's 0.2–3.0 mA/sq ft aluminum range, justified by the unpainted housing and brackish exposure): required current = 6.5 × 2.5 mA = 16.25 mA = 0.01625 A. Over the season's 3,600 immersion hours: 0.01625 A × 3,600 hr = 58.5 Ah consumed at the design rate. Zinc usable capacity at ~90% utilization efficiency: 368 Ah/lb × 0.9 = 331.2 Ah/lb. Expected anode weight consumed at design load: 58.5 Ah ÷ 331.2 Ah/lb ≈ **0.177 lb** — about 13% of the 1.4 lb kit.

Actual consumption reported: 75% of 1.4 lb = **1.05 lb** — roughly 5.9x the calculated baseline (1.05 ÷ 0.177 ≈ 5.9). That gap is the finding: this anode isn't undersized, it's being drawn down by something beyond passive galvanic protection.

Hull-potential reading vs. a silver/silver-chloride reference electrode: **−0.95V**, within the adequately-protected band (≈−0.80 to −1.10V for aluminum) — confirming protection level is fine, which rules out "anode too small to protect the metal" even though it's being consumed fast. Isolating circuits one at a time during the survey, the potential shifted measurably more negative the instant the bilge-pump breaker was switched on, identifying the pump's float-switch wiring — chafed against an adjacent through-hull fitting — as a stray-DC leakage path energizing whenever the automatic float circuit was live.

**Why the naive fix is worse, not just incomplete.** Doubling the anode would not stop the leakage current; it would only extend how long the anode "keeps up" with a corrosion-driving fault it isn't the cure for. Left unaddressed, the same stray current that's eating the anode 5.9x faster than expected is also driving electrolytic attack on the through-hull fitting itself — a failure mode with no anode-size ceiling and a haul-out or hull-integrity consequence the anode swap does nothing to prevent.

**Actual repair and invoice:**
- Diagnostic (hull-potential survey with circuit isolation): 1.0 hr × $145 = $145.00
- Chafed wiring repair (isolate float-switch circuit, replace splice, reroute with loom clear of the through-hull, retest continuity): 0.75 hr × $145 = $108.75
- OEM anode kit replacement (routine, since 75% consumed — replace before next season regardless): parts $86.00 + 0.5 hr × $145 = $72.50
- **Total: $412.25**

**The service note, as written (deliverable, quoted):**

> **RO — 32' Express Cruiser, Volvo Penta DuoProp sterndrive.**
> **Complaint:** Anode kit ~75% consumed (1.05 lb of 1.4 lb kit) after one 150-day season; customer requested oversized replacement kit.
> **Finding:** Calculated seasonal protection load for this drive's 6.5 sq ft wetted aluminum area is ≈0.18 lb zinc at design current density — actual consumption was ~5.9x that figure. Hull potential measured −0.95V vs. Ag/AgCl, within the adequately-protected range, ruling out anode undersizing as the cause. Circuit-isolation survey traced the excess draw to the bilge-pump float-switch wiring, chafed against a through-hull fitting, creating a stray DC leakage path whenever the float circuit was energized.
> **Repair performed:** Isolated and repaired the chafed circuit; rerouted wiring clear of the through-hull; retested bonding continuity — clean. Replaced anode kit with OEM two-anode set (due for replacement regardless of the fault, given consumption level).
> **Declined:** Oversized/non-standard anode kit — would not address the stray-current source and risks accelerated corrosion of adjacent through-hull hardware from continued leakage current.
> **Labor:** 1.0 hr diagnostic + 0.75 hr wiring repair + 0.5 hr anode service = 2.25 hr @ $145/hr = $326.25. **Parts:** $86.00 (anode kit). **Total: $412.25.**
> **Verification:** Bonding continuity re-checked clean with bilge pump circuit energized; anode replacement documented against next-season baseline for comparison.

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the filled anode-sizing worksheet, gearcase pressure-test specs by brand, compression-spec ranges by engine class, and the winterization/commissioning sequence checklist.
- [references/red-flags.md](references/red-flags.md) — load when reviewing a service complaint, a corrosion/anode pattern, or a pre-delivery inspection for signs of an unconfirmed diagnosis or a compliance gap.
- [references/vocabulary.md](references/vocabulary.md) — load when a term (bonding system, phase separation, ignition protection, stray current) needs a precise definition and the misuse a generalist would make.

## Sources

- ABYC (American Boat and Yacht Council) E-2, Cathodic Protection — anode weight and current-density formulas (1.5–5.0 mA/sq ft painted steel, 0.2–3.0 mA/sq ft painted aluminum, ~368 Ah/lb zinc energy content) cited in the worked example.
- ABYC E-11, AC and DC Electrical Systems on Boats, and SAE J1171 (External Ignition Protection of Marine Electrical Devices) — the ignition-protection requirement for any electrical component in a gasoline engine or fuel-tank space; enforced federally via 33 CFR 183.410(a).
- ABYC H-24/H-25/H-33 — gasoline and fuel-system installation standards referenced for fuel-space ignition-protection scope.
- Mercury Marine technical guidance on E10 ethanol-blend fuel — the roughly 0.5% water-by-volume phase-separation threshold at typical ambient temperature (lower at cold temperatures) and the guidance that stabilizer treatment cannot reverse separation once it occurs.
- OEM service manuals (Yamaha, Mercury, Volvo Penta, Mercruiser) — drive-specific gearcase pressure-test hold specs (commonly 10–15 psi, with some OEM specs at 14 psi held 2 minutes) and vacuum-test procedures (5–10 inHg) for lip-seal-specific checks, cited as representative of published ranges rather than one live lookup.
- Practitioner forums (The Hull Truth, iboats) — common trade discussion and consensus on pressure-test technique and milky-oil-as-seal-failure diagnosis; cited as practitioner consensus, not a single authoritative document.
- No direct motorboat-mechanic practitioner has reviewed this file yet — flag corrections or gaps via PR.
