# Playbook

Filled procedures a supervisor actually runs at shift start and mid-shift, with real numbers plugged in. Copy the structure, swap in the floor's own roster and throughput numbers.

## 1. Fleet-mix capacity worksheet

**Formula:**

```
Capacity per equipment class = certified-available operators × measured throughput rate (moves/hr) × shift hours
Total shift capacity          = sum of capacity across all equipment classes in use
Utilization                   = task target ÷ total shift capacity
```

**Worked table — 800-pallet target, 8-hour shift, after pulling two flagged operators:**

| Equipment | Nominal operators | Available (cert-current) | Rate (moves/hr) | Capacity | Notes |
|---|---|---|---|---|---|
| Forklift | 6 | 4 | 14 | 448 | 2 pulled: 1 lapsed cert, 1 open trigger event |
| Reach truck | 3 | 2 | 10 | 160 | 1 called out (unrelated to compliance) |
| Pallet jack | 4 | 4 | 9 | 288 | full roster available |
| **Total** | **13** | **10** | | **896** | |

Utilization = 800 ÷ 896 = **89.3%** — above the 85% no-slack threshold (see §3); flag before committing to the full target.

**Field procedure:**

1. Pull the day's scheduled roster against the certification-currency check (§2) before assigning anything.
2. For each equipment class, multiply available operators × that class's measured throughput rate (from the WMS pick-rate report, not a remembered number) × shift hours.
3. Sum across classes for total shift capacity.
4. Divide the task target by total capacity to get utilization; route the result into the utilization check (§3) before finalizing the assignment.
5. If a class is short, calculate the throughput cost of substituting a different class for that task type before assigning it — don't assume one machine is as good as another for the same task.

## 2. Certification-currency roster check

Run at the start of every shift, before the fleet-mix worksheet.

| Check | Trigger | Action |
|---|---|---|
| 3-year OSHA evaluation date | Date has passed, no completed renewal logged | Pull from all equipment classes until renewal is logged — not just the class they're normally assigned |
| Incident or near-miss involving this operator | Any tip, near-tip, contact, or reported near-miss, regardless of fault | Pull until a post-incident evaluation is logged, regardless of days remaining on the standing card |
| New truck-class assignment | Operator is being put on equipment they haven't run before at this site | Truck-class-specific evaluation required before independent operation on that class, even with a current general certification |
| Changed workplace hazard | New racking layout, new surface, new traffic pattern since last evaluation on this route | Refresher on the changed condition before resuming that specific route |

**Worked example:** Operator Q — general cert current, but 3-year evaluation lapsed 3 days ago pending renewal → pull. Operator R — general cert current, but open near-miss from 2 shifts ago with no logged evaluation → pull from every class, not only the forklift he was on when the near-miss happened. Recompute available capacity per §1 after removing both.

## 3. Utilization threshold check

| Utilization band | Reading | Action |
|---|---|---|
| Below ~40% | Idle cost — equipment and labor paid without matching output | Reallocate the idle class to another task, or consolidate the shift's equipment mix |
| ~40%–85% | Working range with breakdown/PM slack intact | No action required beyond normal monitoring |
| Above ~85% | No slack — one breakdown or PM-due unit directly costs the shift's target | Add a unit, trim the target, or stagger start times before committing |

**Worked example:** 800-pallet target against 896-capacity roster = 89.3% → above threshold. To get back under 85%, the target has to drop to at most 896 × 0.85 = 761.6, so trim to **760 pallets this shift** (760 ÷ 896 = 84.8%, back under threshold) and carry the remaining **40 pallets** to next shift's opening task. Bringing a pulled operator back mid-shift was considered but not viable for Q, whose renewal was still pending.

## 4. Near-miss investigation procedure

1. **Capture the report the same shift it happens** — equipment class, operator, location, what almost happened, what stopped it from becoming an incident.
2. **Classify severity potential**, not just outcome — a near-miss that could have been a fatality (e.g., pedestrian in a blind corner) gets the same investigation depth as an actual minor injury, regardless of the fact that no one was hurt this time.
3. **Pull the operator from that equipment class** (see §2) pending evaluation — the report itself is the trigger event, independent of any standing certification.
4. **Log against the site's own running near-miss-to-incident ratio**, tracked over a rolling 12 months, rather than assuming it should match the historical Heinrich (1:29:300) or Bird (1:10:30:600) study populations — those studies establish *why* the reporting matters, not this site's exact numbers.
5. **Close the loop**: what changed as a result (traffic marking, equipment substitution, refresher training) — a near-miss log with no corrective actions attached is a filing exercise, not a safety program.

## 5. Mixed-equipment traffic coordination

| Situation | Coordination rule | Fallback if uncertain |
|---|---|---|
| Forklift and reach truck sharing a cross-aisle | Forklift yields at the cross-aisle if the reach truck is already committed to the narrow-aisle approach (harder to reverse out of) | Both stop, radio/hand-signal confirmation before either proceeds |
| Pallet jack and forklift sharing a dock staging lane | Pallet jack (lower speed, shorter stopping distance) holds at the lane entrance until the forklift clears | Supervisor designates a one-at-a-time lane rule if congestion recurs |
| Pedestrian crew working a pick face while any powered equipment operates in the same aisle | Powered equipment reduces to walking pace and sounds horn at every approach, regardless of route familiarity | Escort/spotter assigned if visibility is blocked by racking or a loaded truck |
| Two equipment classes assigned overlapping routes for the same shift | Supervisor pre-assigns priority order (typically: reach truck > forklift > pallet jack, since narrow-aisle trucks have the least room to maneuver around a conflict) | Stagger start times so routes don't overlap during peak volume |
