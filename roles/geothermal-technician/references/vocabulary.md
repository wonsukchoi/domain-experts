# Vocabulary

Working vocabulary generalists reliably misuse. Format per term: definition, practitioner usage, common misuse.

### Bore feet vs. pipe feet

- **Definition:** bore feet is the depth drilled into the ground; pipe feet is the total length of HDPE pipe in the ground, which for a single U-bend circuit is roughly twice the bore depth (down leg + up leg).
- **In use:** "That's a 250-ft bore, so figure 500 ft of pipe once you count both legs of the U-bend."
- **Common misuse:** quoting or ordering material off "feet" without specifying which — a materials order built off bore feet instead of pipe feet comes up roughly half short.

### EWT (Entering Water Temperature) vs. EAT (Entering Air Temperature)

- **Definition:** EWT is the fluid temperature entering the heat pump from the loop; EAT is the return-air temperature entering the unit's air-side coil. They're independent measurements diagnosing different halves of the system.
- **In use:** "EWT's inside the design band, so this isn't a loop issue — pull the EAT and check the coil and refrigerant side instead."
- **Common misuse:** reading a low discharge-air temperature and assuming the loop is the problem without ever checking EWT — the loop and the air side fail independently and the diagnostic order matters.

### Closed loop vs. open loop

- **Definition:** closed loop circulates a sealed fluid (water or antifreeze mix) through buried pipe and never contacts groundwater directly; open loop draws groundwater through the heat pump and discharges it back to an aquifer, surface water, or a return well.
- **In use:** "Open loop pencils out here given the well yield, but it brings a separate discharge permit closed-loop jobs never need."
- **Common misuse:** treating open-loop permitting, water-quality, and scaling considerations as a variant of closed-loop rules rather than a genuinely different regulatory and design category.

### Standing column well

- **Definition:** a single deep open-loop well where water is drawn from and returned to the same borehole, relying on the surrounding aquifer to recharge thermally between cycles.
- **In use:** "Standing column only works if the aquifer's transmissivity is high enough to recharge between draw and return — that's a hydrogeology question, not an HVAC one."
- **Common misuse:** assuming any open-loop well can be run as standing column without a site-specific hydrogeological assessment of recharge rate.

### Grout vs. backfill

- **Definition:** grout is the engineered thermally conductive, sealing material tremie-pumped into the annular space of a vertical bore; backfill is the native or imported soil placed over a trench or filled excavation once work is complete.
- **In use:** "Grout goes in before we ever think about backfill — the bore doesn't get covered with dirt until the grout's cured and the pressure test's signed."
- **Common misuse:** using the terms interchangeably, which on a real job site means a bore gets covered with ordinary soil instead of engineered grout — losing both the seal and the thermal conductivity the design assumed.

### Short-circuiting (thermal)

- **Definition:** heat transfer between the supply and return legs of the same U-bend inside a single borehole, which reduces the effective heat exchange with the surrounding ground.
- **In use:** "No spacers on that bore means the legs are probably short-circuiting — that's lost capacity nobody will see until the loop's under full load."
- **Common misuse:** attributing underperformance solely to bore length or grout quality without checking whether spacers were actually installed.

### Turbulent flow / purging

- **Definition:** flow fast enough (above a critical Reynolds number) that fluid mixes across the pipe cross-section rather than moving in smooth parallel layers (laminar flow); purging is the process of running high flow through the loop to remove trapped air and confirm turbulent flow is achieved.
- **In use:** "Flow's technically moving, but it's not purged past turbulent threshold yet — keep the cart running."
- **Common misuse:** treating "the pump is running and fluid is moving" as equivalent to "the loop is properly purged" — laminar flow can persist even with a running pump if velocity or air removal is inadequate.

### Delta-T (heat pump water side)

- **Definition:** the temperature difference between fluid entering and leaving the heat pump's water-side heat exchanger at a given flow rate and capacity.
- **In use:** "Design delta-T's 8 degrees at 9 GPM — if the field reading's 15, something's choking flow."
- **Common misuse:** comparing a measured delta-T to a generic "8–12 is normal" range without computing what this specific unit's design delta-T actually is at its rated capacity and flow.

### Thermal response test (TRT)

- **Definition:** a field test that injects a known heat load into a test borehole and measures the fluid temperature response over time to calculate the site's apparent ground thermal conductivity and undisturbed ground temperature.
- **In use:** "This job's over the TRT threshold — we're not sizing off a benchmark table when it's this much bore footage on the line."
- **Common misuse:** skipping a TRT on a large job to save cost, then discovering the benchmark k-value assumption was wrong only after the full field is drilled and underperforming.

### Ground thermal conductivity (k-value)

- **Definition:** a measure (Btu/hr·ft·°F) of how readily the surrounding formation conducts heat away from (or into) the borehole; the dominant variable in bore-length sizing.
- **In use:** "Same tonnage, same climate, but this lot's k-value is half the last job's — that's why the bore field's nearly double the length."
- **Common misuse:** treating k-value as roughly constant across a region rather than formation-specific — soil, rock, and groundwater conditions vary meaningfully within short distances.

### GPM per ton

- **Definition:** the design fluid flow rate through the loop, expressed per ton of heat pump capacity, typically targeted around 2.25–3 GPM/ton for water-to-air units.
- **In use:** "Confirm we're at 3 GPM per ton before calling this commissioned — anything less and delta-T's going to read high."
- **Common misuse:** verifying total system flow without normalizing to tonnage, which makes a correctly-sized 2-ton system and an undersized 4-ton system look the same on a flow meter.

### Fusion joint (butt fusion vs. electrofusion)

- **Definition:** the heat-based methods used to join HDPE loop pipe — butt fusion melts and presses pipe ends together directly; electrofusion uses an embedded heating element in a fitting to fuse pipe to fitting.
- **In use:** "Butt-fuse the straight runs, electrofuse the tie-ins where you can't get a fusion machine lined up square."
- **Common misuse:** assuming any heat-joined connection is equivalent regardless of technique or equipment calibration — an improperly fused joint can look sound and still fail the pressure test or, worse, pass it and fail later underground.
