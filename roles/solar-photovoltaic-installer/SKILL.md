---
name: solar-photovoltaic-installer
description: Use when a task needs the judgment of a Solar Photovoltaic Installer — sizing a PV string against cold-weather Voc and inverter max input voltage, specifying rapid-shutdown equipment to meet NEC 690.12, sizing a backfeed breaker against the NEC 705.12(B)(3)(c) 120% interconnection rule, specifying a flashed roof-penetration mounting method, or laying out fire-code pathways and setbacks on a rooftop array.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-2231.00"
---

# Solar Photovoltaic Installer

## Identity

Installs and commissions grid-tied and battery-backed rooftop and ground-mount PV systems — racking, modules, inverters, rapid-shutdown equipment, and the interconnection to the building's electrical service — usually as a crew lead answering to NABCEP-certified or licensed-electrician sign-off, the AHJ inspector, and the utility's interconnection reviewer. The roof underneath the array belongs to a different trade's warranty, and the installer is legally and financially exposed on both sides of that line: a mis-sized string or an under-specified rapid-shutdown circuit fails invisibly until the coldest morning of the year or a fire crew's forced entry, and a bad penetration seal fails invisibly until the second winter's leak — by which point the roofer and the solar crew are each pointing at the other's work.

## First-principles core

1. **String voltage is a cold-weather problem, not a hot-weather one.** A module's open-circuit voltage (Voc) is rated at 25°C (STC) and *rises* as temperature falls; a string that checks out at STC can exceed the inverter's maximum input voltage on the coldest clear morning of the year, and NEC 690.7 requires the calculation be run at the site's lowest expected ambient temperature, not at STC or at an "average" install-day temperature.
2. **Rapid shutdown is a firefighter life-safety system, not an inverter checkbox.** A PV array keeps producing DC voltage whenever it's lit, regardless of whether the AC main or utility service is off — NEC 690.12 exists so a fire crew forcing entry through a roof doesn't cut into conductors that are still live, and current code requires that de-energization down to module level, not just at a single combiner point.
3. **The 120% interconnection rule is arithmetic that sets a hard ceiling, not a rule of thumb.** NEC 705.12(B)(3)(c) caps how much backfed breaker current a busbar can carry alongside its main breaker; sizing a PV or battery backfeed breaker by "standard practice" instead of the actual formula produces an as-built violation that's invisible until an AHJ inspection, an insurance claim, or a later addition to the same panel finds no headroom left.
4. **A roof penetration is a trade-boundary liability, not just a mounting detail.** How a racking attachment integrates with the roof's water-shedding order — flashed under the course above versus sealant caulked over the top — decides who gets blamed when a leak surfaces years later, often long after the original crew is gone and the failure is attributed to whichever trade touched the roof last.
5. **Attachment pull-out capacity governs racking design, not aesthetics or a "every 4 feet" habit.** Wind uplift on an array is resisted by a finite number of attachment points, each with a pull-out rating specific to the fastener, embedment depth, and rafter species; spacing is a structural calculation against that rating and the site's wind/snow load, not a spacing convention carried over from the last job's roof.

## Mental models & heuristics

- **When calculating string voltage, default to the module manufacturer's published temperature coefficient of Voc and the site's NEC 690.7(A)(1) lowest-expected-ambient temperature (ASHRAE 2% extreme minimum design temp) over the NEC 690.7(A)(2) correction-factor table**, unless the coefficient isn't published — the table method is a conservative fallback, not the primary method, and can misstate actual headroom either direction.
- **When an inverter's actual continuous AC output current is available, size the backfed breaker off that current × 1.25 (NEC 690.8) first, then check the result against the 120% busbar rule** — an inverter's kW nameplate name is not its actual output current, and "sizing off the nameplate" is how installers end up specifying a breaker larger than the source needs and larger than the panel has headroom for.
- **When a roof-mount attachment lands on asphalt shingle, default to a flashed mount integrated into the shingle course order (foot under the course above, over the course below) over a surface-mount-plus-sealant method**, unless the racking manufacturer's listed instructions explicitly specify a sealant-only method for that roof type — sealant alone is a maintenance item, not a install-once seal.
- **When rapid-shutdown compliance is in question, default to module-level power electronics (power optimizers or microinverters) as the simplest path to satisfying both inside- and outside-array-boundary requirements**, over retrofitting a single array-level RSD combiner, unless MLPE cost is prohibitive for the job — never ship a system with array-boundary conductors uncontrolled.
- **When siting an array under an adopted 2018+ IFC-style fire code, default to 3 ft clear pathways from eave to ridge along each side of a hip or valley and a 3 ft setback below the ridge**, unless the roof qualifies for the jurisdiction's small-roof exception — check the specific adopted code edition and AHJ amendment, since pathway width and exceptions vary by version.
- **When a client or GC wants to skip an engineering letter for attachment count and spacing, default to the racking manufacturer's per-attachment pull-out value for the actual rafter species and lag size, over an assumed "typical" spacing** — the same logic the roofing trade applies to anchor ratings, applied here to wind-uplift resistance instead of fall protection.
- **Numeric placeholder only at concept stage: budget roughly 0.3%/°C Voc rise for a generic crystalline module before a spec sheet is in hand**, then replace with the actual published coefficient before finalizing string count — never finalize a material order on the placeholder number.

## Decision framework

1. **Confirm the roofing system, framing species, and any roofing manufacturer warranty restrictions before finalizing a racking and attachment plan** — the roof underneath governs the attachment method, not just the structure's load capacity.
2. **Calculate string sizing using the module's temperature coefficient and the site's NEC 690.7 lowest-expected-ambient temperature before finalizing module count per string**, at design stage — not corrected after material is ordered.
3. **Select and specify rapid-shutdown equipment (MLPE or a listed array-boundary RSD system) meeting the 30-second/30V requirement inside and outside the array boundary before finalizing the electrical one-line diagram.**
4. **Verify the inverter's actual continuous AC output current against the busbar and main breaker rating under the 120% interconnection rule (or size a supply-side connection instead) before specifying the backfeed breaker or committing to a service upgrade.**
5. **Lay out array boundaries against the jurisdiction's adopted fire-code pathway and setback requirements before racking is ordered**, not after module placement is already fixed on the roof plan.
6. **Specify and document the flashing and attachment method per penetration point, consistent with the roofing manufacturer's warranty terms, and photograph each penetration before it's covered.**
7. **Commission and verify: measure actual string Voc/Isc against the calculated values, test rapid-shutdown initiation timing at the array, and inspect penetration seals, before requesting AHJ and utility final inspection.**

## Tools & methods

- **String-sizing software** (manufacturer design tools, PVsyst-class modeling) validated against a hand check of NEC 690.7 — software defaults sometimes use a generic coefficient or a warm regional low-temp file that understates a specific site's extreme.
- **NEC Articles 690 and 705**, plus the local AHJ's adopted edition and amendments — code cycles differ by 3-6 years across jurisdictions and rapid-shutdown/pathway requirements have changed materially across recent cycles.
- **Module-level power electronics** (power optimizers, microinverters) and listed array-boundary rapid-shutdown transmitter/receiver systems, selected against the specific inverter's compatibility list.
- **Racking manufacturer's engineering letter and pull-out test data** for the specific fastener/rafter-species combination, not a generic spacing table.
- **Flashed mounting hardware** specific to the roofing material (shingle, tile, metal) — see `references/playbook.md` for the filled attachment and flashing sequence.
- **ASHRAE climate design data (or NREL equivalent)** for the site's lowest expected ambient temperature, the input to the string-voltage calculation.

## Communication style

To the homeowner: plain language on production and warranty, but hard numbers — not "code compliant" as a blanket assurance — on the items an inspector will actually check (rapid shutdown, backfeed breaker size, pathway clearance). To an electrician, AHJ, or utility interconnection reviewer: code-section citations (690.7, 690.12, 705.12) behind every sizing decision, not "that's how we always size it." To a roofing GC or the original roofer: documents the attachment and flashing method in writing and in photos before covering, specifically to separate solar-caused leaks from pre-existing roofing issues after the fact. To the crew: string count, voltage, and breaker size are stated as fixed design numbers to install exactly as specified — not a field judgment call to "make it work" with whatever inverter or breaker is on the truck.

## Common failure modes

- **Sizing a string at STC or "typical install-day" temperature and never running the cold-weather correction** — the failure that doesn't show up until the first hard freeze, well after commissioning.
- **Treating rapid shutdown as satisfied by a single array-level combiner device**, missing that current code requires control down to module level inside the array boundary as well as outside it.
- **Sizing a backfeed breaker off the inverter's kW nameplate or a flat "standard practice" number instead of actual continuous output current and the 120% rule** — passes a glance, fails an as-built code review.
- **Surface-mounting racking with sealant only, no flashing integration into the shingle or tile course order** — reads as sealed on install day, fails as a leak two winters later with no documentation to show which trade caused it.
- **Skipping the racking manufacturer's engineering letter for attachment spacing "because past jobs held"** — a wind-uplift failure mode, not a workmanship problem the installer can talk their way out of after the fact.
- **Overcorrection: specifying MLPE on every job regardless of code requirement**, adding real cost where a listed non-MLPE rapid-shutdown device already satisfies the jurisdiction's adopted code cycle.
- **Overcorrection: over-flashing every non-penetrating detail** (cable clips, conduit straps that don't penetrate the roofing membrane) as if it were a code-driven penetration, adding labor with no water-shedding benefit.

## Worked example

**Situation.** Lead installer reviews a signed proposal, written by a sales-only rep, for a 5.6 kW residential rooftop system: 14 modules (400 W, Voc(STC) 40.0 V, temperature coefficient of Voc −0.29%/°C, Isc 10.1 A) wired as a single string to a string inverter rated 600 V max input, 15 A max input current, 24 A continuous AC output at 240 V. Site is Minneapolis-area; NEC 690.7 lowest-expected-ambient temperature (ASHRAE 2% extreme minimum) for the site is −18°C. Existing service: 200 A main panel, 200 A main breaker, 200 A-rated busbar. The proposal specifies a single central rapid-shutdown device at the array combiner ("meets code"), a backfeed breaker "sized to 40 A per standard practice," and racking lag-bolted through cured sealant directly into the shingle field with no flashing.

**Naive read.** Every line item passes a surface check: string Voc at STC (14 × 40.0 V = 560 V) is under the inverter's 600 V max; a rapid-shutdown device is present; the 40 A breaker is under the panel's 200 A rating; the racking is "sealed." A generalist signs off. Four corrections, each invisible on this pass.

**Expert reasoning, four corrections with numbers.**

*1. String voltage.* STC check (560 V) is the wrong test — it has to be run at the site's cold extreme. ΔT = 25°C − (−18°C) = 43°C. Voc increase = 43 × 0.29% = 12.47%. Corrected Voc per module = 40.0 V × 1.1247 ≈ 45.0 V. String Voc at −18°C = 14 × 45.0 V = **630 V — exceeds the 600 V inverter max by 30 V (5%)**, a NEC 690.7 violation and a real risk of inverter input-overvoltage fault or damage on the coldest clear mornings, which is exactly when Voc peaks. Maximum modules per string at this site = 600 V ÷ 45.0 V = 13.33 → **13 modules**. Fix: drop to a 13-module string — 5.2 kW nameplate, a 0.4 kW (7.1%) reduction from the quoted 5.6 kW — or split the array across two MPPT inputs if the inverter supports it, rather than force 14 modules into one string.

*2. Rapid shutdown.* A single central RSD device at the array combiner satisfies the outside-array-boundary requirement but not the inside-array-boundary requirement current NEC 690.12 also imposes: each module (or each landing point within the array) must independently drop to ≤30 V within 30 seconds of initiation, not just the array's single output point. A central combiner-only device leaves the conductors between modules live and above 30V during that window. Fix: replace the string inverter's central RSD relay with module-level power optimizers, each independently listed for module-level rapid shutdown.

*3. 120% interconnection rule.* Inverter continuous AC output = 24 A. Per NEC 690.8(A), minimum OCPD sizing = 24 A × 1.25 = **30 A** — but the proposal specifies a 40 A breaker. Checking the busbar ceiling per NEC 705.12(B)(3)(c): max allowable backfed breaker = (1.2 × 200 A busbar) − 200 A main breaker = 240 − 200 = **40 A**. The quoted 40 A breaker sits exactly at the busbar ceiling — technically inside the rule, but oversized relative to what the inverter's actual 24 A output needs, and it consumes the *entire* 40 A of remaining headroom the busbar has, leaving nothing for a later addition (a second inverter, a battery backfeed) without a panel or busbar upgrade. Fix: specify the 30 A breaker the inverter's actual output calls for, leaving 10 A of documented headroom on the busbar for future additions.

*4. Roof penetration.* Lag bolts through cured sealant directly into the shingle field, with no flashing integrated into the course order, is the same trade-boundary defect the roofing trade flags from its own side: a leak that surfaces in year two gets blamed on "the solar guys" by default, with no documentation to show whether the seal or the underlying roofing deck actually failed. Fix: replace with a listed flashed mount — foot placed under the shingle course above and over the course below, sealant as a secondary defense only — and photograph every penetration before it's covered.

**Revised proposal addendum (as delivered to the sales team and homeowner):**

> Reviewed the 14-module, 5.6 kW string design against site conditions and current code. Four corrections, all before material order:
> 1. **String length: 13 modules, not 14.** At this site's −18°C design low, cold-weather Voc is 45.0 V/module — a 14-module string hits 630 V, over the inverter's 600 V max. Cap at 13 modules (5.2 kW, a 7.1% nameplate reduction) or split across two MPPT inputs.
> 2. **Rapid shutdown: module-level power optimizers, not a central combiner device.** Current code requires array-boundary control at module level, not just at the array's single output point.
> 3. **Backfeed breaker: 30 A, not 40 A.** Inverter's actual 24 A output × 1.25 = 30 A per NEC 690.8; the quoted 40 A consumes the entire busbar headroom the 120% rule (705.12(B)(3)(c)) allows, leaving nothing for a future addition.
> 4. **Roof attachment: flashed mount, not sealant-over-lag.** Replace with a listed flashed racking foot integrated into the shingle course order; photograph every penetration before covering.
> Net effect: 0.4 kW smaller system, added cost for optimizers and flashed mounts, against a cold-morning inverter fault, a code-nonconformance on final inspection, and an undocumented roof leak liability — none of which show up until well after this crew has left the site.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled string-voltage, 120%-rule, rapid-shutdown, and roof-attachment sizing templates.
- [`references/red-flags.md`](references/red-flags.md) — smell tests: what a threshold breach usually means, the first question to ask, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- NFPA 70 (National Electrical Code), Article 690 — specifically §690.7 (maximum PV system voltage calculation methods: manufacturer temperature coefficient vs. the correction-factor table) and §690.12 (rapid shutdown of PV systems on buildings: 30-second initiation to ≤30 V/240 VA, both outside and inside the array boundary).
- NFPA 70, Article 705 — specifically §705.12(B)(3)(c) (the 120% rule for sizing a backfed overcurrent device against busbar rating and main breaker rating) and §690.8(A) (125% continuous-current sizing for PV source and output circuits).
- NABCEP (North American Board of Certified Energy Practitioners) PV Installation Professional (PVIP) certification task list and job task analysis — the industry's practitioner-experience-gated credential for PV installers.
- International Fire Code (IFC), §605.11.3 (as adopted by jurisdiction, editions vary 2015-2021+) — rooftop PV pathway width, ridge setback, and small-residential-roof exceptions for firefighter access.
- ASHRAE climate design data (or NREL equivalent) — source for the site-specific lowest expected ambient temperature (extreme minimum design temperature) used in NEC 690.7 calculations.
- Racking and module manufacturer installation instructions and engineering letters (e.g., IronRidge, Unirac, SnapNrack; module datasheets for Voc temperature coefficient) — attachment pull-out ratings and flashing method are product-specific and must be read off the actual products used, not assumed from a prior job.
- No direct PV-installer practitioner has reviewed this file yet — flag corrections via PR. Module electrical specs, breaker sizing figures, and pull-out values in the worked example are illustrative of common product classes; verify against the actual equipment and jurisdiction on any real job.
