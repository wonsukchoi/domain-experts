# Vocabulary

### VSWR (Voltage Standing Wave Ratio)
A ratio describing how much RF power is reflected back from an antenna/transmission-line mismatch rather than radiated, derived from the reflection coefficient Γ = √(reflected power / forward power).
**In use:** "Main's sitting at 1.5:1, forward power's steady — that's the line, not the PA."
**Common misuse:** Treating any nonzero VSWR as a fault. A well-matched system always has some small reflection (1.05–1.2:1 is normal); the number that matters is the *change* from baseline, not whether it's exactly 1:1.

### Dialnorm
The metadata field (dialogue normalization value) embedded in a compressed audio stream telling a decoder how much to attenuate that content so perceived loudness matches a reference level.
**In use:** "The tag still says −24, but the actual measured loudness is −18 — that's a dialnorm mismatch, not a mic problem."
**Common misuse:** Assuming the dialnorm tag describes the actual audio. It's a label written at encode time; anything downstream that re-processes the audio without re-tagging makes the label wrong.

### LKFS / LUFS
Loudness units relative to full scale — the integrated loudness measurement standard (ATSC A/85 in broadcast, EBU R128 in Europe) that correlates with perceived loudness far better than a peak or VU reading.
**In use:** "Program measured −23.6 LKFS, well inside the −24 ±2 target; the spot's the outlier at −18.2."
**Common misuse:** Reading a peak or VU meter and calling it "loudness." Peak level says nothing about integrated perceived loudness — two clips can peak identically and differ by 6+ LU in how loud they sound.

### EAS (Emergency Alert System) — RWT / RMT
The federally mandated alert relay system; RWT (Required Weekly Test) and RMT (Required Monthly Test) are the two routine compliance tests every station must log.
**In use:** "We missed Tuesday's RWT — decoder heartbeat dropped for 24 minutes — that goes in the log and gets reported today, not folded into the repair ticket."
**Common misuse:** Treating a missed test as purely a maintenance issue. The moment the window closes, it's a filed compliance event regardless of whether the equipment gets fixed the same day.

### As-run log
The automation system's authoritative record of what actually aired, at what time, versus what was scheduled — the legal record for advertisers, ratings, and regulatory audits.
**In use:** "Pull the as-run log for the 6 p.m. break — I want the exact air time and duration of spot 44821, not the traffic schedule."
**Common misuse:** Confusing the *schedule* (what was supposed to air) with the *as-run log* (what actually aired). They routinely diverge — makegoods, preemptions, and automation errors all show up only in the as-run record.

### STL (Studio-Transmitter Link)
The dedicated path (microwave, fiber, or IP) carrying program signal from the studio to the transmitter site, separate from the over-the-air signal the transmitter then radiates.
**In use:** "We lost the primary STL in the storm — switched to the IP-fiber backup, about 90 seconds of manual failover."
**Common misuse:** Confusing an STL outage with a transmitter outage. The transmitter can be fully healthy and the station still goes dark because nothing is reaching it to transmit.

### Foldback
A transmitter's automatic protective response that reduces output power (or shuts down) when it detects a fault condition like excessive VSWR or overcurrent, to protect the final amplifier stage.
**In use:** "If we let VSWR keep climbing past 2:1, the PA will fold back on its own — better to switch to aux before it does that mid-newscast."
**Common misuse:** Treating foldback as a failure to prevent at all costs. It's a protection mechanism working as designed; the actual failure is whatever condition triggered it, and preventing foldback by disabling the protection is worse than letting it fire.

### Dead air
Broadcast industry term for an unintended gap with no program audio (and often no video) reaching the audience — an audience-facing outage, distinct from an equipment alarm that hasn't yet affected the on-air signal.
**In use:** "That's dead air on the OTA signal specifically — cable's fine, so it's downstream of master control, not a source problem."
**Common misuse:** Using "dead air" for any audio dip or a brief processing glitch. It specifically means the audience heard/saw nothing — a momentary level drop that never went silent isn't dead air.

### Remote control system (FCC Part 73.1350 context)
The monitoring/control hardware and software (e.g., Burk, Davicom) that lets an operator read transmitter telemetry and adjust setpoints from off-site, and that produces the logs required for FCC recordkeeping.
**In use:** "Remote control's showing plate current in range, so the fault's not the final amplifier — check the antenna side."
**Common misuse:** Treating the remote-control display as equivalent to a direct inspection of the signal. It reports only the specific points it's configured to sample, at whatever polling interval is set — it can miss anything outside its own instrumented scope.

### CALM Act / ATSC A/85
The Commercial Advertisement Loudness Mitigation Act (2010) is the U.S. law requiring commercials not be louder than the surrounding program; ATSC A/85 is the technical practice (the −24 LKFS ±2 LU target and related measurement method) stations use to comply with it.
**In use:** "That spot's a CALM Act problem the moment it airs again — 5.4 LU over program average, pull it."
**Common misuse:** Treating CALM Act compliance as "the file passed a loudness check once at ingest." Compliance is about what actually airs; a downstream re-processing step that isn't re-checked can silently break compliance after the file already passed.

### Master control
The centralized point (often now a shared facility for multiple stations) where program sources are switched, automated, and sent to transmission — distinct from a production control room, which handles live show switching for a single program.
**In use:** "That's a master-control automation issue, not a production-truck issue — check the playlist, not the switcher."
**Common misuse:** Conflating master control with the technical-direction role that calls a live production switcher. Master control runs the ongoing channel; a technical director runs a specific live production.

### Loudness anchor element
In ATSC A/85 methodology, the specific portion of program content (typically dialogue) used as the reference point for measuring and setting the program's overall loudness level.
**In use:** "We're measuring against the anchor element, not the whole mix, so a loud music bed under quiet dialogue won't itself trip the target."
**Common misuse:** Assuming integrated loudness measurement treats every part of the audio equally. The anchor-element method specifically weights dialogue-present sections, which is why two clips with identical overall energy can have different compliant targets.
