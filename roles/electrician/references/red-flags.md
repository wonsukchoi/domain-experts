# Red flags — panel, wiring, and troubleshooting smell tests

### Double-tapped single-pole breaker (two conductors under one termination not listed for it)
- **Usually means:** a previous circuit addition took the path of least resistance instead of adding a subpanel or a breaker rated for two conductors; second most likely is a DIY splice done at the panel to avoid running a new home run.
- **First question:** "Is this breaker/lug listed by the manufacturer for two conductors?" (Some are — check the panel's UL listing before assuming it's a violation.)
- **Data to pull:** panel manufacturer's installation instructions or UL listing card (often on the inside of the panel door) for that specific breaker model.

### Calculated service demand within 10% of the main breaker rating
- **Usually means:** the service was adequate when installed but has absorbed additions (AC, dryer, hot tub) one at a time, each individually "fine" but never re-totaled; second most likely is an as-built service smaller than what a prior remodel permit assumed.
- **First question:** "Has anyone run the full-house load calculation since the last major appliance or HVAC addition, or has it just been assumed to be fine because nothing's tripped?"
- **Data to pull:** most recent load calculation on file with the permit history, or the panel schedule with nameplate ratings for every 240V appliance.

### Breaker trips instantly on reset with all loads disconnected
- **Usually means:** a short or ground fault in the wiring itself or a hard-wired fixture, not an overloaded circuit; second most likely is a failed breaker (rare relative to wiring faults, but confirm by swapping to a known-good breaker of the same rating only after the wiring has tested clean).
- **First question:** "Does it trip before any load is even connected, or only after running for a while?" — this alone separates a magnetic (fault) trip from a thermal (overload) trip.
- **Data to pull:** continuity/megohmmeter reading hot-to-neutral and hot-to-ground with the circuit fully isolated at the panel.

### Neutral conductor smaller than the ungrounded (hot) conductors on a multiwire branch circuit
- **Usually means:** the circuit was extended or repaired by someone treating the neutral like any other wire, not accounting for the unbalanced/shared-neutral current it can actually carry; second most likely is a legacy installation predating current shared-neutral rules.
- **First question:** "Is this neutral shared across two ungrounded conductors on different phases (a multiwire branch circuit), and if so, is there a common disconnect per 210.4?"
- **Data to pull:** the actual conductor gauge at the panel lug (not just the breaker rating) and confirmation of whether the two hots share a neutral.

### Bonding jumper or main bonding jumper missing or found at a subpanel that also has a neutral-ground bond
- **Usually means:** the subpanel was wired as if it were a service panel (neutral and ground bonded together) instead of keeping neutral and ground separate downstream of the first disconnect; second most likely is a genuinely missing bond at the actual service, which is the more dangerous version.
- **First question:** "Is this the first disconnecting means for the service, or a subpanel fed from another panel?" — the bonding rule flips depending on the answer.
- **Data to pull:** a continuity check between the neutral and ground bus bars at the panel in question (isolated neutral bar = correct for a subpanel; bonded = correct only at the service).

### Aluminum branch-circuit conductors (visually dull gray, common in homes wired 1965–1972)
- **Usually means:** original branch wiring using the older AA-1350 alloy alloy known for connection-point overheating from oxidation and differential thermal expansion; second most likely (less common) is aluminum SE cable at the service entrance, which is a different and generally lower-risk application.
- **First question:** "Are the terminations at devices and splices original, or have they already been remediated with listed connectors?"
- **Data to pull:** a visual inspection log of a sample of outlets/switches for connector type (AlumiConn, COPALUM crimp, or none) and any signs of heat discoloration at the faceplate.

### Knob-and-tube wiring found during an unrelated job (insulation upgrade, remodel)
- **Usually means:** original early-20th-century wiring still in service, which has no equipment ground and cannot legally be in contact with insulation; second most likely is that it's been partially abandoned but still energized at one end.
- **First question:** "Is this circuit still energized, and does the current or planned scope (attic insulation, wall closure) put insulation in contact with it?"
- **Data to pull:** a circuit trace back to the panel to confirm live/dead status before any insulation or remodel work proceeds.

### Voltage drop over 3% on a branch circuit or 5% combined branch+feeder on a long run
- **Usually means:** an undersized conductor for the run length rather than the load — this is a guideline, not a code violation in most jurisdictions, but it predicts dimmer lighting, motor strain, and nuisance issues under load.
- **First question:** "Is this an informational-note guideline in this jurisdiction, or has the local AHJ adopted it as an enforceable requirement?" — determines whether to cite it as a code issue or a recommendation.
- **Data to pull:** actual measured run length (not straight-line distance) and the conductor gauge actually pulled, then recompute VD = (2 × K × I × D) ⁄ CM.

### GFCI or AFCI device that won't hold after one reset attempt
- **Usually means:** a real ground fault or arc fault downstream, not a defective device; second most likely is a shared-neutral configuration confusing the device's internal sensing.
- **First question:** "Does it trip immediately on reset with nothing plugged in, or only when a specific device is plugged in?"
- **Data to pull:** load-by-load isolation test (unplug everything, reset, then reintroduce devices one at a time) before replacing the breaker or receptacle.

### Panel load imbalance greater than ~20% between the two legs under normal operation
- **Usually means:** 120V single-pole circuits were added over time without tracking which leg they land on, concentrating load on one leg; second most likely is a miswired multiwire branch circuit sharing a neutral across the same leg instead of opposite legs.
- **First question:** "Has anyone clamp-metered both legs under a typical load condition, or is this an assumption from the panel schedule?"
- **Data to pull:** clamp-meter reading on both leg conductors at the main lugs during a normal-use period (evening, AC running).
