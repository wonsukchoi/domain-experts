# Microbiologist — Red Flags

### MALDI-TOF reference-library match score below 1.7
- **Usually means:** ambiguous or low-confidence identification — either a novel/rare organism the library doesn't represent well, or mixed-culture contamination of the plate.
- **First question:** is this a pure isolate, or could the plate be a mixed culture producing a composite spectrum?
- **Data to pull:** original plate image/purity check, repeat sub-culture and re-run MALDI-TOF, escalate to 16S rRNA sequencing if the repeat also scores low.

### Same species recovered from two locations without strain typing
- **Usually means:** a common commensal or environmental organism coincidentally present at both sites, not necessarily a shared contamination event.
- **First question:** has strain-level typing (PFGE or WGS) actually been run, or is this a species-match-only conclusion being reported as "confirmed"?
- **Data to pull:** PFGE gel image or WGS SNP-distance report for both isolates.

### Environmental-monitoring isolate exceeds action level at the same location on 3 consecutive sessions
- **Usually means:** a persistent contamination source (equipment, HVAC, personnel practice) rather than a one-off excursion.
- **First question:** has this location's monitoring history been trended, or is each session being reviewed in isolation?
- **Data to pull:** location-specific trending report across the last 6–12 monitoring sessions.

### Susceptibility panel reports S/I/R for a drug outside the isolate's validated CLSI category
- **Usually means:** lab information system auto-populated a result the breakpoint table doesn't actually cover for that organism.
- **First question:** does a CLSI M100 table entry exist for this exact organism-drug pair?
- **Data to pull:** current CLSI M100 edition, organism category cross-reference.

### Sterility test positive with no matching environmental or personnel isolate found
- **Usually means:** either the source wasn't sampled (blind spot in the monitoring plan) or the contamination originated from the product/component itself, not the environment.
- **First question:** does the environmental monitoring plan actually cover the specific step/location where introduction would be most likely?
- **Data to pull:** monitoring plan coverage map against the process flow, raw-material/component bioburden history.

### Negative retest immediately following a documented positive
- **Usually means:** sampling variability (non-uniform low-level contamination) more often than a false original positive — retests rarely sample the exact same population as the original.
- **First question:** was the original positive root-caused (instrument, media, technique) before the retest was drawn?
- **Data to pull:** original culture's chain of custody and technique documentation, retest sampling location/method versus original.

### Growth-kinetics back-calculated onset window has no corresponding process event
- **Usually means:** either the lab-measured generation time doesn't reflect field conditions (temperature, nutrient availability differ), or the process-records review missed an undocumented event.
- **First question:** were the generation-time measurements taken under conditions matching the suspected field environment?
- **Data to pull:** lab growth-curve raw data and conditions, complete process/access log for the back-calculated window (not just the obvious candidate events).

### Isolate identified only by colony morphology and Gram stain, no confirmatory panel run
- **Usually means:** presumptive identification is being treated as final, typically under turnaround-time pressure.
- **First question:** what identification method actually confirmed this call, and does the consequence of being wrong justify escalating the tier?
- **Data to pull:** the lab's ID-tier decision criteria, whether this result's consequence class requires biochemical/MALDI-TOF/sequencing confirmation.

### Selective/differential medium reports no growth
- **Usually means:** the sample may be genuinely clean, or may contain organisms outside what that medium is designed to recover — a negative is medium-specific, not absolute.
- **First question:** what organism categories does this medium select for, and could the suspected contaminant fall outside that range?
- **Data to pull:** medium specification sheet, parallel non-selective culture result if run.

### Contamination investigation closed with "corrective action: retraining" and no named mechanism
- **Usually means:** the investigation stopped at a plausible-sounding generic cause without tracing a specific, physically supported mechanism.
- **First question:** what evidence (strain match, timeline, process record) supports this specific mechanism over an alternative?
- **Data to pull:** the full investigation file — ID confirmation, strain typing if applicable, timeline back-calculation, process-record cross-reference.
