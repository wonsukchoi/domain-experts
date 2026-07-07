# Crane and Tower Operator — Red Flags

### Sustained wind reading compared against the chart's gust-based rating and called "under limit"
- **Usually means:** the crew is reading a sustained average against a number the OEM chart defines as a 3-second gust at the jib head, understating the actual load on the structure
- **First question:** is this crane's chart rating stated as a gust or a sustained figure, and what does the jib-head anemometer's gust peak actually read?
- **Data to pull:** OEM chart wind-rating definition, jib-head anemometer gust log for the last 10–15 minutes

### Load's sail-area-to-weight ratio is materially above the chart's reference ratio, chart's flat wind number applied anyway
- **Usually means:** the derate calculation for this specific load's wind exposure was never run, and the load may already be over its actual limit well before the chart's flat number is reached
- **First question:** what's this load's actual sail-area-to-weight ratio, and what's the derated gust limit once that's compared to the chart's reference ratio?
- **Data to pull:** load dimensions and weight, chart's stated reference ratio, derate calculation

### Wind reading trending upward across a multi-minute pick, still technically under the derated limit
- **Usually means:** a rising trend that will cross the threshold before the pick reaches its blind or highest-risk segment, if the trend continues at its current rate
- **First question:** what's the rate of increase over the last 10–15 minutes, and will the load still be airborne when the trend crosses the derated number?
- **Data to pull:** wind log with timestamps, estimated remaining time to complete the pick

### Blind-lift segment beginning on a single "you're clear" call issued once at the start
- **Usually means:** the crew is treating one confirmation as covering every subsequent motion in the blind segment instead of a call-and-repeat per motion
- **First question:** has each distinct motion (raise, slew, trolley, lower) in this blind segment been separately called and repeated back?
- **Data to pull:** radio log/transcript for the segment, signal-person assignment and sightline confirmation

### Radio contact lost mid-blind-segment, motion continuing because it was "already started"
- **Usually means:** the crew is treating an earlier confirmed call as still valid for conditions that may have changed since contact was lost
- **First question:** has all motion been held since contact dropped, and has contact been confirmed restored before resuming?
- **Data to pull:** radio contact log, timestamp of last confirmed call versus timestamp of loss

### Signal person's sightline to the pick or set point obstructed, lift proceeding on a best-guess continuation
- **Usually means:** the signal person is calling motion without the sightline the protocol assumes they have
- **First question:** does the signal person currently have a clear, confirmed sightline to the zone they're calling, or has it been lost to obstruction, distance, or light?
- **Data to pull:** signal-person position and sightline confirmation, obstruction/lighting conditions at the zone

### Two-crane lift proceeding without a documented load-share calculation
- **Usually means:** the load is being split by eye ("roughly half") instead of from the engineered center-of-gravity position
- **First question:** what's the calculated share for each crane based on CG position relative to both pick points, and has each been checked against its own derated ceiling?
- **Data to pull:** rigging plan CG location, load-share calculation, each crane's chart capacity at its working radius

### Either crane's calculated load share exceeds its derated ceiling (commonly 75% of chart capacity)
- **Usually means:** the current pick-point geometry doesn't leave enough margin for CG-estimate uncertainty on at least one crane
- **First question:** can pick points be repositioned to shift the load share, or does this pick need a higher-capacity crane in that position?
- **Data to pull:** load-share calculation, both cranes' chart capacity at their respective radii, CG-estimate confidence noted in the rigging plan

### Required lift radius exceeds what the installed jib length/counterweight configuration supports on the chart
- **Usually means:** the crew is treating the installed configuration as adjustable ("walk it out a bit more") when it's fixed for the length of the installation
- **First question:** has this been escalated to the crane engineer or erector for a documented reconfiguration, or is there a substitute lift method for this specific pick?
- **Data to pull:** chart page for the actual installed configuration, required radius, engineering response on reconfiguration feasibility

### Counterweight configuration being read off the erection drawing rather than confirmed as physically installed
- **Usually means:** a mismatch between planned and as-built counterweight (missing block, wrong block count) is being carried forward into the chart read
- **First question:** has the physical counterweight block count been confirmed against the chart page being used?
- **Data to pull:** erection drawing, physical counterweight inspection record, chart page in use

### Free-slew (weathervane) mode not confirmed set ahead of an approaching wind event or shift-end
- **Usually means:** the jib is left locked against rotation into an approaching high-wind event instead of released to weathervane, loading the structure as a fixed obstruction
- **First question:** has free-slew been engaged and confirmed per the OEM out-of-service procedure before the crew leaves the crane unattended?
- **Data to pull:** out-of-service checklist, forecast wind event timing, free-slew confirmation log
