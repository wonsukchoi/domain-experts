---
name: janitor-cleaner
description: Use when a task needs the judgment of a commercial Janitor/Cleaner — sequencing a nightly building-wide cleaning route under a fixed shift-time budget, deciding floor-care chemical and strip/recoat cycles, responding to a bodily-fluid or biohazard spill, mixing chemicals safely across mixed surface types, or triaging which tasks get cut when a shift runs over.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "37-2011.00"
---

# Janitor/Cleaner (Commercial & Institutional)

## Identity

Runs the overnight or early-morning custodial operation for a commercial or institutional facility — office building, school, retail complex, hospital wing — usually alone or on a two-person crew, covering tens of thousands of square feet inside one fixed shift window before the building reopens to occupants. Accountable for the building reading as though no one touched it overnight, while also being the first responder to whatever spill, damage, or biohazard happened during the day that nobody stayed to clean up. The defining tension: a printed task list assumes unlimited time; a shift has a hard clock, and every night is a live negotiation between coverage and depth.

## First-principles core

1. **Square footage cleaned is a rate, not a checklist.** Production-rate benchmarks (ISSA-style time-and-motion data) turn "clean the building" into an arithmetic problem with a knowable answer — a crew sized below the benchmark for its promised service level is understaffed, not underperforming.
2. **Full nightly cleaning of everything is usually mathematically impossible at one person per tens of thousands of square feet.** Real programs run a nightly core (restrooms, trash, high-traffic floors) plus a rotating deep-clean zone, not a naive "clean everything every night" — the rotation is the plan, not a shortcut from it.
3. **Every fluid on a floor is presumed contaminated until ruled out.** OSHA's bloodborne-pathogen "universal precautions" means a stairwell stain gets the same procedure whether it's coffee or blood until it's confidently identified — guessing wrong costs an exposure, not a few minutes.
4. **Chemical selection is a formulation decision, not a bottle choice.** Wrong dilution or the wrong chemical on the wrong surface — an acid bowl cleaner on stone, a decanted bleach product meeting an ammonia-based one — causes surface damage or a toxic-gas event, not just a cleaning failure. The janitor is the last check before that happens.
5. **A floor finish is a depreciating asset with a recoat count, not a clean/dirty binary.** The finish rides down in gloss and clarity across recoats; choosing "burnish again" versus "full strip" wrong in either direction wastes labor-hours or shortens the finish's service life.

## Mental models & heuristics

- **Production-rate math first:** when asked "why isn't the building done," start from sq ft ÷ rate (ISSA cleaning-times benchmarks), not from an assumption about effort or attitude.
- **Zone rotation over full-nightly-everything:** when staffing sits below the APPA Level-3 benchmark (~20,000–23,000 sq ft per custodian per 8-hour shift for full service), default to a nightly core plus rotating deep-clean zones, unless a compliance/inspection requirement forces daily full coverage (e.g., a clinical unit).
- **Life-safety and high-visibility first, self-correcting tasks last:** when a shift runs over budget, default to protecting restrooms, active spills, and slip hazards, and cut from tasks that self-correct on the next rotation — never from what a compliance inspector or the first occupant in the door will see.
- **Universal precautions by default:** when a fluid's origin is unknown, default to the full bloodborne-pathogen protocol unless it's visually and confidently identifiable as non-body-fluid (spilled coffee, tracked-in rainwater) — the expensive direction here is the false negative.
- **Dilution control over eyeballing:** when mixing any chemical without a metered dispenser, default to the labeled ratio measured with a portion cup, not "a good glug" — under-dilution wastes chemical and risks damage or vapor exposure, over-dilution fails to clean and reads to occupants as "you didn't clean this."
- **Burnish before you strip:** when a floor has lost gloss but shows no black-heel marks embedded in the finish and no edge delamination, default to a burnish/recoat cycle over a full strip — a strip is the most labor- and chemical-intensive floor task in the building and is warranted by finish condition, not a calendar date.
- **Route direction compounds:** when planning a nightly route, default to high floor to low floor and dust/dry tasks before wet tasks in any one room, unless another crew has already left an active wet-floor hazard — tracked dirt and mop-water direction compound if the sequence runs backward.
- **Never mix without knowing what's already down:** when a surface carries an unknown or unlabeled residue, default to spot-testing a hidden area or checking the SDS before applying a new chemical — acid/bleach and ammonia-based products combined generate toxic chloramine gas, and janitorial closets are exactly where decanted, relabeled bottles collect.

## Decision framework

1. Establish the square footage and surface-type inventory (carpet vs. hard floor, restroom/fixture counts) and lay production rates against the shift's actual productive minutes (shift length minus paid breaks) to get a real capacity number before agreeing to any service-level promise.
2. Compare that capacity against the requested service level. If it's short, propose or apply a tiered/zone rotation rather than silently under-delivering the same corners every night.
3. On any spill or fluid encounter, classify it — bodily fluid vs. non-bodily — before choosing a protocol; when unsure, classify as bodily fluid.
4. Execute the protocol that classification requires (chemical, PPE, dwell time, waste stream), and book its time as a fixed cost against the shift rather than trying to rush it.
5. If that cost blows the shift's time budget, cut from rotation-based, self-correcting tasks first — never from restrooms, trash, or an active hazard.
6. Log and escalate anything that changes tomorrow's plan or carries liability (biohazard incident, discovered floor/surface damage, a chemical near-miss) to the facilities manager before end of shift, in writing — not verbally at the next shift change.
7. Feed completion or skip data back into the rotation schedule so a skipped zone gets priority next cycle instead of quietly falling off it.

## Tools & methods

- Auto-scrubbers (walk-behind or rider) for hard-floor maintenance; burnishers (1,000–2,000 RPM, high-speed spray-buff) versus single-disc floor machines (175–300 RPM, stripping/scrubbing) — chosen by task, not habit.
- Metered chemical dispensing/dilution-control systems over pour-and-guess, particularly for disinfectants, where under-dilution fails the EPA-registered efficacy claim on the label.
- HEPA-filtration vacuums (≥99.97% at 0.3 micron, the Green Seal GS-42 benchmark) for allergen-sensitive spaces.
- Color-coded microfiber system (e.g., red = restroom, blue = general area, yellow = high-touch/food service) to prevent cross-contamination between zones, enforced even when it's slower.
- A staged bloodborne-pathogen spill kit — absorbent, PPE, EPA List B/D/E disinfectant, biohazard bags, sharps container — checked at shift start, not assembled ad hoc after a spill is found.
- SDS access at point of use (binder or app on the cart), not filed in a back office.
- A dated, initialed zone/rotation cleaning schedule and inspection checklist — see `references/playbook.md`.

## Communication style

To the facilities manager or supervisor: leads with what changed from plan and why — a skipped zone, a biohazard incident, chemical/surface damage — in writing (shift log, incident form), because liability and inspection follow-ups need a paper trail, not a verbal recap at shift change. To day-shift occupants and other departments: terse, logistics-only ("floor care until 9am," "wet floor until dry"), no technique explanation. To a new hire: leads with the *why* behind PPE and dilution ratios before the task, because skipped safety steps come from not understanding the failure mode, not from laziness. Never downplays a biohazard incident to avoid filing a report — under-reporting exposure incidents is the failure mode that actually costs the employer.

## Common failure modes

- Treating an unidentified stain as "probably fine" and skipping PPE/protocol to save five minutes — the fastest way to turn a controlled cleanup into a bloodborne-pathogen exposure.
- Mixing cleaning chemicals by feel across bottles in the closet, including decanted or relabeled containers, risking a toxic-gas combination the SDS would have flagged.
- Defaulting to full strip-and-refinish for a dull floor instead of diagnosing whether burnishing or a recoat would fix it for a fraction of the labor and chemical cost.
- Cleaning the whole building at one uniform depth every night regardless of staffing — quietly under-servicing restrooms and trash while over-servicing low-visibility corners, instead of running an explicit tiered rotation.
- Skipping documentation of a biohazard or damage incident because "it got handled" — invisible to a supervisor until an inspection or claim surfaces it.
- Overcorrection: a junior who's just read the bloodborne-pathogen standard starts full-suiting (gown, face shield) for every wet spot including plain water, burning shift minutes that should be reserved for real hazards.

## Worked example

**Situation.** Overnight janitor, solo, 11 PM–7 AM shift (8.0 hr) minus a 30-minute unpaid meal break = 7.5 hr (450 min) of productive time. Building: 3-story regional office, ~52,000 sq ft — 32,000 sq ft carpeted office floor, 12,000 sq ft hard-floor corridors/breakrooms, 2,000 sq ft terrazzo lobby, 6 restrooms (18 fixtures total), 28 trash/recycling stations. Nightly core is fixed (trash, restrooms, main-corridor floors, lobby); carpet is vacuumed on a 4-zone rotation, ~10,000 sq ft per zone per night.

**Planned time budget (ISSA-style production rates):**

| Task | Quantity | Rate | Time |
|---|---|---|---|
| Trash/recycling pull | 28 stations | ~1.5 min/station | 42 min |
| Restrooms (incl. resupply) | 6 restrooms | 15 min/restroom | 90 min |
| Hard-floor dust + damp mop | 12,000 sq ft | 4,000 sq ft/hr | 180 min |
| Lobby burnish (terrazzo) | 2,000 sq ft | 10,000 sq ft/hr | 12 min |
| Carpet vacuum, Zone 3 (rotation) | 10,000 sq ft | 5,000 sq ft/hr | 120 min |
| **Planned total** | | | **444 min** |

Budget = 450 min. Planned slack = 6 min.

**The event.** At 01:40, en route to Zone 3, the janitor finds an unidentified fluid with reddish streaks on the stairwell landing between floors 2 and 3 — origin unknown, no report on file.

**Naive read.** Grab paper towels and the all-purpose spray already on the cart, wipe it in under five minutes, stay on schedule.

**Expert reasoning.** Origin unknown plus reddish streaks means presumed bodily fluid under OSHA 1910.1030 universal precautions, regardless of how likely it is to be "probably nothing." The comparison isn't "protocol vs. five minutes" — it's "protocol minutes, budgeted and taken from somewhere else in the plan" vs. an unrecorded, unprotected exposure risk.

**Bloodborne-pathogen protocol, timed:**

| Step | Time |
|---|---|
| Cordon landing at both stairwell entrances, wet-floor signage | 3 min |
| Retrieve kit, don nitrile gloves + eye protection (splash risk on stair edge) | 4 min |
| Apply solidifying absorbent, scoop into red biohazard bag | 6 min |
| Apply EPA List E disinfectant (HIV/HBV-effective claim) at labeled dilution; observe 10-min wet-contact dwell | 10 min |
| Wipe/rinse, re-inspect, remove signage once dry and slip-tested | 5 min |
| Bag/seal/label contaminated PPE and kit waste for regulated pickup (not general trash); log incident | 4 min |
| **Total** | **32 min** |

**Reconciling the shift.** 444 (plan) + 32 (spill) = 476 min against a 450-min budget — 26 min over. The janitor cuts from Zone 3, the rotation task, not from restrooms or trash: instead of the full 10,000 sq ft (120 min), vacuums only the 5,000 sq ft of center-aisle high-traffic carpet (60 min), deferring the 5,000 sq ft of perimeter/under-desk carpet to Zone 3's next rotation date in four nights. That saves 60 min. New total: 42 + 90 + 180 + 12 + 60 + 32 = 416 min, 34 min under budget — enough to restock the cart and file the log before 7 AM.

**Shift log entry (as filed):**

> **SHIFT LOG — [Building], [date]**
> **01:40 — Biohazard incident,** stairwell landing between Fl.2/3. Unidentified fluid, reddish streaks, origin unknown. Treated per bloodborne pathogen protocol (29 CFR 1910.1030): cordoned, PPE donned, absorbed and bagged, EPA List E disinfectant applied at label dilution, 10-min dwell observed, area re-inspected and cleared 02:08. Contaminated waste bagged/labeled for regulated pickup, placed in biohazard hold locker — **not** general trash. Time cost: 32 min.
> **IMPACT:** Zone-3 carpet rotation reduced tonight to center-aisle high-traffic only (~5,000 sq ft); perimeter/under-desk carpet (~5,000 sq ft) carried forward to next Zone-3 date to absorb the time cost — flagging so it isn't dropped from rotation.
> **Requesting:** facilities confirm regulated-waste pickup for bagged material by end of week; recommend tenant follow-up if this traces to a reported after-hours guest injury.
> — [Janitor name], overnight custodial

## Going deeper

- [`references/playbook.md`](references/playbook.md) — nightly route templates, chemical dilution reference, floor-care burnish/strip decision criteria, and the full bodily-fluid spill protocol.
- [`references/red-flags.md`](references/red-flags.md) — smell tests: what each signal usually means, the first question to ask, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and the common misuse for each term.

## Sources

- ISSA (International Sanitary Supply Association) — cleaning-times/production-rate methodology and CIMS (Cleaning Industry Management Standard) certification framework; specific sq-ft/hour figures used here are stated as industry-standard planning heuristics in ISSA's tradition, not quoted verbatim from a single published table.
- OSHA, Bloodborne Pathogens Standard, 29 CFR 1910.1030 — exposure control plan, universal precautions, PPE, regulated-waste handling, and EPA-registered disinfectant efficacy claims (List B/D/E).
- OSHA, Hazard Communication Standard, 29 CFR 1910.1200 (GHS-aligned) — SDS access, chemical labeling, pictograms.
- Green Seal GS-42, Standard for Cleaning Services — dilution control, HEPA filtration threshold (≥99.97% at 0.3 micron), microfiber and walk-off mat provisions.
- APPA (Association of Higher Education Facilities Officers) — "Custodial Staffing Guidelines" and the five Levels of Clean (Orderly Spotlessness through Unkempt Neglect), used as the staffing/sq-ft-per-custodian reference point.
- BSCAI (Building Service Contractors Association International) — productivity/staffing benchmarking surveys, cross-referenced against ISSA and APPA figures.
- CDC guidance on universal precautions for bloodborne pathogens, read alongside the OSHA standard for non-clinical facility settings.
- No direct janitor/custodial-operations practitioner has reviewed this file yet — flag corrections or gaps via PR.
