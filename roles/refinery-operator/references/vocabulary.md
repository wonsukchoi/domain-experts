# Vocabulary

### Cut point
The effective boiling-point temperature at which a distillation column separates lighter (lower-boiling) product from heavier (higher-boiling) product at a given tray, determined by the combination of tray temperature and column pressure, not temperature alone.
**In use:** "The tray temperature looked normal, but the true cut point shifted lighter because column pressure had crept up — that's what let naphtha into the kerosene draw."
**Common misuse:** Treating tray temperature alone as the indicator of where the column is actually cutting — the true cut point depends on the temperature-pressure relationship, and a temperature reading that looks unchanged can still represent a shifted cut point if pressure has moved.

### API gravity correction
A standardized correction (per API MPMS tables) converting a petroleum product's observed volume and gravity, measured at actual temperature, to a standard reference temperature (commonly 60°F/15.6°C) for accurate custody transfer.
**In use:** "Raw gauge reads 10,200 barrels, but after API gravity/temperature correction to 60°F, the net standard volume is 10,150 — that's the figure that goes on the transfer document."
**Common misuse:** Reporting the raw observed gauge volume as the transaction figure without applying the correction — petroleum volume expands and contracts meaningfully with temperature, and the uncorrected number doesn't represent the actual standardized quantity being bought or sold.

### Relief valve / PSV (pressure safety valve)
A safety device designed to automatically open and release pressure when a vessel or system exceeds its set pressure, acting as the last layer of protection against overpressure.
**In use:** "PSV on the flash drum lifted at 2:15 — that's a process safety event, not something we just note and move on from."
**Common misuse:** Treating a relief valve lift as a self-resolving event once pressure returns to normal — the lift itself is evidence that every upstream control layer failed to prevent the excursion, and that failure needs its own investigation regardless of how quickly pressure normalized afterward.

### Custody transfer
The formal transfer of ownership of a petroleum product between parties (e.g., a refinery and a pipeline, or a terminal and a customer), based on measured and corrected quantity.
**In use:** "Custody transfer meter needs to be proved and calibrated before this delivery — that reading is what both parties get paid or charged against."
**Common misuse:** Treating custody transfer measurement with the same tolerance as internal process monitoring — commercial transactions at bulk petroleum pricing make even small percentage measurement errors financially significant in a way internal monitoring tolerances don't need to account for.

### Startup/shutdown transient
The period during which a process unit is moving between an idle/offline state and steady-state operation (or vice versa), characterized by process variables moving through non-steady ranges and multiple systems changing state simultaneously.
**In use:** "We're still in the startup transient — follow the checklist exactly, this isn't the time for troubleshooting judgment calls."
**Common misuse:** Applying the same flexible, experience-based troubleshooting approach during a transient that's appropriate during steady-state operation — the transient period carries materially higher risk, and the documented procedure exists specifically because it was designed for this higher-risk condition.

### Normalization of deviance
The gradual process by which a deviation from a standard procedure becomes accepted as normal because it repeatedly didn't cause a problem, eroding the original safety margin the standard was meant to preserve.
**In use:** "That alarm's been overridden for two years with no incident — that's exactly the pattern normalization of deviance describes, and it's worth re-checking why."
**Common misuse:** Treating a long track record without incident as evidence that a deviation or override is actually safe — the absence of a problem so far doesn't confirm the original risk assessment was wrong, only that the additional factor needed to turn it into an incident hasn't occurred yet.

### Management of Change (MOC)
The formal review process required before implementing any change to equipment, procedure, or operating conditions in a PSM-covered facility, evaluating the change against the existing hazard analysis.
**In use:** "That's a good efficiency idea, but it's still a process change — it goes through MOC before we run it that way."
**Common misuse:** Assuming MOC review is only needed for changes that look risky — even a change intended to improve safety or efficiency can interact with the existing hazard analysis in ways that aren't obvious without the formal review.

### Distillation column profile
The full set of temperature and pressure readings across a distillation column's trays, evaluated together to understand the column's actual separation behavior, as opposed to any single tray or point reading.
**In use:** "Pull the full column profile, not just the draw tray temperature — the story's in how temperature and pressure relate across the whole column."
**Common misuse:** Diagnosing a column issue from a single tray's reading in isolation — the column's behavior emerges from the relationship between multiple readings, and a single in-range reading can mask a real shift visible only in the fuller profile.

### API tank gauging (strapping)
The process of measuring liquid level in a storage tank (manually via a gauge tape or automatically) and converting that level to volume using the tank's calibrated capacity tables ("strapping tables").
**In use:** "Tank's strapping table gives us volume from the observed level — then we apply temperature correction on top of that for the standard volume."
**Common misuse:** Treating the strapping-table volume conversion as the final answer without the subsequent temperature/API gravity correction step — strapping converts level to observed volume at actual conditions, which still needs correcting to standard conditions for custody transfer purposes.

### Flash point
The lowest temperature at which a petroleum product's vapors will ignite when exposed to an ignition source, a key safety-related product quality specification (tested per ASTM D56 or similar methods).
**In use:** "Kerosene flash point came back at 34, below our 38 minimum — that's a real safety-relevant spec failure, not just an off-spec quality note."
**Common misuse:** Treating flash point as a routine quality metric on par with any other spec parameter — flash point is directly tied to a product's fire/explosion risk in handling and transport, giving a failure here more urgency than a similar-magnitude deviation on a purely cosmetic or performance spec.
