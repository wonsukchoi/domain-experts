# Playbook

Filled reference material: the anode-sizing worksheet, gearcase pressure-test specs by brand, compression-spec ranges by engine class, the ethanol-fuel layup decision table, and the winterization/commissioning sequence.

## 1. Anode sizing worksheet (ABYC E-2 method)

Formula: **Required anode weight (lb) = (Wetted metal area, sq ft × Current density, mA/sq ft × Immersion hours/year) ÷ (Anode capacity, Ah/lb × Utilization factor × 1000 mA/A)**

| Input | Typical value | Notes |
|---|---|---|
| Current density — painted steel | 1.5–5.0 mA/sq ft | Upper end for unpainted or heavily fouled surfaces. |
| Current density — painted aluminum | 0.2–3.0 mA/sq ft | Upper end for unpainted outdrive housings, brackish/saltwater exposure. |
| Zinc anode capacity | 368 Ah/lb | Manufacturer-rated energy content. |
| Aluminum anode capacity | ~1,150 Ah/lb | Higher capacity than zinc; sized smaller for the same protection load. |
| Utilization efficiency | 90% | Remaining 10% is unusable material lost to shape/passivation before full consumption. |
| Immersion | 8,760 hr/year (full-time) or actual in-water days × 24 | Use the boat's actual seasonal in-water period for seasonal-storage boats. |

**Worked reference (matches SKILL.md example):** 6.5 sq ft wetted aluminum, 2.5 mA/sq ft, 3,600 hr season → 0.01625 A × 3,600 hr = 58.5 Ah ÷ (368 × 0.9 = 331.2 Ah/lb) = **0.177 lb expected consumption**. Compare against actual consumption before concluding an anode is undersized — a large gap (5x or more) points at stray current or added unbonded metal, not sizing.

## 2. Hull-potential reference ranges (vs. Ag/AgCl half-cell)

| Reading | Interpretation |
|---|---|
| More positive than ≈ −0.80V | Under-protected — anode undersized, bonding continuity broken, or anode near end of life. |
| ≈ −0.80V to −1.00V | Adequately protected, typical target band for aluminum hulls/drives. |
| ≈ −0.95V to −1.10V | Adequately protected, upper end for steel. |
| More negative than ≈ −1.10V | Over-protected — risk of paint disbondment; on aluminum, risk of hydrogen embrittlement at stressed points over time. |

Take readings at multiple hull locations and with individual DC circuits isolated (breaker off, then on, one at a time) when consumption rate and potential reading disagree — a normal potential with abnormally fast anode consumption is the stray-current signature, not a sizing signature.

## 3. Gearcase pressure/vacuum test specs by brand (confirm against the specific model's service manual before quoting a repair)

| Brand/system | Pressure hold | Vacuum check | Notes |
|---|---|---|---|
| Yamaha outboard | 14 psi, hold 2 min | Not always specified; some techs add 5–10 inHg for lip-seal-specific check | Soap-solution test at prop shaft seal, driveshaft seal, and both drain/fill plug seals. |
| Generic outboard/sterndrive (representative range) | 10–15 psi | 5–10 inHg, several minutes | A pressure test alone can miss a lip seal that only leaks inward under vacuum (water intrusion) without leaking outward under pressure. |
| Segmented seal check | 3–6 psi (shift seal/O-ring only) then 16–18 psi (housing/spaghetti seal) | — | Stepping the pressure isolates which seal stage is failing rather than testing the whole case at one number. |

**Diagnostic sequence:** drain and inspect oil (milky/frothy = presumptive seal failure) → pressure test to locate the leak (soap solution at each seal/plug) → vacuum test if pressure test is inconclusive → repair only the confirmed seal, refill to spec capacity, retest before returning to service.

## 4. Compression spec ranges by engine class (cylinder-to-cylinder spread matters more than the absolute number)

| Engine class | Typical psi range | Acceptable cylinder-to-cylinder spread |
|---|---|---|
| Two-stroke outboard | 90–100 psi | Within ~10–15% of the highest-reading cylinder. |
| Four-stroke outboard | 120–160 psi | Within ~10–15% of the highest-reading cylinder. |
| Sterndrive/inboard (automotive-derived small-block) | 130–190 psi | Within ~10% of the highest-reading cylinder; wider spread on high-hour engines warrants a leak-down test to localize rings vs. valves. |

A cylinder reading 15%+ below its neighbors is the one to chase with a leak-down test regardless of whether the absolute number looks "in range" on paper.

## 5. Ethanol (E10) fuel layup decision table

| Layup duration before next start | Recommended action |
|---|---|
| Under 2–4 weeks | Run the engine periodically or leave as-is; stabilizer optional. |
| 4 weeks to 3 months | Fill tank to at least 90% (minimize headspace/condensation), add stabilizer at label dose, run engine 10–15 min to circulate treated fuel through the system. |
| Beyond 3 months (typical winter layup) | Full tank + stabilizer + circulate through the system; at commissioning, pull a fuel sample in a clear vial before starting — a visible bottom layer means phase separation occurred and the tank must be drained and refilled, not treated. |
| Any duration, tank already shows separation | No additive reverses it — drain, dispose of per local fuel-waste regulations, refill with fresh fuel. |

**Phase-separation threshold reference:** roughly 0.5% water by volume at ~60°F; the tolerance drops at lower temperatures (to roughly 0.3% around 10°F), so a boat winterized in a cold climate has less margin than the same fuel would have in a warm one.

## 6. Winterization sequence (fall layup — do not skip steps under end-of-season volume pressure)

| Step | Action | What it prevents |
|---|---|---|
| 1. Fuel treatment | Top off tank, add stabilizer, run engine to circulate. | Ethanol phase separation and varnish buildup over winter. |
| 2. Fogging | Fog cylinders/intake per engine-specific procedure. | Internal cylinder/valve corrosion during dry storage. |
| 3. Raw-water passage drain/antifreeze | Drain all raw-water passages or fill with propylene glycol (marine, non-toxic) antifreeze per the engine's specific passage map. | Freeze-cracked block, riser, or manifold — invisible until spring start-up. |
| 4. Gearcase oil change | Drain and inspect for water/metal, refill to spec capacity with fresh gear lube. | Storing the drive on contaminated oil that continues corroding seals/bearings over winter. |
| 5. Battery | Remove or maintain on a float charger; note anode/bonding status while accessible. | Dead battery at commissioning; missed opportunity to inspect anodes during the same haul-out. |
| 6. Documentation | Itemize every passage/step confirmed on a per-engine checklist, technician sign-off. | A skipped step with no record, discovered only as a spring failure with no traceable cause. |

## 7. Spring commissioning sequence

| Step | Action | What it catches |
|---|---|---|
| 1. Fuel sample check | Pull a sample in a clear vial before first start. | Phase-separated fuel from winter storage — drain/refill before it reaches the engine. |
| 2. Gearcase check | Verify oil level and condition before launch. | A seal that failed during winter storage, not just in-season. |
| 3. Anode inspection | Check condition against last season's baseline consumption rate. | Establishes this season's starting point for the consumption-rate comparison used in anode diagnostics. |
| 4. Ignition-protection spot check | Visually confirm no non-marine-rated components were introduced during winter repairs. | A well-meaning owner or a rushed shop repair using an automotive part in a fuel-vapor space. |
| 5. First-start verification | Confirm cooling flow, compression baseline if engine hours/history warrant it, and no fuel-delivery symptoms. | Catches a winter-storage-caused fault before the boat is back in the water on a customer's schedule. |
