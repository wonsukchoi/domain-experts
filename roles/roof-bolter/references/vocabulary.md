# Vocabulary

Terms generalists conflate that roof bolters keep sharply separate. Each: definition, a sentence a practitioner would actually say using it, and the common misuse.

## CMRR vs. RMR/RQD

**CMRR (Coal Mine Roof Rating)** is a rock-mass classification built specifically for coal-mine roof, scoring 0–100 based on the strength and structure of the layers that will actually form the bolted beam. **RMR/RQD** are general-purpose rock mass rating systems borrowed from civil/hard-rock tunneling that CMRR was adapted from but isn't interchangeable with — CMRR weights bedding-plane and slaking behavior that generic RMR doesn't capture the same way.

*Practitioner usage:* "Don't pull a generic RMR number off an old borehole log and plug it into the pattern decision — get the CMRR for this specific horizon."

*Common misuse:* treating any rock-mass rating number as equivalent to CMRR when picking bolt length or pattern.

## Tension vs. torque

**Tension** is the actual axial load pulling the bolt plate tight against the roof — the number the regulation cares about (50% of yield or anchorage capacity, whichever is less). **Torque** is the rotational force applied at the nut, which only converts to tension through a specific, bolt-and-thread-dependent relationship.

*Practitioner usage:* "That torque wrench reading doesn't mean anything on its own — it's calibrated to this bolt's thread pitch, and a different bolt on the same wrench setting could be under- or over-tensioned."

*Common misuse:* treating a torque reading as directly equivalent to tension across different bolt types, thread conditions, or lubrication states.

## Anchorage capacity vs. bolt yield strength

**Anchorage capacity** is how much load the resin-to-rock bond can hold before slipping, expressed per foot of encapsulation (tons/ft). **Bolt yield strength** is a property of the steel itself — how much load the bolt can take before it permanently deforms. A pull test can fail because the rock let go (anchorage) or because the steel gave (yield), and they call for entirely different fixes.

*Practitioner usage:* "That pull test topped out at 9 tons per foot — that's an anchorage number, not a yield number, so don't blame the bolt spec, look at the rock."

*Common misuse:* citing a pull-test result as evidence about bolt quality when the failure mode is actually a rock-anchorage problem, or vice versa.

## Gel time vs. spin time vs. hold time

**Gel time** is the total time from resin mixing start until the resin sets. **Spin time** is the portion of that window spent actually rotating the bolt to mix the resin components. **Hold time** is the remaining time the bolt is held stationary (under tension, if applicable) to let the mixed resin cure before release. Spin time plus hold time roughly equals gel time — but spin time alone must stay under gel time or mixing never completes.

*Practitioner usage:* "We're not holding long enough on the slow-set cartridges — spin time's fine, but hold time is what's coming up short on the cold headings."

*Common misuse:* using "gel time" and "spin time" interchangeably, which hides whether a bad result came from insufficient mixing (spin) or insufficient cure (hold).

## Fully grouted vs. mechanical (point-anchor) bolt

**Fully grouted** bolts are resin-encapsulated along their entire length, distributing load along the full bond. **Mechanical (point-anchor)** bolts anchor at a single expansion shell near the bolt's far end, relying on that one point rather than a bonded length. Fully grouted bolts make up the large majority of primary roof support in US coal mines; mechanical bolts still see use, especially for supplemental or temporary support.

*Practitioner usage:* "This heading's plan calls for full-column resin, not a point-anchor mechanical — don't substitute because the mechanical bolts are what's on the truck."

*Common misuse:* treating the two bolt types as interchangeable substitutes when the plan specifies one and not the other.

## SEPT (short encapsulation pull test) vs. full-column pull test

**SEPT** uses a short, controlled resin-encapsulation length on a sample bolt specifically to isolate and measure anchorage capacity (tons/ft), independent of the bolt's full installed length. A **full-column pull test** pulls a bolt installed to the plan's actual full encapsulation, which mixes anchorage-capacity signal with total bond-length effects and is harder to compare directly across headings.

*Practitioner usage:* "Run a SEPT on this stretch before we commit the whole pattern — a short encapsulation gives us the tons-per-foot number faster and cleaner than pulling a full-column bolt."

*Common misuse:* comparing a SEPT tons/ft result directly against a full-column pull-test's raw load number without converting both to the same per-foot basis.

## Drummy roof vs. cutter roof

**Drummy roof** is roof that returns a hollow, resonant sound when sounded with a bar — indicating a separation or void just above the surface layer. **Cutter roof** refers to a specific failure pattern where the roof shears along the rib line, often visible as a step or slip rather than heard as a sound. Both signal ground trouble, but they point to different mechanisms and different fixes (screen/tighter pattern for drummy roof vs. rib support or pattern extension toward the rib for cutter roof).

*Practitioner usage:* "That's not drummy, that's cutter — look at the step right at the rib, we need rib bolts, not just more roof bolts."

*Common misuse:* using "drummy" as a catch-all term for any bad-looking roof condition, which sends the fix toward supplemental roof support when the actual problem is at the rib.

## ATRS setback vs. unsupported roof span

**ATRS setback** is the fixed, regulated distance (≤5 ft) between the ATRS crossmember/rocker pads and the last row of permanent support. **Unsupported roof span** is the broader, general concept of how much roof area has no support at all — setback is one specific, numeric instance of that broader concept, defined by regulation for this exact equipment configuration.

*Practitioner usage:* "I know the span looks small, but measure the actual setback — 'looks close enough' isn't the same as inside 5 ft."

*Common misuse:* eyeballing "unsupported span looks fine" as a substitute for measuring the specific 5-ft ATRS setback figure the regulation sets.

## Extended cut vs. standard cut

**Extended cut** is a longer-than-baseline cut depth (commonly around 20 ft) that a mine earns approval for on a specific horizon based on demonstrated roof-fall history and CMRR. **Standard cut** is the plan's baseline depth, the default anywhere extended-cut approval hasn't been specifically granted for that heading.

*Practitioner usage:* "This panel's next door got extended cut, but this specific heading hasn't been mapped yet — we're on standard cut until engineering signs off."

*Common misuse:* assuming extended-cut approval carries automatically to an adjacent or similar-looking heading that hasn't itself been mapped or authorized.

## Permissible vs. intrinsically safe equipment

**Permissible equipment** is machinery that has met MSHA's approval process (enclosure, spark containment) for use in areas where methane may be present, per 30 CFR 75.503. **Intrinsically safe** is a narrower electrical-design concept (energy-limited circuits that can't produce an ignition-capable spark) that is one way — but not the only way — equipment can achieve permissibility.

*Practitioner usage:* "Don't call it intrinsically safe just because it's low-voltage — check that it's actually on the approved permissible equipment list for this section."

*Common misuse:* treating "low voltage" or "battery-powered" as automatically equivalent to permissible, without checking the actual MSHA approval status of the specific machine.

## Pattern bolt vs. supplemental (spot) bolt

**Pattern bolts** are the bolts installed on the plan's regular, repeating spacing across the full cut. **Supplemental (spot) bolts** are additional bolts added at specific locations flagged by sounding, pull test, or visible geology — on top of, not instead of, the pattern.

*Practitioner usage:* "Don't count the spot bolts we added over the drummy stretch as satisfying the pattern requirement there — the pattern still goes in, the spot bolts are extra."

*Common misuse:* treating supplemental bolts as a substitute for completing the regular pattern in a flagged zone, rather than an addition to it.
