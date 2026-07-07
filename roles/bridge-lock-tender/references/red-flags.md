# Red flags

Smell tests a veteran tender catches before a sequence starts, or before a logged decision gets defended after the fact.

### Gate-down interlock lamp unlit but the tender proceeds on a visual check

- **Usually means:** the down-limit switch hasn't tripped — a misaligned gate arm, a stuck actuator, or a switch fault — and the gate is not actually confirmed seated even if it looks down from the console.
- **First question:** "Has the confirmation lamp actually lit, or are we going by what the camera/window shows?"
- **Data to pull:** limit-switch maintenance log for this gate arm, time since last cycle test, camera timestamp vs. lamp-confirmation timestamp for this event.

### Sound-signal request (one prolonged, one short blast) with no acknowledgment sent within the expected window

- **Usually means:** the tender is off-station, monitoring a different channel, or the horn/radio system has a fault — not that the vessel signal was somehow invalid.
- **First question:** "When did we send the acknowledgment signal, and on what channel was the request received?"
- **Data to pull:** VHF Channel 13 log, sound-signal system status log, time between request and acknowledgment for this event and the trailing 30 days.

### Lock valve opened to full within the first 60 seconds on a chamber lift over 10 ft

- **Usually means:** the operator skipped the staged-opening schedule to speed the lockage, trading surge risk for a few minutes saved.
- **First question:** "What's the staged valve-opening schedule for this chamber's lift, and which stage were we actually at 60 seconds in?"
- **Data to pull:** valve-position log against the certified staging schedule, any hawser-tension or mooring-line incident reports from this chamber in the trailing year.

### Restricted-hours schedule cited to refuse an opening with no exception check logged

- **Usually means:** the tender is treating the posted schedule as absolute rather than checking the specific exception list (advance notice, public vessel, emergency) the same regulation carries.
- **First question:** "Did the requesting vessel meet any exception on this structure's schedule section, and is that check in the log?"
- **Data to pull:** the structure's specific 33 CFR 117.xxx section text, the vessel's notice timestamp if any, the log entry for the refusal.

### Chamber near gates closed while a vessel's stern is still outside the fender-line marker

- **Usually means:** the tender is running ahead of the vessel's actual position, often under time pressure to keep the lockage schedule.
- **First question:** "Where was the vessel's stern relative to the fender line at gate-close command?"
- **Data to pull:** chamber-approach camera timestamp vs. gate-close command timestamp, vessel pilot's position report if radioed.

### Span-lower command issued before the span-up/span-seated limit switch sequence completes

- **Usually means:** the operator is running the reverse sequence on the same "looks done" assumption as the up-cycle — the seated switch, not a visual, is what confirms the span is safe to release traffic gates onto.
- **First question:** "Did the seated-limit switch confirm before gate release, or did we release on visual?"
- **Data to pull:** span-position limit-switch log, gate-release command timestamp, any prior near-miss reports for this structure's down-cycle.

### Same-class vessels getting repeated separate full openings within one interlock-cycle window

- **Usually means:** requests weren't consolidated into a single opening, multiplying vehicle-traffic disruption for no safety benefit — often a coordination gap rather than a deliberate choice.
- **First question:** "Could these requests have been served in one opening cycle instead of two or three?"
- **Data to pull:** VHF request timestamps for the window, number of separate open/close cycles logged versus vessels served.

### Log entries for delayed or refused openings missing a reason code

- **Usually means:** the tender delayed or refused a request without documenting the regulatory basis — the single detail that determines whether a later complaint is a non-event or a citation.
- **First question:** "What's the reason code on this delay, and does it map to an actual exception or restriction in the structure's schedule section?"
- **Data to pull:** the operating log for the event in question, the structure's schedule section, any district-office correspondence about the same structure.

### Danger signal (five or more short blasts) sent but the approaching vessel doesn't respond

- **Usually means:** the vessel didn't receive or didn't recognize the signal — possible steering, engine, or communication trouble on board, which changes this from a scheduling problem into a developing safety event.
- **First question:** "Have we raised the vessel on VHF Channel 13 directly, and do we have a visual on its heading and speed right now?"
- **Data to pull:** VHF call log, vessel's last known speed/heading, whether the district office or Coast Guard sector has been notified.

### Traffic-gate warning cycle shortened below its certified minimum to reduce vehicle wait

- **Usually means:** local pressure (complaints, a backed-up commute) led someone to trim the warning-light/bell cycle timer — this is a deliberate reduction of the only warning a driver or pedestrian gets before the span moves.
- **First question:** "Who authorized a change to the warning-cycle timer, and does it match the structure's certified interlock timing?"
- **Data to pull:** interlock timer configuration and change log, the structure's certified timing documentation, any near-miss or incident reports since the change.
