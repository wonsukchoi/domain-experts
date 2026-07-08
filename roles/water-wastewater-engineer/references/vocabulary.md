# Vocabulary

### Firm capacity
The maximum flow a pump station or treatment train can reliably deliver with its largest single unit out of service (N-1). Distinct from installed or nameplate capacity, which assumes everything is running.
**In use:** "Firm capacity is 320 gpm with the lag pump down for maintenance — that's the number that has to beat peak inflow, not the combined nameplate."
**Common misuse:** Generalists quote the combined capacity of all pumps/units running simultaneously as if that's the reliable number, ignoring that redundancy exists precisely because one unit is routinely offline.

### T10
The time for the first 10% of a tracer dose to pass through a contact basin, used as the conservative "actual" contact time for CT disinfection credit — as opposed to the theoretical detention time (volume/flow), which assumes perfect plug flow.
**In use:** "The clearwell's theoretical detention time is 40 minutes, but the tracer study came back with a T10 of 14 minutes — that's what goes in the CT calc."
**Common misuse:** Using volume/flow directly as "contact time" without applying a baffling factor or tracer-derived T10, which overstates disinfection credit and can mask an actual SDWA violation.

### CT
The disinfection credit calculation: chlorine (or other disinfectant) residual concentration (mg/L) multiplied by contact time (minutes), compared against a required CT value from the regulatory table for the target pathogen log-inactivation, pH, and temperature.
**In use:** "We're short on CT at 5°C — either raise the residual to 1.4 mg/L or add contact volume, because 111 mg-min/L doesn't come from wishing."
**Common misuse:** Treating CT as a single number that's either "met" or "not met" without recomputing it for the specific temperature and pH on the day in question — CT requirements rise sharply as water gets colder.

### Surface overflow rate (SOR)
The flow rate divided by a clarifier or sedimentation basin's plan-view surface area (gpd/ft²) — the parameter that actually governs settling performance, independent of tank depth or volume.
**In use:** "Depth doesn't buy you settling capacity here — SOR at peak hour is 1,450 gpd/ft², over the 1,200 design ceiling, regardless of how deep the tank is."
**Common misuse:** Assuming a bigger (deeper) tank automatically fixes a clarifier performance problem, when the limiting parameter is surface area, not volume.

### Weir loading rate
Flow divided by the total length of effluent weir in a clarifier (gpd/lf), checked separately from SOR — a clarifier can pass SOR and still fail on weir loading if the weir is too short, causing high approach velocities that carry floc over.
**In use:** "SOR's fine, but weir loading is 24,000 gpd/lf against a 20,000 ceiling — add a finger weir before the effluent launder."
**Common misuse:** Checking only SOR and assuming that's the complete clarifier hydraulic check.

### Hydraulic loading rate (HLR) vs. organic loading rate (OLR)
HLR is a flow-per-area parameter (gpm/ft² for filters); OLR is a mass-per-volume-per-time parameter (lb BOD/1,000 ft³/day for trickling filters and similar fixed-film processes). They govern different failure modes and are never interchangeable.
**In use:** "The trickling filter's hydraulically fine, but OLR is 340 lb BOD/1,000 ft³/day — way past high-rate range — the media's going septic, not overflowing."
**Common misuse:** Checking only the hydraulic (flow) capacity of a biological process and assuming that's sufficient, when the organic (mass) loading is the actual limiting factor.

### Peaking factor (PF)
The ratio of a peak flow condition (usually peak hour) to average flow, used to size hydraulic components from a metered or projected average. Derived from formulas like Harmon's (`1 + 14/(4+√P)`, P in thousands of population) or Babbitt's (`5/P^0.2`), or from a utility's own metered peak/average ratio.
**In use:** "Don't use the citywide PF of 2.2 for this infill parcel — small service areas peak harder; Harmon gives 3.4 at this population."
**Common misuse:** Applying a large system's peaking factor to a small subdivision or vice versa — PF is population-scale-dependent, and using the wrong scale under- or over-sizes the pump station.

### Wet well cycling / minimum cycle time
The regulatory/manufacturer-driven minimum time allowed between consecutive pump starts, set by motor horsepower to prevent thermal damage from frequent starting — the constraint that actually sizes a pump station's active storage volume.
**In use:** "It's a 20 hp motor, so minimum cycle time is 13 minutes — the wet well has to hold enough active volume for that, not whatever felt like a safe buffer."
**Common misuse:** Sizing wet well volume as a generic "X minutes at average flow" rule of thumb instead of applying the pump-specific formula (V = Qp·t/4) at the worst-case inflow condition (Qp/2).

### Class A / Class B biosolids
EPA 40 CFR 503 pathogen-reduction classifications for treated sewage sludge. Class B meets a lower pathogen-reduction bar and carries land-application site restrictions (public access limits, crop harvest delays); Class A meets a stricter bar and can be used without those restrictions, including sale as a soil product.
**In use:** "We're Class B today — going to Class A means adding a thermal or lime-stabilization step, and that's a market decision, not something the current permit requires."
**Common misuse:** Treating Class A as an automatic treatment upgrade goal rather than a cost/market tradeoff — Class B is fully compliant and often the more economical, appropriate choice when land application with normal restrictions is viable.

### Turndown ratio
The ratio between a piece of equipment's maximum and minimum controllable output (e.g., a chemical feed pump's max dose rate divided by its min dose rate) — the parameter that determines whether equipment sized for peak/max-day conditions can also operate correctly at minimum flow.
**In use:** "The metering pump's turndown is only 10:1 — sized for max-day dose, it can't get low enough for minimum-hour flow without overdosing."
**Common misuse:** Sizing chemical feed or other dosing equipment only for the maximum design condition without checking whether it can also hit the correct dose at the minimum flow condition.

### Solids retention time (SRT) / sludge age
The average time solids (biomass) remain in a biological treatment process — distinct from hydraulic retention time (how long the water itself is in the tank). SRT governs nitrification, settleability, and process stability; it doesn't change instantaneously when flow changes.
**In use:** "Flow doubled overnight during the storm, but SRT is still 8 days — the biomass hasn't had time to respond, that's why we're not seeing a nitrification crash yet."
**Common misuse:** Assuming a biological process responds to a flow or loading change on the same timescale as a purely hydraulic system — SRT changes over days, not hours.

### Primacy agency
The state (or, rarely, EPA directly) agency delegated authority to enforce the Safe Drinking Water Act and administer the NPDES program within that state — the actual plan-review and permitting authority, as opposed to EPA's national regulations, which set the floor.
**In use:** "EPA's CT table is the federal floor — check the primacy agency's own manual, because this state requires an extra 10% CT safety margin on top."
**Common misuse:** Citing only the federal (40 CFR) requirement and assuming it's binding as written, without checking the state primacy agency's own adopted (and often stricter) manual.

### Force main vs. gravity main
A force main carries wastewater under pressure from a pump station's discharge; a gravity main relies on pipe slope alone. They have different design bases entirely — force mains are sized by pump curve/friction loss and velocity, gravity mains by Manning's equation and minimum slope for self-cleansing velocity at partial flow depths.
**In use:** "Don't apply Manning's n to the force main sizing — it's pressure flow past the pump, use Hazen-Williams and check against the pump curve."
**Common misuse:** Applying gravity-main design methodology (Manning's equation, partial-flow depth) to a force main, or vice versa — the two pipe types are governed by entirely different hydraulic equations.

### Wire-to-water efficiency
The overall efficiency of a pump system from electrical input (wire) to hydraulic output (water), combining motor efficiency and pump hydraulic efficiency — used to convert a hydraulic horsepower requirement into an actual motor size and expected energy cost.
**In use:** "At 65% wire-to-water, that 3.1 hydraulic hp needs roughly 4.8 hp of input — round up to the standard 5 hp motor size."
**Common misuse:** Sizing a motor directly off the hydraulic horsepower number without applying the wire-to-water efficiency factor, undersizing the motor.

### Self-cleansing velocity
The minimum flow velocity in a pipe (gravity or force main) needed to keep solids in suspension and prevent settling — commonly cited as ≥2 ft/s for force mains, with a separate (slope-based) criterion for gravity mains.
**In use:** "Lead-pump-alone flow gives 1.6 ft/s in the force main — below self-cleansing, we'll get solids deposition and eventually odor complaints even though the pipe has plenty of hydraulic capacity."
**Common misuse:** Checking self-cleansing velocity only at the combined lead+lag pump flow, missing a low-velocity condition that occurs during the more common single-pump operating mode.
