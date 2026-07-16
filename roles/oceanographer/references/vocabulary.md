# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

### Mixed layer depth vs. thermocline

- **Definition:** the mixed layer is the surface layer of near-uniform density kept turbulent by wind and convection; the thermocline is the depth range below it where temperature drops fastest with depth.
- **In use:** "Mixed layer's only 15 m right now — that spring bloom chlorophyll max is going to sit right at the base of it, and the satellite won't see it once it deepens past the optical depth."
- **Common misuse:** treating them as synonyms, or assuming the mixed layer depth is fixed — it shoals in summer (strong stratification) and deepens in winter (convective mixing), and the seasonal cycle drives when a satellite can and can't see subsurface productivity.

### Water mass

- **Definition:** a body of water with a common formation history, identified by a characteristic, roughly conservative range of temperature and salinity — not by its current location.
- **In use:** "The near-bottom signature at station 34 sits right on the Antarctic Bottom Water end-member in T-S space, even though we're 3,000 km from the formation region — that's advection, not local cooling."
- **Common misuse:** inferring water-mass identity from geography or depth alone ("it's deep, so it must be X"), instead of from the T-S (or Θ-S) diagram, which is the only reliable fingerprint once mixing and advection are in play.

### Practical Salinity vs. Absolute Salinity (TEOS-10)

- **Definition:** Practical Salinity (PSS-78) is a conductivity-ratio-based scale with no units; Absolute Salinity (TEOS-10, g/kg) is the actual mass fraction of dissolved material and is the input the current standard equation of state expects.
- **In use:** "This dataset's still processed under EOS-80 practical salinity — run it through GSW to get Absolute Salinity before we merge it with the 2019 cruise, or the density field will carry a spurious step."
- **Common misuse:** treating a PSU value and a g/kg Absolute Salinity value as interchangeable, or mixing pre- and post-2010 processed products in one density calculation without conversion.

### Optical depth (ocean color)

- **Definition:** roughly one attenuation length of light in water; satellite ocean-color sensors only retrieve a signal from within about one optical depth of the surface, which can be under 20 m in productive (turbid, high-chlorophyll) water.
- **In use:** "Surface chlorophyll looks flat, but that doesn't rule out a subsurface chlorophyll max below one optical depth — we need a glider profile to check."
- **Common misuse:** treating a satellite chlorophyll composite as a full water-column productivity measurement, when it's a thin-skin proxy that misses subsurface features entirely.

### Aliasing (spatial and temporal)

- **Definition:** a sampling pattern too coarse in space or time to resolve a real signal, which then appears as a false trend or noise instead.
- **In use:** "Two-week mooring gap right during the storm — anything we conclude about that period's heat flux is aliased by the storm, not a clean baseline."
- **Common misuse:** treating a sparse ship-based or short-mooring dataset as if it resolved mesoscale eddy variability (weeks, ~100 km scale) or tidal cycles, when the sampling interval is longer than the process being studied.

### Delayed-mode vs. real-time QC (Argo)

- **Definition:** real-time QC applies automated range/spike checks within hours of a float profile surfacing; delayed-mode QC applies a scientist-reviewed correction (typically against a climatology and nearby historical casts) months later.
- **In use:** "Don't build the climate-trend analysis on real-time Argo data — wait for the delayed-mode product, the salinity sensor drift correction hasn't been applied yet."
- **Common misuse:** using real-time (near-instant, automated) Argo data for a precision trend analysis, when only delayed-mode data has been checked closely enough to trust for that purpose.

### Redfield ratio

- **Definition:** the roughly constant carbon:nitrogen:phosphorus ratio (106:16:1 by atoms) observed in marine plankton biomass and deep-ocean nutrient regeneration.
- **In use:** "N:P drawdown here is way off 16:1 — this is an HNLC region, iron's the limiting nutrient, Redfield stoichiometry won't predict productivity."
- **Common misuse:** applying the ratio as a universal productivity/nutrient-limitation rule rather than a regional default that breaks down under iron or silicate limitation.

### Geostrophic transport

- **Definition:** the current velocity and volume transport inferred from the horizontal density (pressure) gradient between two hydrographic stations, assuming a balance between the pressure-gradient force and the Coriolis force.
- **In use:** "That 0.015 PSU salinity drift at the deep stations will bias the density gradient enough to matter for the transport estimate — rerun it on the corrected profiles."
- **Common misuse:** treating a geostrophic estimate as a direct current measurement; it's a diagnostic calculation sensitive to the precision of the density field, including small salinity errors at depth, and needs a reference (level-of-no-motion or independent ADCP) to be absolute rather than relative.

### Crossover check

- **Definition:** a QC comparison at stations where two independent measurements of the same water sample exist — most commonly CTD-derived salinity/oxygen against a bottle sample analyzed on a reference instrument (Autosal, Winkler titration).
- **In use:** "Twelve crossover stations this cruise — plot the offset against cast number before you average it, a trending offset needs a per-cast correction, not a flat one."
- **Common misuse:** averaging crossover offsets into a single cruise-wide correction without checking whether the offset trends over time, which silently under- and over-corrects different parts of the cruise.

### Hypoxia threshold

- **Definition:** the commonly used operational cutoff of dissolved oxygen below ~2 mg/L (roughly 1.4 mL/L), below which most fish and mobile invertebrates avoid or are stressed in the water column.
- **In use:** "We're at 1.8 mg/L on the buoy sensor — before this goes to the state as a hypoxia advisory, get a Winkler bottle sample, that sensor's been in the water three weeks."
- **Common misuse:** treating any single sensor reading near the threshold as confirmed hypoxia without a reference-method cross-check, given how commonly DO sensors drift low from biofouling over multi-week deployments.
