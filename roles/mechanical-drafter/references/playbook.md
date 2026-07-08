# Mechanical drafting playbook

Filled formulas and table structures for tolerance stack-ups, GD&T symbol selection, BOM/balloon structure, and surface-finish-to-process mapping.

## Tolerance stack-up worksheet (worst-case and RSS side by side)

Structure for any linear dimension chain feeding a functional gap, interference, or clearance requirement. Sign convention: dimensions that add to the gap are `+`, dimensions that subtract from it are `−`.

| Link | Description | Nominal (in) | Tol (±in) | Sign | Contribution | Tol² |
|---|---|---|---|---|---|---|
| L1 | Housing bore depth | 1.750 | 0.005 | + | +1.750 | 0.000025 |
| L2 | Bearing 1 width | 0.375 | 0.002 | − | −0.375 | 0.000004 |
| L3 | Bearing 2 width | 0.375 | 0.002 | − | −0.375 | 0.000004 |
| L4 | Shaft shoulder length | 0.980 | 0.004 | − | −0.980 | 0.000016 |
| **Sum / RSS** | | **Nominal = 0.020** | **WC = 0.013** | | | **Σ = 0.000049** |

- **Nominal** = signed sum of the nominal column = 1.750 − 0.375 − 0.375 − 0.980 = 0.020.
- **Worst-case (WC) tolerance** = sum of the absolute tolerance column (sign-independent) = 0.005 + 0.002 + 0.002 + 0.004 = 0.013. Worst-case range = nominal ± WC.
- **RSS tolerance** = √(Σ tol²) = √0.000049 = 0.007. RSS range = nominal ± RSS. Valid only when each link's process has demonstrated Cpk ≥ 1.33 (or equivalent process-capability evidence) — cite the specific Cpk study, not just "statistical tolerancing."
- **Leverage** of a link = its tolerance ÷ the WC total. In the table above, L1 carries 0.005/0.013 = 38% of worst-case tolerance budget — the highest-leverage link, and the first candidate to tighten if the stack fails spec.
- **Fallback order when a stack fails spec:** (1) tighten the highest-leverage link if the resulting tolerance is still achievable on the existing process, (2) redistribute tolerance across two mid-leverage links rather than over-tightening one, (3) change the datum/dimensioning scheme to remove a link from the chain entirely (e.g., dimension both bearing widths from a single reference instead of stacking two separate ± callouts), (4) escalate to the design engineer that the functional spec itself needs to widen — in that order, not skipped.

## GD&T symbol and modifier selection table

| Interface type | Primary control | Modifier default | Typical value range | Notes |
|---|---|---|---|---|
| Bolted flange, clearance-fit hole pattern | Position (⌖) | MMC | Ø0.010"-Ø0.020" at MMC | Bonus tolerance grows as hole departs from MMC toward LMC; use a functional (fixed) gage to verify. |
| Dowel pin / precision locating hole | Position (⌖) | RFS | Ø0.001"-Ø0.005" RFS | No bonus tolerance — locating accuracy must hold regardless of produced size. |
| Mounting face flatness | Flatness (⏥) | N/A (form tolerances take no modifier) | 0.001"-0.005" per 4" of face | Tighter than the general tolerance block when the face seats a seal or bearing race. |
| Shaft perpendicular to a mounting face | Perpendicularity (⊥) | MMC if the shaft is a clearance pin/hole feature; RFS if it's the functional axis itself | 0.001"-0.010" | Reference the primary datum face (A) directly. |
| Rotating shaft / bearing journal | Circular runout (↗) | N/A | 0.0005"-0.002" TIR | Controls both circularity and coaxiality to the datum axis in one callout — cheaper to verify than separate roundness + position calls. |
| Sealing groove concentric to bore | Total runout (↗↗) or Position | RFS | 0.002"-0.005" | Total runout when the groove's full surface must track the axis (dynamic seal); position when only the groove's centerline location matters (static seal). |

**Datum reference frame order (A\|B\|C):** primary datum (A) removes 3 degrees of freedom, typically the largest flat mounting face, established first from how the part sits in the assembly and in the fixture. Secondary (B) removes 2 more, typically a hole or pin that sets rotation. Tertiary (C) removes the last 1, typically a slot or second hole preventing the last rotational freedom. Pick datums that match the actual assembly/fixturing sequence — a datum scheme that doesn't match how the part is held on the mill produces a drawing the shop can't actually hold to.

## BOM and balloon structure

| Item | Part Number | Rev | Description | Qty | Material/Finish |
|---|---|---|---|---|---|
| 1 | 4471-010 | B | Shaft, pump drive | 1 | 17-4PH SS, black oxide |
| 2 | 4471-020 | A | Bearing, ball, 6205-2RS | 2 | Per mfr spec |
| 3 | 4471-031 | C | Housing, pump | 1 | 356-T6 aluminum, as-cast + machined |
| 4 | 4471-040 | A | Retaining ring, external, 0.062" | 1 | Spring steel, phosphate |
| 5 | MS35338-46 | — | Lock washer, #10 | 4 | Steel, zinc plated |

- **Item number ≠ balloon position.** Every balloon on the assembly-drawing view points to exactly one item number; two identical bearings at different assembly locations still get one item row (item 2, qty 2) — a duplicate item number for the same part number at a second location breaks the BOM's row-per-part-number rule.
- **Mechanically identical parts with different finish get separate item numbers and separate part numbers** (e.g., a black-oxide vs. zinc-plated version of the same machined part), never one item number with a finish note in the description column — a note is easy to miss at receiving inspection; a distinct part number is not.
- **Revision increments the letter (A→B→C), never the base part number**, unless the change breaks form/fit/function interchangeability with prior-rev stock — in that case the base number itself increments (as in item 3 above: 4471-030 → 4471-031) so old and new stock can't be mixed silently.
- **Off-the-shelf hardware** (item 5) carries the vendor/standard part number (MS, ANSI, DIN) directly, no internal part number — internal numbering is reserved for parts the company designs or specifies to a print.

## Surface finish (Ra) by process and function

| Surface function | Ra target | µin equivalent | Typical process |
|---|---|---|---|
| Static, non-mating (bracket face, cosmetic cover) | 3.2-6.3 µm | 125-250 µin | As-milled, as-turned, as-cast |
| Bolted static joint face | 1.6-3.2 µm | 63-125 µin | As-milled or as-turned, no secondary op |
| Press-fit bearing bore / clearance rotating fit | 0.8-1.6 µm | 32-63 µin | Reamed or bored |
| Dynamic sliding seal (rod seal, O-ring bore) | 0.2-0.4 µm | 8-16 µin | Ground, honed, or superfinished |
| Gasket sealing face (static, fluid) | 0.8-1.6 µm | 32-63 µin | Milled with fine feed or ground, per gasket manufacturer's spec |

Each step down the table typically adds one secondary operation and its own setup — do not specify a finer Ra than the function requires; it is the single most common source of unnecessary machining cost on an otherwise correctly toleranced part.
