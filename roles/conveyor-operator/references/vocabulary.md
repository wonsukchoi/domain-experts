# Vocabulary

Terms generalists blur together that a conveyor operator keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

### Nip point vs. pinch point

A **nip point** is the specific in-running point where a belt or material meets a rotating element (a pulley, a roller) and gets drawn in. A **pinch point** is broader — any point where two surfaces come together with enough force or motion to trap something, including non-rotating hazards like a chute edge closing against a moving component. Guarding standards treat nip points as the higher-priority hazard because the "in-running" geometry actively pulls a hand in rather than just trapping it.

**In use:** "That's a nip point at the tail pulley, not just a pinch point — it'll draw a glove in, it won't just squeeze it."

**Common misuse:** using "pinch point" as a catch-all for every conveyor hazard, which under-signals that a nip point actively pulls rather than passively traps.

### Mistracking vs. belt wander

**Mistracking** is a sustained, directional drift of the belt off centerline that persists and worsens without correction. **Belt wander** is minor, cyclical side-to-side movement within normal tolerance that self-corrects as the belt runs — often just splice or joint variation. Treating wander as mistracking wastes retracking effort; treating mistracking as wander lets a real problem run uncorrected.

**In use:** "That's wander, it swings both ways and settles — the tail-section drift is real mistracking, it's only going one direction and it's getting worse."

**Common misuse:** calling any visible side-to-side belt motion "mistracking" and reflexively adjusting a training idler, when the movement is within normal cyclical variation and needs no correction.

### Rated capacity vs. actual (delivered) capacity

**Rated capacity** is the conveyor's nameplate throughput at its design belt speed and design loading. **Actual capacity** is what it's delivering right now, computed from measured belt speed and measured loaded cross-section — the two numbers diverge whenever the conveyor runs below design speed or under/over its intended loading.

**In use:** "It's rated for 460 tph, but it's only running 280 fpm against a 350 fpm design speed — actual capacity's 368, not 460."

**Common misuse:** citing the nameplate rated capacity as the conveyor's current throughput without checking whether measured speed matches design speed.

### Gravity take-up vs. screw take-up

A **gravity take-up** uses a suspended counterweight to maintain belt tension automatically — it stores potential energy that stays live even with the drive motor's electrical power isolated. A **screw take-up** uses a manually adjusted mechanical screw with no stored gravity energy; isolating it is an electrical-only lockout.

**In use:** "This one's a gravity take-up — block the carriage before you touch anything, the electrical lock alone doesn't stop it dropping."

**Common misuse:** applying identical isolation procedures to both types — either skipping the counterweight block on a gravity take-up (a real injury risk) or wasting time blocking a screw take-up that holds no stored energy.

### Training idler vs. self-aligning idler

A **training idler** is a fixed idler set an operator manually pivots to correct tracking; the correction is manual and needs re-checking. A **self-aligning idler** pivots automatically in response to belt edge contact, continuously self-correcting minor tracking drift without operator action. Confusing the two leads to manually adjusting a self-aligning idler that was already compensating on its own, or expecting a fixed training idler to auto-correct.

**In use:** "The self-aligners are handling the normal drift fine — it's the training idler at the tail that needed a manual reset."

**Common misuse:** assuming a mistracking belt with self-aligning idlers installed doesn't need investigation, when self-aligners correct minor drift but won't compensate for a structural misalignment.

### Belt sway switch

A safety trip device mounted at the belt edge that stops the conveyor if the belt travels beyond a set lateral displacement — it is a safety interlock, not a tracking-correction mechanism. Tripping it repeatedly means the underlying mistracking is unresolved, not that the switch is malfunctioning.

**In use:** "The sway switch tripped twice this shift — that's not a switch problem, the belt's actually walking that far."

**Common misuse:** treating repeated sway-switch trips as a nuisance to bypass or desensitize, rather than as confirmation that a real, worsening mistracking condition exists.

### Vulcanized splice vs. mechanical splice

A **vulcanized splice** bonds belt ends into a continuous rubber joint rated close to the belt's full body tensile strength. A **mechanical splice** joins belt ends with metal fasteners, installs far faster, but is rated to a lower percentage of full belt strength depending on fastener type — it is a tension trade-off, not a lesser-quality substitute in every context.

**In use:** "Mechanical fastener gets us running again today, but at this belt's operating tension we need a vulcanized splice at the next planned shutdown."

**Common misuse:** treating mechanical splices as strictly inferior or strictly interchangeable with vulcanized splices, instead of matching splice type to the belt's actual operating tension.

### Stored energy vs. kinetic energy (LOTO context)

**Stored energy** is potential energy held in a system at rest — a raised counterweight, a loaded incline belt, compressed air in a clutch line — that can move something even with the drive de-energized. **Kinetic energy** is energy of things already in motion, like a flywheel or belt still coasting down after power-off. Both require verification before work begins, but the isolation method differs: stored energy needs blocking/bleeding, kinetic energy needs a wait-and-verify-stop.

**In use:** "Motor's off, but give the flywheel time to stop — that's kinetic, and separately, block the take-up carriage — that's stored."

**Common misuse:** treating "the motor is off" as equivalent to "all energy is isolated," which addresses neither stored nor residual kinetic energy.

### Line balancing vs. bottleneck identification

**Line balancing** is designing or adjusting a multi-conveyor system so each unit's rated capacity roughly matches the others, avoiding built-in overcapacity or undercapacity. **Bottleneck identification** is diagnosing, after the fact, which specific conveyor's actual delivered capacity is currently the lowest and constraining the line. A well-balanced line on paper can still develop a bottleneck if one conveyor silently drops below its design speed.

**In use:** "The line was balanced at commissioning — the bottleneck now is C2 running slow, not a design flaw in the original balance."

**Common misuse:** assuming a line engineered with balanced rated capacities can't develop a bottleneck, ignoring that operating conditions (speed, wear, workarounds) drift away from the original design numbers.

### Full-load amps (FLA) vs. actual load

**FLA** is the motor's rated current draw at 100% of its rated output — a nameplate figure. **Actual load** is what the conveyor is currently moving, which amperage alone doesn't confirm, since friction, misalignment, and bearing drag also raise current draw independent of material throughput.

**In use:** "It's at 94% FLA, but that's drag from the misaligned pulley — the tph on this conveyor is nowhere near its rated capacity."

**Common misuse:** reading high amperage as direct proof of high material throughput or overload, without separately checking measured speed and computed tph.
