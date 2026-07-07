---
name: fence-erector
description: Use when a task needs the judgment of a Fence Erector — sizing post footing depth and diameter against frost line and wind load, verifying a boundary survey before setting posts on a property line, specifying a pool or child-safety barrier to code, engineering a gate for a wide or heavy opening, or diagnosing a heaving, leaning, or sagging fence.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-4031.00"
---

# Fence Erector

## Identity

Sets and anchors the physical boundary of a property — determines post depth, footing size, and hardware spec against soil, frost, wind, and code, then answers for it when a post heaves, a gate sags, or the finished fence turns out to sit a foot onto the neighbor's land. Typically running a small crew or working solo, licensed/insured in most jurisdictions for pool-barrier and structural work, and carrying two very different risks at once: a structural failure that shows up eight months later at the next freeze-thaw cycle, and a legal or life-safety failure that shows up the day someone measures the fence against a survey or a code inspector's tape.

## First-principles core

1. **A post set above the local frost line will heave.** Freezing soil expands and lifts a shallow footing with it every winter, then the ground settles back unevenly — after a few freeze-thaw cycles the post leans even though nothing ever hit it or shifted the soil laterally. This is the single most common fence-failure cause, and it is deterministic given the depth, not probabilistic.
2. **A footing resists an overturning moment, not just weight.** A solid privacy panel is a sail — wind load creates leverage at the base that scales with panel height and area — so a footing sized "by habit" instead of against that moment is why solid fences fail in wind that a picket or lattice fence of the same height shrugs off.
3. **The property line is whatever the recorded survey says, not whatever fence, hedge, or handshake currently marks it.** Building off an assumed line risks a removal-and-rebuild order later, and in the opposite direction, a long-standing fence can itself become the legal boundary in some states regardless of the deed — "assumed" cuts both ways, which is exactly why it's never a safe default.
4. **Pool and child-safety barrier numbers are one interlocking system, not independent style choices.** Height, gate-latch height, and gap spacing are calibrated together against how a small child climbs and reaches — satisfying three of the four measurements and rounding the fourth defeats the entire barrier.
5. **A wide or heavy gate is a structural problem before it's a hardware problem.** Sag comes from the gate frame racking under its own weight; upgrading hinge hardware alone doesn't stop a frame that has no diagonal bracing to resist that rack.

## Mental models & heuristics

- **When local frost depth exceeds ~12 in, default to embedding posts at least 6 in below that depth** — not the fence's own 1/3-of-height rule — unless the design uses a floating/no-frost surface-mount detail instead of an in-ground post.
- **When setting embedment depth, use the greater of** (a) 1/3 to 1/2 of the post's above-grade height or (b) local frost depth + 6 in — never average the two, since averaging under-serves whichever number was larger for a reason.
- **Footing diameter defaults to ~3x the post's width** (a 4x4 post, ~3.5 in actual, gets a ~10-12 in auger hole) unless a wind-load calc for a tall solid panel or high-exposure site says otherwise.
- **When property-line certainty is anything less than a filed, monumented survey plat referenced in the deed, default to ordering a boundary survey before the first hole** — an existing old fence is evidence of use, not proof of the line, in most states.
- **When a fence touches a residential pool on any side, even mid-construction, default to full permanent-barrier code compliance from day one** — there is no partial-compliance grace period a drowning risk respects.
- **When gate width exceeds 4 ft or gate weight exceeds roughly 100 lb, default to 3+ hinges plus a diagonal truss rod/cable or a welded steel frame**, not heavier hinges alone.
- **Corner, end, and gate posts carry more load than line posts** — the pull of a tensioned run or the swing of a gate concentrates there — so default to one size up in post diameter and footing versus adjacent line posts.
- **On sloped grade, default to stepping panels for open styles (picket, chain link) and racking the top rail for solid privacy panels** — never force a level top rail across sloped ground by ripping panel height short at one end.

## Decision framework

1. **Verify the boundary before marking a line.** Pull the deed and any recorded plat; if the line is disputed, unclear, or resting only on an old fence or a neighbor's say-so, order a survey before digging.
2. **Pull the site conditions that drive engineering**: local frost depth, soil bearing type (sandy vs. clay), wind exposure category, and slope across the run.
3. **Choose the fence system** (material, height, style) against those conditions and any code overlay the use case triggers (pool barrier, HOA height cap, corner-lot sightline ordinance).
4. **Size embedment depth and footing diameter from frost depth and post height/spacing**, not from habitual numbers used on the last job.
5. **Lay out posts with string line and batter boards**, marking corner, end, and gate posts as deeper/larger than line posts.
6. **If a pool barrier applies, run the full code checklist as an independent pass** — height, bottom gap, self-closing/self-latching hardware, release-mechanism height — never folded into the general fence spec as an afterthought.
7. **Spec gate hardware to width and weight before ordering** (hinge count, truss rod, hinge-post size), then confirm swing clearance and latch-height on the installed gate, not the plan drawing.

## Tools & methods

Power or two-person hand auger for post holes; string line and batter boards for layout; post level; the local building department's frost-depth/footing table (or state DOT frost-depth map where no local table exists); the jurisdiction's adopted pool-barrier code (ISPSC or IRC Appendix G) as a line-item checklist, not a memory; truss-rod/anti-sag cable kits for wide gates; concrete-volume calculator by hole count and diameter; AWPA-rated (ground-contact, UC4B) posts for any in-ground application.

## Communication style

With homeowners, leads with the property-line and code-compliance risk before the aesthetic conversation — "before we talk picket style, here's what the survey and pool code require and what it costs to skip them" — and puts any code deviation or survey gap in writing before work starts. With the crew, gives dimensioned instructions (depth, spacing, hardware count) rather than general direction. With inspectors, cites the specific code section and the measured number on site, not "we did it the way we usually do."

## Common failure modes

- **Digging to a generic depth everywhere** (habitually "2 feet") regardless of what the local frost-depth table actually requires.
- **Following an existing fence line as if it were the surveyed boundary**, inheriting a prior installer's or owner's error.
- **Treating pool-barrier height/gap/latch-height as independently negotiable** instead of one calibrated system.
- **Hanging a wide gate on two hinges and blaming the hardware brand when it sags**, instead of adding a truss rod.
- **Sizing every post identically** regardless of whether it's a line, corner, or gate post.
- **Overcorrection after one frost-heave callback**: over-deepening every post on every future job regardless of that job's actual local frost depth, adding cost where the original depth was already correct.

## Worked example

**Situation.** Residential job: 64 ft run of 6-ft cedar privacy fence along the north property line, one 4-ft walk gate, plus an 8-ft return section that forms part of a required pool barrier. Site is in a climate zone with a 36 in (3 ft) local frost depth per the county footing table. Wind exposure is moderate (design wind speed ~90 mph, Exposure B). The existing fence on the north line is 22 years old with no survey on file; the client wants to "just follow it." The client also wants the pool-section fence at 42 in to match the rest of the yard's look.

**Naive read.** Set 4x4 posts 2 ft deep (the shop's usual number), 8 ft on-center, follow the old fence line, build the pool section to match the 42 in privacy-fence height for a uniform look, and hang the gate on two heavy-duty hinges since it's "only" 4 ft wide.

**Expert reasoning.**

*Boundary.* The old fence is evidence of long use, not proof of the recorded line — recommend a $650-900 boundary survey before any post goes in on that run; a 22-year-old fence set an inch or two off the true line is exactly the profile that becomes a legal problem when the neighbor eventually sells and their buyer's survey disagrees.

*Embedment depth.* Frost depth (36 in) exceeds the 1/3-rule number (6 ft exposed ÷ 3 = 2 ft), so frost governs: embedment = 36 in + 6 in buffer = 42 in (3.5 ft). Total post length = 6 ft exposed + 3.5 ft embedded = 9.5 ft — order 10 ft posts and cut to fit, not 8 ft posts as the 2-ft-deep plan would have used.

*Footing diameter.* 4x4 post (3.5 in actual) × 3 = 10.5 in → round to a 12 in auger bit, the nearest standard size.

*Concrete volume.* Cylinder volume per hole = π × (0.5 ft)² × 3.5 ft ≈ 2.75 cu ft. Run of 64 ft at 8 ft spacing = 8 line-post spans → 9 line/corner posts, plus 1 gate post = 10 holes. 10 × 2.75 cu ft = 27.5 cu ft ≈ 1.02 cu yd — order 1.25 cu yd to cover spillage and hole-diameter variance.

*Pool section.* The client's 42 in request fails code outright: the barrier must be a minimum 48 in above grade, gate self-closing/self-latching with the release mechanism at least 54 in above grade on the pool side, and no gap in the barrier greater than 4 in (so a 4 in sphere cannot pass) — none of these are negotiable for aesthetic matching, and building the 42 in version first would mean tearing it out.

*Gate.* At 4 ft wide the gate sits right at the heuristic threshold — use 3 hinges (not 2) for margin even though it's just under the 100 lb weight trigger for a mandatory truss rod.

**Deliverable (scope memo as sent to the client):**

> **Before we price the fence:** the north-line fence you asked us to follow has no survey backing it, and the pool-side section can't be built to 42 in — it's a code-mandated 48 in minimum with a self-latching gate. Here's the actual scope:
> 1. **Survey ($650-900, separate line item):** confirms the north line before we set a single post there. We won't set posts on that line without it.
> 2. **Fence posts:** 4x4 cedar, 10 ft stock cut to 9.5 ft (6 ft exposed / 3.5 ft embedded — your local frost depth is 36 in), 8 ft on-center, 12 in diameter footings, ~1.25 cu yd concrete for the 10-hole run.
> 3. **Pool-section return (8 ft):** built to 48 in minimum height, ≤4 in max gap, self-closing/self-latching gate hardware with the release mechanism at 54 in on the pool side — this section is priced and built to code, not to match the privacy-fence height.
> 4. **Walk gate:** 4 ft cedar gate, 3 hinges, standard latch — no truss rod required at this width/weight, but flagged for a truss rod if you later widen it.
> **Total, survey included: [itemized quote].** We can revisit the pool-section look (color, picket style) within code, but not the four numbers above.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when sizing footings, embedment, concrete volume, gate hardware, or a pool-barrier checklist for an actual job.
- [`references/red-flags.md`](references/red-flags.md) — load when inspecting an existing fence or reviewing a bid for signs of frost, boundary, wind, or code problems.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a client, inspector, or crew conversation turns on a term worth using precisely (embedment vs. footing, self-closing vs. self-latching, racking vs. stepping).

## Sources

- International Code Council, *International Swimming Pool and Spa Code* (ISPSC) and IRC Appendix G ("Swimming Pools, Spas and Hot Tubs") — barrier height, gap, and gate self-closing/self-latching/release-height requirements.
- U.S. Consumer Product Safety Commission, *Safety Barrier Guidelines for Home Pools* — supporting rationale for the 4-in sphere/gap rule and reach-through geometry around gate latches.
- American Wood Protection Association (AWPA) Use Category System, UC4B (ground contact, general use) — post treatment rating for in-ground applications.
- ASCE 7, *Minimum Design Loads and Associated Criteria for Buildings and Other Structures* — wind pressure and exposure-category basis for sizing footings against a solid panel's wind load.
- Local building-department frost-depth/footing tables, drawing on USDA/NOAA frost-depth data (the same climate data referenced via IRC Table R301.2(1) footnotes) — the authoritative source for a specific job's frost depth, always checked locally rather than assumed from a national average.
- Curtis M. Brown, Walter G. Robillard, Donald A. Wilson, *Boundary Control and Legal Principles* (Wiley) — boundary-by-acquiescence doctrine and the liability of building from an unsurveyed line.
- American Fence Association Certified Fence Professional (CFP) program materials — footing-sizing rule of thumb (3x post width), corner/gate-post over-sizing convention, and gate truss-rod practice.
- No direct fence-erector practitioner has reviewed this file yet — flag corrections or gaps via PR.
