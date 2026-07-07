# Playbook

Filled procedures a freight/material-mover crew or dock lead actually runs, with real numbers plugged in.

## 1. Axle-weight distribution check (beam approximation)

**Formula (stated heuristic, not exact tractor/fifth-wheel dynamics):**

```
Tandem share of a load  = w × (x / L)
Kingpin share of a load = w × (1 − x / L)
```

Where *w* is the piece's weight, *x* is its distance from the kingpin, and *L* is the kingpin-to-trailer-tandem centerline span (commonly 38–41 ft on a standard van or flatbed). Kingpin share transfers almost entirely to the tractor's drive-tandem axle group, since the fifth wheel sits over it.

**Legal limits (23 CFR 658.17, Federal Bridge Gross Weight Formula, and standard federal axle limits):** 20,000 lb single (steer) axle, 34,000 lb per tandem axle group, 80,000 lb gross combination weight — each checked independently; passing gross weight does not imply passing axle-group weight.

**Worked table — 30,000 lb of freight, two layouts, same trailer (L = 38 ft):**

| Layout | Trailer tandem total | Drive tandem total | Gross combination weight | Result |
|---|---|---|---|---|
| Rear-clustered (positions 30–37.5 ft) | 36,171 lb | 14,829 lb | 61,000 lb | Tandem over 34,000 lb limit — gross still legal |
| Evenly spread (positions 3–33 ft) | 23,211 lb | 27,789 lb | 61,000 lb | Both axle groups under limit |

**Field procedure:**

1. Pull piece weights and plan positions from the manifest before the first piece is loaded, not after.
2. For each piece, compute its tandem share using the beam formula and running-sum it against the 34,000 lb tandem limit and the kingpin/drive-tandem share against the same limit.
3. If a layout driven by delivery sequence (last-on-first-off) pushes one axle group over its limit, redistribute positions first — spread weight toward the opposite end — before considering a tandem-slide adjustment.
4. If redistribution alone can't resolve it (freight genuinely must stay where the stop sequence puts it), slide the trailer's tandem axle group to shift the split, then physically confirm the slide pins are fully seated in matching holes before the tractor moves — an unpinned slide is a rolling hazard the axle math didn't catch.
5. Where a certified scale is available before dispatch, weigh each axle group and reconcile against the plan; log any deviation greater than ~500 lb per group as a plan-versus-actual gap for the next load.

## 2. Dock leveler / dockboard safety-lock verification

**Before any wheeled equipment (pallet jack, forklift) crosses:**

1. Confirm the leveler's rated capacity (marked per ANSI/MH14.1, typically 20,000–45,000 lb for mechanical/hydraulic dock levelers) covers the loaded equipment's gross weight — equipment plus freight, not freight alone.
2. Lower/extend the leveler onto the trailer bed and confirm the mechanical or hydraulic lock (lip lock, safety leg, or maintenance strut) is engaged — visually, and by the audible click or hydraulic-lock indicator the unit is built with, not by assuming stability because the plate isn't shifting under foot traffic.
3. Confirm the trailer itself is restrained (wheel chocks or an engaged ICC bar / trailer-restraint dock lock) before any equipment enters it — a leveler crossing doesn't substitute for trailer restraint, and an unrestrained trailer can creep away from the dock under load.
4. If the gap between dock and trailer bed exceeds the leveler's rated span or the leveler shows visible deck damage, stop and escalate rather than bridging the excess gap with dunnage or improvised material.
5. Re-verify lock engagement after any leveler cycling (raised and lowered again mid-load) — a lock that engaged on first extension is not guaranteed to re-engage identically.

## 3. Blocking, bracing, and tiedown sizing for irregular freight

**Two independent rules, both must pass (49 CFR 393.106/393.110):**

- **Aggregate working-load-limit (WLL) rule:** the sum of the WLL of all tiedowns/blocking devices securing a piece (or group secured as a unit) must be at least 50% of that piece's weight.
- **Minimum tiedown-count rule:** at least one tiedown for every 10 ft (or fraction) of the article's length, with a minimum of two tiedowns for any article regardless of how low that puts the required aggregate WLL.

**Worked example — 5,000 lb, 6-ft machinery skid:**

| Check | Requirement | Chosen securement | Pass? |
|---|---|---|---|
| Aggregate WLL ≥ 50% of 5,000 lb = 2,500 lb | ≥ 2,500 lb | 2 chains × 4,700 lb WLL = 9,400 lb | Yes |
| Minimum tiedown count (≤10 ft article) | ≥ 2 tiedowns | 2 chains | Yes |

**Common miss:** a single high-capacity chain rated 5,000+ lb WLL alone would satisfy the 50% rule (5,000 ≥ 2,500) but fails the 2-tiedown minimum — the count rule binds independently of whether the WLL math already clears.

**Blocking sequence for a piece with void space or no self-interlocking shape:**

1. Place fore-and-aft dunnage (2×6 or 2×4 lumber, load bars, or E-track-mounted blocking) tight against the piece on both ends of its direction of likely travel.
2. Apply tiedowns meeting both the count and aggregate-WLL rules above, routed to avoid sharp edges that could cut webbing or kink chain.
3. Fill remaining void space with dunnage or airbags rather than leaving gaps that let the piece build momentum before contacting a brace.
4. Recheck tension after the first ~50 miles or first stop on a multi-stop run — dunnage and straps settle as the load shifts slightly under initial transit.

## 4. NIOSH lifting index applied to irregular freight

Same RWL/LI formula as uniform-carton handling, but the coupling multiplier (CM) and asymmetry multiplier (AM) are the two that move most on irregular freight:

| Scenario | CM (coupling) | AM (asymmetry/twist) | Other multipliers held equal | Resulting LI (40 lb piece) | Risk |
|---|---|---|---|---|---|
| Cased good, cutout handholds, no twist | 1.00 | 1.00 | as in golden-zone lift | 0.62 | Under 1.0 — acceptable |
| Drum or skid, no handholds, no twist | 0.90 | 1.00 | same | 0.69 | Under 1.0 — acceptable |
| Drum or skid, no handholds, 45° twist to clear blocking | 0.90 | 0.86 | same | 0.80 | Elevated relative to the cased-good baseline at the same weight — the freight's shape, not its weight, drove the change |

**Field procedure:**

1. Do not assume CM = 1.0 (good coupling) on any piece without cutout handholds, straps, or cleats — treat drums, rolls, and slick-sided skids as poor coupling (CM ≈ 0.90 or lower) by default.
2. Where placing blocking or a tiedown forces a twisted reach around the piece, factor that twist into the AM estimate rather than treating the lift and the blocking step as separate, unscored actions.
3. Where LI comes out elevated for a recurring piece type (same skid design on repeat shipments), flag it for a mechanical-aid requirement (pallet jack, lift table, two-person team lift) rather than re-absorbing the same elevated LI shipment after shipment.
