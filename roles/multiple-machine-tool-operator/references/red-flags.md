# Red flags

### A machine sitting idle/stopped while the operator follows a fixed visiting rotation to a different machine
- **Usually means:** rotation order is being followed mechanically instead of triaging by actual consequence of delay.
- **First question:** how long has the idle machine been stopped, and does it need attention sooner than the machine currently being visited?
- **Data to pull:** time since each machine's last check/visit, current status (running vs. stopped) of each machine.

### An in-process tolerance check performed later than its specified interval
- **Usually means:** the visiting sequence didn't account for that specific machine's risk-based check requirement.
- **First question:** was this machine's check interval based on its actual tolerance/wear risk, or lumped into a generic rotation?
- **Data to pull:** the machine's specified check interval, actual time elapsed since the last check.

### A setup or changeover started without checking the status/slack of other machines being tended simultaneously
- **Usually means:** the setup was scheduled for convenience rather than for a window when the other machines could tolerate the attention gap.
- **First question:** what is the remaining safe unattended time for each other machine at the moment the setup begins?
- **Data to pull:** cycle status and risk profile for every other machine in the tending group at setup start time.

### A new machine added to a tending assignment without recalculating the visiting sequence
- **Usually means:** the previous sequence, optimized for a different workload, is still being used even though it no longer matches actual demand.
- **First question:** has the visiting sequence been recalculated since this machine was added, or is the operator still running the prior pattern?
- **Data to pull:** current machine count and cycle times in the group, the sequence/logic actually being used.

### Multiple machines alarming or signaling simultaneously with no clear priority given to the response
- **Usually means:** the operator is responding in the order alarms arrived or by proximity rather than by consequence of delay.
- **First question:** does one of the simultaneous signals represent a stopped/idle condition (pure output loss) versus a running condition with remaining slack?
- **Data to pull:** the nature of each simultaneous signal (stopped vs. running-but-flagged), estimated consequence of delay for each.

### A part discovered out of tolerance after a machine ran unattended longer than its normal interval
- **Usually means:** the visiting interval for that machine was either too long for its actual risk, or was extended due to attention being consumed elsewhere.
- **First question:** how long was this machine actually unattended compared to its intended check interval?
- **Data to pull:** time since last check, parts produced during that gap, out-of-tolerance extent found.

### A machine's cycle time observed to have changed without the visiting sequence being updated
- **Usually means:** a tooling, material, or program change shifted the machine's actual pace, but the tending plan still assumes the old cycle time.
- **First question:** does the current visiting sequence reflect this machine's actual current cycle time, or an outdated one?
- **Data to pull:** current observed cycle time vs. the cycle time the visiting plan was based on.

### An operator falling behind schedule continuing the original planned visiting order rather than re-triaging
- **Usually means:** the operator is following the plan mechanically rather than reassessing which machines now carry the most risk given the delay.
- **First question:** given the current delay, which machines now have the least remaining slack, regardless of the original plan's order?
- **Data to pull:** current status and remaining slack for every machine in the group at the point the delay was recognized.

### A machine consistently requiring emergency attention (jams, stoppages) more often than others in the same tending group
- **Usually means:** a machine-specific issue (tooling, material feed, mechanical wear) rather than a general tending-pattern problem.
- **First question:** does this specific machine's stoppage frequency exceed the others', or is the whole group experiencing similar issues?
- **Data to pull:** stoppage/intervention frequency by machine over recent shifts.

### A shift handoff describing the tending group generically ("all machines running fine") without per-machine status
- **Usually means:** the incoming operator isn't getting the specific cycle/risk information needed to build an effective visiting sequence from the start.
- **First question:** does the handoff include each machine's current cycle status, check interval, and any known risk factors?
- **Data to pull:** the handoff record, per-machine status at end of the outgoing shift.
