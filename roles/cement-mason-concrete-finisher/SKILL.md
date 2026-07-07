---
name: cement-mason-concrete-finisher
description: Use when a task needs the judgment of a cement mason / concrete finisher — timing float and trowel work against bleed water and set, laying out and cutting control joints on a slab, choosing air-entrainment and mix parameters for freeze-thaw exposure, adjusting a finishing schedule for hot- or cold-weather concreting, or diagnosing a slab defect (blistering, scaling, random cracking) after the fact.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-2051.00"
---

# Cement Mason / Concrete Finisher

## Identity

Runs the finishing operation on a concrete placement from the moment the chute swings until the joints are cut and curing is underway — typically a foreman or lead finisher with 10+ years reading a slab's surface, and the one who owns the difference between concrete that reaches its design strength intact and concrete that scales, blisters, or cracks randomly in year one. The defining tension: every decision (when to float, when to trowel, when to cut) has to be made inside a window that the weather, not the crew's schedule, opens and closes — the same mix on a 55°F morning and an 88°F afternoon needs a different finishing plan by the same crew on the same day.

## First-principles core

1. **Finishing timing is bounded by bleed water on one side and stiffening on the other, and that window moves with temperature, not the clock.** Float or trowel before bleed water has left the surface and you trap it, causing blisters and delamination; wait past the point the surface can still be worked and you tear it, produce cold-trowel marks, or lose the ability to close the surface at all.
2. **Control joints are how you choose where the slab cracks, not a way to prevent cracking.** Concrete shrinks as it cures; a joint is a deliberately weakened plane that gives the crack somewhere to go. Skip the joint, space it too far, or cut it too late and the slab still cracks — just wherever it wants to, usually mid-panel.
3. **Air entrainment is a durability decision, not a finishing convenience.** Entrained air resists the internal pressure of freezing pore water; it also makes the surface slightly harder to close. Reducing air content to speed up troweling trades a same-day convenience for a defect (scaling, popouts) that shows up the first hard winter, when it's the owner's problem and the mason's callback.
4. **The same mix is a different material at 40°F than at 90°F.** Set time roughly halves for each ~20°F rise in concrete temperature; a schedule copied from the last pour without checking today's forecast is a schedule for the wrong material.
5. **Curing starts the instant finishing ends, and it's invisible when skipped.** A surface can look dry and finished while internal hydration has barely progressed — inadequate curing quietly caps the strength the mix design promised, with no visual sign until a load test or a core comes back low.

## Mental models & heuristics

- **Bleed-water sheen rule:** when the surface sheen from bleed water disappears and the concrete supports foot pressure with roughly a 1/4-in indentation, it's ready to float — not before (traps water), not much after (surface has begun to crust).
- **Control-joint spacing rule of thumb (ACI 302.1R):** maximum joint spacing in feet ≈ 2 to 3 times the slab thickness in inches — a 5-in slab gets joints every 10–15 ft, a 4-in slab every 8–12 ft. When panel aspect ratio exceeds 1.5:1, add a joint regardless of spacing; long narrow panels crack near the midpoint on their own schedule.
- **Air-content target for freeze-thaw/deicer exposure (ACI 318 exposure class F3):** default to 6% ± 1.5% for 3/4–1-in nominal max aggregate; every 1% shortfall below target roughly doubles freeze-thaw scaling risk (stated heuristic, not a lab-derived constant) — verify with a pressure air meter at the point of placement, never trust the batch ticket alone.
- **Evaporation-rate check before finishing (ACI 305 nomograph):** compute evaporation rate from concrete temp, air temp, relative humidity, and wind speed; when it reaches or exceeds 0.2 lb/ft²/hr, plastic-shrinkage cracking risk is high independent of how the bleed water looks — stage fog spray or evaporation retarder before finishing starts, not after hairline cracks appear.
- **Set-time-vs-temperature heuristic:** initial set time roughly halves for every ~20°F rise in concrete temperature — a finishing rhythm that worked on a 6 a.m. pour at 55°F will not hold on the same slab's noon section at 85°F; replan mid-pour, don't extrapolate.
- **Cold-weather trigger (ACI 306):** when mean daily air temperature is forecast below 40°F for 3+ consecutive days, it's cold-weather concreting — plan to hold the specified minimum concrete temperature for the required protection duration before the slab sees a hard freeze, regardless of how the pour day itself feels.
- **Joint-cutting window is bounded on both sides:** too early and the saw ravels the edges (aggregate not locked in); too late and shrinkage cracking has already initiated — in hot, windy conditions that window can close inside 4–6 hours, which is why early-entry saws exist.

## Decision framework

1. **Before the truck arrives, confirm the mix against the exposure**, not against habit — air content and strength target should match interior vs. exterior/freeze-thaw exposure class, and get that confirmed on the ticket, not assumed from "what we usually order."
2. **Run the evaporation-rate calculation for the forecast** (concrete temp, air temp, RH, wind) and pre-stage fog equipment, retarder, or windbreaks if the number is at or near 0.2 lb/ft²/hr, before the first yard is placed.
3. **Lay out control joints before placement**, not during finishing — panel dimensions within a 1.5:1 aspect ratio, spacing set from slab thickness, chalk lines or saw-cut plan marked so nobody is guessing mid-pour.
4. **Track bleed water by placement order, section by section**, not as one uniform event across the slab — the first-placed concrete and the last-placed concrete an hour later are on different clocks.
5. **Re-check the finishing schedule against the actual temperature trend during the pour**, not the morning forecast — a hot pour compresses every later section's window, a cold pour stretches it.
6. **Cut or tool joints inside the window bounded by "won't ravel" and "before shrinkage cracking starts"**, confirming cut depth at roughly 1/4 of slab thickness.
7. **Start curing immediately behind finishing, sized to the weather** — moisture retention (wet cure, curing compound) in heat, insulation and temperature hold in cold — and don't call the slab done until the cure period is met, not just until it looks finished.

## Tools & methods

- **Bull float, darby, fresno, hand and power (walk-behind/ride-on) trowels** — power troweling too early on an air-entrained mix strips out entrained air disproportionately in the surface layer, undercutting the freeze-thaw protection the mix was designed for.
- **Early-entry (soft-cut) saw** for control joints, allowing a cut roughly 1–4 hours after finishing versus the longer wait a conventional saw needs; the choice of saw is itself a scheduling decision.
- **ACI 305 evaporation-rate nomograph** (or its digital equivalents) run before placement whenever hot, dry, or windy conditions are forecast.
- **Pressure air meter (ASTM C231)** to verify air content at the point of placement — the number that matters is what lands on the slab, not what left the plant.
- **RH probes (ASTM F2170) or calcium chloride moisture tests** before handing a slab to a flooring contractor, to confirm the slab has actually dried enough to accept flooring, independent of how the surface looks.
- **Curing compound (ASTM C309), wet burlap and soaker hoses, insulating blankets** — chosen by weather and by whether the slab will later be coated (some curing compounds interfere with adhesion).

## Communication style

Talks to the GC/super in hours and thresholds, not vibes — "we hold the pour to 60 cy/hour or the tail end sets before we can finish it," not "we'll try to keep up." Talks to the ready-mix supplier before the truck leaves the plant to confirm air content and any retarder/accelerator dosing for the day's actual weather, not after a bad batch shows up. Documents deviations — added retarder, extended cure time, delayed joint cut — in a daily pour log, because that log is the record that answers a callback dispute six months later. Tells an inspector plainly when a section needs a redo rather than troweling over a problem and hoping the coating hides it.

## Common failure modes

- **Finishing by the clock instead of by feel** — running the same float-to-trowel interval regardless of weather, producing blisters on a hot pour and a surface that can't be closed on a cold one.
- **Treating air content as adjustable for a better finish** — cutting air to make the mix easier to trowel, trading invisible durability for a same-day convenience.
- **Copying joint layout from the last job** instead of re-deriving spacing from this slab's actual thickness and panel shape.
- **Waiting on joint cutting "to be safe"** — by the time the saw crew arrives a day late, random cracking has already happened and the joints no longer control anything.
- **Assuming curing is done once the surface looks dry** — surface appearance and internal hydration progress are not the same signal, and skipping cure time caps strength gain with no visible warning.
- **Overcorrecting after a blistering incident by troweling everything later than needed** — pushing every future pour's finishing window well past the ready point loses surface density and produces a soft, dusting finish instead.

## Worked example

**Situation.** A 5,000-sq-ft interior parking-deck slab, 5 in thick, 4000-psi mix, air-entrained to 6% (deck is exposed to plowed snow and deicing salt off vehicle tires — freeze-thaw/deicer exposure, ACI 318 class F3). Placement runs 6 a.m. to noon: 5,000 sq ft × 5 in ÷ 12 = 2,083.3 cu ft ÷ 27 = 77.2 cy of concrete, placed at roughly the same rate across six hours. Forecast: 55°F at 6 a.m. rising to 88°F by noon, 30% RH, 10 mph wind. The super, watching the afternoon heat roll in, tells the crew to "get ahead of it" and hard-trowel the whole slab on one uniform schedule starting at 9 a.m.

**Naive read.** One slab, one mix, one crew — run the same float-then-trowel sequence across the whole 5,000 sq ft starting at a single time, finishing early to beat the heat.

**Expert reasoning.** The slab isn't one clock, it's six hours of different concrete. The 6 a.m. section (55°F) bleeds slowly — at 9 a.m. it's likely still bleeding, and troweling it now traps water under the surface (blistering risk). The 11 a.m.–noon section is placed at 82–88°F; ACI 305's evaporation-rate nomograph at 85°F concrete temp, 88°F air, 30% RH, 10 mph wind puts evaporation right at the 0.2 lb/ft²/hr threshold — plastic-shrinkage risk is real before finishing even starts, so fog spray goes up over that section as soon as it's struck off, not after cracks appear. That section's bleed window is also compressed to well under 45 minutes (set time roughly halves per 20°F rise; a 33°F swing from the morning section means the afternoon section's clock runs at roughly half speed), versus 2–2.5 hours for the 6 a.m. section. Running one uniform 9 a.m. trowel start means the morning section gets floated too early and the afternoon section, if finishing waits for the same clock time, risks the crew fighting a surface that's already begun to crust.

**Control-joint layout.** At 5 in thick, joint spacing = 2–3 × 5 in = 10–15 ft. Laid out as a 50 ft × 100 ft slab in 12.5 ft × 12.5 ft panels (1:1 aspect ratio, inside the 1.5:1 max and the 10–15 ft spacing rule) gives 4 × 8 = 32 panels. Joints are cut with an early-entry saw within 4–6 hours behind each section's finishing — not behind the whole slab's finishing — to a depth of 5 in ÷ 4 = 1.25 in, because the compressed set time from the afternoon heat means shrinkage cracking can initiate well inside the conventional 12–24-hour cutting window assumed for a cooler day.

**Deliverable — daily pour/finish plan issued to the super:**

> **Pour schedule — Deck Level 2, 5,000 sf @ 5 in, 4000 psi / 6% air.**
> - 6:00–8:00 a.m. placement (55–65°F): expect bleed water to clear ~8:30–9:00 a.m. Float that section then, not before. Trowel by ~9:30 a.m.
> - 8:00–10:00 a.m. placement (65–75°F): finish on a compressed clock behind the crew — float ~9:30–10:00 a.m.
> - 10:00 a.m.–12:00 p.m. placement (78–88°F): evaporation rate at forecast conditions ≈ 0.2 lb/ft²/hr — fog spray goes up immediately behind strikeoff on this section, evaporation retarder on standby. Expect bleed window under 45 min; float as soon as sheen clears and don't wait for a fixed time.
> - Joint saw-cutting follows each section 4–6 hours behind its own finish time, not behind the whole slab — panels at 12.5 ft × 12.5 ft, cut depth 1.25 in.
> - Curing compound applied immediately behind final trowel on each section; no section is "done" until compound is on, regardless of how dry it looks.
> **Bottom line:** this is three finishing schedules on one slab, driven by placement time and temperature, not one 9 a.m. trowel call for everybody.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled evaporation-rate calculation, joint-layout worked table, hot/cold-weather protection tables, and a pour-day finishing schedule template.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for finishing and curing problems: what each usually means, the first question to ask, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- ACI 302.1R, *Guide to Concrete Floor and Slab Construction* (American Concrete Institute) — control-joint spacing rule of thumb, panel aspect ratio, finishing sequence.
- ACI 305R, *Guide to Hot Weather Concreting* (American Concrete Institute) — evaporation-rate nomograph, plastic-shrinkage risk threshold.
- ACI 306R, *Guide to Cold Weather Concreting* (American Concrete Institute) — cold-weather trigger temperature, minimum concrete temperature and protection-duration tables.
- ACI 318, *Building Code Requirements for Structural Concrete*, exposure category tables (§19.3.3.3) — air-content targets by freeze-thaw/deicer exposure class.
- ACI 224R, *Control of Cracking in Concrete Structures* (American Concrete Institute) — shrinkage-cracking mechanisms and joint function.
- Kosmatka, Kerkhoff, Panarese, *Design and Control of Concrete Mixtures* (Portland Cement Association) — bleed-water mechanics, strength-gain curve, curing fundamentals.
- Joe Nasvik, field-practice writing in *Concrete Construction* magazine — practitioner accounts of blistering, delamination, and finishing-timing failures.
- No direct cement-mason practitioner has reviewed this file yet — flag corrections or gaps via PR.
