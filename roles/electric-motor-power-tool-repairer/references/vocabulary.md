# Vocabulary

Terms generalists conflate that practitioners keep sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse to avoid.

## Insulation resistance (IR) vs. Polarization Index (PI)

**IR** is a single megohmmeter reading (typically at 1 minute) of a winding's resistance to ground, compared against an absolute minimum (rated kV + 1, in megohms). **PI** is the ratio of the 10-minute reading to the 1-minute reading on the same test — it exposes the *trend* of moisture/contamination absorbing or dissipating charge over time, which a single-point IR reading can't show.

*Practitioner usage:* "IR passed at 8 megs, but PI came in at 1.4 against a 2.0 minimum — that winding's still moving, don't clear it on the IR number alone."

*Common misuse:* running only a 1-minute IR check and calling the winding healthy because it cleared the absolute minimum, skipping the timed PI test entirely.

## Burnout vs. bake-out (dry-out)

**Burnout** is high-temperature processing (target ≤650–700°F/343–371°C, controlled) used to strip old winding insulation and varnish off a stator core before rewinding — done once, destructively, to the old winding. **Bake-out (dry-out)** is a much lower-temperature cycle (roughly 90–110°C) applied to a winding still in service, meant to drive out moisture and raise a failing PI reading — it changes nothing structurally and is not a substitute for rewind when physical damage is present.

*Practitioner usage:* "Don't confuse the two — we're bake-out drying this one to see if PI recovers, not burning it out. If we still see a carbon track after drying, it goes to burnout for a real rewind."

*Common misuse:* using "burn it out" loosely to mean any heat treatment, which leads a junior tech to over-temperature a winding that only needed a dry-out, damaging core steel that didn't need to be touched.

## Rewind vs. rebuild vs. recondition

**Rewind** replaces the copper winding itself (stator or armature) after burnout strips the old one. **Rebuild** typically means replacing wear components — bearings, brushes, seals — without touching the winding. **Recondition** is a vaguer trade term customers use for either, or both, and should be pinned down before quoting.

*Practitioner usage:* "This is a rebuild, not a rewind — bearings and seals only, the winding tested clean on IR/PI."

*Common misuse:* a customer asking for a "recondition" and being quoted a full rewind (or vice versa) because nobody clarified which components actually need work.

## Core loss (no-load loss) test

A test of input power drawn at rated voltage with the motor uncoupled and unloaded — isolates losses inherent to the stator/rotor core and windings from load-dependent losses. Run before stripping and again after rewind, it's the only direct evidence a rewind preserved the motor's efficiency.

*Practitioner usage:* "Pre-strip no-load was 850 watts, post-rewind came in at 880 — that's a 3.5% increase, within the range we'd expect from a properly controlled burnout."

*Common misuse:* treating "the motor runs and doesn't overheat" as proof the rewind was done right — a motor can run fine while carrying 3–5 efficiency points of hidden core damage that only a no-load comparison reveals.

## BPFO/BPFI/BSF/FTF vs. slip-related sidebands

The first four are bearing defect frequencies (outer race, inner race, ball spin, cage/fundamental train) calculated from bearing geometry and shaft speed — they don't move with load or slip. **Slip-related sidebands** (at ±2×slip×line-frequency around the fundamental) are the signature of a rotor-bar or rotor-asymmetry fault, and they shift with load because slip itself changes with load.

*Practitioner usage:* "Those peaks don't match any of the calculated bearing frequencies for this bearing at this speed — check for slip-locked sidebands before we condemn the bearing."

*Common misuse:* calling any non-fundamental vibration peak "a bearing" without calculating whether it actually lands on a bearing defect frequency or a slip-derived rotor frequency.

## Slip

The difference between a motor's synchronous speed (set by pole count and line frequency) and its actual running speed, expressed as a fraction of synchronous speed. It's the number that locates rotor-bar-fault sidebands in a current or vibration spectrum, and it changes with load.

*Practitioner usage:* "At 1750 RPM against a 1800 RPM sync speed, slip is 0.0278 — sidebands should sit about 3.3 Hz off the 60 Hz fundamental if this is a rotor-bar fault."

*Common misuse:* treating slip as a fixed nameplate number rather than something that shifts with actual load — using nameplate full-load slip when the motor was running at partial load during the test throws off the sideband-location math.

## Growler test

A bench test using an induction-coil fixture to detect turn-to-turn or coil-to-coil shorts in a winding by inducing current and checking for an imbalance (steel-strip vibration or ammeter deflection) — catches shorts a standard ground-fault megohmmeter reading won't reveal, since the short is between turns of the same phase, not to ground.

*Practitioner usage:* "IR and PI both looked fine, but the growler showed a dead short between two turns in coil 4 — that's why it was drawing high no-load current."

*Common misuse:* treating a passing megohmmeter test as ruling out all winding shorts — it only tests resistance to ground, not turn-to-turn insulation.

## TIR (total indicated runout)

The total variation in a rotating surface's radius measured with a dial indicator over one full revolution — used on commutators and shaft journals to catch out-of-round conditions before they cause brush chatter or bearing wear patterns.

*Practitioner usage:* "Commutator TIR read 0.06mm, over the 0.05mm chatter threshold — it's going on the lathe before we put new brushes in, or they'll wear unevenly again in a week."

*Common misuse:* eyeballing a commutator or shaft for "roundness" instead of measuring TIR with a dial indicator — out-of-round conditions well under visual detection threshold still cause brush arcing and bearing wear.

## Interference fit (shaft-to-bearing, housing-to-bearing)

The deliberate, small dimensional overlap between a bearing bore and shaft (or a bearing outer race and housing bore) that holds the bearing in place under rotation and load without additional fasteners — specified in thousandths of an inch or hundredths of a millimeter by bearing tolerance class, not "tight enough to need force to install."

*Practitioner usage:* "Shaft measured 0.0004 inch over nominal — that's within the interference-fit spec for this bearing size, good to press on."

*Common misuse:* judging fit by installation feel ("it went on tight, must be fine") instead of measuring against the bearing manufacturer's tolerance class — both too loose and too tight produce premature failure, and neither is detectable by feel alone.

## NEMA Premium / IE efficiency class

Nameplate-stamped efficiency classifications (NEMA Premium in North America; IE1–IE4 internationally) that set the minimum efficiency a motor of a given frame size and speed must meet when new — relevant to rewind-vs-replace economics because an older motor being repaired may predate the efficiency class its replacement would carry, changing the payback math beyond the simple repair-cost ratio.

*Practitioner usage:* "This is a pre-EISA standard-efficiency motor — the replacement would be NEMA Premium, so factor the energy-cost difference into the rewind-vs-replace call, not just the sticker price."

*Common misuse:* comparing rewind cost only against a new motor's purchase price, ignoring that a higher-efficiency replacement changes the long-run operating cost side of the same decision.
