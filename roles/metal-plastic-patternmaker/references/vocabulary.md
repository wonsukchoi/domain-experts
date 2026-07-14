# Vocabulary

### Matchplate
A mounting plate holding multiple patterns (often for different parts, or multiples of the same part) in a fixed, coordinated arrangement, used in automated or semi-automated molding to produce multiple castings per molding cycle.
**In use:** "Six patterns on this matchplate — checking their coordinated spacing as a set, not just verifying each one alone."
**Common misuse:** Verifying each pattern on a matchplate individually without checking their relationship to each other — patterns can each be individually dimensionally correct while still misaligned in spacing or orientation relative to the rest of the plate, causing molding or gating problems that only appear when they're used together.

### Flaskless molding
An automated molding process that forms and handles sand molds without a separate flask (frame), typically using matchplate-mounted patterns and requiring specific draft/pulling force compatibility from the pattern.
**In use:** "This pattern's draft needs to work with the flaskless machine's pulling force spec, not just a general hand-molding draft standard."
**Common misuse:** Designing pattern draft and parting line to a generic standard without checking the specific automated molding equipment's actual requirements — flaskless and other automated molding machines can have different tolerance for friction/binding than a skilled hand molder who could otherwise compensate.

### Machining precision (vs. dimensional correctness)
The accuracy with which a CNC or other machining process hits its programmed target dimension, distinct from and independent of whether that programmed target is itself the correct dimension for the intended outcome.
**In use:** "The machine cut this bore to within half a thousandth of the program — but if the program didn't include the shrink allowance, that precision was aimed at the wrong number."
**Common misuse:** Assuming high machining precision substitutes for or implies correct dimensional planning — a CNC machine executing a wrong program with perfect precision still produces a wrong part, since precision and correctness of the target are entirely separate questions.

### Pattern durability (material/volume matching)
The relationship between a pattern's construction material (wood, metal, plastic) and its expected wear life, which should be matched to the actual anticipated production volume rather than defaulted to either extreme.
**In use:** "Fifty thousand units justifies the machined aluminum pattern cost — for a two-hundred-unit run, we'd use wood instead."
**Common misuse:** Defaulting to a single pattern material choice regardless of production volume — building an expensive, durable pattern for a short run wastes cost, while using an inadequate pattern for a high-volume run risks premature wear and dimensional drift mid-production.

### Coordinated tolerance (multi-pattern layout)
The dimensional accuracy requirement for the relative positioning of multiple patterns on a shared tooling plate, distinct from each pattern's own individual dimensional tolerance.
**In use:** "Each pattern's within its own tolerance, but the coordinated spacing tolerance across the plate is a separate check we still need to run."
**Common misuse:** Treating individual pattern tolerance and multi-pattern coordinated tolerance as the same check — a matchplate can pass every individual pattern's inspection while still failing a coordinated spacing/alignment requirement that only shows up when checking the patterns as a complete set.

### Pattern wear (metal/plastic, long-term)
Gradual dimensional degradation of a metal or plastic pattern from repeated molding-cycle handling and clamping forces over its production life, occurring more slowly than wood pattern wear but not eliminated by the more durable material.
**In use:** "We're past twenty-five thousand cycles on this pattern — due for a re-verification even though it's aluminum, not wood."
**Common misuse:** Assuming a metal or plastic pattern's greater durability means it never needs re-verification over its production life — wear still accumulates, just at a slower rate and longer interval than a wood pattern would require.

### First-casting trial (metal/plastic pattern)
The practice of producing and dimensionally verifying an initial casting from a new metal/plastic pattern before releasing it for full production volume, particularly important given the larger production commitment these patterns typically represent.
**In use:** "First-casting trial confirms the bore lands at spec — clearing this pattern for the full fifty-thousand-unit run now, not before."
**Common misuse:** Skipping or abbreviating first-casting verification because the pattern was CNC-machined to tight tolerance — machining precision doesn't confirm the casting result, since shrinkage and other casting-specific factors only show up once metal is actually poured and cooled.

### Production volume matching (tooling investment)
The principle that tooling investment (pattern material, construction robustness, precision) should scale with the actual planned production quantity, since both under- and over-investment carry real costs.
**In use:** "We're not building a fifty-thousand-unit-grade pattern for a two-hundred-piece prototype run — that's the wrong tool for this volume."
**Common misuse:** Applying a single default tooling standard regardless of actual production volume — either extreme (overbuilding for a short run, underbuilding for a long one) wastes resources or creates production risk relative to what the volume actually requires.
