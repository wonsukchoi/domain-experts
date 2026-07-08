# Playbook

## 1. Concrete field acceptance test — fillable data sheet

```
Project: ______________   Date: ______   Pour location: ______________
Mix design ID: ______   f'c: _______ psi   Spec slump: ____ ± ____ in
Spec air content: ____ % ± ____ %   Ambient temp: ____°F

Sample taken per ASTM C172 (composite, ≥2 portions, combined within 15 min): Y / N
Truck/load #: ______   Batch ticket time: ______   Time sampled: ______ (must be ≤15 min after sampling window opens, tested within 30 min of sampling for slump/air)

Slump (ASTM C143):        measured ____ in   spec range ____–____ in   PASS / REJECT
Air content (ASTM C231):  measured ____ %     spec range ____–____ %   PASS / REJECT
Concrete temp (ASTM C1064): measured ____°F    limit 50–90°F (ACI 305/306)  PASS / REJECT

Cylinders molded (ASTM C31): Set ID ______   # molded: ____ (std. 4, min for 7d+28d×2+hold)
  Cylinder 1 — 7-day break (informational): ____ psi
  Cylinder 2 — 28-day break: ____ psi
  Cylinder 3 — 28-day break: ____ psi
  Strength test result (avg of 28-day pair) = ____ psi
  Cylinder 4 — held in reserve, break only if a result is disputed.
```

## 2. ACI 318 §26.12.3.1 acceptance criteria — apply both, every time

| f'c | Criterion (a) — running average | Criterion (b) — individual test floor |
|---|---|---|
| ≤ 5,000 psi | avg of any 3 consecutive strength test results ≥ f'c | no single result more than 500 psi below f'c |
| > 5,000 psi | avg of any 3 consecutive strength test results ≥ f'c | no single result more than 0.10 × f'c below f'c |

- A "strength test result" is the **average of two cylinders** broken at 28 days from the same sample — not a single cylinder.
- Both criteria must pass. A result that clears criterion (b) but drags the 3-test average below f'c still fails criterion (a).
- If either criterion fails: notify the engineer of record immediately (don't wait for a written report), and expect a request for core tests (ASTM C42) evaluated per ACI 318 §26.12.5 — cores pass if the average of 3 cores ≥ 0.85 × f'c and no single core < 0.75 × f'c.

## 3. Minimum sampling frequency (ACI 318 §26.12.2.1)

Sample not less than:
- Once per day of placement, **and**
- Once per 150 yd³ placed, **and**
- Once per 5,000 ft² of surface area for slabs or walls.

Whichever produces the most samples governs. Round pour volume up: 210 yd³ / 150 = 1.4 → 2 sets required, not 1.

## 4. Proctor compaction — relative compaction worksheet

```
Governing method: Standard (ASTM D698) / Modified (ASTM D1557)  — confirm against spec, do not assume
Lab max dry density (γd-max): ________ pcf
Lab optimum moisture content (OMC): ________ %
Spec minimum % compaction: ________ %
Spec moisture window: OMC ± ____ % (commonly ±2%)

Field test method: Nuclear gauge (ASTM D6938) / Sand cone (ASTM D1556) / Drive cylinder (ASTM D2937)
Lift #: ______   Location/station: ______
Field wet density: ________ pcf
Field moisture content (w): ________ %
Field dry density = wet density / (1 + w/100) = ________ pcf

% Compaction = field dry density / lab max dry density × 100 = ________ %
Moisture check: field moisture within OMC ± tolerance?  Y / N

PASS requires BOTH: % Compaction ≥ spec minimum, AND moisture within window.
```

**Standard vs. Modified Proctor — do not mix curves:**

| Method | Compactive effort | Typical use | Effect vs. Standard |
|---|---|---|---|
| Standard (ASTM D698) | ~12,375 ft-lb/ft³ | General structural fill, building pads | Baseline |
| Modified (ASTM D1557) | ~56,000 ft-lb/ft³ | Pavement subgrade/base, heavy-load areas | Higher max dry density, lower OMC than Standard for the same soil |

A field result reported as "97% compaction" without stating which curve is unusable — the same field density can be 97% of a Modified curve and well over 100% of a Standard curve for the same soil.

**Typical spec minimums (confirm against the actual geotechnical report — these are common defaults, not code):**

| Application | Compaction requirement | Method |
|---|---|---|
| Structural fill under footings | ≥ 95% | Standard Proctor (D698) |
| General building pad fill | ≥ 92–95% | Standard Proctor (D698) |
| Pavement subgrade | ≥ 95% | Modified Proctor (D1557) |
| Pavement base course | ≥ 98% | Modified Proctor (D1557) |
| Utility trench backfill (non-structural) | ≥ 90% | Standard Proctor (D698) |

## 5. Quantity takeoff reconciliation

**Concrete volume:**
```
Volume (ft³) = Length (ft) × Width (ft) × Depth/Thickness (ft)
Volume (CY) = Volume (ft³) / 27
Order quantity (CY) = Volume (CY) × (1 + waste factor)
```

| Element | Typical waste factor |
|---|---|
| Slab on grade | 3–5% |
| Footings / grade beams | 5–8% |
| Foundation walls (formed) | 5–8% |
| Columns / piers | 8–10% |

**Rebar weight** (ASTM A615 standard bar sizes, straight bar, lb/linear ft):

| Bar size | Diameter (in) | Weight (lb/ft) |
|---|---|---|
| #3 | 0.375 | 0.376 |
| #4 | 0.500 | 0.668 |
| #5 | 0.625 | 1.043 |
| #6 | 0.750 | 1.502 |
| #7 | 0.875 | 2.044 |
| #8 | 1.000 | 2.670 |
| #9 | 1.128 | 3.400 |
| #10 | 1.270 | 4.303 |

**Worked footing takeoff — 8 ft × 8 ft × 2 ft spread footing, #6 bars @ 12" o.c. each way, 3" clear cover:**
```
Concrete: 8 × 8 × 2 = 128 ft³ / 27 = 4.74 CY, × 1.08 (8% waste) = 5.12 CY → order 5.25 CY (round to nearest 0.25 CY)

Rebar, one direction: bars at 12" o.c. across 8 ft = 9 bars, each 8 ft − (2 × 0.25 ft cover) = 7.5 ft long
Both directions (mat is two-way): 18 bars × 7.5 ft = 135 ft
Weight = 135 ft × 1.502 lb/ft (#6) = 202.8 lb ≈ 203 lb
```

**Reconciliation check at end of pour:**
```
Theoretical volume (from plan takeoff, + waste factor): ________ CY
Delivered volume (sum of batch tickets):                ________ CY
Variance = (Delivered − Theoretical) / Theoretical × 100 = ________ %

Within ± waste factor band: no flag.
Exceeds waste factor band on the high side: flag — likely over-excavation, formwork bulge, or subgrade loss; route to PM/PE.
Below theoretical (delivered short): flag — likely a formwork or dimension error; do not assume the placement is complete.
```
