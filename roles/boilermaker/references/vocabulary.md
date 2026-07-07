# Vocabulary

Terms generalists conflate or use loosely that a boilermaker keeps sharply separate.

## WPS vs. PQR vs. WPQ

**WPS** (Welding Procedure Specification) is the written instruction a welder follows — process, filler metal, preheat, amperage, position. **PQR** (Procedure Qualification Record) is the test record proving that WPS's parameters actually produce a sound weld, established once via mechanical test coupons. **WPQ** (Welder Performance Qualification) certifies a specific welder's ability to execute a specific process/material/position combination — it's about the person, not the procedure.

*In use:* "The WPS is qualified for this material group, but check the welder's WPQ covers 6G position before you assign this joint."

**Common misuse:** treating "the WPS is qualified" as sufficient to assign any welder to the job — the WPS qualifies the procedure, the WPQ qualifies the individual welder, and both are required, separately.

## Repair vs. alteration

A **repair** restores a component to the condition described in its original manufacturer's data report — same material, thickness, and design. An **alteration** changes any of those: thickness, design pressure or temperature, or configuration. The distinction is legal, under the National Board Inspection Code, not a judgment about how difficult or skilled the work is.

*In use:* "Replacing this tube with the original spec is a repair; upsizing the wall to fix chronic thinning is an alteration — different authorization, different paperwork."

**Common misuse:** classifying work as a "repair" based on how routine or skill-appropriate it feels, rather than whether it changes anything the original data report specifies.

## "R" stamp / Certificate of Authorization

The National Board's **"R" Certificate of Authorization** is the legal credential permitting an organization to perform Code repairs (and, if scoped, alterations) on boilers and pressure vessels. It belongs to the employer/organization, not to an individual welder's skill or certification, and it has a defined scope and renewal cycle.

*In use:* "We can weld this joint fine, but check our R stamp's scope covers alterations before we upsize that tube wall."

**Common misuse:** assuming a skilled welder or a competent crew is automatically authorized to perform a Code repair — the authorization is organizational and scope-limited, independent of individual skill.

## MAWP vs. design pressure vs. operating pressure

**MAWP** (maximum allowable working pressure) is the highest pressure a component is certified safe to hold in its current, as-built condition — it can be lower than the original design pressure if the component has thinned or been altered. **Design pressure** is the pressure the component was originally engineered to. **Operating pressure** is what it actually runs at day to day, always at or below MAWP with margin.

*In use:* "Don't hydro test against operating pressure — the test is 1.5 times MAWP, and MAWP may have dropped since the original design pressure if this drum has thinned."

**Common misuse:** using operating pressure or original design pressure as the hydro-test basis instead of the component's current, as-inspected MAWP.

## Hydrostatic test vs. pneumatic test

A **hydrostatic test** pressurizes the vessel with water (or another liquid) to a multiple of MAWP, held for a specified time — the standard, lower-energy method since liquid doesn't store compressive energy the way gas does. A **pneumatic test** uses air or gas at pressure, storing far more energy per unit volume and carrying materially higher risk if the vessel fails during test — used only when a hydro test is impractical, and under stricter procedural controls.

*In use:* "We're hydro testing, not pneumatic — same 1.5x MAWP target, but nobody's clearing the area for a gas-test blast radius."

**Common misuse:** treating "pressure test" as one generic procedure — the test medium changes both the required precautions and, in some cases, the acceptable pressure multiplier.

## Rolled joint vs. seal weld

A **rolled joint** expands a tube mechanically into a drum or tubesheet hole using a roller expander, relying on the resulting metal-to-metal interference fit to seal and hold the tube. A **seal weld** adds a weld bead at the tube-to-drum face, either as the primary joint method or as a supplement to a rolled joint. The two have different failure modes and different qualification requirements — a seal weld is a Code weld requiring WPS/WPQ; a rolled joint is a mechanical fit requiring expansion-percentage verification.

*In use:* "This drum uses rolled joints only, no seal weld — don't skip the drift-pin check assuming a weld will backstop an under-rolled tube."

**Common misuse:** assuming a seal weld compensates for an under-rolled joint, or that a rolled joint needs the same NDT treatment as a weld.

## Wall reduction (tube expansion) — percentage

The **percent wall reduction** in a rolled tube joint is the fractional decrease in tube wall thickness (and corresponding ID increase) produced by the roller expander, measured against the tube's original wall thickness before rolling. It is the actual sizing target for the joint, distinct from torque or turn-count, which are indirect proxies for it.

*In use:* "Target is 4 to 6 percent wall reduction — verify with the drift pin, the expander's torque reading alone doesn't tell you the actual percentage."

**Common misuse:** using expander torque or a fixed turn count as if it directly specifies the wall reduction achieved — torque response varies with tube hardness and expander wear, so it drifts from the true percentage over time.

## Porosity vs. slag inclusion vs. lack of fusion

**Porosity** is trapped gas forming rounded voids in the weld metal. **Slag inclusion** is trapped, non-metallic residue from the welding flux left inside the weld. **Lack of fusion** is a failure of the weld metal to bond completely with the base metal or a prior pass — a planar, not rounded, discontinuity, generally treated as more severe than either rounded-indication type because it creates a sharp crack-like flaw.

*In use:* "That's lack of fusion on the RT film, not porosity — this one doesn't get evaluated against the rounded-indication acceptance table, it's rejected outright."

**Common misuse:** applying the aggregate-length acceptance criteria written for rounded indications (porosity, slag) to a planar discontinuity like lack of fusion, which is evaluated under a stricter standard.

## Authorized Inspector vs. owner-user inspector

An **Authorized Inspector (AI)** is a third-party inspector, commissioned by the National Board and employed by an insurance company or independent inspection agency, who signs off on Code repairs, alterations, and hydro tests for the jurisdiction of record. An **owner-user inspector** is an inspector employed directly by the equipment's owner, permitted in some jurisdictions to perform certain in-house inspections under a separate accreditation — not a substitute for AI sign-off where the jurisdiction requires it.

*In use:* "Owner-user inspection covers our internal wall-thickness surveys, but the R report on this repair still needs the AI's signature."

**Common misuse:** treating an owner-user inspector's sign-off as equivalent to Authorized Inspector sign-off for Code repair/alteration documentation, when the jurisdiction requires the latter.

## PWHT (post-weld heat treatment) vs. preheat

**Preheat** raises the base metal temperature before and during welding to slow the cooling rate and reduce cracking risk as the weld is made. **PWHT** is a separate, controlled heat-treatment cycle applied after welding is complete, holding the completed weldment at temperature to relieve residual stress and temper the weld and heat-affected zone. Preheat happens during welding; PWHT happens after, on a specified time-temperature schedule.

*In use:* "We held preheat through the whole weld sequence, but this thickness still calls for PWHT afterward — they're not interchangeable requirements."

**Common misuse:** assuming preheat during welding satisfies a PWHT requirement, or skipping PWHT because preheat was maintained throughout the weld.
