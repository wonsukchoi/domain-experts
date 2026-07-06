### Analysis is being performed directly on original evidence rather than a verified image
- **Usually means:** Metadata (access times, file states) is being altered by the analysis itself, and any finding built this way is not defensible.
- **First question:** Has a forensic image been created and hash-verified, and is all analysis being performed on that image rather than the original device?
- **Data to pull:** Imaging log, hash verification record, analysis workstation access log.

### A live system was powered down before volatile evidence was captured
- **Usually means:** Memory contents, active network connections, and running process state have likely been permanently lost.
- **First question:** Was a memory capture and network connection log taken before the system was powered down or the disk was imaged?
- **Data to pull:** Evidence acquisition log showing order of operations for this specific device.

### A forensic image's hash wasn't verified against the source before analysis began
- **Usually means:** There's no confirmed proof the image is a true, unaltered copy of the original evidence, undermining any conclusion drawn from it.
- **First question:** What is the source device's hash value, and does it match the image's hash exactly?
- **Data to pull:** Source and image hash values (MD5/SHA-256).

### A cross-source timeline compares timestamps without checking each system's clock configuration
- **Usually means:** Clock skew or timezone differences between systems could produce an incorrect event sequence, potentially reversing the actual order of events.
- **First question:** What timezone and clock synchronization configuration does each source system use, and has that been normalized before comparing timestamps?
- **Data to pull:** Each system's clock/timezone configuration, any known clock drift.

### Chain-of-custody documentation begins only once evidence reaches the forensics lab
- **Usually means:** A gap exists from the point of seizure to lab intake that an opposing party can use to challenge the evidence's integrity.
- **First question:** What documentation exists for who handled this evidence and what was done to it between seizure and lab intake?
- **Data to pull:** Full custody log from the moment of seizure forward.

### An expected log or artifact is missing with no further investigation into why
- **Usually means:** This could be evidence of anti-forensic activity (deliberate deletion or wiping) rather than simply an absence of activity.
- **First question:** Is there a corroborating independent source (a separate system's log, a third-party service log) that would be expected to show related activity, and does it show a gap too, or does it remain intact?
- **Data to pull:** The missing artifact's expected location and format, any independent corroborating source.

### A timeline conclusion relies on a single timestamp source with no independent corroboration
- **Usually means:** A single-source timestamp is more vulnerable to clock error, tampering, or misconfiguration than a finding corroborated by an independent source.
- **First question:** Is there a second, independent source (badge logs, a separate service's logs) that corroborates this specific timestamp?
- **Data to pull:** The primary timestamp source, any available independent corroborating log.

### A finding presented in a report doesn't document the specific methodology (imaging tool, hash algorithm, timezone correction) used
- **Usually means:** Without this documentation, another examiner cannot independently verify or reproduce the finding, weakening it under scrutiny.
- **First question:** Does the report specify the imaging tool and hash algorithm used, and how any timezone/clock corrections were determined and applied?
- **Data to pull:** Forensic report's methodology section (or its absence).
