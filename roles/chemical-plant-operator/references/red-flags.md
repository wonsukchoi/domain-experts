# Red flags

### In-process mass balance doesn't reconcile within expected tolerance, even though individual readings look normal
- **Usually means:** a leak, instrumentation fault, or unaccounted side reaction.
- **First question:** what specifically explains the gap — normal process loss (e.g. evaporation), or something unaccounted for?
- **Data to pull:** cumulative feed/output totals compared against actual measured inventory and expected process loss.

### Batch reaction temperature trends upward above setpoint, and the response is to wait and observe rather than act immediately
- **Usually means:** risk of exotherm acceleration outpacing available cooling capacity.
- **First question:** what's the actual temperature trend rate versus the cooling capacity margin at current conditions?
- **Data to pull:** temperature trend rate compared against cooling capacity margin.

### Multiple alarms trigger simultaneously and are responded to in order of occurrence rather than by consequence severity
- **Usually means:** a higher-consequence but less-frequent alarm gets deprioritized behind a lower-consequence, more-familiar one.
- **First question:** what's each alarm's actual priority classification versus the order they were actually responded to?
- **Data to pull:** alarm priority classification compared against actual response order and timing.

### Reactant addition sequence or rate deviates from the specified procedure
- **Usually means:** risk of an unintended reaction pathway distinct from the intended process, even if the same total materials eventually combine.
- **First question:** what was the actual addition sequence and rate versus the specified procedure?
- **Data to pull:** actual addition sequence/rate compared against the specified procedure.

### Several process variables are each individually within normal limits but simultaneously near their respective limits
- **Usually means:** a combined operating condition that's unsafe even though no single-variable check would flag it.
- **First question:** what are the current values of all key variables together, not just each checked separately?
- **Data to pull:** current values of all key variables compared against their individual limits, evaluated jointly.

### A process deviation or near-miss is resolved and logged without documenting the mass balance reconciliation or corrective action
- **Usually means:** the next shift or operator lacks the information needed to recognize a recurring or developing issue.
- **First question:** does the shift log actually match the DCS/alarm event history for that period?
- **Data to pull:** shift log entries compared against the actual DCS/alarm event history for the same period.

### A specific alarm is repeatedly acknowledged or silenced without investigation because "it always does that"
- **Usually means:** alarm fatigue masking a genuine, potentially worsening condition behind a habitually dismissed signal.
- **First question:** has the root cause of this recurring alarm ever actually been investigated?
- **Data to pull:** alarm acknowledgment log and frequency compared against whether root cause was ever investigated.
