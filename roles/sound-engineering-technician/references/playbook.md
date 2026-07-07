# Sound Engineering Technician — Playbook

## Platform delivery loudness specs (filled reference table)

| Platform/target | Integrated loudness | True peak ceiling | Tolerance | Notes |
|---|---|---|---|---|
| Spotify | -14 LUFS | -1 dBTP | ±1 LU | Louder masters get turned down; quieter ones NOT turned up — mix to spec, don't rely on normalization |
| Apple Music | -16 LUFS | -1 dBTP | ±1 LU | Sound Check normalization applied on playback |
| YouTube | -14 LUFS | -1 dBTP | ±1 LU | Re-encodes audio; leave true-peak margin for codec overshoot |
| Netflix | -27 LKFS (dialogue-gated) | -2 dBTP | ±2 LU | Dialogue-gated measurement excludes silence/music-only passages |
| ATSC A/85 (US broadcast) | -24 LKFS | N/A (RMS-based) | ±2 dB | US TV/cable delivery standard |
| EBU R128 (EU broadcast) | -23 LUFS | -1 dBTP | ±1 LU | European broadcast standard |

## Gain-staging reference levels

| Stage | Target average level | Target peak level | Why |
|---|---|---|---|
| Mic preamp | -18 dBFS | -12 to -6 dBFS | Leaves headroom for unpredictable transients before A/D conversion |
| Individual DAW track | -18 dBFS | -12 dBFS | Matches preamp target; summing multiple tracks at this level avoids bus overs |
| Mix bus (pre-master) | -12 to -6 dBFS | -6 to -3 dBFS | Headroom for mastering/limiting stage |
| Master bus (post-limiter) | Set by delivery spec (see table above) | Spec's true-peak ceiling | Final delivered level |

## Signal-chain troubleshooting sequence

When a noise, distortion, or unexpected level problem appears, isolate stage by stage rather than guessing from the symptom:

1. **Source/mic** — swap or reposition; does the problem follow the mic?
2. **Cable/connector** — swap cable; does the problem persist?
3. **Preamp/interface input** — check gain setting, phantom power state, input impedance match.
4. **Converter (A/D)** — check for clipping at this stage independent of downstream gain.
5. **DAW track** — check track gain, any inserted plugin bypassed one at a time.
6. **Bus/group** — check bus gain and any bus-level processing.
7. **Master/output** — check final limiter and output gain.

Stop at the first stage where the problem disappears when isolated — that stage (or the one immediately before it) is the source.

## Mic-placement distance table (3:1 rule application)

| Mic-to-source distance | Minimum distance to next mic (same source) |
|---|---|
| 6 inches | 18 inches |
| 12 inches | 36 inches |
| 24 inches | 72 inches |

Below these ratios, expect audible comb filtering when the two signals are summed to mono. Past two mics on one source at comparable distance, the rule stops resolving the problem — phase-align in the DAW or accept the coloration as a deliberate tradeoff (e.g. a close mic blended with a room mic for character).

## Loudness-fix decision table

| Situation | Fix |
|---|---|
| Measured loudness below target, true peak has headroom to ceiling | Flat gain increase |
| Measured loudness below target, flat gain would exceed true-peak ceiling | True-peak limiter, driven to hit loudness target |
| Measured loudness above target | Flat gain reduction (limiting rarely needed — you're removing energy, not adding it) |
| Measured loudness within tolerance but at the edge | Nudge toward center of tolerance before final render — protects against downstream re-encode/normalization drift |
