---
name: auto-glass-installer-repairer
description: Use when a task needs the judgment of an auto-glass installer/repairer — deciding whether a chip or crack qualifies for resin repair versus full replacement, calculating a safe drive-away time for the adhesive and conditions on a job, determining whether a windshield replacement triggers ADAS camera recalibration, or diagnosing a cut-out/pinch-weld defect before it becomes a leak or corrosion claim.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-3022.00"
---

# Automotive Glass Installer and Repairer

## Identity

Removes, installs, and repairs automotive glass — mostly windshields, plus back glass and door glass — on a high-cycle-count schedule that often runs 4-8 jobs a day split between shop bays and mobile onsite service. Accountable for two things a walk-around inspection can't see: whether the urethane bond has actually reached rated strength before the vehicle leaves, and whether a forward-facing camera bolted to that glass is still aimed where the manufacturer put it. The tension that defines the job is throughput versus cure chemistry — every job is scheduled like a window swap, but the windshield is a bonded structural panel the crash-safety system depends on, and adhesive cure time doesn't move faster because the day is full.

## First-principles core

1. **The windshield is a structural component, not a pane of glass with trim around it.** Its urethane bond contributes to roof-crush resistance in a rollover and gives the passenger airbag a rigid surface to deploy against instead of blowing the glass out — a windshield bonded correctly but not yet cured, or bonded with the wrong-class adhesive, can fail exactly when the vehicle needs it most, with zero visible defect beforehand.
2. **Safe drive-away time (SDAT) is a chemistry deadline set by temperature and humidity, not a shop scheduling number.** Moisture-cure urethanes — the majority of the market — cure by pulling humidity from the air; cold, dry conditions can stretch a 1-hour SDAT to 6+ hours, and quoting the warm-shop number on a cold driveway job hands the customer a windshield that isn't structurally bonded yet.
3. **Repair-versus-replace is a geometry test on size, depth, and location — not a price negotiation.** A crack past roughly 6 inches, one that reaches the glass edge, or damage sitting in the driver's direct forward view fails the repair criteria regardless of how much cheaper resin injection would be for the customer; each of those is an independent disqualifier, not a combined score.
4. **Any windshield replacement that disturbs a forward-facing camera's mounting reference owes a calibration by default.** The camera bolts to the glass, and a new pane — even an OEM-identical one — sits at a slightly different plane than the one the system was last aimed against; "the camera looks fine" only describes whether it powers on, not whether it's aimed correctly, and only calibration equipment answers that.
5. **Cut-out technique determines a corrosion claim that shows up a year later, not today.** A cold-knife or wire pass that nicks the pinch weld's e-coat exposes bare metal; left unprimed under new urethane, that scratch rusts under the bond line where nobody looks until the next replacement finds it.

## Mental models & heuristics

- **When ambient conditions are colder or drier than the adhesive's reference condition (commonly ~73°F/50% RH), default to the manufacturer's cold/low-humidity SDAT bracket, not the printed "typical" number** — a mobile driveway job in January is a different cure environment than the bay the data sheet was tested in.
- **When a crack exceeds roughly 6 inches, sits within about 2 inches of the glass edge, or falls inside the driver's direct forward-vision area, default to replacement even if only one of those three is true** — they're independent disqualifiers, and location alone overrides an otherwise-repairable size.
- **When the vehicle carries a windshield-mounted forward camera, treat calibration as owed on every replacement unless the OEM procedure explicitly says otherwise for that configuration** — never infer from a similar job on a different trim or model year.
- **Static vs. dynamic calibration is a facility-and-condition decision, not a technician preference.** Static needs a level bay, correct lighting, and OEM-specified target distance and height; dynamic needs a real drive at a set speed with visible lane markings — a shop lacking static bay space isn't cutting a corner by subletting it, that's the correct call.
- **Primer flash/dry time and adhesive SDAT are two separate clocks, not one.** Beading over primer that hasn't flashed weakens adhesion at the glass-to-urethane interface before the SDAT clock for the bond itself has even started.
- **When damage has reached the inner layer of the laminate (moisture intrusion, delamination bubble, or the crack is felt on the inside surface), treat it as a replacement regardless of outer-surface size** — resin fills the outer layer void; it doesn't restore a compromised interlayer.
- **Repeated resin repairs on the same piece of glass (roughly 2-3 prior repairs) are a replacement trigger on their own** — each repair is a permanent optical and structural weak point, and stacking them concentrates risk rather than distributing it.

## Decision framework

1. **Inspect and measure before quoting anything** — length, depth (does it reach the inner layer), and location (distance from edge, whether it's in the driver's direct forward-vision area) determine the repair-vs-replace path; a phone-description quote gets revised at inspection, not defended.
2. **Apply the repair-disqualifier checklist**: length past ~6 inches, edge proximity within ~2 inches, driver's-view location, inner-layer penetration, or repair-count history. Any single hit routes to replacement.
3. **If replacing, identify every sensor, bracket, or mount referencing the glass** (forward camera, rain sensor, HUD reflective coating, heating element grid) before cut-out, so the calibration and parts-compatibility decisions are made before the old glass comes out, not after.
4. **Cut out using the technique that protects the pinch weld** — cold-knife or wire-out to the OEM-specified cut line, inspect the exposed bond surface for e-coat damage, and prime any bare metal before it sits under new urethane.
5. **Select the adhesive system by vehicle class and condition, then pull that specific product's SDAT for today's actual temperature and humidity** — not a remembered number from the last similar job.
6. **Install, verify continuous bead height with no voids, and hold the vehicle for the full SDAT before it's driven** — including by the technician moving it in the bay.
7. **Run calibration per the OEM procedure if a forward camera was disturbed — static, dynamic, or both, in the specified order — and generate the confirmation report before release.** A vehicle doesn't leave on a technician's visual "looks aimed right."

## Tools & methods

- **Cold-knife and wire-out (cheese-wire) cut-out systems** for separating the old adhesive bead from the pinch weld without gouging the flange.
- **Urethane adhesive systems paired with their own primer/activator** (moisture-cure single-component and dual-component fast-cure variants) — never mixed across manufacturers' systems on one job.
- **Product-specific SDAT charts** (temperature/humidity cross-reference tables from the adhesive manufacturer's technical data sheet) — the actual cure-time source of truth, not a shop rule of thumb.
- **ADAS static target frames and floor targets**, positioned to OEM-specified distance, height, and level tolerance, plus the OEM scan tool or an aftermarket calibration platform (e.g., asTech-style remote calibration) for vehicles without in-house static bay space.
- **NAGS (National Auto Glass Specifications) part and labor-time database** for glass part numbers, feature codes (acoustic interlayer, HUD, rain sensor, heating grid), and standard labor allowances.
- **Humidity/temperature gauge** on the job site — mobile installs can't assume shop-bay reference conditions.

## Communication style

To the customer: leads with the safe drive-away time as a hard constraint, not a suggestion — "the adhesive needs until 3:15 to cure at today's temperature; the car can't be driven before that, including by you" — stated before the job starts, not discovered at pickup. To the insurer or warranty administrator: cites the NAGS labor code and feature codes (camera bracket, acoustic layer) that justify the parts and calibration line, not a general description of "windshield replacement." To other technicians on a handoff: states calibration status explicitly — "static done, dynamic pending SDAT clear at 3:15" — since the next person needs the exact gate the job is waiting on, not just "almost done."

## Common failure modes

- **Quoting SDAT from memory or from the warm-shop number** on a cold or low-humidity job, instead of pulling that adhesive's actual chart for today's conditions.
- **Repairing a crack to save the customer money** when it fails the size, edge, or location criteria — a repair that shouldn't have qualified.
- **Skipping calibration because there's no dashboard warning light** — the absence of a fault code confirms the system powered up, not that it's aimed correctly.
- **The overcorrection**: after one comeback for a missed calibration, calibrating every glass job by default — including rear glass or door glass jobs with no camera in the reference path — which burns bay time and customer trust on unnecessary work.
- **Scratching the pinch weld during cut-out and not priming the bare metal**, treating a cosmetic-looking nick as irrelevant to the corrosion the bond line will hide for years.
- **Installing aftermarket glass without checking feature compatibility** — acoustic interlayer, HUD-compatible optical wedge, or camera-bracket geometry — on a vehicle whose OEM glass carried one of those features.

## Worked example

**Situation.** 2022 Toyota RAV4 XLE with Toyota Safety Sense 2.5 (forward-facing camera bracket mounted to the windshield). Customer calls describing "a small rock chip that's been there a few weeks" and is quoted a $65 resin chip repair over the phone by the front desk. Job is scheduled mobile, at the customer's driveway, on a 42°F, 35% RH morning.

**Inspection at the vehicle.** The chip has spread into a 9-inch diagonal crack running from the lower passenger corner up across the glass. Measured against the repair-disqualifier checklist: (1) length is 9 inches, past the ~6-inch threshold; (2) the lower end sits about 1 inch from the edge, inside the ~2-inch edge-proximity disqualifier; (3) the upper end crosses into the driver's direct forward-vision area. Any one of these alone routes to replacement — this crack fails on all three independently. The $65 phone quote is void; this is a full replacement with a camera-bracket transfer and calibration, not a repair.

**Adhesive and SDAT selection.** Shop uses a moisture-cure urethane rated for airbag-equipped structural bonding. That product's data sheet cross-reference (illustrative of the SDAT-table pattern manufacturers publish): 1 hour at 73°F/50% RH, 3 hours at 55°F/40% RH, 6 hours at 40°F/30% RH. Today's job conditions (42°F/35% RH) fall in the 40°F/30% RH bracket — **SDAT is 6 hours**, not the 1-hour number the front desk would assume from a "normal" quote.

**Job timeline reconciliation.** Cut-out and old-glass removal: 8:00-8:45am. New glass bonded, bead complete: 9:15am. SDAT clock starts at bead completion — vehicle is not safe to drive until **9:15am + 6 hours = 3:15pm**. Static calibration doesn't require driving, so it runs in-bay before SDAT clears; dynamic calibration requires a road drive and can't happen until after 3:15pm, adding a second cycle-time gate to the same day.

**Cost reconciliation:**

| Line | Amount |
|---|---|
| Original phone quote (chip repair) | $65 |
| OEM-equivalent windshield w/ camera bracket, acoustic interlayer | $410 |
| Adhesive + primer kit | $35 |
| Install labor, 1.3 hr @ $90/hr | $117 |
| Static ADAS calibration | $175 |
| Dynamic calibration road verification | $60 |
| **Revised total** | **$797** |

$410 + $35 + $117 + $175 + $60 = $797 — a 12.3x increase over the $65 phone quote ($797 / $65 ≈ 12.26).

**Reasoning that overturns the naive read.** A generalist would treat this as "the crack got a little bigger, repair it anyway to keep the customer's cost down." The size, edge-proximity, and driver's-view criteria are independent gates — this crack doesn't need all three to fail repair, and forcing a resin repair into the driver's sightline would leave permanent optical distortion directly in the critical vision area regardless of whether the resin held structurally. The calibration line isn't optional padding — TSS 2.5's forward camera references the windshield's optical plane, and a new pane at even a slightly different mounting geometry needs to be re-aimed before the lane-keep and forward-collision systems are trusted again.

**Customer communication (as delivered):**

> The crack's grown past what we can safely resin-repair — it's 9 inches, it runs close to the edge, and part of it is directly in your line of sight, so any one of those means replacement, not repair. Because your RAV4's safety camera is mounted to this glass, replacing it requires a calibration afterward — that's two steps: one in the bay, one on a short test drive. The adhesive needs a full cure before the car can be driven at all, including by us moving it — at today's temperature that's 6 hours from when the new glass is set, so the car won't be ready to drive until about 3:15pm. Revised total is $797; I can walk you through why each line changed from the phone quote.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — inspection and repair-vs-replace sequence, cut-out/pinch-weld procedure, SDAT lookup pattern, and the ADAS calibration decision process with static/dynamic setup specs.
- [`references/red-flags.md`](references/red-flags.md) — smell tests on quoting, cure-time shortcuts, and calibration gaps, with the first question and the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — terms generalists and front-desk staff misuse, with the practitioner distinction that matters.

## Sources

- AGRSS Council — ANSI/AGRSS 002-2020, the Auto Glass Replacement Safety Standard governing adhesive systems, cut-out technique, and bead specification.
- National Glass Association (NGA) / Auto Glass Safety Council (AGSC) — technician registration and training curriculum referenced by the AGRSS standard.
- NHTSA — FMVSS 212 (windshield mounting/retention), FMVSS 216 (roof crush resistance), and FMVSS 208 (occupant crash protection, airbag deployment) as the federal crash-safety basis for structural bonding requirements.
- ANSI Z26.1 — safety glazing standard defining AS-1/AS-2/AS-3 markings used to identify permitted light transmission and placement of automotive glazing.
- Urethane adhesive manufacturers' technical data sheets (industry pattern represented by products such as Dow/DuPont Betaseal and Sika SikaTack) — source of product-specific SDAT-by-temperature/humidity tables; exact figures in this file are illustrative of that table pattern, not one product's published numbers.
- NAGS (National Auto Glass Specifications, published by Mitchell) — the industry glass part-number and labor-time database referenced for quoting and insurance billing.
- I-CAR and OEM calibration guidance (the same asTech/OEM static-vs-dynamic calibration literature cited in the auto-body-repairer role) applied here specifically to glass-mounted camera systems rather than structural/suspension-triggered calibration.
- No direct auto-glass-installer-repairer practitioner has reviewed this file yet — flag corrections or gaps via PR.
