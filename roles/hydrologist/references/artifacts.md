# Hydrologist — Artifacts

## Flood-frequency analysis table (Log-Pearson Type III)

Gage: USGS 08158000-type station, n=30 annual peaks, mean log10(Q)=3.20, std log10(Q)=0.25, weighted skew=-0.02.

| Return period (yr) | AEP | K (skew -0.02) | log10(Q) | Q (cfs) | 90% CI (cfs) |
|---|---|---|---|---|---|
| 2 | 50% | -0.017 | 3.196 | 1,570 | 1,410-1,750 |
| 5 | 20% | 0.842 | 3.410 | 2,570 | 2,260-2,930 |
| 10 | 10% | 1.283 | 3.521 | 3,318 | 2,850-3,860 |
| 25 | 4% | 1.750 | 3.638 | 4,335 | 3,600-5,220 |
| 50 | 2% | 2.050 | 3.713 | 5,157 | 4,150-6,410 |
| 100 | 1% | 2.330 | 3.783 | 6,062 | 4,850-7,900 |
| 500 | 0.2% | 2.950 | 3.938 | 8,660 | 6,500-12,300 |

K-values are standard Log-Pearson III frequency factors for the given skew — pull from a Bulletin 17C K-table or compute via the Wilson-Hilferty approximation, do not eyeball. Confidence intervals widen fast past the period of record (30 years here) — the 500-year CI spans nearly 2x, the 10-year CI spans about 1.35x.

## Watershed water-balance worksheet

| Component | Value (in/yr, basin-averaged) | Source |
|---|---|---|
| Precipitation (P) | 42.3 | NOAA Atlas 14 / gage network, 10-yr average |
| Evapotranspiration (ET) | 26.8 | MODIS ET product, basin-averaged |
| Streamflow / runoff (Q) | 14.9 | USGS gage, converted to depth over drainage area |
| Storage change (ΔS) | +0.3 | Groundwater level trend, converted to depth via specific yield |
| **Balance check** | P - ET - Q - ΔS = 42.3 - 26.8 - 14.9 - 0.3 = **0.3** | Residual = 0.7% of P — acceptable (target <5%) |

A residual above ~5-10% of P usually means one term is wrong (commonly ET, the hardest to measure directly) rather than an unmodeled process — recheck the ET estimate and gage rating curve before accepting a large residual as "ungauged loss."

## Aquifer pumping-test summary (Theis method)

| Parameter | Value |
|---|---|
| Pumping rate (Q) | 500 gpm (96,300 ft³/day) |
| Test duration | 24 hours |
| Observation well distance (r) | 150 ft |
| Drawdown at t=1440 min | 4.2 ft |
| Match-point (Theis type curve) | W(u)=1.0, u=0.1, s=1 ft, 1/u·t=10 min |
| **Transmissivity (T)** | T = (Q/4πs)·W(u) = (96,300/4π·1)·1.0 ≈ **7,660 ft²/day** |
| **Storativity (S)** | S = 4Tut/r² = 4(7,660)(0.1)(1/1440 day)/(150)² ≈ **9.5×10⁻⁴** |
| Classification | S in 10⁻³-10⁻⁵ range → confined aquifer (unconfined typically 0.05-0.30) |

Report both T and S with the match-point values used — a T number without the type-curve match documented can't be checked or reproduced by a reviewer.

## Deliverable excerpt — water-availability memo (water-rights context)

"Based on the weighted-skew Log-Pearson III analysis of the [stream] gage record (Table 1), the median annual flow is estimated at 1,570 cfs (2-year event), with a 10% annual exceedance probability flow of 3,318 cfs. Per [state] Water Rights Division records, senior appropriative rights on this reach total 1,850 cfs (priority dates 1889-1952). During the median-flow scenario, approximately 280 cfs of decreed but unexercised junior rights would be subject to curtailment under a call from the senior right holders — this is a legal availability constraint, not a physical shortage, since actual median flow exceeds total senior demand in most years. Physical shortage risk becomes material only in years falling below the 25% AEP flow threshold of approximately 2,100 cfs (interpolated), which the 30-year record shows occurring in 6 of 30 years (20%)."
