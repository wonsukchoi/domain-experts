# Mechanical Insulator — playbook

Filled procedures and reference tables for the four governing cases (thermal efficiency, condensation control, personnel protection, fire-stop) plus the asbestos-determination protocol. Load this when a spec, takeoff, or field diagnosis needs the actual numbers, not just the decision logic in `SKILL.md`.

## 1. Governing-case thickness quick-check (condensation control)

Use this as a field sanity check on whether an installed or proposed thickness is in the right range for a below-ambient line — **not** as the design-of-record calculation. It's conservative (i.e., not risky) for NPS 8 and larger, where pipe curvature has little effect on insulation performance; for NPS 6 and smaller, curvature reduces performance per inch versus a flat slab, so run the actual cylindrical case in 3E Plus or the MICA condensation-control table before finalizing a spec on smaller pipe.

**Formula:**

```
Ts = Ta − (Ta − Tp) × Rsurf / (Rsurf + Rins)
Rsurf = 1 / h            (h ≈ 1.65 Btu/(h·ft²·°F), still-air film coefficient)
Rins  = t / k             (t = thickness in., k = Btu·in/(h·ft²·°F) at mean insulation temp)
```

Target: Ts ≥ ambient dew point, with a few degrees of margin.

**Worked example — 8 in. NPS chilled-water line, 44°F design supply, ambient design condition 85°F DB / 70% RH:**

1. Dew point at 85°F/70% RH ≈ 74.1°F (psychrometric calc). Design target surface ≥ 75°F for ~1°F margin.
2. k = 0.23 Btu·in/(h·ft²·°F) (ASTM C547 max, 75°F mean); Rsurf = 1/1.65 = 0.606.
3. Solve for Rins: `Rtotal = (Ta − Tp) × Rsurf / (Ta − Ts) = (85 − 44) × 0.606 / (85 − 75) = 24.85 / 10 = 2.485`
4. `Rins = 2.485 − 0.606 = 1.879` → `t = Rins × k = 1.879 × 0.23 = 0.43 in.`
5. This is well under the ASHRAE 90.1 energy-minimum thickness for this service (commonly ≥1.5 in. at 8 in. NPS in this temperature range), so the energy-code minimum already covers condensation control on the straight run here — **but this quick check only covers the wall, never supports, valves, or penetrations** (see Section 2).

**When the quick check says code-minimum is *not* enough** (typically: high ambient RH combined with a thin code-minimum thickness, or NPS 6 and under where curvature isn't accounted for): pull the actual MICA condensation-control table or run 3E Plus for the governing thickness, and use double-layer construction (Section 4) if the result exceeds ~1.5–2 in.

## 2. Support/hanger detailing (the part the wall-thickness calc never covers)

Every point of support on a below-ambient line needs a rigid, load-bearing insert under a metal shield — never a bare or foam-wrapped clevis. Field rule of thumb for insert/shield length, centered on the support point [heuristic — confirm against the project's specific MICA edition and pipe schedule]:

| NPS | Insert/shield length | Insert material |
|---|---|---|
| ≤2 in. | 4 in. | Calcium silicate or cellular glass |
| 2.5–5 in. | 8 in. | Calcium silicate or cellular glass |
| 6–10 in. | 12 in. | Cellular glass (higher load rating) |
| ≥12 in. | 18 in. | Cellular glass, engineered saddle |

Every insert gets a vapor-stop mastic ring on each side before the outer jacket is wrapped over it, on any below-ambient line — the insert itself is rigid but not automatically vapor-tight at its ends.

## 3. Jacketing selection by exposure

| Exposure | Jacket | Typical field life | Notes |
|---|---|---|---|
| Indoor, dry, non-abusive | ASJ (all-service jacket) | 15–20 yr | Commercial-spec default; paper/foil-scrim laminate, not weather-rated |
| Indoor, dry, low mechanical abuse | PVC | 15–20 yr | Cheaper than ASJ for exposed runs; UV-degrades in 2–3 yr if it ends up outdoors |
| Outdoor or mechanically exposed | Aluminum, 0.016–0.024 in., smooth or stucco-embossed | 20–30 yr | Standard outdoor/rooftop choice; stucco-embossed resists oil-canning |
| Wash-down, corrosive, marine, food-process | Stainless steel, 0.010–0.016 in. | Decades | Highest cost; specify when chemical or wash-down exposure is present regardless of budget pressure to downgrade |

## 4. Double-layer construction threshold

When calculated or code-minimum thickness exceeds roughly 1.5–2 in. in a single layer, apply two layers with staggered circumferential and longitudinal joints (inner layer joints offset from outer layer joints by roughly half the segment length). A single thick layer's joints run straight through the wall and give both vapor and bulk moisture a direct path from the outer jacket to the pipe; staggered joints in a double layer don't line up, so there's no single straight path through.

## 5. Asbestos-determination protocol (pre-1981 or unlabeled TSI)

1. **Stop before disturbing.** Any pre-1981 or unlabeled pipe/boiler/duct/tank insulation is presumed ACM (PACM) under OSHA 29 CFR 1926.1101 until a bulk sample clears it — treat it as regulated material from the first look, not after a lab result comes back positive.
2. **Classify the work before scoping it:**
   - **Class I** — removal of TSI or surfacing ACM/PACM.
   - **Class II** — removal of other ACM (e.g., roofing, flooring) — not typically the insulator's TSI scope.
   - **Class III** — repair/maintenance where ACM/PACM is likely to be disturbed (the common case for retrofit tie-ins, hanger repairs, or valve access on existing insulated systems).
3. **Bulk-sample** per EPA/AHERA method at an accredited lab before any Class I or Class III work proceeds on unconfirmed material.
4. **Exposure limits govern the work area regardless of class:** 0.1 fiber/cc as an 8-hour time-weighted average, 1.0 fiber/cc over any 30-minute sampling period — competent-person air monitoring applies to Class I and, where exposure is expected to exceed the limits, Class III work.
5. **Document the determination** (sample result or presumed-ACM handling) in the job file before the segment is insulated over or the record is lost with the next re-jacketing.
