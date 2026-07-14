# Red flags

### A new mold cut using a shrinkage rate not verified against the current material formulation
- **Usually means:** an outdated or assumed shrinkage rate could produce a systematically undersized (or oversized) final part.
- **First question:** has the current material's actual shrinkage rate been characterized/confirmed, or is a prior formulation's rate being assumed?
- **Data to pull:** current material's shrinkage rate documentation, the rate actually used in mold dimension calculation.

### A finished (fired/cured) part measuring consistently off-target across an entire production run
- **Usually means:** a systematic shrinkage compensation error in the mold itself, rather than a per-part process variation.
- **First question:** is the deviation consistent across all parts from this mold, or does it vary part-to-part?
- **Data to pull:** dimensional data across multiple parts from the same mold, mold's calculated vs. actual green dimension.

### A part demolded on a fixed elapsed-time schedule regardless of actual firmness/moisture condition
- **Usually means:** demolding timing isn't being verified against the material's actual readiness, risking deformation (too early) or sticking/damage (too late).
- **First question:** was a readiness signal (firmness check, moisture measurement) used, or just an elapsed-time rule?
- **Data to pull:** the material's specified readiness criteria, actual method used to determine demold timing.

### A part with uneven thickness or geometry dried/cured at a rate optimized for overall speed
- **Usually means:** the slowest-drying section may not have been accounted for, risking cracking from differential shrinkage stress.
- **First question:** does the drying/curing schedule account for this part's thickest or slowest-drying section specifically?
- **Data to pull:** part geometry/thickness variation, drying schedule basis (fastest-convenient vs. slowest-section).

### Cracking appearing in a specific, consistent location across multiple parts from the same design
- **Usually means:** a geometry-driven drying/curing stress point, likely tied to a thickness transition or the slowest-drying section.
- **First question:** does the crack location correspond to a thickness change or geometric transition in the part?
- **Data to pull:** part geometry, crack location pattern across multiple parts.

### A casting/pour performed without deliberate venting or vibration technique
- **Usually means:** trapped air risk wasn't actively managed, even if the poured material appeared to fully fill the mold.
- **First question:** was venting or vibration technique applied consistently, or was the pour assumed adequate based on visual fill?
- **Data to pull:** pouring/casting process record, any post-cure inspection for voids.

### A structural failure or surface defect discovered after firing/curing that traces to a void or air pocket
- **Usually means:** air entrapment during casting wasn't adequately prevented, and the defect was invisible until this later stage.
- **First question:** does the failure location correspond to a likely air-trap area in the original pour/mold geometry?
- **Data to pull:** the pour/casting record, mold geometry at the failure location.

### A high-use mold not recently verified for dimensional accuracy
- **Usually means:** wear or degradation (moisture absorption in plaster, parting-line wear in rigid molds) may have shifted actual output dimension from original spec.
- **First question:** when was this mold's output last verified against spec, and how many cycles has it run since?
- **Data to pull:** mold usage count/cycles since last verification, dimensional check results if performed.

### A material batch with different moisture content or composition than usual, processed with unchanged timing/technique
- **Usually means:** shrinkage behavior, drying rate, and demold timing may all differ from what was validated for the typical material batch.
- **First question:** has this specific batch's characteristics been checked against what the process was validated for?
- **Data to pull:** current batch's moisture/composition data, the process's validated material specification.

### A part released to the next process stage without post-shrinkage (fired/cured) dimensional verification
- **Usually means:** only the green/wet dimension was checked, which doesn't confirm the final, actually-relevant dimension.
- **First question:** was the part measured after firing/curing, or only before, at the green stage?
- **Data to pull:** dimensional verification record, stage at which measurement was taken.
