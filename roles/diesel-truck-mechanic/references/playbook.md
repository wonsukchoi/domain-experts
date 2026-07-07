# Diesel Truck Mechanic — Playbook

Filled reference sequences: DEF/SCR fault isolation, CVSA out-of-service thresholds, PM-A/PM-B scope, and the repair-now-vs-limp-to-terminal decision.

## 1. DEF/SCR/DPF fault isolation sequence

Work in this order — each step is cheaper and faster than the next, so don't skip ahead to component replacement.

| Step | Action | Pass criterion | If fail |
|---|---|---|---|
| 1 | Pull full fault history (last 5,000 mi), not just active code | No repeat codes in same subsystem | Repeat codes → look for upstream cause (EGR cooler, injector) before touching the current code |
| 2 | Refractometer test on DEF tank sample | 31.8–33.2% concentration (ISO 22241, nominal 32.5%) | Out of spec → drain/flush/refill tank ($90–150 fluid, ~1.2 hr labor); do not replace DEF quality sensor yet |
| 3 | Compare NOx sensor readings pre-SCR vs. post-SCR (scan tool live PID) | Delta consistent with SCR conversion efficiency spec (OEM-specific, typically >90% reduction at operating temp) | Delta below spec with correct DEF concentration → SCR catalyst degradation or NOx sensor drift, not a fluid issue |
| 4 | Check DEF dosing valve commanded vs. actual injection quantity | Actual within ~10% of commanded | Mismatch → dosing valve or injector line fault, not sensor or fluid |
| 5 | Only after steps 2–4 clear DEF/dosing as causes, replace the named sensor | Code clears and stays clear over a 15+ min road test | Recurs → escalate to catalyst or wiring harness inspection |

**DPF regen decision:**

| Condition | Action |
|---|---|
| DPF differential pressure trending up <5%/interval, no active code | No action — normal soot accumulation curve |
| Differential pressure up 15%+ over 3 consecutive PM intervals | Investigate upstream cause (injector, EGR, short-trip duty cycle) before forcing a regen |
| Soot load >80% of filter capacity (ECM PID) or active "regen needed" lamp | Parked forced regen, then re-check differential pressure after cool-down |
| Forced regen fails to bring soot load below ~30% | DPF likely ash-loaded past cleaning threshold — pull and clean or replace, don't force-regen again |

## 2. CVSA out-of-service quick reference (illustrative — always confirm against the current-year handbook)

| Item | Out-of-service threshold |
|---|---|
| Brake pushrod stroke, Type 30 long-stroke chamber | Stroke exceeds 2 in — adjust or replace, no partial credit |
| Brake pushrod stroke, Type 24 chamber | Stroke exceeds 1¾ in |
| Defective brakes, whole vehicle/combination | 20% or more of service brakes on the unit are defective |
| Steer axle tire tread depth | Below 4/32 in at any point |
| Other axle tire tread depth | Below 2/32 in at any point |
| Annual inspection currency | More than 12 months since last qualifying inspection (49 CFR §396.17) |

## 3. PM-A / PM-B scope and interval template

| Interval | Typical mileage (long-haul duty) | Scope |
|---|---|---|
| PM-A | Every 25,000–30,000 mi or 3 months, whichever first | Oil/filter change, chassis lube, visual safety walk (lights, glass, wipers, mirrors, leaks), tire pressure/tread spot-check, fluid levels |
| PM-B | Every 50,000–100,000 mi or annual, whichever first | Full PM-A scope plus: brake pushrod stroke measurement all axles, slack adjuster function, steering linkage/kingpin wear check, U-joint/driveline inspection, DEF system check (concentration + dosing), coolant system pressure test, full undercarriage inspection |

Adjust downward (shorter interval) for vocational/stop-and-go duty cycles — idle hours and PTO cycles wear brakes and driveline components faster per mile than steady highway running.

## 4. Repair-now vs. limp-to-terminal vs. tow decision

Compare three cost lines for each option before choosing:

```
Total cost = parts + labor + (downtime hours ÷ 24) × daily truck revenue + risk premium
```

Risk premium: add a full lost-day equivalent if the option risks a second roadside event or an OOS defect being cited (roadside OOS write-ups also count against the fleet's CSA Vehicle Maintenance BASIC score, which raises inspection-selection frequency fleet-wide).

**Example comparison (regional dry-van tractor, $2,100/day revenue):**

| Option | Parts + labor | Downtime | Risk premium | Total |
|---|---|---|---|---|
| Repair on-site now (part in stock) | $264 | 2 hrs (~$175 revenue-equivalent) | none | ~$439 |
| Limp to home terminal 40 mi away, repair there | $264 | 4 hrs (~$350) | none (within limp-home spec) | ~$614 |
| Tow to nearest shop, part overnight | $264 + $180 tow | 24 hrs ($2,100) | none | ~$2,544 |
| Drive on with active OOS-level defect (never do this) | — | — | roadside OOS write-up + CSA BASIC score hit + potential second breakdown | not a valid option |

Choose the lowest total that doesn't cross an out-of-service threshold or risk stranding the truck a second time.
