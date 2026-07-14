# Red flags

### A pattern piece nested with a rotation different from the specified grain direction
- **Usually means:** yield optimization is being prioritized over the grain constraint, risking a functionally or aesthetically wrong part.
- **First question:** does this piece's orientation match the template's specified grain direction, or was it rotated to fit more efficiently?
- **Data to pull:** the template's grain direction specification, the actual layout orientation used.

### A pattern piece positioned over or partially overlapping a visible material defect
- **Usually means:** yield was prioritized over defect avoidance, risking a part that fails later at the flaw location.
- **First question:** does this defect fall within a non-critical/hidden area the design specifically allows, or is it in a structural/visible area?
- **Data to pull:** the flaw's location and size, the product design's defect-tolerance zones if any exist.

### Cut edges showing dragging, fraying, or slight distortion rather than a clean line
- **Usually means:** blade sharpness has degraded enough to affect cut quality, even if individual pieces still look superficially acceptable.
- **First question:** when was the blade last sharpened or replaced, and does current cut quality meet the standard?
- **Data to pull:** blade service log, dimensional measurement of recent cut pieces against spec.

### A cutting template in extended use with no recent verification against the master pattern
- **Usually means:** the template may have worn or shifted, setting an inaccurate ceiling on every part cut from it.
- **First question:** when was this specific template last verified against the master pattern?
- **Data to pull:** template verification log, actual template dimensions vs. master pattern.

### A stretch or bias-cut material piece measured immediately after cutting, while still under handling tension
- **Usually means:** the measured dimension may not reflect what the piece will actually be once it relaxes to its natural state.
- **First question:** was the piece allowed to relax before final measurement, or measured while still under tension from layout/handling?
- **Data to pull:** the material's known relaxation behavior, timing of measurement relative to handling.

### Yield significantly below expectation for a given material lot
- **Usually means:** either an unusual concentration of natural defects in this specific lot, or a process/layout inefficiency — needs distinguishing.
- **First question:** does this lot show more defects than typical, or is the cutter's nesting approach less efficient than standard?
- **Data to pull:** defect count/density for this lot vs. historical average, layout efficiency data.

### A finished, assembled product showing mismatched panel appearance or drape across otherwise identical parts
- **Usually means:** one or more panels may have been cut off-grain relative to the others.
- **First question:** do all panels in this product share the same grain orientation, verified against the original cutting layout?
- **Data to pull:** cutting layout records for the specific panels involved, grain direction specification.

### A part failing in service at a location later traced to a hide/material flaw
- **Usually means:** a defect was cut into a functional area rather than routed around during layout.
- **First question:** does the failure location correspond to a known or visible defect that existed in the material before cutting?
- **Data to pull:** the original cutting layout/inspection record for that specific part, if traceable.

### A cutter working from a template without checking its version against the current job specification
- **Usually means:** an outdated or superseded template may be in use.
- **First question:** does the template in hand match the current, active version specified for this job?
- **Data to pull:** template version control record, job specification's referenced template version.

### Blade replaced on a fixed calendar schedule regardless of actual cut quality or usage volume
- **Usually means:** the replacement schedule may not match actual wear, either replacing too early (waste) or too late (quality risk) depending on actual usage intensity.
- **First question:** does actual cut quality data support the current replacement interval, or would usage-based tracking be more appropriate?
- **Data to pull:** cut quality trend data relative to blade age/usage, current replacement schedule basis.
