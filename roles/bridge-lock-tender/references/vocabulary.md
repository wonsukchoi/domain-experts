# Vocabulary

Terms generalists flatten into loose synonyms that a tender keeps sharply separate, because the distinction is what a regulation or a safety sequence actually hinges on.

## Opening on signal vs. scheduled opening

**Opening on signal** is the federal default under 33 CFR Part 117: the bridge opens promptly whenever a vessel gives the required request, no advance notice needed. A **scheduled opening** is a structure-specific exception published in that structure's own 117.xxx section, restricting openings to certain hours or requiring advance notice — and that exception itself usually carries its own carve-outs.

*In use:* "This bridge isn't opening-on-signal during the commute window — it's scheduled, but the tow gave the notice the schedule requires, so we open anyway."

*Common misuse:* treating "scheduled" as if it means "closed," when it actually means "opens under a different, still-mandatory condition."

## Interlock

An electrical/mechanical system that physically prevents one motion (span lift, gate closure) from starting until a prior motion (gate-down, chamber-clear) is confirmed by a limit switch, not by a timer or a visual check.

*In use:* "The interlock never released the lift command — the down-switch on gate two never tripped, so the span physically couldn't move even if I'd pressed lift."

*Common misuse:* calling any safety procedure or checklist an "interlock." A checklist is a human process; an interlock is a hardware/software lockout that doesn't care whether the human skipped a step.

## Bascule vs. swing vs. vertical-lift span

**Bascule** spans pivot upward like a drawbridge leaf (single or double-leaf). **Swing** spans rotate horizontally around a central pier. **Vertical-lift** spans rise straight up between towers, keeping the roadway horizontal throughout. Each has a different interlock geometry and a different failure signature.

*In use:* "It's a vertical-lift span, so the failure mode we watch for is the counterweight cable, not the trunnion bearing we'd worry about on a bascule."

*Common misuse:* using "drawbridge" as a catch-all for all three types when writing an incident report — the mechanism matters for root-causing a failure.

## Lift vs. head

**Lift** is the vertical distance a lock chamber's water level moves between low pool and high pool for that specific lock. **Head** is the instantaneous water-level differential across the closed gates at any moment during the fill or empty cycle — it starts at the full lift value and decreases to zero as the chamber equalizes.

*In use:* "The lock's lift is 18 feet, but right now, three minutes into the fill, head is down to about 5 feet — that's why we can safely move to full valve opening at this stage."

*Common misuse:* using "head" and "lift" interchangeably; lift is a fixed property of the lock, head is a moving number during the cycle.

## Culvert valve (filling/emptying valve)

The gate-controlled opening in a lock's culvert system that admits or releases water to raise or lower the chamber. Staged incrementally rather than opened fully at once, because full-open against high head creates turbulence.

*In use:* "Bring the filling valve to 25% and hold — we're still at 11 feet of head, too much for the next stage yet."

*Common misuse:* referring to the culvert valve as simply "the valve" in a log entry with multiple valves in play, which makes a later incident review impossible to reconstruct precisely.

## Air draft vs. draft vs. horizontal clearance

**Draft** is how deep a vessel sits below the waterline. **Air draft** is how tall a vessel is above the waterline — the number that determines whether it clears a bridge without an opening at all. **Horizontal clearance** is the channel width available between fenders, piers, or a lock's chamber walls.

*In use:* "Their air draft is 14 feet at low tide; our fixed clearance here is 12 — they need the opening regardless of how shallow their draft is."

*Common misuse:* citing a vessel's draft when the relevant number for a bridge opening decision is air draft — they aren't correlated, and a shallow-draft vessel can still have a tall air draft (e.g., a sailboat mast).

## VHF Channel 13 vs. VTS channel

**Channel 13** is the designated bridge-to-bridge frequency under 33 CFR Part 26 that bridge tenders and vessels use directly for opening requests and coordination. A **VTS (Vessel Traffic Service) channel** is a separate frequency a port authority's traffic center uses to sequence vessel movement across an entire harbor or river system — a tender may need to monitor both if the structure sits inside a VTS zone.

*In use:* "Get the tow's intentions on 13 for the opening itself, but their overall transit sequence through the harbor is being run on VTS — check both before committing to a time."

*Common misuse:* assuming a single radio channel covers both purposes; a busy VTS zone superimposes a broader sequencing authority on top of the bridge's own opening request channel.

## Lockage

A single complete cycle of a vessel entering a lock chamber, the chamber equalizing, and the vessel exiting on the other side — the standard unit of work for lock operations, distinct from a bridge "opening," which is the span-cycle unit.

*In use:* "We can combine three recreational boats into one lockage, but that tug needs its own — the chamber's not wide enough to lock them together safely."

*Common misuse:* using "opening" and "lockage" interchangeably in reports covering a combined bridge-and-lock structure; they're governed by different regulations and have different safety sequences.

## District-office exception vs. informal hold request

A **district-office exception** is a Coast Guard-authorized deviation from the posted schedule, with its own documentation and legal standing. An **informal hold request** — a supervisor, event organizer, or local official asking the tender to delay openings for a parade or event without going through the district office — carries no such standing.

*In use:* "I can't hold openings for the festival on your say-so — get it authorized through the district office first, then I'll log it as an exception."

*Common misuse:* treating a verbal or local request as equivalent to an authorized exception; acting on it anyway shifts liability for any resulting delay onto the tender personally rather than the authorizing agency.

## Danger signal vs. delayed-opening signal

Under the standardized sound-signal code, a **delayed-opening signal** (one prolonged blast plus two short blasts) tells an approaching vessel the draw will open but not immediately. A **danger signal** (five or more short blasts) tells the vessel the draw will not open at all right now — a materially different message that changes what the vessel should do next.

*In use:* "We gave the danger signal, not the delay signal — that tow needs to hold position or turn, not just slow down and wait."

*Common misuse:* treating any non-immediate response as interchangeable "not yet" signaling; the two codes carry different instructions to the vessel and mixing them up creates a genuine collision-course risk.
