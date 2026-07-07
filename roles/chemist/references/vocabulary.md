# Chemist — Vocabulary

### Specificity
A method's ability to distinguish the analyte from everything else that might be present (impurities, degradants, matrix components) without interference.
**In use:** "The method's specific for the parent compound, but we haven't confirmed it's specific against the oxidative degradant yet."
**Common misuse:** treated as synonymous with "selective" or assumed proven just because the standard's peak looks clean — specificity has to be demonstrated against real interferents (forced degradation, matrix), not inferred from a clean reference-standard chromatogram.

### LOD (Limit of Detection)
The lowest concentration reliably distinguishable from noise (commonly S/N=3), without implying the value is quantitatively trustworthy.
**In use:** "We're seeing a peak at 0.02%, that's right around LOD — call it detected, not quantifiable."
**Common misuse:** confused with LOQ; a result at LOD gets reported as "present" or "not detected," never as a precise percentage.

### LOQ (Limit of Quantitation)
The lowest concentration at which a result carries validated accuracy and precision (commonly S/N=10).
**In use:** "0.06% is our LOQ — anything below that we report as below-LOQ, not as a number."
**Common misuse:** treated as a soft guideline rather than a hard reporting boundary; results below LOQ get reported as exact values anyway.

### Mass balance (synthesis context)
Accounting for a reaction's input mass across product, recovered starting material, and identified byproducts/losses, to explain where the theoretical yield actually went.
**In use:** "The mass balance only accounts for 88% — we're missing 12% somewhere, probably the aqueous workup."
**Common misuse:** conflated with a "yield calculation" — yield is one number; mass balance is the accounting that explains the gap between theoretical and actual.

### Peak purity (spectral/chromatographic)
A diagnostic (commonly PDA-based) confirming a chromatographic peak represents a single component, not an unresolved co-elution.
**In use:** "Peak purity angle is under threshold, so we're confident that's one compound, not two riding together."
**Common misuse:** assumed automatically satisfied by a "clean-looking" peak shape — co-eluting compounds with similar retention and similar UV spectra can pass a visual check and still fail the purity-angle diagnostic, or vice versa.

### System suitability
A set of checks (resolution, tailing factor, theoretical plates, replicate %RSD) run before a batch of samples to confirm the instrument/method is performing acceptably that day.
**In use:** "System suitability passed, so the instrument's fine — if this sample fails, it's not the system."
**Common misuse:** run once at method validation and assumed to hold forever; system suitability is a per-sequence check, not a one-time certification.

### Robustness (method validation)
A method's resistance to small, deliberate variations in operating parameters (flow rate, temperature, mobile-phase composition) without a meaningful change in result.
**In use:** "We flexed %B by ±2 and flow by ±0.1 — still within 3% of nominal, method's robust."
**Common misuse:** confused with "ruggedness" (inter-lab/inter-analyst reproducibility) — robustness is about small parameter changes within one lab, ruggedness is about transfer across labs/analysts.

### Out-of-specification (OOS) result
A test result falling outside the established acceptance criteria, triggering a formal investigation before disposition.
**In use:** "That's an OOS — we open the investigation before anyone touches a retest."
**Common misuse:** treated as a synonym for "bad result to retest away," when it is formally a triggering event requiring documented root-cause investigation regardless of what a retest later shows.

### Forced degradation
Deliberately stressing a compound (heat, humidity, light, acid/base, oxidation) beyond normal storage conditions to generate degradation products and confirm a method can resolve them from the parent.
**In use:** "Run the 60°C/75%RH forced-deg sample before we call this method stability-indicating."
**Common misuse:** skipped or treated as optional when a method just needs to pass an initial validation — without it, specificity against real-world degradants is unverified.

### Stability-indicating method
A method demonstrated (via forced degradation) to resolve the parent compound from its likely degradation products, not just from unrelated impurities.
**In use:** "This method's validated for release, but it's not stability-indicating yet — don't use it for the shelf-life program."
**Common misuse:** assumed automatically true of any validated release method — specificity against process impurities does not prove specificity against degradation products, which are chemically different.

### Theoretical yield
The maximum possible product mass calculable from stoichiometry, assuming complete conversion and no losses.
**In use:** "Theoretical's 14.2 g at this scale — we isolated 11.7 g pure, so we're at 82%."
**Common misuse:** calculated from the wrong limiting reagent, or without accounting for a reagent used in excess, inflating or deflating the reported percent yield.

### Recovery (accuracy validation)
The percentage of a known spiked amount that a method successfully measures back, used as the accuracy check.
**In use:** "Recovery's consistently 99–101% across all three spike levels — accuracy's solid."
**Common misuse:** checked only at one concentration level near the specification limit, missing a recovery bias that only shows up at the low or high end of the range.

### Retention time (RT) shift
A change in when a compound elutes from run to run, used as an early warning of column or method drift.
**In use:** "RT's crept 0.15 min over the last twenty injections — check the column before we trust the next batch."
**Common misuse:** ignored as long as integration "still works," even though a drifting RT can eventually co-elute with a neighboring peak and silently corrupt results.
