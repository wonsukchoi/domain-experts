# Food Scientist — Red Flags

### Single-temperature accelerated study (only one elevated condition tested)
- **Usually means:** Someone needed a fast shelf-life number and skipped the second/third temperature point needed to actually fit a Q10 or Arrhenius curve.
- **First question:** "What's the confidence interval on this extrapolation, and how many temperature points support it?"
- **Data to pull:** The raw ASLT design — number of temperature conditions and whether a real-time control run is in progress.

### Q10 assumed without identifying the failure mechanism
- **Usually means:** A default Q10 (often 2 or 3) was applied without checking whether the degradation is chemical (oxidation/browning) or physical (staling/moisture migration) — the latter has a much lower Q10.
- **First question:** "What specifically failed on the panel — flavor/color (chemical) or texture (physical)?"
- **Data to pull:** The panel's descriptive comments or attribute scores at the failure point, not just the pass/fail date.

### Printed shelf life equals the tested failure point, with no safety margin
- **Usually means:** The 70-80% safety-margin fraction was skipped, or the person setting the date didn't know it existed.
- **First question:** "Is this the day panelists first detected a difference, or the day we decided to print on the label?"
- **Data to pull:** The ASLT report's stated failure day vs. the label copy's printed date.

### Hedonic ("liking") score used to justify a shelf-life extension
- **Usually means:** A liking score held steady near the failure point, which was read as "no meaningful change" — but liking and detectability are different questions.
- **First question:** "Was a difference test (triangle/duo-trio) run alongside the hedonic panel, and did it also come back non-significant?"
- **Data to pull:** Both the hedonic scores and any parallel difference-test p-value.

### Reformulation sensory panel run, but no water-activity or pH re-test
- **Usually means:** The change was treated as flavor-only because the sensory profile looked unchanged, missing a shift in free water or acidity that changes microbial risk.
- **First question:** "Did the ingredient change move total sugar, salt, fat, or moisture by more than 5% relative?"
- **Data to pull:** Before/after water-activity (aw) and pH measurements for the reformulated product.

### CCP list includes a step with no measurable control action
- **Usually means:** A plausible-sounding hazard got listed as a CCP without a specific critical limit and monitoring method attached — often because "could contaminate" was confused with "can be controlled and verified here."
- **First question:** "What's the critical limit at this step, and who measures it, at what frequency?"
- **Data to pull:** The HACCP plan's monitoring column for that line item — if it's blank or vague ("visual inspection, periodically"), the CCP designation is likely wrong.

### Metal-detector or CCP monitoring log has gaps or unexplained interpolation
- **Usually means:** Monitoring frequency wasn't actually met, and the log was filled in after the fact.
- **First question:** "Can you show me the raw timestamped log, not the summary sheet?"
- **Data to pull:** Original monitoring records for the shift/day in question, cross-checked against production run times.

### Allergen cross-contact control relies on cleaning alone, with no verification swab
- **Usually means:** A changeover cleaning procedure exists on paper but isn't verified to actually remove allergen residue below a detectable threshold.
- **First question:** "When was this cleaning procedure last validated with an ELISA or lateral-flow allergen swab test?"
- **Data to pull:** Most recent allergen-verification swab results for the shared line.

### Shelf-life claim extended based on accelerated data alone, no real-time confirmation
- **Usually means:** The product shipped on an extrapolated number before the real-time (non-accelerated) control run reached the same age, so the extrapolation model is still unvalidated against ground truth.
- **First question:** "Has the real-time control sample reached the claimed shelf-life age yet, and did it pass?"
- **Data to pull:** Real-time study timeline and current elapsed time vs. the claimed shelf life.

### Supplier certificate of analysis (COA) accepted without matching allergen/spec fields
- **Usually means:** Receiving accepted a COA on file presence alone, not a field-by-field match against the purchase spec (especially allergen statements).
- **First question:** "Does this lot's COA allergen statement match our approved supplier spec exactly, including 'may contain' language?"
- **Data to pull:** The specific COA for the lot in question, side by side with the approved ingredient specification.
