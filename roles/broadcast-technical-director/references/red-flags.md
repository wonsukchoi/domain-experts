# Red flags

Smell tests a facility engineer or technical director should catch before signing off on a show or a build-out, not after.

### "We have redundancy" with no named exclusion for the backup path
**Usually means:** the backup shares a fiber entrance, a power feed, a building conduit run, or a vendor firmware version with the primary — the diagram shows two paths, reality has one point of failure feeding both.
**First question:** "What does the backup path *not* protect against?"
**Data to pull:** facility riser diagrams for physical routing of both paths; power one-line diagram; firmware/software version match between primary and backup hardware.

### Router protect-path or grandmaster failover has never been triggered live during a rehearsal
**Usually means:** the failover was designed and configured but only ever verified on paper or in a lab, not exercised by the actual crew under actual show conditions — acquisition time under load is unmeasured.
**First question:** "When did we last pull the primary live, with the crew calling it, and time the failover?"
**Data to pull:** rehearsal logs; failover acquisition-time measurements; date of last live exercise per path.

### Loudness normalizer reads clean but the content source changed recently
**Usually means:** a re-cut promo, a new ad-insertion vendor, or a codec change was inserted downstream of the normalization stage, or the normalizer's calibration predates the change.
**First question:** "When was this specific insert last spot-checked against ATSC A/85, and where does it enter the chain relative to the normalizer?"
**Data to pull:** LKFS measurement on the specific file/insert (not the channel average); signal-chain diagram showing normalizer position; date of last codec or vendor change.

### Internal facility clock is free-running instead of genlocked/PTP-synced to the network reference
**Usually means:** a truck or facility that hasn't been checked against the network house clock recently; drift compounds silently and surfaces as a missed ad-avail join, not as an alarm.
**First question:** "What's our offset against network house clock right now, and when did we last check?"
**Data to pull:** current PTP offset or genlock phase reading; drop-frame vs. non-drop-frame mode setting; ad-avail contract tolerance (frames).

### EAS Required Monthly Test scheduled without checking the live-event calendar
**Usually means:** whoever scheduled the compliance test didn't cross-reference programming; a test firing during a high-profile live broadcast risks viewer confusion and a PR problem distinct from the compliance issue itself.
**First question:** "Does this month's RMT window overlap any scheduled live sports or breaking-news programming?"
**Data to pull:** state EAS plan required test window; live programming calendar; last RMT/RWT log entries per §11.61/§11.55.

### A shift handoff log with no open-defect carryover section filled in
**Usually means:** either the shift genuinely had zero anomalies (rare on a busy facility) or minor events (a transient packet-loss blip, a vendor ticket) were dismissed as "nothing" rather than logged for pattern detection across shifts.
**First question:** "Walk me through every alarm or anomaly from the last 8 hours, however minor."
**Data to pull:** system alarm logs for the shift; open vendor tickets; comparison against the prior 3 shift-handoff logs for a repeating pattern.

### Post-incident report says "human error" or "equipment failure" with no procedural or configuration change named
**Usually means:** the report stopped at the proximate cause instead of the actual gap (an untested acquisition time, a rehearsal script that didn't cover the failure mode, a threshold set from vendor defaults instead of measured facility performance).
**First question:** "What specific procedure or configuration changes as a result of this, and who owns it by when?"
**Data to pull:** the rehearsal checklist used before the incident; whether the failed scenario was in scope of that checklist; the actual remediation ticket, not just the report narrative.

### Facility engineering budget requests every path duplicated after one bad incident
**Usually means:** an overcorrection — blanket 2N redundancy proposed regardless of each path's actual blast radius and time-to-detect, which burns budget on low-risk paths while potentially leaving the actual shared point of failure (power, fiber entrance) unaddressed.
**First question:** "Which specific failure mode does each proposed duplication address, and what's its blast radius if it's not fixed?"
**Data to pull:** the exposure ranking from the last technical risk review; cost per path vs. likelihood/impact; whether the actual root cause of the recent incident is even addressed by the proposed spend.

### Ad-avail join consistently late by a small, consistent number of frames
**Usually means:** a clock/timecode reference mismatch (non-drop vs. drop-frame, or an unlocked local clock) rather than a one-off operator error — a consistent offset is a systemic drift, not a mistake.
**First question:** "Is the offset growing over the course of the show, or constant?"
**Data to pull:** timecode mode and reference source for the affected path; offset measurements at multiple points during the broadcast; history of make-good charges from the network.

### Closed-caption stream verified on primary path only
**Usually means:** the caption encoder pass-through was never confirmed on the protect path, so a failover event — otherwise clean — produces an FCC captioning compliance gap the moment it's needed.
**First question:** "When did we last confirm captions pass through the protect path specifically, not just the primary?"
**Data to pull:** caption verification logs per path; date of last protect-path failover test; FCC captioning complaint history if any.
