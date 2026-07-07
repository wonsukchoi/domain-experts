# Playbook

Filled checklists and decision tables this role runs on nearly every shift, with real thresholds and worked arithmetic — not descriptions of what a checklist should contain.

## 1. Transport-mode classification (decide before wheels roll)

| Signal | Classification | Driving mode | Authorization needed to change |
|---|---|---|---|
| Scheduled discharge, PCS on file, no acute symptoms | Non-emergency | Posted limits, normal right-of-way | Medical control or supervisor, logged |
| Repetitive dialysis/therapy transport, PCS on file | Non-emergency (repetitive) | Posted limits | Same as above; also subject to CMS RSNAT prior-authorization rules after the 3rd round trip in 10 days in applicable states |
| 911 dispatch, dispatcher-coded emergency | Emergency | Lights-and-siren authorized | N/A — already the assigned mode |
| Inter-facility transfer, sending physician flags acute deterioration risk | Emergency (if agency/state scope allows non-EMT crew) | Lights-and-siren, with medical control on standby | N/A — decided at dispatch |

**Rule:** the mode on the dispatch ticket is the mode you drive until a specific person (medical control, supervisor, or dispatch relaying either) authorizes a change and it's logged with a timestamp. A verbal request from family, facility staff, or your own read of the traffic is not authorization.

## 2. The "is it worth running hot" arithmetic

Before agreeing to any mid-route mode-upgrade request, run this math — it usually undercuts the request:

```
Time at posted mode   = distance ÷ avg_posted_speed × 60          (minutes)
Time at L&S mode       = distance ÷ avg_LS_speed × 60              (minutes)
Nominal time saved     = Time at posted mode − Time at L&S mode

Intersection tax       = (# controlled intersections on route) × ~12 sec
                          (cost of doing the complete-stop-and-clear correctly,
                          which L&S mode does NOT exempt you from)

Realistic time saved   = Nominal time saved − (Intersection tax ÷ 60)
```

**Worked example** (8.4-mile arterial/highway route, 6 controlled intersections):
- Posted mode: 8.4 ÷ 27 mph × 60 = 18.7 min
- L&S mode: 8.4 ÷ 34 mph × 60 = 14.8 min
- Nominal saved: 3.9 min
- Intersection tax: 6 × 12 sec = 72 sec = 1.2 min
- **Realistic time saved: 2.7 minutes**

**Threshold:** if realistic time saved is under ~5 minutes and there is no documented change in patient condition, the answer to a mode-upgrade request is no — solve the actual underlying problem (a late appointment, an anxious family member) directly instead.

## 3. Intersection-clearing sequence (every controlled intersection, every run, emergency or not)

1. **Cover the brake** on approach; begin scanning cross-traffic from at least 150-200 feet out, not at the stop line.
2. **Come to a complete stop** if the signal or sign requires it for opposing traffic — lights-and-siren changes your legal privilege to proceed, not your obligation to stop first.
3. **Visually clear lane 1**, confirming the nearest cross-traffic lane's vehicles have stopped or yielded — don't infer it from their brake lights alone; wait for the vehicle to actually be stationary or clearly yielding.
4. **Proceed into lane 1 only**, then repeat the visual-clear for lane 2, and each subsequent lane, one at a time — multi-lane intersections are cleared lane-by-lane, not as a single glance across all lanes.
5. **If any lane's traffic is not clearly yielding, stop again** before entering that lane, even mid-intersection.
6. **Do not accelerate to normal running speed until fully through the intersection and back into your lane of travel.**

**Rule:** the ~10-15 seconds this costs per intersection is non-negotiable and is already priced into the "is it worth running hot" arithmetic above — it's not a discretionary safety margin to skip when behind schedule.

## 4. Pre-trip and loading checklist (filled)

**Vehicle/equipment, before patient contact:**
- [ ] Cot weight rating checked against assigned patient's known/estimated weight (manual cots typically 500-650 lb rated; powered cots higher — confirm against the specific unit's placard)
- [ ] Cot locking mechanisms cycled and moving freely (not just "looks fine")
- [ ] Restraint straps present and undamaged (lap, chest, knee, shoulder as required)
- [ ] Backup lift-assist device (stair chair, transfer board) loaded if the pickup location has stairs or a narrow doorway per the dispatch notes

**At patient loading:**
- [ ] Weight/mobility estimated at ~125 lb or more of dependent lift → two-person lift or powered-cot assist, no exceptions
- [ ] Patient transferred and cot returned to transport height
- [ ] **Four-point lock check, visual, not by sound:** head-end locked / foot-end locked / both side rails locked / IV pole (if present) secured in its bracket
- [ ] Restraints applied and checked snug, not just draped
- [ ] Cot secured to the vehicle floor mount, mount lever confirmed engaged

**Rule:** the four-point check happens even when the cot "clicked" on the way up — the click confirms the latch engaged, not that it's carrying load correctly under transit vibration.

## 5. Mid-route status-change protocol

If the patient's condition visibly changes (new pain, altered mental status, respiratory distress) or a facility/family member requests a mode upgrade for a non-clinical reason:

1. State the observation or the request over the radio to dispatch or medical control, factually, without editorializing.
2. Ask the direct question: "Does this warrant a mode change to lights-and-siren?"
3. Wait for an explicit yes/no and a name/unit attached to the authorization.
4. If authorized, note the time, who authorized it, and the reason in the run report before or immediately after the change — not from memory at end of shift.
5. If not authorized, and the requester is family or facility staff, address the underlying problem directly (call ahead, ask the receiving party to adjust their schedule) rather than relitigating the driving decision with them.
