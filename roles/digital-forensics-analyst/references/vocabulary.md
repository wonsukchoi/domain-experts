### Write-blocker
A hardware or software tool that allows read-only access to a storage device, preventing any write operation from altering the original evidence during imaging.
**In use:** "The disk was imaged through a write-blocker to ensure the original wasn't modified during acquisition."
**Common misuse:** Connecting original evidence directly to an analysis workstation without a write-blocker, risking inadvertent modification of the evidence.

### Forensic image
A bit-for-bit copy of a storage device, including all allocated and unallocated space, used for analysis in place of the original evidence.
**In use:** "All analysis is performed on the forensic image, never the original laptop."
**Common misuse:** Treating a standard file-level copy (which misses unallocated space and deleted-file remnants) as equivalent to a full forensic image.

### Hash verification
The process of computing a cryptographic hash (e.g., SHA-256) of both the original evidence and its forensic image, confirming they match exactly to prove the image is an unaltered copy.
**In use:** "Source and image hashes matched exactly — the image is verified as a true copy."
**Common misuse:** Skipping hash verification or only checking file sizes, which doesn't confirm bit-for-bit integrity the way a cryptographic hash comparison does.

### Order of volatility
The principle (formalized in RFC 3227) that evidence should be collected in order from most perishable (registers/cache, memory, network state) to least perishable (disk, archival media), since capturing less volatile evidence first risks losing the more perishable evidence permanently.
**In use:** "We captured the memory dump and network connections before powering down the system, per order of volatility."
**Common misuse:** Imaging the disk first (or powering down the system) before capturing memory and network state, permanently losing volatile evidence.

### Chain of custody
The documented, unbroken record of who has handled, accessed, or transferred evidence from the moment of seizure through final analysis and disposition.
**In use:** "Chain of custody starts at 9:03 AM with the initial seizure, not when the device reached the forensics lab."
**Common misuse:** Beginning custody documentation only once evidence formally enters a lab intake process, leaving an undocumented gap from the point of seizure.

### Clock skew
The difference between a system's internal clock and actual (correct) time, or between two systems' clocks, which can distort the apparent sequence of events if not corrected for.
**In use:** "This system's clock was configured to UTC while the organization operates in Eastern time — a 5-hour skew that needed correcting before building the timeline."
**Common misuse:** Comparing timestamps from different systems at face value without checking for clock skew or timezone configuration differences.

### Timestomping
An anti-forensic technique that alters a file's timestamp metadata to conceal when it was actually created, modified, or accessed.
**In use:** "The file's modified timestamp doesn't align with any other activity on the system — that's consistent with timestomping."
**Common misuse:** Trusting file timestamps at face value without cross-checking them against other independent activity indicators when tampering is a plausible concern.

### Anti-forensic activity
Deliberate actions taken to destroy, alter, or obscure digital evidence — including log wiping, timestomping, secure deletion, and encryption — used to hinder an investigation.
**In use:** "The gap in the event log, combined with the intact external service log, is consistent with anti-forensic log wiping."
**Common misuse:** Treating missing expected evidence as simply an absence of activity rather than actively investigating whether it reflects deliberate anti-forensic action.

### Volatile evidence
Evidence that exists only while a system is running or in a particular state and is lost when the system is powered down or its state changes — RAM contents, active network connections, running processes.
**In use:** "Volatile evidence like the memory dump had to be captured before the laptop was shut down for imaging."
**Common misuse:** Treating volatile evidence as recoverable after the fact, when in most cases it's permanently lost once the system state changes.

### Metadata (forensic analysis)
Data about data — file creation/modification/access timestamps, file system attributes, and similar descriptive information — often as forensically significant as the file's content itself.
**In use:** "The file's content wasn't unusual, but its metadata showed it was accessed at a time inconsistent with the user's claimed activity."
**Common misuse:** Focusing analysis only on file content while overlooking metadata, which often carries critical timeline and authenticity information.
