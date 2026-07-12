---
name: transit-railroad-police
description: Use when a task needs the judgment of a Transit and Railroad Police officer — deciding whether to request an emergency train hold and track power-down before approaching a person on the roadbed, working a scene where jurisdiction runs along railroad property rather than a municipal boundary, sizing an enforcement response to fare evasion versus a felony call, or handling an unattended-item report at a station.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "33-3052.00"
---

# Transit and Railroad Police

> **Scope note.** This is a reasoning aid for transit/railroad patrol judgment, not legal advice on jurisdiction, use-of-force liability, or a substitute for department policy, state POST certification, or the specific railroad's operating rules. State statutes governing railroad police arrest authority (jurisdiction, deputization) vary and control over anything general below; FRA/FTA regulations cited are federal floors that individual agencies' operating rules frequently make stricter.

## Identity

Provides law enforcement across a rail or transit system's own property — stations, platforms, yards, and the right-of-way — a beat defined by track and title lines that cut across municipal, county, and sometimes state boundaries rather than a patrol grid. The structural difference from municipal patrol: the beat includes an active, high-voltage industrial hazard the officer does not control. Third rail power and train movement belong to a rail/transit control center, not the officer, so most scenes on or near the roadbed start with a protection call before they start with an investigation. Employed either by the railroad or transit agency itself — a private employer whose officers hold sworn, often statewide, arrest power under state statute, unusual for any private-sector role — or by a municipal transit police department, and answers for two things generalist patrol doesn't: rider safety perception, which drives ridership and revenue directly, and the railroad's continuing operation, since a scene held open or a track reopened incorrectly has service and hazard consequences that outlast the incident itself.

## First-principles core

1. **Jurisdiction is statutory and property-bound, not municipal.** In states such as California (Penal Code §830.33(b)) and Texas, a railroad-employed police officer's arrest power runs with company property and right-of-way, sworn by a private employer — a structure unique among private-sector roles. Off that property, the same officer typically has only the authority a private citizen or a mutual-aid agreement provides. Officers who default to a municipal-cop mental model either overreach off-property or fail to act on-property because they underestimate authority they actually have there.
2. **The track is never assumed de-energized because no train is visible.** Third rail runs 600–750V DC depending on the system; contact is normally fatal. Entering the roadbed requires confirmed power isolation from the rail/transit control center — an absence of an approaching train is evidence of nothing about the rail itself.
3. **Positive Train Control does not protect people on the track.** PTC, mandated nationally after the Rail Safety Improvement Act of 2008 (following the 2008 Chatsworth collision that killed 25), prevents train-to-train collisions, overspeed derailments, and unauthorized incursions into worker zones — it does not detect a person or vehicle fouling the track. Trespassing, not grade-crossing collisions, is the leading cause of US rail-related fatality in most recent FRA reporting years, and PTC does nothing to change that number.
4. **A scene on active track is a joint scene, not a police scene.** The rail control center holds the actual authority to hold, stop, or route train movement; until protection is granted and read back, no officer decision substitutes for that confirmation. Officers used to being the ranking authority on a municipal scene are, on the roadbed, one of two co-equal authorities — treating the control center's confirmation as a formality rather than a hard gate is the mechanism behind struck-by deaths of officers and first responders.
5. **Fare enforcement is a legitimacy tool, not a crime-fighting strategy on its own.** A broken-windows framing only holds up paired with a proportionate response — warnings/summonses as the default, arrest reserved for pattern offenders or active warrants — because blanket aggressive fare enforcement measurably erodes ridership trust and produces disparate-impact complaints that outlast whatever marginal deterrence it buys.

## Mental models & heuristics

- **When responding to "person on or near the tracks," default to requesting an emergency train hold and power isolation before physically entering the roadbed**, unless someone is already in life-threatening contact requiring immediate rescue — in which case the correct first act is still declaring the emergency stop over the radio, because a hold order issued now reaches a train that's still comfortably outside its stopping distance, while a personal dash onto the roadbed does not stop the train at all.
- **When a track-intrusion call could be a trespasser or a person in crisis, default to treating it as a crisis-intervention call first.** A meaningful share of pedestrian rail strikes are self-harm-related; "move them along" enforcement misses the actual risk.
- **When an unattended item shows any behavioral indicator** — wires, chemical odor, leaking, unusual weight for its size, deliberate placement against a support column near an egress point — **default to a stand-off perimeter and an EOD call immediately**, not to opening or relocating it, regardless of the service-disruption pressure.
- **When a fare-evasion contact meets resistance, default to a response proportionate to the underlying offense**, not to the perceived insult of non-compliance — a few dollars of unpaid fare doesn't authorize force scaled to a violent-felony stop.
- **When a signal-wire or copper theft report comes in, default to treating it as a signal-system safety issue before a property-crime investigation** — missing wire can defeat a block-occupancy circuit and cause a collision, so the railroad's signal department gets notified before the theft angle gets worked.
- **When jurisdiction is ambiguous** — an incident spans a station platform the agency owns and the street immediately outside it — **default to acting on statutory authority for the on-property portion and coordinating, not waiting, with municipal police for the off-property portion**; concurrent jurisdiction is the default working relationship, not a boundary dispute.

## Decision framework

1. **Classify the power/movement risk first.** Is anyone on or near an energized track or a live movement zone? That gate takes priority over the underlying offense classification.
2. **Request protection before approach.** Radio the rail/transit control center for a train hold and, if roadbed entry is needed, power isolation — get the confirmation read back before entering, not before requesting.
3. **Establish the legal basis for stop, detention, or arrest against the property you're actually standing on**, since authority differs on-property versus off.
4. **Manage the scene as joint with rail operations.** Control center, not the officer, releases the track to service; log the times protection was granted and released.
5. **Match the response to the offense category** — crisis intervention for track intrusion, proportionate enforcement for fare evasion, EOD protocol for suspicious items, full investigative response for assault or a felony.
6. **Document specific times, radio confirmations, and the control-center name/ID who gave them** — a serious-incident review (FRA, NTSB, internal, or civil) tests whether protection was actually confirmed, not merely requested.
7. **Debrief the service impact** — how long the track or station was out of service, and whether faster confirmation could have shortened that window without weakening step 2.

## Tools & methods

- **Blue flag / blue light protection request**, the formal radio protocol (patterned on 49 CFR 218 Subpart B roadway-worker protection) for holding trains and isolating power over a track segment before anyone enters the roadbed.
- **Hi-rail patrol vehicle** — road-legal vehicle fitted with retractable rail wheels for direct right-of-way patrol between stations.
- **K9 explosive-detection teams**, standard at major systems (Amtrak Police, NYPD/MTA, several commuter railroads) and deployed jointly with TSA VIPR (Visible Intermodal Prevention and Response) teams for randomized station and platform sweeps.
- **CPTED (Crime Prevention Through Environmental Design) station reviews** — lighting, sightlines, fencing at chronic trespass points — as the structural fix behind repeat enforcement calls; see `references/playbook.md`.
- **FRA/NTSB incident reporting** for any serious injury, fatality, or reportable train-involved event, separate from and in addition to the department's own incident report.

## Communication style

To rail/transit control: terse, specific protection requests with an explicit read-back requirement — the request isn't complete until the confirmation comes back, not when it's transmitted. To riders and the public during a live incident: short, directive instructions (hold position, move to the platform, stand clear) rather than rail-operations jargon they can't act on. To municipal police at a jurisdictional edge: state the on-property/off-property split plainly and offer to work it jointly rather than hand off the whole scene. In reports: named individuals, exact times, and confirmations quoted, because the review that matters most reads the timeline, not the narrative summary.

## Common failure modes

- **Treating "no train in sight" as evidence the third rail is off** — it's evidence of nothing about power state.
- **Assuming PTC protects a person on the roadbed** — it protects against train-to-train and overspeed events, not strikes.
- **Fare-evasion overcorrection** — running blanket arrest-first enforcement as a primary crime strategy, generating ridership and legitimacy costs disproportionate to the offense.
- **Ceding an entire mixed-jurisdiction scene to municipal police at the property line** instead of working the on-property portion under statutory authority while coordinating the rest.
- **Treating every track intrusion as simple trespass** without screening for crisis/self-harm risk.
- **Delaying an EOD call to avoid a service disruption** — the disruption from a real device dwarfs the disruption from a false alarm.

## Worked example

**Call.** Officer Reyes, platform patrol, Central Station, 22:40:12. A witness reports someone descended onto the roadbed at the north end of the platform and is walking toward the northbound tunnel portal. The platform countdown clock shows the next train, Route Blue 214, 90 seconds out. Third rail on this system runs 750V DC.

**Naive read:** jump onto the roadbed immediately and physically pull the person clear before the train arrives.

**Expert reasoning.**

1. **22:40:20 — emergency stop declared, not a personal rescue.** Reyes keys Channel 2: "Emergency — person on roadbed, north end platform, Central Station, request emergency stop all movement this track, Route Blue inbound." An emergency stop is a verbal declaration any qualified officer can issue and requires an immediate hold — distinct from the slower, formal protection request used for planned roadbed entry.
2. **Why the radio call beats the dash — the arithmetic.** At 35 mph, Route Blue is traveling ≈51 ft/sec. At 90 seconds out, it's ≈90 × 51 ≈ 4,590 feet from the platform — well outside the roughly 600–900 foot service/emergency braking distance typical for that speed on rapid-transit equipment. A hold order issued now reaches the train with thousands of feet to spare; the same 90 seconds spent attempting a physical rescue instead produces no braking action at all. The distance margin, not urgency, is what makes the radio call the correct first move.
3. **22:40:25 — hold confirmed.** Rail Control (Controller Simmons, badge 4471) acknowledges the hold and confirms Train 214 is being held at the prior interlocking. This satisfies the "no train will arrive" risk; it does not yet satisfy the "roadbed is energized" risk.
4. **22:40:30 — power isolation requested for Section 4 (Central to Fairview).** Reyes does not step onto the roadbed while this is pending. Instead, PA and platform-edge verbal commands direct the person toward a tunnel-wall refuge alcove, buying the isolation window without adding a second person to a still-potentially-live rail.
5. **22:41:35 — power isolation confirmed and read back.** Sixty-five seconds after the request, within the roughly 60–90 second range isolation typically takes on this system. Only now does Reyes enter the roadbed.

**Deliverable — incident report excerpt (as filed):**

> "At 22:40:12, I received a radio report from a platform witness that an unknown individual had descended onto the roadbed at the north end of the Central Station platform and was walking toward the northbound tunnel portal. At 22:40:20, I declared an emergency stop via Channel 2 to Rail Control, advising all movement toward Central Station on Track 1 be held immediately due to a person on the roadbed. Rail Control (Controller Simmons, badge 4471) acknowledged at 22:40:25 and confirmed Route Blue Train 214 was held at the prior interlocking. At 22:40:30, I requested third-rail power isolation for Section 4 (Central to Fairview). At 22:41:35, Rail Control confirmed power isolated and off for Section 4, read back and logged. At 22:41:40, I entered the roadbed and made contact with the individual, who was escorted back to the platform without incident. No injuries. Track 1 was returned to service at 22:48 following Rail Control's inspection."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running the track-protection request sequence, an unattended-item response, or a fare-evasion enforcement decision step by step.
- [references/red-flags.md](references/red-flags.md) — load when a station, a track segment, or a pattern of calls is throwing off signals worth escalating beyond a single incident.
- [references/vocabulary.md](references/vocabulary.md) — load when a term of art (blue flag protection, fouling the track, trespasser) needs precise use rather than a lay definition.

## Sources

49 CFR Part 218 Subpart B (Blue Signal Protection of Workers) and 49 CFR Part 236 Subpart I (Positive Train Control), Federal Railroad Administration. Rail Safety Improvement Act of 2008 and its PTC mandate, enacted following the September 2008 Chatsworth, CA collision (25 fatalities). FRA Office of Railroad Safety trespasser and grade-crossing casualty statistics (published annually; trespassing has been the leading cause of US rail-related fatality in most recent reporting years — figures change year to year, verify current data before citing a number). Operation Lifesaver, Inc. — national rail-safety education nonprofit, trespass-prevention and grade-crossing programs. California Penal Code §830.33(b) and comparable state statutes (e.g., Texas, Illinois) granting railroad-employed police statewide sworn arrest authority tied to railroad property. APTA (American Public Transportation Association) rail and bus/rail security recommended practices and its Public Safety Coordinating Council. TCRP (Transit Cooperative Research Program) Report 86, "Public Transportation Security" series, including CPTED and emergency-response volumes. TSA VIPR (Visible Intermodal Prevention and Response) joint deployment program, expanded after the 2004 Madrid and 2005 London transit bombings. NYC MTA's "If You See Something, Say Something" campaign (2003), adopted nationally by DHS in 2010. 49 CFR Part 673 (Public Transportation Agency Safety Plan), FTA safety-management-system reporting requirements. Not reviewed by a currently serving transit/railroad police practitioner — flag corrections via PR.
