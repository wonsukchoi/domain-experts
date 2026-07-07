# Hydrologist — Vocabulary

### Annual exceedance probability (AEP)
The probability that a given flow (or greater) occurs in any single year, expressed as a percentage — the modern, less-misleading alternative framing to "return period."
**In use:** "The 100-year flood is better communicated as the 1% AEP flood — it makes clear this is a per-year probability, not a 100-year clock."
**Common misuse:** treating "100-year flood" as meaning "happens once every 100 years on a schedule," rather than a 1%-per-year independent probability that can recur in consecutive years.

### Return period / recurrence interval
The average number of years between exceedances of a given flow, over a very long time horizon — the reciprocal of AEP (a 1% AEP event has a 100-year return period).
**In use:** "The bridge is designed to pass the 100-year (1% AEP) return-period flow with one foot of freeboard."
**Common misuse:** using it interchangeably with "worst case" or "maximum possible flood," when higher-magnitude, lower-probability events (500-year, PMF) still exist above it.

### Log-Pearson Type III
The standard statistical distribution (per USGS Bulletin 17C) fit to the base-10 logarithms of annual peak-flow data to estimate flood magnitudes at various return periods.
**In use:** "We fit a Log-Pearson III distribution to the 30-year annual peak series to get the 100-year design discharge."
**Common misuse:** assuming any statistical distribution fit to flow data qualifies as "the" flood-frequency analysis — regulatory work in the U.S. specifically requires Log-Pearson III per Bulletin 17C unless an agency approves an alternative.

### Skew coefficient (station vs. regional)
A measure of the asymmetry of the log-transformed flood distribution; "station skew" comes from the local gage record alone, "regional skew" from a broader study combining many gages, and Bulletin 17C prescribes weighting the two based on their relative reliability.
**In use:** "With only 22 years of record, we weighted the station skew against the regional skew study per Bulletin 17C rather than using station skew alone."
**Common misuse:** using station skew unweighted when the record is short, which lets a handful of unusual years distort the estimated tail of the distribution.

### Rating curve
The empirical relationship between water-surface elevation (stage) at a gage and the corresponding discharge (flow rate), used to convert continuously measured stage into a flow record.
**In use:** "The rating curve needs updating after the channel scoured during the last flood — the old stage-discharge relationship no longer holds."
**Common misuse:** assuming a rating curve is a fixed, permanent conversion rather than something that shifts after channel geomorphology changes (scour, deposition, ice effects) and needs periodic re-verification.

### Transmissivity (T)
The rate at which water is transmitted through the full saturated thickness of an aquifer under a unit hydraulic gradient — the product of hydraulic conductivity (K) and saturated thickness (b).
**In use:** "The pumping test gave a transmissivity of about 7,700 ft²/day, consistent with a moderately productive sand-and-gravel aquifer."
**Common misuse:** confusing transmissivity with hydraulic conductivity (K) — T integrates over the full aquifer thickness, K is a point/material property; a thick, low-K aquifer and a thin, high-K aquifer can have the same T.

### Storativity (specific storage / specific yield)
The volume of water an aquifer releases from or takes into storage per unit change in head, per unit area — "storativity" for confined aquifers (typically 10⁻³-10⁻⁵), "specific yield" for unconfined (typically 0.05-0.30).
**In use:** "The storativity value of 9.5×10⁻⁴ confirms this is behaving as a confined aquifer, not unconfined."
**Common misuse:** applying a confined-aquifer storativity range to an unconfined aquifer analysis (or vice versa) without checking which storage mechanism actually governs — the values differ by 1-2 orders of magnitude.

### Baseflow
The portion of streamflow sustained by groundwater discharge into a channel, as opposed to direct storm runoff — what's left in a stream between rain events.
**In use:** "Baseflow separation on the hydrograph shows about 60% of annual flow volume comes from groundwater contribution, not direct runoff."
**Common misuse:** treating "baseflow" and "low flow" as synonyms — low flow is simply the flow during dry periods, which is mostly but not entirely baseflow (some low flow can still include slow interflow or regulated releases).

### Curve Number (CN)
An empirical parameter (0-100) from the SCS/NRCS method representing a watershed's runoff potential based on soil type, land cover, and antecedent moisture — higher CN means more runoff for a given rainfall.
**In use:** "We used a composite CN of 78 for the mixed residential/forest sub-basin, adjusted for antecedent moisture condition II."
**Common misuse:** applying CN methodology to large or highly heterogeneous watersheds where it wasn't validated, or forgetting to adjust for antecedent moisture condition, which can shift computed runoff substantially.

### Prior appropriation (vs. riparian water rights)
A water-rights doctrine (dominant in the Western U.S.) where rights are allocated by priority date — "first in time, first in right" — regardless of land ownership adjacent to the water source, contrasted with riparian doctrine (Eastern U.S.), where rights attach to land bordering the water body.
**In use:** "Under prior appropriation, the 1889 senior right holder can call for water ahead of the 1952 junior right even during a shortage."
**Common misuse:** assuming water rights work the same way everywhere in the U.S. — the governing doctrine varies by state and fundamentally changes how a shortage gets allocated.

### Water balance
The accounting identity that precipitation equals evapotranspiration plus runoff plus change in storage (P = ET + Q + ΔS) over a defined watershed and time period.
**In use:** "The water balance doesn't close — we're missing about 8% of precipitation, probably an underestimated ET term."
**Common misuse:** treating a water balance as a model output to be tuned to match, rather than a mass-conservation check that any model or dataset must satisfy — if it doesn't close, something is measured or estimated wrong.

### Regional regression equation
A statistical equation, developed from many gaged watersheds in a physiographic region, that estimates flood magnitudes or other flow statistics at ungaged sites from basin characteristics (drainage area, slope, etc.).
**In use:** "For the ungaged tributary, we used the USGS regional regression equation for this hydrologic region rather than trying to transfer data from the mainstem gage."
**Common misuse:** applying a regional regression equation to a site outside its documented range of drainage area, slope, or physiographic region — most published equations state explicit applicability limits that get ignored under time pressure.

### Probable Maximum Flood (PMF)
The theoretical maximum flood that could occur at a location, derived from the Probable Maximum Precipitation (PMP) rather than a statistical frequency analysis — used for high-hazard dam design, not routine floodplain mapping.
**In use:** "The dam's spillway is sized to the PMF, not the 100-year flood, because a dam failure would be catastrophic."
**Common misuse:** confusing PMF with an extreme statistical return period (like the 10,000-year flood) — PMF is a deterministic meteorological/hydrologic estimate, not a point on the same probability curve as the 100-year or 500-year flood.
