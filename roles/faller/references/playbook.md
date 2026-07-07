# Playbook

Filled worksheets for the three calculations that determine whether a tree gets hand-felled, how, and how it's cleared for: the lean/hang-weight direction call, whether wedges can hold the lean, and how big the escape/exclusion zones need to be. Numbers below are worked examples against stated field heuristics, not universal constants — remeasure on site.

## 1. Lean and hang-weight direction worksheet

Two separate readings feed one target lay direction. Don't skip straight to "it leans that way" from a glance at the trunk.

**Trunk lean** — read with a plumb bob (sighted against the trunk) or an inclinometer, given as an angle from vertical toward (or away from) the intended lay:

`Forward lean distance (ft) ≈ tree height (ft) × sin(lean angle)`

Worked example: 100 ft tree, 5° lean → 100 × sin(5°) ≈ 8.7 ft forward lean distance at the top.

**Hang weight (crown offset)** — visual assessment of crown mass distribution (lopsided limbs, broken/dead top, storm damage), estimated as a lateral skew angle off the trunk-lean plane, applied at the estimated height of the crown's mass center:

`Lateral hang offset (ft) ≈ crown mass-center height (ft) × tan(crown skew angle)`

Worked example: crown mass-center height 75 ft, estimated 4° lateral skew → 75 × tan(4°) ≈ 5.2 ft.

**Resultant direction** — combine the two components as a simple right-triangle offset from the forward-lean axis [stated heuristic — simplified field vector method, not a rigorous engineering calculation; use it to judge how far off the trunk-lean-only line the real pull is, not as a precise bearing]:

`Resultant angle off forward-lean axis ≈ arctan(lateral offset / forward offset)`

Worked example: arctan(5.2 / 8.7) ≈ 31° — the notch gets aimed roughly 30° off the naive trunk-lean line, not at it.

Reading this: when the resultant angle is small (under roughly 10–15°), trunk lean alone is a reasonable proxy and standard notch aim holds. When it's large, as above, the crown is doing more work than the stem angle suggests, and the notch aim — not the wedge plan — is what has to absorb the correction.

## 2. Wedge-correction range

Wedges act along the backcut plane and correct fore-aft lean only; they do nothing for a lateral hang-weight component.

| Forward lean, expressed as grade-equivalent (forward lean distance ÷ tree height) | Correction approach |
|---|---|
| Under ~5% | Single wedge, standard notch, no mechanical assist needed |
| ~5–10% | Single wedge typically sufficient on mid-diameter trees; check wedge lift rating against tree weight |
| ~10–15% | Stacked wedge pair near the upper end of typical hand-correction range; open-face notch preferred to keep the notch closed longer through the fall arc |
| Above ~15%, or heavy top weight compounding the lean | Beyond hand-wedge correction — use cable/tractor-line pull, or leave the tree for mechanized equipment |

Worked example: 8.7 ft forward lean over 100 ft height ≈ 8.7% grade-equivalent — within the single-to-stacked-wedge range, so wedges are viable for the forward component. The 31° lateral pull calculated above is handled entirely by notch aim, since no wedge count corrects a lateral offset.

## 3. Notch and hinge dimensions by DBH

| Notch type | Face angle | When to use |
|---|---|---|
| Conventional (45°) | 45° | Straightforward lean, no tension-wood/barber-chair concern, standard hand-felling |
| Open-face | 70–90° | Heavy forward lean, tension-wood species (Douglas-fir, southern pine), any barber-chair risk — the wider angle keeps the notch closed longer through the fall, holding directional control further into the fall arc |
| Humboldt | ~45°, inverted (bottom cut angled up from the stump) | Sawlog value recovery at the butt log in commercial timber, functionally similar directional control to conventional |

**Hinge sizing** (applies across notch types):

`Hinge thickness ≈ 10% of DBH`
`Hinge width ≈ 80% of diameter, after rounding the corners`

Worked example, 32 in DBH: hinge thickness ≈ 3.2 in, hinge width ≈ 25–26 in.

**Bore (plunge) cutting**: for trees with barber-chair risk or heavy lean, plunge the saw into the center of the trunk behind the planned hinge line, cut sideways to establish full hinge width first, then cut backward toward the far side, leaving a trigger/strap of uncut wood (commonly ~2 in on a tree in this size class) on the back of the trunk. The strap holds the tree until it's deliberately cut last, once escape routes and crew clearance are confirmed — this avoids the moment in a straight backcut where a fast-splitting tree can sit back on the bar before the cut is finished.

## 4. Escape-route and exclusion-zone sizing

| Scenario | Sizing |
|---|---|
| Escape routes (per tree, two required) | Roughly 45° off the backcut line, on the side opposite the final lay direction, cleared to bare ground for at least ~15–20 ft |
| Faller-to-faller spacing in the same felling area | At least two tree-lengths of the taller tree (OSHA 1910.266), or fell the tree between them first |
| Hazard tree (snag, hung top, widow-maker) exclusion zone | Treat the hazard tree's own height as the minimum working radius until a qualified person drops or rigs it down |
| Hung tree (didn't reach ground) | No radius substitutes for the rule: never cut the supporting tree, never walk under the hang — clear it with a winch, rotation via cant hook, or by felling the holding tree from outside its own hazard radius |

Worked example continued: with the lay corrected 30° left of the original flag, both escape routes are re-walked against the corrected backcut line (not the original flagged line) and confirmed clear of tree #15's canopy footprint, which sits 40 ft to the right — outside the corrected escape corridor once the lay shift is accounted for.
