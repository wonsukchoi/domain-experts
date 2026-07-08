# Playbook — sizing calcs and design criteria tables

Filled tables and worked formulas to execute the calcs referenced in `SKILL.md`. Every threshold below traces to Ten States Standards, EPA guidance, or 40 CFR as cited; where a range is "typical practice" rather than a hard code minimum, it's labeled as such — verify against the state's currently adopted manual before using in a stamped design.

## 1. Design-flow definitions (use the right one)

| Flow basis | Typical use | How to derive |
|---|---|---|
| Average day (ADF) | Cost, staffing, digester loading | Metered billing / per-EDU generation rate × EDU count |
| Maximum day (MDF) | Chemical feed capacity, filter design | ADF × max-day peaking factor (often 1.5–2.5×, utility-specific) |
| Peak hour (PHF) | Pump/hydraulic sizing, pipe capacity | ADF × Harmon or Babbitt formula, or utility-specific PF |
| Minimum hour (MinH) | CT check, wet-well cycling at low end | ADF × 0.3–0.5 (typical low-flow ratio, utility-specific) |

**Harmon formula** (peaking factor, wastewater collection, population in thousands, P):
`PF = 1 + 14 / (4 + √P)`
Example: P = 3 (3,000-person service area) → PF = 1 + 14/(4+1.732) = 1 + 2.44 = **3.44**. Caps around 5.0 for very small P and floors around 2.0 for large P in most state adaptations — check the state manual for the exact bounds it uses (some states substitute Babbitt's formula, `PF = 5/P^0.2`, which gives similar results at mid-range P).

## 2. Pump station / wet well sizing

**Minimum cycle time between starts, by motor size** (Ten States Standards-derived bracket — verify current edition/state adoption):

| Motor size | Minimum cycle time (t) |
|---|---|
| ≤ 15 hp | 10 min |
| > 15–30 hp | 13 min |
| > 30–50 hp | 15 min |
| > 50–100 hp | 18 min |
| > 100 hp | 20 min |

**Required active (cycling) storage volume:**
`V (gal) = Qp × t / 4`
where Qp = pump rated capacity (gpm) at the operating point, t = minimum cycle time (min) for that motor's hp bracket. The 4 comes from the worst-case cycling condition occurring at inflow = Qp/2 (derivation: cycle time = V/(Qp−Qi) + V/Qi, minimized over Qi at Qi=Qp/2, giving cycle time = 4V/Qp).

**Wet well drawdown depth from required volume:**
`Drawdown (ft) = V (gal) / (π/4 × D² × 7.48)`
where D = wet well diameter (ft). Round the drawdown up to a buildable increment (typically nearest 0.1–0.5 ft), never down — rounding down under-delivers the code-minimum volume.

**Pump/system curve intersection** (find the actual operating point, not the catalog rating): tabulate pump head at several flows from the manufacturer curve, tabulate system head (static lift + friction loss × 1.05–1.15 for fittings) at the same flows, and interpolate for the flow where the two are equal. Do this every time a pump, wet well depth, or force main length/diameter changes — none of the three can be sized independently of the other two.

**Force main self-cleansing velocity check:**
`V (ft/s) = 0.4085 × Q (gpm) / d² (in)`
Target ≥ 2 ft/s at the lead-pump-alone operating flow (the more restrictive case — checking only lead+lag flow can miss a low-velocity condition during normal single-pump operation). Below 2 ft/s, solids settle and the main goes septic (H2S, odor, corrosion) well before it becomes a hydraulic problem.

## 3. Clarifier / filter loading criteria (Ten States Standards Wastewater, typical ranges — verify state adoption)

| Unit process | Governing parameter | Typical design range |
|---|---|---|
| Primary clarifier (rectangular) | Surface overflow rate | ≤ 1,000 gpd/ft² at average flow; ≤ 2,500 gpd/ft² at peak hourly flow |
| Secondary clarifier (activated sludge) | Surface overflow rate | ≤ 800 gpd/ft² at average flow; ≤ 1,200–2,000 gpd/ft² at peak hourly flow (varies by process: conventional vs extended aeration) |
| Secondary clarifier | Weir overflow rate | ≤ 20,000 gpd/lf of weir at average flow |
| Trickling filter, standard rate | Organic loading rate | 5–25 lb BOD5 / 1,000 ft³/day |
| Trickling filter, high rate | Organic loading rate | 25–300 lb BOD5 / 1,000 ft³/day (media-dependent) |
| Rapid sand/dual-media filter | Hydraulic loading rate | ≤ 2 gpm/ft² (conventional); up to 4 gpm/ft² for approved dual/mixed media with pilot-scale data |

**Converting a raw MGD flow to the governing rate:** `SOR (gpd/ft²) = Q (gpd) / surface area (ft²)`. A "the clarifier handles 2 MGD fine" statement is not a design check until it's converted to gpd/ft² against the table above — and checked at peak hourly flow, not just average.

**Filter redundancy note:** when computing filter HLR, use the area of filters actually in service (N total minus at least 1 offline for backwash), not total installed area — a plant with 4 filters checked against total area silently assumes all 4 are always online.

## 4. Disinfection CT (chlorine, EPA SWTR Guidance Manual — illustrative excerpt, verify current published table)

**3-log Giardia lamblia inactivation, CT (mg·min/L), free chlorine, pH 7.0, residual C = 1.0 mg/L:**

| Temperature | Required CT |
|---|---|
| 0.5 °C | 137 |
| 5 °C | 111 |
| 10 °C | 89 |
| 15 °C | 67 |
| 20 °C | 44 |
| 25 °C | 22 |

**Applying it:** required contact time at a given residual = CT_required / C_actual. Example: at 10 °C with a maintained residual of 1.4 mg/L (not the table's 1.0 mg/L baseline), required time = 89/1.4 = 63.6 min — CT tables are indexed by residual bin in the full published table; interpolating linearly between adjacent residual columns is the common field approximation, not exact.

**T10 vs theoretical detention time:** `T10 = theoretical detention time (V/Q) × baffling factor`. Baffling factors (Ten States / EPA guidance, unbaffled through well-baffled): unbaffled ≈ 0.1, poor baffling ≈ 0.3, average baffling ≈ 0.5, superior (serpentine, over-under) baffling ≈ 0.7–0.9. Use the tracer-study value if one exists for the specific basin; default to the conservative end of the range (favoring 0.1–0.3) when none exists and the basin geometry isn't a demonstrated serpentine/plug-flow design.

## 5. Biosolids quick-reference

| Parameter | Typical value | Note |
|---|---|---|
| Anaerobic digestion VS destruction | 40–60% | Below ~35% suggests underloading, low temperature, or toxicity |
| Belt filter press cake solids | 18–25% TS | Below ~15% TS suggests inadequate polymer dose or poor feed conditioning |
| Centrifuge cake solids | 20–30% TS | Higher capital/energy cost than belt press, less polymer-sensitive |
| Class B pathogen reduction (40 CFR 503) | Fecal coliform < 2,000,000 MPN/g TS | Land application restrictions apply (site access, crop harvest delay) |
| Class A pathogen reduction (40 CFR 503) | Fecal coliform < 1,000 MPN/g TS | Unrestricted use — market decision layered on top of treatment, not required by treatment alone |
