# Vocabulary

### Tool offset (wear vs. geometry)
A value in the CNC control compensating for a tool's actual dimensions relative to its programmed/nominal path — a geometry offset accounts for the tool's base size, a wear offset compensates for gradual dimensional change from use.
**In use:** "We adjusted the wear offset, not the geometry offset — the tool's base size didn't change, it's just worn."
**Common misuse:** Adjusting the wrong offset type, or treating repeated wear-offset adjustments as a permanent fix rather than a temporary compensation with a tool-replacement plan behind it.

### First-article inspection
A full dimensional and specification check of the first part produced from a new or changed setup, validating that the program, tool offsets, and fixture are correct together before production quantity is run.
**In use:** "First article passed all callouts — cleared to run the full 500-piece order."
**Common misuse:** Treating a visual check or "it looks right" as equivalent to a first-article inspection — first-article specifically means measuring against the full print, not a subjective assessment.

### Work-holding repeatability
The consistency with which a fixture positions and secures a part in the same physical location relative to the machine's coordinate system, cycle after cycle.
**In use:** "Parts are drifting in a way that doesn't match the tool wear curve — checking work-holding repeatability before we blame the tool."
**Common misuse:** Assuming a fixture is repeatable because it "worked before" without periodic verification — wear, damage, or debris in a fixture can degrade repeatability without any visible change to the fixture itself.

### Tool life curve
The characterized relationship between a tool's usage (parts produced or time run) and its expected dimensional wear, used to predict when a tool will need replacement or offset compensation.
**In use:** "We're at 95 of this insert's characterized 400-part life — the wear rate we're seeing tracks the expected curve."
**Common misuse:** Treating tool life as a fixed number that applies regardless of material or conditions — the characterized life curve assumes specific material and cutting conditions, and a change in either (a harder material lot, a different feed rate) can shift actual wear rate away from the characterized curve.

### In-process measurement / SPC sampling
Measuring parts at specified intervals during a production run (rather than only at the beginning or end) to catch a developing out-of-tolerance trend before it produces a large quantity of nonconforming parts.
**In use:** "Sampling every 20th part per the quality plan — that's what caught this trend before it crossed spec."
**Common misuse:** Treating each individual in-process measurement as a standalone pass/fail check rather than a data point in a trend — a single in-tolerance reading doesn't tell you whether the next several parts are safely in tolerance too if a clear drift is underway.

### Trend extrapolation
Projecting a measured trend forward to estimate when a monitored dimension will cross a tolerance limit, used to decide whether the current sampling interval provides adequate margin.
**In use:** "Extrapolating this drift rate, we cross tolerance around part 100 — that's exactly our next scheduled sample, so we're tightening the interval now."
**Common misuse:** Waiting for the next scheduled sample point to confirm a trend crossing rather than extrapolating proactively — by the time a scheduled check confirms an out-of-tolerance part, every part produced since the prior check is of unknown status.

### CMM (Coordinate Measuring Machine)
A precision measurement device that uses a probe to record a part's exact physical dimensions in three-dimensional space, used for detailed dimensional verification beyond what handheld gauges can check.
**In use:** "Sending this first article to the CMM for a full dimensional report before we commit to the run."
**Common misuse:** Relying on CMM data alone without also tracking in-process trend data during the run — a CMM check confirms a single part at a point in time, while in-process trend monitoring is what catches drift developing across a run.

### Tool breakage / collision alarm
A machine control alarm triggered by an unexpected condition (excessive tool load, a probe/positioning fault) that can indicate a broken tool, a collision, or an out-of-tolerance condition mid-cycle.
**In use:** "Alarm tripped mid-cycle — checking the tool and the in-process part before clearing it and restarting."
**Common misuse:** Clearing an alarm and resuming the cycle as a reflex without investigating its cause — an alarm can indicate a condition that resuming blindly would compound (continuing to cut with a broken tool, for example).

### Program revision control
The practice of tracking which specific version of a CNC program is currently loaded and verified against the job's approved specification, distinct from an older or draft version that may still exist in the system.
**In use:** "Confirm the program revision matches the job traveler before running — the wrong rev is a common source of a whole batch going out of spec."
**Common misuse:** Assuming the program currently loaded on the machine is automatically the correct, current revision without checking it against the job's specification — an outdated or draft revision left loaded from a prior job is a common, avoidable setup error.

### Nominal dimension
The exact target value a part's feature is designed to, distinct from its tolerance range (the acceptable deviation from that target).
**In use:** "We're not just aiming for 'within tolerance' — the wear-offset correction is meant to bring us back near nominal, not just inside the band."
**Common misuse:** Treating "anywhere within tolerance" as an equally good target as nominal — running consistently near one edge of the tolerance band (even if technically compliant) leaves less margin for the next source of variation, compared to running near nominal.
