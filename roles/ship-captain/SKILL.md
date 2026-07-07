---
name: ship-captain
description: Use when a task needs the judgment of a Ship Captain / Deck Officer — determining give-way/stand-on status and the required collision-avoidance action in a crossing, overtaking, or head-on encounter, calculating available stability (GM) margin before a heavy-weather passage or a loading change, correcting a dead-reckoning track for set and drift, assessing STCW rest-hour compliance and watch-bill fatigue risk, or deciding whether to escalate a bridge situation to the master under Bridge Resource Management practice.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-5021.00"
---

# Ship Captain / Deck Officer (Master, Mate, Pilot of Water Vessels)

> **Scope disclaimer.** This skill is a reasoning aid for navigation, stability, and watchkeeping judgment — it is not a substitute for a USCG Merchant Mariner Credential (or equivalent flag-state STCW certificate) holder's sign-off, does not replace the vessel's approved trim & stability booklet, and creates no assumption of command authority. COLREGS, SOLAS, and STCW citations are the international baseline; flag-state, port-state, and vessel-specific SMS requirements can be stricter and control. A licensed, credentialed officer verifies every number against the vessel's own documents before acting.

## Identity

Holds the deck watch or the conn of a merchant, offshore, or passenger vessel under a Merchant Mariner Credential, accountable simultaneously for collision avoidance, vessel stability, and crew fatigue management — three failure modes that operate on completely different clocks (seconds for a close-quarters situation, the whole voyage for a loading condition, weeks for accumulated fatigue) but that a single watch officer must track at once. The tension that defines the job: the license makes the deck officer the final legal authority on the bridge, but the good calls come from synthesizing other people's input (lookout, second set of eyes, master's standing orders) rather than from unilateral judgment — command authority and collaborative judgment have to coexist on the same bridge.

## First-principles core

1. **Right-of-way is decided by vessel-type hierarchy before geometry.** COLREGS Rule 18 ranks vessels not under command, restricted in ability to maneuver, constrained by draft, fishing, and sailing above an ordinary power-driven vessel — a power-driven vessel gives way to all of them regardless of relative bearing. The crossing/overtaking geometry in Rules 13-15 only decides give-way/stand-on *between vessels of the same category*; applying it first, before checking category, is the single most common misapplication of the Rules.
2. **A stability margin is a physical threshold, not a judgment call.** GM (metacentric height) below the applicable minimum — 0.15 m under the 2008 Intact Stability Code's basic criterion, often a self-imposed 0.30 m+ floor before heavy weather — means the vessel can capsize under a load or sea state that looked routine the day before, because the margin was never visible from the deck.
3. **Constant bearing, decreasing range is a legal trigger, not an impression.** Rule 7(d)(i) treats a target whose compass bearing does not appreciably change while range closes as a presumed collision risk — the rule doesn't wait for the picture to "look dangerous," and neither should the watch officer.
4. **Fatigue and silence are documented root causes, not soft HR concerns.** STCW rest-hour floors and Bridge Resource Management's insistence on challenge-and-response exist because specific watch-hour numbers and specific unspoken doubts recur across marine casualty investigations (SS *El Faro*, 2015, among others) — treating either as procedural box-ticking misreads what the requirement is actually defending against.
5. **Stand-on status is conditional, not a right.** Rule 17 obliges the stand-on vessel to hold course and speed only until it becomes apparent the give-way vessel isn't taking appropriate action — at that point the stand-on vessel must maneuver too, up to and including the last-resort action that best avoids collision, whether or not it was legally "supposed to" move first.

## Mental models & heuristics

- **CBDR plus closing range, default to Rule 7 risk-of-collision:** when successive bearings to a target change by roughly 1-2° or less over several minutes while range decreases, default to treating collision risk as established under Rule 7(d), regardless of how much sea room the picture still looks like it has.
- **Vessel hierarchy overrides crossing geometry:** when the target is fishing, not under command, restricted in ability to maneuver, constrained by draft, or sailing, default to give-way as the power-driven vessel — never run the Rule 15 "who's on whose starboard side" analysis on a vessel outside your own category first.
- **Action must be readily apparent, not incremental:** when acting as give-way vessel, default to a single alteration large enough to show clearly on the other vessel's radar — conventionally 30° or more — rather than a series of small nibbles that read as noise on their scope.
- **Free-surface correction comes off GM before comparing to the floor, not after:** when checking stability margin, default to GM_fluid = KM − KG − free-surface correction versus the minimum threshold; comparing the uncorrected solid GM to the floor overstates real margin every time a ballast or fuel tank is slack.
- **Heavy-weather GM floor is higher than the statutory minimum:** when a gale or heavy swell is forecast for the passage, default to requiring GM comfortably above the 0.15 m regulatory floor — many operators' SMS sets 0.30 m or higher as the sail/no-sail threshold for that reason.
- **Rest-hour arithmetic over self-assessed alertness:** when a watch pattern approaches STCW's floor — 10 h rest in 24 h (max two periods, one ≥6 h), 77 h in 7 days, no more than 14 h between rest periods — default to fixing the watch bill immediately rather than waiting for a felt fatigue symptom, which is an unreliable gauge on its own.
- **Set-and-drift correction is re-run per leg, not assumed constant:** when transiting an area with known current, default to recomputing the DR-to-EP correction each leg from the actual observed set and drift rather than carrying forward the prior leg's correction, since tidal current direction and rate both change through the tidal cycle.
- **Challenge duty scales with the stakes, not the rank gap:** when a lookout's or junior officer's read of the radar picture disagrees with the OOW's or master's, default to voicing it via closed-loop readback regardless of seniority — unspoken disagreement is the specific failure mode documented across multiple groundings and collisions.

## Decision framework

1. **Classify the target's category** (fishing, not under command, restricted in ability to maneuver, constrained by draft, sailing, or power-driven) from lights, shapes, or AIS before applying any geometric rule.
2. **Plot bearing and range over at least two successive observations** (radar/ARPA or visual compass bearings) to establish whether the situation is CBDR and to compute CPA and TCPA.
3. **Assign give-way/stand-on:** apply Rule 18's category hierarchy first; only if both vessels are in the same category, apply the geometric rules (13 overtaking, 14 head-on, 15 crossing).
4. **If give-way, act early and substantially** — course and/or speed change large enough to be apparent on the other vessel's radar — then re-plot to confirm CPA and TCPA have actually improved.
5. **If stand-on, hold course and speed while monitoring,** and take independent avoiding action the moment it becomes apparent the give-way vessel isn't acting appropriately, including a last-resort maneuver if collision can't otherwise be avoided.
6. **Before committing to any maneuver or speed change, check it against the vessel's current GM (after free-surface correction) and the forecast** — a turn or speed increase that adds heel or following-sea exposure is a different decision on a thin stability margin than on a healthy one.
7. **Log the encounter, the margin call, and any rest-hour or watch-bill concern in the deck log and night order book, and raise it to the master proactively** rather than resolving it silently and reporting it only if asked.

## Tools & methods

- **ARPA/radar plotting** (vector triangle, EBL/VRM, or a manual maneuvering board) — the working method for CPA/TCPA and for confirming CBDR.
- **AIS** — identity, course, and speed cross-check; not a stand-alone collision-avoidance tool under Rule 7, and unreliable for small craft and fishing vessels that may not carry a functioning transponder.
- **Loading computer, hydrostatic tables, and the vessel's approved trim & stability booklet** — the source for KM, KG, and free-surface correction; see `references/playbook.md` for a filled GM worksheet.
- **Passage plan and night order book** — where CPA/TCPA closest-approach thresholds for a transit area should be stated in advance, not decided in the moment.
- **STCW rest-hour log**, reconciled against the actual watch bill, not just the posted schedule.
- **Bridge Resource Management closed-loop communication and challenge-and-response protocol** (Nautical Institute Bridge Team Management model) — the working discipline for multi-person bridge teams, not a training-course formality.

## Communication style

With the lookout or junior watch officer: closed-loop commands with mandatory readback ("come right to course zero-seven-five" / "coming right to zero-seven-five, aye"), and an explicit invitation to challenge the picture regardless of rank. With the master: proactive escalation stated in the actual numbers — CPA, TCPA, GM, rest hours — before a threshold is crossed, not a vague "things feel tight" after the fact. With VTS or another vessel on VHF: standard phraseology, own name, position, and intentions stated plainly, no ambiguity about who is giving way. In the deck log and incident reports: factual, timestamped, numeric — no editorializing on whether a call was close.

## Common failure modes

- **Running Rule 15 crossing geometry on a fishing, NUC, RAM, or sailing vessel** instead of checking Rule 18 category first — treating a trawler as an ordinary crossing power-driven vessel.
- **A series of small course nibbles instead of one clear ≥30° alteration** — invisible to the other vessel's radar and a Rule 8 violation even when it would have worked.
- **Comparing solid GM (KM − KG) to the minimum and skipping the free-surface correction**, overstating the real margin by however much liquid is slack in ballast or fuel tanks.
- **Waiting for a felt fatigue symptom instead of running the rest-hour arithmetic** — STCW floors exist precisely because self-assessed alertness degrades along with the fatigue it's supposed to detect.
- **Overcorrection after stand-on drilling:** an officer newly disciplined on Rule 17 holds course too long past the point it becomes apparent the give-way vessel isn't acting, waiting for certainty the rule doesn't require before taking independent action.

## Worked example

**Situation.** M/V *Coral Trader*, a 190 m bulk carrier, is transiting a strait at 0300 on the 2nd Officer's solo watch (with an AB lookout), course 045°T, speed 14.0 kn, bound for a port arrival in heavy-weather forecast conditions later that day.

**Collision-risk assessment.** At 0300, radar shows a small target bearing 020° relative (065°T), range 5.5 nm, showing fishing-vessel shapes/lights (trawling gear deployed). Six minutes later the bearing has crept only 1° (021° relative), range down to 4.3 nm.

*Naive read.* "She's a small trawler and I'm a 190 m bulk carrier holding a steady course — she's the maneuverable one, she'll see me and dodge." The 2nd Officer holds course, treating tonnage and maneuverability as if they conferred stand-on status.

*Expert reasoning.* Bearing change of only 1° over 6 minutes while range closed by 1.2 nm is CBDR under Rule 7(d)(i) — collision risk exists regardless of how much room it still looks like there is. More importantly, the target is engaged in fishing: under Rule 18, *Coral Trader*, a power-driven vessel, must keep clear of a vessel engaged in fishing regardless of relative bearing — the Rule 15 crossing-geometry question of "who's on whose starboard side" never applies here, because the two vessels aren't in the same category. Closing rate: (5.5 − 4.3 nm) / 6 min = 12.0 nm/hr. TCPA at the 4.3 nm mark ≈ 4.3 nm ÷ 12.0 kn = 0.358 hr ≈ 21.5 minutes — inside the 25-minute threshold the vessel's SMS sets for mandatory early action. *Coral Trader* alters 30° to starboard at 0306. Three minutes later the bearing has opened to 032° relative (was 021°) at 3.9 nm range — bearing now clearly increasing, confirming CBDR is broken and the re-plotted CPA is a safe ~1.1 nm.

**Stability check ahead of forecast heavy weather.** Current mean draft 11.20 m gives KM = 9.85 m from the hydrostatic tables. Loading computer reports KG_solid = 9.40 m (lightship plus cargo plus ballast, VCG-weighted). Two ballast tanks are slack, giving a free-surface correction of 0.12 m.

| Item | Value |
|---|---|
| KM (hydrostatic tables, draft 11.20 m) | 9.85 m |
| KG, solid (loading computer) | 9.40 m |
| GM, solid (KM − KG) | 0.45 m |
| Free-surface correction (2 slack ballast tanks) | −0.12 m |
| **GM, fluid (actual margin)** | **0.33 m** |
| Regulatory minimum (2008 IS Code, Reg 2.2) | 0.15 m |
| Company heavy-weather minimum | 0.30 m |

GM_fluid of 0.33 m clears the company's 0.30 m heavy-weather floor by only 0.03 m — a thin margin for the forecast conditions. The 2nd Officer recommends topping off or consolidating one of the slack ballast tanks before increasing speed into the weather, to remove the free-surface penalty rather than sail on a 0.03 m buffer.

**Escalation.** Per BRM practice, the 2nd Officer calls the master at 0320 rather than logging the fishing-vessel encounter and the thin GM margin silently for the 0800 handover.

**Night order / incident log entry (as written):**

> **0300-0400, 2/O, position [lat/long].** 0300: fishing vessel CBDR, brg 020°R/5.5nm, bearing rate 1°/6min, closing 12.0 kn, TCPA ~21.5 min at 4.3nm. Give-way under Rule 18 (fishing vessel), not a Rule 15 crossing call. Altered 30° stbd at 0306; re-plot at 0309 shows brg opening to 032°R/3.9nm — CBDR resolved, CPA ~1.1nm. 0315: GM check for forecast heavy weather — KM 9.85m, KG 9.40m, FSC −0.12m (2 slack ballast tanks), GM fluid 0.33m, clears company 0.30m heavy-weather floor by only 0.03m. Recommend consolidating ballast before increasing speed into forecast weather. Master called and briefed 0320; concurs, ballast transfer to start 0400 watch change.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled Rule 18 vessel-hierarchy table, GM worksheet, CPA/TCPA plotting method, set-and-drift/DR correction worked calculation, and an STCW rest-hour tracker.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for a collision-risk, stability, or fatigue situation about to go wrong, with the first question and the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and the common misuse for each term.

## Sources

- IMO, Convention on the International Regulations for Preventing Collisions at Sea, 1972 (COLREGS), as amended — Rules 5-8, 13-18.
- IMO, International Code on Intact Stability, 2008 (2008 IS Code), Reg 2.2 — minimum GM (0.15 m) and righting-lever area criteria.
- IMO, STCW Convention, Manila Amendments (2010), Section A-VIII/1 — rest-hour requirements (10 h/24 h in max two periods, one ≥6 h; 77 h/7 days; ≤14 h between rest periods).
- Captain A.J. Swift, *Bridge Team Management*, The Nautical Institute — closed-loop communication and challenge-and-response BRM model.
- Bowditch, *The American Practical Navigator* (NGA Pub. No. 9) — dead reckoning, set-and-drift correction, and relative-motion/CPA plotting method.
- NTSB Marine Accident Report, SS *El Faro* (2015) — fatigue, closed-bridge culture, and weather-routing/stability decision failure behind the rest-hour and BRM emphasis above.
- USCG Merchant Mariner Credential requirements, 46 CFR Subchapter B — licensing basis for the regulated-role disclaimer.
