# Red flags

### Time study run for fewer cycles than the minimum-cycles check (N') requires
- **Usually means:** the analyst never ran N' against the observed variance, or stopped early against schedule pressure and never revisited it.
- **First question:** what confidence/precision was this study specified to hit, and was N' computed from the pilot cycles or just assumed?
- **Data to pull:** raw cycle-by-cycle times, Σx and Σx² for the highest-variance element, the stated target confidence/precision.

### Work-sampling percentage reported with no confidence interval
- **Usually means:** the analyst treated the point estimate as the finding instead of computing e = z√(p̂(1−p̂)/n).
- **First question:** what was n, and what's the half-width at the stated confidence?
- **Data to pull:** raw tally counts by category, n, the target precision the study was sized against.

### Rating factor identical across every element in a manual cycle
- **Usually means:** rating wasn't assessed element-by-element — either copied from a template or applied once to the whole cycle.
- **First question:** which elements, if any, are machine-paced and should be locked at 100 regardless?
- **Data to pull:** the element-by-element rating sheet, not just the summary NT.

### PFD allowance unchanged for 2+ years after a documented process or ergonomics change
- **Usually means:** nobody re-ran a work-sampling study after the change; the book/table value is being carried forward by default.
- **First question:** when was this allowance last validated, and did the process change plausibly move the delay percentage up or down?
- **Data to pull:** the last work-sampling study's date and result, the process-change log for this station.

### Standard time set from the fastest cycle observed, not the rated mean
- **Usually means:** the analyst picked the best-case reading instead of computing OT×rating across the full retained sample.
- **First question:** what's the mean of all retained cycles, and what rating was applied to it?
- **Data to pull:** full raw cycle sheet, not just the reported "representative" time.

### Foreign element or outlier excluded with no logged cause or threshold
- **Usually means:** an inconvenient high reading was dropped by feel rather than against a documented ±3σ or assignable-cause rule.
- **First question:** what threshold or event justified excluding this reading, and where's it logged?
- **Data to pull:** the foreign-element/outlier log; if none exists, that absence is itself the finding.

### Work-sampling observations clustered in one part of the shift
- **Usually means:** the "random" schedule wasn't actually random — observations were taken whenever convenient (e.g., all before lunch).
- **First question:** what generated the observation times — a random-interval tool, or the observer's own schedule?
- **Data to pull:** timestamps of every observation, checked for even spread across the shift and across days.

### A station running >110% of its assigned standard for 2+ consecutive shifts, unaddressed
- **Usually means:** the standard is stale, the line has drifted (tooling wear, a methods change nobody logged), or the balance itself needs re-work.
- **First question:** is this a measurement issue (re-time it) or a real drift (escalate to the IE of record)?
- **Data to pull:** re-timed samples from the last 2+ shifts, any recent methods or tooling changes at that station.

### A "standard" with no traceable time study behind it
- **Usually means:** the number was inherited from a spreadsheet, a prior employee's notes, or engineering judgment with no study ever run.
- **First question:** can anyone produce the original study — raw cycles, rating, allowance — or is this number unsupported?
- **Data to pull:** the study file/ID this standard is supposed to trace to.

### Two technicians' studies on the same job diverging by more than 10% with no reconciliation
- **Usually means:** inconsistent rating practice between the two, or one study undercounted cycles/mis-sized the sample.
- **First question:** were both studies rated against the same reference pace (e.g., both trained on the same benchmark films)?
- **Data to pull:** both raw studies side by side — element breakdown, ratings, sample sizes.

### Machine-paced element rated above or below 100
- **Usually means:** the analyst rated the whole cycle as one block instead of locking the machine-controlled portion at 100.
- **First question:** which portion of this element's time is actually operator-controlled versus fixed by the machine cycle?
- **Data to pull:** the machine's cycle-time spec for that operation, compared against the rated element time.

### Allowance percentage borrowed from a mismatched job class
- **Usually means:** a generic or nearby line's PFD allowance (e.g., light assembly) was applied to a job with materially different physical demand (e.g., heavy foundry work) without checking the table's job-class breakdown.
- **First question:** which ILO (or internal) table category does this specific job's physical demand actually match?
- **Data to pull:** the table's category definitions and the job's actual demand characteristics (weight handled, posture, environment).
