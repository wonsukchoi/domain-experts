# Vocabulary

### True position
The GD&T control (symbol ⌖) that defines a cylindrical (for a hole/pin) or spherical tolerance zone around a feature's theoretically exact location, rather than a square zone from ± coordinate dimensioning.
**In use:** "Call out the four mounting holes at true position Ø0.014 at MMC, datums A|B|C, instead of ± dimensioning them off the corner."
**Common misuse:** treating "position" and "location tolerance" as interchangeable with a plain ± dimension — position is always a diameter/zone value referenced to a datum frame, never a plus-or-minus on X and Y independently.

### MMC (Maximum Material Condition)
The condition where a feature contains the most material allowed by its size tolerance — the smallest hole diameter or the largest shaft diameter within tolerance.
**In use:** "At MMC that hole is Ø0.250 — as it grows toward Ø0.252 we pick up 0.002 of bonus position tolerance."
**Common misuse:** assuming MMC always means "tightest" tolerance overall — it means tightest *material*, which for a hole is the smallest diameter, but for a shaft is the largest diameter; the direction flips between internal and external features.

### Bonus tolerance
Additional positional (or other geometric) tolerance a feature earns as it departs from MMC toward LMC, available only when a modifier (Ⓜ) is explicitly called out.
**In use:** "The hole measured Ø0.2515 — that's 0.0015 of departure from MMC, so add 0.0015 of bonus to the stated Ø0.010 position tolerance before rejecting the part."
**Common misuse:** applying bonus tolerance to an RFS-toleranced feature — without the MMC modifier explicitly stated, there is no bonus, regardless of how far the feature is from MMC.

### Datum reference frame (DRF)
The ordered set of three mutually perpendicular planes (primary, secondary, tertiary datums) that fully constrains a part's position and orientation for measurement, established from real features in a specified order.
**In use:** "Reference the DRF as A|B|C — A is the mounting face, B is the two-hole slot, C is the single hole; that's the order the fixture actually constrains it."
**Common misuse:** picking datums for drawing-view convenience (whatever face is facing the camera) rather than matching the actual fixturing or assembly sequence — this produces a DRF the shop can measure to but that doesn't represent how the part functions in the assembly.

### RFS (Regardless of Feature Size)
The default condition for a geometric tolerance when no modifier is stated — the tolerance applies at the feature's actual produced size, with no bonus regardless of how far that size is from MMC or LMC.
**In use:** "That dowel hole needs position at RFS — it's a precision locating feature, we can't let it float extra just because the hole came out a hair oversize."
**Common misuse:** assuming RFS is "the strict one" and MMC is "the loose one" in general — RFS is correct (not merely stricter) whenever the feature's function depends on its produced size, which is a design-intent question, not a default toughness setting.

### Worst-case tolerance stack-up
A tolerance-chain analysis that sums the absolute value of every link's tolerance, producing a range guaranteed to bound 100% of produced assemblies (assuming each link independently stays within its own tolerance).
**In use:** "Worst-case says the float chain runs 0.007 to 0.033 — that's a guarantee, not a probability, so if it fails spec the design fails, full stop."
**Common misuse:** treating a worst-case pass as "wasteful over-tolerancing" and reflexively switching to RSS without process-capability data to justify the statistical assumption RSS depends on.

### RSS (Root-Sum-Square) stack-up
A statistical tolerance-chain analysis that combines link tolerances as the square root of the sum of their squares, producing a tighter (less conservative) range than worst-case, valid when each link's process is independently, normally distributed with demonstrated capability.
**In use:** "RSS gives us 0.013 to 0.027 on the float chain, but only cite it once we've got Cpk data on the housing bore and shaft-length ops."
**Common misuse:** applying RSS to a one-off or low-volume build, or without any process-capability evidence, to make a marginal design "pass" on paper.

### Third-angle projection
The multiview drawing convention (ASME Y14.3M, standard in the US) where each view shows the object as if the viewing plane were between the observer and the object — the top view is placed above the front view.
**In use:** "This is going to a domestic supplier — third-angle, and put the projection symbol in the title block so there's no ambiguity."
**Common misuse:** assuming projection convention is a stylistic choice that doesn't need a symbol on the sheet — omitting the symbol makes the drawing genuinely ambiguous to a reader who doesn't already know which convention the originating company uses.

### First-angle projection
The multiview drawing convention (ISO standard, common outside the US) where the object is placed between the observer and the viewing plane — the top view is placed below the front view, mirrored from third-angle placement.
**In use:** "Customer's in Germany and their PO calls out ISO drawing standards — redo the view layout in first-angle."
**Common misuse:** treating first- and third-angle as producing identical drawings with different labels — the view *placement* on the sheet is genuinely different, not just the symbol.

### Surface finish (Ra)
Arithmetic average roughness of a surface's measured profile, expressed in micrometers (µm) or microinches (µin), specified per surface based on its mating/sealing/sliding function.
**In use:** "Bearing bore gets Ra 0.8 µm reamed — that's a reamer finish, no grinding needed."
**Common misuse:** specifying a uniformly fine Ra across an entire part "to look precise" rather than per-surface by function — each step finer typically adds a distinct secondary operation and its own setup cost.

### Flatness, perpendicularity, runout (form and orientation controls)
GD&T controls on a single feature's shape (flatness — no datum reference) or its relationship to a datum (perpendicularity, runout — datum reference required); runout combines position and form control on a rotating feature in one callout.
**In use:** "Call the bearing journal at 0.001 TIR circular runout to datum A instead of separate roundness and coaxiality tolerances — cheaper to inspect and functionally equivalent here."
**Common misuse:** stacking a separate roundness callout and a separate position callout on a rotating shaft when a single runout callout already controls both, doubling drafting and inspection effort for no added functional control.

### Balloon
A circled reference number on an assembly drawing that identifies a specific part or subassembly, tied one-to-one to a row in the BOM.
**In use:** "Balloon 3 on the exploded view has to match item 3 on the BOM exactly — same part number, same rev."
**Common misuse:** assigning a new balloon number to a second instance of an already-ballooned identical part instead of reusing the same balloon/item number and incrementing only the quantity.

### Bill of Materials (BOM)
The structured parts list tied to an assembly drawing — item number, part number, revision, description, quantity, and material/finish — that purchasing, planning, and receiving use as the assembly's single source of truth for what to buy and build.
**In use:** "Don't hand-edit the drawing's BOM table directly — pull it from the PLM system so the part numbers stay synced with engineering's master record."
**Common misuse:** treating the BOM as a drawing annotation rather than a controlled record — editing quantities or descriptions on the drawing without updating the PLM/PDM system of record, so the two diverge.

### K-factor / bend allowance
The ratio (K-factor) or absolute length (bend allowance/bend deduction) used to compute a sheet-metal part's flat-pattern length from its bent, formed dimensions, dependent on material thickness, bend radius, and material type.
**In use:** "Flat pattern's off by 0.020 across two bends — check whether the K-factor used in the model matches this material's actual thickness and temper."
**Common misuse:** using a generic or default K-factor (e.g., 0.44) across all materials and thicknesses instead of the value specific to the actual gauge and alloy being formed, which shifts the flat-pattern dimension enough to matter on a tight-tolerance part.
