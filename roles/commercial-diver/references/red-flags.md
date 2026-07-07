# Red flags

Smell tests a dive supervisor or lead diver catches before or during a dive, with what the signal usually means, the first question to ask, and the data to pull before anyone proceeds.

## 1. Primary gas remaining at or below the reserve threshold, task not finished

**Usually means:** the dive plan's gas math was tight from the start, or actual consumption ran above planned SAC rate due to harder-than-expected exertion or cold. Either way, the threshold exists precisely for this moment.

**First question:** "What's the exact reading right now, and is the diver already inside the reserve line or approaching it?"

**Data to pull:** current gas gauge reading vs. planned reserve line; elapsed bottom time vs. planned; diver's reported exertion level; whether any decompression obligation is already owed.

## 2. Bottom time creeping past the planned no-decompression limit "to finish the task"

**Usually means:** production pressure overriding the plan — a seized bolt, a slower cut, a longer weld pass — with someone deciding in the moment to just keep going rather than surface and replan.

**First question:** "Are we now inside a decompression obligation, and does the bailout gas plan already account for a stop?"

**Data to pull:** actual vs. planned bottom time and depth; current table's decompression requirement for the actual profile; bailout bottle sizing against that requirement (see `playbook.md` §1).

## 3. Diver reports joint pain, tingling, or unusual fatigue after surfacing

**Usually means:** decompression sickness (DCS) until ruled out — Type I (joint/skin) if mild and localized, Type II (neurological/pulmonary) if it involves numbness, weakness, confusion, or breathing difficulty. Delay in treatment is where permanent injury comes from.

**First question:** "Are we starting recompression now, or waiting for symptoms to confirm?" — the answer should be recompression now.

**Data to pull:** actual dive profile (depth/time) vs. table limits; time since surfacing; full symptom description; chamber availability and treatment table appropriate to the profile.

## 4. A load-bearing structural weld is specified or delivered as a wet weld

**Usually means:** either the engineering scope never distinguished weld class by load role, or cost/schedule pressure quietly downgraded a primary-member repair to the cheaper method without an engineering sign-off.

**First question:** "What AWS D3.6M class does this joint's load role actually require, and does a wet weld meet it?"

**Data to pull:** structural drawing showing the joint's load path (static vs. cyclic, primary vs. secondary); required weld class per the repair spec; welder's procedure qualification record for the method actually used.

## 5. Standby diver not fully suited while the working diver is in the water

**Usually means:** a shortcut taken to save prep time or personnel, on the assumption nothing will go wrong — exactly the assumption the standby-diver requirement exists to not need to rely on.

**First question:** "How long would it take the standby diver to actually be in the water right now?"

**Data to pull:** standby diver's current dress state; time-to-deploy estimate; whether this matches the site's written dive plan and OSHA/ADCI staffing requirement for the dive mode in use.

## 6. Dive supervisor is also the working diver on a complex task

**Usually means:** understaffing or a cost-cutting decision that removed the topside redundancy the role structure depends on — someone assumed the task was simple enough not to need dedicated topside attention, and that assumption is usually wrong precisely when it matters.

**First question:** "Who has full, undivided attention on the gas panel, comms, and abort authority right now?"

**Data to pull:** site staffing plan vs. actual roster present; task complexity assessment; whether this arrangement was approved in the dive plan or improvised on site.

## 7. Repetitive dive planned on a short surface interval without a recalculated limit

**Usually means:** the team is treating the second dive's no-decompression limit as fresh rather than reduced by residual nitrogen from the first dive — a common shortcut when the crew is behind schedule.

**First question:** "What's the adjusted allowable bottom time for this depth after the residual nitrogen carryover, not the fresh-dive number?"

**Data to pull:** dive 1's actual depth/time and resulting repetitive group; actual surface interval elapsed; current table's residual nitrogen time for that group/interval/depth combination (see `playbook.md` §2).

## 8. SCUBA mode used in conditions that no longer clear its limits

**Usually means:** gear was already staged and switching to surface-supplied felt like it would cost too much time, even though water temperature, current, visibility, or task scope (e.g., overhead/penetration) no longer meet the conditions SCUBA mode is restricted to.

**First question:** "Which specific condition — temperature, current, visibility, or task type — are we outside of right now?"

**Data to pull:** measured water temperature and current at time of dive; visibility estimate; task description (does it involve penetration or entanglement risk); site's written SCUBA-mode authorization criteria.

## 9. NDT thickness reading shows a step-change drop from the last survey

**Usually means:** either a genuine accelerated corrosion or erosion event (e.g., new flow-induced wear, coating failure) or a measurement/calibration error — both need ruling out before either scheduling repair or dismissing the reading.

**First question:** "Is this reading reproducible on a re-scan, and does the UT gauge's calibration check out against the reference block?"

**Data to pull:** current and prior survey grid readings at the same location; gauge calibration log; any known change in service conditions (flow rate, coating inspection history) since the last survey.

## 10. Umbilical tension or kink reported without an immediate stop-work

**Usually means:** the tender or diver noticed a problem but continued the task rather than pausing to clear it, often because the task felt close to done.

**First question:** "Is the umbilical clear right now, confirmed by the tender, before anyone continues?"

**Data to pull:** tender's real-time report on umbilical tension/slack; diver's own report on umbilical routing; whether the task was paused the moment the issue was noticed or continued through it.
