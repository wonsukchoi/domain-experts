# Vocabulary

### Turn count
The exact number of wire wraps in a coil, which directly determines inductance and transformer voltage ratios — a value that must be exactly correct, since inductance scales with the square of turn count.
**In use:** "Inductance is off by two percent — that tracks with roughly a one percent turn-count discrepancy, given the squared relationship."
**Common misuse:** Assuming a small turn-count error produces a proportionally equal-sized electrical error — because inductance depends on the square of turn count, a small count deviation can produce a noticeably larger inductance deviation than intuition suggests.

### Turn counter cross-check
The practice of periodically verifying a mechanical or electronic turn counter's accuracy against an independent counting method, catching counter slip or drift before it affects a full winding.
**In use:** "Cross-checked the counter at the 250 mark against the layer-count calculation — caught a two-turn discrepancy before it compounded to the full 500."
**Common misuse:** Trusting a turn counter's display without periodic independent verification — mechanical counters can develop a slip or wear-related drift that produces a systematically wrong count while the display continues to show the expected value.

### Wire tension (winding)
The controlled pulling force applied to wire during coil winding, which must stay within a specified range for the wire gauge and insulation type to avoid both insulation damage (too tight) and loose windings (too loose).
**In use:** "Tension's set to spec for this 28-gauge magnet wire — not just 'feels about right.'"
**Common misuse:** Setting wire tension by feel or general experience rather than to the specific range appropriate for the wire gauge and insulation being wound — different wire gauges and insulation types have different tolerance for tension, and a setting that's fine for one can damage or under-tension another.

### Insulation nick (magnet wire)
A scratch or break in a wire's enamel insulation coating, often occurring during winding from contact with guides or tensioning equipment, that creates a latent short-circuit risk between adjacent turns.
**In use:** "That hi-pot failure traces to an insulation nick from the wire guide — not a material defect in the wire itself."
**Common misuse:** Assuming insulation damage would be visible on inspection or would immediately cause a detectable short — a nick can be invisible to visual inspection and not cause an immediate failure, only manifesting as a latent weak point that fails later under electrical or thermal stress.

### Hi-pot (high-potential) test / dielectric test
An electrical test applying a high voltage across a coil's insulation to verify it can withstand the voltage without breaking down, used to detect insulation defects not visible by inspection.
**In use:** "Hi-pot test at the specified voltage and duration — that's what actually confirms insulation integrity, not looking at the wire."
**Common misuse:** Treating hi-pot testing as optional for a coil that "looks fine" — insulation integrity specifically requires this electrical verification, since visual inspection can't detect the kind of insulation defect the test is designed to catch.

### LCR meter
A test instrument measuring inductance (L), capacitance (C), and resistance (R), used to verify a wound coil's actual electrical characteristics against specification.
**In use:** "LCR meter shows twelve-point-oh-five millihenries — within our twelve-plus-or-minus-five-percent spec."
**Common misuse:** Relying on resistance measurement alone to characterize a coil's electrical health — inductance is the parameter most directly affected by turn count and winding pattern, and skipping its measurement misses the characteristic most likely to reveal a winding error.

### Winding pattern (layering)
The specified sequence and arrangement of wire layers in a coil, affecting mechanical stability and electrical characteristics like inter-turn capacitance and spacing consistency.
**In use:** "Layering's specified in a particular sequence — deviating from it, even with the right total turn count, can change the coil's capacitive behavior."
**Common misuse:** Treating winding pattern as a cosmetic or convenience-driven choice as long as total turn count is correct — layering pattern affects real electrical characteristics (capacitance, spacing consistency) independent of turn count.

### Magnet wire
Insulated copper (or aluminum) wire used in coil winding, coated with a thin enamel insulation layer rather than a thicker jacket, making it more susceptible to insulation damage from handling than typical hookup wire.
**In use:** "This is magnet wire, not standard hookup wire — the insulation's much thinner and nicks a lot more easily."
**Common misuse:** Handling magnet wire with the same technique used for more robustly insulated wire types — magnet wire's thin enamel coating is more vulnerable to nicking from guides, tensioners, and handling than thicker-jacketed wire.

### Layer-count calculation (independent turn verification)
A method of verifying total turn count by calculating layers × turns-per-layer from the winding specification, used as an independent cross-check against a mechanical/electronic counter's reading.
**In use:** "Counter says 250 — layer-count calculation from the winding spec says 248. That two-turn gap is real, not a rounding difference."
**Common misuse:** Treating a mechanical counter's reading as the sole source of truth for turn count without an independent method to catch a developing discrepancy — the layer-count calculation exists specifically to catch counter errors that would otherwise go undetected.
