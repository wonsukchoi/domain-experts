# Vocabulary

Terms generalists conflate that a lighting technician keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## DMX universe

One DMX512 data line carrying a fixed 512 channels of control data, regardless of how many physical fixtures share it. A modern moving fixture can consume 20–40+ channels by itself, so a universe holds far fewer *fixtures* than its channel count suggests.

**In use:** "Fourteen movers at 36 channels each is 504 — we're basically full before we even add the conventional dimmers, split it now."

**Common misuse:** assuming "one universe" means "up to 512 fixtures," which is only true if every fixture is a single-channel dimmer; addressable moving fixtures fill a universe far faster.

## RDM (Remote Device Management)

A bidirectional extension of DMX512 (ANSI E1.20) that lets a console query and remotely configure fixture addresses, personalities, and status over the same data line, instead of walking the rig to set addresses by hand.

**In use:** "RDM shows fixture 12 still on its default address — someone swapped it during strike and never re-addressed it."

**Common misuse:** assuming every fixture and every splitter in the chain supports RDM; a single non-RDM device in the line can block discovery for everything downstream of it.

## Soft patch vs. hard patch

**Hard patch** is a fixture's physical DMX address set at the unit. **Soft patch** is the console's internal mapping of console channel numbers to those physical addresses, letting a programmer renumber for convenience without touching hardware.

**In use:** "Don't re-address the fixture, just soft-patch it to a different channel number in the show file — leave the hard patch alone."

**Common misuse:** re-patching in the console and assuming the physical address changed too, or vice versa — the two can silently drift apart if one is changed without updating the other.

## Working load limit (WLL) vs. safety factor

**WLL** is the maximum load a rigging component is rated to carry in normal service. **Safety factor** is the ratio between the component's actual breaking strength and its WLL — entertainment rigging typically targets 5:1 or higher (per ANSI E1.2 and house engineering), well above general industrial norms, because failure happens over people.

**In use:** "That shackle's WLL is 2,000 lb — we're hanging 240, so we're nowhere near it, but the *point* itself isn't rated in the grid plot, and that's the actual unknown."

**Common misuse:** treating WLL as a target to approach rather than a ceiling to stay well under, or citing a component's WLL while ignoring that the structural point it's attached to may be the weaker link.

## Continuous load (the 80% rule)

A load that operates at or near full value for an extended period — a multi-hour show qualifies — must be sized to circuits and breakers derated to roughly 80% of their rating, per the continuous-load logic carried from NEC Art. 210.19/210.20 into entertainment power practice (NFPA 70 Art. 520/530).

**In use:** "That leg's at 86% of the breaker — fine for a five-minute cue-to-cue check, not fine for a two-hour show."

**Common misuse:** applying the 80% derate uniformly to genuinely intermittent loads (a followspot that's only hot for seconds), which wastes real available capacity instead of reserving the derate for actual continuous runs.

## Company switch

The single large connection point (often camlock) where a venue or generator provides bulk power to a touring production's own distribution system, as opposed to the venue's permanently wired house dimmers.

**In use:** "We're pulling off the company switch tonight, not house dimmers — venue's system stays untouched."

**Common misuse:** quoting the company switch's total rated capacity as proof the rig is safe, without checking how that bulk feed gets subdivided and balanced across phases downstream.

## Socapex / multicable vs. home run

**Socapex (or multicable)** bundles multiple circuits (commonly six) into one connector and cable run, cutting cable count at the cost of losing per-circuit independence — one bad pin can take out every circuit in the bundle. A **home run** wires one circuit individually all the way back to the dimmer rack, isolating it completely.

**In use:** "Wash positions go on socapex, fine to lose all six together if a connector fails — the followspot power and the practical stay on home runs."

**Common misuse:** running anything mission-critical (a single special, a practical, followspot power) through multicable for convenience, so an unrelated circuit's failure takes it down too.

## Followspot vs. wash vs. key light

A **followspot** is a manually or remotely aimed narrow-beam light tracking a moving subject live. A **wash** is broad, even, non-specific coverage of an area. **Key light** is the primary light establishing an on-camera subject's exposure and modeling, around which fill and back light are built.

**In use:** "Followspot picks up the soloist at the mic; the wash just needs to hold the rest of the stage so the spot reads as a highlight, not the only light on."

**Common misuse:** using "spotlight" generically for any narrow beam, including a fixed narrow-focus conventional that isn't operated live — a true followspot implies an operator tracking a moving target in real time.

## Gobo vs. iris vs. gate

A **gobo** is a patterned metal or glass insert that projects a shape or texture through a fixture's beam. An **iris** mechanically adjusts a fixture's beam diameter. The **gate** is the internal focal plane inside a fixture where gobos, irises, and shutters all sit in relation to the lens for a sharp image.

**In use:** "Sharpen the gobo edge by racking focus at the gate, then bring the iris in two points to tighten the whole beam."

**Common misuse:** asking to "focus the gobo" when the actual issue is gate alignment or lens distance — gobo sharpness is a function of the whole optical path, not a property of the gobo itself.

## CRI vs. TM-30 (Rf/Rg)

**CRI** (Color Rendering Index) is an older single-number metric (0–100) for how faithfully a light source renders a standard set of reference colors, weak specifically at saturated reds (R9) that matter for skin tone. **TM-30** (IES) replaces it with two numbers — **Rf** (fidelity) and **Rg** (gamut, whether colors are rendered as more or less saturated than reference) — giving a fuller picture, especially for LED sources.

**In use:** "This fixture reads CRI 92 but R9 is only 38 — check its TM-30 Rf/Rg before trusting it on camera for skin tone."

**Common misuse:** treating a high CRI number alone as proof a fixture is broadcast-safe; a fixture can post a strong CRI while still rendering reds and skin tones poorly.

## Gaffer / best boy electric / genny operator

Film and TV set-lighting department roles: the **gaffer** is the department head executing the director of photography's lighting design; the **best boy electric** is the gaffer's second, managing crew, equipment, and logistics; the **genny operator** runs and maintains the generator powering the lighting package on location.

**In use:** "Route that question to the best boy, not the gaffer directly — crew scheduling and equipment calls go through them."

**Common misuse:** using "gaffer" as a generic term for any set electrician; on a unionized set the title maps to a specific role with specific authority, not a catch-all label.

## Practical

A light source that appears as part of the set or scene itself (a lamp, a window, a car's headlights) rather than a purely theatrical/production instrument, often requiring its own dedicated, independently switchable circuit distinct from the general rig.

**In use:** "The table lamp's a practical — home-run it separately so we can kill it on its own cue without touching the wash."

**Common misuse:** patching a practical through the same dimmer/multicable group as unrelated washes for convenience, losing the ability to control it independently on its own cue.

## Cue stack — "standby" vs. "go"

The console's sequenced, numbered list of lighting states triggered in order during a show. **"Standby"** is the verbal warning that a cue is imminent; **"go"** is the explicit call to execute it — the two are never merged into one call, because a crew needs the warning beat to prepare.

**In use:** "Standby cue 34... go" — with a real pause between them, not read as one phrase.

**Common misuse:** calling "go" without a preceding "standby," which removes the crew's preparation window and is exactly the kind of ambiguity a live cue call exists to prevent.
