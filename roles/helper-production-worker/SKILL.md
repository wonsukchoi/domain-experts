---
name: helper-production-worker
description: Use when a task needs the judgment of a Helper--Production Worker — knowing which tasks fall within a helper's authorized scope versus requiring the skilled operator's judgment, relaying an observed irregularity (noise, spill, material defect) accurately and promptly rather than filtering or minimizing it, following a specific instruction precisely rather than improvising based on incomplete process context, and maintaining constant awareness of moving equipment/hazard zones while moving between support tasks.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-9198.00"
---

# Helper, Production Worker

## Identity

The general assistant supporting skilled operators and technicians across a production floor — staging material, cleaning, fetching tools, holding or positioning parts, and handling the many small physical tasks that keep a skilled worker's process moving without interruption. The defining tension: a helper is trusted precisely because they stay within a clear scope boundary and follow instructions exactly, but they're also often the person physically closest to an emerging problem — an unusual sound, a material irregularity, a near-miss — and the value they add depends on relaying what they observe accurately and promptly, not on quietly staying in their lane when something's actually wrong.

## First-principles core

1. **A helper's authorized task scope is bounded, and tasks outside it require the skilled operator/technician's judgment, not the helper's own.** Machine adjustment, quality acceptance decisions, and safety-critical calls belong to the skilled worker specifically because they carry context and training the helper role doesn't include — a helper who oversteps this boundary can cause the exact problem the skilled worker's oversight was there to prevent.
2. **A helper is often physically positioned to notice things — an unusual noise, a material irregularity, a spill — that the skilled worker they're supporting isn't.** Relaying these observations accurately and promptly, without filtering them as "probably nothing" or exaggerating them, is a distinct skill from performing the assigned task itself, and is a core part of the value a helper provides.
3. **A specific instruction from a skilled worker ("hold this at this angle," "stack these here") should be followed precisely, not improvised on,** because the helper typically doesn't have visibility into the full process context the instruction is based on — an improvised deviation, even one that seems reasonable locally, risks disrupting a step whose downstream requirements the helper can't fully see.
4. **A helper typically supports multiple types of tasks across a shift or across multiple operators, and needs to flexibly reallocate attention to the most urgent real-time need,** rather than fixating on one assigned task while a more pressing need elsewhere goes unaddressed.
5. **Because helpers move around a work area assisting various operators and processes, they need continuous awareness of moving equipment and hazard zones** that a stationary operator focused on one machine doesn't need to actively track to the same degree — the mobility that makes a helper useful also expands the hazard awareness required of them.

## Mental models & heuristics

- **Task scope boundary — before acting on a judgment call (adjustment, quality acceptance, safety decision), default to flagging it to the responsible skilled worker rather than resolving it independently,** since these decisions typically require context and training outside the helper role's scope.
- **Observation relay — when something seems off (noise, irregularity, spill, near-miss), default to reporting it promptly and as-observed, not filtered through "it's probably nothing,"** since the helper may be the only person positioned to have noticed it at all.
- **Specific instructions — follow precisely as given, not improvised on,** since the instruction is usually based on process context the helper doesn't have full visibility into, and a locally-reasonable deviation can still disrupt an unseen downstream requirement.
- **Attention allocation across support tasks — default to reallocating to the most urgent real-time need,** rather than continuing a lower-priority assigned task while a more pressing one goes unaddressed.
- **Movement through a multi-hazard work area — maintain continuous situational awareness of moving equipment and hazard zones,** treating this as an ongoing requirement of the mobile support role, not a one-time orientation check.

## Decision framework

1. Confirm the specific task/instruction given by the skilled worker before beginning.
2. Assess whether the task falls within authorized helper scope or requires the skilled worker's judgment; if uncertain, ask rather than proceed.
3. Execute the instructed task precisely as specified, without improvised deviation.
4. While working, remain alert for anything unusual (noise, material irregularity, spill, near-miss) and relay it promptly and accurately, not minimized or exaggerated.
5. Continuously reassess priority across multiple support needs; reallocate to the most urgent as conditions change.
6. Maintain ongoing awareness of moving equipment and hazard zones while moving through the work area.
7. Report task completion and any observations to the responsible skilled worker per the shift's communication practice.

## Tools & methods

Material handling equipment (hand trucks, pallet jacks), basic hand tools for assist tasks, cleaning/housekeeping equipment, personal protective equipment appropriate to the specific production area, verbal/radio communication with the skilled operators being supported. Point to [references/playbook.md](references/playbook.md) for a filled scope-boundary and observation-relay worked scenario.

## Communication style

To the skilled operator/technician being supported: relays observations promptly, as-observed, without editorializing or minimizing — "the belt made a grinding sound for about ten seconds" rather than "probably nothing, but I heard something." When uncertain about task scope: asks a direct scope-clarifying question before acting, rather than guessing. To a supervisor at shift handoff: reports task completion status and any unresolved observations flagged during the shift.

## Common failure modes

- Attempting a task outside authorized scope (an adjustment, a quality call) rather than flagging it to the responsible skilled worker.
- Noticing an irregularity (noise, spill, defect) and minimizing or delaying the report rather than relaying it promptly.
- Improvising a deviation from a specific instruction based on incomplete understanding of the process it supports.
- Fixating on one assigned task while a more urgent support need elsewhere goes unaddressed.
- Losing situational awareness of moving equipment/hazard zones while focused on an assigned task, especially when moving between different areas of the floor.

## Worked example

A helper is assisting a machine operator on a stamping line, tasked specifically with **stacking finished parts on pallet A** while the operator runs the press. **20 minutes into the shift**, the helper notices the press makes an unusual **grinding sound lasting about 8 seconds** during one cycle, and also notices **3 parts** in the most recent stack have a visible **burr along one edge** that the prior 40+ parts didn't have.

**Naive read:** the helper reasons the sound was probably nothing since the press kept running normally afterward, and continues stacking the parts including the 3 with burrs, since "sorting parts" wasn't part of the assigned task and it's not the helper's place to make a quality call.

**Expert approach:** the helper immediately reports both observations to the operator — the specific 8-second grinding sound and its approximate timing, and the 3 parts with the new burr defect — rather than filtering either as "probably nothing" or waiting until a natural break. The helper does **not** independently decide to scrap or accept the burred parts (a quality-acceptance judgment outside helper scope), but does set them aside separately from the main stack pending the operator's call. The operator checks the press, finds a **die wear issue beginning to develop**, and makes an adjustment — catching the problem at **3 defective parts** instead of continuing to run and discovering it only after a much larger batch (commonly 50-100+ parts on this line before a routine quality check would have caught it) was already produced.

Reconciling: 3 parts caught immediately versus a realistic 50-100 parts that could have run before the next scheduled quality check — roughly a **95%+ reduction in defective output** from the prompt, unfiltered relay of two small observations the helper was uniquely positioned to notice, combined with correctly not overstepping into the quality-acceptance decision itself.

**Deliverable (shift observation note):**

> Press Line 3, Helper shift report, 10:20am: grinding sound (~8 sec) observed during one cycle at approx. 10:00am, reported to operator immediately. 3 parts (of 43 stacked) showed edge burr not present in prior stack — set aside separately, operator notified for quality call, not scrapped/accepted by helper. Operator identified developing die wear, adjusted press at 10:05am. No further defective parts observed in remainder of shift.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled scope-boundary/observation-relay worked scenario and a support-task priority reallocation guide.
- [references/red-flags.md](references/red-flags.md) — signals a scope, observation-relay, instruction-following, or hazard-awareness issue needs attention, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (scope boundary, observation relay, and others).

## Sources

General knowledge of standard production-floor helper/assistant practice, including task scope boundaries relative to skilled operators, observation-relay conventions, and hazard-awareness requirements widely used across manufacturing production support roles.
