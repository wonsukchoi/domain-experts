# Food Science Technician — Red Flags

Lab-execution smell tests. Format per flag: what it usually means, the first question to ask, the record to pull.

### A result gets retested three or more times until it passes, with no record of the failing runs
- **Usually means:** "Testing into compliance" — the single most common audit finding at the bench level. Either the technician doesn't know every run has to be documented, or knows and is hiding a real problem.
- **First question:** "Show me every run on this sample today, not just the one you're filing."
- **Data to pull:** Raw instrument logs (timestamped) for the full shift, cross-checked against the LIMS entries actually submitted.

### Calibration verification is overdue or skipped on a day a borderline result comes through
- **Usually means:** Production pressure pushed the verification step to "later," and the borderline result may be a drifted instrument, not a real product issue — but nobody can tell without the check.
- **First question:** "When was this instrument last verified against a reference standard, and can I see that log?"
- **Data to pull:** Calibration/verification log for the instrument, timestamped against the sample-run log.

### A Zone 2 or Zone 3 environmental positive is closed out after one clean re-swab
- **Usually means:** The positive signaled a harborage point (equipment frame, drain, low-traffic surface) that a single clean sample doesn't rule out — organisms in biofilm can survive a surface clean and reappear.
- **First question:** "How many vector swabs were taken around the positive site, and over how many rounds?"
- **Data to pull:** The full intensified-swabbing map and results across at least two rounds, not just the re-swab of the original point.

### Moisture content is reported as a proxy for water activity
- **Usually means:** Someone treated %moisture and aw as interchangeable because they're usually correlated — true for a homogeneous, unchanged formulation, false the moment an ingredient (humectant, sugar type) or mix uniformity changes.
- **First question:** "Was aw actually measured on this batch, or inferred from moisture?"
- **Data to pull:** The aw instrument's raw log for the batch in question; if absent, that's the finding.

### A near-spec result is accepted on a single reading, no replicate
- **Usually means:** Time pressure skipped the triplicate the SOP calls for near a control limit, so the accepted number could be within normal instrument noise of failing.
- **First question:** "Was this run in replicate, and what's the spread across replicates?"
- **Data to pull:** All replicate values for the sample, not just the one recorded on the batch record.

### LIMS entries for a shift are all timestamped within a narrow window at shift end
- **Usually means:** Results were recorded on paper or memory during the shift and batch-entered later, breaking the contemporaneous-record expectation (ALCOA+) and opening the door to transcription drift or after-the-fact "smoothing."
- **First question:** "Where's the original bench sheet or instrument printout this entry was transcribed from?"
- **Data to pull:** Raw bench notes/instrument printouts for the shift, compared timestamp-by-timestamp against LIMS entry times.

### A sensory panel was pulled from "whoever's on the floor" for a difference test
- **Usually means:** The panel is underpowered or unscreened, so a non-significant result gets reported as "no difference" when it's actually "no ability to detect one."
- **First question:** "How many panelists, were they screened, and does that meet the protocol's minimum n?"
- **Data to pull:** Panelist roster against the protocol's screening criteria and minimum-count requirement.

### A reagent, media, or standard is in use past its labeled expiry, or with no positive-control check on record
- **Usually means:** Nobody caught the expiry during setup, or the positive-control check that would catch a dead reagent lot was skipped to save time.
- **First question:** "What's the expiry date on this lot, and where's today's positive-control result?"
- **Data to pull:** Reagent/media lot receiving log and today's positive-/negative-control plate or standard-check result.

### A control chart shows 6+ consecutive points trending toward a limit, but every point is still "in spec"
- **Usually means:** A slow drift (calibration creep, raw-material lot shift, seasonal environmental change) is underway that pass/fail spec checks alone won't catch until it's already failed.
- **First question:** "Has anyone looked at the trend, or only the individual pass/fail calls?"
- **Data to pull:** The control chart itself for the parameter, at least 20 points back.

### A supplier certificate of analysis (COA) is filed without a technician-level field match to the purchase spec
- **Usually means:** The COA's presence was treated as sufficient without checking that its specific values (allergen statement, micro limits, moisture) actually match what was ordered for this lot.
- **First question:** "Does this lot's COA match the approved spec field-by-field, or just generally look right?"
- **Data to pull:** The COA for the specific lot received, side by side with the approved ingredient specification sheet.
