# Mobile Heavy Equipment Mechanic — Playbook

Filled reference sequences: hydraulic pressure/flow diagnostic isolation, undercarriage wear measurement against replacement bands, ISO 4406 cleanliness targets by component, and the on-site-vs-haul-to-shop cost comparison.

## 1. Hydraulic diagnostic isolation sequence

Work in this order — each step is cheaper than the next, so don't jump to component replacement on a single reading.

| Step | Action | Pass criterion | If fail |
|---|---|---|---|
| 1 | Pull fault/alarm history and PM log (last 500 hrs) | No repeat faults in the same circuit | Repeat faults → suspect an unaddressed contamination or misalignment cause, not a new part failure |
| 2 | Main relief pressure test at the affected circuit | Within OEM spec band (e.g., 3,000–3,100 psi on a typical dozer implement circuit; excavator main circuits often run 4,500–5,100 psi — confirm against the specific machine's service spec) | Below spec → relief valve mis-set or worn, or a bypass elsewhere bleeding pressure before the gauge |
| 3 | In-line flow test under load at rated rpm | Flow within ~10% of rated pump output at that rpm | Flow deficit with normal pressure → do not condemn the relief valve; move to case-drain test |
| 4 | Case-drain flow test on the pump/motor | Case drain leakage under roughly 10% of rated flow | Above ~10% → internal wear (piston/vane/gear clearance), pump or motor is the root cause |
| 5 | Cylinder drift/isolation test (raise/extend, hold valve neutral, block hose to isolate cylinder alone, watch 60 sec) | Drift under roughly 1 in./60 sec under rated load | Drift beyond that → internal seal bypass in the cylinder, not the pump or valve |
| 6 | Only after steps 2–5 clear pump, valve, and cylinder individually, inspect the directional control valve spool for wear/scoring | Spool clearance within OEM spec | Out of spec → valve rebuild or replacement, now with a confirmed root cause |

## 2. Undercarriage wear measurement and replacement bands

| Component | Measurement | Replace-now threshold (commonly cited OEM guidance) | Notes |
|---|---|---|---|
| Track chain pitch elongation | Pitch gauge against new-chain pitch | ~3% elongation | Beyond this, sprocket tooth damage accelerates because the chain no longer meshes at the sprocket's designed pitch |
| Sprocket tooth profile | Wear-profile gauge ("hook" wear stage) | Roughly 50% tooth-tip wear point, replace before profile hooks | A hooked sprocket will itself accelerate wear on a new chain if not replaced together |
| Bushing OD | Micrometer/gauge against new OD | Roughly 50–80% wear band for planned replacement; beyond ~80% risk of pin/bushing seizure and chain failure | Bushings can often be turned/reversed once if not yet through-worn — confirm against OEM reman spec before condemning |
| Track shoe/grouser height | Height gauge against new grouser height | Roughly 50% height loss for a planned-replacement call on abrasive sites; up to 70–80% tolerable on low-wear ground before traction loss becomes the limiting factor | Site ground conditions (rock vs soil) shift this band more than for other components |
| Roller/idler flange | Flange thickness gauge | Roughly 50% of original flange thickness | Beyond this, derailment risk under side-load (turning, sloped ground) increases sharply |

**Matched-set rule:** when chain pitch elongation and sprocket wear are both approaching their thresholds within the same PM cycle, replace as a set. Installing a new sprocket against a chain already at 3%+ elongation (or vice versa) measurably shortens the new part's service life below its rated hours.

**Abrasive-site adjustment:** halve the OEM's stated re-inspection interval (not necessarily the replacement threshold) on quarry, sand, or demolition-rubble sites versus a graded-lot or paving duty cycle — the wear rate per hour is materially higher, so the same percent-worn point arrives sooner than the printed interval assumes.

## 3. ISO 4406 cleanliness targets by component sensitivity

| Component type | Target ISO 4406 code | Why |
|---|---|---|
| Servo valves | 16/14/11 | Tightest tolerance, smallest orifice/clearance, most sensitive to particulate |
| Proportional valves | 18/16/13 | Second-tightest — common in modern excavator/loader implement circuits |
| Piston pumps/motors | 18/16/13 to 19/17/14 | Close internal clearances wear faster with particulate above target |
| Standard directional valves, cylinders | 20/18/15 | Looser tolerance, but still fails prematurely well above this code |
| Low-pressure/return-line circuits | 21/19/16 | Least sensitive, but a source of contamination migrating into tighter circuits downstream |

**Post-repair rule:** any circuit opened for a hose, cylinder, pump, or valve repair should be sampled after button-up, not assumed clean because the new part was clean out of the box — installation is itself a contamination event (ingress during disconnection, residual debris in fittings). Run a filter cart pass if the sample reads worse than the target code for the most sensitive component on that circuit before returning the machine to service.

## 4. On-site repair vs haul-to-shop decision

```
Total cost (on-site) = mobile dispatch fee + (travel hours x idle-crew rate) + parts + labor + any rental backup for downtime beyond same-day
Total cost (haul)     = tow/lowboy cost + parts + shop labor + (downtime hours / 24) x idle-crew or rental-backup daily rate
```

Idle-crew rate: the fully loaded cost of the crew and equipment standing idle waiting on this machine (operator wage + adjacent-equipment idle cost + any liquidated-damages exposure on a scheduled job), not just the machine's own owning/operating cost.

**Example comparison (quarry-site dozer, $850/day rental backup + $400/trip delivery, 35 miles from shop):**

| Option | Parts + labor | Travel/downtime | Total |
|---|---|---|---|
| On-site repair, part carried on service truck | $340 + $405 | 3 hrs, no rental needed (same shift) | ~$745 |
| On-site repair, part not on truck, same-day delivery | $340 + $405 | half-day rental backup, $425 | ~$1,170 |
| Haul to shop, part in shop stock | $340 + $405 (shop rate, lower labor rate assumed same here) | tow $600 round trip + same-day turnaround, no rental needed | ~$1,345 |
| Haul to shop, part not in stock, overnight freight | $340 + $405 | tow $600 + 2 days rental/delivery $2,500 | ~$3,845 |

Choose the lowest total that doesn't require a repair beyond the service truck's capability (major component replacement, frame-straightening, or anything needing shop lift/press equipment routes to the shop regardless of cost, since it isn't executable on-site at all).
