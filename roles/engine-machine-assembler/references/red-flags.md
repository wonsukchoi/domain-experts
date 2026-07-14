# Red flags

### A multi-bolt joint torqued sequentially to final value rather than in the specified multi-stage pattern
- **Usually means:** uneven clamping load or component warping risk, even if every bolt ends up at the correct final torque.
- **First question:** was the specified sequence/staging pattern followed, or was each bolt taken directly to final torque in convenient order?
- **Data to pull:** the joint's specified torque sequence and stages, actual method used.

### Bearing clearance confirmed only by checking that a component turns freely or "goes together" by hand
- **Usually means:** direct clearance measurement wasn't performed, and neither excessive nor insufficient clearance is reliably caught by this check alone.
- **First question:** was clearance directly measured (plastigauge, feeler gauge, or specified method), or only confirmed by free rotation?
- **Data to pull:** the specified clearance measurement method and spec, actual measurement if performed.

### A sub-assembly integrated into the complete machine without being tested independently first
- **Usually means:** a defect in that sub-assembly, if present, won't be caught until final test, when it's far more costly to diagnose and correct.
- **First question:** was this sub-assembly tested before integration, or is testing deferred entirely to final assembly?
- **Data to pull:** sub-assembly test record if one exists, integration sequence.

### A break-in procedure skipped or compressed to save time
- **Usually means:** components requiring a controlled wear-in period (rings, bearings) may not seat properly, risking reduced performance or premature wear.
- **First question:** was the full specified break-in profile completed, or was it shortened/skipped?
- **Data to pull:** the specified break-in procedure, actual break-in performed.

### A critical clearance assumed correct because every individual component passed its own inspection
- **Usually means:** an unfavorable tolerance stack-up across multiple in-spec components could still produce an out-of-spec assembly.
- **First question:** has the actual assembled clearance been measured directly, or only inferred from individual component tolerances?
- **Data to pull:** individual component tolerance data, actual assembled clearance measurement if performed.

### A performance issue (overheating, vibration, premature wear) appearing after assembly with no clear diagnosis
- **Usually means:** the root cause could be torque sequence, clearance/preload, stack-up, or break-in — each requiring different diagnostic checks.
- **First question:** has each of these distinct possible causes been checked individually, or has one been assumed without verification?
- **Data to pull:** torque sequence record, clearance measurements, break-in completion record.

### A component substitution (different shim, bearing shell, or part lot) made without re-verifying critical clearance
- **Usually means:** the substitution may shift the actual stack-up even if the substitute part is itself within its own individual tolerance.
- **First question:** was clearance re-measured after the substitution, or assumed unaffected since the substitute part is in spec?
- **Data to pull:** the substitution made, clearance measurement before and after if available.

### Multiple units from the same assembly line showing a similar premature failure pattern
- **Usually means:** a systematic assembly practice issue (torque sequence not followed, clearance measurement skipped) rather than isolated unit variation.
- **First question:** do the failing units share a common assembly source or process step?
- **Data to pull:** failure traceability by assembly source, common process step across affected units.

### A torque wrench used for a sequenced multi-stage procedure without verification it was set/used correctly at each stage
- **Usually means:** an error at an intermediate stage (e.g., skipping the 30% stage and going straight to 70%) could still produce uneven clamping even with correct final values.
- **First question:** does the record show torque values applied at each specified stage, or only the final value?
- **Data to pull:** stage-by-stage torque application record if documented.

### An assembly returned for rework with clearance or torque not re-verified after the rework
- **Usually means:** the specific issue prompting rework may have been addressed, but other parameters disturbed during rework weren't re-checked.
- **First question:** was full clearance/torque re-verification performed after rework, or only the specific reworked component addressed?
- **Data to pull:** rework record, post-rework verification results.
