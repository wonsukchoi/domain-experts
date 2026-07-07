# Construction and Building Inspector — Playbook

## Standard hold-point inspection sequence and what each gates

| Order | Inspection | What it verifies | What it gates (can't proceed without passing) |
|---|---|---|---|
| 1 | Foundation | Footing depth/width, rebar placement and size, soil bearing, setback from property line | Backfill and framing — footing/rebar becomes unverifiable once poured over and backfilled |
| 2 | Framing | Structural members, headers, connectors/hardware, bracing, sheathing nailing pattern | Insulation and drywall — every framing member becomes hidden once insulated and covered |
| 3 | Rough-in (electrical/plumbing/mechanical) | Wire routing and protection, box fill, pipe joints and pressure test, duct sizing and sealing | Insulation and drywall — pipe joints and wire runs become unverifiable non-destructively once covered |
| 4 | Insulation | R-value per climate zone, vapor barrier placement, air-sealing at penetrations | Drywall — insulation and air-sealing become inaccessible once drywall is hung |
| 5 | Final | All systems operational, all prior corrections closed, life-safety devices installed and tested | Certificate of Occupancy — nothing further gates this; it's the last check before occupancy |

**Use:** Never combine two hold points into one visit to save the contractor a trip, even if both look ready — each inspection exists specifically because the next phase makes it unverifiable, and a rushed combined check reproduces exactly the missed-connector or unverified-joint failure the sequence is designed to prevent.

## Re-inspection fee and schedule-delay economics (illustrative figures)

| Scenario | Cost/delay to contractor | Pressure this creates |
|---|---|---|
| First-time inspection fails, re-inspection scheduled next business day | Re-inspection fee ($75–$150 typical municipal range) + 1 day schedule slip | Low — routine, budgeted into most schedules |
| Fails twice on the same item | Second re-inspection fee, often at a doubled or escalated rate; 2–3 day slip | Moderate — contractor may push back harder on the third visit |
| Fails on a life-safety item (egress, fire separation) after drywall is already hung | Demolition and rework cost, not just a fee — can run into thousands of dollars and 1–2 weeks | High — this is the scenario contractors most want to avoid, and the scenario the hold-point sequence exists to prevent |
| Trade crew (e.g., drywall) is on-site the day of a failed rough-in | Crew stand-down or reschedule cost, borne by the general contractor, not the inspector | High and immediate — this is the single most common source of on-site pressure to pass marginal rough-in work |

**Use:** All of these are the contractor's cost-of-doing-business figures, not code information. The inspection determination does not change based on which row of this table the contractor is currently in — documenting the finding the same way regardless of the fee/delay context is what keeps a correction notice defensible later.

## Egress window compliance calculation (filled example)

| Step | Value |
|---|---|
| Measured opening: width | 22 in |
| Measured opening: height | 22 in |
| Net clear opening area = width × height | 22 × 22 = 484 sq in = 3.36 sq ft |
| IRC R310.2.1 minimum net clear opening (above grade) | 5.7 sq ft (820.8 sq in) |
| IRC R310.2.1 minimum net clear opening (grade-floor/basement) | 5.0 sq ft (720 sq in) |
| IRC R310.2.2 minimum net clear height | 24 in |
| IRC R310.2.3 minimum net clear width | 20 in |
| **Result** | Width passes (22 in ≥ 20 in); height fails (22 in < 24 in); area fails (3.36 sq ft vs. 5.7 sq ft, 59% of minimum) |

**Use:** Check width, height, and total net clear area against all three sub-thresholds independently — a window can pass one dimension and still fail on net clear area, and area alone can look close while a single dimension is the actual disqualifying factor.

## GFCI/AFCI and smoke/CO detector placement checklist (illustrative, per IRC family)

| Location | Requirement | Common miss |
|---|---|---|
| Kitchen countertop receptacles | GFCI-protected, all countertop receptacles (IRC E3902.6) | Protecting only receptacles within 6 ft of the sink instead of all countertop receptacles |
| Bathroom receptacles | GFCI-protected, all receptacles regardless of distance from sink (IRC E3902.1) | Assuming only the receptacle nearest the sink needs protection |
| Garage and unfinished basement receptacles | GFCI-protected (IRC E3902.2, E3902.3) | Overlooking a single receptacle added later for a freezer or workbench |
| Bedroom branch circuits | AFCI-protected (IRC E3902.12/E3902.16, per code cycle) | Confusing AFCI (arc-fault, bedrooms/living areas) with GFCI (ground-fault, wet locations) — they protect against different failure modes and are not interchangeable |
| Smoke alarms | Inside each bedroom, outside each sleeping area, one per additional story (IRC R314.3) | Placing a required alarm within the code-excluded distance of a bathroom door with a shower/tub (nuisance-alarm risk; check local amendment for exact distance, commonly 3 ft) |
| CO alarms | Outside each separate sleeping area in the immediate vicinity of bedrooms, in dwellings with fuel-fired appliances or an attached garage (IRC R315.3) | Omitting CO alarm entirely in a remodel that adds a fuel-fired water heater or furnace, treating it as a new-construction-only requirement |

**Use:** Section numbers shift between code cycles (2018/2021/2024 IRC) and jurisdictions amend them — treat the section numbers here as the pattern to look up in the specific adopted edition, not a citation to copy verbatim into a correction notice without verifying against that jurisdiction's current code.

## Correction notice — filled example (life-safety item)

> **Correction Notice — Permit #RES-2026-0447, Rough-In Electrical Inspection**
> **Result: FAILED. Re-inspection required before any concealment (drywall, insulation) proceeds.**
> Item: Bedroom 2 egress window, measured net clear opening 22 in × 22 in = 3.36 sq ft, against IRC R310.2.1 minimum 5.7 sq ft — 59% of required opening area.
> Classification: Life-safety, zero-tolerance.
> Correction: Replace window unit to meet minimum net clear opening before any wall covering is installed.
> Re-inspection fee: $85 per Permit Fee Sec. 4.2.
> Photo on file: BR2-WIN-01 (tape measure in frame).

**Use:** A defensible correction notice always carries five elements together — exact code section, exact measurement or condition, classification (life-safety vs. standard), the specific correction required, and a photo reference. Dropping any one of the five is what makes a notice read as an opinion rather than a finding on appeal.

## Plans-vs-field discrepancy routing decision table

| Discrepancy type | Inspector authority | Correct routing |
|---|---|---|
| As-built wall location off by a few inches, non-structural, non-egress | Inspector discretion — approve if code-neutral | Document as-built note, proceed |
| Header size or species installed differs from stamped plan | Outside inspector authority — structural judgment | Hold inspection, route to engineer of record for a field-change approval or stamped revision |
| Room use changed from what plans show (e.g., "office" built out as an extra bedroom) | Outside inspector authority — affects egress/occupancy requirements | Hold inspection, route to plan review before proceeding |
| Fixture count or minor layout shift within the same room, no structural or life-safety effect | Inspector discretion — approve if code-neutral | Document as-built note, proceed |

**Use:** The dividing line is whether resolving the discrepancy requires an engineering or code-intent judgment (route it out) versus a purely as-built factual note with no structural or life-safety consequence (inspector can close it). When in doubt, route it — an inspector who resolves a structural question in the field has exceeded the inspection's actual authority.
