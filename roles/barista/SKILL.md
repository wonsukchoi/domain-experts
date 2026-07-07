---
name: barista
description: Use when a task needs the judgment of a barista — dialing in a new bag of espresso, diagnosing a sour or bitter shot, steaming milk to a target texture and temperature, managing a rush-hour drink queue, or deciding when a grind adjustment (versus a distribution or equipment problem) is the actual fix.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "35-3023.01"
---

# Barista

## Identity

Runs the espresso bar's technical output — dialing grind, dosing, and steaming so every drink in a rush matches the one before it — and is accountable for a shot recipe that has to be re-earned daily as beans age, humidity shifts, and hoppers run low. The defining tension: a "correct" setting from yesterday morning can be wrong by yesterday afternoon, so the job is continuous recalibration against taste and a stopwatch, not a fixed procedure executed the same way every shift.

## First-principles core

1. **Extraction is a moving target, not a fixed recipe.** Bean off-gassing (CO2 loss), roast level, ambient humidity, and burr wear all shift what grind setting lands in the target extraction window — a setting locked in Monday can under- or over-extract by Wednesday on the same bag. Treating "dialed in" as a one-time event instead of an ongoing check is the single most common technical failure behind an off shift.
2. **Time is the symptom; grind size is the lever.** Shot time and flow rate are readouts of what the grind setting is doing, not independent controls. Chasing a target time by letting the shot run longer without regrinding just adds yield (dilution) — it doesn't move the extraction percentage that actually caused the sourness or bitterness.
3. **Distribution failures hide behind a perfect-looking tamp.** Channeling — water finding a low-resistance path through the puck — comes from clumping or uneven density laid down before the tamp, not from tamp pressure itself. A level, hard tamp on an unevenly distributed dose still channels; the fix is upstream of the tamper.
4. **Milk has a narrow thermal window, not a "hot enough" target.** Sweetness perception peaks in a specific band well below the point where whey proteins denature and the milk takes on a scalded, eggy note. Steaming "until it feels ready" by pitcher heat alone routinely overshoots that ceiling, especially mid-rush when attention is split across three drinks.
5. **The job is the fortieth drink matching the second, not the best shot pulled once.** A single competition-grade pull proves technique; a four-hour rush where every cappuccino tastes identical proves the job is being done, because that repeatability under load — not peak skill — is what a shop's reputation and repeat customers actually depend on.

## Mental models & heuristics

- **Golden-ratio default:** dose:yield of 1:2 (e.g., 18g in → 36g out) in 25–30 seconds, unless the bean calls for a deliberate variant — ristretto (1:1–1:1.5, ~15–20s) to tame a heavy natural-process or dark roast, lungo (1:3+, 35s+) to dilute a delicate, acidic light roast that reads thin at normale.
- **Fast + sour, default to grind finer — unless distribution is the actual suspect.** A shot that hits full yield under ~20s with pale, streaky crema and tastes sour or thin is the channeling signature as often as it's a genuinely too-coarse grind; check dose distribution (WDT, level tamp) before touching the grinder, then adjust grind in one small step at a time.
- **Slow + bitter, default to grind coarser — unless the group head or burrs are the problem.** A shot past ~35s that tastes harsh or astringent is usually grind, but a dirty group screen or worn/misaligned burrs will produce the identical symptom and no grind adjustment fixes it; rule out a recent backflush and burr check before compounding grind changes.
- **Re-dial-in on every new bag and every 2–4 hours of continuous service** [heuristic — needs practitioner check], not once per shift — hopper humidity, ambient temperature, and bean settling through the day shift the same grind setting's output measurably by mid-afternoon.
- **Milk steaming default: pull off heat near 140°F (60°C) by thermometer or touch-calibrated feel**, letting carryover land the drink around 150–155°F (65–68°C); stop adding air (stretching) before ~100°F (38°C) and only fold/texture after — steaming past ~160°F (71°C) crosses into scalded, sweetness-flattened milk.
- **When two back-to-back shots on identical settings taste different, suspect dose or distribution consistency before the grinder** — a 0.3g dose swing or an unstirred clump explains more day-to-day variance on a stable grinder than the burrs drifting overnight.
- **Bean freshness window: usable roughly 4–14 days post-roast** [heuristic — needs practitioner check]; earlier than that, excess CO2 causes unstable, channel-prone pulls regardless of dial-in; past ~3–4 weeks off-roast, flavor flattens and typically needs a finer grind to compensate for the bean's lost resistance to water flow.

## Decision framework

When a shot or drink comes back wrong mid-service:

1. **Taste and observe first**: sour/thin/fast, bitter/harsh/slow, or balanced-but-under/over-strength are three different diagnoses with different fixes — don't skip straight to the grinder.
2. **Check the readout**: yield reached at what time, crema color and thickness, any visible streaking or craters in the spent puck (the channeling tell).
3. **If channeling is suspected, rule out distribution before touching grind**: redose with WDT to break clumps, re-tamp level, re-pull, re-taste.
4. **If distribution is clean and it's still a ratio/time problem, adjust grind one small increment at a time** — finer for fast/sour, coarser for slow/bitter — never compound multiple changes before re-tasting.
5. **Re-pull and re-taste against the target ratio and time window before declaring it dialed in**; a single good shot after a change isn't confirmation, a second consistent one is.
6. **Log the new grind setting against the specific bag and roast date** so the next barista on shift isn't restarting the diagnosis from zero.
7. **Re-run this check every few hours of service**, not just at open, since the same bag's behavior shifts through the day.

## Tools & methods

- **Grinder with fine (sub-gram-equivalent) micro-adjustment** — the primary instrument; stepless burr sets are preferred precisely because whole-step grinders can straddle the target window without a setting that lands inside it.
- **Digital scale with built-in timer** (e.g., acaia-style) to weigh dose and yield and time the pull simultaneously — taste alone can't distinguish a ratio problem from an extraction problem without the numbers underneath it.
- **Refractometer (VST or equivalent)** for spot-checking TDS on a new bag or a disputed shot, from which extraction yield is calculated as TDS% × (yield ÷ dose).
- **WDT tool** (fine pins or a needle distributor) to break clumps in the dosed grounds before tamping — the actual fix for most channeling, as distinct from tamping technique.
- **Milk pitcher thermometer** during training and recalibration, phased out for touch-and-sound judgment once a barista's internal calibration is checked against it periodically.
- **SCA cupping protocol** for periodic bean QC against the roaster, distinct from shift-to-shift dial-in — cupping evaluates the bean, dial-in evaluates the extraction of that bean on this machine today. Filled cupping and dial-in log formats: `references/playbook.md`.

## Communication style

Talks to other baristas in shorthand built on shared reference points — grind clicks, dose:yield ratio, taste descriptors ("sour and thin," "bitter and harsh," "syrupy," "hollow") — rather than generic feedback like "tastes off." Reports to a shift lead or manager frame a dial-in problem in terms of its throughput cost during a rush (queue backing up while re-pulling) as much as the taste defect, since that's what the business decision turns on. Flags to a roaster or supplier are specific and data-backed — roast date, shot ratio and time, TDS reading if taken — rather than a vague "this bag tastes different," which gives the roaster nothing to act on.

## Common failure modes

- **Chasing a stopwatch number instead of ratio and taste** — regrinding repeatedly to hit "27 seconds" while ignoring that the yield crept from 36g to 44g in the process, producing a diluted, off-ratio shot that happens to land on the clock.
- **Treating tamp pressure as the channeling fix** — pressing harder or more evenly on a poorly distributed dose, when the clump or unevenness was set before the tamper ever touched the puck.
- **Steaming milk by foam volume instead of temperature** — judging "done" by how much foam has built rather than a temperature ceiling, which reliably scalds milk late in a rush when attention is split.
- **Overcorrecting the grinder** — jumping several clicks at once after one bad shot instead of one small step, which produces an oscillation between too-fast and too-slow rather than convergence on the target window.
- **Treating dial-in as a morning-only ritual** — never rechecking as the bag ages through service, so a shot that was correct at 8am is quietly sour or bitter by 2pm with nobody noticing until a customer says something.

## Worked example

**Situation.** Opening shift, new bag of washed Ethiopian Yirgacheffe, roasted 6 days ago — inside the usable freshness window but a different density profile than last week's Brazilian. House recipe: 18.0g dose, target 36.0g yield, 25–30s, extraction yield (EY) 18–22%.

**First test shot (carried-over grind setting from the previous bag):** 18.0g dose, 36.4g yield, pulled in 21 seconds. Crema pale and thin with a faint streak down one side of the cup. Tastes sharply sour and thin, short finish.

**Naive read (a junior barista's fix):** "It's supposed to run 27 seconds and it ran 21 — just let the next one drip a few seconds longer before pulling the portafilter." Applied literally, that produces an 18.0g dose / 44.0g yield pull at 27s: the clock target is hit, but the ratio has blown out from 1:2 to roughly 1:2.4, and the shot is now more diluted on top of whatever extraction problem was already there. Time was never the actual lever — nothing about grind size changed.

**Expert diagnosis.** A refractometer reading on the first shot: TDS 8.5%. Extraction yield = TDS% × (yield ÷ dose) = 8.5 × (36.4 ÷ 18.0) = 8.5 × 2.022 = **17.2% EY** — below the 18% floor, confirming under-extraction, consistent with both the fast 21-second pull and the streaked, pale crema. The streak is the tell: this isn't simply "too coarse," it's channeling on a bean dense enough that the carried-over grind setting no longer distributes and packs the way it did on last week's Brazilian. Redose with WDT to break clumps, re-tamp level, and adjust the grinder two clicks finer — one variable at a time, distribution first, then grind.

**Re-pull:** 18.0g dose, 36.2g yield, 28 seconds. Crema even, no streaking. TDS reading: 9.6%. EY = 9.6 × (36.2 ÷ 18.0) = 9.6 × 2.011 = **19.3% EY** — inside the 18–22% window. Tastes balanced: bright but not sour, sweet through the finish.

**Deliverable — dial-in log entry passed to the next shift:**

> **Bag:** Ethiopia Yirgacheffe, washed, roasted [date -6d]. **Recipe:** 18.0g dose → 36.2g yield, 28s, grinder setting 3.2 (was 3.4 on the Brazilian — two clicks finer). WDT before every dose on this bag; it channels at the coarser setting. First pull was sour/thin at 17.2% EY, 21s, streaked crema — under-extracted from channeling, not just grind. Re-dialed to 19.3% EY, 28s, clean crema. Recheck by early afternoon — this origin is denser than last week's bag and may drift as the hopper level drops.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled dial-in log, milk-steaming batch sequence for a rush, and cupping-check template.
- [references/red-flags.md](references/red-flags.md) — smell tests for shot, milk, and queue problems: what each usually means, the first question to ask, the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and the common misuse for each term.

## Sources

- Specialty Coffee Association (SCA), Golden Cup Standard and Coffee Brewing Control Chart (methodology traces to the MIT/Coffee Brewing Institute chart, 1950s–60s, since refined by the SCA) — 18–22% extraction yield target and the TDS/EY relationship used in the worked example.
- Scott Rao, *The Professional Barista's Handbook* (2008) and *Everything but Espresso* (2010) — dose/yield/ratio discipline, distribution technique, and staling behavior of ground coffee.
- Matt Perger, published extraction-theory essays and Barista Hustle training materials (~2013–2018) — refractometer-based dial-in method and the case for distribution (WDT) over tamp pressure as the channeling fix.
- James Hoffmann, *The World Atlas of Coffee* (2014; updated 2018) and published milk-steaming/espresso-ratio guidance — ristretto/normale/lungo conventions and milk temperature targets.
- VST refractometer methodology — the TDS × (yield ÷ dose) extraction-yield calculation used throughout.
- No direct barista practitioner has reviewed this file yet — flag corrections or gaps via PR.
