# Rail Car Repairer — Playbook

Filled reference sequences: wheel/coupler/brake condemning-limit inspection, the single-car air brake test, and the defect-vs-wear-and-tear billing classification.

## 1. Wheel inspection sequence

Work each measurement in order; a wheel that fails any one line is condemned regardless of the others.

| Step | Measurement | Condemning limit (illustrative — confirm against current AAR MSRP Section G / 49 CFR 215) | If fail |
|---|---|---|---|
| 1 | Flange thickness (gauge) | At or below 7/8 in (22 mm) | Condemn wheel — climb-derailment risk independent of tread condition |
| 2 | Flange height (gauge) | At or above roughly 1 9/16 in (39.7 mm) | Condemn — usually paired with hollow-worn tread |
| 3 | Tread hollow-wear depth | Deeper than roughly 3/16 in (4.8 mm) | Condemn — flange no longer rides correctly on rail |
| 4 | Flat spot length | Single flat ≥2.5 in, or two adjacent flats each ≥2 in | Condemn — impact loading at speed risks bearing/axle damage |
| 5 | Thermal crack / heat check on tread or plate | Any visible crack | Condemn — usually from a dragging or stuck brake shoe; check that shoe/rigging too |
| 6 | Wheel diameter difference, same axle | Exceeds roughly 1/2 in | Condemn — mismatched rolling diameters cause differential slip and bearing load |

**If a flat spot is found:** check the chatter-mark pattern before writing the cause. Sharp-edged, uniform-depth marks with a matching brake-shoe wear pattern on the same truck indicate a slide event (wheel locked under braking). A smooth, gradually worn tread with no matching shoe anomaly indicates ordinary wear-out — pull the car's Umler mileage-since-service to confirm which pattern fits.

## 2. Brake shoe and rigging check

| Item | Condemning limit (illustrative) | Note |
|---|---|---|
| Composition brake shoe, remaining thickness | At or below roughly 3/8 in | Retarding force falls off nonlinearly near the backing plate — replace, don't stretch the interval |
| Cast-iron brake shoe, remaining thickness | At or below roughly 3/4 in | Higher starting thickness, same nonlinear-wear logic |
| Uneven shoe wear across a truck (>2x difference between shoes) | Any | Check for a stuck or dragging brake cylinder/rigging on the thin side before just replacing shoes |
| Brake rigging travel (piston travel) | Outside car's rated range (commonly 7–9 in depending on equipment) | Adjust or replace slack adjuster before release |

## 3. Coupler and knuckle inspection

| Step | Action | Pass criterion | If fail |
|---|---|---|---|
| 1 | Visual inspection of knuckle, yoke, and coupler body for cracks | No visible cracks | Any visible crack → scrap the part, no weld repair |
| 2 | Magnetic-particle inspection (Magnaflux) on knuckle and pin | No subsurface indications | Any crack indication → scrap, regardless of visual appearance |
| 3 | Knuckle throw / coupler gauge check | Within AAR gauge tolerance for the coupler type | Out of gauge → replace knuckle or coupler, don't shim or force |
| 4 | Coupler pulling face wear | Within AAR wear-limit gauge | Beyond limit → replace coupler body |

**Never weld-repair a knuckle, coupler yoke, or coupler body.** These are heat-treated castings; welding destroys the temper that gives them fatigue strength, and the next failure happens without warning — this is a scrap-and-replace item across the industry, not a shop-judgment call.

## 4. Single-car air brake test (SCTD, per AAR S-486)

Run this sequence on every car that had brake-system work before re-stenciling and releasing it to interchange.

| Step | Action | Pass criterion | If fail |
|---|---|---|---|
| 1 | Charge brake pipe to car's rated pressure (commonly 90 psi for freight equipment) | Full charge reached and holds | Slow charge → check angle cocks, hose connections, strainer |
| 2 | Brake pipe leakage test (isolate car, monitor pressure decay) | Leakage at or below shop's pass threshold (commonly cited around 5 psi/min) | Above threshold → find and fix the leak, then retest — don't adjust and re-run without finding the source |
| 3 | Full-service brake pipe reduction (commonly 20 psi) | Brake cylinder develops to the car's rated pressure range (commonly in the 50–55 psi band for a 20 psi reduction on standard freight brake equipment) | Under- or over-development → check control valve, cylinder piston travel, or brake equipment type mismatch |
| 4 | Release test | Brake cylinder pressure releases fully within rated time | Slow or incomplete release → check control valve exhaust or retainer valve position |
| 5 | Record actual pressures and leakage rate, not just pass/fail | — | This record is what makes the car interchange-legal; keep it with the repair order |

## 5. Defect-vs-wear-and-tear billing worksheet

Before drafting the repair bill, work through this in order:

1. **What's the physical evidence?** Impact bruising, sharp chatter marks, coupler misalignment, or discoloration from overheating point to a handling event. Smooth, gradual wear consistent with mileage points to ordinary use.
2. **What does the car's service history say?** Pull mileage or time since the component was last serviced from Umler. A defect appearing far short of the component's normal service life is evidence against ordinary wear-out.
3. **Is there a logged handling event?** Check for a recent derailment, hard coupling, over-speed hump, or reported rough-ride complaint tied to a specific road's possession of the car.
4. **Classify and bill accordingly:**

| Classification | Who pays | Evidence pattern |
|---|---|---|
| Wear-and-tear | Car owner | Gradual wear pattern, mileage/time since service consistent with normal component life, no logged handling event |
| Handling-caused | Road that had possession when the event occurred | Impact/slide/overheat pattern, mileage/time since service inconsistent with gradual wear, and/or a logged event on that road's watch |

5. **Document the classification with the physical evidence cited**, not just the conclusion — this is the record a disputing road's billing clerk will review 30–90 days later, and a bare conclusion without evidence loses disputes on the merits regardless of whether the original call was correct.

**Example comparison (illustrative dollar figures):**

| Scenario | Repair cost | Billed to | Basis |
|---|---|---|---|
| Wheel wearing out at 280,000 miles, smooth gradual tread wear | $1,182.50 | Car owner | Within normal wear-out range, no handling event logged |
| Wheel flat-spotted at 42,000 miles since last service, sharp chatter marks, matching shoe wear pattern | $1,391.25 | Handling road | Far short of normal wear-out range, slide-event evidence pattern |
