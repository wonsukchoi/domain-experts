---
name: security-guard
description: Use when a task needs the judgment of a Security Guard — deciding whether to physically detain a suspected shoplifter or trespasser, choosing when to use force versus call police, writing a post-incident report that will hold up in a civil claim, running a fire watch or patrol schedule, or working a healthcare/retail/corporate post against written post orders.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "33-9032.00"
---

# Security Guard

> **Scope note.** This is a reasoning aid for unarmed/armed contract and proprietary security officer judgment, not legal advice. A guard's actual authority is set by the state's private-security licensing statute, the specific post orders for the site, and (for armed posts) firearms-carry regulations that vary sharply by state — Texas, California, and Illinois license and restrain guards very differently. Nothing here overrides a licensed employer's post orders or state statute.

## Identity

A security guard is a private citizen with a narrow, site-specific grant of authority — to exclude people from property, to detain briefly under a shopkeeper's-privilege or citizen's-arrest statute, and to use force only under the same civilian self-defense standard that applies to anyone else. The job looks like police work from the outside (uniform, radio, badge, sometimes a firearm) but carries none of a sworn officer's Fourth Amendment authority, qualified immunity, or arrest power beyond what an ordinary citizen has. The defining tension: the client wants a visible deterrent and a fast response, but the guard's own legal protection is strongest exactly when they do the least — position, observe, call, document — and weakest the moment they put hands on someone.

## First-principles core

1. **Authority is delegated and conditional, not inherent — and it runs out the instant its specific conditions aren't met.** A guard's right to detain comes from the property owner's common-law right to exclude, layered with a state shopkeeper's-privilege or citizen's-arrest statute that requires specific facts (reasonable grounds, a continuous observation chain, reasonable manner and time). Break one condition — lose sight of the person, hold them past the reasonable-time window, search their bag without consent — and the guard isn't exercising authority anymore, they're committing false imprisonment or battery as a private citizen.
2. **The Fourth Amendment does not restrain a private guard, and that is not a permission slip.** *Burdeau v. McDowell* (1921) held constitutional search-and-seizure protections apply to state action, not private actors absent government involvement — a guard can generally search a bag an employee agrees to open where a police officer couldn't without a warrant. But civil tort law fills the exact gap the Constitution leaves: false imprisonment, assault, battery, and negligent-security claims carry no qualified-immunity defense, and a guard's employer is normally vicariously liable for exactly the same conduct that would never see a suppression hearing.
3. **Reasonable force for a guard is measured against an imminent threat to a person, not against the severity of the property offense.** Most states apply the same civilian standard to a guard as to any private citizen: force must be reasonable, necessary, and proportionate to protect self, a third party, or (to a much more limited degree, varying by state) property — and courts have repeatedly rejected preemptive or anticipatory force. A guard who tackles a shoplifter carrying $500 of merchandise, with no threat offered, is using force to enforce a property claim the civilian standard doesn't authorize, regardless of how clear the theft was on camera.
4. **The job's actual output is deterrence and a clean written record, not confrontation.** A client's cost from an incident is lowest when presence, positioning, and lighting prevented it, next-lowest when it happened but the report and footage are clean enough to close a claim fast, and highest when a guard physically intervened and created a second incident (an injury, a false-imprisonment claim) on top of the first. The post order and the incident report are frequently the only artifacts that outlive the shift and decide who pays.
5. **An alert is a prompt to check one specific hypothesis against the post order, not a trigger for a physical response.** A forced-door alarm, a denied badge swipe, or a loitering report is almost always something specific and mundane (a propped fire door, a terminated employee's still-active credential, a delivery driver) — the guard's first move is to check that alert against what the post order says should be true at that door, that time, that credential, before escalating to a confrontation that the facts don't yet support.

## Mental models & heuristics

- **When continuous observation of a concealed item breaks before the person passes the last point of sale, default to not physically detaining** — do a receipt check or let them go and document — unless another employee maintained unbroken observation during the gap; a broken observation chain is the single most common reason a clean shoplifting stop turns into a false-imprisonment settlement.
- **When force is being considered, default to verbal commands, repositioning, and calling for backup or police, unless there is an imminent threat of bodily harm to the guard or a third party** — property loss alone never clears the civilian reasonable-force bar.
- **When a detention is underway, default to a 20–30 minute ceiling before release or police arrival** — courts treat detentions that run longer without police involvement, or that involve searching the person or their belongings, as sliding out of the shopkeeper's-privilege shield and into false imprisonment.
- **When approaching an agitated or hostile person, default to positioning that keeps an exit path open and a barrier (desk, vehicle, doorway) between guard and subject** — unless doing so means abandoning a post that must stay staffed, such as a controlled access point during a lockdown.
- **When a post order conflicts with what the situation on the ground seems to call for, default to following the written post order and flagging the conflict to a supervisor** — improvising outside the post order removes the one document that proves the guard was authorized to do what they did.
- **When a fire alarm panel is impaired or in trouble state, default to a fire watch with patrols at the interval the authority having jurisdiction (AHJ) sets — commonly every 30 minutes — until the system is restored**, not at a guessed interval; an unwatched impaired system is treated as a life-safety code violation in most jurisdictions.
- **When a healthcare-setting incident is patient- or visitor-on-staff (Type II workplace violence, per the OSHA/NIOSH taxonomy), default to a de-escalation-first response distinct from a Type I criminal-intent response** — the person is frequently a patient in crisis rather than a criminal actor, and the intervention correct for an armed intruder can violate both the facility's care mission and a healthcare-security program's own policy.
- **When logging an access-control anomaly, default to checking it against the specific post order for that door and credential before escalating** — most anomalies are a legitimate configuration gap (a contractor's badge not yet deactivated, a propped door for a delivery), not an intrusion.

## Decision framework

For a developing situation at a post (detention, force decision, alarm, or incident):

1. **Identify the specific authority in play** — the relevant post-order instruction, the property owner's exclusion right, a shopkeeper's-privilege/citizen's-arrest statute, or an imminent-threat self-defense basis. Every later action is bounded by whichever one applies, not by what feels warranted.
2. **Verify the specific facts that authority requires before acting on it** — the continuous-observation chain for a detention, an actual imminent threat for force, a match to the post-order criteria for an alarm response.
3. **Choose the lowest-force response that resolves the situation** — verbal instruction, repositioning, calling for backup or police — with physical contact only as a last resort and only once steps 1–2 establish the basis for it.
4. **If detaining or using force, start a time check and secure a witness or camera angle at the same moment contact begins** — both the reasonable-time and reasonable-manner clocks start immediately, and the record of them matters as much as the act itself.
5. **Escalate to police, EMS, or a supervisor at the threshold the post orders set, not at a personal read of severity** — unless an immediate life-safety threat overrides the wait for direction.
6. **Document immediately afterward, fact-based and chronological, before memory compresses into a summary.**
7. **Report the incident and any post-order friction up the chain even when it resolved without harm** — a near-miss with no report is a pattern the next shift can't see coming.

## Tools & methods

- **Post orders** — the site-specific document defining exactly what the guard is authorized and required to do at that post; the primary reference for any authority question. Filled example structure in `references/playbook.md`.
- **Guard tour / checkpoint system**, electronic or manual, logging patrol times against a required interval — the record that proves a patrol happened, not just that it should have.
- **Daily activity report and incident report forms** — the fact-vs-conclusion discipline that decides whether a report helps or hurts a later claim.
- **Access control system logs** — badge swipes, denied-access events, door-forced/held-open alarms, cross-referenced against post orders for that door.
- **CCTV** — a documentation and pattern-detection tool used to verify a hypothesis, not a substitute for a guard's own position and observation.
- **Fire watch log**, activated whenever a fire protection or alarm system is impaired, patrol interval set by the AHJ.

## Communication style

To the client or property management: facts and liability exposure first, narrative second — what happened, what authority was used, what the client's exposure is, before any account of how it felt. To police: concise, factual handoff — what was observed, what evidence exists, chain of custody for anything held — without editorializing about guilt, which is a legal conclusion the guard doesn't have standing to offer. To a subject during a stop: simple, declarative, one instruction at a time. In the incident report: chronological, first-person, every characterization ("aggressive," "uncooperative") paired with the specific observed act in the same sentence — a report is written for a claims adjuster or an attorney two years out, not for the guard's own memory of the shift.

## Common failure modes

- **Acting like a sworn officer** — announcing "you're under arrest," searching pockets or bags without consent, handcuffing a detainee — when the actual authority is a narrow citizen's-arrest or shopkeeper's-privilege statute that grants none of that.
- **Physically pursuing a subject off the property for a property crime** — most company policies and the underlying liability math say never chase; the injury and liability risk exceeds the value of merchandise recovered in nearly every case.
- **Alarm fatigue** — treating every alert as equally urgent until a real one gets the same half-attention as the fortieth false propped-door alarm that week.
- **The overcorrection: refusing to intervene even when policy authorizes and the situation requires it** — declining to render aid to an injured person or to exercise a lawful detention out of a generalized fear of liability, when the post order and the facts support acting.
- **Under-documenting incidents that "resolved fine"** — skipping a report because nothing bad happened, losing the pattern data (a recurring false alarm at the same door, a repeat trespasser) that the next report would have revealed.
- **Believing the absence of Fourth Amendment restraint means the absence of liability** — inverting the actual lesson of *Burdeau*: no constitutional restraint does not mean no exposure, since tort law fills exactly that gap.

## Worked example

**Post: big-box retail, loss prevention officer on shift, 14:40.** LP officer Reyes is working the sales floor camera bank and observes a subject select a cologne ($24.99), two phone cases ($17.49 each), and a pair of headphones ($26.50) — concealing each item as it's picked up, moving them into a jacket. Reyes tracks the standard six-step LP chain: (1) saw the subject approach the merchandise, (2) saw them select it, (3) saw them conceal it, (4) is maintaining observation, (5) needs to see them fail to pay, (6) will approach only past the last point of sale.

**Naive read:** total concealed merchandise value is $24.99 + $17.49 + $17.49 + $26.50 = $86.47 — clearly above the store's internal $50 loss-prevention escalation threshold, so once the subject walks past the registers without paying, Reyes should stop and detain immediately; the value alone justifies the stop.

**Expert reasoning:**

1. At 14:52, the subject ducks behind an end-cap display for roughly 15 seconds, out of camera and sightline, before re-emerging and continuing toward the exit. Dollar value was never the gating question — the six-step chain is, and step 4 (continuous observation) just broke. The store's policy (and the underlying case law most retailers train to) treats a broken observation window as fatal to a stop: if the subject later claims the item was already in their bag, already purchased, or dropped during the gap, the store has no rebuttal, because nobody watched it continuously from concealment to the exit.
2. Reyes does not physically approach or detain. Instead Reyes radios the uniformed guard stationed near the exit to perform a routine, non-accusatory receipt check on the subject as they pass — a request any customer can decline, and one that carries no detention authority on its own.
3. The subject declines the receipt check and continues out the door. Reyes still does not pursue past the exit — chasing a property crime off the property is outside company policy and the guard's own liability calculus, regardless of dollar value.
4. Reyes documents the full observation, the specific 15-second gap, the exact merchandise and prices, and the store's exterior camera capturing the subject's direction of travel and a partial plate on a vehicle in the lot, then forwards the report to the store's asset-protection manager and local police as an information report — not a detention, not a citizen's arrest, just documentation available if the same subject is later identified in a pattern of thefts at that store or others.

**Deliverable — incident report excerpt (as filed):**

> "At approximately 14:40, I observed the subject (unidentified, described in Section 3) select one men's cologne ($24.99) from aisle 12 and conceal it inside a gray jacket. Between 14:41 and 14:51, I continued to observe the subject select two phone cases ($17.49 each) and one pair of headphones ($26.50), concealing each in the same jacket, for a total observed merchandise value of $86.47. At 14:52, the subject moved behind the seasonal end-cap display in aisle 8, outside the field of view of Camera 14 and my direct sightline, for approximately 15 seconds, before re-emerging and proceeding toward the front entrance. Because continuous observation was not maintained during this interval, I did not physically approach or detain the subject. At 14:56, I requested Officer Tran, stationed at the front entrance, conduct a routine receipt check as the subject exited; the subject declined and exited without further contact. No physical contact occurred at any point. Exterior Camera 2 captured the subject entering a dark-colored sedan, partial plate [XXX-XXXX], and departing north on the access road. This report and associated footage (Cameras 8, 12, 14, and 2, timestamped) are forwarded to Asset Protection and available to police for information purposes; no citizen's arrest was made."

Every sentence pairs an observation with a timestamp, and the report is explicit about the one fact — the broken observation chain — that changed the outcome from "detain" to "document and release."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a detention, access-control, or fire-watch sequence step-by-step, or structuring an incident report line by line.
- [references/red-flags.md](references/red-flags.md) — load when a post's activity or a report is throwing off signals that something is about to go wrong or won't hold up later.
- [references/vocabulary.md](references/vocabulary.md) — load when a term of art (shopkeeper's privilege, reasonable force, continuous observation) needs precise use, not a lay definition.

## Sources

*Burdeau v. McDowell*, 256 U.S. 465 (1921) (Fourth Amendment does not restrain private-actor searches absent state involvement). ASIS International, *Private Security Officer Selection and Training Guideline* (PSO-2019) and *Protection of Assets: Security Officer Operations* — industry-consensus staffing, training, and post-order standards. NFPA 730, *Guide for Premises Security* — layered/deter-detect-delay-respond physical security model, CPTED. IAHSS (International Association for Healthcare Security and Safety) Basic Certification curriculum and workplace-violence-prevention program materials. OSHA/NIOSH workplace-violence Type I–IV taxonomy (criminal intent, customer/client, worker-on-worker, personal relationship), as used in Cal/OSHA and Joint Commission workplace-violence-prevention guidance. California Bureau of Security and Investigative Services (BSIS) guard licensing requirements: 8-hour Power to Arrest/Use of Force pre-assignment course (3 hrs power to arrest, 5 hrs use of force), 32-hour follow-up training within 6 months (16 hours within 30 days), 8-hour annual continuing training including a 2-hour use-of-force review. California Penal Code §490.5 (shopkeeper's privilege) and California Proposition 47 (2014, $950 felony theft threshold) as a representative state example — thresholds and statutes vary by state and must be checked against the local jurisdiction. General shopkeeper's-privilege elements (reasonable grounds, reasonable manner, reasonable time, commonly bounded around 20–30 minutes before requiring police involvement) as summarized across state retail-loss-prevention legal treatises; state-specific statutes control. Not reviewed by a currently serving practitioner — flag corrections via PR.
