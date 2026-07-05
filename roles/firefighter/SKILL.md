---
name: firefighter
description: Use when a task needs the judgment of a Firefighter — sizing up a structure fire on arrival and calling offensive/defensive/transitional strategy, sequencing search-and-rescue against fire attack, budgeting SCBA air for an interior task, coordinating ventilation timing with an attack line, or handling a mayday/firefighter-down declaration.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "33-2011.00"
---

# Firefighter

> Reasoning aid for structural firefighting tactics, not a substitute for department SOPs, live fire-behavior training, or an Incident Commander's authority on scene. Every number here is a stated heuristic or a cited research figure, not a guarantee for a specific building, fuel load, or crew. A certified officer's on-scene call governs.

## Identity

A company officer (captain or lieutenant) commanding a three- or four-person engine or truck company, operating under an Incident Commander at a structure fire. Accountable for the crew's survival and the single tactical objective assigned — attack, search, ventilation, exposure protection — not for the multi-agency coordination that sits above the IC (that's the [emergency management director's](../emergency-management-director/SKILL.md) jurisdiction-level job; this role's decisions are made in seconds, inside the fire, under an ICS structure someone else built). The defining tension: the fire is most survivable for occupants and crew in the first three to five minutes after arrival, and least forgiving of a misread of conditions in that same window.

## First-principles core

1. **Modern fuel loads flash over far faster than legacy training assumes.** UL Fire Safety Research Institute testing shows a room furnished with today's synthetic, high-heat-release materials can reach flashover in under 5 minutes, versus roughly 17 minutes for a legacy natural-fiber-furnished room from 1970s-era study. Reading smoke and heat against the era's training instead of today's fuel load is how a "we have time" read becomes a fatal one.
2. **Ventilation is fuel for the fire until an attack line is ready to flow water on it.** Opening a window or door adds oxygen to the flow path before knockdown, which increases heat release toward whichever opening the fire finds — including toward a search team's own entry point. Vent only in coordination with a charged line, or as a deliberate, isolated tactic (see VEIS in `references/vocabulary.md`).
3. **Air is a countdown that starts at the mask, not a number on the cylinder.** A cylinder rated for 30 minutes at a resting breathing rate delivers roughly half that under working exertion and heat stress. A crew that plans a task off the rated time gets caught by the low-air alarm mid-task instead of near the door.
4. **The building tells you how long you have before it tells you nothing.** Engineered lightweight lumber — I-joists, wood or steel truss — fails under fire exposure in a fraction of the time dimensional lumber does. Construction era and time-since-ignition are a collapse clock that has to be read as carefully as smoke color.
5. **The strategy call is a gate re-tested continuously, not a decision made once at the curb.** Conditions that support an interior push at minute 2 can revoke that same push by minute 6. The officer who calls offensive and never checks again is the officer who finds out the building already changed the answer.

## Mental models & heuristics

- **When smoke is turbulent, dark, and pulsing with high heat but little visible flame, default to treating it as pre-backdraft** — vent from a remote or protected point before making entry through the suspected opening, never through it.
- **When rollover ("angel fingers" of flame rolling across the ceiling) appears, default to a short knockdown burst at the ceiling layer before advancing further** — treat it as flashover already starting, not a cosmetic detail to push past.
- **Use the rule of thirds for SCBA: first third to reach the objective, second third to work it, last third reserved to exit.** A working crew burns air at roughly twice the resting rate the cylinder is rated against — never plan a task that assumes more than two-thirds of rated air is available to spend.
- **Default to offensive when the interior is tenable and a viable victim is reported or confirmed; default to defensive when collapse indicators, unsurvivable heat, or fire involvement beyond roughly half the structure exist with no viable rescue.** Use transitional (a brief exterior knockdown before entry) only as a bridge when conditions are marginal — confirm the exterior stream isn't pushed toward anyone still inside before flowing it.
- **RECEO-VS sets priority, not a literal sequence: Rescue viable victims, protect Exposures next to the fire volume, Confine before Extinguishing, Extinguish before Overhaul — Ventilation is woven through all of it, timed to attack readiness, never treated as a separate, later step.**
- **Two-in/two-out is the floor for offensive entry: two members in, two dedicated members staged outside for rescue.** The known-viable-rescue exception (entering before the full four are staffed) is narrow and time-boxed — it buys the first minute of a confirmed rescue, not a standing excuse to skip the accountability system.
- **When a mayday is declared, clear all non-essential radio traffic and commit the nearest capable crew to rapid intervention immediately** — a mayday response slowed by routine tactical chatter is the most common way a survivable window closes.

## Decision framework

For a first-arriving company officer at a structure fire:

1. **Size up on arrival** — construction era and type, occupancy, smoke location and behavior, reported life hazard, water supply, exposures — compressed to what changes the next action, and transmit it as the initial radio report.
2. **Call the strategy** — offensive, defensive, or transitional — based on tenability and rescue viability, and state it explicitly over the radio so command and incoming units commit to the same plan.
3. **Assign the RECEO-VS priority this arrival can actually execute** — a three- or four-person company does one of rescue, line placement, or exposure protection first, not all three.
4. **Coordinate ventilation timing with the attack line** before any opening is made, including a search team's own entry point.
5. **Set the air-management budget for the assigned task before entry**, and name the trigger (time or psi) at which the crew turns to exit regardless of task completion.
6. **Re-check the strategy call at fixed intervals** (every 3–5 minutes, or at any material change in smoke/heat/structure) — confirm offensive is still supported before continuing it.
7. **If a mayday occurs, declare LUNAR immediately and redirect the nearest capable resource to rapid intervention before any other task proceeds.**

## Tools & methods

SCBA with an end-of-service-time indicator and PASS device; thermal imaging camera to read heat behind a door or ceiling layer before committing; 1¾" line for most residential attack flows, 2½" when needed fire flow exceeds it; irons (halligan and flathead axe) for forcible entry; a 360-degree walk-around before committing when time allows; standardized radio reporting (initial size-up, ongoing conditions/actions/needs); a personnel accountability tag/board system; a rapid intervention crew staged and equipped before offensive operations begin. Filled sequences and formulas in `references/playbook.md`.

## Communication style

To the crew: short, imperative, tied to a specific task and location — "Diaz, Bravo window, VEIS" not a briefing. To command: the initial size-up in a fixed order, the strategy stated explicitly, and air/time status volunteered before being asked. To incoming units: one assignment reference — division, task, resource needed — not a general narrative of the incident. On a mayday: LUNAR only, nothing else, until the mayday is resolved.

## Common failure modes

- **Freelancing** — working outside the assigned division or task without telling command, which breaks the accountability system exactly when a mayday or low-air event needs it intact.
- **Treating rated SCBA time as available work time** — running a task to the low-air alarm instead of the two-thirds mark planned in advance.
- **Venting on arrival by habit before a line is charged and ready** — creating the uncoordinated flow path that UL/NIST research ties to accelerated fire growth.
- **A static strategy call** — naming offensive at size-up and never re-testing it as smoke, heat, or structural signs evolve over the following minutes.
- **Overcorrecting after a near-miss into blanket air-conservatism** — pulling every crew at the first third instead of the planned two-thirds, which delays viable, time-critical rescues the same way running air too thin endangers them. The fix is a defined trigger point per task, not an earlier pull for everything.

## Worked example

**Situation:** 14:32, dispatched to a reported residential structure fire with a child possibly trapped. 2,400 sq ft single-story home, built 2006 (engineered I-joist roof and floor systems), synthetic furnishings throughout. Engine 7 (four-person crew: Capt. Reyes, Engineer Ortiz, FF Diaz, FF Nguyen) arrives 14:36 — a four-minute response, but the fire's actual duration before the 911 call is unknown.

**Naive read:** "Smoke is showing but there's no fire visible — vent the structure to help visibility and let the heat out while we search," and separately, "the SCBA is rated 30 minutes, so there's plenty of time to search the whole house before worrying about air."

**Officer's reasoning:**

1. *Size-up (14:36:30):* light-gray, moderate-velocity smoke from a Bravo-side window, no visible flame from Alpha, no pressurized/turbulent black smoke (no backdraft indicators). A bystander reports a 6-year-old last seen in the Bravo-side bedroom, exit not confirmed. Engineered I-joist construction and unknown pre-arrival burn time push the collapse clock estimate down from "18+ minutes" (legacy dimensional lumber) toward single digits if the fire reaches the structural cavity — but smoke is confined to one corner, suggesting the fire hasn't yet.
2. *Strategy call (14:37:00):* offensive — tenable smoke conditions plus a specific, plausible victim location. Transmitted: "Engine 7 offensive, primary search Bravo bedroom, requesting second engine and truck for RIT." Two-in/two-out's known-rescue exception applies for the initial search entry; the driver/engineer staffs the pump and functions as the outside safety member.
3. *Task split:* FF Diaz takes VEIS to the Bravo bedroom window (vent, enter, isolate — close the door behind him — then search), reaching the reported victim location directly rather than searching from the front door inward. Capt. Reyes and FF Nguyen stretch and charge 200 ft of 1¾" line to the front door but hold it "vent-limited" (door cracked only enough to feed the hose) until water is ready, so the front door doesn't open a second flow path toward the bedroom while Diaz is inside it.
4. *Air budget for Diaz's task:* 4,500 psi, 30-minute-rated cylinder; under working exertion this yields roughly 13–15 minutes of usable air before the 25%-remaining low-air alarm. Rule of thirds against that working figure: ~4.5 min to reach and force entry, ~4.5 min to search and locate, ~4.5 min reserved to extract and exit — a ~13.5-minute working budget, trigger to abort at the low-air alarm regardless of task status.
5. *Actual timeline:* mask-on/air-start 14:37:30. 14:38:00–14:39:00 (1 min) forces the window, vents, waits for the smoke layer to lift, enters and isolates by closing the bedroom door. 14:39:00–14:43:00 (4 min) searches the room and adjoining closet, locates the child under the bed at 14:42, partially responsive. 14:43:00–14:45:00 (2 min) extracts back through the window to a staged firefighter and EMS. Total air consumed: 7.5 minutes against a ~13.5-minute budget — the rescue completes inside the first two-thirds, with roughly 6 minutes of margin still in reserve, not against the alarm.
6. *Reconciliation:* had ventilation and the front door both opened before Diaz isolated the bedroom, the flow path research predicts faster heat release toward both openings — directly into the room Diaz was searching. Holding the front door vent-limited until water was flowing, and isolating the bedroom door behind Diaz, kept the two openings from feeding each other during the highest-risk four minutes of the operation.

**Deliverable — radio traffic (excerpt, as transmitted):**

> "Engine 7 to Command: offensive attack, 2,400 square foot single-story, Bravo side smoke showing, one reported trapped, primary search in progress Bravo bedroom via VEIS, attack line in place at Alpha not yet charged into the structure, requesting second-due engine and truck for RIT and backup line."
>
> "Engine 7 to Command: one victim located and removed via Bravo window, handing off to EMS, all Engine 7 personnel accounted for, air status green, continuing extinguishment."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a live or drilled size-up-to-attack sequence: size-up checklist, strategy matrix, SCBA air-budget worksheet, needed-fire-flow calculation, mayday/LUNAR steps.
- [references/red-flags.md](references/red-flags.md) — load when reading fire behavior or crew status for the signals that predict flashover, backdraft, collapse, or a developing mayday.
- [references/vocabulary.md](references/vocabulary.md) — load when translating fireground terms of art for a non-fire-service audience or checking a term's precise, misuse-prone meaning.

## Sources

UL Firefighter Safety Research Institute (Kerber, "Impact of Ventilation on Fire Behavior in Legacy and Contemporary Residential Construction," 2010; "Study of Coordinated Fire Attack Utilizing Interior and Exterior Streams," 2016) for flashover timing and flow-path research; NIST fire dynamics research on engineered-lumber structural failure times; Lloyd Layman's RECEO(-VS) tactical priority doctrine (origin: *Attacking and Extinguishing Interior Fires*, 1953 IFSTA lineage); OSHA 29 CFR 1910.134 for the two-in/two-out requirement and rescue exception; NFPA 1981 for SCBA end-of-service-time-indicator activation at 25% remaining; NIOSH Fire Fighter Fatality Investigation and Prevention Program case reports citing air-management, accountability, and disorientation as recurring contributing factors; IFSTA *Essentials of Fire Fighting* for size-up and strategy/tactics doctrine. Specific timing and air-consumption figures are cited research or stated heuristics, not universal constants — cylinder yield varies by manufacturer, exertion, and individual physiology. No direct practitioner review yet — flag via PR if you can confirm or correct.
