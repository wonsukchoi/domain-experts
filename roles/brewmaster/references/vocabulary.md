# Vocabulary

### VDK
Vicinal diketones — the combined GC readout of diacetyl and 2,3-pentanedione, reported together in ppm because they share a biosynthetic pathway and a release threshold.
**In use:** "Pull VDK at day 9, not just diacetyl — the GC method reports both compounds as one number."
**Common misuse:** Generalists use "VDK" and "diacetyl" as interchangeable synonyms, then read a diacetyl-only spec sheet against a combined VDK lab result and think the batch is further out of spec (or further in spec) than it actually is.

### Diacetyl rest
A deliberate temperature ramp (commonly to 15–18°C, held 48–72 hours) applied while yeast are still warm and metabolically active, so they reabsorb VDK before cold crash locks the flavor fault in.
**In use:** "VDK's still high at terminal gravity — hold at fermentation temp and run a diacetyl rest before crashing."
**Common misuse:** Treated as "let it sit a bit longer" on the existing schedule. A rest requires raising temperature to keep yeast active; simply extending time at fermentation temp without the ramp, or extending time after cold crash, does not reabsorb VDK the same way because chilled, settled yeast are no longer metabolically active.

### Mash pH (room-temperature reading)
The pH of the mash, read after cooling a sample to room temperature rather than at mash temperature, because the temperature-correction offset is large enough to mask a real deviation.
**In use:** "That 5.4 was read hot off the mash tun — pull a sample, let it cool, and re-read before we trust it."
**Common misuse:** Reading pH directly off a hot mash sample, or applying a rough mental temperature correction instead of actually cooling the sample, which can hide an out-of-band reading or flag an in-band one as a false fault.

### HSO / CSO
Hot-side oxidation (wort exposed to oxygen above ~80°F/27°C during brewing) and cold-side oxidation (oxygen pickup after fermentation, during transfers, dry-hopping, and packaging) — two mechanistically distinct failure modes with different fixes.
**In use:** "That papery note is HSO from the underback transfer, not CSO — the DO meter at packaging reads clean."
**Common misuse:** Lumping both under one generic "oxidation problem" and applying a cold-side fix (e.g., tighter packaging DO control) to a fault that was actually introduced hot-side during the brew, or vice versa.

### Terminal gravity
The gravity at which a batch has stopped changing measurably, confirmed by two consecutive same-day readings — not simply "the number written on the recipe as target FG."
**In use:** "Gravity's flat at 2.8°P for two days — that's terminal, not just close to the recipe's projected FG."
**Common misuse:** Treating terminal gravity and the recipe's predicted final gravity as the same thing, then flagging a batch as stuck or contaminated when it terminates a point or two off the printed prediction despite two flat readings confirming it's actually done.

### Apparent vs. real attenuation
Apparent attenuation is calculated straight from hydrometer/refractometer gravity readings (which overstate sugar consumption because alcohol is less dense than water); real attenuation corrects for that alcohol effect and is always the lower number.
**In use:** "Apparent attenuation reads 78%, but real attenuation on this one is closer to 63% once you correct for the ABV."
**Common misuse:** Quoting apparent attenuation (the number a simple OG/FG plug-in gives) as if it were real attenuation, which overstates how much fermentable sugar the yeast actually consumed.

### Pitch rate (cells/mL per °Plato)
Yeast cell count scaled to wort gravity, not a flat cell count — 0.75 million cells/mL per °Plato for ales, 1.5 million for lagers, roughly halved for a fresh lab-propagated culture.
**In use:** "This is 16°P wort going into a lager — that's 24 million cells/mL, not the flat pitch we'd use on an 11°P ale."
**Common misuse:** Using one standard pitch quantity (by vial count or slurry volume) across different-gravity batches instead of scaling to °Plato, which under-pitches high-gravity beers and over-pitches low-gravity ones.

### ASBC method
A named, specific procedure from the American Society of Brewing Chemists' *Methods of Analysis* (e.g., spectrophotometric alpha-acid testing, hemacytometer-plus-methylene-blue viability counts) — not a generic label for "the lab did it properly."
**In use:** "Viability was run per ASBC hemacytometer/methylene-blue method, not just an eyeball count under the scope."
**Common misuse:** Citing "ASBC method" as a blanket credibility stamp without naming which specific method was used, which makes a result impossible to reproduce or defend if a downstream number is later challenged.

### HACCP CCP (Critical Control Point)
A specific, documented process step — such as pasteurization held at a defined minimum temperature — where control is monitored and logged per batch because failure there is a food-safety hazard, not just a quality variance.
**In use:** "Pasteurization is our CCP — log every batch's hold temperature and time, not just the ones that look off."
**Common misuse:** Treating "CCP" as a synonym for any quality checkpoint (like a routine gravity reading) rather than the specific, HACCP-designated, per-batch-logged control step it actually is — which means the mandatory logging discipline gets applied to the wrong steps or skipped on the real one.

### Membrane filtration (spoilage detection)
A microbiological test method that passes a beer sample through a fine filter to trap and culture spoilage organisms, used specifically to detect contamination — distinct from filtration as a clarity/haze process step in packaging.
**In use:** "Run membrane filtration on the suspect lot before we clear it, separate from the regular haze filter."
**Common misuse:** Confusing this QC test with the production-line filter used for beer clarity, as if passing beer through any filter constitutes spoilage testing.

### Cold crash vs. lagering
Cold crash is a short chill (hours to a couple days) mainly to drop yeast and haze particles out of suspension before packaging; lagering is a extended cold conditioning (weeks) that also drives flavor maturation and further sedimentation — they are not the same step at different durations.
**In use:** "This is going into a proper 3-week lager, not just a cold crash — don't rush packaging because the tank looks clear early."
**Common misuse:** Treating lagering as "cold crash, just longer," which leads to packaging a beer as soon as it looks clear instead of once its flavor has actually matured.

### Dry-hop creep
A secondary, slower fermentation restart caused by residual fermentable material and enzymes carried in whole-cone or pelletized hops added during dry-hopping — distinct from the primary fermentation's CO2 production, and it can push gravity down and pressure up after the beer was believed finished.
**In use:** "Watch tank pressure after dry-hop addition — creep can restart fermentation even though primary was done a week ago."
**Common misuse:** Attributing a post-dry-hop pressure rise or gravity drop entirely to residual primary-fermentation CO2, missing that the hops themselves reintroduced fermentable material and enzymatic activity.

### SPC control chart (2-sigma rule)
A statistical process control chart that flags a process (e.g., milling gap consistency) as out of control when two of three consecutive points fall beyond 2 standard deviations from the mean — a run-based signal, not a single-reading alarm.
**In use:** "Two of the last three milling-gap readings are past 2-sigma — that's a real signal, pull the roller gap and check it."
**Common misuse:** Reacting to any single out-of-band point as an emergency (or, conversely, ignoring a genuine two-of-three-point run because no single reading looks dramatic), rather than applying the actual run rule the chart is built on.

### TTB tolerance (±0.3% ABV)
A hard federal regulatory gate on how far a packaged batch's actual ABV can deviate from its printed label claim — not a rounding convenience or a suggested QC target.
**In use:** "Batch tests at 6.9% against a 6.5% label — that's outside TTB tolerance, it can't ship under this label as printed."
**Common misuse:** Treating the ±0.3% figure as an internal quality-control cushion that can be waived under schedule pressure, rather than the regulatory ship/no-ship gate it actually is, independent of how the beer tastes.
