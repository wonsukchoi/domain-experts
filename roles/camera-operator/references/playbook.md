# Playbook

Filled examples of the artifacts a camera operator actually produces and uses day to day: camera reports, a headroom/noseroom reference, dual-aspect safe-zone math, and a shutter-angle cheat sheet.

## Camera report (per setup, filled example)

Travels with footage to editorial/DIT; the operator's flags are what save a dailies review from re-deriving problems from scratch.

| Scene | Take | Roll/Card | Lens | T-stop | ND | Frame rate | Shutter | Circle? | Operator flag |
|---|---|---|---|---|---|---|---|---|---|
| 14A | 1 | A014_0301 | 50mm | T2.8 | 0.9 | 24fps | 180° | No | Reframe late on actor cross, ~6 frames — hold for review |
| 14A | 2 | A014_0301 | 50mm | T2.8 | 0.9 | 24fps | 180° | Yes | Clean, matches blocking rehearsal |
| 14A | 3 | A014_0301 | 50mm | T2.8 | 0.9 | 24fps | 180° | No | Line crossed — B-cam drifted past axis on the reverse, do not cut against 14A/2 |
| 14B | 1 | A014_0302 | 85mm | T2.0 | 0.6 | 24fps | 180° | Yes | Focus soft on actor's final line — confirm with 1st AC before wrap |

**Reading it:** Take 2 is the protected circle take. Take 1 is held in reserve only if editorial needs the extra half-second of reaction the actor gave. Take 3 is flagged unusable against the reverse angle regardless of how it looks in isolation — the line-cross makes it a non-starter for a cut, not just a lesser take. Take 4 (14B/1) is circled but flagged, which tells editorial and the DP exactly what to check before locking a scene on it — an operator who circles clean and silently omits the focus note has produced a landmine, not a favor.

## Headroom / noseroom reference

Values are house-style defaults, not universal law — always confirm the production's shot-style guide first.

| Shot size | Headroom (frame from top of head to top of frame) | Noseroom / lookspace |
|---|---|---|
| Wide/establishing | Generous, ~15–20% of frame height | N/A — full environment context is the point |
| Medium (waist-up) | ~10–12% of frame height | Full third of frame in the direction of gaze/movement |
| Close-up | ~5–8% of frame height | Reduced, roughly a sixth of frame — enough to avoid a "trapped" look, not enough to feel loose |
| Extreme close-up | Near zero — frame can crop top of head deliberately | Minimal; composition reads by eye placement, not by rule-of-thirds math |

**Rule of thumb progression:** headroom shrinks and noseroom shrinks roughly in proportion as the shot gets tighter — a close-up with wide-shot-style headroom looks like a framing mistake, not a stylistic choice, unless a director has specifically called for that discomfort (e.g., horror, interrogation scenes).

## Dual-aspect safe-zone math (16:9 capture, common verticals)

Given a 16:9 capture at resolution `W × H`, the centered vertical-safe width for a target `a:b` output (holding full height) is:

```
safe_width = H × (a / b)
safe_zone_start = (W − safe_width) / 2
safe_zone_end   = safe_zone_start + safe_width
```

| Capture res | Target crop | safe_width | safe zone (x-range) |
|---|---|---|---|
| 1920×1080 | 9:16 (vertical) | 1080 × 9/16 = 607.5px | 656px – 1264px |
| 1920×1080 | 1:1 (square) | 1080px | 420px – 1500px |
| 3840×2160 (UHD) | 9:16 | 2160 × 9/16 = 1215px | 1312.5px – 2527.5px |
| 3840×2160 (UHD) | 4:5 (social portrait) | 2160 × 4/5 = 1728px | 1056px – 2784px |

**Default when a shot must survive more than one downstream ratio:** frame the subject inside the *narrowest* safe zone in the table above (usually 9:16), with margin for handheld drift — the widest ratio never clips if the narrowest one doesn't.

## Shutter-angle cheat sheet (180° default and common deviations)

Exposure time per frame ≈ `shutter_angle / 360 / frame_rate`.

| Frame rate | 180° (default, natural blur) | 90° (crisper, used for action) | 45° (Saving Private Ryan-style stutter) | 360° (max blur, dreamlike) |
|---|---|---|---|---|
| 24fps | ≈1/48s (rounds to 1/50s) | ≈1/96s | ≈1/192s | 1/24s |
| 30fps | ≈1/60s | ≈1/120s | ≈1/240s | 1/30s |
| 60fps | ≈1/120s | ≈1/240s | ≈1/480s | 1/60s |

**Default:** hold 180° unless the DP has specified otherwise for a stylistic reason — a shutter angle that drifts between setups on the same scene (e.g., an operator's rig defaults back to 90° after a battery swap) produces a motion-blur mismatch that reads as a continuity error, not a stylistic choice, once cut together.
