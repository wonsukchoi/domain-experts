# AV Install Playbook

Filled worksheets for the four calculations that get argued after handoff: screen size, screen brightness, signal-run transport, and room acoustics — plus the EDID diagnostic sequence and a commissioning checklist.

## 1. Screen size worksheet (viewing distance → minimum image height)

Ratio: farthest viewer distance ÷ image height ≤ 6 (analytical/detailed content: spreadsheets, CAD, fine text) or ≤ 8 (basic content: video, large-type slides).

| Room type | Farthest viewer | Content type | Ratio | Min. image height | Min. diagonal (16:9, height=0.49×diag) |
|---|---|---|---|---|---|
| Huddle room | 8ft (96in) | Basic (video call) | 8 | 12in | 25in |
| Standard conference room | 20ft (240in) | Analytical (spreadsheets) | 6 | 40in | 82in |
| Training room | 30ft (360in) | Analytical (fine text) | 6 | 60in | 122in |
| Auditorium | 60ft (720in) | Basic (slides/video) | 8 | 90in | 184in |

Rule: always round the specified diagonal *up* to the nearest stock size above the calculated minimum — never down, and never to the minimum exactly (no margin for people seated beyond the "farthest viewer" assumption during an overflow meeting).

## 2. Brightness worksheet (ambient lux → minimum nits)

Take the lux reading at the screen face with shades/blinds in their most-open realistic position (not blacked out — that's not how the room will actually be used).

| Ambient light at screen | Bracket | Minimum display brightness | Notes |
|---|---|---|---|
| <150 lux (blackout-capable / windowless) | Low | 300–350 nits | Standard commercial conferencing panel is adequate. |
| 150–300 lux (interior room, some ambient) | Medium | 350–500 nits | Typical office conference room with shades drawn. |
| 300–500 lux (glass wall, shades open) | High | 500–700 nits | Matches the worked-example room (450 lux → 500 nit spec). |
| >500 lux (direct sun exposure at screen) | Very high | 700–1500 nits, or reposition/add anti-glare treatment | Consider whether the screen placement itself is the actual fix. |

This is integrator-standard bucketed guidance (Extron/commercial-display-manufacturer spec sheets), not a single formula — treat the boundaries as ±50 lux, not exact cutoffs.

## 3. Signal-run transport table (distance ceilings by transport)

| Transport | Practical distance ceiling | Resolution/chroma held | When to use |
|---|---|---|---|
| Passive HDMI (2.0/2.1 certified cable) | ~15ft (5m) | 4K60 4:4:4 | Rack-to-display within the same closet/credenza only. |
| Active/optical HDMI cable | Up to ~100ft (30m) | 4K60 4:4:4 | Single run, no switching needed, budget-sensitive. |
| HDBaseT (standard class extender) | ~230ft (70m) | 4K30 or 4K60 4:2:0 | Long single run, lower-bandwidth content acceptable. |
| HDBaseT (higher-bandwidth 18Gbps-class extender) | ~130–150ft (40–46m) | 4K60 4:4:4 | Long run where full-chroma 4K60 is required — check the specific extender's class rating, this ceiling drops as bandwidth rises. |
| AVoIP (1Gb network, e.g. NVX/NAV/Q-SYS) | Limited only by network topology, not cable distance | 4K60 4:4:4 (codec-dependent) | Matrix-switched or multi-room/campus distribution, not a single point-to-point run. |

Rule: spec against the *lowest* ceiling in the chain — a 4K60 4:4:4 source through a 4K30-rated extender caps the whole run at 4K30, regardless of what the display supports.

## 4. Acoustic design worksheet

- **RT60 target:** 0.6–0.8 seconds for a conferencing/huddle room; above 0.8s, add absorptive treatment (ceiling tile, wall panels, or soft furnishings) before blaming the mic or codec.
- **NC (noise criteria) target:** NC-30 to NC-35 for conference rooms (HVAC/background noise); above NC-35, background noise competes with speech pickup regardless of mic quality.
- **Speaker spacing (distributed ceiling):** spacing between adjacent speakers ≈ 1.5–2x the mounting height above ear level (seated ear height ≈ 4ft/1.2m). Example: 9ft ceiling, drop to a 9ft mount height minus 4ft ear height = 5ft effective height → spacing ≈ 7.5–10ft between speakers.
- **STI (Speech Transmission Index) target:** ≥0.6 ("good") for conferencing; below 0.45 ("poor") is a redesign trigger, not a settings tweak.

Worked spacing example: a 24ft × 16ft conference room, 9ft ceiling. Effective mounting height above ear level = 9 − 4 = 5ft. Spacing target = 5 × 1.75 (midpoint of 1.5–2x) ≈ 8.75ft. Room width 16ft ÷ 8.75ft ≈ 1.8, so 2 rows; length 24ft ÷ 8.75ft ≈ 2.7, so 3 columns — a 2×3 grid of 6 ceiling speakers, adjusted to align with the actual ceiling grid rather than forcing the raw math onto tile lines that don't exist.

## 5. EDID diagnostic sequence (source-to-sink handshake failure)

Run in this order — each step is cheaper and faster than the next, so don't skip ahead:

1. **Reproduce with a different source at the same sink over the same run.** If a second source (e.g. a laptop) works where the original source (e.g. a room PC) doesn't, the cable/run/sink are confirmed good — the fault is source-side negotiation, not the physical layer.
2. **Pull the sink's currently-negotiated EDID with a handheld reader** and compare it against the display's actual native EDID (resolution list, timings, audio block). A mismatch (e.g. a generic 1080p60 fallback table instead of the display's native 4K table) points at an intermediate device's EDID handling, not the display itself.
3. **Check every switcher/extender/scaler in the chain for its EDID management mode** — "internal/fixed," "downstream/pass-through," or "learned" — and confirm it's set to pass through the actual sink's EDID rather than substituting a canned table.
4. **Separately verify HDCP compliance at each link** (source, any switcher/extender, sink) — an EDID that negotiates correctly but an HDCP mismatch downstream produces the same blank/flickering symptom and is a distinct failure mode.
5. **Only after 1–4 are exhausted, treat it as a physical-layer fault** (connector, cable, or run-distance issue) and re-terminate or re-run.

## 6. Commissioning / handoff checklist

- [ ] EDID/HDCP handshake verified clean on every input, not just the one used for the acceptance demo.
- [ ] Signal run distances measured and logged against each transport's rated ceiling (not just "it displayed an image").
- [ ] Display brightness and ambient lux reading logged together, with the bracket used to justify the spec.
- [ ] RT60/STI or at minimum a subjective speech-clarity test conducted with the room's actual furniture and occupancy, not an empty shell.
- [ ] Control-system programming signed off separately by the certified programmer of record, with a named scene-by-scene test log.
- [ ] As-built rack elevation, cable labeling, and signal-flow diagram delivered to the client — not just left in the installer's own files.
- [ ] Trouble-ticket escalation path documented: who gets called, and what diagnostic step happens first (see section 5 above).
