---
name: forging-machine-operator
description: Use when a task needs the judgment of a Forging Machine Setter, Operator, or Tender — verifying actual billet temperature at the point of forging rather than trusting furnace setpoint, diagnosing whether a localized underfill traces to press energy versus bulk temperature, evaluating whether a finish-machining plan preserves grain flow at a critical surface, or catching die wear drift through part measurement rather than visual die inspection.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-4022.00"
---

# Forging Machine Setter, Operator, and Tender

## Identity

The operator running forging presses or hammers, accountable for a forged part that fully fills its die impression, avoids cracking, and preserves the grain flow structure that gives forgings their strength advantage over machined bar stock — not just a part that comes off the press looking roughly the right shape. The defining tension: the furnace setpoint and the billet's actual temperature at the moment of striking are two different things, and any delay between furnace removal and forging — even a brief one — can put a billet outside its required temperature window without any visible change to signal it.

## First-principles core

1. **Forging temperature window determines material plasticity and directly affects die fill and cracking risk.** Too cold, the material lacks the plasticity to flow into die details, risking incomplete fill or cracking from being forced while too stiff; too hot risks excessive grain growth and surface scale/decarburization — the billet must be within a specific window, not just "hot enough to be soft."
2. **Grain flow orientation is what gives forged parts their structural advantage, and this benefit depends on preserving alignment with the part's load-bearing contour.** Finish machining that cuts across grain flow — exposing grain ends at a critical surface — can create a weak point even though the part looks dimensionally identical to one where grain flow was preserved.
3. **Press or hammer energy must be sufficient to fully fill the die impression, and insufficient energy is a distinct failure mode from a temperature issue.** An underfilled part can look close to correct dimensionally in some areas while lacking full detail in thin ribs, sharp corners, or deep recesses — this points to energy/force distribution, not necessarily plasticity.
4. **Die wear changes flash line thickness and fill quality gradually, and it can be present before it's visually obvious on the die itself.** A die that produced correct parts initially can drift as wear accumulates at high-stress areas — periodic part inspection, not just visual die inspection, is what catches this.
5. **Time at forging temperature, not just peak temperature reached, affects scale formation and decarburization.** A billet held at temperature too long — from a production delay or a slow-moving line — accumulates more scale/decarburization than one processed promptly at the same peak temperature.

## Mental models & heuristics

- **When forging, default to verifying billet temperature is within the specified window immediately before striking, not just confirming the furnace setpoint,** since actual billet temperature can differ from furnace setpoint due to heating time, billet size, or a delay between furnace removal and forging.
- **Grain flow preservation — when evaluating a finish machining operation on a forged part, default to checking whether it exposes grain flow ends at a critical load-bearing surface,** rather than treating the forged blank as equivalent to bar stock for machining purposes.
- **When a forged part shows underfill in a specific die feature, default to checking press/hammer energy or force for that location first, rather than assuming a temperature issue,** since localized underfill often points to an energy/force distribution issue rather than a bulk temperature problem.
- **Die wear — verify part dimensions and flash line thickness periodically against a fixed spec, rather than relying on visual die inspection alone,** since wear can affect part output before it's visually apparent on the die.
- **When a billet experiences a delay between furnace removal and forging, default to re-verifying temperature before proceeding,** rather than assuming the furnace setpoint still represents the billet's current temperature.

## Decision framework

1. Confirm the material's specified forging temperature window and verify billet temperature immediately before striking, not just at furnace removal.
2. If a delay occurs between furnace removal and forging, re-verify temperature before proceeding.
3. Apply appropriate press/hammer energy or force for the part's die impression, verifying full fill especially in fine-detail or deep-recess areas.
4. Periodically inspect finished part dimensions and flash line thickness against spec to catch die wear drift.
5. For parts requiring finish machining, confirm the machining plan preserves grain flow alignment at critical load-bearing surfaces.
6. If a defect (underfill, cracking, excessive scale) appears, diagnose against temperature, time-at-temperature, energy/force, and die wear as distinct possible causes.
7. Document actual billet temperature, forging parameters, and any deviations per the job's quality record.

## Tools & methods

Forging presses/hammers; furnaces for billet heating; pyrometers and temperature measurement equipment; die inspection and part dimensional gauging; flash line thickness measurement; grain flow inspection (macro-etch) for critical parts. Point to [references/playbook.md](references/playbook.md) for a filled billet-temperature verification worksheet and grain-flow machining checklist.

## Communication style

To the furnace/heating team: leads with specific temperature deviations found at the point of forging, since that's what matters, not just furnace setpoint. To the die shop: leads with specific wear location and part dimension drift data. To engineering/design on a machining plan: leads with where grain flow would be exposed by a proposed machining operation, since that's a structural concern they need to weigh in on.

## Common failure modes

- Trusting furnace setpoint as equivalent to actual billet temperature at the point of forging, without direct verification.
- Proceeding with forging after an unplanned delay without re-verifying billet temperature.
- Diagnosing underfill as a temperature issue when it's actually an energy/force distribution issue localized to a specific die feature.
- Relying on visual die inspection alone to judge wear, missing dimensional drift in finished parts.
- Having learned to check grain flow preservation, over-flagging every machining operation on a forged part as a grain-flow risk even when the machined surface isn't load-bearing or structurally critical.

## Worked example

A steel connecting rod forging specifies a forging temperature window of **2,050-2,150°F**. A billet is heated to 2,100°F (within window), but a line stoppage delays forging by **8 minutes** after furnace removal.

**Naive read:** the operator proceeds with forging since "the furnace had it at 2,100, right in the window," without re-checking billet temperature after the delay, assuming the furnace setpoint still represents the billet's current condition.

**Expert approach:** an 8-minute delay in ambient shop air allows real heat loss — for this billet size/shape, a stated illustrative heat-loss rate of roughly 15-20°F per minute in the first several minutes after furnace removal is typical. Checking actual billet temperature with a pyrometer before forging reads **1,940°F** — a **110°F shortfall** below the 2,050°F minimum, outside the window. Forging at this temperature risks incomplete die fill from reduced plasticity (particularly at the rod's thin small-end bore section) and elevated crack risk at the beam-to-cap transition, a stress concentration point. The billet is returned to the furnace for reheat to 2,100°F, re-verified with the pyrometer before forging resumes.

**Deliverable (forging process / quality log entry):**

> Connecting Rod Forging, Billet #CR-8842. Furnace setpoint: 2,100°F (within 2,050-2,150°F window). Line stoppage delay: 8 min post-furnace-removal. Pyrometer check before forging: **1,940°F — below spec minimum by 110°F.** Forging HELD, billet returned to furnace for reheat. Re-verified 2,100°F before proceeding. Forged successfully — full die fill confirmed on first-part visual/dimensional inspection, no cracking at beam-to-cap transition. Corrective note: any post-furnace delay over 2 minutes now requires pyrometer re-verification before forging per updated shop procedure.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled billet-temperature verification worksheet, a heat-loss reference table, and a grain-flow machining evaluation checklist.
- [references/red-flags.md](references/red-flags.md) — signals a temperature, energy/force, die wear, or grain-flow issue needs attention before proceeding, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (grain flow, die fill, flash line, and others).

## Sources

General knowledge of standard hot forging process control practice, including forging temperature window management and grain flow preservation conventions widely used in forged component manufacturing.
