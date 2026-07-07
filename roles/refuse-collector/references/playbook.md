# Playbook

Filled decision tables and step sequences for the situations that come up every shift: backing, contamination screening, jam clearance, and route-time reconciliation.

## Backing protocol decision table

| Condition at the stop | Required action | Fallback if condition changes mid-maneuver |
|---|---|---|
| Straight pull-through, no parked vehicles, no pedestrians within 50 ft, documented on route sheet | Proceed with backup alarm/camera active, no full stop required | If anyone enters the zone, stop immediately and re-classify |
| Cul-de-sac or dead-end, sightlines partially blocked by parked cars | Full stop, spotter assigned with hand signals; if no spotter, GOAL before reversing | Re-GOAL if >10-15 sec pass or a vehicle/pedestrian appears |
| School zone, playground frontage, or any stop flagged "persistent hazard" in the route-hazard log | Full stop, spotter mandatory regardless of visible traffic, horn tap sequence before reversing | If spotter is unavailable, do not back — radio dispatch for route-sequence workaround |
| Backup camera/alarm reported inoperative | Truck should not be dispatched without a compensating spotter assignment for every backing stop on the route | If discovered mid-route, radio dispatch immediately; do not continue backing without a spotter for remaining stops |
| Construction, delivery, or utility vehicle blocking the normal pull-through | Full stop, spot-back with spotter, log the obstruction and estimated delay | If obstruction recurs on a later pass, escalate to a standing route-hazard entry |

**Spotter hand signal set (standardized, non-verbal):**
- Raised flat palm, arm extended = stop
- Both arms waving inward, repeated = continue straight back
- One arm angled left/right = angle that direction
- Crossed forearms overhead = full stop, hazard, do not move

## Contamination screening decision table

| Container contents observed | Action | Basis |
|---|---|---|
| Clean single-stream recyclables, no visible contamination | Collect normally | Standard |
| One isolated minor item (single paper cup, small food residue on cardboard) | Collect | Below the threshold that meaningfully changes load contamination |
| Bagged household trash mixed with recyclables | Tag ("oops tag" — check "bagged trash" box), leave, log address | Bagged material is the most common single trigger for MRF rejection; opening bags at the curb isn't standard practice, so it defaults to tag-and-leave |
| Food waste, liquids, or soiled containers (grease, dairy) in volume | Tag (check "food/liquid contamination" box), leave, log address | Organic contamination degrades the whole batch's marketability, not just the one container |
| Hazardous or non-recyclable large items (propane tank, garden hose, electronics, batteries) | Do not collect under any circumstance; tag with hazard-specific note, escalate to route supervisor same shift | Some of these are outright unsafe to run through a packer, independent of contamination economics |
| Repeated contamination from the same address (3rd occurrence logged in the tag system) | Tag, leave, and flag address for a targeted education mailer rather than continued silent rejection | Escalation path exists precisely because per-stop tagging alone doesn't change habitual behavior |

**Why the threshold matters:** many MRF contracts price contamination in bands — roughly clean-to-modest contamination processes at the standard rebate rate, a mid-range band (commonly cited around 15-25% by weight) triggers a per-load surcharge, and above that band the whole load is rejected and redirected to landfill [heuristic bands — verify against the specific MRF contract in force]. A collector's per-container screening decision is the only point in the chain where that band gets managed before the truck is already full.

## Hopper/packer jam-clearing sequence (lockout/tagout)

1. Stop the vehicle, set the parking brake, and disengage the PTO (power take-off) controlling the packer mechanism.
2. Shut down the engine (not just the packer cycle) if the jam requires reaching into or near the hopper or compaction chamber.
3. Apply lockout device to the designated energy-isolating point per the vehicle's ANSI Z245.1-compliant lockout procedure; attach a tag identifying who locked it out and why.
4. Verify zero energy state — attempt to cycle the packer control from the operator position; it must not respond.
5. Clear the jam manually, using the tool specified for that vehicle (never bare hands into a pinch point).
6. Remove tools and any loose material from the hopper/chamber before removing lockout.
7. Remove lockout only from the operator position, restart, and run one empty cycle before resuming collection at that stop.

**Fallback:** if the designated lockout point is inaccessible or the tag/lock kit is missing from the vehicle, do not clear the jam — radio dispatch for a service truck. There is no time-pressure exception to this sequence.

## Route time-per-stop benchmarks

| Collection method | Typical budgeted time/stop | What drives variance |
|---|---|---|
| ASL (automated side loader), standard residential cart | ~15-20 sec | Curb clearance/container spacing, arm cycle time, need for repositioning |
| Rear-loader, manual residential collection | ~30-45 sec | Walking distance from truck to container, number of containers per stop, lifting |
| Front-loader, commercial dumpster route | Several minutes/stop, but far fewer stops/day | Dumpster fill level, access/gate constraints, compaction cycles per stop |

**Reconciliation template (end of shift):**

```
Route: ____   Stops budgeted: ____   Stops completed: ____
Time budgeted: ____ min   Time actual: ____ min   Variance: ____ min

Delay events (each >5 min):
  Location / Cause / Duration / Spotter used? (Y/N)

Contamination tags issued: ____   Addresses flagged for repeat: ____
Near-misses logged: ____ (same-shift, per event above)

Stops running >2x per-stop benchmark: ____ (flag for route-design review, not driver review)
```

Use this to separate a one-time delay (weather, an obstruction, an equipment fault) from a systemic route-density problem — the first gets a shift-extension or re-sequencing decision, the second gets escalated to route design.
