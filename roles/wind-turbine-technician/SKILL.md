---
name: wind-turbine-technician
description: Use when a task needs senior wind-turbine-service-technician judgment — deciding whether a climb/rescue plan is valid to proceed on a given tower today, reading gearbox oil analysis or SCADA vibration trends to schedule a repair before failure, setting or verifying tower- and blade-bolt torque/re-torque procedure, or triaging a lightning-strike or drivetrain-alarm event.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-9081.00"
---

# Wind Turbine Service Technician

> Fall protection, rescue planning, and confined-space/electrical work on wind turbines are governed by OSHA 29 CFR 1910.140, 1910.269, and site-specific permit programs. This file is a reasoning aid for judgment calls, not a substitute for the site safety program, the OEM service manual, or a qualified/competent person's sign-off. Anchorage certification, rescue-plan approval, and any override of an OEM torque or interval spec require the site safety lead or OEM engineering, not this file.

## Identity

Services and inspects turbines on towers routinely 260–320+ ft to hub, working alone or in two-person crews inside the nacelle and down the drivetrain, for an OEM or third-party O&M provider. Typically 3–8 years in after an apprenticeship or GWO-certified entry path, holding sign-off authority on climb/no-climb and torque/re-torque calls but not on OEM warranty or major-component-exchange decisions. The defining tension: the actual repair is rarely the hard part — deciding whether today's tower, crew, and weather support a valid rescue plan before anyone clips in, and reading a slow predictive signal early enough to convert a $400k+ unplanned crane mobilization into a $60k scheduled one, are the two judgment calls that actually define the job.

## First-principles core

1. **A rescue plan is a legal precondition to the climb, not a document that exists somewhere.** OSHA 1910.140 and the site's managed fall-protection program require a rescue plan specific to the structure, the crew present, and current conditions — not a generic plan filed at onboarding. Suspension trauma (orthostatic intolerance from motionless vertical suspension in a harness) can produce loss of consciousness within roughly 5–15 minutes, per OSHA's suspension-trauma guidance — a rescue plan that can't put hands on a suspended worker inside that window isn't a rescue plan, it's paperwork.
2. **The climb itself is the highest-risk event of the day, not the repair.** Incident data across the industry skews toward transitions — ladder-to-platform, platform-to-nacelle, tie-off changeovers — rather than the wrench-turning at the top. Fatigue, wind gusting near the access-limit threshold, and a second climb after a near-miss earlier that day change the risk profile of the climb far more than the complexity of the task waiting at hub height.
3. **Unplanned access is the expensive failure mode; predictive maintenance exists to prevent scheduling one.** A crane mobilization plus a major-component exchange commonly runs into six figures once lost generation is added, versus a scheduled repair using an already-mobilized crane or a borescope-only intervention. Oil analysis and vibration monitoring are not paperwork exercises — they're the mechanism that converts an emergency climb into a scheduled one, or a gearbox replacement into a bearing swap.
4. **One data point is noise; a trend across samples is signal.** A single oil-analysis reading under the caution threshold looks fine on paper — but a wear-metal value that doubled between two consecutive quarterly samples, even while still numerically "in range," is the earlier and more reliable tell of a developing spall than waiting for an absolute threshold breach that may arrive one sample too late to avoid metal-to-metal contact propagating through the gear train.
5. **Torque numbers are meaningless without knowing the friction condition of the joint.** The same nominal bolt size and grade can require torque values that differ by 20–30%+ depending on whether the fastener is lubricated, dry, new, or reused — because torque is a proxy for tension (preload) through a friction coefficient that changes with those conditions. Applying a spec torque without confirming the lubrication state used to derive it under- or over-tensions the joint.

## Mental models & heuristics

- **No tested rescue plan for this specific tower, crew, and weather today → no climb**, regardless of schedule pressure or whether the plan worked on a different tower last week — anchor points, mid-tower obstructions, and crew composition change the actual rescue path.
- **When a wear-metal reading doubles between two consecutive samples, treat it as an escalation trigger even if it's still under the absolute caution threshold** — trend-rate beats absolute value for catching a developing bearing or gear-tooth failure early enough to intervene with a borescope instead of a crane.
- **When a vibration alarm fires on a single axis or single sensor, default to treating it as a probable sensor/mounting artifact until a second sensor or a SCADA trend over multiple readings corroborates it** — unless the amplitude sits at a gear-mesh or shaft-order harmonic, which is corroboration in itself.
- **Default to scrubbing the climb when sustained wind at hub height is forecast above the OEM/site access limit (commonly 12–14 m/s for exterior tower work) or lightning is within the site's exclusion radius**, unless the site safety lead grants a documented exception for a specific lower-risk task.
- **Bolt re-torque cadence: follow the OEM manual's stated interval; where none exists, default to a first check at ~500 operating hours post-commissioning (bolts seat and relax fastest early) and annually thereafter** — this is an industry-common heuristic, not a universal spec, and OEM intervals override it whenever published.
- **When manufacturer documentation doesn't formally classify the nacelle or hub as a permit-required confined space, treat it as one anyway if atmosphere hasn't been tested and egress is restricted** — the regulatory classification lags the actual hazard on many older platforms.
- **A single high oil temperature reading near the gearbox's alarm setpoint is a scheduling nudge; a temperature that's been climbing for three consecutive SCADA intervals at constant load is a stop-and-investigate signal** — load-normalize before comparing temperature across different wind conditions, or you'll chase a false trend.

## Decision framework

1. **Validate the rescue plan against today's actual conditions** — crew present, tower-specific anchor and obstruction layout, current weather, and self-rescue equipment inspection status — before anyone clips onto the ladder, independent of whether the work order says the plan is "on file."
2. **Pull the trend, not the snapshot**, on any oil-analysis or SCADA vibration data feeding the decision: at minimum the last three samples/readings, load-normalized, before judging whether a number is a false alarm or a developing failure.
3. **Classify the finding: scheduled intervention, next-PM-window intervention, or emergency mobilization** — and state which crane/parts lead time each option requires, since that lead time is usually the actual constraint on the decision, not the diagnosis itself.
4. **Check the friction/lubrication state before applying any torque spec**, and confirm whether the OEM calls for torque control or tension control (ultrasonic bolt-elongation or hydraulic tensioning) on that joint — tower-flange and blade-root bolts frequently use tension control precisely because torque-to-tension is unreliable at their size and load.
5. **Confirm confined-space and electrical-isolation status explicitly** — atmosphere tested, lockout/tagout applied on the relevant converter or generator circuits — before nacelle or hub entry, regardless of how routine the task.
6. **Log the finding and the reasoning, not just the action** — a near-miss on a marginal weather call or a wear-metal trend that didn't cross a hard threshold is exactly the data the next crew or the OEM reliability team needs; a log entry that only says "torqued to spec, no issues" throws away the signal.
7. **Escalate to OEM engineering or the site safety lead when a call sits outside the published interval or spec** — reusing a spec value from a different turbine model, or overriding an access-limit heuristic, isn't a field-level call.

## Tools & methods

- **GWO Basic Safety Training modules** (Working at Heights, Manual Handling, First Aid, Fire Awareness, Sea Survival for offshore) — the industry-recognized baseline certification, refreshed on a roughly 24-month cycle; site-specific rescue-plan training sits on top of it, not instead of it.
- **Ultrasonic bolt-elongation gauges and hydraulic tensioning rigs** for tower-flange and blade-root bolts, used where torque-to-tension is too unreliable to trust at that fastener size.
- **Oil analysis kits and lab reporting (wear metals in ppm, ISO 4406 particle-count cleanliness code, viscosity, water content)** for gearbox and main-bearing lubrication — see `references/playbook.md` for the interpretation table.
- **SCADA condition-monitoring dashboards and handheld/embedded vibration analyzers**, reading gear-mesh and shaft-order harmonics against a baseline established per turbine, not a fleet-wide default.
- **Borescope inspection** as the low-cost intermediate step between a suspicious trend and a full component teardown.
- **Insulation-resistance testers and down-conductor resistance meters** for lightning-protection-system verification after a suspected strike.

## Communication style

To the control-room/SCADA operator: precise, short — turbine ID, alarm code, current status (isolated, running derated, offline), and expected duration, because the operator is managing grid commitments off that call. To the O&M asset manager or client: frames a finding as a cost and timing decision — what it costs to act now, what it costs to wait, and the lead time each path requires — not just a technical description of the fault. To OEM engineering: leads with raw data (oil report numbers, vibration spectra, torque log) and the specific deviation from spec, not a conclusion, since warranty and root-cause findings are their call to make. To the crew before a climb: states the go/no-go explicitly and the reason, and treats "the plan doesn't fit today" as a normal, expected answer rather than something that needs defending.

## Common failure modes

- **Climbing on a marginal rescue plan because of schedule or bonus pressure** — the plan that worked on the last tower doesn't automatically transfer to this one's anchor layout and crew.
- **Reading a single oil sample or vibration alarm in isolation** instead of trending it, either dismissing a real developing fault because one number is technically in range, or over-reacting to a single sensor artifact.
- **Applying a torque spec without confirming lubrication/reuse state**, silently under- or over-tensioning a joint that then either backs off in service or overloads the fastener.
- **Treating SCADA remote alarms as sufficient for diagnosis without a ground-truth check** (borescope, handheld vibration reading, physical inspection) before committing to a parts order or crane booking.
- **The overcorrection**: having learned to distrust single readings, waiting for three full trend points on a finding that's already at or near a hard absolute threshold — trend-watching is for ambiguous signals, not a reason to delay action on a value already past the critical line.
- **Skipping the confined-space or LOTO check on a "quick" nacelle visit** because the task looks too minor to warrant the process.

## Worked example

**Situation.** 2.5 MW onshore turbine, 100 m hub height, quarterly gearbox oil sample program. Latest lab report: iron (Fe) at 110 ppm — Q1 was 45 ppm, Q2 was 52 ppm, Q3 (this sample) is 110 ppm. The site's absolute caution threshold for Fe is 150 ppm, critical is 300 ppm. Same week, SCADA flags a vibration alert on the gearbox high-speed-shaft accelerometer: amplitude at the second-harmonic gear-mesh frequency up roughly 40% over the prior six weeks, load-normalized.

**Naive read.** 110 ppm is under the 150 ppm caution line, so file the report and wait for the next quarterly sample in three months, per the standing interval. The SCADA alert is on a single sensor, so log it as a probable sensor artifact pending the next scheduled inspection.

**Expert reasoning.** Fe more than doubled quarter-over-quarter (52 → 110 ppm, a 111% increase) after being nearly flat the prior quarter (45 → 52 ppm, 16%) — that acceleration is the signal, not the absolute 110 ppm value, because a developing high-speed-shaft bearing spall sheds wear metal at an accelerating rate long before the oil crosses an absolute critical line. The SCADA alert corroborates rather than contradicts this: the elevated amplitude sits specifically at the gear-mesh second harmonic on the high-speed shaft — the same location the oil sample implicates — rather than at a random frequency, which rules out simple sensor drift. Two independent signals agreeing on the same component is enough to justify a borescope now rather than waiting three months.

**Cost comparison (why acting now, not later, is the call):**

*Unplanned failure path (waiting for absolute threshold breach, then crane mobilization at failure):* crane mobilization ~$180,000 + gearbox replacement parts/labor ~$220,000 + lost generation during ~21-day outage: 2.5 MW × 35% capacity factor = 0.875 MW average × 24 h × 21 days = 441 MWh × $40/MWh = $17,640. **Total ≈ $417,640.**

*Scheduled intervention now (borescope confirms bearing spall on the high-speed shaft, bearing-only swap using a crane already mobilized for two other turbines that quarter):* parts/labor for bearing replacement ~$45,000 + shared crane mobilization allocation ~$15,000 + 2-day scheduled outage: 0.875 MW × 24 h × 2 days = 42 MWh × $40/MWh = $1,680. **Total ≈ $61,680.**

**Savings from acting on the trend now: $417,640 − $61,680 = $355,960.**

**Deliverable — escalation memo sent to the O&M asset manager (quoted):**

> **Turbine T-14, gearbox oil/vibration escalation — recommend borescope this week, not next quarterly cycle.**
> Fe trend: 45 → 52 → 110 ppm over three quarters (111% jump last quarter, still under the 150 ppm caution line on an absolute basis). SCADA vibration confirms an amplitude rise at the gear-mesh 2nd harmonic on the high-speed shaft, up ~40% over six weeks, load-normalized. Two independent signals point at the same bearing.
> **Recommendation:** borescope inspection of the high-speed-shaft bearing this week. If spall is confirmed, schedule a bearing-only swap using the crane already booked for T-09 and T-22 this quarter — est. $61.7k all-in versus an estimated $417.6k if this runs to an unplanned gearbox failure and crane mobilization.
> **If we wait for the next quarterly sample:** Fe trajectory suggests a realistic chance of crossing the 300 ppm critical line before then, at which point metal-to-metal wear on the gear teeth themselves, not just the bearing, becomes the likely finding — and the cost moves from bearing-only to full gearbox exchange.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — pre-climb go/no-go checklist, tower/blade bolt torque-tension procedure with worked calculation, oil-analysis and SCADA vibration interpretation tables, confined-space/rescue equipment checklist.
- [`references/red-flags.md`](references/red-flags.md) — smell tests: what each red flag usually means, the first question to ask, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- OSHA 29 CFR 1910.140 (Personal Fall Protection Systems, general industry) — anchorage strength requirements (5,000 lbf minimum per user for non-certified anchorage, or twice the maximum arrest force with a safety factor of at least 2 for certified/engineered systems).
- OSHA 29 CFR 1910.269 (Electric Power Generation, Transmission, and Distribution) — applies to most turbine O&M electrical work, including LOTO on converter/generator circuits.
- OSHA Suspension Trauma Fact Sheet (2011) — orthostatic-intolerance onset timeframe informing rescue-plan time-to-reach targets.
- ANSI/ASSP Z359.2-2017, *Minimum Requirements for a Comprehensive Managed Fall Protection Program* — rescue-plan and program-management provisions.
- Global Wind Organisation (GWO) Basic Safety Training standard — industry-recognized Working at Heights/rescue training baseline and refresher cadence.
- IEC 61400-24:2019, *Wind energy generation systems — Part 24: Lightning protection* — lightning-protection-system design and inspection basis.
- ISO 20816-21:2017 (formerly ISO 10816-21), *Mechanical vibration — Evaluation of machine vibration — Part 21: Horizontal axis wind turbines with gearbox* — vibration severity-zone basis for SCADA condition-monitoring alarms.
- VDI 2230 Part 1, *Systematic calculation of high duty bolted joints* — torque-tension calculation method used for tower-flange and blade-root bolt design and re-torque procedure.
- NREL Gearbox Reliability Collaborative (GRC) — J. Keller, Y. Guo, S. Sheng et al., published gearbox failure-mode and condition-monitoring research; wear-metal ppm caution/critical bands here are stated as industry-common practice derived from this body of work and OEM/oil-lab guidance, not a single universal spec — OEM-published thresholds override these when published.
- No direct wind-turbine-technician practitioner has reviewed this file yet — flag corrections or gaps via PR.
