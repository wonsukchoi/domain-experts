# Underground Loader (LHD) Operator — Playbook

Filled reference sequences: round-tonnage/cycle-time calculation, misfire response, scaling sign-off and ride-on/remote decision, and DPM exposure check.

## 1. Round-tonnage and cycle-time calculation

Use this to determine whether a shift's tonnage target is achievable, and whether the bottleneck (if any) is cycle time, ore-pass capacity, or oversize frequency.

| Input | Typical range | Source/note |
|---|---|---|
| In-situ ore density | 150–180 lb/cf (base-metal sulfide ore) | Hartman & Mutmansky; confirm against site-specific assay/geotech data — varies by ore type and gangue content |
| Swell factor on breakage | 30–50% | Hustrulid & Bullock; confirm against site muck-pile survey if available |
| LHD bucket fill factor | 80–95% (lower on blocky ore, higher on fines) | stated illustrative range; confirm against this machine's actual duty cycle |
| Ride-on tram speed, loaded / empty | ~2.5–3.5 mph loaded / ~3.5–5 mph empty | OEM spec dependent; confirm against the specific LHD model |
| Remote-control tram speed, loaded / empty | roughly 40–60% of ride-on speed | stated illustrative range reflecting reduced-visibility joystick tramming; confirm against site remote-control policy |

**Working steps:**

1. Calculate round volume: drift width (ft) × height (ft) × blasted pull (ft, from the shot report — not the drilled depth).
2. Convert to tons: volume (cf) × in-situ density (ton/cf, from lb/cf ÷ 2,000).
3. Calculate loose bulk density: (round tons × 2,000) ÷ (round volume × (1 + swell factor)).
4. Calculate tons per bucket: bucket rated capacity (cf) × fill factor × loose bulk density (lb/cf) ÷ 2,000.
5. Divide round tons by tons per bucket, rounding up, to get buckets required.
6. Calculate cycle time for the applicable mode (ride-on or remote): load + tram loaded (distance ÷ speed) + dump + tram empty (distance ÷ speed).
7. Multiply buckets required × cycle time to get total mucking time for that mode; compare against effective shift time remaining (shift minutes × utilization factor, typically 75–85%).
8. If total mucking time exceeds effective time remaining under either mode, the shortfall is a cycle-time problem — flag for a second machine or a shorter tram route. If it fits comfortably, a "no time for it" call is usually wrong; see the worked figures in SKILL.md's Worked example for a full derivation.
9. If cycle time isn't the constraint but tonnage is still short, check the ore pass/drawpoint fill state (Step 5 below) and oversize count before concluding cycle time is the cause.

## 2. Misfire response sequence (30 CFR Part 57, Subpart J)

| Indicator in the muck pile | Required action |
|---|---|
| Unexplained gap between drilled and fired hole count on the shot report | Treat the heading as suspect before mucking begins; verify against the blaster's log before entry |
| Visible explosive material, detonator wire, or unusual chemical odor in the pile | Stop mucking that location immediately |
| Bucket contact produces a suspected detonation-capable object (cartridge, cap) | Stop the machine, back out, notify the shift boss and a qualified/certified person by radio immediately |

**Working steps:**

1. Before mucking any freshly blasted round, cross-check the shot report's drilled-hole count against the fired/detonated count logged by the blaster.
2. If the counts don't reconcile, or any suspected missed-hole indicator is present, do not muck — barricade the heading entrance and notify the shift boss.
3. Only a qualified/certified person may approach or handle a confirmed or suspected misfire, per the mine's approved misfire procedure — the LHD operator's job is to stop, barricade, and report, not to investigate further.
4. Log the location, indicator observed, and time in the shift record immediately.
5. Do not resume mucking that heading until a qualified person has cleared it and the clearance is documented.

## 3. Scaling sign-off and ride-on/remote decision

1. Before trailing the machine to a freshly blasted heading, check the ground control log for a scaling/support sign-off entry specific to that heading and shift.
2. If the sign-off shows full scaling and support complete: ride-on operation is permitted.
3. If the sign-off shows partial or no scaling/support: remote-control tramming only, positioned outside the unsupported span — regardless of how the back looks from the drift mouth.
4. Recalculate cycle time and total mucking time for remote mode (Section 1, Steps 6–7) before assuming a schedule conflict — the time cost of remote is frequently smaller than production pressure assumes.
5. If remote-mode total time genuinely exceeds the effective shift time remaining, escalate to the shift boss for a second machine, a partial-round handoff to the next shift, or an expedited scaling crew — not a ride-on exception.
6. Once scaling/support is completed and signed off mid-shift, re-verify the sign-off entry (don't rely on a verbal "it's done") before switching to ride-on.

## 4. DPM (diesel particulate matter) exposure check

1. Confirm the current DPM sampling source (personal sampler vs. area monitor) and whether today's reading reflects a full shift or a partial one before treating a number as representative.
2. If a reading trends toward or exceeds 160 µg/m³ total carbon (8-hour TWA, per 30 CFR §57.5060), identify the likely source before assuming a respirator or PPE fix: idle time at a dead-end face, ventilation short-circuiting, or a degraded diesel exhaust filter are the three most common causes.
3. Reduce unnecessary idle time at the face (shutting down rather than idling during extended waits) as the first, lowest-cost intervention while the ventilation or filter issue is investigated.
4. Log the reading, suspected cause, and any corrective action taken in the shift record; escalate to the ventilation engineer if the cause is airflow-related rather than operator-controllable.
5. Do not resume extended dead-end idling in that heading until the corrective action is confirmed effective by a follow-up reading.
