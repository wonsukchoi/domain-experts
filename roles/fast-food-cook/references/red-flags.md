# Red flags

Smell tests a fast food cook (or the shift lead reading over their shoulder) should catch fast, with the first question to ask and the data to pull before deciding anything.

### A fry basket held past its ~7-minute quality-hold timer without being discarded

- **Usually means:** a shift lead overrode the timer under queue pressure, or the sticker/timer wasn't started at the actual pull-from-oil moment.
- **First question:** "What time did this basket come out of the oil, and what does the timer actually show right now?"
- **Data to pull:** the timer-start timestamp versus current time, and whether a discard-exception was logged for it.

### Fryer oil TPM reading at or above ~24% with a rush still ahead

- **Usually means:** the scheduled oil change was pushed past its window to avoid a mid-rush fryer downtime, or the meter wasn't checked at shift start.
- **First question:** "When was oil last tested, and what's today's forecasted volume against one fryer being down for a change?"
- **Data to pull:** the TPM log for the fryer and the shift's volume forecast.

### The same sandwich comes back to the window twice in one rush for a build error

- **Usually means:** a build card step got skipped or reordered under speed pressure, most often the condiment sequence.
- **First question:** "Was that build made off the picture card, or from memory?"
- **Data to pull:** the specific build card for that item and which crew member assembled it.

### Drive-thru average total time climbing past target with car count unchanged

- **Usually means:** a single station (usually fry or bun-toast) has become the bottleneck and isn't staffed for the current queue depth, not that every station has slowed down evenly.
- **First question:** "Which station is the line actually waiting on right now?"
- **Data to pull:** per-station cycle times for the last 15 minutes and current queue depth from the lane camera or POS.

### A crew member freelancing an ingredient order or portion "because it tastes better"

- **Usually means:** a tenured crew member has started reading personal judgment back into a scripted station, often after praise from a regular customer.
- **First question:** "What does the build card say for this item, step by step?"
- **Data to pull:** the printed build card and a photo of the last three sandwiches that crew member assembled.

### An expired batch served after a manager or shift lead directive to "just bag it"

- **Usually means:** speed-of-service pressure is being prioritized over hold-timer compliance in the moment, usually without a logged exception.
- **First question:** "Is there a logged exception for this, and what's the documented reason?"
- **Data to pull:** the shift log's exception entries and the timer reading at the moment of the override.

### A new hire timing every step off memory instead of the picture build card

- **Usually means:** training skipped the card-first method and relied on verbal instruction, which drifts from spec faster under a first-week hire.
- **First question:** "Where's the build card for this station — has it been in front of you today?"
- **Data to pull:** that hire's build-error or remake rate over their first two weeks versus store average.

### Portion scoop or squeeze-pattern tool missing or visibly worn at a station

- **Usually means:** a tool went missing mid-shift and crew is eyeballing portions instead of flagging it for replacement.
- **First question:** "What's being used to portion this right now if the scoop isn't at the station?"
- **Data to pull:** the station's tool checklist from opening and any portion-variance complaints logged that shift.

### The shift log shows zero timer or build exceptions across a full rush

- **Usually means:** either a genuinely clean shift, or exceptions are happening and not being logged — worth checking against waste totals.
- **First question:** "Does the waste count for fries and patties match what a zero-exception shift should produce?"
- **Data to pull:** waste/discard totals from the POS or waste log cross-checked against the shift log's exception entries.

### A discarded-item waste count that doesn't match the number of logged timer exceptions

- **Usually means:** discards are happening without being logged, which breaks the store's ability to explain a waste spike during a franchise audit.
- **First question:** "What's driving today's waste count that isn't already in the shift log?"
- **Data to pull:** POS waste/void entries itemized by product against the shift log's exception list for the same window.
