# Railroad Conductor and Yardmaster — Red Flags

### Blue flag or blue signal displayed with no matching work order or crew accounted for
- **Usually means:** protection left up after the work was actually completed (removal forgotten), less commonly an unauthorized or miscommunicated placement
- **First question:** who placed this protection, and are they still on the job or car it's protecting?
- **Data to pull:** blue-signal placement log, job briefing record for that work location, crew roster and current task assignment

### Operative power-brake percentage measured below roughly 85% on the initial terminal test
- **Usually means:** several cars sharing a common defect (contaminated air supply, a cut-out valve left in the wrong position), less commonly unrelated defects coinciding by chance
- **First question:** which specific cars are cut out, and is there a common cause across them?
- **Data to pull:** initial terminal brake test record, individual car defect codes, air source pressure log

### Radio communication lost for more than a few seconds during a shoving movement
- **Usually means:** a dead zone or handset/battery failure, less commonly a crew member incapacitated or out of position
- **First question:** has the movement already been stopped?
- **Data to pull:** radio log timestamps, point person's last transmission and car count called, any movement/event recorder if the equipment carries one

### Consist car count or car order doesn't match what's physically coupled
- **Usually means:** a late add or pull wasn't reflected in the consist system, less commonly a switching error moved a car to the wrong position
- **First question:** when was the consist last updated relative to the last completed switch move?
- **Data to pull:** consist timestamp vs. switch-list completion time, yard tracking system's car-order scan, most recent switch move log

### Placarded hazmat car positioned adjacent to the locomotive or to another incompatible placarded car without a buffer car
- **Usually means:** a rebuild or re-switch after the original hazmat placement plan skipped the buffer-car check, common during a rushed re-block
- **First question:** was this block rebuilt or re-switched after the original hazmat placement was set?
- **Data to pull:** consist hazmat position field, buffer-car assignment, 174.85 checklist status for this train

### Classification track nearing full while the switch list still shows unassigned inbound cars for that block
- **Usually means:** the nominal car-length assumption didn't match this block's actual car mix (long tank cars, double-stacks), less commonly a miscount of what's already on the track
- **First question:** what's the actual measured car-length total for this block versus available track footage?
- **Data to pull:** track footage rating, car-length manifest for the block, current occupied footage on the track

### Same block pulled and reclassified more than once in a shift
- **Usually means:** the original block plan didn't follow reverse-set-out-order logic, less commonly a late priority car forced a legitimate rebuild
- **First question:** what changed between the original switch list and the current one?
- **Data to pull:** switch-list revision history, priority/hot-car flags, track assignment log

### Crew reports a shove went further than the called car count
- **Usually means:** a miscounted car length or a missed hand signal, less commonly an unnoticed loss of sightline that wasn't reported as a communication loss
- **First question:** did the point person maintain continuous sightline or radio contact for the entire move?
- **Data to pull:** job briefing notes on the point-protection method used, radio log, car count called versus distance actually moved

### Job briefing not renewed after the switch list or plan changed mid-shift
- **Usually means:** the crew treated a radioed correction as sufficient under time pressure instead of a full re-briefing
- **First question:** what specifically changed since the last briefing, and did every crew member hear it directly?
- **Data to pull:** job briefing log timestamp versus plan revision timestamp, radio log of the change notification

### Train tonnage or car count on the consist doesn't reconcile with the sum of the yard's per-block figures
- **Usually means:** a car was added or pulled after the consist was generated, less commonly a weight field was estimated rather than pulled from actual car data
- **First question:** which block's car count or tonnage changed most recently relative to the consist's generation time?
- **Data to pull:** per-block car list and weight, consist generation timestamp, timestamp of the last switch move affecting that block
