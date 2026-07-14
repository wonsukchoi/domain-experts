# Playbook

Filled reference tables and step sequences for scoping and executing a wallcovering install. Treat the specific numbers as representative of manufacturer spec sheets, not a substitute for the actual product's instructions on a live job.

## 1. Roll-yield math by pattern match type

Formula: **cut length = drop height + top/bottom trim, rounded up to the next full repeat increment; drops per roll = floor(roll length ÷ cut length); rolls needed = ceil(strips needed ÷ drops per roll).**

| Match type | How it consumes paper | Example |
|---|---|---|
| Straight match (no offset) | Every strip's pattern lines up at the same height as its neighbor; waste is only the trim-to-repeat rounding | 24 in repeat, 8 ft wall → cut length rounds to 10 ft (5 repeats) |
| Drop/offset match (e.g. "24/12 in") | The pattern only lines up at a specified vertical offset between adjacent strips (half-drop is the common case); every other strip needs its own registration point | 24 in repeat, 12 in offset — odd and even strips are cut from different points in the pattern, typically no extra paper cost but doubles the registration checks during hang |
| Random match | No repeat to register — strips can be cut back-to-back off the roll | No repeat waste; cut length = drop height + trim only |

**Worked example — straight match, 24 in repeat, 8 ft ceiling, 33 ft roll:**

| Step | Calculation | Result |
|---|---|---|
| Cut length | 8 ft + 4 in top + 4 in bottom = 8 ft 8 in, round up to next 24 in multiple | 10 ft |
| Drops per roll | 33 ft ÷ 10 ft | 3 (floor), 3 ft offcut per roll |
| Wall length (45 ft net, 20.5 in / 1.71 ft strips) | 45 ÷ 1.71 | 26.3 → 27 strips |
| Rolls needed | 27 ÷ 3 | 9 rolls exactly |

**Rule of thumb:** order 1 extra roll per 8–10 rolls of the base calculation as working overage for miscuts and future repairs, from the same run number — this is a stated heuristic, not a manufacturer spec, and should be flagged to the client as an optional line rather than folded silently into the total.

## 2. Paste and primer selection by backing and substrate

| Wallcovering backing | Correct paste class | Wall substrate condition | Primer/sizing needed |
|---|---|---|---|
| Non-woven ("paste-the-wall") | Non-woven-specific clear paste, applied to the wall, not the paper | New or previously painted drywall, sound | Acrylic wallcovering primer/sizer, always — bare or painted drywall alike |
| Traditional paper (unpasted) | Wheat- or cellulose-based paste, applied to paper, booked | Skim-coated or previously papered wall | Acrylic wallcovering primer/sizer; strip old paper to substrate first if it's not a true liner |
| Fabric-backed or solid vinyl | Clay- or vinyl-specific heavy-duty paste, applied to paper, booked | Painted drywall or plaster | Acrylic wallcovering primer required — vinyl over unprimed drywall risks tearing the drywall's paper face on future removal |
| Pre-pasted | Water-activated factory paste — no separate paste unless the manufacturer specifies an activator/booster | Painted drywall | Primer still applies; pre-pasted refers only to the adhesive step, not substrate prep |

**Never substitute:** a diluted wall paint primer for a wallcovering primer/sizer. Wallcovering primers are nonrewettable and create a release layer so the covering can be stripped later without pulling the wall's paper face; a standard paint primer doesn't have that property and can bond the covering to the wall permanently.

## 3. Corner sequencing

1. Check every inside and outside corner with a level or plumb bob before planning strip layout; record the out-of-plumb amount top to bottom.
2. **Under ~6 mm out of plumb over the strip height:** wrap a full strip around the corner, then immediately snap a fresh plumb line on the new wall for the next strip rather than trusting the wrapped edge as plumb.
3. **Over ~6 mm out of plumb, or any commercial/high-visibility corner:** two-piece the corner — cut the strip so it wraps 15–20 mm (5/8–3/4 in) onto the adjacent wall, snap a new plumb line on that wall, and hang the next strip to the plumb line, overlapping the wrapped edge and matching pattern as closely as the overlap allows.
4. **Outside corners:** always two-piece regardless of plumb reading — a full strip wrapped around an outside corner is exposed to abrasion and impact along the wrap edge and is the first place a covering lifts in a hallway or stairwell.
5. Plan the pattern-break seam (where the final strip won't quite match the first) for the least conspicuous location — behind a door, in a closet, or centered above a doorway — before starting, not by default at the point you run out of wall.

## 4. Seam and cure timing

| Step | Timing | Why |
|---|---|---|
| Booking (traditional paper, paste-the-paper) | Fold pasted ends to center, wait 5–10 min per manufacturer spec | Lets paper finish expanding before it goes on the wall; hanging before it's done expanding shows up as bubbles that won't roll out |
| Non-woven paste-the-wall | No booking — hang dry strip directly onto the pasted wall section | Non-woven backing doesn't expand on paste the way traditional paper does |
| Seam rolling | Wait 2+ hours after hanging before rolling seams | Rolling while paste is still viscous squeezes adhesive out of the seam rather than seating it; the seam then opens as it dries |
| Full cure / first cleaning | 24–72 hours depending on product and ambient humidity, per manufacturer TDS | Seams and adhesive bond are still developing; cleaning or taping over a wall before cure risks lifting an edge |

## 5. Prep scope by wall condition — pricing as its own line

| Wall condition found | Prep required | Typical time relative to hang time (stated heuristic) |
|---|---|---|
| Sound, previously painted, no texture | Wash, spot-prime, size | 10–20% of hang time |
| Light texture or orange-peel finish | Skim-coat high spots, sand, prime | 40–60% of hang time |
| Existing strippable wallcovering, intact | Strip, wash residue, size | 50–80% of hang time |
| Existing non-strippable/painted-over wallcovering | Skim-coat over or remove by scoring + steam, dry out, prime | 100%+ of hang time — price and schedule as a near-equal second job |
