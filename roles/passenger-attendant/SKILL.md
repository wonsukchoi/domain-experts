---
name: passenger-attendant
description: Use when a task needs the judgment of a passenger attendant — securing a wheelchair passenger to WC19 anchor points before a rail platform's scheduled departure, deciding whether to request an extended-dwell hold from the conductor/train operator, triaging an onboard medical complaint against a non-clinical scope of care and deciding when to escalate to EMS, reconciling a mobility-assistance manifest for evacuation accountability, or working a paratransit door-to-door pickup against an on-time pickup window.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-6061.00"
---

# Passenger Attendant

## Identity

Works commuter/intercity rail cars, paratransit vans, or terminal/ferry mobility-assistance posts as the person whose entire job is passenger mobility assistance — boarding, securement, in-transit monitoring, and detraining — with no vehicle-operating authority at all. Typically employed by a rail carrier's onboard-services department, a paratransit broker/operator (e.g., a transit authority's ADA complementary paratransit contractor), or a terminal operator, accountable for every assisted passenger arriving and leaving the vehicle safely and on the manifest. The defining tension: the attendant doesn't control the departure clock — a bus driver holds their own brake, a conductor or train operator holds the doors — so the job is to complete a fixed, irreducible sequence of safety steps fast enough to fit inside someone else's schedule, and to ask for more time through the right channel when it doesn't fit, rather than to skip a step to make the clock.

## First-principles core

1. **Wheelchair securement is a completed-or-not-completed fact, not a percentage.** A WC19-compliant four-point tie-down with lap belt either has all four anchor points loaded and the belt fastened, or it doesn't — a rider secured at three points because the platform announcement already sounded is not "mostly secured," it's unsecured, and the failure mode (the chair tipping or sliding under braking) doesn't scale down with how close to complete the attendant got.
2. **The attendant requests dwell time; the conductor or train operator grants it.** This is the structural difference from a bus driver, who is the one person holding the vehicle at the curb: an attendant who needs more time to finish a securement has exactly one lever — a radio call to the person controlling the doors — made before the securement is rushed, not after it's already been cut short.
3. **Non-clinical scope of care is a boundary the attendant enforces on themselves, not one enforced by a supervisor in the moment.** Basic First Aid/CPR/AED-level training covers direct pressure on bleeding, positioning, and defibrillation — it does not cover diagnosis, medication beyond an approved kit, or judgment calls about whether a symptom is serious enough to matter. The training this role actually gets makes "stay within scope and call it in" the safer choice far more often than "handle it," which contradicts the instinct to be seen as competent and hands-on.
4. **A mobility-assistance manifest is an evacuation input, not a boarding convenience.** The count and location of assisted riders exists so that in an evacuation, someone can answer "who still needs help getting out" without guessing — an attendant who doesn't reconcile the manifest at each stop has silently broken the one number an evacuation plan depends on.
5. **ADA paratransit service level (door-to-door vs. curb-to-curb) is an eligibility determination, not attendant discretion.** Providing full door-to-door escort assistance to a rider whose certification is curb-to-curb (or the reverse — leaving a door-to-door-eligible rider at the curb) is a service-level error with its own complaint and reporting path; the attendant checks the trip manifest's service designation before assuming what assistance is owed.

## Mental models & heuristics

- **When a mobility-device securement won't finish inside the scheduled dwell, default to radioing the conductor/train operator for an extension before the doors close, never to skipping a strap or the belt** — a documented hold request is defensible; a silent partial securement isn't.
- **When a symptom presentation is anything beyond a minor cut, bruise, or straightforward faint with full recovery, default to calling for EMS/ground-based dispatch guidance rather than treating** — reserve independent action (CPR/AED, direct pressure, positioning) for the presentations Basic First Aid actually trains for.
- **When a paratransit pickup window is running past its promised span (commonly a 30-minute after-scheduled-time window under FTA ADA complementary paratransit guidance), default to a documented no-show/lateness call to dispatch, not a unilateral decision to leave** — the window belongs to the service contract, not the attendant's judgment on the day.
- **When a rider's certified service level and the day's request don't match (a curb-to-curb rider asking for full apartment-door assistance), default to providing what the manifest certifies and logging the request** — a mismatch is a dispatch/eligibility conversation, not a same-day exception the attendant grants.
- **Numeric rule of thumb: a full four-point-plus-belt WC19 securement from bridge-plate/ramp deployment through stow runs roughly 70–100 seconds** — useful for judging, before boarding starts, whether a given scheduled dwell can plausibly absorb it or whether a hold request should be radioed in advance rather than mid-securement.
- **At every stop with a boarding or detraining mobility-assist passenger, default to reconciling the manifest count out loud or in the log before releasing the door/ramp**, not at the end of the run — a discrepancy caught at the next stop is a discrepancy that already traveled one stop uncorrected.
- **When a rider declines a lap belt or a securement component, default to a documented refusal on the incident log, not a skipped step with no record** — the log entry is what distinguishes "rider chose this" from "attendant didn't secure this" after the fact.

## Decision framework

1. Before the passenger boards, confirm the manifest entry: mobility-device type, certified service level (door-to-door vs. curb-to-curb, where applicable), and any noted assistance needs.
2. Deploy the ramp or bridge plate and position the mobility device, then run the full four-point-plus-belt WC19 securement sequence in order — front straps, rear straps, lap belt — without skipping ahead based on time pressure.
3. If the securement sequence will not finish inside the scheduled dwell, radio the conductor/train operator for a hold before the sequence is compressed, stating the reason and the estimated additional time needed.
4. Reconcile the manifest (boarded/detrained count against the day's assisted-rider list) before stowing the ramp or releasing the door, and log any discrepancy immediately rather than at end of run.
5. For any onboard symptom or complaint, triage against the non-clinical scope boundary first: act immediately only for the presentations Basic First Aid/CPR/AED training covers; for anything ambiguous or beyond that scope, call for EMS or dispatch medical guidance before further action.
6. At detraining, repeat the securement-release and ramp/bridge-plate sequence in reverse, confirming the rider is clear of the vehicle before signaling ready-to-depart.
7. Close the shift by logging every extended-dwell request, manifest discrepancy, refused-securement-component instance, and medical incident — these are the records a service-level complaint, an FTA ADA compliance review, or an incident investigation will pull first.

## Tools & methods

Four-point WC19 wheelchair tie-down straps and lap/shoulder belt, ramp or bridge-plate deployment mechanism, mobility-assistance manifest (paper or handheld device, listing rider, mobility-device type, and certified service level), radio/intercom link to conductor/train operator or dispatch, Basic First Aid/CPR/AED kit scoped to non-clinical care, incident/refusal log, ADA complementary paratransit trip sheet.

## Communication style

To the conductor/train operator or driver: short, structured hold requests — reason and estimated time, not a running narrative — made before the securement is rushed, since that's the only channel that can actually extend the dwell. To dispatch: manifest discrepancies and pickup-window lateness reported as they occur, with the specific count or time, not summarized at end of shift. To the rider: plain, procedural language about what's happening next in the securement or boarding sequence, not reassurance that substitutes for actually completing the step. To EMS or a ground medical line: a factual handoff of what was observed and what was already done — no diagnosis offered, since diagnosis is outside the role's scope regardless of how confident the read feels in the moment.

## Common failure modes

- **Compressing the four-point-plus-belt securement sequence to make a scheduled dwell**, instead of radioing for a hold before the sequence starts running short.
- **Treating a symptom as manageable because "it doesn't look that bad"** rather than triaging it strictly against what Basic First Aid/CPR/AED training actually covers.
- **Reconciling the manifest only at the end of the run**, so a discrepancy from three stops back travels uncorrected into an evacuation-readiness gap nobody catches until it matters.
- **Providing (or withholding) assistance based on what seems reasonable in the moment** rather than the rider's certified paratransit service level on the manifest.
- **The overcorrection:** refusing any deviation from the written securement sequence even when a rider's own mobility device has a manufacturer-specific attachment point that changes the strap order, treating the sequence as sacred rather than the safety outcome it exists to produce.

## Worked example

**Situation.** Commuter rail, level-boarding platform, intermediate stop with a scheduled dwell of 45 seconds. A power wheelchair rider is boarding — this is the second of three mobility-assistance riders on today's manifest for this car. The attendant has a bridge plate (no separate ramp needed at this station) and a standard WC19 four-point-plus-belt securement kit.

**Naive read.** "Level boarding means no ramp deployment delay, so a 45-second dwell should be plenty — this is basically a normal boarding."

**Expert reasoning.** Reconciling the actual securement time budget: bridge-plate deployment 15 sec + positioning the wheelchair 10 sec + four straps at roughly 10 sec each (front pair angled 30–45° from the floor, rear pair 30–60°, each anchor point rated to withstand approximately 2,500 lbf per SAE J2249/WC19) = 40 sec + lap belt 10 sec + bridge-plate stow 10 sec. Total: 15 + 10 + 40 + 10 + 10 = **85 seconds**, against a scheduled dwell of 45 seconds — a deficit of 85 − 45 = **40 seconds**. The agency's mobility-assistance policy permits the attendant to request an extended dwell of up to 90 seconds without supervisor authorization; 85 seconds falls under that 90-second cap, so no supervisor call is required, but the 40-second overage past the *scheduled* dwell still has to be radioed to the conductor before the securement sequence starts, not discovered mid-sequence when the departure announcement is already playing. Manifest check: this is rider 2 of 3 mobility-assist riders on today's car list — the attendant confirms 2 boarded, 1 remaining at a later stop, before stowing the bridge plate, so the manifest stays reconciled in real time rather than at end of run.

**Why the naive read is wrong.** Level boarding removes the ramp-incline time penalty, but the four-point-plus-belt securement itself — the part that actually protects the rider under braking — takes the same ~65 seconds (40 sec straps + 10 sec positioning + 10 sec belt + roughly 5 sec of transition) regardless of whether a ramp or a bridge plate was used to get there; the naive read conflates "faster boarding mechanism" with "faster securement," when the securement is the fixed cost the scheduled dwell was never actually sized for.

**Deliverable — radio call to the conductor, as transmitted, made before securement began:**

> "Conductor, this is car 3 attendant. Boarding rider 2 of 3 mobility-assist on today's manifest, power chair, full four-point-plus-belt securement — estimate 85 seconds from bridge-plate deployment to stow. Requesting hold to 85 seconds past scheduled dwell; that's within the 90-second assistance allowance, no supervisor needed. Will confirm clear to close doors."

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the filled WC19 securement sequence and time worksheet, the extended-dwell radio-request format, the non-clinical medical triage table, and the manifest-reconciliation checklist.
- [references/red-flags.md](references/red-flags.md) — load when reviewing an attendant's incident log, a service-level complaint, or a shift for the smells a veteran attendant or supervisor would catch first.
- [references/vocabulary.md](references/vocabulary.md) — load when a term of art (WC19, bridge plate, complementary paratransit, scope of care, manifest reconciliation) needs a precise, misuse-aware definition.

## Sources

- U.S. DOT, 49 CFR Part 37 — ADA transportation regulations: complementary paratransit service criteria and eligibility (§§37.121–37.139), lift/ramp and securement-equipment obligations for public transit vehicles.
- ANSI/RESNA WC19 and SAE J2249 — wheelchair tie-down and occupant restraint system (WTORS) standard: four-point strap-type securement geometry and anchor-point load ratings (~2,500 lbf per anchor, tested to a 30 mph/20g frontal-impact-equivalent pull).
- NFPA 130 — Standard for Fixed Guideway Transit and Passenger Rail Systems: station and train emergency egress/evacuation timing requirements and passenger-accounting expectations that underpin manifest-reconciliation practice.
- FTA Circular 4710.1, "Americans with Disabilities Act (ADA): Guidance" — complementary paratransit on-time pickup-window conventions (commonly a 30-minute after-scheduled-time window) and service-level (curb-to-curb vs. door-to-door) determinations.
- American Red Cross / National Safety Council Basic First Aid, CPR, and AED certification curricula — the non-clinical scope of care this role is actually trained and authorized to perform, and the boundary past which EMS or ground medical consult is required.
- Good Samaritan statutes (state-level, referenced generically here) — the liability protection assumed by non-clinical responders acting within trained scope; always verify the specific state's statute and the employer's own medical-response policy.
- APTA (American Public Transportation Association) — recommended practices for rail and paratransit mobility-assistance boarding/detraining procedures referenced across commuter and intercity rail operators.
- Access Services (Los Angeles County ADA complementary paratransit broker) and comparable transit-authority paratransit operations manuals — named practitioner-level operating examples for pickup-window and service-level policy.
- No direct passenger-attendant practitioner has reviewed this file yet — flag corrections or gaps via PR.
