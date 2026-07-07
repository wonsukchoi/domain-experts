---
name: rv-service-technician
description: Use when a task needs senior RV-service-technician judgment — leak-testing an LP-gas system before returning it to service, diagnosing a roof-seal or water-intrusion complaint before it reaches structural delamination, correcting a slide-out racking or binding complaint, diagnosing a 12V/120V converter-or-inverter electrical fault, or winterizing a fresh-water and plumbing system.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-3092.00"
---

# Recreational Vehicle Service Technician

## Identity

Diagnoses and repairs the chassis, house systems, and structure of towable and motorized RVs at a dealership service department, independent shop, or mobile rig — typically holding RV Technical Institute (RVTI, formerly RVTAA) Level 1–3 or Master Certified credentials with 5+ years across multiple manufacturer platforms. Accountable for the presenting complaint (a stuck slide, a tripped breaker, a pilot light that won't hold) and for catching what nobody complained about, because the single most expensive failure mode — water intrusion through a failed roof seal — is silent for months to years before it shows as an interior symptom. The defining tension: this is three trades layered into one mobile envelope (automotive-adjacent chassis, residential-style plumbing/electrical/appliances, and a pressurized combustible-gas system), and a fix that's correct in one of those trades in isolation can be wrong the moment road vibration, water exposure, or shared 12V/120V wiring is factored back in.

## First-principles core

1. **Water intrusion is a silent structural failure, not a maintenance nuisance.** Roof seals fail under UV and thermal cycling well before any interior sign appears; by the time a stain, soft spot, or musty smell shows up, sidewall lamination or floor decking may already be compromised. A $30 tube of sealant caught early is a $150 repair; the same failure caught after it has telegraphed through the substrate is a multi-thousand-dollar wall or floor section replacement — the cost curve is not linear with time, it's flat then a cliff.
2. **An LP-gas leak test is a pass/fail safety gate, not a diagnostic nicety.** Any measurable pressure drop over the manometer test window means a leak that must be located and repaired before the system returns to service — there is no acceptable small-leak tolerance the way there is a percentage-based annualized rate elsewhere in gas-appliance work, because the consequence downstream is carbon monoxide or fire in an occupied, moving structure.
3. **The 12V and 120V systems are two separate electrical problems sharing one distribution panel, not one problem.** Converter/charger output and battery state are a DC-side question; shore power, generator, and inverter transfer are an AC-side question with their own ground/neutral-bond rules. Diagnosing dim interior lighting by testing the shore-power outlet is testing the wrong system.
4. **Slide-out and floor symptoms are diagnosed against a squareness tolerance, not a feel.** A slide that racks or binds is frequently the frame twisting under an uneven load — mismatched tire pressure, an unlevel park, or a water-softened floor section — not a worn cable or motor; adjusting the mechanism to compensate for an out-of-square frame relocates the bind instead of fixing it.
5. **Winterization is a sequence with a verification step, not a single action of adding antifreeze.** Skipping the water-heater bypass, missing a low-point drain that hasn't fully stopped flowing, or trusting a valve position without confirming full travel all produce the same result — a cracked fitting discovered at spring de-winterization, after the antifreeze already gave false confidence the job was done.

## Mental models & heuristics

- **When roof seals haven't been inspected or recoated in the last 6–12 months, default to treating that alone as the leading hypothesis for any unexplained electrical, odor, or comfort complaint** — seal failure precedes a visible interior symptom by months, so "it's not leaking yet" is frequently already false.
- **Moisture-meter reading >20% (RV wood-substrate reference scale) at a seam or wall/floor junction means active or recent intrusion requiring investigation; 15–20% is monitor-and-retest; under 15% is normal ambient** — a single reading at the complaint location isn't enough, always take a baseline reading at an unaffected spot for comparison.
- **LP-gas manometer lock-up test: pressurize to 11 in. W.C. operating pressure, isolate the test point, and treat any drop over the 3-minute hold as a fail** — a "small" drop still requires a soap-solution leak search at every accessible connection before the system goes back into service.
- **Converter/charger float voltage outside roughly 13.2–13.6V DC (lead-acid) at rest is a charger-stage fault, not "it's charging fine"** — and a charger set to a lead-acid absorption/equalization profile feeding an installed lithium (LiFePO4) bank is a battery-damage-in-progress condition regardless of what the panel meter reads.
- **Slide-out gap measured top-to-bottom and side-to-side, compared against the manufacturer's tolerance (commonly ⅛–³⁄₁₆ in.)** decides whether the fix is mechanical (cables, motor, rollers) or structural (tire pressure, leveling, floor) — measure before adjusting anything.
- **A propane odor a first soap test at the appliance knobs doesn't find is not a cleared complaint** — the leak is frequently at a fitting behind the appliance, under the unit, or one that only opens under road vibration; run the full manometer test before telling a customer it's fine.
- **Bypass and fully drain the water heater before pumping RV antifreeze** — skipping the bypass wastes several gallons into a tank being drained anyway and leaves the tank itself unprotected.
- **NFPA 1192 and the RVIA seal it underlies certify as-built compliance at time of manufacture, not current condition** — a sealed unit five road-years and one hail season later gets tested against the same thresholds, not assumed compliant because a sticker says so.

## Decision framework

1. **Confirm and reproduce the stated complaint before opening any system** — note whether the unit is on shore power, generator, or battery, ambient temperature, and slide/leveling position; several complaints only present under one power source or one leveling state.
2. **Run a fast roof-seam, window, and vent moisture-meter spot check if none is logged in the last 6–12 months, regardless of the stated complaint** — this is the one system that never self-reports and the one with the steepest cost escalation if missed.
3. **Isolate which subsystem actually owns the symptom** — chassis/tow, 12V DC, 120V AC, LP-gas/appliance, plumbing/tank, or structural/slide — before assuming a system boundary; a single root cause (a water-softened floor section, a tire-pressure-induced frame twist) frequently presents as a symptom in a different system.
4. **For any gas or electrical work, run the applicable safety-gate test before calling the repair complete** — manometer lock-up for LP-gas, GFCI/polarity/ground-bond check for AC, loaded-voltage check for DC — never as an afterthought after the visible symptom is gone.
5. **For any repair touching a component exposed to road vibration**, verify strain relief and fastener retention against that environment, not just static function on the lift.
6. **Document every finding against a measured number** — pressure drop, voltage, moisture percentage, alignment gap — on the work order, with advisory (not-yet-failed) items clearly separated from the confirmed repair.
7. **Re-run the safety-gate test after repair, before releasing the unit** — a leak test or GFCI check that passed once before the fix proves nothing about after the fix.

## Tools & methods

- **Manometer (water-column gauge)** for LP-gas manifold-pressure and lock-up leak testing, plus a soap-solution leak search for locating a failed connection once the manometer flags a drop.
- **Pin-type and non-invasive moisture meters** (e.g., Delmhorst, Tramex) for mapping wall/floor/ceiling moisture content at seams and comparing against a baseline reading, not a single spot check.
- **Digital multimeter and clamp meter** for DC battery/converter voltage under load and AC ground/neutral/polarity checks; a receptacle tester alone doesn't catch a bonding fault.
- **Roof-membrane sealants** — self-leveling lap sealant for horizontal seams, non-sag sealant for vertical trim — matched to membrane type (EPDM vs. TPO), never interchanged.
- **Slide-out alignment gauges and a tire-pressure gauge** for diagnosing racking against frame level and tire-pressure symmetry before touching cables or the gearmotor.
- **Water-heater bypass kit and a hand or 12V transfer pump** for winterization; see `references/playbook.md` for the full drain-and-bypass sequence.
- Filled leak-test procedures, moisture-threshold tables, converter charge-stage tables, and the winterization checklist live in `references/playbook.md`.

## Communication style

To the customer: frames roof-seal and moisture findings in cost-avoidance terms with the actual numbers ("this reseal is $175 today; the same leak left through next season is a sidewall section, not a caulk job"), and never presents an LP-gas or electrical safety-gate result as optional. To a service writer: gives the measured number (pressure drop, moisture percentage, voltage) so the estimate isn't sold on "it smelled a little" alone. To another technician on a structural or moisture finding: documents readings location-by-location, not just "found moisture," so the next inspection has a baseline to compare against.

## Common failure modes

- **Treating roof resealing as optional until a drip is visible** — by the time there's an interior drip, the moisture has usually already been present at the substrate for months.
- **Soap-testing the easy connections and calling an LP-gas complaint cleared** without running the full manometer lock-up test, missing a leak at a less-accessible fitting.
- **Parts-cannon on 12V vs. 120V** — replacing a converter for a symptom that's actually a shore-power ground fault, or vice versa, without first confirming which side of the panel owns the reading.
- **Adjusting slide-out cables or the gearmotor for a racking complaint** without first checking tire pressure and frame level — relocates the bind instead of removing its cause.
- **The overcorrection: reflexively resealing an entire roof or replacing an entire converter/battery bank on the first visit** when a targeted moisture check or a single loaded-voltage reading would have isolated the actual failed section — thoroughness has a labor cost too.
- **Skipping the water-heater bypass during winterization**, or trusting a low-point drain valve's position without confirming flow has actually stopped, producing a frozen-and-cracked fitting discovered at spring de-winterization.

## Worked example

**Situation.** 2019 32-ft travel trailer, 6 years old, in for pre-winter service. Customer's stated complaints: "slide-out is hard to bring in" and "sometimes smells like propane near the stove." Shop labor rate $145/hr.

**LP-gas system.** Manometer connected at the range's test port, system pressurized to **11 in. W.C.** operating pressure, supply valve isolated, 3-minute timer started. Reading after 3 minutes: **9.25 in. W.C. — a 1.75 in. W.C. drop.** Fail; a lock-up test at operating pressure should hold with no measurable drop. Soap-solution search at every accessible connection finds bubbling at the 3/8 in. flare fitting behind the range, loose from vibration. Fitting re-torqued to the appliance connector's 15 ft-lb spec. Retest: pressurize to 11 in. W.C., isolate, 3-minute hold — reading remains **11 in. W.C.** Pass.

**Roof and moisture.** No roof seal inspection on file since delivery. Visual check finds a hairline crack in the self-leveling sealant at the right-rear roof vent. Moisture-meter pin reading at the ceiling/wall seam directly below that vent: **28%** (above the 20% active-intrusion threshold). Baseline reading at an unaffected corner 20 ft away: **12%** — confirms the 28% is localized, not ambient humidity. Probing finds no soft decking yet — caught before floor involvement. Repair scoped now: reseal the vent and re-finish a contained 2×2 ft interior ceiling panel. **Left another 12–18 months, this pattern (unaddressed seam leak reaching the substrate) is the mechanism that turns into a full sidewall or floor section replacement [stated heuristic — cost escalation pattern, not a specific quoted figure].**

**Slide-out.** Gap measured with the slide extended: **top rail 0.75 in., bottom rail 0.25 in. — a 0.5 in. difference**, well outside the ⅛–³⁄₁₆ in. (0.125–0.1875 in.) tolerance. Before touching cables or the gearmotor, tire pressure checked by position: rear axle at **45 psi against a 65 psi placard spec — a 20 psi deficit**, twisting the frame and racking the slide opening. Tires reinflated to 65 psi. Gap remeasured: **top 0.4 in., bottom 0.3 in. — a 0.1 in. difference**, within tolerance. Slide operates smoothly; no mechanism repair performed.

**Winterization.** Water heater bypass valves confirmed turned and tank fully drained before introducing antifreeze — skipping this step would have wasted several gallons into a tank being drained anyway. Fresh system blown down, then **3 gallons of RV antifreeze** pumped through until pink discharge at every fixture including the toilet and outdoor shower.

**Naive read a generalist would produce:** smell propane, soap-test the visible stove knobs, find nothing, tell the customer it's probably fine. Diagnose the slide as mechanism wear and quote a cable/gearmotor replacement ($450–$600 in parts and labor). Note the roof crack "for next season" since there's no active drip. Winterize by adding antifreeze without checking the bypass valves.

**Why it's wrong:** the propane leak is still live and untested by a spot soap-check alone — an unresolved fire/CO risk. The slide "repair" replaces functioning hardware while leaving the actual cause (tire pressure) untouched, and the bind returns the next time pressure drops. The roof leak, deferred, is exactly the failure mode that turns a $175 reseal into a structural repair. And an unconfirmed bypass risks a cracked water-heater fitting discovered frozen in spring.

**Work order, as written (deliverable, quoted):**

> **RO #7742 — 2019 32-ft travel trailer, pre-winter service.**
> **LP-gas:** Manometer lock-up test at 11 in. W.C. failed (9.25 in. W.C. after 3 min, 1.75 in. W.C. drop). Soap-search located leak at range 3/8 in. flare fitting. Re-torqued to 15 ft-lb spec. Retest: 11 in. W.C. held, no drop over 3 min. **Pass.** Labor 1.0 hr @ $145 + fitting $6.00 = **$151.00**.
> **Roof/moisture:** Hairline crack in vent sealant, right-rear. Moisture 28% at adjacent ceiling/wall seam vs. 12% baseline elsewhere. Resealed vent, repaired 2×2 ft interior panel section — contained, no floor involvement. Labor 2.5 hr @ $145 + materials $75.00 = **$437.50**.
> **Slide-out:** Racking measured 0.75 in. top / 0.25 in. bottom (0.5 in. delta) vs. ⅛–³⁄₁₆ in. spec. Cause: rear tires 45 psi vs. 65 psi placard. Reinflated; remeasured 0.4 in. / 0.3 in. (0.1 in. delta) — in tolerance. No mechanism repair needed. Labor 0.3 hr @ $145 = **$43.50**.
> **Winterization:** Water heater bypassed and drained, fresh system blown down, 3 gal RV antifreeze to pink discharge at all fixtures. Labor 1.0 hr @ $145 + antifreeze $18.00 = **$163.00**.
> **Total labor:** 4.8 hr @ $145/hr = $696.00. **Total parts/materials:** $99.00. **Grand total: $795.00.**
> **Not done today:** No slide cable, roller, or gearmotor work — mechanism tested sound once frame-square condition was corrected.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load for the filled LP-gas leak-test sequence, moisture-threshold and roof-membrane-interval tables, converter/inverter charge-stage table, slide-out alignment procedure, and the full winterization sequence.
- [`references/red-flags.md`](references/red-flags.md) — load when a complaint or PDI turns up a symptom that needs a first question and the specific data to pull before touching gas, electrical, or structural systems.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term (racking, bulk/absorption/float, delamination, bypass kit) needs a precise definition and the misuse that causes a wrong diagnosis.

## Sources

- NFPA 1192, *Standard on Recreational Vehicles* (2021+ editions, superseding ANSI/RVIA A119.2) — LP-gas, electrical, and plumbing system construction and test requirements referenced throughout for pressure and safety-gate figures.
- NFPA 58, *Liquefied Petroleum Gas Code* — general propane storage, cylinder, and handling requirements referenced for LP-gas system context.
- RV Industry Association (RVIA) — seal/certification program confirming as-built NFPA 1192 compliance; the basis for the "seal certifies at manufacture, not current condition" distinction.
- RV Technical Institute (RVTI, formerly RVTAA — RV Technician Association) — Level 1–3 and Master Certified RV Technician curriculum, the practitioner-consensus baseline for diagnostic sequence and safety-gate discipline in this trade.
- Dicor Corporation technical bulletins — EPDM/TPO roof membrane care, sealant type selection (self-leveling lap vs. non-sag), and recoat-interval guidance.
- Progressive Dynamics and WFCO technical manuals — multi-stage converter/charger bulk/absorption/float voltage profiles and lead-acid vs. lithium (LiFePO4) charge-profile mismatch risk.
- National RV Training Academy (NRVTA) instructional material — slide-out alignment diagnosis against frame level and tire pressure, and winterization bypass sequencing, as taught in the trade-school curriculum.
- No direct RV-service-technician practitioner has reviewed this file yet — flag corrections or gaps via PR.
