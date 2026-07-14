# Vocabulary

### Climb milling vs. conventional milling
Two directions of feed relative to cutter rotation — climb milling feeds in the same direction as cutter rotation at the point of contact, conventional milling feeds opposite — producing genuinely different cutting mechanics and different risk profiles depending on machine characteristics.
**In use:** "This machine has enough backlash that climb milling risks a dig-in — running conventional on this one instead."
**Common misuse:** Treating the choice between climb and conventional milling as purely a surface finish preference — on a machine with meaningful feed mechanism backlash, climb milling can allow the workpiece to be pulled uncontrolled into the cutter, a real safety and tool-breakage risk, not just a finish trade-off.

### Backlash (machine feed mechanism)
Mechanical play or looseness in a machine's feed drive system, which becomes a specific safety consideration for climb milling since it can allow uncontrolled workpiece movement toward the cutter.
**In use:** "Checked this machine's backlash before deciding on milling direction — that's what determines whether climb milling is safe here."
**Common misuse:** Assuming all machines have equivalently low backlash and that milling direction choice doesn't need machine-specific consideration — backlash varies between machines and directly affects whether climb milling is safe on a given setup.

### Workholding rigidity (lateral force resistance)
The capacity of a fixture or clamping setup to resist the lateral (side) cutting forces generated during milling without the workpiece shifting, distinct from simply holding the workpiece in a fixed position for inspection.
**In use:** "Clamped and looks solid, but checking whether this fixture actually resists the lateral force this operation generates — that's a different question than 'is it held in place.'"
**Common misuse:** Confirming workholding adequacy by a static check (the workpiece doesn't move when pushed by hand) rather than evaluating it against the actual lateral cutting forces the specific milling operation will generate — a setup that resists hand pressure can still shift under real cutting load.

### Cutter deflection (end mill)
The bending or flexing of a milling cutter under cutting load, which increases with the cutter's length-to-diameter ratio and produces a tapered or bowed cut wall rather than a straight one.
**In use:** "That taper at the bottom of the slot is cutter deflection — the tool bent under load at full stickout."
**Common misuse:** Assuming a milled feature's walls will be straight simply because the programmed toolpath is straight — a long, thin cutter physically deflects under cutting load, and the actual cut geometry can differ meaningfully from the programmed path as a result.

### Length-to-diameter ratio (end mill)
The ratio between a milling cutter's effective cutting length (stickout) and its diameter, a key factor in how much it deflects under cutting load — analogous to the same concept in boring bars and turning workpieces.
**In use:** "Six-to-one length-to-diameter on this end mill at full depth — that's well into deflection-risk territory, not a standard-parameters situation."
**Common misuse:** Applying standard cutting parameters regardless of a cutter's length-to-diameter ratio at the specific depth being cut — a cutter that's rigid at shallow depth becomes progressively more deflection-prone as more of its length is engaged in a deep feature.

### Multi-pass strategy (roughing and finishing)
Cutting a deep pocket or slot through a sequence of passes — heavier roughing passes removing most material, followed by a light finishing pass — rather than attempting the full depth in one pass.
**In use:** "Three roughing passes to get to depth, then a light finishing pass to clean up the walls — not trying this in one shot."
**Common misuse:** Attempting a full-depth cut in a single pass to save time, especially on a deep feature with a long, thin cutter — a single heavy pass risks both tool breakage from excessive cutting force and deflection-driven dimensional/finish defects that a proper multi-pass strategy avoids.

### Dig-in (climb milling failure mode)
An uncontrolled event where a workpiece is pulled into the cutter faster than intended, typically caused by climb milling combined with machine feed mechanism backlash, risking tool breakage or part/machine damage.
**In use:** "That's a classic dig-in signature — climb milling on a machine with enough backlash to let the workpiece grab and pull."
**Common misuse:** Treating a dig-in event as a random tool failure or operator error rather than recognizing it as a predictable outcome of combining climb milling with meaningful machine backlash — the combination itself is the identifiable, avoidable cause.

### In-process feature verification (milling)
Measuring the actual dimensions of a cut pocket, slot, or profile — rather than trusting the programmed toolpath alone — especially important for deep or narrow features where cutter deflection risk is highest.
**In use:** "Measuring the slot at three depths, not just trusting the program says it should be point-two-five-oh throughout."
**Common misuse:** Assuming a programmed toolpath's dimensions represent the actual cut result — cutter deflection, especially on deep/narrow features, can cause real deviation from the programmed geometry that only direct measurement reveals.
