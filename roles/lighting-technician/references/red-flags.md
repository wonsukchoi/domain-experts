# Red flags

Smell tests a lighting technician catches early in load-in or tech. Format for each: what it usually means, the first question to ask, and the data to pull before anyone touches a breaker or a cue.

## 1. Any phase leg drawing over 80% of its breaker rating on a run over ~3 hours

**Usually means:** the rig was patched by convenience — whichever breaker sat nearest each hang position — instead of by phase balance. The aggregate wattage-vs-service-capacity number looked fine and hid the leg-level problem.

**First question:** "Show me amperage per phase leg, not total connected kVA against the switch rating."

**Data to pull:** the per-phase circuit schedule and dimmer patch sheet; the breaker rating feeding each dimmer rack; whether any load on that leg is genuinely continuous (a multi-hour show) versus intermittent (a followspot).

## 2. DMX flicker or dropout that only appears once fixtures have been running a while

**Usually means:** a daisy-chained run past the reliable device count or cable length, or a missing terminator, causing voltage-drop/reflection errors that heat makes worse — not a fixture defect.

**First question:** "Is there a terminator on the last device in that chain, and how many devices or feet of cable sit before the first splitter?"

**Data to pull:** the DMX patch sheet and physical cable-run log; universe map showing daisy-chain segments versus splitter-fed segments; whether the failure correlates with specific fixtures heating up (thermal) or with total run length (electrical).

## 3. A followspot missing or late on cue

**Usually means:** the cue sheet was never walked with the stage manager at tech, or the spot booth's actual sightline to the mark was never checked from that specific angle — not that the operator is careless.

**First question:** "Did the spot op rehearse this cue sheet from the actual booth position, and can they physically see the mark from there?"

**Data to pull:** the numbered spot cue sheet; booth sightline notes from tech; whether the mark or blocking changed after the spot cues were set.

## 4. Visible sag or unexpected deflection at a rigging point

**Usually means:** the point is carrying more than its working load limit, or a multi-point hang is missing a bridle/spreader that would have distributed the load — this is a stop-work signal, not a note-for-later.

**First question:** "What's the documented working load limit for this specific point, and what's the actual measured load on it right now?"

**Data to pull:** the venue's grid plot with per-point WLL; the rigging plot showing what's hung from that point; the safety factor achieved versus the target (generally 5:1 or higher per ANSI E1.2 and house engineering).

## 5. Matched fixtures rendering color inconsistently across a symmetric position

**Usually means:** LED binning variance across production batches, or a firmware/calibration mismatch between units bought or rented at different times — not a gel or gobo problem.

**First question:** "Are every one of these units on the same firmware version and the same color-calibration batch?"

**Data to pull:** firmware version per fixture; purchase/rental batch and serial ranges; whether the mismatch is visible in white light only or across the full color range (narrows it to calibration versus a specific LED channel).

## 6. A fixture at the same position failing or derating repeatedly

**Usually means:** insufficient back-vent airflow at that hang position causing thermal shutdown, or an over/under-voltage condition specific to that circuit — rarely "just a bad unit," especially if a swapped-in replacement fails there too.

**First question:** "Does a known-good fixture from a different position fail at this same spot, or does this specific unit fail everywhere it's hung?"

**Data to pull:** measured voltage at that specific circuit under load; airflow/clearance at that hang position; failure log by position versus by serial number.

## 7. Board's cue doesn't match the focus notes on paper

**Usually means:** someone re-patched a fixture's DMX address after focus was logged, and the console's soft patch was never reconciled back to the focus sheet — the paper and the board have quietly diverged.

**First question:** "Has anything been re-patched since focus, and was the change called back to whoever's holding the focus notes?"

**Data to pull:** the patch sheet's revision history/timestamp; the focus log; console show file version compared against the last confirmed-good save.

## 8. Strike running long enough to trigger overtime

**Usually means:** the crew struck "whatever's easiest to reach" instead of reversing the load-in sequence, or cable wasn't labeled by run during load-in, so nobody can tell what belongs to which circuit without tracing it live.

**First question:** "Are we striking in the reverse of the hang order, and is every cable labeled by run, not just by type?"

**Data to pull:** the load-in hang order and timestamp log; cable labeling convention used; a count of how many circuits had to be traced live versus read off a label.

## 9. A generator's voltage sags when a bank of fixtures kicks on together

**Usually means:** the genny is undersized for the combined connected load plus inrush, or fuel/load management didn't account for the continuous-load derating that applies to a generator feed the same way it applies to a house company switch.

**First question:** "What's the genny's rated continuous output, and what's the actual combined connected load of everything it's feeding, including inrush on simultaneous strike?"

**Data to pull:** generator nameplate continuous rating; connected load list for everything on that genny; timing of the voltage sag relative to which fixture bank fired.

## 10. A house's existing dimmers "look dim" compared to a touring rig's rental fixtures

**Usually means:** an older SCR dimmer curve mismatched against the touring rig's expectations, or a non-dim (relay) circuit was mistakenly patched through a dimmer channel — not that the house rig is simply weaker.

**First question:** "Is that circuit actually patched to a dimmer, or is it a non-dim/relay circuit being asked to dim?"

**Data to pull:** the house's dimmer-vs-non-dim circuit schedule; dimmer curve/type documentation; a side-by-side intensity reading at matched percentages between house and touring fixtures.
