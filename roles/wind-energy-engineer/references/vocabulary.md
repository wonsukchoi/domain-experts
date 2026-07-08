# Vocabulary

Terms generalists flatten together that a wind energy engineer keeps sharply separate — the value is in the misuse, not the definition.

## Betz limit vs. power coefficient (Cp)

The **Betz limit** (16/27 ≈ 0.593) is the theoretical maximum fraction of wind kinetic energy any rotor can extract, derived from momentum theory on an idealized actuator disk. **Cp** is the actual fraction a specific turbine achieves at a specific operating point — a function of wind speed, tip speed ratio, and blade design, always below the Betz limit.

**In use:** "The certified curve shows Cp peaking at 0.47 around 7–9 m/s and falling off both toward cut-in and above rated — that peak is the number to cite, not the Betz limit."

**Common misuse:** treating the Betz limit as an achievable target or an average Cp figure, instead of the theoretical ceiling real Cp is always meaningfully below.

## Tip speed ratio (TSR / λ)

The ratio of blade tip speed to free-stream wind speed (λ = ωR/V), the governing parameter for a rotor's aerodynamic operating point. Variable-speed turbines adjust rotor speed to hold TSR near its optimal value (maximizing Cp) across a range of wind speeds in Region 2, below rated.

**In use:** "Below rated, the controller is tracking optimal TSR to hold Cp near its peak — that's why Cp stays roughly flat across 5–9 m/s instead of varying with wind speed."

**Common misuse:** assuming Cp varies smoothly and continuously with wind speed the way raw power output does, rather than recognizing the controller actively holds TSR (and therefore Cp) near constant across much of the below-rated range.

## Weibull shape (k) and scale (c) parameters

The two parameters defining a site's wind-speed probability distribution: **c** (scale, m/s) sets the characteristic wind speed, and **k** (shape, dimensionless) sets how peaked or spread the distribution is — k = 2 is the special case called a Rayleigh distribution, commonly assumed as a default when no site-specific fit exists.

**In use:** "Our met mast fit gives k = 2.0, c = 8.5 — don't substitute a generic k = 2 Rayleigh assumption once we have a real site fit, even though the number happens to match here."

**Common misuse:** treating k = 2 as a universal default rather than a specific case that should be replaced by a measured site fit whenever data exists — a site with a genuinely different k (more or less variable wind) will produce a meaningfully different AEP for the same mean wind speed.

## Design load case (DLC)

A defined combination of wind condition (normal turbulence, extreme wind speed model, etc.), turbine operating state (power production, parked, fault), and load type (ultimate or fatigue) specified in IEC 61400-1, each carrying its own partial safety factor. A component's design load is the governing DLC's result, not an arbitrary worst-case guess.

**In use:** "DLC 6.1 governs the tower base's ultimate overturning moment; DLC 1.2 governs the blade root's fatigue life — don't reuse one DLC's number for the other component's check."

**Common misuse:** citing a single "design load" for a component without specifying which DLC produced it, or assuming the same load case governs every component on the turbine.

## IEC 61400-1 wind turbine class

A standardized rating (I, II, III, or site-specific Class S) defined by reference wind speed (Vref) and turbulence category, matched to a site's extreme wind and turbulence conditions — not its average wind speed.

**In use:** "The site's average wind speed suggests Class III, but the extreme-gust analysis pushes us to Class II — order the turbine on the extreme number, not the average."

**Common misuse:** selecting turbine class from average annual wind speed alone, skipping the extreme-wind and turbulence-category check the class rating is actually built to cover.

## Wake decay constant (k) and the Jensen/Park model

A dimensionless parameter in the Jensen/Park wake model controlling how quickly a turbine's wake recovers to free-stream velocity with downstream distance — commonly 0.075 onshore (rougher terrain, faster recovery) and 0.04 offshore (smoother surface, slower recovery).

**In use:** "This is an open onshore site — use k = 0.075, not the offshore default, or the wake-loss estimate will run low."

**Common misuse:** applying an offshore wake decay constant to an onshore site (or vice versa) without checking terrain roughness, which shifts the calculated wake loss in the wrong direction.

## Thrust coefficient (Ct)

The dimensionless ratio of the axial thrust force on the rotor to the dynamic force of the free-stream wind on the swept area — the key input to the Jensen/Park wake-deficit equation, distinct from the power coefficient Cp.

**In use:** "Ct near rated is close to 0.8; use that in the wake calc, not the power coefficient — they're different numbers describing different forces."

**Common misuse:** confusing Ct (which drives the wake-deficit calculation) with Cp (which drives the power-output calculation) — the two curves have different shapes and neither substitutes for the other.

## P50 / P90 / P99

**P50** is the AEP value expected to be met or exceeded 50% of the time (the statistical mean case). **P90** and **P99** are the values expected to be met or exceeded 90% and 99% of the time respectively — increasingly conservative figures used for debt-sizing, derived by applying a standard-normal z-value to the stacked uncertainty, not by an arbitrary discount.

**In use:** "The debt facility sizes off P90 for the 10-year term and P99 for the 1-year covenant test — quote both, not just the P50 headline."

**Common misuse:** presenting P50 as if it were a conservative or bankable figure, when it is by definition the value with a roughly 50% chance of falling short in any given year.

## Capacity factor vs. availability

**Capacity factor** is actual (or predicted) energy output divided by the energy the turbine would produce running at rated power continuously for the period — driven by wind resource, wake losses, and downtime combined. **Availability** is the fraction of time the turbine is mechanically ready to operate, independent of whether the wind was blowing — a turbine can hit its contractual availability target while still missing its capacity-factor-implied production target.

**In use:** "Availability came in at 98%, on target — but capacity factor missed because this was a low-wind quarter, not an equipment problem."

**Common misuse:** treating a strong availability number as proof that production targets were met, when a shortfall driven by wind resource or wake losses shows up in capacity factor, not availability.

## Extreme wind speed model (EWM) vs. normal turbulence model (NTM)

**EWM** defines the 50-year (or 1-year) return-period extreme wind condition used in ultimate-load DLCs like 6.1 — a rare, severe event. **NTM** defines the turbulence intensity used for normal power-production DLCs like 1.1/1.2 — the everyday operating turbulence a turbine experiences constantly across its design life.

**In use:** "The tower-base extreme calc uses EWM's Ve50; the blade fatigue analysis runs off NTM's turbulence spectrum across the full wind-speed range — different models for different DLCs."

**Common misuse:** applying the extreme wind speed model's single severe-gust value to a fatigue calculation that actually needs the normal turbulence model's full operating-range spectrum, or vice versa.

## Power curve warranty test (IEC 61400-12-1)

A standardized methodology for measuring a turbine's actual power output against wind speed, binned into discrete wind-speed intervals and corrected to a reference air density, used to verify a manufacturer's guaranteed power curve.

**In use:** "The as-measured curve tracks the guarantee within tolerance up to 9 m/s, then underperforms by 4% in the 10–12 m/s bins — that's the band to escalate to the OEM, not the average across the whole curve."

**Common misuse:** comparing measured and guaranteed output as a single average figure across all wind speeds, which can mask a real shortfall concentrated in one wind-speed band behind an acceptable overall number.
