# Vocabulary

Terms generalists blur together that a technical director/facility engineer keeps sharply separate — the separation is usually where the actual decision lives.

### Genlock vs. PTP
**Genlock** is the traditional SDI-era practice of distributing a single reference signal (black burst or tri-level sync) over coax so every device's frame timing aligns. **PTP** (Precision Time Protocol, IEEE 1588, profiled for media as SMPTE ST 2059) is the IP-era equivalent, distributing time-of-day and frequency reference over the same IP network the video travels on, from a grandmaster clock.
**In use:** "We're not genlocked in this facility anymore — everything hangs off the PTP grandmaster, so check the boundary clock offset, not a tri-level signal."
**Common misuse:** using "genlock" generically for any sync system, which hides that PTP failure modes (grandmaster loss, network jitter affecting clock delivery) are different from genlock failure modes (a bad BNC cable) and need different troubleshooting.

### N+1 vs. 2N redundancy
**N+1** means one spare unit or path covers any single failure among N active ones — cost-efficient, but two simultaneous failures exceed it. **2N** means every active path has its own fully duplicated twin — survives simultaneous failures on different paths, at roughly double the cost.
**In use:** "The router core is N+1 — fine for a single card failure, but if we want to survive a full frame outage we need 2N, and that's a different budget conversation."
**Common misuse:** calling any spare equipment "redundant" without specifying which posture — N+1 protects against one class of failure, not all classes, and station leadership often assumes the stronger guarantee.

### LKFS vs. LUFS
**LKFS** (Loudness, K-weighted, relative to Full Scale) is the unit used in the U.S. broadcast standard (ATSC A/85). **LUFS** (Loudness Units relative to Full Scale) is the equivalent unit in the international EBU R128 standard. The measurement algorithm (ITU-R BS.1770) is shared between them; the units are numerically interchangeable but tied to different regional standards and target levels.
**In use:** "Our target is −24 LKFS per ATSC A/85 — if this creative was mastered to EBU R128's −23 LUFS target for a European client, that's within our ±2 dB tolerance, but check it, don't assume."
**Common misuse:** treating "loudness compliant" as a single universal number instead of checking which standard (and which target) the specific content was mastered against.

### Drop-frame vs. non-drop-frame timecode
**Non-drop-frame** timecode counts every frame sequentially assuming an exact 30 fps; **drop-frame** timecode periodically skips frame *numbers* (not actual frames) to keep the displayed timecode matching real elapsed clock time, because NTSC video actually runs at 29.97 fps, not exactly 30. Uncorrected, non-drop timecode drifts from real time at a fixed rate: roughly 108 frames (3.6 seconds) per hour.
**In use:** "We're joining the network feed for two avails over three hours — that's 324 frames of drift if this truck is running non-drop. Re-genlock to their drop-frame reference before rehearsal."
**Common misuse:** assuming timecode drift is a post-production editorial concern; in live broadcast with frame-accurate network joins, it's a live-show compliance risk with contractual make-good consequences.

### SCTE-35 cue vs. ad avail
An **ad avail** is the contractual window of time reserved for an advertisement or local insertion. **SCTE-35** is the technical cue-tone standard that signals the exact frame at which the avail starts and ends within the video stream, so downstream systems (ad insertion, network affiliates) can splice cleanly.
**In use:** "The avail is 2 minutes; the SCTE-35 cue tells the splicer the exact frame to cut on — if our clock's off, the avail duration is right but the splice point is wrong."
**Common misuse:** treating avail duration and cue-tone accuracy as the same problem — a station can nail the 2-minute length and still miss the network's required return frame if the cue timing itself is off.

### RMT vs. RWT (EAS)
**RWT** (Required Weekly Test) is a routine, low-stakes EAS test transmitted weekly with no public alerting content, testing the local encoder/decoder path only. **RMT** (Required Monthly Test) simulates a fuller alert chain including audio/visual alert tones, during a state-EAS-plan-specified time window, and must be scheduled around live programming.
**In use:** "The RWT can run anytime overnight, but the RMT window this month overlaps our marquee Friday broadcast — move it to Sunday afternoon."
**Common misuse:** scheduling both tests the same way, without recognizing that an RMT's fuller simulated-alert content is the one that risks colliding visibly with live programming.

### Master control vs. the truck (remote production)
**Master control** is the fixed facility (often at the station or network hub) that owns final signal integrity, playout, and compliance logging before the signal leaves the building. **The truck** is the mobile production unit at the event venue where the live switching, camera ISOs, and replay actually happen; its output feeds master control, it doesn't replace it.
**In use:** "The glitch was on the truck-to-facility path, not inside master control — check the IP link first, not the playout server."
**Common misuse:** using "control room" generically for both, which obscures who owns which failure — a truck engineer can't fix a master-control playout defect and vice versa.

### Blast radius vs. likelihood (in redundancy planning)
**Blast radius** is how much of the operation a given failure takes down if it occurs (one show vs. the whole facility vs. every affiliate downstream). **Likelihood** is how often it's expected to occur. A low-likelihood, large-blast-radius failure (shared fiber entrance) often deserves more budget than a frequent, small-blast-radius one.
**In use:** "That router card fails maybe twice a year and only affects one path — low blast radius. The shared conduit run is rare but takes out both primary and backup simultaneously — fix that first."
**Common misuse:** prioritizing fixes by how recently or how often something failed, ignoring blast radius, which is how the actual catastrophic single point of failure stays unaddressed for years.

### Failover trigger vs. failover acquisition time
The **trigger** is the condition (packet loss threshold, loss of lock) that initiates a failover. **Acquisition time** is how long the backup path takes to actually lock in and become clean once triggered. A correctly firing trigger with a slow acquisition time still produces a visible on-air glitch.
**In use:** "The trigger fired exactly on spec, but acquisition took 200ms — four frames visible on air. We need to fix acquisition time, not the trigger threshold."
**Common misuse:** treating "the failover worked" as binary (fired or didn't) instead of measuring whether it was fast enough to be invisible.

### Line-up vs. dress rehearsal
A **line-up** (technical rehearsal) exercises the signal chain, clocks, redundancy, and compliance systems — a technical pass, typically without full editorial content. A **dress rehearsal** runs the actual show content end-to-end for timing and creative flow. Skipping the line-up in favor of only a dress rehearsal misses exactly the technical failure modes (clock drift, failover timing) that dress rehearsals aren't designed to surface.
**In use:** "We ran a full dress rehearsal but no line-up — nobody actually pulled the primary router path to confirm the protect path works."
**Common misuse:** assuming a clean dress rehearsal implies the technical infrastructure is sound; dress rehearsals test editorial timing, not failover behavior.
