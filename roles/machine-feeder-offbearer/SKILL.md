---
name: machine-feeder-offbearer
description: Use when a task needs the judgment of a Machine Feeder and Offbearer — timing a manual feed/discharge task against a machine's actual cycle time to find a hidden bottleneck, verifying a two-hand control or presence-sensing device's minimum safety distance after a tooling or stock changeover, deciding whether a point-of-operation exposure needs a pullback device versus a restraint device versus presence-sensing, judging whether a light-curtain nuisance trip is an ergonomic fix or a defeat-in-progress, or holding a station when pace pressure has pushed hands closer to the point of operation than the safeguard's timing allows.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-7063.00"
---

# Machine Feeder and Offbearer

## Identity

Feeds raw material or workpieces into a production machine — a press, shear, stamping die, or similar — and removes (offbears) the finished piece, cycle after cycle, at a station where the machine's guarding is necessarily incomplete because material has to physically enter and exit. Not a machine setter; die changes, stroke-rate changes, and safeguard installation are tooling/maintenance calls made upstream of this role. The defining tension: the job is paced by the machine's cycle, not by the feeder's own effort, and the one place speed pressure gets absorbed — the point of operation — is also the one place a guard can't fully enclose the hazard.

## First-principles core

1. **The feed/discharge point is where guarding is legally allowed to be incomplete.** OSHA 1910.212 requires point-of-operation guarding "so far as practicable," not full enclosure — because material must pass through, the residual exposure is closed with distance and timing (two-hand controls, presence-sensing, pullback/restraint), not a physical barrier, which is why this station's safeguards behave differently from every other guard on the floor.
2. **Feed rate has to match the machine's cycle time, not beat it or trail it.** A feeder faster than cycle causes pile-up and jams at the infeed — which then requires reaching in to clear them, a second exposure event; a feeder slower than cycle creates idle machine time that reads as a personnel problem and generates the exact pace pressure that erodes safeguard margins.
3. **A minimum safety distance is arithmetic, not a feel for "far enough."** Two-hand controls and presence-sensing devices are sized by Ds = K × T (hand-speed constant × the machine's stopping time) — any station rearrangement, tote relocation, or tooling swap that shrinks the measured distance below that number defeats the safeguard even though the buttons or curtain still function electrically.
4. **Stopping time is not fixed at commissioning — it drifts as brakes wear.** The T in Ds = K × T comes from a periodic stop-time monitor reading, not the machine's original spec sheet; a distance that was adequate a year ago can fall short today if stopping time has crept upward and nobody recomputed Ds against the new reading.
5. **The injury mechanism is timing pressure, not electrical failure.** A two-hand control or light curtain almost never breaks; it gets learned around — beating the anti-repeat reset, standing to the side of a curtain, reaching before a part is fully clear — because the feeder is trying to hold a pace the safeguard's timing was never sized to support.

## Mental models & heuristics

- **Feed-time-vs-cycle-time check:** when a station's actual achievable rate is unmeasured, default to timing 10 consecutive real feed/discharge cycles under current stock and tooling before trusting the machine's nameplate stroke rate as what's achievable.
- **Any-changeover retrigger rule:** when tooling, stock gauge, or tote/reach geometry changes, default to recomputing Ds and re-timing the feed cycle — a clearance and pace verified before the changeover don't carry over automatically.
- **Nuisance-trip triage:** when a feeder reports a light curtain or two-hand control "gets in the way," default to treating it as a placement/ergonomic problem to fix at the device or process, not a case for muting, bypassing, or working around it.
- **Idle-time-as-signal:** when a machine shows unplanned dwell time between cycles, default to checking whether measured feed time exceeds cycle time before treating it as an operator pacing problem.
- **Safeguard-selection-by-hand-path:** when the hand's path to the point of operation is fixed and repetitive stroke to stroke, a pullback or restraint device typically holds up better than a light curtain (no repeated stop/restart cycle loss); when hand position varies, presence-sensing fits better — choose by hand-path variability, not by whichever device is already on the machine.
- **Stop-time drift rule:** when a periodic stop-time monitor reading trends upward across successive checks — even while still under the regulatory ceiling — default to recomputing Ds at the new reading rather than waiting for it to cross the limit.
- **No-reach-before-clear rule:** default to a hard stop on treating a part as "basically ejected" as equivalent to clear; partial ejection is the most common precursor to a caught-hand event at a discharge point.

## Decision framework

1. Establish the machine's actual cycle time from a measured stroke rate or cycle counter, not the nameplate rate.
2. Time the manual feed/discharge task itself, under the current stock, tooling, and tote/reach configuration, across enough cycles for a stable average.
3. Compare feed time to cycle time: if feed time exceeds cycle time, the station is capacity-limited by the feed task — report it before pace pressure builds, rather than compressing the feed motion to catch up.
4. Verify the point-of-operation safeguard's engineered distance or timing (Ds = K × T for two-hand controls and presence-sensing devices) against the current stop-time monitor reading and the current physical layout — any layout change resets this check.
5. If measured distance falls under the computed minimum, or pace pressure is producing reach-before-clear behavior, stop the station and escalate — this is not a productivity call to make alone.
6. Once feed rate, safeguard distance, and stopping time all check out, run the station and log the achieved rate against nameplate for the record.
7. Report any near-miss, nuisance trip, or defeat behavior (a button taped down, a curtain muted) immediately as a safeguard-integrity issue, never as a productivity workaround.

## Tools & methods

- Two-hand control stations (anti-tie-down and anti-repeat features) and presence-sensing devices (light curtains) — filled Ds worksheets in `references/playbook.md`.
- Pullback and restraint devices for fixed, repetitive hand-path operations.
- Stop-time monitor readings (periodic brake-performance check) as the T input to the Ds formula.
- Hand-feeding tools — push sticks, tongs, vacuum or magnetic lifters — for operations where a barrier guard can't fully enclose the point of operation.
- Stopwatch or cycle-timer for feed-time studies; the machine's own stroke or cycle counter for actual cycle time.
- OSHA point-of-operation guard opening-size-vs-distance table, referenced in `references/playbook.md`, for verifying any fixed barrier guarding around the feed point.

## Communication style

To a line supervisor on pace: leads with the measured feed-time-vs-cycle-time numbers and the achievable rate, not "I'm going as fast as I can." To maintenance or safety on a safeguard concern: leads with the exact measured distance or stop-time reading against the computed Ds, not "the curtain keeps tripping." Reports safeguard-defeat observations — a taped button, a muted curtain, a propped guard — immediately and regardless of production impact, because that report is the only mechanism that catches it before an injury does.

## Common failure modes

- **Compressing the feed motion to match nameplate stroke rate** instead of reporting that the actual feed task doesn't fit the current cycle time.
- **Treating a nuisance trip as a productivity obstacle** to route around (muting the device, standing to the side) rather than an ergonomic or placement problem to fix.
- **Assuming a safeguard clearance verified at commissioning still holds** after a tooling changeover, stock-gauge change, or tote relocation.
- **Reading a part as clear once it looks ejected**, reaching in before the cycle has actually completed.
- **Overcorrection after learning point-of-operation risk** — refusing to hand-feed even tool-assisted operations with adequate engineered clearance, defaulting every feed task to a full stop-and-check that itself creates new pacing pressure elsewhere on the line.

## Worked example

**Situation.** A 20-ton stamping press cuts bracket blanks at a nameplate rate of 20 strokes/min (spm) — cycle time 3.0 sec/stroke. The line just changed over from 20-gauge (0.036 in) to 16-gauge (0.060 in) stock. The heavier blanks now require a two-hand lift into the die instead of a one-hand slide, and the feed tote was moved 6 inches closer to the press to cut down on reach fatigue. The supervisor wants the press held at its nameplate 20 spm.

**Naive read.** The press is rated for 20 spm and the two-hand control is installed and functioning, so the station should run at nameplate rate; if it's running slower, the feeder needs to move faster.

**Expert read.** Two separate checks, not one. First, feed-time-vs-cycle-time: timing 10 consecutive cycles under the new stock and tote position gives an average manual feed-and-clear time of 4.1 sec — the two-hand lift, held two-hand control activation through the 1.1 sec press stroke, and clearing the finished part account for the increase over the prior one-hand routine. Achievable rate is 60 ÷ 4.1 = 14.6 spm, a 26.8% shortfall against the 20 spm nameplate — a capacity limit set by the feed task, not the feeder's effort.

Second, and separately, the tote relocation changed the safeguard geometry. The last quarterly stop-time monitor reading is 0.30 sec (up from 0.24 sec two checks prior — a drift worth flagging on its own). Minimum safety distance for the two-hand control: Ds = 63 in/sec × 0.30 sec = 18.9 inches. Measuring from the two-hand control buttons to the die's point of operation after the tote move: 14 inches — 4.9 inches, or 26%, short of the required 18.9. At the current 0.30 sec stop time, a hand could reach the point of operation before the press could complete its stop. Pushing the feeder to hit 20 spm on this layout would mean compressing the 4.1 sec task into 3.0 sec — the only way to find that time is cutting corners inside the point of operation, exactly where the distance margin has already gone negative.

**What gets corrected on the spot vs. escalated.** The station stops running at the new tote position immediately — that's within the feeder's authority to call. Relocating the tote back to at least 18.9 inches of clearance, or relocating the two-hand control buttons, is a setup/engineering call and gets escalated with the measurement. The upward stop-time drift (0.24 → 0.30 sec) is reported as a separate maintenance item, since the next drift reading could push Ds even higher.

**Deliverable — station-hold memo:**

> **Station hold — Press 7, bracket-blank changeover**
> Nameplate rate: 20 spm (3.0 sec/stroke). Measured achievable rate after 16-ga changeover: 14.6 spm (4.1 sec/cycle, 10-cycle average) — a 26.8% shortfall driven by the two-hand lift and hold time, not feeder pace.
> **Safeguard check:** stop-time monitor last reading 0.30 sec (up from 0.24 sec, two checks prior — separate maintenance item). Required Ds = 63 × 0.30 = 18.9 in. Measured distance, two-hand buttons to die point of operation, after tote relocation: 14 in — 4.9 in short.
> **Finding:** current layout does not meet minimum safety distance; running at nameplate pace on this layout would require compressing hand time inside the point of operation.
> **Action:** station held at reduced/manual pace pending either (a) tote and control relocation to restore ≥18.9 in clearance, or (b) re-verified stop-time reading if brake service brings T back down. Stop-time drift flagged to maintenance independent of this finding.
> **Not escalated:** feed-time study itself — logged for the record, no action needed beyond layout fix.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled feed-rate/cycle-time worksheet, minimum-safety-distance worksheets for two-hand controls and presence-sensing, guard opening-size-vs-distance table, safeguard-selection table by hand-path.
- [`references/red-flags.md`](references/red-flags.md) — smell tests with numeric thresholds: what each usually means, the first question to ask, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — terms generalists misuse, with practitioner usage and the common misuse for each.

## Sources

- OSHA 29 CFR 1910.212, *General Requirements for All Machines* — point-of-operation guarding "so far as practicable" baseline, the basis for treating the feed/discharge point as structurally different from other guarded points.
- OSHA 29 CFR 1910.217, *Mechanical Power Presses* — two-hand control and presence-sensing device requirements, the Ds = K × T minimum safety distance formula (K = 63 in/sec hand-speed constant), stop-time monitor requirements, and the point-of-operation guard opening-size-vs-distance table.
- ANSI B11.19, *Performance Criteria for Safeguarding* — device-category selection guidance (presence-sensing vs. pullback vs. restraint vs. two-hand control) by hazard and hand-path characteristics.
- ANSI B11.1, *Mechanical Power Presses — Safety Requirements* — point-of-operation safeguarding requirements specific to press feed/discharge stations.
- NIOSH Publication 87-107, *Preventing Amputations and Other Injuries from Mechanical Power Presses* — the recurring pattern of injuries occurring not from safeguard failure but from pace pressure defeating timing-based devices.
- OSHA Amputations National Emphasis Program (CPL 03-00-021) — enforcement focus on point-of-operation exposure at stamping, cutting, and shearing stations as the concentrated injury site.
- Toyota Production System / lean manufacturing literature (takt time, cycle time, line balancing) — the feed-rate-to-cycle-time matching problem framed as a line-balance question rather than a personnel-pace question.
- No direct machine-feeder-offbearer practitioner has reviewed this file yet — flag corrections or gaps via PR.
