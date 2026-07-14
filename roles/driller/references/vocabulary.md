# Driller vocabulary

### Kick
An influx of formation fluid (gas, oil, or water) into the wellbore because formation pressure exceeded the mud's hydrostatic pressure at that depth.
**In use:** "We took an 8-barrel kick on the break at 9,800 — shut in on the annular."
**Common misuse:** Used loosely for any pit gain or gas showing, including ones later explained by an operational cause; a kick specifically means a confirmed influx, established by a positive flow check, not any anomaly on the pits.

### Drilling break
A sudden increase in rate of penetration with no corresponding increase in WOB or RPM.
**In use:** "Got a break at the last connection, 45 to 140 — flow-checking before we go further."
**Common misuse:** Treated as automatically good news ("we're drilling faster") rather than a diagnostic trigger; the break itself doesn't tell you which cause it is until the flow check does.

### SIDPP / SICP (Shut-In Drill Pipe Pressure / Shut-In Casing Pressure)
The stabilized pressures read at surface on the drill pipe and casing/annulus immediately after shutting in on a kick, used to calculate formation pressure and kill mud weight.
**In use:** "SIDPP came in at 350, SICP at 420 — running the kill sheet now."
**Common misuse:** Read too early, before pressures fully stabilize, which understates formation pressure and produces an undersized kill mud weight.

### Trip margin
Extra mud weight (or an equivalent pipe-speed limit) carried above static balance before pulling out of hole, to offset the swab pressure reduction caused by pipe movement.
**In use:** "We're running 0.3 ppg trip margin on this section, tight hole."
**Common misuse:** Treated as a fixed number applied to every well regardless of hole condition, mud weight, or trip speed, instead of read off the drilling program's swab/surge model for the current configuration.

### Swab / Surge
Swab: the transient pressure reduction below a moving drillstring pulled out of hole, which can drop effective bottomhole pressure enough to induce a kick. Surge: the transient pressure increase below a string run in too fast, which can exceed fracture gradient and cause losses.
**In use:** "Slow it down through that zone, we don't have swab margin for that speed."
**Common misuse:** Conflated with static mud weight as if pipe speed doesn't matter once mud weight is set — swab and surge are functions of speed and hole geometry on top of static mud weight, not separate from it.

### Driller's Method
A well-control kill technique using two circulations: the first circulates the kick out on the original (pre-kick) mud weight, the second circulates kill-weight mud once it's mixed.
**In use:** "Shoe's got margin and mixing's going to take 45 minutes — we're running Driller's Method."
**Common misuse:** Assumed to be the default choice in all cases rather than one of two standard methods selected based on shoe strength, weight-up time, and site policy; Wait-and-Weight is the other, not an inferior fallback.

### Wait-and-Weight (Engineer's Method)
A well-control kill technique that circulates only once, after the mud has already been weighted up to kill weight, so kill mud reaches the shoe and bit sooner.
**In use:** "Weak shoe on this one — we're waiting and weighting before we start circulating."
**Common misuse:** Assumed to always be "safer" because it protects the shoe sooner; it delays the start of circulation while mud is weighted up, which has its own cost depending on well conditions.

### Mechanical Specific Energy (MSE)
The energy input per unit volume of rock removed, combining WOB, torque, RPM, and ROP into a single real-time efficiency number; a sustained rise in MSE without a matching ROP gain signals the bit has passed its founder point.
**In use:** "MSE's climbing and ROP's flat — back the weight off, we're past founder."
**Common misuse:** Read as a pure "drilling efficiency score" to maximize in isolation, rather than as a diagnostic for when added WOB stops converting to rock removal.

### Founder point
The WOB (at given RPM) beyond which additional weight no longer increases ROP proportionally, because the bit is bogging down, balling, or whirling instead of cutting more efficiently.
**In use:** "We're past founder on this bit — more weight isn't buying us anything but wear."
**Common misuse:** Confused with simply "high WOB," when it specifically means the point where the ROP-to-WOB relationship breaks down, which varies by bit, formation, and cleaning efficiency.

### Differential sticking
The pipe becoming pinned against the wellbore wall by the pressure differential between an overbalanced mud column and a lower-pressure permeable formation, worsened by extended static (non-moving) time across that interval.
**In use:** "We've been static too long across that sand at this overbalance — working the pipe until the connection's made."
**Common misuse:** Called "stuck pipe" generically without distinguishing it from mechanical sticking (cuttings pack-off, keyseat, wellbore instability), which requires a different freeing approach.

### Kick tolerance
The maximum influx volume a well can take and still be circulated out safely without exceeding the fracture gradient at the casing shoe, given the current mud weight and well geometry.
**In use:** "Kick tolerance on this interval is thin — we're keeping a tighter pit-gain alarm here."
**Common misuse:** Treated as a single fixed number for the whole well rather than something that changes with depth, mud weight, and how close the shoe's fracture gradient is to current formation pressure.

### Connection gas
A rise in gas content of the returning mud associated with each connection, caused by the brief pressure reduction (a form of swab) when pumps stop and pipe is added.
**In use:** "Connection gas has been climbing the last five connections — trend's worth flagging even though each spike falls off."
**Common misuse:** Dismissed individually because each spike is small and falls off after pumps restart, missing the trend across multiple connections that signals a thinning pressure margin.

### Annular preventer
A BOP component that seals around the drillstring (of varying sizes) using a rubber packing element, typically the fastest BOP element to close in a shut-in and the first one used.
**In use:** "Shutting in on the annular, then we'll space out for the rams."
**Common misuse:** Treated as interchangeable with the pipe rams; the annular seals around variable pipe sizes and is usually the first-response closure, while rams provide the higher-pressure, longer-duration seal.

### Slow Circulating Rate (SCR) pressure
The standpipe pressure recorded at a reduced ("kill") pump rate, measured periodically before any kick occurs, used as the baseline for calculating initial and final circulating pressures during a kill.
**In use:** "Pull the current SCR off the log — we need it for the kill sheet, not a guess."
**Common misuse:** Estimated or reused from an old, stale reading after mud properties or hole depth have changed, instead of using the most recent pre-kick measurement, which throws off the entire ICP/FCP schedule.
