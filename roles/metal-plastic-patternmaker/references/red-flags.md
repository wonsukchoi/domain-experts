# Red flags

### A CNC-programmed pattern dimension set to the literal target casting dimension, with no shrink rule applied
- **Usually means:** machining precision is being conflated with dimensional correctness — the casting will shrink by the metal's characteristic rate regardless of how precisely the pattern was cut.
- **First question:** was the metal's shrink rule applied to the programmed dimension before machining, or was the pattern cut to the literal target?
- **Data to pull:** the metal type being cast, the shrink rule applied (if any), pattern's programmed vs. target dimensions.

### A high-volume production pattern built from a material/construction not matched to its actual anticipated volume
- **Usually means:** either an overbuilt pattern for a short run (wasted cost) or an inadequate pattern for a long run (premature wear/failure).
- **First question:** does the pattern's material and construction match the actual planned production volume for this tooling?
- **Data to pull:** anticipated production volume, pattern material/construction specification.

### Multiple patterns on a matchplate verified individually without checking their coordinated spacing/alignment
- **Usually means:** each pattern may be dimensionally correct alone while still misaligned relative to the others as a set.
- **First question:** has spacing and alignment been verified across the full matchplate layout, or only per individual pattern?
- **Data to pull:** matchplate layout coordination check results, individual pattern dimensional data.

### A pattern's draft/parting line designed without confirming compatibility with the specific automated molding machine in use
- **Usually means:** a draft standard appropriate for hand-molding may not suit the automated machine's actual pulling mechanism and cycle requirements.
- **First question:** does the pattern's draft angle and parting line design match this specific molding machine's documented requirements?
- **Data to pull:** the molding machine's pulling mechanism specification, pattern's draft/parting line design.

### A metal/plastic pattern in long-term production use with no periodic dimensional re-verification
- **Usually means:** an assumption that metal durability eliminates wear risk, when repeated clamping/handling can still cause gradual dimensional drift.
- **First question:** when was this pattern's dimensional accuracy last verified, and has a periodic re-check schedule been established?
- **Data to pull:** pattern re-verification log, production volume/cycles since last check.

### Castings from a mature, long-running pattern showing a dimensional trend developing over time
- **Usually means:** wear-driven pattern drift, even in a metal/plastic pattern previously assumed durable and stable.
- **First question:** does casting dimension data show a trend correlating with cumulative production volume on this pattern?
- **Data to pull:** dimensional trend data across the pattern's production history, cumulative cycle count.

### A new pattern released to production without a first-casting dimensional trial
- **Usually means:** a shrinkage or design error wouldn't be caught until a significant production commitment has already been made against this tooling.
- **First question:** was a first-casting trial produced and dimensionally verified before full production release?
- **Data to pull:** first-casting trial record if one exists.

### A pattern modified or repaired without re-verifying shrink rule application and matchplate coordination on the affected area
- **Usually means:** a repair may have inadvertently altered dimensions or affected coordination with other patterns on the same plate.
- **First question:** was the repaired area re-measured against the shrink rule and matchplate coordination requirements after the repair?
- **Data to pull:** repair record, post-repair verification if performed.

### Castings consistently mis-sized across a production run using an established, previously validated pattern
- **Usually means:** either the pattern itself has drifted from wear, or something about the current casting process (metal composition, pour parameters) has shifted from what the pattern was validated for.
- **First question:** does the deviation trace to the pattern's own dimensions, or to a process change on the casting side?
- **Data to pull:** direct pattern dimension re-check, any recent casting process changes.

### A pattern's shrink rule based on a general metal category (e.g., "steel") rather than the specific alloy being cast
- **Usually means:** shrinkage rates vary meaningfully within a metal category by specific alloy composition, and a generic category rate may not match the actual alloy.
- **First question:** does the shrink rule used correspond to this specific alloy's characterized rate, or a general category assumption?
- **Data to pull:** the specific alloy being cast, its characterized shrinkage rate vs. the rate applied.
