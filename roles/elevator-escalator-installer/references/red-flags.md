# Red flags

Smell tests a licensed mechanic catches before signing a test report or returning equipment to service. Verify every numeric threshold against the code edition adopted by the local AHJ — the figures here are the commonly cited values and are flagged where they vary by edition.

### Governor trip speed reads outside 100–110% of rated speed (mid-speed cars; band narrows at higher rated speeds)

- **Usually means:** governor calibration drift, or a prior field adjustment intended to stop nuisance trips that quietly removed the code's overspeed margin.
- **First question:** "When was this governor last calibrated, and has anyone adjusted the trip point since the last Category 1 or Category 5 test?"
- **Data to pull:** governor maintenance/calibration history, prior periodic test reports' recorded trip speeds (look for a trend toward the boundary, not just today's single reading), tachometer calibration certificate.

### Door restrictor allows manual opening beyond ~4 in (100 mm) outside the unlocking zone

- **Usually means:** worn or misadjusted restrictor mechanism, or a restrictor retrofit that was never actually verified after installation.
- **First question:** "Has the restrictor been pry-tested with a gauge since installation, or only visually confirmed present?"
- **Data to pull:** restrictor installation/retrofit date and commissioning test record, current pry-test gauge reading, unlocking-zone dimension confirmed against the adopted code edition.

### Buffer strike test shows average retardation above ~1g, or peak retardation exceeding ~2.5g for more than a brief interval

- **Usually means:** buffer stroke undersized for the actual (not nameplate-assumed) governor tripping speed, or a spring buffer that has taken a compression set and no longer delivers its rated stroke.
- **First question:** "What governor tripping speed was actually measured today, and does the installed buffer's rated stroke cover that speed with margin?"
- **Data to pull:** measured governor tripping speed, buffer nameplate stroke and rated speed, computed minimum required stroke at 1g (see `references/playbook.md`), buffer manufacture/install date.

### Category 5 (5-year full-load) test overdue or partially completed in a prior no-load cycle

- **Usually means:** a Category 1 (annual, no-load) test was filed in place of, or mistaken for, the due Category 5 full-load test, most often for the counterweight safety, which is easy to skip when only the car-side items get full-load attention.
- **First question:** "Pull the last Category 5 report — was the counterweight safety tested at full load in this cycle, or is that record still from an earlier annual test?"
- **Data to pull:** full periodic test history for the unit, load weight actually used in the most recent full-load test, QEI witness signature and date on file.

### A jumper, bypass wire, or inspection-mode override is found on the safety circuit during a routine visit

- **Usually means:** a prior troubleshooting visit removed a redundant device from the circuit to isolate a fault and never restored it — the most direct route to converting defense-in-depth into a single point of failure.
- **First question:** "Who was the last mechanic on this unit, and what fault were they chasing?"
- **Data to pull:** service call log for the unit, wiring as-built vs. current physical wiring, controller fault history around the date of the last service call.

### Car speed measured on an independent tachometer disagrees with the controller's displayed speed by more than a small margin

- **Usually means:** encoder/selector drift, rope slip at the drive sheave (traction loss), or a controller speed-reference fault — any of which invalidates a governor test performed against the controller's displayed value instead of a calibrated independent reading.
- **First question:** "Was the governor test's speed reading taken from the tachometer or from the controller display?"
- **Data to pull:** independent tachometer reading vs. controller display at the same instant, rope tension and traction data, encoder calibration record.

### Releveling requires repeated correction beyond the normal tolerance band at a given landing

- **Usually means:** hydraulic valve drift, traction motor drive calibration issue, or (on hydraulic units) oil temperature/viscosity effects — all of which raise the risk of a door-open-movement near miss if releveling drifts far enough that the door zone and door-open interlock logic disagree about whether the car is "at floor."
- **First question:** "How many releveling corrections has this landing needed this week, and is the trend getting worse?"
- **Data to pull:** releveling event log by landing, door-zone sensor calibration, hydraulic valve or drive parameter history.

### Counterweight safety not tested to the same load standard as the car safety in the current 5-year cycle

- **Usually means:** an incomplete Category 5 test filed as complete — same failure pattern as the overdue-Category-5 flag above, but specifically the counterweight side, which has no rider-visible symptom to prompt a complaint.
- **First question:** "Show me the counterweight safety's load-tested trip record for this 5-year cycle specifically, not the car safety's."
- **Data to pull:** counterweight safety test load and date, car safety test load and date, whether both fall inside the same 5-year window.

### Escalator step-chain elongation reading is within ~10% of the tensioning device's remaining take-up travel

- **Usually means:** the chain is approaching the end of its adjustable range; the next elongation increment has nowhere to go, which forces an unplanned chain replacement rather than a scheduled one.
- **First question:** "What was the elongation reading 6 and 12 months ago, and is the rate of change accelerating?"
- **Data to pull:** elongation gauge readings over the last several service visits, tensioning device's total remaining travel, ridership/duty-cycle data if elongation rate looks unusually fast for the unit's age.

### Firefighters' Service Phase I/II key switch is found engaged during normal passenger operation

- **Usually means:** the switch was left engaged after a test, drill, or actual fire-department activation and never returned to normal, which changes how the car responds to hall calls and door operation without an obvious visual cue to riders or building staff.
- **First question:** "When was Phase I/II last activated, and by whom — a drill, a test, or an actual alarm event?"
- **Data to pull:** fire alarm system activation log cross-referenced with elevator controller event log, last scheduled Phase I/II functional test date.
