# Nuclear Engineer — vocabulary

### Defense-in-depth
Multiple independent, diverse layers of protection such that no single failure defeats the safety function.
**In use:** "That design only credits defense-in-depth if the backup train doesn't share a power bus with the primary."
**Common misuse:** treating two redundant components as "defense-in-depth" even when they share a common-cause vulnerability (same room, same power source) — redundancy without independence isn't defense-in-depth.

### ALARA (As Low As Reasonably Achievable)
The principle that radiation dose should be minimized below the regulatory limit whenever the further reduction is cost-effective, not just kept under the legal limit.
**In use:** "We're under the dose limit, but ALARA says we still owe a cost-benefit check before calling this final."
**Common misuse:** assuming "under the regulatory limit" satisfies ALARA — ALARA is a separate, lower design objective with its own cost-benefit test.

### Core Damage Frequency (CDF)
The predicted frequency (events per reactor-year) of an accident sequence leading to significant reactor core damage, computed from the plant's PRA model.
**In use:** "That maintenance deferral would push our CDF contribution from this train above the safety goal benchmark."
**Common misuse:** treating CDF as a single fixed plant number rather than something that shifts with maintenance state, operating mode, and specific configurations being evaluated.

### Large Early Release Frequency (LERF)
The predicted frequency of an accident sequence resulting in a large, early (before effective protective action) release of radioactive material — a second NRC safety goal alongside CDF.
**In use:** "This containment bypass sequence matters for LERF even though its CDF contribution is small."
**Common misuse:** conflating LERF with CDF — a sequence can be a small CDF contributor but a large LERF contributor if it bypasses containment.

### Fussell-Vesely importance
A PRA importance measure: the fraction of total risk (CDF/LERF) attributable to a component's failure, given how it currently performs.
**In use:** "Its Fussell-Vesely is low because it rarely fails — that's not the same as it not mattering if it does."
**Common misuse:** using Fussell-Vesely alone to deprioritize a component's maintenance, ignoring Risk Achievement Worth.

### Risk Achievement Worth (RAW)
A PRA importance measure: how much risk (CDF/LERF) would increase if a component were assumed failed — captures components that rarely fail but matter enormously when they do.
**In use:** "RAW on that valve is 22 — treat it as Tier 1 even though it's never failed in twenty years."
**Common misuse:** ignoring RAW because a component's failure history looks clean — a clean history and a critical function aren't mutually exclusive.

### 10 CFR 50.59
The NRC regulation governing whether a facility can make a change to its licensing basis without prior NRC approval, based on specific screening criteria (margin of safety, new accident possibility, Tech Spec limits).
**In use:** "This change screens out of 50.59 because it doesn't touch a Tech Spec limit or a described design function — document the screening and proceed."
**Common misuse:** treating 50.59 screening as a formality that can be done from memory rather than against the actual FSAR description of the affected function.

### Final Safety Analysis Report (FSAR)
The licensing-basis document describing the plant's design, safety analyses, and operating limits — the reference document every 50.59 screening and design change is checked against.
**In use:** "Pull the FSAR section on this system before we conclude the change doesn't affect a described design function."
**Common misuse:** assuming current as-built or as-operated plant configuration matches the FSAR without checking — configuration drift from the licensing basis is itself a finding.

### Half-Value Layer (HVL)
The thickness of a given shielding material that reduces radiation intensity by half; shielding thickness is sized in whole HVLs against a required attenuation factor.
**In use:** "We need 850x attenuation, which is 9.73 HVLs — round up to 10, not down."
**Common misuse:** rounding a fractional HVL count down to save material cost, which under-shields the design target.

### Cumulative Usage Factor (CUF)
A fatigue-tracking metric (per ASME Section III) summing the fraction of allowable fatigue cycles consumed by actual operating transients, compared against a limit of 1.0.
**In use:** "CUF on that nozzle is at 0.71 after the load-following campaign — re-baseline before the next uprate evaluation."
**Common misuse:** treating CUF as a one-time calculation at initial licensing rather than a running total that needs re-evaluation after operating-mode changes (e.g. starting load-following).

### Common-cause failure
The failure of multiple redundant components from a single shared cause (fire, flood, seismic event, design/manufacturing defect, shared maintenance error) rather than independent random failure.
**In use:** "Both trains are in the same fire zone — that's a common-cause vulnerability, not redundancy."
**Common misuse:** modeling redundant components as statistically independent in a risk argument without checking for shared location, power, or human-action dependencies.

### Design-basis accident
A postulated accident scenario the plant's safety systems must be designed to withstand, analyzed with mandated conservative assumptions (not best-estimate).
**In use:** "The design-basis LOCA analysis has to use the Appendix K conservative assumptions, not the realistic best-estimate method, unless the plant has NRC approval for the alternative methodology."
**Common misuse:** substituting a best-estimate result for the design-basis conservative result because it produces a more favorable margin.

### Technical Specifications (Tech Specs)
The legally binding operating limits and surveillance requirements for a licensed facility, derived from and cross-referenced to the FSAR safety analyses.
**In use:** "That surveillance interval extension needs a Tech Spec amendment, not just an internal engineering evaluation."
**Common misuse:** treating Tech Specs as internal guidance that can be locally waived for schedule reasons — they are licensed, enforceable limits.
