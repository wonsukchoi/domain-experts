# Red flags

### First-off stamped part's angle or dimension deviates from print by an amount consistent with uncompensated springback
- **Usually means:** the die was cut to the print's nominal dimension without a springback allowance applied.
- **First question:** what springback compensation, if any, was applied when this station was cut?
- **Data to pull:** the tool build sheet's compensation log for that specific station.

### Stamped edge burr height exceeds roughly 10% of material thickness
- **Usually means:** punch-die clearance is set too loose or too tight for the material and thickness.
- **First question:** what clearance percentage was actually cut into this die versus the standard for this material/thickness?
- **Data to pull:** the die's measured clearance compared against the tooling specification.

### Progressive die strip tears or distorts between stations
- **Usually means:** insufficient carrier web width left at a specific station.
- **First question:** which station's web width falls below the minimum required for this strip?
- **Data to pull:** the strip layout drawing, checking web width at each station.

### Injection-molded first-shot parts are consistently undersized across all dimensions by a similar percentage
- **Usually means:** shrinkage compensation wasn't applied, or the wrong resin's shrink rate was used, when the cavity was machined.
- **First question:** what shrinkage factor was used for this specific resin when the cavity was cut?
- **Data to pull:** the mold design sheet's shrinkage factor compared against the resin manufacturer's published rate.

### Hardened die component doesn't fit or seat correctly after heat treatment
- **Usually means:** fitting was done against pre-heat-treat dimensions rather than dimensions re-verified after heat treatment.
- **First question:** were critical dimensions actually re-measured after heat treatment before final fitting?
- **Data to pull:** the post-heat-treat inspection report for the affected components.

### Die produces good parts initially, but dimensional drift appears after a large production run
- **Usually means:** cutting-edge wear at the punch or die, not a design flaw in the tool.
- **First question:** how many hits or cycles has this die run since its last sharpening or maintenance?
- **Data to pull:** the die's maintenance and hit-count log.

### Two dies built to the "same" print produce parts with measurably different dimensions
- **Usually means:** different compensation values were used, or assumed, between the two builds.
- **First question:** what compensation values (clearance, springback, shrinkage) does each build's tool sheet actually show?
- **Data to pull:** the tool build sheets for both dies, compared side by side.
