# Vocabulary

### MAOP (Maximum Allowable Operating Pressure)
The highest pressure at which a pipeline or pipeline segment is legally and safely permitted to operate, established by federal pipeline safety regulation and the pipe's design/material characteristics.
**In use:** "We're at 55 against a 60 MAOP — that's our normal margin, and we don't run it any tighter than that for throughput."
**Common misuse:** Treating MAOP as a target ceiling to run as close to as possible for maximum throughput — it's a hard limit with an engineered safety margin built in specifically so it's not approached routinely.

### Odor fade
The reduction in detectable odorant concentration as gas travels through a distribution system, caused by absorption into pipe walls, oxidation, or other loss mechanisms over distance and time.
**In use:** "Injection point reads fine, but we still check odorant at the far end of the system because of odor fade."
**Common misuse:** Assuming a compliant odorant injection rate at the plant guarantees detectability everywhere downstream — fade is a real, distance-dependent phenomenon that requires its own verification, not an assumption based on the source reading.

### Dew point (gas)
The temperature at which moisture in natural gas begins to condense out of the gas phase at a given pressure — a key indicator of hydrate formation risk in pipelines.
**In use:** "Dew point's fine at atmospheric pressure, but we need to check it against our actual line pressure, not a generic table value."
**Common misuse:** Evaluating a moisture or dew point reading against a standard/generic threshold without adjusting for the specific system's actual operating pressure — dew point margin depends on both moisture content and pressure, and the same moisture reading can be safe at one pressure and risky at another.

### Hydrate formation
The formation of ice-like solid crystals (gas hydrates) inside a pipeline when moisture, gas, and certain pressure/temperature conditions combine, capable of physically blocking flow.
**In use:** "That flow restriction downstream matches a hydrate formation signature, not a mechanical blockage — moisture and pressure conditions line up for it."
**Common misuse:** Assuming hydrate formation only happens in extreme cold — hydrates can form at temperatures well above freezing under sufficient pressure, so "it's not cold enough" isn't a reliable way to rule it out.

### PSM (Process Safety Management)
An OSHA regulatory framework (29 CFR 1910.119) requiring documented procedures, hazard analyses, and controls for facilities handling flammable or highly hazardous chemicals above specified quantities.
**In use:** "This is a PSM-covered process — any change to the procedure goes through MOC, not a field judgment call."
**Common misuse:** Treating PSM procedures as guidelines that can flex based on an operator's in-the-moment assessment — the documented procedure is what the facility's hazard analysis was built around, and deviating from it breaks that basis regardless of how reasonable the deviation seems.

### MOC (Management of Change)
The formal review process required before making any change to equipment, procedures, or operating conditions in a PSM-covered facility, ensuring the change is evaluated against the facility's hazard analysis before implementation.
**In use:** "Good idea, but it needs to go through MOC before we actually run it that way — even a 'safer-seeming' change needs the review."
**Common misuse:** Assuming a change that appears to improve safety doesn't need MOC review — any change, including one intended to improve safety, can have unintended interactions with the existing hazard analysis and needs the same formal review.

### Combustible gas indicator (CGI)
A field instrument that detects and measures the concentration of combustible gas in air, expressed as a percentage of the lower explosive limit (LEL), used for leak detection and confined-space safety checks.
**In use:** "CGI reading at the reported location came back at 15% LEL — that's a real detection, not background noise."
**Common misuse:** Treating any nonzero CGI reading as automatically requiring the same response — the appropriate action scales with the reading's magnitude and location (open air vs. confined space), and a blanket response for any detection misses the actual risk gradient.

### BTU content
A measure of natural gas's energy content per unit volume, used for billing, quality specification, and interoperability with connected pipeline systems.
**In use:** "This gas is coming in below spec BTU — need to check the source blend before it goes further downstream."
**Common misuse:** Treating BTU content as purely a commercial/billing metric disconnected from operational relevance — connected pipeline systems and downstream equipment (like turbines) can have real operational tolerances for BTU content, not just contractual ones.

### Leak survey
A systematic inspection of a pipeline system (using combustible gas detection equipment, often vehicle- or foot-based) to locate gas leaks, performed both on a routine schedule and in response to a specific anomaly.
**In use:** "Anomaly on Section 7 triggered an unscheduled leak survey — found it within the hour."
**Common misuse:** Relying solely on the routine scheduled survey cadence and not triggering an unscheduled survey when SCADA data suggests a possible leak — a routine schedule catches slow, gradual leaks, but a sudden anomaly needs its own immediate investigation, not a wait for the next scheduled pass.

### Odorization
The regulatory-required process of adding a detectable odorant (commonly a mercaptan compound) to otherwise odorless natural gas so leaks are detectable by smell before reaching a hazardous concentration.
**In use:** "Odorization rate's within spec at the injection skid — now we verify it's still detectable at the system's far points."
**Common misuse:** Treating odorization as satisfied once the injection equipment is confirmed running at its specified rate — the regulatory intent is detectability throughout the system, which requires downstream verification, not just injection-point compliance.
