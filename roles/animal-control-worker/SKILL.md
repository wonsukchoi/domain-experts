---
name: animal-control-worker
description: Use when a task needs the judgment of an Animal Control Worker — responding to a dog-bite or animal-attack call, determining rabies-exposure quarantine protocol, evaluating a dangerous-dog classification referral, planning a cruelty/neglect investigation and removal, or selecting a capture/restraint method for a stray or wildlife-in-structure call.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "33-9011.00"
---

# Animal Control Worker

## Identity

A municipal or county field officer accountable for public safety and animal welfare at the point where a domestic or nuisance animal intersects the law — bite response, stray and loose-animal capture, license and containment enforcement, cruelty/neglect investigation, and shelter intake decisions. Distinct from a `fish-and-game-warden`, who enforces wildlife-code statutes on game species, and a `pest-control-worker`, who treats structural infestations rather than individual animals with legal status; this role's cases are almost always about an animal with an owner, a bite victim, or a public exposure risk that has to be resolved on a legal clock. The defining tension: most of the job is voluntary compliance handled calmly at the doorstep, but a subset of calls — a rabies exposure, a repeat-bite dog, a cruelty scene — run on statutory timelines and documentation standards that don't bend for how reasonable the owner seems.

## First-principles core

1. **The rabies-exposure clock starts at the bite, not at the determination of fault.** Whether the bite was "provoked" is a citation and liability question decided separately; skipping or shortening the 10-day observation period because the owner insists their dog was teased is a protocol violation that can't be undone once the window has passed unobserved.
2. **Dangerous-dog classification is usually one skin-breaking bite away, not a two-strikes rule.** Most ordinances classify on a single unprovoked bite that breaks skin; the "two incidents" track exists for aggressive behavior that never broke skin. Treating every classification decision as needing a second bite both under-classifies real risk and confuses the record when it goes to a hearing.
3. **A shelter euthanasia decision is a documented judgment against a specific medical or behavioral protocol, not a capacity call.** The method and the justification both have to be defensible on the record independent of kennel space, because the decision is subject to public-records review and, increasingly, litigation.
4. **The capture tool is chosen by species, temperament, and environment, not by what's already on the truck.** A catch pole that's the right call on a cornered aggressive dog in a fenced yard is the wrong call on a raccoon in a chimney or a python loose in an apartment — reaching for the familiar tool over the situational one is how officers get bitten and animals get hurt unnecessarily.
5. **The statutory stray hold clock runs independent of how abandoned the animal looks.** The hold period exists to give an owner a real chance to reclaim; fast-tracking an apparently unclaimed animal to adoption or euthanasia before the hold expires is a procedural violation even when the outcome would have been identical.

## Mental models & heuristics

- **When a bite involves a captured rabies vector species (raccoon, skunk, fox, bat, coyote), default to euthanizing and submitting for testing rather than quarantining** — no validated quarantine period exists for RVS, so holding one for observation doesn't answer the rabies-status question the way it does for a dog, cat, or ferret.
- **When a bitten dog, cat, or ferret has current rabies vaccination, no signs of illness, and no prior bite on file, default to home quarantine; a prior bite history or an owner who can't secure the animal moves it to facility quarantine** — facility is the fallback for elevated risk, not the default for every bite.
- **When grading bite severity for a report or classification referral, default to Dunbar's 6-point bite scale over a subjective "minor/major" label** — Level 1–2 (no puncture) and Level 3+ (puncture, possible tearing) route to different statutory tracks in most ordinances, and a subjective label doesn't map to either cleanly.
- **Named benchmark: the 90% live-release "no-kill" threshold — useful as a shelter-wide save-rate target next to intake volume, garbage-in when applied animal-by-animal as a reason to hold a genuinely dangerous or suffering individual past what the documented protocol calls for.**
- **When working a suspected cruelty/neglect complaint, default to documenting body-condition score and environmental conditions with dated photographs before removal, unless the animal is in immediate medical crisis** — the removal is the point most likely to be challenged later, and on-scene documentation is what supports it in a hearing.
- **When a call involves livestock or an exotic/venomous species at large, default to requesting a specialized-response unit or partner (large-animal vet, wildlife rehabber) rather than adapting standard dog-handling technique** — the equipment and species knowledge for a loose bull or an escaped python is a different skill set, not a scaled-up version of a catch pole.
- **When an owner disputes a dangerous-dog classification, default to building the hearing record from bite reports, medical records, and witness statements rather than the animal's demeanor at the hearing** — a dog can sit calmly in a hearing room and still meet every statutory element for classification based on the incident record.

## Decision framework

1. Secure the scene and confirm no ongoing injury risk before engaging the animal — a bite victim's medical needs come before capture or classification work.
2. Identify the species; if a bite occurred, grade severity on the Dunbar scale and determine whether the animal is a rabies vector species.
3. Set the rabies-exposure protocol: RVS captured → euthanize and submit for testing; domestic species → confirm vaccination status and bite history to set quarantine location (home vs. facility) and start the 10-day clock.
4. Pull the animal's and owner's incident history from the department record system before deciding on citation or classification referral — identical bite severity routes differently for a first-time versus repeat incident.
5. Select the restraint/capture method by species, temperament, and environment, not habit; disengage and call for specialized support if the situation exceeds standard equipment.
6. Document the scene before leaving — photographs, witness statements, bite location and severity, vaccination and registration status — this record is what a hearing or prosecution runs on later, not memory.
7. Route the case (citation, dangerous-dog hearing referral, cruelty investigation, or close-out) and calculate the specific fee, fine, and registration exposure tied to that route rather than estimating a generic penalty.

## Tools & methods

Catch pole and snare pole, humane box trap, catch net, chemical capture (dart) for large/dangerous animals via specialized units, body-condition scoring (the Purina/WSAVA 9-point BCS) for cruelty documentation, the Dunbar bite scale, shelter/incident record systems (e.g., Chameleon, PetPoint), rabies vector species list maintained by the state health department, quarantine agreement forms, AVMA-acceptable euthanasia method reference. Filled worksheets and calculation tables live in `references/playbook.md`.

## Communication style

To a pet owner in the field: plain, non-adversarial explanation of what's legally required and why — most compliance is voluntary and an escalated tone produces resistance where a clear one produces cooperation. To dispatch or patrol: concise status and threat-level updates, not narrative. To a hearing officer or prosecutor on a dangerous-dog or cruelty referral: lead with the statutory elements met and the documentation chain, the way a report has to stand alone as the case file. To shelter medical/behavior staff: lead with specific findings against protocol criteria (bite severity, medical prognosis, behavioral test result), not a personal impression of the animal.

## Common failure modes

- Treating provocation as grounds to skip or shorten the rabies-exposure quarantine clock, when provocation is a citation question decided separately from the exposure protocol.
- Waiting for a second bite before considering dangerous-dog classification, missing that most ordinances classify on the first skin-breaking bite.
- Reaching for the familiar tool — catch pole on everything, or bare hands on a "friendly-looking" stray — instead of matching the method to species, temperament, and environment.
- Cutting the statutory stray hold short because an animal looks unclaimed or abandoned, when the hold clock is a procedural requirement independent of appearance.
- Overcorrection after one bad euthanasia decision or public complaint: holding every borderline animal indefinitely instead of working the documented protocol, which just relocates the harm into an overcrowded shelter with no better outcome for the animal.

## Worked example

A resident's Rottweiler mix bites a delivery driver on the forearm during an off-leash yard delivery. Officer response: dog is current on rabies vaccination (booster given 8 months ago, 3-year vaccine), microchipped, and the department's record system shows one prior incident 14 months ago — an unprovoked nip during a leash walk that did not break skin.

Naive read: "First bite that broke skin — that's a leash citation, maybe a $150 fine, and we'll see if it happens again before calling it a dangerous dog."

Expert reasoning: the current bite is graded Dunbar Level 4 (puncture with tearing, four stitches required) — under this jurisdiction's representative ordinance structure, any single unprovoked bite that breaks skin already meets the statutory threshold for a dangerous-dog classification referral; the prior incident doesn't need to "count" toward a two-strikes rule because the two-strikes track is for non-skin-breaking aggression, and this case never needed that track. Because the dog has a prior bite on file, elevated-risk criteria route the quarantine to the shelter facility rather than the owner's home, despite current vaccination.

Quarantine: facility board, $28/day × 10 days = **$280**.
Citation, animal at large / bite incident (first documented at-large citation on this address): **$200**.
Dangerous-dog registration, annual (pending hearing outcome): **$150**.
Rabies booster: not required — vaccination current, no additional cost.

Fee subtotal: $280 + $200 + $150 = **$630** — before any ongoing compliance cost (6-foot secure enclosure, muzzle-in-public requirement, and a $100,000 liability bond most ordinances require once a dog is classified, none of which is a one-time fee). The naive $150 estimate misses the classification referral entirely and understates first-contact financial exposure by more than 4×.

Deliverable (incident report excerpt, routed to the dangerous-dog hearing docket):

> **ANIMAL CONTROL INCIDENT REPORT — Case #AC-24-1187**
> Subject animal: Rottweiler mix, microchip #985141000234567, owner [name/address].
> Incident: unprovoked bite to right forearm of delivery driver, off-leash in owner's yard. Bite graded Dunbar Level 4 (puncture with tearing, 4 sutures) per attending ER documentation.
> Rabies status: current (vaccination 8 months prior, 3-year product). Quarantine: facility, Day 0–10, elevated-risk track due to prior incident on file (Case #AC-23-0342, non-skin-breaking, 14 months prior).
> Statutory basis for dangerous-dog referral: single unprovoked bite breaking skin meets classification threshold independent of prior incident.
> Fees assessed: quarantine board $280 (10 days @ $28), at-large citation $200, dangerous-dog registration $150. **Subtotal: $630**, plus post-classification containment and $100,000 liability bond requirement pending hearing outcome.
> Hearing scheduled per notice to owner; record includes ER documentation, prior incident report, and scene photographs.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled bite-response worksheet, rabies-quarantine decision table, and fee/fine calculation tables.
- [references/red-flags.md](references/red-flags.md) — signals a case needs a second look before it proceeds, with the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (RVS, quarantine tracks, bite scale, BCS).

## Sources

National Animal Care & Control Association (NACA) Training Standards & Certification Academy curriculum (Level I–III officer training); *AVMA Guidelines for the Euthanasia of Animals: 2020 Edition* (American Veterinary Medical Association); *Compendium of Animal Rabies Prevention and Control*, National Association of State Public Health Veterinarians (NASPHV, published annually) — source for the 10-day domestic-bite observation period and the no-valid-quarantine rule for rabies vector species; Dr. Ian Dunbar's dog bite assessment scale, widely adopted in animal-behavior and bite-response training; *Animal Control Management: A New Look at a Public Responsibility*, Mark Kumpf (ICMA); CDC rabies post-exposure guidance; Purina/WSAVA 9-point body condition scoring system as used in cruelty-case documentation. Specific dollar figures, fee schedules, and classification-threshold structures in the worked example are illustrative of representative municipal-ordinance patterns, not a universal figure — actual fee schedules and statutory thresholds vary by jurisdiction and must be checked against the specific local code in force.
