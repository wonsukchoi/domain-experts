# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

### OOS (Out-of-Specification) vs OOT (Out-of-Trend)

- **Definition:** OOS is a result that falls outside the written specification/acceptance criterion. OOT is a result that falls inside spec but outside the expected historical pattern for that material or process.
- **In use:** "The assay result is in-spec at 98.1%, so it's not OOS — but it's the first result outside our normal 99–101% band in eighteen lots, so I'm logging it OOT and starting a trend investigation, not a formal OOS."
- **Common misuse:** treating "in spec" as "no action needed." OOT results don't require a Phase I/Phase II OOS investigation, but ignoring them is how a real process shift gets discovered only after it produces an actual OOS three lots later.

### Testing into compliance

- **Definition:** the practice of retesting a failing sample repeatedly, with no documented investigation or root cause, until a passing result appears, then reporting only the pass.
- **In use:** "We can't just rerun this dissolution — that's testing into compliance and it's the single most cited finding in OOS-related 483s. Open the Phase I investigation first."
- **Common misuse:** assuming any retest is testing into compliance. A retest is legitimate when it's authorized by a pre-existing SOP, follows a documented assignable-cause finding, and is applied to the number of units the protocol specifies — the violation is the absence of documentation and predefinition, not the act of retesting itself.

### Assignable cause vs common cause

- **Definition:** assignable (special) cause is a specific, identifiable event producing an unusual result (missing sinker, expired standard, instrument fault). Common cause is the routine variation inherent to a stable process, present in every result to some degree.
- **In use:** "The low result traces to a missing sinker — that's assignable, and it's fixable at the source. The ±1.5% lot-to-lot variation we always see is common cause; you don't chase that with a CAPA, you set your control limits around it."
- **Common misuse:** launching a full root-cause investigation into ordinary common-cause variation, or conversely, dismissing a genuine special-cause signal as "just normal variation" because no single result is OOS.

### System suitability

- **Definition:** a set of checks (resolution, tailing factor, replicate-injection precision, retention-time reproducibility) run on an analytical system immediately before or interleaved with sample analysis, confirming the system is performing well enough that day to produce trustworthy data.
- **In use:** "System suitability failed on tailing factor before we even injected the samples — nothing from this sequence counts as data until we fix the column and rerun suitability."
- **Common misuse:** treating system suitability as a once-a-week formality rather than a per-sequence gate; a system that passed Monday can fail suitability Wednesday from column degradation, and Wednesday's samples inherit that failure if suitability wasn't checked that day.

### Cpk vs Ppk

- **Definition:** Cpk is short-term process capability, calculated from within-subgroup variation (assumes the process is in statistical control). Ppk is long-term/overall performance, calculated from total observed variation including between-subgroup shifts.
- **In use:** "Cpk from the last 5 lots looks great at 1.6, but Ppk across the full year is 0.9 — the process is capable in short bursts but something is shifting it between campaigns."
- **Common misuse:** reporting Cpk alone as "the" capability number. Cpk without control-chart confirmation that the process is actually in control is an assumption dressed as a measurement — if the process isn't in control, Cpk is not meaningful and Ppk is the honest number.

### Specification vs action limit vs alert limit

- **Definition:** specification is the regulatory/contractual pass-fail boundary. An action limit is an internal, tighter threshold that triggers investigation before spec is breached. An alert limit is tighter still, a heads-up to watch the trend.
- **In use:** "We're at the alert limit, not the action limit — I'm logging it and watching the next lot, not opening an investigation yet."
- **Common misuse:** collapsing all three into "the spec," which either causes overreaction to every internal alert-limit touch or, worse, means nobody reacts until the actual regulatory spec is already breached.

### Data integrity / ALCOA+

- **Definition:** the principle, and FDA-cited acronym, that a record must be Attributable, Legible, Contemporaneous, Original, and Accurate, plus Complete, Consistent, Enduring, and Available.
- **In use:** "This entry was made two days after the run with no explanation — it fails 'contemporaneous,' and that alone is enough to question the whole record even if the number itself is probably right."
- **Common misuse:** treating ALCOA+ as a paperwork checklist applied after the fact rather than a description of how the record has to be built in real time — you can't retroactively make an entry contemporaneous.

### Retest vs resample vs reanalysis

- **Definition:** retest = reanalyzing the *same* prepared sample. Resample = pulling a *new* physical sample from the batch/lot. Reanalysis = a broader term covering either, usually invoked when reviewing whether the original analytical result itself is suspect.
- **In use:** "The investigation points to a prep error, not a sampling issue, so we retest the same sample — pulling a fresh sample from the tank would be resampling, and that's a different, harder-to-justify decision because it implies the original sample itself was unrepresentative."
- **Common misuse:** using "retest" and "resample" interchangeably; resampling implies the original sample was invalid, which is a much stronger and more consequential claim than a prep or instrument error on an otherwise valid sample.

### Method validation vs method verification

- **Definition:** validation establishes that a method meets required performance characteristics (accuracy, precision, specificity, linearity, range, robustness) for its intended use — done once, by the method's owner, typically on a new or modified method. Verification confirms a *previously validated, compendial* method (e.g., a USP monograph method) performs as expected in your specific lab, on your equipment, with your analysts.
- **In use:** "It's a USP compendial method, so we verify — precision and specificity in our hands — we don't need a full validation package since USP already validated the method itself."
- **Common misuse:** skipping verification entirely because "it's a USP method so it must work here" — a compendial method can still fail in a specific lab due to column, instrument, or matrix differences; verification is required, validation is not, for that case.

### Reference standard vs working standard

- **Definition:** a reference standard (often a compendial standard like USP Reference Standard) is the primary, highest-purity material a result is ultimately traceable to. A working standard is a secondary standard, qualified against the reference standard, used for routine day-to-day testing to conserve the primary material.
- **In use:** "We qualify each new working-standard lot against the current USP Reference Standard before releasing it for routine use — the working standard is what's actually on the bench."
- **Common misuse:** using an unqualified in-house standard as if it carries the same traceability as a compendial reference standard, which breaks the chain of custody a result's accuracy claim depends on.

### AQL (Acceptable Quality Limit) vs zero-defect sampling

- **Definition:** AQL sampling (e.g., ANSI/ASQ Z1.4) accepts a lot with some nonzero, statistically bounded defect rate; it does not guarantee zero defects in the lot, only that the sampled evidence is consistent with the stated quality level.
- **In use:** "An AQL of 1.0 on this sampling plan means we're willing to accept lots averaging around 1% defective in the long run — it is not a zero-defect guarantee, and a customer expecting zero needs a different, more expensive inspection plan."
- **Common misuse:** presenting AQL-based acceptance as equivalent to "we checked and there are no defects" — the entire point of AQL is a defined, nonzero risk tolerance, not a certification of perfection.
