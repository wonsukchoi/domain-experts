# Red flags

Smell tests a senior valve tech catches on the first pass through a work request or a diagnostic trend. Format for each: what it usually means, the first question to ask, and the data to pull before committing to a repair plan.

## 1. Positioner signature test shows stiction/deadband greater than ~3% of travel span

**Usually means:** packing over-torque or a mismatched packing material, or a worn positioner feedback linkage — not a tuning problem, even if the process symptom is a limit cycle.

**First question:** "When was this valve last repacked, and to what torque/material spec — does it match what's actually installed?"

**Data to pull:** last packing work order and torque spec sheet, current signature-test trend, feedback linkage/cam inspection record.

## 2. Valve operating at under 20% of rated Cv at normal flow

**Usually means:** the trim or valve body is oversized for the current process case — often a body sized for a future capacity that never materialized, or a post-debottleneck rate reduction that was never fed back into sizing.

**First question:** "What's the current design flow case versus the one this valve was originally sized against?"

**Data to pull:** process design basis/data sheet, Cv sizing calculation, current flow trend at normal operation.

## 3. Loop retuned more than twice in 90 days without resolving an oscillation

**Usually means:** a mechanical cause — stiction, backlash, or actuator air-supply instability — is being treated as a controller tuning problem.

**First question:** "Has a valve signature or stroke test been run on this valve, or has every attempt gone straight to the PID parameters?"

**Data to pull:** PID tuning change history, process trend showing the oscillation, most recent (or absent) signature test.

## 4. Seat leakage test result exceeds the specified FCI 70-2 class allowable rate

**Usually means:** seat or seal wear, trapped debris, or a trim material mismatch for the actual service conditions (temperature, particulate, corrosive component) — the original class specification may still be correct even though the current hardware fails it.

**First question:** "What class was specified for this service, and is that class still the right one, or has the service changed?"

**Data to pull:** test report with measured leakage rate, original valve spec sheet and trim material certification, any process change since original specification.

## 5. Actuator stroke time has drifted more than ~10% slower than its commissioning baseline

**Usually means:** degraded instrument air supply (fouled filter/regulator), diaphragm or spring wear, or rising packing friction — any of which reduces available actuator authority before it reduces stroke speed enough to fail a pass/fail test outright.

**First question:** "Has supply air pressure and quality been checked directly at the actuator, not just at the header?"

**Data to pull:** stroke-time trend since commissioning, air supply pressure log at the actuator, filter-regulator maintenance record.

## 6. A PHMSA-regulated regulator or relief-valve test is due within 30 days of the 15-month deadline with no test scheduled

**Usually means:** the interval is being tracked reactively against the hard deadline rather than proactively, leaving no time to repair and retest if the device fails.

**First question:** "When exactly is the test scheduled, and is there enough float built in to retest if it doesn't pass the first time?"

**Data to pull:** PHMSA compliance tracking log, last test date and result, current test scheduling window.

## 7. A hydrostatic or pneumatic test shows the pressure drop only in the last third of the hold time

**Usually means:** a slow weep-type leak — packing, a gasket, or a micro-crack — rather than a gross seat or shell defect, which typically shows an immediate, steep drop.

**First question:** "Exactly when in the hold period did the pressure start moving, and does that correlate with a specific joint or seal?"

**Data to pull:** full pressure-versus-time log for the test (not just the pass/fail result), joint-by-joint visual inspection notes.

## 8. Actuator thrust/torque margin was calculated at normal operating ΔP, not at maximum shutoff ΔP

**Usually means:** the actuator will pass every normal-operation acceptance check and still stall or fail to fully close during an upset or emergency shutdown, when the differential pressure is highest.

**First question:** "What's the required thrust at the worst-case shutoff differential — valve closed, full upstream pressure, atmospheric downstream — not the normal-flow ΔP?"

**Data to pull:** actuator sizing calculation and its assumed ΔP, process P&ID for the worst-case pressure scenario, actuator rated thrust at minimum expected supply pressure.

## 9. A positioner is recalibrated to correct a symptom without first checking the mechanical linkage or feedback for wear

**Usually means:** a zero/span shift or worn feedback linkage is being papered over electronically rather than fixed at its mechanical source, and the same drift will return.

**First question:** "Is the feedback linkage, cam, or potentiometer free of play, or is that being assumed rather than checked?"

**Data to pull:** linkage/feedback inspection record, positioner calibration history (frequency and magnitude of past recalibrations).

## 10. The same valve requires repacking or reseating more than once within 12 months

**Usually means:** an actual process condition — temperature cycling, cavitation, flashing, or particulate loading — exceeds the trim or packing material's design basis, not a one-off workmanship error.

**First question:** "Has the actual process condition at this valve (ΔP, temperature swing, cavitation index) been checked against what the original trim/packing selection assumed?"

**Data to pull:** process trend at the valve over the repair interval, original trim material spec, cavitation/flashing calculation if one exists.

## 11. A valve is specified or accepted at a leakage class tighter than the service's actual consequence-of-leak requires

**Usually means:** a prior incident drove a blanket over-specification (e.g., Class VI everywhere) rather than a service-by-service consequence assessment, adding cost and maintenance burden without a matching safety benefit.

**First question:** "What specific consequence justifies bubble-tight shutoff on this particular valve, versus the class it would otherwise need?"

**Data to pull:** original specification justification, service description and consequence-of-leakage assessment, comparable valves in similar service and their specified class.
