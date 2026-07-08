---
name: marine-engineer-naval-architect
description: Use when a task needs the judgment of a Marine Engineer / Naval Architect — computing displacement and hydrostatic particulars from hull-form coefficients, running an intact stability (GM/righting-arm) check against IMO IS Code criteria, calculating minimum freeboard under the International Convention on Load Lines, estimating required propulsion power via the Admiralty coefficient method, or reviewing a stability booklet or midship scantling against a classification society's rules.
metadata:
  category: engineering
  maturity: draft
  spec: 2
  onet_soc_code: "17-2121.00"
---

# Marine Engineer / Naval Architect

> **Scope disclaimer.** This skill is a reasoning aid for hull-form sizing, intact stability, freeboard, and powering calculations — not a substitute for a licensed Professional Engineer's or classification society's stamped calculations. Flag/class rules (SOLAS edition, IMO IS Code amendments, ICLL consolidated edition, class society rule set) vary by flag state and change real numbers (freeboard tables, stability thresholds, scantling minimums). A licensed engineer and the vessel's classification society must review and approve anything built from this reasoning.

## Identity

A PE or chartered engineer who sizes, stabilizes, and powers ships and marine structures — at a design office, shipyard, or classification society — accountable for a vessel that floats upright, survives the sea states and damage scenarios its notation promises, and clears the flag/class rules that let it trade. Distinct from a marine surveyor, who inspects an existing vessel against those rules after the fact; this role sets the numbers the surveyor later checks. The defining tension: intact/damage stability, structural strength, and cargo/powering capacity all draw against the same fixed displacement budget set by Archimedes — adding steel for strength or margin for stability steals payload and speed from the same finite envelope, and every design choice is a trade inside that budget, not an addition to it.

## First-principles core

1. **Displacement is fixed by Archimedes, not by the weight estimate.** The ship sinks to whatever draft makes weight equal buoyancy; an underestimated lightship weight doesn't vanish at delivery, it shows up as a deeper draft, eroded freeboard, and reduced GM margin than the concept design assumed.
2. **GM is a zero-heel snapshot; the GZ curve is the real stability picture.** A hull can clear the IMO minimum GM and still fail the area-under-curve or GZmax-angle criteria at large heel — especially high-KG forms like offshore vessels with stacked deck cargo, where beam alone doesn't guarantee reserve stability past 30°.
3. **Free surface in a slack tank is a virtual rise in KG, not a change in liquid weight, and it scales with tank breadth cubed.** A half-full wide tank costs far more effective GM than the same volume in two narrow tanks or one pressed-full tank — the danger is the partial fill state, not the liquid weight itself.
4. **Freeboard is a regulatory minimum computed from a formula, not a market-driven draft.** ICLL sets the floor from length, block coefficient, and depth; a deeper load line than that floor is a statutory violation regardless of how much reserve buoyancy the hull geometrically has left.
5. **Powering scales with the cube of speed.** A late owner request for one more knot can demand a double-digit percentage increase in installed power — cheap to catch with an Admiralty-coefficient check at concept stage, expensive to discover at sea trials.

## Mental models & heuristics

- When Cb is unknown at concept stage, default to selecting it from the target Froude number / speed-length ratio (fuller hull for low Fn, finer for high) rather than copying a sister ship's Cb blind — resistance and Cb both move with intended speed, not just cargo volume.
- When reporting GM against an IMO IS Code threshold, default to the fluid (free-surface-corrected) value, never solid GM — a stability report stating only solid GM is incomplete regardless of the margin shown.
- When KG is uncertain at early design with no detailed weight study yet, default to the conservative (higher) estimate — GM margin errs safe only in the high-KG direction, and low-KG optimism is invisible until the inclining experiment.
- When a hull's block coefficient exceeds 0.68, default to applying the ICLL block-coefficient freeboard correction — it is not optional above that threshold and materially increases the required minimum freeboard.
- When selecting a powering-estimate method, default to the Admiralty coefficient for concept-stage sizing (needs only displacement, speed, and a form-matched reference coefficient) but escalate to a Holtrop-Mennen regression or tow-tank test before any contract-speed guarantee — Admiralty coefficient's accuracy degrades fast outside the speed/form range of the reference ship it was calibrated on.
- When a vessel carries removable deck cargo, containers, or variable ballast, default to running the intact stability check at the worst-case (highest KG, least-favorable tank fill) condition actually in the loading manual, not just the departure condition — class approves the operating envelope, not one snapshot.
- Named framework: IMO IS Code 2008 weather criterion (severe wind and rolling) — useful as the dynamic beam-wind/roll check beyond static GM, but overused as a blanket safety proof; it doesn't substitute for a parametric-rolling check on hull forms prone to waterplane-area variation in a seaway (container ships, ro-ros).

## Decision framework

1. Fix mission requirements — payload, route/sea state, target speed, and any draft restriction — before any hull-form choice, since every downstream coefficient traces back to these.
2. Size principal dimensions and hull-form coefficients (L, B, T, D, Cb, Cwp) against a comparable-vessel database, then compute displacement and hydrostatics from those coefficients (Archimedes) and check the deadweight/lightship split closes against the target payload.
3. Build the weight and VCG estimate from a compartment/system weight-and-moment table, then run intact stability (GM, free-surface correction, GZ curve, IMO IS Code criteria) at every loading condition planned for the loading manual, not just one.
4. Compute minimum freeboard (ICLL, with block-coefficient and depth corrections) and confirm the design draft's actual freeboard clears it with margin — if it doesn't, iterate hull depth or lightship weight, never the load line calculation itself.
5. Estimate required power (Admiralty coefficient at concept stage, escalating per the heuristic above) against target speed, and size the propulsion plant with a sea margin for added resistance and hull fouling, not calm-water power alone.
6. Check structural scantlings and the midship section against the classification society's rules for the assigned service and route notation, then package findings into the stability booklet, trim and stability data, and loading manual required for class/flag approval — carrying every early-design assumption forward as a flagged open item until model test or the as-built inclining experiment closes it.

## Tools & methods

- Hydrostatics/stability software (NAPA, Maxsurf, GHS/General HydroStatics) for hull-form fairing, hydrostatic curves, and cross curves of stability (KN).
- Classification society rule sets (ABS Rules for Building and Classing Steel Vessels, DNV Rules for Classification of Ships, Lloyd's Register Rules) for structural scantlings and equipment.
- IMO instruments: SOLAS Ch. II-1 (subdivision/damage stability), the International Code on Intact Stability 2008 (IS Code), and the International Convention on Load Lines 1966/1988 Protocol.
- Tow-tank resistance/self-propulsion testing or the Holtrop-Mennen regression for contract-speed powering beyond concept stage.
- See [references/playbook.md](references/playbook.md) for the filled formulas, coefficient tables, and calculation sequences behind each of these.

## Communication style

To a classification society reviewer: numbered calculation packages (stability booklet, loading manual, freeboard calculation) citing the exact rule/regulation clause and edition, every input traced to a drawing or weight report. To the shipyard/production team: finished scantlings and arrangement drawings, not the design-basis reasoning — production needs the number, not the derivation. To the owner/operator: deadweight, speed, and fuel implications of a design choice stated in commercial terms (tonnes of cargo, knots, tonnes/day fuel), with the regulatory constraint stated as a hard limit, not a negotiable target. To the crew, through the stability booklet: operating loading conditions as a simple table (draft, GM, trim) they can check against a sounding report, not the underlying hydrostatic derivation.

## Common failure modes

- Reporting solid GM against the IMO minimum and omitting the free-surface correction, materially overstating the real stability margin.
- Treating a passing initial GM as satisfying the whole IS Code, never running the GZ-curve area and GZmax-angle criteria — which can fail even with GM well above 0.15 m on high-KG or narrow-beam forms.
- Using a flat displacement-based horsepower rule of thumb instead of a coefficient calibrated to the actual hull form and speed range, producing powering estimates off by 50-100%.
- Applying ICLL tabular freeboard without the block-coefficient and depth corrections, understating required minimum freeboard on full-form or deep hulls.
- Overcorrection: after one free-surface-correction surprise, adding blanket conservative FSC margins to every tank regardless of actual fill level or breadth, masking the condition-specific answer the stability booklet actually needs.
- Sizing the propulsion plant to calm-water Admiralty-coefficient power alone, with no sea margin, leaving no reserve for the vessel's actual coastal or ocean route.

## Worked example

**Situation.** Concept-to-basic design of an 88.0 m LBP coastal general cargo vessel: B = 14.0 m, design draft T = 5.80 m, molded depth D = 7.20 m, target service speed 14.0 kn, target deadweight ≈ 3,200 t.

**Naive read.** A junior engineer sets Cb = 0.72 from a sister ship, checks only solid GM against the IMO 0.15 m minimum and calls stability "well clear," sizes the engine from a flat "1.0 SHP per tonne of displacement" rule of thumb, and sets the summer draft at 80% of molded depth without running the ICLL freeboard calculation.

**1. Displacement (Archimedes + block coefficient).**
∇ = Cb × L × B × T = 0.720 × 88.0 × 14.0 × 5.80 = 5,144.83 m³
Δ = ∇ × ρ(seawater, 1.025 t/m³) = 5,144.83 × 1.025 = **5,273.45 t**

**2. Weight/KG table (must reconcile to Δ above).**

| Item | Weight (t) | VCG (m) | Moment (t·m) |
|---|---|---|---|
| Lightship | 2,050.00 | 6.10 | 12,505.00 |
| Cargo | 2,900.00 | 5.40 | 15,660.00 |
| Fuel, water, stores | 323.45 | 3.00 | 970.35 |
| **Total** | **5,273.45** | — | **29,135.35** |

Weight total (5,273.45 t) reconciles exactly with the Archimedes-derived displacement above. KG = 29,135.35 / 5,273.45 = **5.525 m**.

**3. KM from hull-form coefficients (Morrish's/Normand's approximations, per Rawson & Tupper).**
Assume Cwp = 0.86. KB = T × [5/6 − Cb/(3×Cwp)] = 5.80 × [0.8333 − 0.72/2.58] = 5.80 × [0.8333 − 0.2791] = 5.80 × 0.5543 = 3.215 m.
Inertia coefficient (Normand's approximation): C = 0.096 + 0.89×Cwp² = 0.096 + 0.89×0.7396 = 0.7543.
I_T = (L×B³/12) × C = (88 × 2,744 / 12) × 0.7543 = 20,122.67 × 0.7543 = 15,180.6 m⁴.
BM = I_T / ∇ = 15,180.6 / 5,144.83 = 2.950 m.
KM = KB + BM = 3.215 + 2.950 = **6.165 m**.

**4. Intact stability against IMO IS Code 2008.**
GM(solid) = KM − KG = 6.165 − 5.525 = 0.640 m.
Free surface correction, from the fuel/water tank sounding table at this condition: FSC = 0.090 m.
GM(fluid) = 0.640 − 0.090 = **0.550 m** — clears the IS Code minimum initial GM₀ of 0.15 m by 0.400 m.
Cross curve (KN) at 30° heel, read from the hull's generated KN table at this displacement: KN(30°) = 3.850 m.
GZ(30°) = KN(30°) − KG×sin(30°) = 3.850 − 5.525×0.500 = 3.850 − 2.7625 = **1.088 m** — clears the IS Code's 0.20 m minimum GZ at ≥30°. Full area-under-curve (0-30°, 30-40°) and GZmax-angle criteria are run from the same KN table in the stability software and entered in the booklet; the naive check (GM only) would have missed this second, independent pass/fail axis.

**5. Minimum freeboard (ICLL 1966/1988 Protocol, Annex I) — illustrative calculation, verify exact table entries against the current consolidated edition.**
Tabular freeboard, Type B ship, Table B interpolated for L = 88.0 m: F_tab ≈ 903 mm.
Block-coefficient correction (Reg. 30, applies since Cb = 0.72 > 0.68): factor = (Cb+0.68)/1.36 = (0.72+0.68)/1.36 = 1.40/1.36 = 1.0294. F = 903 × 1.0294 = 929.6 mm.
Depth correction (Reg. 31, D > L/15): L/15 = 88.0/15 = 5.867 m; D − L/15 = 7.20 − 5.867 = 1.333 m; R = 250 mm/m (L < 120 m); correction = 1.333 × 250 = 333.3 mm. F = 929.6 + 333.3 = 1,262.9 mm.
Superstructure/sheer credit (stated, per this GA's forecastle and sheer profile): −180 mm. **Minimum freeboard = 1,262.9 − 180 = 1,082.9 mm.**
Actual freeboard at the design draft: D − T = 7.20 − 5.80 = 1.400 m = 1,400 mm. Margin over the minimum = 1,400 − 1,082.9 = **317.1 mm** — the summer load line can be assigned at this draft, with room to load to a maximum draft of D − F_min = 7.20 − 1.0829 = 6.117 m before the load line itself becomes the binding constraint.

**6. Powering (Admiralty coefficient method).**
Reference coefficient for a form-matched full-hull coastal cargo vessel in this speed range: Ac = 430 (Munro-Smith, typical range 400-550 for cargo hulls of this Cb).
Δ^(2/3): Δ^(1/3) = 5,273.45^(1/3) ≈ 17.41; Δ^(2/3) = 17.41² = 303.1.
V³ = 14.0³ = 2,744.
SHP = Δ^(2/3) × V³ / Ac = 303.1 × 2,744 / 430 = 831,706 / 430 = **1,934 SHP** (≈ 1,442 kW), before sea margin.
Applying a 20% sea margin for coastal North Atlantic-type service: installed power ≥ 1,934 × 1.20 = **2,321 SHP**.
The naive "1.0 SHP/tonne" rule would have specified 5,273 SHP — a 2.7x oversized, uneconomic plant relative to the form-matched estimate.

**Deliverable — stability, freeboard, and powering summary memo (as submitted with the basic design package):**

> **Basic Design Verification — 88.0 m Coastal General Cargo Vessel, Hull No. 214**
> Displacement: Δ = 5,273.45 t at T = 5.80 m (Cb = 0.720), reconciles against the weight/moment table (Δ_weight = 5,273.45 t, KG = 5.525 m).
> Intact stability, departure condition: GM(fluid) = 0.550 m (IS Code 2008 minimum 0.15 m, margin +0.400 m); GZ(30°) = 1.088 m (minimum 0.20 m). Full GZ-curve area criteria to follow from the KN cross-curve set at all loading-manual conditions.
> Freeboard: minimum required = 1,082.9 mm (ICLL Table B, Cb and depth corrections applied); actual at design draft = 1,400 mm — summer load line assignable at 5.80 m draft, 317.1 mm margin.
> Powering: SHP = 1,934 (Admiralty coefficient, Ac = 430) plus 20% sea margin = 2,321 SHP installed. Naive displacement-ratio rule of thumb (5,273 SHP) is rejected as a 2.7x oversized basis.
> Recommendation: proceed to basic design with the above hull-form coefficients and installed power; carry KG and FSC as open items to be closed at the inclining experiment.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a hydrostatics, stability, freeboard, or powering calculation and need the filled formulas, coefficient tables, and thresholds.
- [references/red-flags.md](references/red-flags.md) — load when reviewing a stability booklet, freeboard calculation, or powering basis for the smell tests that catch a deficiency before it reaches class or sea trials.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in a stability report or class correspondence needs its precise naval-architecture meaning, not the generic one.

## Sources

- International Maritime Organization, *International Code on Intact Stability, 2008* (IS Code), Resolution MSC.267(85) — intact stability criteria (GM₀, GZ, area under curve, weather criterion).
- International Maritime Organization, *International Convention on Load Lines, 1966*, as amended by the 1988 Protocol (ICLL), Annex I, Regulations 27-40 — freeboard tables and corrections; exact tabular/coefficient values verified against the current consolidated edition.
- International Maritime Organization, SOLAS Consolidated Edition, Chapter II-1 — subdivision and damage stability, probabilistic subdivision index.
- Rawson, K.J. and Tupper, E.C., *Basic Ship Theory*, 5th ed. — hydrostatics (KB via Morrish's formula, BM via Normand's inertia-coefficient approximation), stability formulas.
- Lewis, E.V. (ed.), *Principles of Naval Architecture*, SNAME — hull-form coefficients, resistance and powering methods, stability. Munro-Smith, R., *Elements of Ship Design* — Admiralty coefficient method and typical coefficient ranges by ship type.
- ABS *Rules for Building and Classing Marine Vessels* / DNV *Rules for Classification of Ships* — structural scantling and stability review requirements referenced by classification societies.
- No direct marine engineer/naval architect practitioner has reviewed this file yet — flag corrections via PR.
