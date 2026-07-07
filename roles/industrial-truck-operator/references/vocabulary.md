# Vocabulary

Terms generalists conflate or oversimplify — practitioners keep them precise because the safety math depends on it.

## Rated capacity vs. load center

**Rated capacity** is the maximum weight the plate certifies the truck to lift — but only **at the reference load center** stated on the same plate (commonly 24 inches from the fork face for standard-pallet Class I–V trucks). **Load center** is the distance from the fork face to the load's actual center of gravity. The two numbers are inseparable; quoting one without the other is meaningless.

*In use:* "It's rated 5,000 lb at 24 inches — this coil's center is out at 34, so the real number for this load is 4,074, not 5,000."

*Common misuse:* treating "rated capacity" as a flat weight ceiling and never checking where the actual load center falls, especially on long, offset, or irregularly shaped loads where the center of gravity clearly isn't at the pallet's geometric middle.

## Moment (load moment)

The product of weight and distance from the front axle — the actual physical quantity the truck's capacity rating protects against, expressed as weight × (load center + axle-to-fork distance). The plate's stated capacity is a weight number, but the underlying limit is a moment limit.

*In use:* "The plate says 5,000 lb, but that's really 220,000 inch-pounds of moment — do the math for this load's actual distance before you trust the weight number."

*Common misuse:* assuming capacity scales linearly with weight alone and ignoring that a longer distance eats into the same fixed moment budget.

## Stability triangle

The three-point support system formed by the two front wheels and the pivot point of the steer (rear) axle. The truck is stable only while the combined center of gravity of the truck plus its load stays within this triangle; it is a static concept applied to a constantly shifting dynamic situation as the load is raised, tilted, or the truck turns and brakes.

*In use:* "Raising that load to eight feet and tilting forward pushed the combined center of gravity right to the front edge of the triangle — one hard brake and it's over the line."

*Common misuse:* treating the stability triangle as something checked once at the start of a lift, rather than something that changes continuously with mast height, tilt angle, and the truck's speed and turning.

## Load-center de-rating

The reduction in a truck's safe carrying capacity that results from a load's center of gravity sitting further from the fork face than the plate's reference distance — calculated by re-solving the moment equation at the actual distance rather than the reference one.

*In use:* "This load doesn't just 'lose some capacity' at 34 inches — it de-rates to 4,074 lb, which is below what we're trying to move."

*Common misuse:* assuming the capacity loss is small or roughly proportional to the extra distance; because the moment is fixed and the divisor is the total distance (load center plus axle-to-fork distance, not load center alone), the actual percentage loss is easy to underestimate without running the calculation.

## Class of truck (I–VII)

The ANSI/ITSDF classification of powered industrial trucks by power source and design (Class I: electric counterbalanced rider; Class IV/V: internal-combustion cushion/pneumatic tire; Class VII: rough-terrain, etc.). Each class has different stability characteristics, capacity conventions, and certification requirements — a certification on one class doesn't automatically cover another.

*In use:* "She's certified on Class I sit-down counterbalance, not Class II reach trucks — she needs a class-specific evaluation before she runs the reach truck in the narrow-aisle racking."

*Common misuse:* treating "forklift certified" as a single blanket credential rather than a class-and-truck-specific one.

## Beam capacity / rack load placard

The load rating posted on a pallet-racking beam or bay, governed by the racking manufacturer's engineering (per ANSI MH16.1) and independent of what any forklift can lift onto it. It is a property of the rack structure — bolted connections, beam deflection, column loading — not of the truck that placed the load there.

*In use:* "The forklift had no trouble setting that pallet down — the problem is the beam's only rated for 5,500 lb and this bay's now at 5,900."

*Common misuse:* assuming a stable, successful lift and placement means the destination could safely hold the weight — the truck's stability and the rack's capacity are two unrelated failure modes.

## Tow tractor / tugger

A powered industrial truck (the "tractor" half of the O*NET title) designed to pull a train of wheeled carts rather than lift a load on forks — used for line-side delivery and long-distance material moves where lift height isn't needed. Stability considerations shift from tip-over risk to jackknifing and load-sway on turns with a long cart train.

*In use:* "Don't take that corner at tugger speed with six carts behind you — the train will jackknife before the tractor itself has any stability problem."

*Common misuse:* applying counterbalance-forklift stability thinking (mast height, tilt, load center) to a tugger, when the actual risk profile is about cart-train length, turn radius, and load-sway.

## Attachment derating

The additional capacity reduction that comes from mounting an attachment (clamp, side-shifter, boom, fork extension) onto the truck's carriage — the attachment adds its own weight and typically moves the effective load center further from the mast, both of which reduce the truck's usable capacity below its base nameplate rating.

*In use:* "The base truck is rated 5,000 lb, but with the paper-roll clamp mounted it's derated to 3,800 — that's the number on the clamp's own plate, and that's the one that governs."

*Common misuse:* reading only the truck's base nameplate and ignoring the attachment manufacturer's separate, lower derated rating.

## Grade rating vs. ramp/dock plate rating

**Grade rating** is the maximum slope (percent grade) the truck itself is rated to travel, loaded, per the manufacturer. **Dock plate/ramp rating** is a separate structural weight limit for the plate or ramp bridging a gap, independent of the truck's own grade capability. A truck within its grade rating can still exceed a dock plate's load limit.

*In use:* "The truck's fine on a 10% grade loaded, but this dock plate's only rated for 6,000 lb combined — check that number separately."

*Common misuse:* assuming a truck cleared for a grade is automatically cleared to cross any ramp or dock plate at that grade, without checking the plate's own structural rating.

## Struck-by (pedestrian) incident

An incident category where a person is hit by a moving powered industrial truck or a load it's carrying, as distinct from a tip-over or a truck-versus-rack collision. It is tracked separately in fatality data because its causes (blind corners, shared aisles, lack of horn discipline) and its prevention measures (traffic separation, mirrors, right-of-way protocol) are different from stability-related incidents.

*In use:* "Our tip-over rate is low — the exposure we actually need to fix is struck-by risk at the dock corner, which is a traffic problem, not a stability problem."

*Common misuse:* funneling all forklift safety attention into load/stability training while under-investing in pedestrian traffic management, even though struck-by incidents are a leading cause of forklift-related fatalities.
