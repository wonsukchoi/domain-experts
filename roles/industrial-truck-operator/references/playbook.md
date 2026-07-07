# Playbook

Filled procedures an operator or supervisor actually runs, with real numbers plugged in. Copy the structure, swap in the truck's own data-plate numbers.

## 1. Load-center / moment calculation worksheet

Every truck's data plate states rated capacity **at a reference load center** (commonly 24 in for standard pallet loads on Class I–V counterbalanced trucks). The plate also implies a fixed distance from the front axle to the fork face — call it **D** — which is a property of that specific truck, found on its spec sheet or nameplate.

**Formula:**

```
Rated moment (M)        = Rated capacity × (Reference load center + D)
De-rated capacity (LC2) = M ÷ (Actual load center + D)
```

**Worked table — three trucks, same 34-inch-load-center load:**

| Truck | Rated capacity | Ref. load center | D (axle-to-fork) | Rated moment (M) | De-rated capacity @ 34" LC | Cleared for 4,200 lb load? |
|---|---|---|---|---|---|---|
| Unit 5-ton | 5,000 lb | 24 in | 20 in | 220,000 in-lb | 220,000 ÷ 54 = 4,074 lb | No — 126 lb short |
| Unit 6-ton | 6,000 lb | 24 in | 22 in | 276,000 in-lb | 276,000 ÷ 56 = 4,928 lb | Yes — 728 lb margin |
| Unit 3-ton | 3,000 lb | 24 in | 18 in | 126,000 in-lb | 126,000 ÷ 52 = 2,423 lb | No — 1,777 lb short |

**Field procedure:**

1. Measure or estimate the load's center of gravity from the fork face (long/odd loads: measure to the visual midpoint of mass, not the pallet's geometric center).
2. Pull rated capacity, reference load center, and D from the truck's data plate / spec sheet.
3. Compute M, then de-rated capacity at the actual load center.
4. If de-rated capacity < actual load weight, do not lift — swap trucks, reposition the load closer to the fork face, or split the load.
5. Re-run the calculation for any attachment in place (clamp, side-shifter, boom) using the attachment's own plate, which restates capacity at its own reference point and typically pushes the load center further out again.

## 2. Rack/beam capacity verification

1. Locate the level's RMI/ANSI MH16.1 placard — it states **capacity per beam level** and sometimes **per bay** (the sum across levels in one bay/upright pair).
2. Sum current staged weight on that level (ask the WMS/inventory system or check tags, don't estimate by eye) plus the incoming load.
3. Compare to the placard. If within 10% of the limit, treat it as full — flag for supervisor before adding more, since scale/estimate error eats that margin fast.
4. If no placard is visible or legible, treat the level as **do not load** until facilities posts one — this is a stop condition, not a judgment call.

**Example:** Level rated 5,500 lb combined. Currently staged: 1,150 lb. Incoming coil pallet: 4,200 lb load + 50 lb pallet = 4,250 lb. Total after placement: 5,400 lb — 100 lb of headroom, under the 10%-margin (550 lb) threshold, so flagged: no further staging on that span without relieving weight first.

## 3. Pedestrian-traffic protocol at blind corners and cross-aisles

| Situation | Action | Fallback if uncertain |
|---|---|---|
| Approaching marked blind corner or dock doorway | Horn (two short blasts), reduce to walking pace (~3 mph or site-posted limit) | Full stop, wait for mirror/camera confirmation of clear cross-aisle |
| Convex mirror shows a pedestrian in the cross-aisle | Stop and wait for pedestrian right-of-way per site signage | If mirror view is obstructed or missing, treat as occupied |
| Operating in a mixed pedestrian-forklift zone with no marked lanes | Escort/spotter for any load blocking forward visibility | Request facilities add floor marking before continuing routine moves through that zone |
| Backing with a load that blocks rear visibility | Spotter or camera confirmation before reversing | Sound reverse alarm and pause at first movement, listening/looking for a stop signal |

## 4. Post-incident / trigger-event recertification decision tree

1. **Did a tip, near-tip, contact with a rack/pedestrian, or unsafe-operation observation occur?**
   - Yes → pull operator from that truck immediately; do not resume on the calendar-valid certification alone.
   - No → continue to next check.
2. **Is the operator being assigned a truck type/class they haven't operated before** (e.g., reach truck operator assigned to a counterbalanced sit-down)?
   - Yes → truck-specific evaluation required before independent operation, per OSHA 1910.178(l), even with a current general certification.
3. **Has the workplace hazard changed** (new racking layout, new surface, new pedestrian traffic pattern) since the operator's last evaluation on this route?
   - Yes → refresher covering the changed condition before resuming that specific route.
4. **Is it simply the 3-year mark since the last evaluation?**
   - Yes → standard recertification evaluation, no incident required — this is the calendar floor, not a substitute for the trigger-event checks above.

## 5. Ramp/grade orientation quick reference

| Condition | Loaded truck orientation | Empty truck orientation |
|---|---|---|
| Traveling up a grade | Load (forks) pointed upgrade | Forks pointed downgrade |
| Traveling down a grade | Load (forks) pointed upgrade (travel in reverse) | Forks pointed downgrade |

Never turn on a grade above the manufacturer's posted maximum grade rating; travel straight up or down, tilt mast back, keep load low.
