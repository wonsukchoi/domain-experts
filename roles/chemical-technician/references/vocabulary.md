# Vocabulary

### Control chart (Shewhart chart)
A run chart of a QC or calibration-check value over time, plotted against a centerline (historical mean) and statistical control limits (typically ±2σ warning, ±3σ action), derived from baseline data — not from the spec limit.
**In use:** "The check standard's still inside spec, but it's tripped Rule 6 on the control chart — hold it and get the titrant restandardized before we release anything else off this batch."
**Common misuse:** Treating "inside spec" and "in statistical control" as the same thing — a result can pass spec every day for a week while the chart shows it's already drifting toward failure.

### Nelson Rules / Western Electric Rules
A standard set of run-rule tests (single point beyond 3σ, 2 of 3 beyond 2σ, 6+ points trending, 8+ points on one side of center, etc.) applied to a control chart to detect non-random, "special cause" variation before it produces an out-of-spec result.
**In use:** "That's not just noise — five points in a row moving the same direction is a Rule 6 flag, not a coincidence."
**Common misuse:** Applying only the single-point 3σ rule and ignoring the trend/run rules, which catch drift days or weeks earlier.

### NIST-traceable
A reference standard or calibration weight whose value is linked, through an unbroken chain of comparisons, to a National Institute of Standards and Technology (or equivalent national) primary standard, with a certificate documenting that chain.
**In use:** "Pull the cal weight's cert before you sign off — if it's past its recertification date, today's balance check isn't traceable and neither is anything weighed on it."
**Common misuse:** Assuming any certificate labeled "NIST-traceable" is automatically current — the traceability claim expires with the certificate, not the physical weight.

### Chain of custody (COC)
The documented, unbroken record of who possessed a sample, when, and under what conditions, from collection through disposal — required for any result that may need to hold up in a regulatory, legal, or accredited context.
**In use:** "The extraction looks clean, but there's a four-hour gap on the COC between receipt and login — that has to be explained before this result goes anywhere."
**Common misuse:** Treating COC as paperwork that can be backfilled after the fact; a COC completed retroactively is functionally broken even if every transfer actually happened as described.

### Method blank
A sample matrix carried through the entire analytical procedure with no target analyte added, run to detect contamination introduced by reagents, glassware, or the process itself — distinct from a calibration blank, which only zeroes the instrument.
**In use:** "Method blank's showing a peak above the MDL — check what ran right before it in the sequence before we trust any of today's low-level results."
**Common misuse:** Confusing a method blank with a calibration/instrument blank; a clean instrument blank says nothing about contamination introduced during sample prep.

### Matrix spike / spike recovery
A sample matrix spiked with a known amount of the target analyte and carried through the full method, used to check whether the method recovers accurately in that specific real-world matrix (not just in a clean standard).
**In use:** "Recovery on the matrix spike came back at 68% against an 80–120% acceptance window — something in this sample matrix is suppressing the signal, run a dilution before reporting."
**Common misuse:** Skipping the matrix spike because the method validated fine on clean standards — validation on standards doesn't guarantee recovery in every real sample matrix.

### Chemical Hygiene Plan (CHP)
The written, site-specific plan required under OSHA's Laboratory Standard (29 CFR 1910.1450) covering exposure controls, PPE requirements, and emergency procedures for a specific lab's actual chemical inventory and processes.
**In use:** "That solvent's not on the standard PPE list in the CHP for this bench — check with EHS before you start using it here."
**Common misuse:** Treating a generic safety training as equivalent to the site's CHP; the CHP is specific to the lab's actual chemicals and processes, not a one-size template.

### Contemporaneous documentation
Recording data (readings, timestamps, initials, observations) at the time the work happens, not reconstructed afterward from memory — the core requirement behind "if it isn't written down, it didn't happen" under GLP.
**In use:** "Log the balance reading now, not after you finish the whole batch — reconstructing it at the end of shift is exactly what an audit flags."
**Common misuse:** Believing accurate after-the-fact recall is equivalent to contemporaneous entry — in a regulated lab, the timing of the entry is itself part of the data's integrity, not just its accuracy.

### Out-of-specification (OOS) vs. out-of-trend (OOT)
OOS is a result that fails a defined acceptance/spec limit; OOT is a result that's still inside spec but inconsistent with the established trend or history for that sample/method — OOT can, and should, trigger investigation before it ever becomes OOS.
**In use:** "It's not OOS, it's OOT — three consecutive stability pulls trending down faster than the historical rate. That's worth flagging now, not waiting for it to actually fail."
**Common misuse:** Only having a procedure for OOS and treating OOT results as non-events because they technically pass.

### LIMS (Laboratory Information Management System)
Software system tracking samples, results, instrument data, and chain of custody from login through final report, serving as the authoritative record in most modern labs.
**In use:** "Don't email the result around — log it in the LIMS with the instrument file attached, that's the record of truth if this ever gets audited."
**Common misuse:** Treating a spreadsheet or notebook copy as equally authoritative once the LIMS entry exists; discrepancies between the two become their own finding.

### Satellite accumulation area (RCRA)
A location at or near the point of hazardous-waste generation where waste may accumulate without a formal storage permit, subject to strict limits (commonly a 55-gallon cap per waste stream and a requirement to move to a central accumulation area promptly once full) under RCRA.
**In use:** "That drum's been sitting since November with no accumulation-start date on the label — that's not a satellite area anymore, that's an unpermitted storage violation waiting to happen."
**Common misuse:** Assuming "satellite accumulation" means indefinite on-site storage; the exemption depends on active generation and prompt transfer once volume/time limits are reached.

### Proficiency testing (PT) sample
A sample with a known (but blind to the analyst) reference value, sent by an accrediting body or PT provider, analyzed exactly as a routine sample to independently verify a lab's method performance.
**In use:** "PT results came back — we're within the acceptable z-score range on everything except the trace-metals panel, so that method's getting a full review before the next PT round."
**Common misuse:** Treating a PT sample differently (extra care, repeat runs, cherry-picked analyst) from routine samples — that defeats the entire point of blind proficiency testing.

### System suitability
A set of checks (resolution, tailing factor, replicate precision, retention time reproducibility, depending on the method) run on an instrument system immediately before sample analysis, confirming the system is performing adequately for that specific run — not a one-time instrument qualification.
**In use:** "System suitability failed on peak tailing this morning — don't run samples on this column until that's resolved, even though the instrument passed its annual qualification fine."
**Common misuse:** Confusing system suitability (a same-day, per-run check) with instrument qualification/validation (a periodic, broader check) — passing one doesn't substitute for the other.

### Certified Reference Material (CRM)
A reference material with a certified property value and stated uncertainty, issued by an accredited producer, used to verify method accuracy against a value with documented, traceable provenance — distinct from an in-house or vendor "reference standard" without that certification chain.
**In use:** "Use the CRM for the accuracy check, not the in-house stock solution — we need the certified uncertainty on file for the audit."
**Common misuse:** Treating any purchased "standard" as a CRM; only materials with an accredited certificate of analysis and stated measurement uncertainty qualify.
