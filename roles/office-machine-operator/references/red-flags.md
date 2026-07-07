# Office Machine Operator — Red Flags

### Same jam code returns after one clear-and-test cycle
- **Usually means:** A worn part (fuser roller, pickup roller, sensor) rather than a one-off paper problem; sometimes a stock issue that a single test sheet didn't reproduce.
- **First question:** Did the test sheet come from the same stock/tray as the failure, or a different one?
- **Data to pull:** Machine's jam-history log for this code over the past 30 days; impression count since last preventive-maintenance service.

### Jam frequency rises sharply on one specific stock lot, not others
- **Usually means:** Grain-direction mismatch or a bad mill lot (moisture, thickness variance) in that specific reorder, not a machine fault.
- **First question:** Is this stock from the same vendor/lot as prior reorders, or a new lot?
- **Data to pull:** Stock packaging lot number; grain-direction spec vs. machine's feed-path requirement.

### Postage-meter dollar total is off but piece counter matches the manifest
- **Usually means:** A rate-class or weight-break error, not a duplicate/skipped run.
- **First question:** Did every piece in this run qualify for the rate class used, or were some over the weight break?
- **Data to pull:** Sample-weigh a handful of pieces from the run against the rate class's weight limit.

### Postage-meter piece counter doesn't match the manifest piece count
- **Usually means:** A jam-recovery restart re-ran part of the batch, or a batch was split across two runs and one piece-count wasn't reconciled.
- **First question:** Was there a jam or interruption mid-run, and if so, was the restart point confirmed?
- **Data to pull:** Job's run log for any pause/restart events during this job.

### Three or more power-cycles on the same job within an hour
- **Usually means:** An operator is treating a developing hardware fault as a routine paper jam and escalation is overdue.
- **First question:** Has this exact error code appeared on this machine in the past week?
- **Data to pull:** Machine's error-code history across the past 7 days, not just today.

### A short job (low page count) consistently runs behind schedule
- **Usually means:** The job's setup complexity (multi-part stock, tight registration, unusual finishing) isn't reflected in a page-count-only schedule.
- **First question:** What's the setup time for this job type versus its run time?
- **Data to pull:** Actual elapsed time for the last three runs of this job type, split into setup vs. run.

### Output shows banding or density variation with no jam reported
- **Usually means:** A consumable (toner/developer) is near end-of-life, not a paper-path fault — jam-code diagnostics won't find it.
- **First question:** What's the page count on the current cartridge/developer unit versus its rated yield?
- **Data to pull:** Consumable-life counter from the machine's supply-status screen.

### A rush job is inserted mid-run on a multi-set collated job
- **Usually means:** The re-registration/re-collation cost of stopping mid-set is about to exceed the time saved by not waiting for the current set to finish.
- **First question:** Is the rush job's deadline inside the time remaining on the current set, or does it just feel urgent?
- **Data to pull:** Remaining run time on the current set vs. the rush job's actual required completion time.

### Meter needs a reset (funds added) mid-run
- **Usually means:** The job was larger than the funded amount anticipated, or a prior job wasn't reconciled before this one started.
- **First question:** Was the prior job's postage reconciled and logged before this run started?
- **Data to pull:** Prior job's discrepancy log entry, if any.
