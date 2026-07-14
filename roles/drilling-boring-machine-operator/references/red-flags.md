# Red flags

### A hole with depth-to-diameter ratio exceeding 3-5x programmed for continuous feed
- **Usually means:** chip evacuation risk hasn't been accounted for, risking heat buildup and drill breakage.
- **First question:** does this specific tool/material combination have a characterized exception for continuous deep-hole drilling, or should this be peck drilled?
- **Data to pull:** hole depth-to-diameter ratio, tool manufacturer's guidance for this specific drill type and material.

### A drill breaking partway through a deep hole
- **Usually means:** chip packing from insufficient peck frequency or inadequate coolant delivery to the cutting point.
- **First question:** was peck drilling used, and if so, was the peck interval appropriate for this depth/diameter/material?
- **Data to pull:** programmed peck cycle parameters, coolant delivery method (through-tool vs. external flood).

### A hole showing measurable deviation from straight (wander) at depth
- **Usually means:** the hole start wasn't adequately established, allowing early wander to compound over depth.
- **First question:** what technique was used to establish the initial hole start (pilot, initial engagement support)?
- **Data to pull:** hole straightness measurement, hole-start technique used.

### A long-reach boring operation run with the same feed/speed/depth of cut as a short-reach setup
- **Usually means:** bar deflection under load hasn't been accounted for, risking chatter or taper.
- **First question:** what is this setup's reach-to-diameter ratio, and were parameters adjusted for it relative to a standard short-reach job?
- **Data to pull:** boring bar reach and diameter, cutting parameters used, comparison to standard short-reach parameters.

### A bore showing taper (larger at the opening than at depth, or vice versa)
- **Usually means:** boring bar deflection, consistent with an under-adjusted parameter set for this reach-to-diameter ratio.
- **First question:** does the taper direction and magnitude match what would be expected from bar deflection at this reach?
- **Data to pull:** bore diameter measurements at multiple depths, bar reach/diameter specifications.

### A drilled/bored hole diameter or finish drifting despite a visually sharp-looking tool
- **Usually means:** tool wear isn't always visible, and actual hole measurement is needed to catch dimensional drift.
- **First question:** has hole diameter been measured directly and compared to a trend, or only the tool inspected visually?
- **Data to pull:** hole diameter trend data across recent parts, tool usage count/hours since last change.

### Coolant relying on general flood delivery for a deep-hole drilling operation
- **Usually means:** coolant may not be effectively reaching the cutting point as hole depth increases.
- **First question:** is through-tool coolant available and being used for this operation, or only external flood coolant?
- **Data to pull:** coolant delivery method, hole depth, any heat-related symptoms observed (discoloration, tool wear rate).

### A new material or hardness change run on an existing drilling/boring program without re-verifying parameters
- **Usually means:** parameters validated for a different material may not be appropriate, affecting chip formation, tool wear, or deflection behavior.
- **First question:** does the current material match what this program's parameters were validated for?
- **Data to pull:** current material specification, program's original validation material.

### A broken tool extraction attempted without first confirming the part can still meet spec if extraction succeeds
- **Usually means:** effort may be spent on extraction for a part that will need to be scrapped anyway due to other damage.
- **First question:** if extraction succeeds, will the part actually still meet its specification, or is scrapping the more efficient path?
- **Data to pull:** extent of damage from the break, part's remaining feature/tolerance requirements.

### Repeated peck-drilling cycle interruptions or increased retraction frequency needed compared to the programmed cycle
- **Usually means:** actual chip formation/evacuation is behaving differently than the program assumed, possibly from tool wear or material variation.
- **First question:** does actual chip condition/formation match what the peck cycle was designed around, or has something changed?
- **Data to pull:** chip condition observed, tool wear status, material lot consistency.
