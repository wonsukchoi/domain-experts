# Vocabulary

Terms generalists conflate or use loosely that a practitioner keeps sharply separate.

## Class A vs. Class B (pathway/circuit class)

**Class B** is a two-wire circuit topology where a single wire break disables every device downstream of the fault. **Class A** is a four-wire topology with a redundant return path, so a single break degrades to Class B behavior for that segment but the rest of the circuit keeps reporting. Neither is universally "better" — the choice follows occupancy risk and the locally adopted code.

*In use:* "This is a three-story assembly occupancy — the local amendment mandates Class A on the NAC circuits, so the panel needs the extra return-path terminals."

*Common misuse:* treating Class A as always the safer, always-correct choice and speccing it regardless of code requirement or budget, or conversely defaulting to Class B out of habit without checking whether the occupancy or amendment requires Class A.

## UL listed vs. system compatible

**UL listed** means an individual device or panel has passed UL's testing standard (UL 864 for panels, UL 268 for smoke detectors) on its own. **System compatible** means a specific panel-device combination appears on the panel manufacturer's published compatibility list — a requirement layered on top of individual listing, not replaced by it.

*In use:* "Both parts carry a UL mark, but this detector isn't on the panel's compatibility list — swap it before we call this a listed system."

*Common misuse:* assuming that because every component is individually UL listed, the assembled system is automatically a listed system.

## Candela vs. lumens vs. decibel (notification appliance ratings)

**Candela** measures luminous intensity in a specific direction — the rating NFPA 72's visual notification spacing tables use. **Lumens** measure total light output in all directions, a spec-sheet number that doesn't map directly to the code's spacing tables. **Decibel (dB)** measures audible notification loudness, governed by a separate requirement (audible above ambient by a defined margin) from the visual candela requirement.

*In use:* "The appliance's lumen rating on the box doesn't tell us anything for code compliance — we size off candela at the mounting height and room dimension."

*Common misuse:* comparing two notification appliances by lumens as if that settles code compliance, when the applicable code table is candela-based.

## Initiating device vs. notification appliance

**Initiating devices** detect the alarm condition (smoke detectors, heat detectors, pull stations, waterflow switches). **Notification appliances** alert occupants once the panel processes an alarm (horns, strobes, speakers). They sit on different circuit types (IDC vs. NAC) with different code requirements and different failure consequences.

*In use:* "The false trips are on the initiating side, not the NAC — don't touch the horn/strobe wiring, the problem is upstream at the detector."

*Common misuse:* using "detector" and "alarm" interchangeably to mean the whole system, which obscures which half of the circuit actually has the fault.

## Supervisory signal vs. trouble signal vs. alarm signal

**Alarm** signals a fire/intrusion condition requiring response. **Supervisory** signals a condition that could impair fire protection if not corrected (a closed sprinkler control valve, a low water-tank level) but isn't itself an emergency. **Trouble** signals a system fault (open circuit, ground fault, low battery) unrelated to an actual fire/intrusion condition.

*In use:* "That's a supervisory on the tamper switch, not a trouble — someone closed the sprinkler valve, it's not a wiring fault."

*Common misuse:* treating all three as "the panel's beeping, go check it" without distinguishing urgency — a supervisory on a closed valve needs faster response than a low-battery trouble.

## NICET certification vs. state/local contractor license

**NICET certification** (Levels I–IV, Fire Alarm Systems program) is a national, individual technical credential documenting a person's demonstrated knowledge and experience. A **state or local fire alarm contractor license** is the legal authorization for a business (and often a named qualifying individual) to perform the work in that jurisdiction — requirements for which level of NICET certification qualifies vary by state and by AHJ.

*In use:* "He's NICET Level III, but that doesn't put his name on our contractor license — we still need the qualifying individual signed off with the state."

*Common misuse:* treating NICET certification as interchangeable with a business license, or assuming a NICET level automatically satisfies every AHJ's design-sign-off requirement without checking the local rule.

## Verified response vs. enhanced call verification (ECV)

**Verified response** is a broader municipal policy under which police/fire dispatch is contingent on some form of confirmation that an alarm is real, reducing dispatch to unconfirmed activations. **Enhanced call verification (ECV)** is the specific practice within that policy: the monitoring station calls two designated contacts before requesting dispatch, rather than dispatching on the first signal.

*In use:* "This jurisdiction's under an ECV ordinance — if we can't reach either contact within the call window, the account doesn't get police dispatch on a straight burglary trip."

*Common misuse:* using "verified response" and "ECV" as fully interchangeable — ECV is one implementation mechanism; some verified-response ordinances allow other verification methods (video, audio) instead of or alongside phone calls.

## Duct detector vs. area (open-space) smoke detector

**Duct detectors** sample air moving through HVAC ductwork via a sampling tube, sized to the duct's air velocity, and typically shut down air handling on alarm to prevent smoke recirculation. **Area smoke detectors** sample ambient room air directly and are spaced per the open-area spacing tables. They serve different code purposes (duct detectors protect against smoke recirculation through HVAC, not general life-safety notification) and are not substitutes for each other.

*In use:* "The duct detector shutting down the AHU doesn't count toward our required area coverage in that room — we still need ceiling-mounted units per the spacing table."

*Common misuse:* assuming a duct detector in a room's HVAC return satisfies the room's area-detection requirement.

## False alarm vs. nuisance alarm vs. unwanted alarm

**False alarm** (or malicious/malfunction alarm) originates from equipment failure, misuse, or a deliberate false activation with no fire/intrusion condition present. **Nuisance alarm** is a real detector response to a real but non-hazardous condition (steam, dust, cooking smoke) — the detector worked correctly, the environment was the problem. **Unwanted alarm** is the umbrella term some jurisdictions and NFPA data use for both categories combined when tallying dispatch and fine statistics.

*In use:* "That's a nuisance alarm, not a false one — the detector saw real steam and did exactly what it's supposed to do. The fix is detector placement or type, not a defective-unit warranty claim."

*Common misuse:* calling every non-fire activation a "false alarm," which obscures whether the fix is a defective device (false), a placement/technology mismatch (nuisance), or something else — each has a different remediation.
