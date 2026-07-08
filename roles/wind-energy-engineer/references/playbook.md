# Playbook

Filled tables and worked mini-calculations a wind energy engineer runs against during turbine selection, load-case verification, and layout diligence. Verify current standard editions, site-specific measured data, and turbine-specific certified curves before citing any of these in a stamped calculation — these are commonly applied methods and named standards, not a substitute for project data.

## 1. IEC 61400-1 wind turbine class reference

| Class | Reference wind speed Vref (10-min avg, m/s) | Annual average wind speed Vave (m/s) | Turbulence category A (Iref) | Turbulence category B (Iref) | Turbulence category C (Iref) |
|---|---|---|---|---|---|
| I | 50 | 10 | 0.16 | 0.14 | 0.12 |
| II | 42.5 | 8.5 | 0.16 | 0.14 | 0.12 |
| III | 37.5 | 7.5 | 0.16 | 0.14 | 0.12 |
| S | Site-specific — designer-specified values outside the standard classes | — | — | — | — |

**Rule:** class is selected from the site's measured 50-year extreme wind speed and turbulence intensity, not from Vave alone — a site with Vave = 7.2 m/s (which would suggest Class III) but a measured 50-year gust exceeding 37.5 m/s's implied extreme needs Class II or a Class S site-specific design instead. The SKILL.md worked example's site (c = 8.5 m/s Weibull scale, Vave ≈ 7.53 m/s) would screen toward Class III on average wind speed alone; the extreme-gust and turbulence-category check has to confirm that independently before ordering turbines.

## 2. Design load case (DLC) selection, abridged

| DLC | Design situation | Wind condition | Load type | Partial safety factor γf (IEC 61400-1 Table 3) |
|---|---|---|---|---|
| 1.1 | Power production | Normal turbulence model (NTM), Vin–Vout | Ultimate, extrapolated | 1.35 (N) |
| 1.2 | Power production | NTM, Vin–Vout | Fatigue | 1.0 (fatigue partial factors per material S-N curve) |
| 2.1 | Power production + fault | NTM at Vr ± 2 m/s, control system fault | Ultimate | 1.35 (N) |
| 6.1 | Parked (standing still or idling) | Extreme wind speed model (EWM), 50-yr return | Ultimate | 1.35 (N) |
| 6.2 | Parked, grid loss | EWM, 50-yr return, loss of electrical network | Ultimate, abnormal | 1.1 (A) |
| 6.4 | Parked | Normal wind profile, longer duration | Fatigue | 1.0 |
| 7.1 | Parked, maintenance/transport | Reduced Vref | Ultimate | 1.35 (N) |

**Rule:** DLC 1.1/1.2 (operating) and DLC 6.1 (parked, extreme) commonly govern different components on the same structure — DLC 1.2's cyclic operating loads over a 20–25 year design life govern blade-root and main-shaft fatigue life, while DLC 6.1's single extreme 50-year gust governs the tower base and foundation's ultimate overturning moment. Checking a foundation against DLC 6.1 alone without a fatigue check on the anchor bolts (DLC 1.2-driven) leaves the bolts unverified for the failure mode that actually dominates their design.

## 3. Tower-base extreme load — worked mini-calculation (DLC 6.1, parked, distinct from SKILL.md's operational AEP/wake case)

**Turbine:** same as SKILL.md's worked example — Class I site, rotor diameter 130 m, hub height 100 m, Vref = 50 m/s (10-min average, Class I).

- Extreme wind speed model (EWM), 3-second gust: Ve50 = 1.4 × Vref = 1.4 × 50 = **70 m/s**.
- Parked turbine, blades feathered: effective drag area (feathered blade edges + nacelle + hub, not the full swept disk) estimated at 45 m²; drag coefficient Cd = 1.1 (bluff-body estimate for this geometry).
- Extreme thrust force: F = 0.5 × ρ × Cd × A × Ve50² = 0.5 × 1.225 × 1.1 × 45 × 70² = 0.6125 × 1.1 × 45 × 4,900 = **148.56 kN**.
- Apply IEC 61400-1 Table 3 partial safety factor for a normal (N) ultimate load case, γf = 1.35: design thrust = 148.56 × 1.35 = **200.56 kN**.
- Tower-base overturning moment (thrust applied at hub height, conservatively ignoring the shorter moment arm of nacelle/tower drag component): M = F_design × h_hub = 200.56 kN × 100 m = **20,056 kN·m** (≈ 20.06 MN·m).

**Rule:** this moment is the ultimate-limit-state design input the foundation engineer sizes the base slab and anchor cage against — it is not the number to reuse for a fatigue check, which instead comes from cycling through the full DLC 1.2 turbulent wind time series, not a single extreme gust.

## 4. Jensen/Park wake model — parameter reference

ΔV/V₀ = (1 − √(1 − Ct)) × (D / (D + 2kx))², where D = rotor diameter, x = downstream distance, k = wake decay constant, Ct = thrust coefficient at the operating wind speed.

| Parameter | Typical value | Notes |
|---|---|---|
| Wake decay constant k, onshore | 0.075 | Higher terrain roughness increases wake decay (faster recovery) |
| Wake decay constant k, offshore | 0.04 | Smoother surface, slower wake recovery — wakes persist farther downstream |
| Thrust coefficient Ct, below-rated operation | 0.7–0.85 | Peaks near rated wind speed, then falls as pitch control reduces thrust above rated |
| Thrust coefficient Ct, near cut-out | 0.2–0.3 | Blades pitched aggressively to shed load approaching cut-out |

**Rule:** k = 0.075 (onshore, open terrain) is the SKILL.md example's assumption; using the offshore value (0.04) on an onshore open-terrain site would understate wake recovery and overstate downstream power deficit — always confirm which k applies to the site's actual terrain roughness class before running the layout comparison.

## 5. P50/P90/P99 uncertainty stack — component ranges

| Uncertainty source | Typical range (1-sigma, %) | Driver |
|---|---|---|
| Wind resource measurement | 4–8% | Met mast/LIDAR data duration and quality, long-term correlation to a reference station |
| Wake model | 3–6% | Model choice (Jensen/Park vs. CFD) and terrain complexity |
| Availability estimate | 2–4% | O&M contract terms, turbine fleet maturity |
| Electrical losses | 1–2% | Collector system design, transformer losses |

Combine in quadrature: σ_total = √(Σσᵢ²). Convert to an exceedance level using the standard normal z-value: Pₓ = P50 × (1 − z_x × σ_total), where z90 = 1.2816, z95 = 1.6449, z99 = 2.3263.

**Worked check against SKILL.md's example:** σ_total = √(6² + 4² + 3² + 1²) = 7.87%. P99 (1-year debt-sizing case) = 134.26 × (1 − 2.3263 × 0.0787) = 134.26 × 0.8169 = **109.68 GWh/yr** — the figure a lender would use for a 1-year debt-service-coverage stress test, materially lower than either the P50 (134.26 GWh/yr) or the P90 (120.71 GWh/yr) quoted in the feasibility memo.
