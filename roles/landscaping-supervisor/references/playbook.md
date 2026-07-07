# Playbook

Filled worksheets and thresholds for the three recurring supervisory acts: estimating/re-costing a route, making the weather go/no-go call, and staffing licensed-applicator coverage.

## Production-rate table (starting estimates, NALP-style labor units)

Adjust every figure for actual walked conditions (obstacle density, slope, bed edging, wet/dry) before locking a route — these are the estimator's baseline, not the crew's target.

| Task | Equipment | Base rate | Notes |
|---|---|---|---|
| Mow, open turf | 60" zero-turn | ~1 acre/hr | Flat, obstacle-light; drops to ~0.6–0.7 acre/hr with heavy bed/tree obstacles |
| Mow, open turf | 21" push/self-propelled | ~0.15–0.2 acre/hr (~7,000–8,700 sq ft/hr) | Used for gated backyards, small lots, trim-adjacent areas |
| String trim | Handheld | ~4,000–6,000 linear ft/hr of edge | Heavier around dense bed edging or fence lines |
| Blow/cleanup | Backpack blower | ~0.25–0.4 acre/hr equivalent | Scales with hardscape area (driveways, walks) more than lot size |
| Residential ¼-acre "full service" (mow+trim+blow) | 3-person crew, 60" ZTR + trimmer + blower | ~10–14 min/stop | This is the number that should reconcile against sold hours per stop |
| Bed maintenance (weed/mulch/prune, established bed) | Hand tools | ~150–250 sq ft/hr per laborer | Highly obstacle- and plant-density-dependent |

## Job-costing worksheet (per route, weekly)

```
Route revenue (sum of contracted per-stop or per-route price)     $______
Raw labor: crew-hours × avg hourly wage                            $______
  × burden multiplier (payroll tax + workers' comp class rate
    + benefits — commonly 1.30–1.45x raw wage for landscaping)     $______  <- fully loaded labor $
Equipment hour cost (amortized mower/trimmer/truck cost per hr
  × hours used — commonly $8–15/hr for a ZTR, plus fuel)           $______
Material cost (fertilizer, seed, mulch — maintenance routes
  are typically 5–15% material; install jobs run much higher)     $______
--------------------------------------------------------------
Total route cost                                                   $______
Labor cost as % of revenue        = labor $ ÷ revenue               ____%
  Target band: 30–35% for standard maintenance routes.
  >5 points over band -> check crew-to-stop ratio and billable %
  before assuming a pricing problem.
Billable % (service time ÷ paid time)                               ____%
  Target: ~80%+. Below ~65% -> route has a drive-time/density
  problem, not a labor-speed problem.
Drive-time share (drive time ÷ paid time)                            ____%
  Target ceiling: ~15–20%. Above that, re-cluster the route
  before adding headcount.
```

## Weather / spray go-no-go thresholds

| Condition | Action |
|---|---|
| Sustained wind > 10 mph at application site | Pull backpack/broadcast spray work at that stop; most general-use herbicide labels cap application wind at 10 mph. Confirm against the specific product label — some formulations allow up to 15 mph with low-drift nozzles. |
| Wind gusting but under label ceiling, direction blowing toward adjacent property/water feature | Reschedule regardless of speed — drift-complaint cost is asymmetric to the cost of a rescheduled visit. |
| >0.25" rain in prior 24 hrs, or visibly saturated/spongy turf | Skip mowing that stop; substitute trim/detail/bed work. Mowing saturated turf compacts soil and clumps clippings, both of which generate callbacks. |
| Heat index ≥ 90°F sustained | Move to a work/rest cycle (commonly 15 min rest per 45–60 min work, per NIOSH heat-stress guidance), increase water-break frequency, and shift the day's schedule earlier where possible. |
| Heat index ≥ 103°F | Treat as a hard stop for peak-exposure tasks (spraying in full PPE, heavy manual bed work) during the hottest 2–3 hours; reschedule to early morning. |
| Lightning within 10 miles (30-30 rule: <30 sec between flash and thunder) | Immediate stand-down, equipment off, crew to vehicles, resume only after 30 min with no further activity. |

## Licensed-applicator staffing math

- Every crew applying any pesticide product must have a certified/licensed applicator either **on the crew** or **reachable and able to reach the site within the state's required response window** (varies by state lead agency; commonly framed as "direct supervision" for restricted-use product and looser "reachable by phone, on-site within a defined window" for general-use product under an uncertified technician).
- Staffing example: a branch running 5 spray-capable crews on a given day with 2 certified applicators on staff must either (a) assign one certified applicator per crew and cover only 2 of the 5 crews' spray work that day, or (b) confirm both certified applicators are reachable and within the state's response-time radius for the other 3 crews' locations — not simply "on staff somewhere."
- Recordkeeping per application: product name/EPA registration number, rate, target site, date/time, wind speed and temperature at application, and applicator of record (certified supervisor's name even when a technician made the physical application). Missing wind/temp at time of application is the single most common gap that turns a routine drift complaint into a documentation problem.
- Default fallback order when applicator coverage is short for the day: (1) reassign the spray-dependent stops on that crew's route to a crew with confirmed coverage, (2) reschedule the spray-only portion of the stop to a day with coverage while still mowing/trimming on schedule, (3) as a last resort, pull the spray service entirely from that day's stops rather than run it without confirmed coverage.
