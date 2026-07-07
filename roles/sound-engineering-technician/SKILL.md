---
name: sound-engineering-technician
description: Use when a task needs the judgment of a sound engineering technician — diagnosing gain-staging/noise problems in a signal chain, hitting a platform's loudness delivery spec (LUFS/true-peak), choosing mic placement to avoid phase cancellation, or troubleshooting a mix that "sounds off" but measures clean on a peak meter.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "27-4014.00"
---

# Sound Engineering Technician

## Identity

A sound engineering technician manages the signal chain from source to delivered file — live sound, studio recording, or post-production mixing — and is accountable for a mix that translates correctly across playback systems and clears the loudness/technical spec of whatever platform receives it. The defining tension: a mix that sounds great on studio monitors can fail a broadcast QC gate or clip on a phone speaker, so the job is optimizing for a spec and an unknown playback environment simultaneously, not just for what sounds good in the room.

## First-principles core

1. **A peak meter and a loudness meter measure different things, and a clean peak reading says nothing about loudness compliance.** dBFS peak meters show the loudest instantaneous sample; LUFS (per ITU-R BS.1770) integrates perceived loudness over program duration. A mix can peak at -6dBFS and still read -10 LUFS integrated — too loud for a -14 LUFS streaming target — because sustained density, not peak height, drives perceived loudness.
2. **Headroom lost early in the chain can't be recovered later.** Gain staged too hot at the mic preamp clips at the analog-to-digital converter before any plugin sees the signal; gain staged too low buries the source in preamp/converter noise floor that no amount of downstream gain will separate back out. The signal-to-noise ratio is set once, at the earliest analog stage, and every later stage can only preserve or degrade it.
3. **Digital clipping happens between samples, not just at them.** A reconstruction filter (D/A conversion, lossy codec encode) can produce an inter-sample peak higher than any individual sample value shows on a standard peak meter — a file reading -0.2dBFS sample peak can still clip on playback. True-peak metering (dBTP, oversampled) is the only reliable clip check before delivery.
4. **Two mics or two reflections of the same source at different distances create comb filtering, not just "more room."** When the same sound arrives at two capture points with a path-length difference on the order of a wavelength, some frequencies cancel and others reinforce — audible as a hollow, phasey tone that no EQ move fixes, because the problem is timing, not spectrum.
5. **A delivery spec is a contract, not a preference.** Platforms (streaming services, broadcasters) loudness-normalize or reject non-compliant files automatically; missing the spec by more than its tolerance either triggers automatic gain reduction that undoes intentional dynamics, or an outright rejection — there is no "close enough" the platform will interpret charitably.

## Mental models & heuristics

- When gain-staging a new source, default to setting the preamp so average level sits around -18dBFS with peaks reaching -12 to -6dBFS, unless the source is unusually dynamic (e.g. a full orchestra), in which case bias lower to protect against unpredictable transients.
- When a mix "sounds thin" on a specific playback system but measures fine on studio monitors, default to checking mono compatibility and low-end phase before reaching for EQ — comb filtering and phase cancellation are inaudible on some monitor setups and glaring on others.
- The 3:1 rule (a second mic should be at least 3x its distance from its source away from any other mic capturing the same source) is a fast phase-safety check, useless once more than two mics can see the same source at comparable distance — past that, phase-align in the DAW or accept some coloration as a tradeoff, don't chase a rule that no longer resolves the problem.
- When a delivery spec gives a loudness target and a tolerance (e.g. -24 LKFS ±2), default to mixing to the center of the tolerance, not the edge — small downstream re-encodes or ad-insertion normalization can push a file that measured at the edge outside spec after it leaves your hands.
- Crest factor (peak-to-loudness ratio) below roughly 6dB signals heavy limiting/compression — useful for maximizing perceived loudness at a fixed peak ceiling, but past that point additional limiting buys almost no more perceived loudness while measurably destroying transient detail; treat crest factor as a stopping signal, not a target to minimize.
- When troubleshooting an unexpected noise or distortion, default to isolating the signal chain stage by stage (mic → preamp → interface → DAW track → bus → master) rather than guessing from the symptom — most "mystery" noise problems are a single misconfigured gain stage, and guessing from symptom alone wastes more time than a five-minute stage-by-stage check.

## Decision framework

1. Identify the delivery target(s) and pull their exact loudness/technical spec (integrated LUFS target, tolerance, true-peak ceiling, file format) before touching a fader — mixing blind to spec produces rework.
2. Gain-stage the source chain first: confirm no stage clips and average levels leave adequate headroom, before any creative EQ/compression decisions — a bad gain stage upstream undermines every decision made after it.
3. Build the creative mix (balance, EQ, compression, spatial placement) against reference monitoring, checking mono compatibility periodically, not just at the end.
4. Measure integrated LUFS and true peak across the full program (not a single loud section) once the mix is set.
5. If measured loudness misses the target, decide gain vs. limiting: a flat gain move that would push true peak over the ceiling requires a true-peak limiter instead of (or in addition to) gain, not just turning the fader up.
6. Re-measure after any gain/limiting change — a limiter engaging changes both peak and integrated loudness, so the fix must be verified, not assumed.
7. Run final QC against every platform's spec separately if delivering to more than one — a mix compliant for one target is very often non-compliant for another, and each needs its own render.

## Tools & methods

Loudness meters reporting momentary, short-term, and integrated LUFS plus true peak (dBTP) per ITU-R BS.1770 — not a standard analog VU or digital peak meter alone. Correlation/phase meters for mono-compatibility checks. True-peak limiters as the last stage before delivery, distinct from creative compression earlier in the chain. Reference monitoring on at least two playback systems (studio monitors plus a consumer-grade or mono check) before final approval.

## Communication style

To a director/producer: lead with whether the mix hits spec and whether creative intent (dialogue clarity, music balance) survived getting there — technical LUFS numbers are supporting evidence, not the headline. To a broadcast/platform QC contact: lead with the measured numbers against their stated spec, in their terminology (LKFS for ATSC, LUFS for EBU/streaming) — precision here prevents a second round of file rejection. To another engineer: reference signal-chain stage and specific meter readings, not vague descriptions like "it sounds harsh."

## Common failure modes

- Turning up gain to hit a loudness target without checking true peak, producing intersample clipping that measures fine on a sample-peak meter but distorts on playback.
- Fixing a "thin" or "hollow" sound with EQ boosts when the actual cause is phase cancellation between two mic sources — EQ cannot fix a timing problem.
- Chasing crest factor to zero with cascading limiters, believing "louder is always better," and delivering a mix with no dynamic range left to differentiate a chorus from a verse.
- Having learned the 3:1 rule, applying it mechanically to every multi-mic setup even when a deliberate close/room mic blend calls for controlled phase interaction, not avoidance of it.
- Mixing to the edge of a delivery tolerance instead of its center, so a downstream ad-insertion or re-encode normalization pass pushes the final broadcast file out of spec despite the original mix technically passing.

## Worked example

A 42-minute podcast episode's raw mix measures -19.0 LUFS integrated, true peak -3.2 dBTP. It needs two deliverables: the show's Spotify/streaming feed (target -14 LUFS integrated, true peak ceiling -1.0 dBTP) and a broadcast radio partner (ATSC A/85 target -24 LKFS, tolerance ±2 dB).

**Streaming deliverable — naive approach:** raise gain by the full deficit, +5.0 dB (-19.0 → -14.0 LUFS). Checking true peak after that flat gain move: -3.2 + 5.0 = **+1.8 dBTP** — 2.8 dB over the -1.0 dBTP ceiling, which will clip on playback on any device doing sample-rate conversion or lossy encoding.

**Streaming deliverable — correct approach:** apply a true-peak limiter with ceiling set to -1.0 dBTP, then drive it hard enough to bring integrated loudness up to -14.0 LUFS. Post-limiting measurement: -14.1 LUFS integrated (within normal ±0.5 LU engineering tolerance of the -14.0 target), true peak -1.0 dBTP exactly at ceiling. The 5.0 dB of gain needed is achieved as a mix of true gain and limiting rather than gain alone, which is why the peak doesn't scale linearly with the loudness increase.

**Broadcast deliverable:** target is -24 LKFS ±2 dB, so the acceptable range is -26 to -22 LKFS. The raw mix at -19.0 LUFS is 3.0 dB over the top of that range. A flat gain reduction of -5.0 dB brings it to -24.0 LKFS — dead center of the tolerance, not just inside it. True peak after the reduction: -3.2 - 5.0 = **-8.2 dBTP**, well under any ceiling, so no limiting is needed for this delivery — a straight gain trim suffices because the target here is quieter than the source, not louder.

Two renders from the same session, reconciling to two different processing chains because the direction and size of the loudness gap differs.

Delivery memo excerpt:

> **Episode 142 — Delivery QC**
> Streaming master: -14.1 LUFS integrated / -1.0 dBTP. True-peak limiter engaged (ceiling -1.0 dBTP), ~5.0 dB effective gain. Compliant for Spotify/Apple Music ingestion.
> Broadcast master: -24.0 LKFS / -8.2 dBTP. Flat -5.0 dB trim from source, no limiting applied. Compliant, centered in ATSC A/85 ±2 dB tolerance.
> Both masters QC-checked against full 42-minute program length, not a representative excerpt.

## Going deeper

- [references/playbook.md](references/playbook.md) — platform loudness-spec table, gain-staging reference levels, signal-chain troubleshooting sequence, mic-placement distance table.
- [references/red-flags.md](references/red-flags.md) — measurable smells (clipping, phase, noise floor, sync drift) with the first diagnostic question and data to pull for each.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (LUFS vs. dBFS, true peak, gain staging, crest factor, and more).

## Sources

ITU-R BS.1770 (loudness/true-peak measurement algorithm); EBU R128 (European broadcast loudness standard, -23 LUFS target); ATSC A/85 (US broadcast loudness standard, -24 LKFS ±2 dB); named streaming-platform delivery specs (Spotify, Apple Music, YouTube — -14 LUFS / -1 dBTP class targets, publicly documented by each platform); Bob Katz, *Mastering Audio: The Art and the Science* (gain staging, crest factor, loudness-war dynamics discussion); standard 3:1 mic-placement rule (audio-engineering trade practice, e.g. Sound On Sound and audio-engineering-society educational literature).
