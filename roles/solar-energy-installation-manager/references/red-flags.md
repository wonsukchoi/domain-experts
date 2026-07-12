# Red Flags

### Site survey conducted more than 30 days before crew mobilization with no re-walk scheduled
- **Usually means:** roof penetrations, vent stacks, or a re-roof happened in the gap and the sold design no longer matches the field; second most likely, the original survey measured rafter spacing off a satellite image instead of an attic probe.
- **First question:** "Has anyone been back on this roof since the survey date, and did they carry a tape measure or a phone camera?"
- **Data to pull:** the dated survey report (SunEye/Aurora export) against the permit-submittal date; property records for any roofing permit pulled after the survey date.

### Fall exposure of 6 feet or more with the "infrequent and temporary" exemption invoked
- **Usually means:** the crew wants to skip tie-off on a short job and is citing only the frequency half of the OSHA exemption; second most likely, no one on site can produce the written 15-foot no-approach rule the exemption also requires.
- **First question:** "Show me the written rule barring workers within 15 feet of the unprotected edge — not just that the job is short."
- **Data to pull:** the site-specific safety plan's fall-protection section and the competent-person designation on file for this crew.

### Rapid-shutdown voltage not verified at 30 seconds during commissioning
- **Usually means:** the design software's calculation was trusted without a field measurement; second most likely, the shutdown-initiation label is present but worded or placed in a way the inspector will reject regardless of the actual voltage curve.
- **First question:** "Did we measure inside-boundary voltage at the 30-second mark on this specific string, or are we relying on the datasheet?"
- **Data to pull:** commissioning voltage log at t=30s for in-boundary conductors (target ≤80V) and out-of-boundary conductors (target ≤30V), plus a photo of the installed rapid-shutdown label.

### Redistributed per-point uplift load exceeds the AC428 allowable by any percentage
- **Usually means:** an attachment point was dropped (vent, skylight, unbuildable rafter bay) and the row's design uplift was spread across the remaining points without rechecking the per-point allowable; second most likely, embedment depth at the remaining points was assumed rather than verified.
- **First question:** "After removing that point, what's the new load per remaining fastener, and does it still clear capacity ÷ 1.5?"
- **Data to pull:** the PE's row-level uplift number, remaining attachment-point count, manufacturer withdrawal-capacity table at actual embedment depth, and the AC428 1.5x margin calculation.

### Only one derate applied when sizing a circuit already carrying the NEC 690.8 125% multiplier
- **Usually means:** the continuous-current multiplier was applied and the designer stopped there, skipping ambient-temperature correction and conduit-fill derating; second most likely, the derates were applied in the wrong order and the final ampacity was back-calculated to fit existing wire on hand.
- **First question:** "After the 125% multiplier, what's the ambient-temperature-corrected and conduit-fill-corrected ampacity — not just the 125% number?"
- **Data to pull:** the electrical single-line diagram's derate worksheet, showing all three factors applied in sequence with the final conductor ampacity.

### A single shaded module's production loss modeled as proportional to module count
- **Usually means:** the estimator treated one shaded module out of N as a 1/N output loss instead of accounting for bypass-diode activation dragging the whole string down 30-50%; second most likely, module-level power electronics are assumed present when the as-sold design doesn't include them.
- **First question:** "Does this string have module-level power electronics, or will one shaded module pull the whole string's output down?"
- **Data to pull:** the shading report's solar-access percentage per string (not per-roof average) and the inverter/optimizer bill of materials for that string.

### Permission-to-Operate quoted from a national median instead of the specific utility's published range
- **Usually means:** the estimator pulled a generic PTO timeline instead of checking the interconnecting utility's own published range (commonly 4-6 weeks solar-only vs. 8-12, occasionally 16, weeks with storage); second most likely, overcorrection from a prior missed date has padded every quote to worst case regardless of scope.
- **First question:** "Which utility is this site on, and what's their current published range for this specific configuration — solar-only or solar-plus-storage?"
- **Data to pull:** the per-utility interconnection/PTO tracker, filtered to this utility and this system type (storage attached or not).

### Equipment model numbers differ across the site plan, structural calc, and single-line diagram
- **Usually means:** a mid-design change (module or racking substitution) was updated in one document and not propagated to the others; second most likely, a template from a prior job was reused without a full model-number pass.
- **First question:** "Pull up all three documents side by side — do the module and racking model numbers match on every page?"
- **Data to pull:** the permit-package checklist's model-number cross-reference across site plan, structural calc, and single-line diagram.

### Permit package title block missing jurisdiction, parcel, or contractor-license fields at submittal
- **Usually means:** the package was assembled from a template and the job-specific fields weren't filled in before the deadline to submit; second most likely, a revision was made post-review and the title block wasn't updated to match.
- **First question:** "Has anyone run this package against the title-block checklist since the last edit?"
- **Data to pull:** the permit-package checklist (structural-calc presence, model-number consistency, title-block completeness) dated after the most recent revision.

### Crew mobilized before a survey-driven change order is signed
- **Usually means:** schedule pressure pushed the crew to site before the customer signed off on a scope change discovered in survey; second most likely, the change order was sent but never confirmed received before mobilization.
- **First question:** "Is the signed change order in hand, or are we starting on the assumption the customer will sign later?"
- **Data to pull:** the change-order document with signature timestamp, checked against the crew dispatch date.

### A dropped attachment point or module treated as a fractional loss rather than a full-row loss
- **Usually means:** the estimator subtracted one module or one fastener point from the total count instead of recognizing that racking rail continuity, setback pathways, and per-string electrical design force a full-row loss; second most likely, the redesign was done at the module level without checking whether the row's rail can still be spliced legally at that point.
- **First question:** "Does dropping this one point actually cost us the whole row, once rail continuity and string voltage are rechecked?"
- **Data to pull:** the revised row-level layout with rail-splice locations and the recalculated string voltage/current for the shortened string.

### Site-specific safety supervision assumed covered by crew members' individual NABCEP certification
- **Usually means:** the JTA-certified installer competency is being treated as equivalent to a designated, accountable site safety supervisor; second most likely, no single person on site has been named the competent person for that day's fall-protection and safety decisions.
- **First question:** "Who is the named competent person on this site today, separate from who holds a NABCEP card?"
- **Data to pull:** the site-specific safety plan's competent-person designation log for the current job date.
