# Vocabulary

### Case depth
The depth to which a hardening treatment, like carburizing, has altered a part's surface layer composition and hardness, governed by a time-temperature diffusion relationship rather than time alone.
**In use:** "Case depth target's 1.0mm — that's a time calculation from the diffusion constant, not a doubled-time guess."
**Common misuse:** Assuming case depth scales linearly with treatment time, when it actually follows a square-root-of-time relationship at a given temperature.

### Carburizing
A case-hardening process that diffuses carbon into a steel's surface layer at elevated temperature, followed by quenching and tempering.
**In use:** "Carburizing at 925°C for 4 hours to hit the 1.0mm case depth target on this alloy."
**Common misuse:** Treating carburizing time as the sole and linear determinant of case depth, ignoring the actual diffusion relationship and temperature's role.

### Quench rate
The speed at which a heated part cools during quenching, which determines the resulting microstructure and hardness, and must be matched to the specific alloy's hardenability.
**In use:** "This alloy needs a faster quench rate than the last one — oil won't cool it fast enough to hit target hardness."
**Common misuse:** Selecting a quenchant by default habit or "faster is always better" assumptions, rather than matching it to the specific alloy's documented cooling-rate requirement.

### Hardenability
A specific alloy's inherent capacity to be hardened to a given depth or degree by a given quench rate, distinct from hardness itself.
**In use:** "Hardenability's lower on this alloy — even a fast quench won't get full hardness through the thicker sections."
**Common misuse:** Confusing hardenability, how deep or well an alloy can harden under a given quench, with hardness, the actual resulting property, assuming any alloy will respond identically to the same quench method.

### Tempering
A controlled reheat after hardening that reduces brittleness in exchange for some hardness, tuned to a target hardness/toughness balance for the application.
**In use:** "Tempered at 400°F for this application — that's the balance point between hardness and the toughness this part needs in service."
**Common misuse:** Treating hardening alone as a complete process, or applying a generic tempering step without tuning temperature and time to the specific target balance the application requires.

### Quench delay
The elapsed time between removing a part from the austenitizing furnace and immersing it in the quenchant, which affects the part's actual temperature and transformation state at the moment quenching begins.
**In use:** "Quench delay's tracked at under 10 seconds for this alloy — any longer and we're risking partial transformation before it even hits the tank."
**Common misuse:** Not tracking or controlling quench delay, allowing inconsistent partial cooling or transformation to occur before quenching actually starts.

### Distortion (heat treatment)
Warping or dimensional change in a part caused by uneven heating/cooling during heat treatment, influenced by part geometry, quench method, and fixturing.
**In use:** "Fixtured this part for quench specifically because of its asymmetric section thickness — free-quenching it would risk warping."
**Common misuse:** Addressing distortion reactively after a part comes out warped, rather than planning fixturing and orientation proactively based on the part's known geometry and distortion risk.

### Austenitizing
Heating steel to a temperature at which its microstructure transforms to austenite, the starting point before quenching to form martensite.
**In use:** "Austenitizing hold time and temperature are specific to this alloy's composition — not just 'hot enough.'"
**Common misuse:** Assuming any sufficiently high temperature achieves proper austenitizing, without verifying the specific temperature and hold time needed for this alloy's composition.

### Rockwell / Brinell hardness testing
Standardized methods for measuring a material's hardness via indentation, used to verify heat-treated parts against a target hardness specification.
**In use:** "Rockwell C reading confirms hardness on the actual part — that's what clears it, not the recipe log alone."
**Common misuse:** Releasing a heat-treated part based on the process recipe having been followed rather than an actual hardness test result at a representative location on the part.

### Diffusion constant (case hardening)
An empirically-verified process-specific value relating case depth to the square root of treatment time at a given temperature, used to calculate required time for a target depth.
**In use:** "Diffusion constant's verified at k=0.5 for this exact furnace and alloy — that's what the time calculation is built on."
**Common misuse:** Assuming a diffusion constant from a different furnace, alloy, or temperature applies directly to the current process, rather than verifying it empirically for this specific combination.
