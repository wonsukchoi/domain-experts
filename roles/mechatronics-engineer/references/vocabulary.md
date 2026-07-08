# Vocabulary

Terms of art generalists misuse — not terms they could resolve by looking up a definition, but terms whose textbook definition survives while the practitioner implication gets dropped.

## Backlash

**Definition.** The bounded range of load-side motion that produces zero change in motor/sensor-side reading, caused by clearance between mating gear teeth or other drivetrain elements — not wear, though wear increases it.

**In use:** "Measured gear-train backlash is 2.1 mm — that's 4.2× the ±0.5 mm stopping-accuracy requirement, so it has to be compensated, not tuned around."

**Misuse note.** Generalists treat backlash as a property the control loop can just "tune out" with gain (see First-principles #2 in `SKILL.md` for why it can't). The fix is an explicit compensation algorithm (e.g., reversal dither, `references/playbook.md` §2) or elimination via load-side sensing/mechanical preload — not a gain change.

## Resolution

**Definition.** The smallest position (or velocity) increment a sensor can report — a property of the sensor and its scaling, independent of what the sensor can actually see.

**In use:** "1000 counts/mm resolution is three orders of magnitude finer than the ±0.5 mm target — but that's not the same claim as meeting the accuracy spec."

**Misuse note.** Generalists equate fine resolution with accuracy. Resolution only bounds accuracy from below; a fine-resolution sensor placed upstream of an uncompensated error source (like backlash) still produces gross positioning error, because the sensor is precisely reporting the wrong thing.

## Reflected inertia

**Definition.** The load-side inertia as it appears to the motor through a gear reduction, scaled by 1/G² for a reducer of ratio G — not the raw load inertia.

**In use:** "A 5:1 reducer divides reflected load inertia by 25, which is why gearing down is the standard fix when the inertia ratio blows the 10:1 ceiling."

**Misuse note.** Generalists apply the gear ratio linearly to inertia (divide by G) instead of by the square of the ratio (divide by G²), which understates by how much a modest gear ratio change fixes an inertia-mismatch problem, or leads them to over-spec a gearbox when a smaller ratio would have sufficed.

## Inertia ratio

**Definition.** The ratio of reflected load inertia to motor (rotor) inertia at a coupled servo axis — the sizing quantity that predicts tuning difficulty and settling behavior, distinct from the mechanical gear ratio.

**In use:** "Reflected inertia ratio comes in at 7:1 — inside the 10:1 ceiling, but past the 5:1 comfort line, so expect the tuning pass to take longer."

**Misuse note.** Generalists conflate inertia ratio with gear ratio because both are expressed as "N:1." They're different physical quantities that happen to share notation — gear ratio is a kinematic choice; inertia ratio is its dynamic consequence and is what actually predicts control stability.

## Load-side sensing / motor-side sensing

**Definition.** Load-side (direct) sensing places the position sensor on the driven member itself, downstream of all drivetrain compliance; motor-side (indirect) sensing places it on the motor shaft, upstream of gear backlash, belt stretch, and coupling compliance.

**In use:** "Motor-side encoding is retained for cost, but that means backlash between it and the load is invisible to the loop and has to be compensated explicitly."

**Misuse note.** Generalists treat the sensor-location choice as interchangeable with a cost/precision tradeoff on the sensor part number alone. The real tradeoff is architectural: motor-side sensing doesn't just cost less, it structurally cannot see downstream mechanical error, which then has to be paid for as calibration/algorithm engineering.

## Bandwidth (servo loop)

**Definition.** The frequency up to which a control loop (velocity loop or position loop) can command and track motion with acceptable phase lag — a control-system property distinct from the sensor's sample/update rate, which only sets an upper bound on achievable bandwidth.

**In use:** "Structural resonance needs to sit at least 3× the velocity-loop bandwidth, or the loop will excite the resonance while trying to close it fast."

**Misuse note.** Generalists use "bandwidth" and "update rate" interchangeably. A 500 Hz servo update rate does not mean 500 Hz loop bandwidth — bandwidth is typically a fraction of the sample rate and is further constrained by structural resonance margin, not just by how fast the controller samples.

## Structural resonance

**Definition.** The natural mechanical frequency at which a coupled structure (bracket, coupling, drivetrain) amplifies excitation — a mechanical property that bounds how aggressively the control loop can be tuned before it excites instability.

**In use:** "Resonance margin was 3× at commissioning; once bearing wear dropped damping in the field, the same gain setting rang the structure."

**Misuse note.** Generalists treat resonance margin as a one-time commissioning check rather than a lifetime one — see the 3×/6× margin heuristic under Mental models in `SKILL.md` for the field-wear mechanism that erodes it after commissioning.

## Shield termination (single-ended grounding)

**Definition.** The practice of connecting a cable's shield to ground at exactly one end (the controller end, by convention) so the shield diverts induced noise without becoming a current path between two separated ground references.

**In use:** "Terminate the shield at the controller end only — grounding both ends turns the shield into a ground-loop conductor instead of a noise diversion path."

**Misuse note.** Generalists assume more grounding is always better shielding and connect the shield at both ends "for safety." That creates a ground loop between the two chassis ground potentials, which injects noise current through the shield rather than diverting it — the opposite of the intended effect.

## Pigtail (shield termination)

**Definition.** An unbraided shield gathered into a single twisted lead and landed under a screw terminal or connector pin, rather than terminated 360° around the connector backshell.

**In use:** "The intermittent noise traced back to a pigtailed shield on the encoder cable — swap it for a 360° backshell termination before touching any filtering."

**Misuse note.** Generalists treat "the shield is grounded" as sufficient and don't distinguish termination geometry. A pigtail adds inductance and creates a gap in shield coverage right at the connector, defeating the shield at the exact frequencies EMC problems tend to occur, regardless of how well-specified the cable itself is.

## Loop area (EMC)

**Definition.** The physical area enclosed by a current-carrying conductor and its return path — the geometric quantity that sets induced-noise coupling via V ≈ A·dB/dt, independent of wire gauge or shielding.

**In use:** "The noise didn't drop after upgrading to heavier-gauge cable, because the fix needed was routing the return conductor tighter to the source, not a thicker wire."

**Misuse note.** Generalists respond to EMC problems by upgrading cable spec (gauge, shielding rating) because that's the purchasable lever. Induced voltage scales with loop area times rate of field change, not wire gauge — a large loop area with premium cable still couples noise; a tight loop with modest cable often doesn't.

## Concurrent (V-model / RFLP) design

**Definition.** Per VDI 2206, decomposing a mechatronic system top-down (requirement → functional → logical → physical) with mechanical, electrical, and firmware domains run in parallel and cross-checked at each level, then integrating and verifying bottom-up — distinct from a sequential handoff between disciplines.

**In use:** "Run the RFLP decomposition concurrently across domains and flag every point where a mechanical choice bounds an electrical one — don't finalize the gear ratio before controls has weighed in on achievable bandwidth."

**Misuse note.** Generalists read "V-model" as just a project-phase diagram and implement it as a sequential handoff (mechanical finishes, then electrical starts, then firmware) — not a valid reading of it; see First-principles #3 in `SKILL.md` for why sequencing compromises cost and performance. The V-model's actual point is running domains concurrently with explicit cross-domain dependency flags.

## Compliance (mechanical)

**Definition.** The inverse of stiffness — how much a structure or coupling deflects under a given load — a property that, like backlash, sits between sensor and load and is invisible to a sensor placed upstream of it.

**In use:** "Belt stretch is compliance, not backlash — it doesn't create a dead zone, but it does add a load-dependent position lag the motor-side encoder can't see."

**Misuse note.** Generalists lump compliance in with backlash as "mechanical slop" and expect the same fix (dither/preload). Compliance produces a continuous, load-dependent error rather than a bounded dead zone, so it needs a different compensation approach (stiffness increase or load-side sensing), not a reversal-dither move.

## Domain isolation (fault diagnosis)

**Definition.** The diagnostic step of determining which discipline (mechanical, electrical/EMC, firmware/calibration, or materials/chemistry) actually owns a field defect before ordering a fix — distinct from noting which discipline the symptom presents in.

**In use:** "The warning light is an electrical symptom, but domain isolation on the last three units traced it to solder/fluid chemistry, not the wiring harness."

**Misuse note.** Generalists fix the domain the symptom looks like it belongs to (an electrical-looking fault gets an electrical fix) rather than isolating the domain that actually causes it. A symptom's presenting domain and its defect's owning domain are frequently different, and skipping isolation leads to swapping the wrong part.
