# Artifacts

Filled formulas, tables, and worked calculations an agricultural engineer runs against directly. Verify site-specific values (soil survey, manure analysis, pump test) before applying — these are standard-referenced starting points, not a substitute for the governing project data.

## 1. Grain-bin lateral wall pressure — Janssen's equation (ASABE EP433)

**p_h = (γR)/(2μ') × [1 − e^(−2μ'Kh/R)]**

Where: γ = grain bulk (test) weight (lb/ft³), R = hydraulic radius = D/4 for a circular bin (ft), μ' = coefficient of friction between grain and wall material, K = ratio of lateral to vertical pressure, h = depth below grain surface (ft).

**Typical values for shelled corn against galvanized steel:** γ ≈ 45 lb/ft³ (56 lb/bu ÷ ~1.25 ft³/bu), μ' ≈ 0.35, K ≈ 0.5. Values shift by grain type and wall material — soybeans, wheat, and smooth-wall vs. corrugated bins each carry different μ'/K pairs; confirm against EP433's table before using these as a default for a non-corn crop.

*Example: 30 ft diameter bin (R = 30/4 = 7.5 ft), grain fill depth h = 40 ft to the eave.*

- Exponent: 2μ'Kh/R = (2 × 0.35 × 0.5 × 40) / 7.5 = 14 / 7.5 = 1.867
- e^(−1.867) = 0.1547
- p_h = (45 × 7.5) / (2 × 0.35) × (1 − 0.1547) = 337.5 / 0.7 × 0.8453 = 482.1 × 0.8453 = **407.6 lb/ft² at the wall base**

**Compare to a hydrostatic (fluid) assumption** at the same depth: p = γh = 45 × 40 = **1,800 lb/ft²** — 4.4× the Janssen value. A wall designed on the hydrostatic assumption is not simply "conservative": it's the wrong shape of curve. Janssen pressure asymptotes toward p_max = γR/(2μ') = 482.1 lb/ft² as h → ∞ (already at 84.5% of that asymptote at 40 ft) — pressure growth flattens with depth because wall friction is carrying an increasing share of the grain's weight vertically. Near the eave, where h is small, the Janssen and hydrostatic curves haven't diverged yet — under-margining the upper wall on a "it's overbuilt anyway" assumption is the actual risk, not the lower wall.

**Rule:** never substitute a hydrostatic pressure profile for Janssen's equation on a grain structure — the two curves only agree at h → 0.

## 2. Manning's equation — open channel/waterway capacity check (NRCS NEH-650)

**Q = (1.49/n) × A × R^(2/3) × S^(1/2)** (US customary units, Q in cfs)

Where: n = Manning's roughness coefficient, A = cross-sectional flow area (ft²), R = hydraulic radius = A/P (ft), P = wetted perimeter (ft), S = channel slope (ft/ft).

**Manning's n by channel condition (NRCS grassed-waterway retardance guidance):**

| Condition | n |
|---|---|
| Concrete-lined channel | 0.013–0.015 |
| Excavated earth, clean | 0.022–0.030 |
| Established grass waterway, good stand | 0.035–0.05 |
| Established grass waterway, dense/retardance-C | 0.04–0.06 |
| Channel with woody brush/poor maintenance | 0.05–0.10 |

*Example: trapezoidal grassed waterway, bottom width b = 4 ft, side slope z = 3:1 (H:V), flow depth y = 1.5 ft, channel slope S = 1.5% (0.015), n = 0.045 (established grass, good stand).*

- Area: A = (b + zy)y = (4 + 3×1.5) × 1.5 = 8.5 × 1.5 = 12.75 ft²
- Wetted perimeter: P = b + 2y√(1+z²) = 4 + 2×1.5×√10 = 4 + 3×3.1623 = 13.487 ft
- Hydraulic radius: R = A/P = 12.75 / 13.487 = 0.9454 ft
- R^(2/3) = 0.963
- S^(1/2) = √0.015 = 0.1225
- Q = (1.49/0.045) × 12.75 × 0.963 × 0.1225 = 33.11 × 12.75 × 0.963 × 0.1225 = **49.8 cfs capacity at 1.5 ft flow depth**

Check against the design peak flow from an NRCS TR-55 curve-number analysis for the contributing watershed (e.g., a 160-acre row-crop watershed's 10-year, 24-hour peak runoff estimate) — if the design storm's peak flow is at or below the channel's computed capacity with adequate freeboard (commonly 0.3–0.5 ft above design flow depth), the channel is adequate; if not, widen the base, flatten the side slope, or reduce the slope before increasing depth alone.

**Rule:** capacity scales with R^(2/3) and S^(1/2), not linearly with cross-sectional area — doubling depth on a narrow channel gains less capacity than widening the base on a shallow one; check both before specifying a fix.

## 3. Irrigation system capacity and application efficiency (ASABE EP458)

**Q (gpm) = 452.6 × A(ac) × d(in/day) / [T(hr/day) × Eff]**

Where 452.6 is the conversion constant (1 acre-inch = 27,154 gal; 27,154 ÷ 60 min = 452.6).

**Typical application efficiency by system type:**

| System | Application efficiency |
|---|---|
| Drip/microirrigation | 90–95% |
| Center pivot, low-pressure drop nozzles | 85–90% |
| Center pivot, high-pressure impact sprinklers | 75–80% |
| Solid-set / hand-move sprinkler | 70–80% |
| Gravity/furrow, no tailwater recovery | 55–65% |
| Gravity/furrow, with tailwater recovery | 65–75% |

**Standard center-pivot coverage on a 160-acre quarter section, no corner arm:** radius 1,320 ft (half the 2,640 ft quarter-section side) → area = πr² = π×1,320² = 5,473,175 ft² ÷ 43,560 = **125.7 acres** (≈126 ac), leaving ≈34 ac of dryland corners. A corner-arm system extends coverage toward the full 160 ac but adds mechanical complexity and its own capacity math — treat it as a separate system, not a pro-rated extension of the base circle's capacity.

**Rule:** use the system's actual application efficiency, not a generic 75–80% assumed across all types — a drip system credited at pivot efficiency under-estimates delivered water; a furrow system credited at drip efficiency over-estimates it.

## 4. Manure first-year nitrogen availability and mass balance (MWPS-18, ASABE, land-grant extension guidance)

**Available N (lb/ac) = Total N applied (lb/ac) × first-year availability coefficient**

**First-year N availability coefficients by manure type and application method** (commonly published extension ranges — confirm against current state nutrient-management guidance before finalizing a plan):

| Manure type / method | First-year availability |
|---|---|
| Liquid swine, injected | ~85–90% |
| Liquid dairy, injected | ~75–80% |
| Liquid swine/dairy, surface-applied, not incorporated | ~50–60% |
| Solid dairy/beef, incorporated within 24 hr | ~35–40% |
| Solid dairy/beef, surface-applied, not incorporated | ~20–25% |
| Poultry litter, incorporated | ~55–60% |

*Example: solid dairy manure, incorporated within 24 hr, applied at 20 tons/ac; manure analysis 10 lb total N/ton (as-is basis). Following crop: corn after corn, yield goal 200 bu/ac, university N recommendation 1.1 lb N/bu.*

- Total N applied: 20 tons/ac × 10 lb N/ton = 200 lb total N/ac
- First-year available N (incorporated solid dairy, 40% coefficient): 200 × 0.40 = **80 lb available N/ac**
- Crop N requirement: 200 bu/ac × 1.1 lb N/bu = **220 lb N/ac**
- Supplemental commercial N still required: 220 − 80 = **140 lb N/ac**

**Rule:** the manure application does not "cover" 200 lb of the crop's N need just because 200 lb of total N was applied — only the availability-coefficient-adjusted portion counts against this season's requirement; the remaining organic N mineralizes into subsequent seasons' credits and has to be tracked, not treated as used up.

## 5. Tile-drainage coefficient by soil and land use (ASABE EP260, NRCS CPS 606)

| Land use / soil | Drainage coefficient |
|---|---|
| Row crop, mineral silt-loam soils (Midwest baseline) | 3/8 in/day (0.375) |
| Row crop, heavy clay soils | 1/4 in/day (0.25) |
| Intensively managed vegetable/muck soils | 3/4–1 in/day |

Drainage coefficient sets the design outflow rate the tile system must remove per day to keep the water table at the target depth for field trafficability and root-zone aeration — it is an input to tile size and spacing calculations (e.g., Hooghoudt's equation for spacing given soil hydraulic conductivity and depth to a restrictive layer), not the pipe diameter itself.

**Rule:** never carry one drainage coefficient across a field with mixed soil types on the same design — segment the design by mapped soil unit (SSURGO) and apply the matching coefficient to each.
