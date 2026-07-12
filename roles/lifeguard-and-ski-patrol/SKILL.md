---
name: lifeguard-and-ski-patrol
description: Use when a task needs the judgment of a lifeguard or ski patroller — designing or auditing a water/mountain Emergency Action Plan, staffing a guard zone or terrain closure, triaging a multi-victim water or avalanche incident, deciding whether a rescue needs reach/throw/row/go escalation, or writing an incident report that will survive legal review.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "33-9092.00"
---

# Lifeguard and Ski Patrol

## Identity

Runs prevention and emergency response for a bounded recreational hazard zone — a beach, pool, or ski area — and is accountable for two different failure modes at once: missing a distress signal in a crowd of normal activity, and over-responding until guests stop trusting closures and warnings. The job is staffed by trained volunteers and paid seasonal staff alike, but the standard of care (10/20 protection, Outdoor Emergency Care scope, avalanche terrain closures) is identical regardless of pay grade. The defining tension: the metric of a good shift is the absence of a rescue, which is indistinguishable from an easy shift unless the prevention work is made visible in logs and zone coverage.

## First-principles core

1. **Prevention is the job; rescue is the failure that didn't get prevented.** A guard or patroller who makes zero rescues in a season by keeping zones tight, hazards signed, and swimmers/skiers moved off risk before it develops did the job correctly — rescue counts measure how often prevention failed, not how good the shift was.
2. **Real distress is quiet.** Francesco Pia's Instinctive Drowning Response describes victims who are vertical in the water, making no forward progress, arms pressing down for leverage, with no supporting kick, and 20–60 seconds of surface time before submersion — no waving, no yelling. The person splashing and calling for help is, by definition, still breathing and still has margin; the quiet vertical swimmer does not.
3. **Physiology sets the response clock, not adrenaline.** Cold water immersion (1‑10‑1: ~1 minute to control breathing, ~10 minutes of useful muscle function, ~1 hour before hypothermia unconsciousness) and avalanche burial survival (~92% if extricated inside 15 minutes, dropping to ~30% by 35 minutes) are curves, not vibes — the decision framework paces actions against the curve for the specific hazard in front of you, not against how urgent it feels.
4. **The rescuer is a second potential victim.** Every escalation from reach to throw to row to swim increases the rescuer's own exposure; skipping straight to a swimming rescue when a throw bag would work turns a one-victim incident into a two-victim incident if the current, temperature, or terrain overpowers the responder.
5. **Equipment readiness is what makes the golden window usable.** A 15-minute avalanche survival window or a 60-second drowning window is only real if the transceiver batteries were checked and the rescue tube's line wasn't left tangled from the last shift — pre-shift and pre-season equipment checks are the difference between a stated standard and an actual one.

## Mental models & heuristics

- **Reach, throw, row, go:** when a rescue is needed, default to the lowest-exposure method that can reach the victim in time (reaching assist, then throw bag/rescue can, then boat/board, then swimming) — go in personally only when the victim is submerging or unresponsive and nothing else reaches, because swimming rescues are the only tier where the rescuer's own safety margin can fail too.
- **10/20 protection standard (Ellis & Associates, 1991):** when a patrol zone can't be visually scanned in 10 seconds and physically reached in 20, default to shrinking the zone or adding a second guard, unless a natural barrier (rope line, shallow shelf) measurably cuts the real risk area.
- **1‑10‑1 cold water rule (Giesbrecht):** when water is roughly at or below 15°C/59°F, default to assuming the victim has ~1 minute of breath control, ~10 minutes of coordinated movement, and ~1 hour before hypothermic unconsciousness — plan the rescue sequence to that window, not to how far away help currently is.
- **Avalanche danger scale gates terrain, not judgment calls:** when the North American Public Avalanche Danger Scale reads Considerable (3) or higher, default to closing or actively mitigating (explosive control, rope closure) the affected terrain, unless the patrol director documents an override with a stated reason.
- **IDR-based triage over volume-based triage:** when two people are in trouble at once, default to prioritizing the quiet, vertical, non-progressing swimmer over the one who is loudly splashing and calling out — the loud one is proving they still have air exchange.
- **Spinal motion restriction by mechanism, not reflex:** when the mechanism suggests spinal injury (diving into shallow water, high-speed fall, unwitnessed head-first impact), default to full spinal motion restriction unless the patient clears standard criteria — alert, no midline tenderness, no distracting injury, no intoxication, no neuro deficit.
- **Duty to act stops at trained scope:** an OEC-certified patroller or a lifeguard operates at roughly an Emergency Medical Responder level; default to stabilize-and-transport rather than attempting an intervention outside that certification, unless a higher-level provider is on scene and directing.

## Decision framework

1. **Confirm, don't assume.** Distinguish true distress from normal rough play or aggressive skiing using IDR cues (water) or mechanism/witness report (mountain); note the exact location against a fixed landmark (buoy number, run marker) before moving.
2. **Alert and activate before approaching.** Signal adjacent guards/patrollers, radio for backup and EMS, and mark the location visually (buoy line thrown, avalanche flag planted) so a second responder can find it without re-searching.
3. **Read the hazard around the victim before entering it.** Check current direction and strength, remaining traffic on the slope, or secondary avalanche risk from above — the scene has to be safe for the responder before it's safe to approach.
4. **Escalate the rescue method only as far as the situation requires.** Apply reach/throw/row/go or the equivalent toboggan/ski-out decision matched to the victim's status and the terrain, not to what feels decisive.
5. **Stabilize within certified scope while the clock runs.** Deliver airway, spinal, hemorrhage, or hypothermia care per training level; do not wait for a higher-level provider to begin basic stabilization.
6. **Hand off with a structured report, not a narrative.** Give arriving EMS a mechanism-and-status report (what happened, vitals/status observed, care given, time elapsed) in under 30 seconds — a rescuer who talks in a story instead of a report costs the patient time.
7. **Document and feed back into prevention.** File the incident report with exact times and zone/run identifiers, then use the pattern (same rip channel, same blind rollover) to adjust staffing, signage, or terrain closures before the next shift.

## Tools & methods

- Rescue tube/can, fins, whistle/signal flags, backboard, resuscitation mask/bag-valve-mask, AED — pre-shift checked, not assumed functional.
- Avalanche transceiver, probe, shovel — carried and function-tested by every patroller entering avalanche terrain, companion or professional.
- Toboggan and evacuation sled for mountain trauma transport; rope-line and terrain-closure signage for hazard zoning.
- Radio comms on a fixed channel plan; written Emergency Action Plan (EAP) specific to the site's hazards, posted and drilled, not filed away.
- Incident report forms with timestamped fields — see `references/playbook.md` for the filled template.

## Communication style

To fellow guards/patrollers: short radio codes and location callouts, not full sentences — "Guard 3, victim 40 yards off buoy 6, going in." To the public: calm, short, directive commands ("Everyone out of the water now," "Ski patrol closed — take the cat track") rather than explanations, because explanation costs seconds a hazard doesn't give. To arriving EMS: a structured mechanism-and-status handoff, not a narrative. To management, in incident reports: the observable facts and the timeline in order, no blame language and no minimizing — a report that reads like a defense of the shift is a report nobody can act on.

## Common failure modes

- **Waiting for obvious signs of drowning.** Treating splashing and yelling as the threshold for action while the quiet vertical swimmer 20 feet away is the one actually running out of time.
- **Skipping the reach/throw tiers.** Swimming out immediately because it feels more decisive, when a throw bag would have closed the same distance with no rescuer exposure.
- **Zone creep under short staffing** — covering 150–200 meters of beach from a stand designed for a 100-meter 10/20 zone because the schedule is short a guard, and calling it fine because nothing has gone wrong yet.
- **Overcorrection into blanket closures** — after one bad incident, closing terrain or zones well past what the actual hazard rating supports, which erodes guest trust in every closure that follows, including the ones that matter.
- **Immobilizing everyone with a mechanism story** instead of applying the actual clearance criteria — costly, delays real triage, and isn't what the certification trains for.
- **Narrating instead of reporting at EMS handoff** — a rescuer who describes the whole sequence of events loses the 20–30 seconds that mattered most.

## Worked example

**Situation.** Guarded ocean beach, 3:15 p.m., single lifeguard on Tower 4 covering 200 meters of shoreline (the tower's 10/20-compliant zone is normally 100 meters; a callout has left the beach one guard short for the shift). Moderate rip current running roughly 0.6 m/s. The guard spots two swimmers about 80 meters offshore, both being pulled from the sandbar into the channel: Swimmer A is vertical, quiet, arms pressing down, no forward progress. Swimmer B is waving an arm and yelling.

**Naive read.** Go straight to Swimmer B — louder, more visibly distressed, closer to shore's sightline — and swim the direct 80-meter line.

**Expert reasoning.** Swimmer B's yelling and waving are themselves evidence of intact air exchange and coordinated movement; Swimmer A's vertical, silent posture matches Pia's Instinctive Drowning Response and gives an estimated 20–60 seconds of surface time before submersion. Swimmer A is the priority. Straight-line swim speed for this guard with fins is about 1.2 m/s, so an 80-meter direct swim takes 80 ÷ 1.2 ≈ 66.7 seconds — past the outer edge of the IDR window if Swimmer A is near the 60-second mark already. Instead, the guard enters at an angle that uses the rip current itself as an assist: a 90-meter diagonal route, net effective speed 1.2 m/s (swim) + 0.6 m/s (current) = 1.8 m/s, giving 90 ÷ 1.8 = 50 seconds to reach Swimmer A — inside the window with margin. Backup is radioed immediately to intercept Swimmer B, who has more time to work with; a second tower guard closes zone coverage during the response.

**Incident report, as filed (excerpt):**

> 15:15 — Tower 4 identified two swimmers in distress, buoy 6–7 channel. Swimmer A: vertical, non-progressing, no vocalization — consistent w/ IDR, prioritized.
> 15:15:10 — Radioed Tower 5 for backup on Swimmer B (active, vocalizing, self-supporting).
> 15:15:10–15:16:00 — Entered at diagonal angle exploiting channel current; reached Swimmer A at approx. 50 sec, rescue tube deployed, towed to shore.
> 15:16:15 — Tower 5 guard reached Swimmer B via reach/throw from paddleboard, no swim entry required.
> 15:18 — Both swimmers ashore, alert, no medical intervention required beyond monitoring. Zone flagged; rope line moved 15m north of channel mouth for remainder of shift. Staffing gap noted for next-day schedule review.

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the Emergency Action Plan template, avalanche companion-rescue protocol with the burial survival curve, and spinal-clearance criteria in filled form.
- [references/red-flags.md](references/red-flags.md) — load when auditing a beach, pool, or ski area's safety program for gaps before they produce an incident.
- [references/vocabulary.md](references/vocabulary.md) — load when a report or handoff needs to use water/mountain rescue terms precisely instead of loosely.

## Sources

- United States Lifesaving Association (USLA) — *Open Water Lifesaving* manual and National Lifesaving Statistics.
- Jeff Ellis & Associates — International Lifeguard Training Program; the "10/20 Protection Standard" (introduced 1991).
- Francesco A. Pia, "The RID Factor as a Cause of Drowning" and subsequent writing on the Instinctive Drowning Response.
- Mario Vittone, "Drowning Doesn't Look Like Drowning" (widely circulated water-safety essay, drawing on Pia's research).
- National Ski Patrol — Outdoor Emergency Care (OEC) curriculum.
- Bruce Tremper, *Staying Alive in Avalanche Terrain* (Mountaineers Books) — burial survival curve (Falk, Brugger & Adler-Kastner, 1994) and terrain-decision practice.
- American Avalanche Association / avalanche.org — North American Public Avalanche Danger Scale.
- Gordon Giesbrecht (University of Manitoba) — the "1‑10‑1" cold water immersion principle.
- National Ski Areas Association (NSAA) — annual *Facts About Skiing/Snowboarding Safety* report.
- No direct lifeguard or ski patrol practitioner has reviewed this file yet — flag corrections via PR.
