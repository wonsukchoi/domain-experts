# Playbook

Filled formulas, thresholds, and workflows a transportation engineer runs against. Verify against the governing agency's current design manual and the applicable HCM/AASHTO edition — these are commonly applied national standards, not a substitute for the jurisdiction-specific rule in front of you.

## 1. Stopping sight distance (AASHTO Green Book)

**SSD = 1.47 × V × t + V² / (30 × (f ± G))**, where V = design speed (mph), t = perception-reaction time (2.5 s, AASHTO standard), f = friction factor (design-speed-dependent), G = grade (decimal, + uphill / − downhill).

| Design speed (mph) | SSD, level grade (ft, Green Book Exhibit 3-1) |
|---|---|
| 25 | 155 |
| 30 | 200 |
| 35 | 250 |
| 40 | 305 |
| 45 | 360 |
| 50 | 425 |
| 55 | 495 |
| 60 | 570 |

*Example: V=45 mph, t=2.5 s, f=0.32, G=0 → reaction distance 1.47×45×2.5=165.4 ft; braking distance 45²/(30×0.32)=210.9 ft; SSD=376.3 ft, reconciling to the tabulated 360 ft.*

**Rule:** compare field-measured available sight distance against the table value for the governing design speed — this check is independent of any capacity/LOS result and is not satisfied by a passing LOS grade.

## 2. Intersection sight distance (ISD) vs. SSD

ISD (AASHTO Green Book Ch. 9, Case B) uses a different formula sized to the time needed to complete a turning/crossing maneuver, not to stop for an object — do not substitute the SSD table for an ISD check at a driveway or minor-street approach; they answer different questions.

## 3. HCM unsignalized (TWSC) capacity and control delay

**Potential capacity: c_p,x = v_c,x × e^(−v_c,x·t_c/3600) / (1 − e^(−v_c,x·t_f/3600))**

| Minor-street movement | Critical gap t_c (s) | Follow-up time t_f (s) |
|---|---|---|
| Right turn from minor street (2-lane major) | 6.9 | 3.3 |
| Left turn from major street | 5.1–5.3 | 2.2 |
| Through/left turn from minor street (2-lane major) | 6.5–7.5 | 4.0 |
| Left turn from minor street (2-lane major) | 7.5 | 3.5 |

*Example: v_c=900 vph, t_c=7.5 s, t_f=3.5 s → c_p = 900×e^(−1.875)/(1−e^(−0.875)) = 900×0.1534/0.5831 = 236.8 vph.*

**Control delay: d = 3600/c_p + 900T[(x−1) + √((x−1)² + (3600/c_p·x)/(450T))] + 5**, where x = v/c_p, T = analysis period in hours (0.25 for a 15-min period), v = demand flow rate (vph).

*Example: c_p=236.8, v=34, x=0.144, T=0.25 → 3600/c_p=15.20; (x−1)²=0.733; (15.20×0.144)/(112.5)=0.0195; √(0.733+0.0195)=0.867; bracket=−0.856+0.867=0.011; 225×0.011=2.5; d=15.20+2.5+5=22.7 s/veh.*

**Rule:** run the demand volume (post-trip-generation, post-distribution) through this formula — never the raw ITE gross trip number.

## 4. LOS threshold tables — signalized vs. unsignalized (do not interchange)

| LOS | Unsignalized (TWSC/AWSC) control delay (s/veh) | Signalized control delay (s/veh) |
|---|---|---|
| A | 0–10 | 0–10 |
| B | >10–15 | >10–20 |
| C | >15–25 | >20–35 |
| D | >25–35 | >35–55 |
| E | >35–50 | >55–80 |
| F | >50 | >80 |

**Rule:** these are two different tables. A signalized-intersection delay of 22 s is LOS B; the same 22 s at an unsignalized approach is LOS C. Confirm control type before reading the grade.

## 5. Trip generation workflow (ITE Trip Generation Manual, 11th ed.)

| Step | Operation | Applies to |
|---|---|---|
| 1 | Gross trips = rate × (size/1,000 GLA or per unit) | Corridor + driveway analysis |
| 2 | Subtract published pass-by trip % | Corridor-level new-trip capacity analysis only |
| 3 | Apply directional split (AM/PM in/out %) | New-external trips |
| 4 | Distribute by direction (trip-distribution study or gravity model) | New-external trips |
| 5 | Assign to specific turning movements at each driveway/intersection | New-external + pass-by (pass-by re-enters here) |

*Example: 45 KSF LUC 820, PM rate 3.71/KSF → 167 gross; pass-by 34% = 57; new external = 110; 48/52 split → 53 in / 57 out; 60% of exiting new-external trips assigned left = 34 vph.*

**Rule:** pass-by trips are excluded from Step 2's corridor-capacity check but re-enter at Step 5 for the driveway/turn-lane volume and warrant check — the same trip is treated differently depending on which analysis is being run.

## 6. Left-/right-turn lane volume-speed warrant (NCHRP 279-derived nomograph pattern)

| Design speed (mph) | Commonly cited opposing-volume threshold (vph) | Commonly cited left-turn-volume threshold (vph) |
|---|---|---|
| ≤35 | ≈400–450 | ≈40–50 |
| 40 | ≈350 | ≈30 |
| 45–50 | ≈300 | ≈20 |
| ≥55 | ≈200 | ≈10 |

**Rule:** thresholds fall as design speed rises — higher-speed facilities warrant a turn lane at lower conflict volumes because closing speeds increase collision severity. Verify against the governing state DOT access-management manual; NCHRP 279 break points are commonly adopted but not universal.

## 7. Turn-lane storage and taper length

**Storage length ≥ 95th-percentile queue length from the HCM output**, rounded up to the next standard increment (commonly 25 or 50 ft). **Taper length = (design speed in mph) × (lane offset width in ft)**, a widely used state-DOT rule of thumb (e.g., a 12-ft lane offset at 45 mph → 45×12 = 540 ft taper), subject to the governing manual's own taper table.

**Rule:** storage and taper are sized independently and fail differently — undersized storage causes queue spillback into the through lane; undersized taper causes an abrupt, unsafe merge. Check both.
