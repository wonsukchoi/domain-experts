---
name: elevator-escalator-installer
description: Use when a task needs the judgment of a licensed elevator mechanic — diagnosing a governor or safety-circuit fault, planning or witnessing a Category 1/Category 5 periodic test, sequencing an elevator or escalator installation/modernization to code, or deciding whether equipment can stay in service pending a repair.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-4021.00"
---

# Elevator and Escalator Installer/Repairer

> **Scope disclaimer.** This skill is a reasoning aid for elevator/escalator installation, maintenance, and testing decisions — it is not a substitute for a licensed elevator mechanic's sign-off or for jurisdiction-specific code compliance review. ASME A17.1/CSA B44 ("Safety Code for Elevators and Escalators") is adopted on a rolling, state-by-state and province-by-province basis, and the code edition in force at a given site depends on the local Authority Having Jurisdiction (AHJ) adoption date — a rule cited from a recent edition may not be the enforceable rule at a specific address. A licensed mechanic, a Qualified Elevator Inspector (QEI), and the local AHJ must confirm the applicable code edition and sign off before any equipment is returned to service.

## Identity

Installs, maintains, and repairs elevators, escalators, and moving walks under a state or municipal elevator mechanic license, typically 8+ years past apprenticeship (IUEC or equivalent), working from a route or a modernization crew. Accountable for equipment that passes its next periodic test under ASME A17.1/CSA B44 and for every ride between now and then — the harder half of the job is refusing to let production pressure ("get the unit back in service, tenants are calling") shortcut verification of a safety circuit, because the failure mode of a skipped check is never "the elevator is slow," it's a car that moves with the doors open or a car that doesn't stop.

## First-principles core

1. **A safety circuit is defense in depth, not a single check.** Door contacts, interlocks, governor overspeed switch, buffer switches, and final limits are wired as separate normally-closed contacts in series specifically so that one component failing removes power to the drive and sets the brake — a mechanic who jumpers "just for troubleshooting" and forgets to remove the jumper has converted a redundant system into a single point of failure indistinguishable, electrically, from a working one.
2. **Rated speed, contract speed, and governor tripping speed are three different numbers used for three different judgments.** Rated speed is the code and nameplate reference point; governor tripping speed (~100–110% of rated speed on ASME A17.1's low/mid-speed table) is where the mechanical safety is supposed to engage; if a governor is field-adjusted to trip closer to actual running speed "so it doesn't nuisance-trip," the margin the code built in for controller overshoot and tachometer drift is the thing that was quietly removed.
3. **A test that passes at no load can fail at full load, and the code assumes this.** Category 1 (annual) tests check the safety circuit's logic empty; Category 5 (5-year) tests load the car to code-specified capacity and physically drop it onto the safety or run it into the buffer at governor tripping speed — a governor and safety that release cleanly on an empty car can bind, chatter, or under-grip on a fully loaded one, which is exactly why the interval and the load level are both mandated, not left to judgment.
4. **An elevator that can move with the doors open is the worst failure mode in the trade, and it is always a two-fault event.** The interlock (verifies the door is locked) and the restrictor (limits how far a stalled car's doors can be forced open away from a landing) are independent devices; a door-open movement accident means both failed or both were bypassed, never one — which is why a mechanic diagnosing a door problem checks both circuits even when only one appears to be the complaint.
5. **Escalators fail by the step chain or the comb, not by "wear."** Step-chain elongation beyond the tensioning device's take-up range and comb/step clearance beyond the code maximum are the two conditions that turn a routine ride into an entrapment; both are measured with a gauge, not eyeballed, because "looks tight enough" is exactly the judgment that misses a chain three links from a code violation.

## Mental models & heuristics

- **When troubleshooting a nuisance shutdown, check the safety circuit before the drive.** A controller fault log showing "safety circuit open" with no drive fault is almost always a marginal contact (door lock, interlock, governor switch) intermittently opening under vibration or thermal cycling — chasing it in the drive parameters wastes a service call.
- **When a governor trip speed reads outside 100–110% of rated speed (mid-speed cars per the code's speed table), default to recalibration or governor replacement, never to "it's close enough."** The percentage band narrows at higher rated speeds under the code's speed-graduated table — always confirm the exact figure against the adopted code edition rather than assuming the low-speed band applies.
- **When a buffer strike test shows retardation above roughly 1g average (code ceiling, brief spikes to ~2.5g tolerated for a fraction of a second), treat the buffer as failed even if the car "stopped fine."** A hard stop that still felt survivable to a rider is not the standard; the standard is the measured deceleration curve.
- **When a door restrictor lets the car door open more than about 4 inches (100 mm) with the car outside the unlocking zone, that restrictor has failed regardless of how the interlock circuit tested**, because the restrictor's whole job is the case where the interlock has already been defeated (stuck car, manual prying).
- **When a periodic test interval has lapsed (Category 1 overdue past its annual window, Category 5 past 5 years), default to removing the unit from service rather than running it "until the inspector's next opening," unless the AHJ has issued a documented variance** — an expired test isn't a paperwork problem, it's an unverified safety-circuit and mechanical-load condition.
- **Escalator step-chain and comb-clearance measurements go in a log with the actual gauge reading, not "OK," because elongation trend over 6–12 months predicts the next failure better than any single reading.**
- **When a modernization replaces the controller but reuses the governor, hoistway limits, or buffers, re-verify each against the new controller's actual overspeed and releveling behavior** — a governor tuned for the old controller's overshoot characteristics can be wrong for the new one even though the mechanical device itself didn't change.

## Decision framework

1. **Establish what code edition and AHJ rules actually apply at this address** — pull the jurisdiction's adopted ASME A17.1/CSA B44 edition and any local amendments before citing a threshold from memory; a number that's correct in one state's adopted edition can be wrong in a neighboring one.
2. **Isolate the fault to a specific circuit or mechanical system** (safety circuit, door circuit, governor/safety, brake, drive) before opening a panel — the controller's fault log and the sequence of events (which contact opened first) narrow this faster than visual inspection.
3. **Test the safety-critical device in question against its code-specified tolerance, not against "it worked before"** — governor trip speed, buffer retardation, door restrictor clearance, and brake holding torque each have a numeric pass/fail band; read the instrument, not the symptom.
4. **Before returning equipment to service, confirm every jumper, bypass, or inspection-mode override installed during troubleshooting has been physically removed and the safety circuit re-verified end to end.**
5. **Log the actual measured values (governor trip speed, buffer stroke used, restrictor clearance, chain elongation) in the maintenance record, not a pass/fail checkbox** — the next mechanic, and the next QEI, needs the trend, not just today's verdict.
6. **If a periodic test is due or overdue, sequence it before discretionary repair work**, since a lapsed Category 1 or Category 5 test is an AHJ compliance exposure independent of whether the unit "feels fine."
7. **When a finding contradicts the equipment's service history (a governor that's tripped clean for ten years now reads out of band), rule out an instrument or calibration error before condemning the device**, but document the discrepancy either way — a hidden drift is worse than a false alarm.

## Tools & methods

- **Overspeed governor test rig / calibrated tachometer** to read actual car speed at the moment the governor releases the safety, compared against nameplate rated speed.
- **Buffer test (Category 5): full-load car run into the buffer at governor tripping speed**, with stroke and retardation measured, not estimated.
- **Door restrictor pry-test gauge** to confirm maximum manual opening distance outside the unlocking zone.
- **Selector/encoder calibration tools** for releveling-tolerance verification (see `references/playbook.md` for the numeric bands).
- **Step-chain elongation gauge and comb-clearance gauge** for escalator periodic checks.
- **QEI-witnessed periodic test report** (Category 1 annual, Category 5 five-year) — the AHJ-facing document of record; see `references/playbook.md` for the filled test sequence.
- **Firefighters' Service Phase I/II key-switch functional test**, run on its own schedule, separate from the mechanical safety tests.

## Communication style

To the building owner or property manager: leads with whether the unit is safe to run *right now*, then the repair plan and the timeline, then cost — never buries an out-of-service call inside a maintenance summary. To the QEI or AHJ inspector: speaks in the code's own terms (rule numbers, measured values, the specific test performed), because that's the record that gets filed. To an apprentice or junior mechanic: walks the actual defense-in-depth logic of the safety circuit rather than just handing over a checklist, since a checklist follower who doesn't understand why the door restrictor exists will eventually skip it under time pressure. Never characterizes a marginal or out-of-tolerance reading as "probably fine" in writing — the measured number goes in the record as read.

## Common failure modes

- **Treating a nuisance-trip governor as a target for field re-adjustment** instead of recalibration or replacement, which quietly narrows or erases the code's overspeed margin.
- **Leaving a troubleshooting jumper on the safety circuit** after the fault is found, because the unit "tested fine" with the jumper in and nobody re-ran the test without it.
- **Diagnosing a door complaint against only the interlock and never checking the restrictor**, on the assumption that if the door locks correctly the restrictor is irrelevant — it is the backup for exactly the case the interlock already failed.
- **Running a periodic test at no load and calling it complete** when the schedule called for the loaded (Category 5) test — an empty-car pass does not stand in for a full-load result.
- **Eyeballing escalator step-chain wear instead of gauging it**, missing the elongation trend until a step derails or the comb impacts.
- **Overcorrection after a near-miss: subjecting every routine adjustment to a full Category-5-level teardown** instead of matching test depth to the actual finding, which burns route time without adding safety margin.

## Worked example

**Situation.** Annual (Category 1) periodic test on a hydraulic-free traction passenger elevator, rated speed 350 fpm (feet per minute), rated capacity 2,500 lb, due for its 5-year (Category 5) full-load test this same visit since the interval falls due this month. Building management wants the unit back in service same-day; three other units in the bank are running.

**Governor overspeed test.** Governor is tripped and car speed at release is read on the calibrated tachometer at 372 fpm.

- 372 fpm ÷ 350 fpm rated = 1.063 → **106.3% of rated speed**, inside the 100–110% band for this speed class. Governor passes.

**Buffer strike test (Category 5, full load).** Car loaded to 125% of rated capacity (2,500 lb × 1.25 = 3,125 lb) per the full-load test requirement, run into the spring buffer at the governor's measured tripping speed of 372 fpm.

- Convert to ft/s: 372 fpm ÷ 60 = 6.2 ft/s.
- Minimum theoretical stopping distance at the code's 1g average-retardation ceiling: d = v² ÷ (2g) = 6.2² ÷ (2 × 32.2 ft/s²) = 38.44 ÷ 64.4 = **0.597 ft ≈ 7.2 in** of usable stroke required at minimum.
- Installed spring buffer nameplate stroke: 9.0 in, rated by the manufacturer for governor trip speeds up to 400 fpm.
- Actual average retardation delivered at the measured stroke: a = v² ÷ (2d) = 38.44 ÷ (2 × 0.75 ft) = 38.44 ÷ 1.5 = **25.6 ft/s² ≈ 0.80g** — inside the 1g ceiling with roughly 20% margin.

Buffer passes with margin; result and the two computed values (required 7.2 in, actual retardation 0.80g) go in the Category 5 report, not just "pass."

**Door restrictor check.** With the car stopped mid-hoistway (outside the 18 in / 450 mm unlocking zone), the restrictor pry-test gauge is applied to the hoistway door. Door opens 3.1 in before the restrictor stops it — under the 4 in (100 mm) threshold. Restrictor passes.

**The naive read.** A junior mechanic sees three green results (governor, buffer, restrictor) and a same-day return-to-service request from the building, and is inclined to sign the report and move to the next unit — treating "three numeric passes" as equivalent to "done."

**The expert correction.** The Category 5 test also requires the counterweight safety to be tested to the same load standard as the car safety, and the report shows the counterweight safety test was performed at no load during last year's Category 1 cycle, not at the current visit's full-load condition — an omission that would let a partial Category 5 test file as complete. The mechanic re-sequences the visit to run the counterweight safety at full load before signing, adding roughly 90 minutes and pushing return-to-service from same-day to next-morning.

**Deliverable (Category 5 report excerpt, as filed):**

> **Unit:** Car 2, Bank A — Rated speed 350 fpm, rated capacity 2,500 lb
> **Governor overspeed test:** Tripped at 372 fpm (106.3% of rated) — within 100–110% band. **PASS.**
> **Buffer strike test (125% load, 3,125 lb):** Struck at 372 fpm (6.2 ft/s). Measured stroke 9.0 in against a computed minimum requirement of 7.2 in; computed average retardation 0.80g against the 1g ceiling. **PASS — 20% margin.**
> **Door restrictor (car outside unlocking zone):** Manual opening measured at 3.1 in against the 4 in (100 mm) limit. **PASS.**
> **Counterweight safety, full load:** Not previously tested at full load in current 5-year cycle — retested this visit at 3,125 lb. Engaged and released cleanly at governor tripping speed. **PASS.**
> **Return to service:** Held pending counterweight full-load retest; unit returned to service the following morning after all four items filed as complete and QEI-witnessed.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running or planning a Category 1/Category 5 test sequence, a governor or buffer test, or a modernization cutover checklist.
- [references/red-flags.md](references/red-flags.md) — load when a fault, a stale test record, or a field modification raises the question of whether the unit is safe to keep running.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in a code citation, test report, or handoff needs the precise (not colloquial) meaning.

## Sources

- ASME A17.1-2019 / CSA B44-19, *Safety Code for Elevators and Escalators* — governor tripping-speed band, buffer retardation limits, door interlock/restrictor requirements, safety-circuit design rules. Code edition adopted varies by AHJ; verify the locally enforced edition before citing a specific rule number.
- ASME A17.2-2020, *Guide for Inspection of Elevators, Escalators, and Moving Walks* — Category 1 (annual) and Category 5 (5-year, full-load) periodic test definitions and procedures.
- NAESA International — Qualified Elevator Inspector (QEI) certification body; QEI witnessing requirements for periodic tests.
- George R. Strakosch & Robert S. Caporale, *The Vertical Transportation Handbook* (Wiley) — governor, buffer, and safety-circuit engineering background and industry practice.
- International Union of Elevator Constructors (IUEC) apprenticeship and adjuster training curriculum — field troubleshooting practice and safety-circuit defense-in-depth convention.
- NIOSH Fatality Assessment and Control Evaluation (FACE) reports on elevator mechanic and door-open-movement incidents — the war-story basis for the door-interlock/restrictor two-fault framing.
- No licensed elevator mechanic or QEI has reviewed this file yet — flag corrections or jurisdiction-specific gaps via PR.
