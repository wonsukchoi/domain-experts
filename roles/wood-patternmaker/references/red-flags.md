# Red flags

### A pattern built to the exact target final part dimension with no shrinkage allowance applied
- **Usually means:** the resulting casting will be systematically undersized once the metal shrinks during cooling.
- **First question:** what shrink rule (specific to the actual metal being cast) was applied to this pattern's dimensions?
- **Data to pull:** the metal type being cast, the shrink rule applied (if any), pattern dimensions vs. target part dimensions.

### A shrink rule applied that doesn't match the actual metal being cast
- **Usually means:** different metals shrink at meaningfully different rates, and using the wrong rule produces a systematic dimensional error.
- **First question:** does the shrink rule used correspond to this specific casting alloy, or was a different metal's rule applied?
- **Data to pull:** the actual casting alloy specification, the shrink rule/tool used during pattern construction.

### A pattern surface with no draft angle, or minimal draft, on a surface that will be withdrawn from the mold
- **Usually means:** the pattern may bind and damage the mold on withdrawal.
- **First question:** does every surface in the withdrawal direction have adequate draft per the molding method's requirement?
- **Data to pull:** draft angle measurements on withdrawal surfaces, molding method's minimum draft specification.

### A parting line chosen for geometric simplicity without checking draft direction or core print interaction
- **Usually means:** the pattern may be difficult to mold cleanly, or push unnecessary finishing burden onto the casting.
- **First question:** does the parting line placement account for draft direction and core print access together, or was it chosen independently of those factors?
- **Data to pull:** parting line location, draft direction on both sides of the split, core print locations relative to the parting line.

### A core print sized without reference to the actual core's weight or the casting's pour dynamics
- **Usually means:** risk of core shift during pouring, producing uneven wall thickness around the internal cavity.
- **First question:** was core print size/position calculated from the actual core weight and expected metal pressure, or estimated by appearance?
- **Data to pull:** core weight, core print dimensions, casting's pour rate/pressure characteristics.

### A new pattern released to production without a first-casting dimensional verification
- **Usually means:** a pattern error (shrinkage, draft, core print) wouldn't be caught until many castings have already been produced from it.
- **First question:** was a first casting produced and dimensionally checked against target spec before full production release?
- **Data to pull:** first-casting verification record if one exists.

### A casting consistently measuring undersized or oversized across an entire production run
- **Usually means:** a systematic pattern error (wrong or missing shrink rule), not per-casting process variation.
- **First question:** is the dimensional deviation consistent across castings, or does it vary randomly?
- **Data to pull:** dimensional data across multiple castings from this pattern, the pattern's shrink rule documentation.

### A casting showing uneven wall thickness around an internal cavity
- **Usually means:** the core shifted during pouring, likely from an undersized or mispositioned core print.
- **First question:** does the wall thickness variation pattern match a core-shift signature (thinner on one side, thicker on the opposite)?
- **Data to pull:** wall thickness measurements around the cavity, core print design specifications.

### Mold damage occurring during pattern withdrawal
- **Usually means:** insufficient draft angle on the pattern surfaces being pulled.
- **First question:** does the damaged mold area correspond to a pattern surface with minimal or no draft?
- **Data to pull:** draft angle at the damaged location, molding method's draft requirement.

### A pattern modified or repaired without re-verifying shrinkage allowance and draft on the affected area
- **Usually means:** a repair may have inadvertently altered dimensions or removed draft without those changes being re-checked.
- **First question:** was the repaired area re-measured against the shrink rule and draft requirement after the repair?
- **Data to pull:** repair record, post-repair dimensional/draft check if performed.
