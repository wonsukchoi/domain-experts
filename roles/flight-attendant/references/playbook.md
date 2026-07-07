# Flight Attendant Playbook

Filled worksheets and reference tables for the calculations and sequences the SKILL.md decision framework calls for. Numbers below are illustrative, self-consistent examples in the shape of typical widebody/narrowbody Part 121 operations — always substitute the operating carrier's actual FAM, MEL, and certification basis.

## 1. Required flight attendant count by seat count (14 CFR 121.391)

Formula: 19 or fewer seats → not addressed by this section; >19 and <51 → 1; >50 and <101 → 2; >100 → 2 + ceil((seats − 100) / 50).

| Passenger seats | Excess above 100 | Units (ceiling) | Required flight attendants |
|---|---|---|---|
| 50 | — | — | 1 |
| 100 | — | — | 2 |
| 116 | 16 | ceil(16/50) = 1 | 2 + 1 = 3 |
| 150 | 50 | ceil(50/50) = 1 | 2 + 1 = 3 |
| 151 | 51 | ceil(51/50) = 2 | 2 + 2 = 4 |
| 216 | 116 | ceil(116/50) = 3 | 2 + 3 = 5 |
| 300 | 200 | ceil(200/50) = 4 | 2 + 4 = 6 |
| 350 | 250 | ceil(250/50) = 5 | 2 + 5 = 7 |

**Rule this table demonstrates:** crossing a 50-seat boundary by even 1 seat (150 → 151) adds a full additional required flight attendant — there is no partial-credit reading of "part of a unit."

## 2. Exit-status worst-case worksheet

Certification worst case assumes half of an aircraft's exits are blocked; the demonstrated per-exit load is total passengers ÷ (usable exits ÷ 2).

| Aircraft config | Total exits | Normal worst-case usable (half) | Demonstrated load/exit | Exit lost to MEL | Worst-case usable after MEL | Load/exit after MEL | Change |
|---|---|---|---|---|---|---|---|
| 216 seats, 8 exits | 8 | 4 | 216/4 = 54.0 | 1 (assumed-open side) | 3 | 216/3 = 72.0 | +33.3% |
| 180 seats, 6 exits | 6 | 3 | 180/3 = 60.0 | 1 (assumed-open side) | 2 | 180/2 = 90.0 | +50.0% |
| 300 seats, 10 exits | 10 | 5 | 300/5 = 60.0 | 1 (assumed-open side) | 4 | 300/4 = 75.0 | +25.0% |
| 150 seats, 6 exits | 6 | 3 | 150/3 = 50.0 | 1 (assumed-blocked side) | 3 (no change) | 150/3 = 50.0 | 0% |

**Rule this table demonstrates:** an MEL-deferred exit only degrades the worst-case scenario if it sits on the side the certification assumed would stay open. Confirm which side/pair the operator's certification data assumes before concluding "no impact" — the last row shows the case where an inoperative exit changes nothing because it falls on the already-assumed-blocked side.

## 3. Door-arming/disarming cross-check sequence

| Step | Action | Callout |
|---|---|---|
| 1 | Flight attendant physically moves the door mode selector to ARMED | "Door 1 Left, armed" (spoken aloud, not silent) |
| 2 | Crossing/opposite flight attendant visually confirms the mode indicator | "Confirmed, Door 1 Left armed" |
| 3 | Both flight attendants log the arm on the cabin door status if the aircraft/operator requires a written check | Initial or tick the door-status card |
| 4 | On arrival, before any door is opened: flight attendant states intended action | "Door 1 Left, disarming" |
| 5 | Crossing/opposite flight attendant confirms mode selector moved to DISARMED/DOORS TO MANUAL before the door is touched | "Confirmed, Door 1 Left disarmed" |
| 6 | Only after step 5's verbal confirmation does the door get opened | — |

**Rule this sequence demonstrates:** every step has a spoken half and a confirmed half — a flight attendant who arms or disarms a door without hearing the confirmation back has completed the physical action but not the cross-check, and the physical action alone is the incomplete half of the procedure.

## 4. Unruly passenger escalation ladder (filled example)

| Tier | Trigger | Action | Documentation |
|---|---|---|---|
| 1 — Verbal warning | Non-compliance with a single crew instruction (seatbelt sign, stow tray table) | Direct, specific verbal instruction, repeated once | Mental note of time and behavior |
| 2 — Written notice | Repeated non-compliance, or any instance of verbal abuse toward crew/passengers | Passenger Disturbance Report initiated; passenger informed in writing that continued behavior may result in prosecution | Time-stamped incident report with witness names |
| 3 — Captain notification / restraint consideration | Physical aggression, threat, or interference with a safety duty | Captain briefed; physical restraint per FAM procedure only if behavior is physically dangerous; law enforcement pre-alerted at destination or nearest suitable airport | Full written statement, photos of any injury/damage, witness statements collected before landing |
| 4 — Diversion / law enforcement handoff | Continued danger to flight safety, or Tier 3 threshold met with meaningful remaining flight time | Captain declares diversion if warranted; passenger met by law enforcement on arrival; FAA civil penalty referral (up to $37,000/violation) and/or criminal referral under 49 U.S.C. § 46504 | Complete incident package handed to law enforcement and filed with company security |

**Rule this ladder demonstrates:** each tier requires the documentation of the tier below it to already exist — a Tier 3 restraint decision with no Tier 1/2 paper trail is defensible in the moment but weak in the subsequent legal or FAA process.

## 5. In-flight medical event triage flow (filled example)

| Presentation | Immediate action | Ground consult before treatment? | Kit/equipment |
|---|---|---|---|
| Unresponsive, no pulse | CPR + AED immediately, no consult delay | No — act first, consult in parallel if possible | AED, basic first-aid kit |
| Chest pain, diaphoretic, history of cardiac disease | Oxygen, position of comfort, vitals | Yes, immediately, in parallel with first aid | Enhanced Emergency Medical Kit (EMK): nitroglycerin, aspirin (per consult direction) |
| Severe allergic reaction, difficulty breathing, swelling | Epinephrine auto-injector if available and consult unreachable in time-critical window | Preferred, but do not delay epinephrine for an unambiguous anaphylaxis presentation | EMK: epinephrine, antihistamine |
| Seizure, now resolved, patient confused | Protect from injury, recovery position, monitor | Yes, before any medication | EMK: basic monitoring items |
| Fainting, recovered, vitals normal | Position of comfort, fluids, monitor | Optional — physician on board or ground consult if recurrence | Basic first-aid kit only |

**Rule this table demonstrates:** the only presentations that skip the ground-consult-first default are the ones where delay itself is the harm (cardiac arrest, unambiguous anaphylaxis); everything short of that gets triaged through consult before medication from the enhanced kit is administered.
