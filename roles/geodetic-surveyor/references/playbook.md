# Playbook

## 1. Accuracy classification tables

### GPS relative-positioning standard (FGCC 1988) — use for GNSS-observed baselines

| Order | Formula (95% relative accuracy) | Typical use |
|---|---|---|
| AA | 3 mm + 1×10⁻⁸ D | National/global geodynamics, crustal-motion monitoring |
| A | 5 mm + 1×10⁻⁷ D | Primary national/regional network |
| B | 8 mm + 1×10⁻⁶ D | Secondary densification, airport/engineering control |
| Not classically GPS-tabled below B — use classical order/class for further densification with total-station or lower-precision methods | — | — |

D = distance between the two stations, same units as the constant term (mm here). Example: D = 24,300,000 mm (24.3 km), B-order allowable = 8 + (1×10⁻⁶ × 24,300,000) = 8 + 24.3 = 32.3 mm = 3.23 cm.

### Classical order/class (FGCS 1984) — use for traverse/triangulation-based work or as a reference floor

| Order/Class | Formula (95% relative accuracy) | Ratio |
|---|---|---|
| First Order | 1 cm + 1×10⁻⁵ D | 1:100,000 |
| Second Order, Class I | 2 cm + 2×10⁻⁵ D | 1:50,000 |
| Second Order, Class II | 3 cm + 5×10⁻⁵ D | 1:20,000 |
| Third Order, Class I | 5 cm + 1×10⁻⁴ D | 1:10,000 |
| Third Order, Class II | 8 cm (fixed) | 1:5,000 |

## 2. Session design by target classification

| Target order | Minimum independent sessions | Minimum session length | Notes |
|---|---|---|---|
| AA/A | 3 independent sessions, different days | 6+ hours each | Multi-day spread to average atmospheric/orbital geometry variation |
| B | 2 independent sessions, different days | 4 hours each | Standard for engineering/airport-grade densification |
| First order (classical-equivalent) | 2 independent sessions | 2–4 hours each | Shorter acceptable given strong CORS baseline geometry |
| Mapping-grade only (not geodetic control) | 1 session acceptable | 15 min–2 hr | Not a substitute for the above; flag explicitly as non-geodetic if used for control |

Rule of thumb: never accept a single unrepeated session as final control for anything B-order or better — the session count is the redundancy, not the hour count.

## 3. Field log — required fields per session (fill exactly this shape)

```
Station PID / name:        RWY09
Session date:               2026-03-11
Session start (UTC):        14:02
Session stop (UTC):         18:04
Receiver make/model:        [make/model]
Antenna make/model:         [make/model]
Antenna S/N:                [serial]
Height measurement method:  slant (to ARP) — NOT base-of-mount
Measured slant height:      1.673 m (measured twice, agreement to 2 mm)
Sky obstruction check:      >10° elevation mask clear, no metal roofing/fence within 15 m
Observer initials:          [initials]
```
Missing any field (especially height method) is a re-observe, not a note-and-proceed.

## 4. OPUS processing and screening sequence

1. Submit each session's raw observation file to OPUS (or OPUS-Projects for multi-session campaigns) independently — never pre-combine sessions before processing.
2. Confirm OPUS selected 3+ CORS baselines with reasonable RMS (check the solution report's "Peak-to-Peak" and "Overall RMS" fields).
3. Record each session's solution (NAD83(2011) epoch 2010.00 and ITRF/current epoch, both reported by OPUS) separately.
4. Differance independent sessions' solutions component-wise (ΔN, ΔE, ΔU or Δx, Δy, Δz); compute horizontal scatter = √(Δx² + Δy²).
5. Screen against thresholds: horizontal scatter ≤ 3 cm, vertical scatter ≤ 6 cm. Exceeding either → re-observe before proceeding to adjustment, don't average past it.

## 5. Least-squares adjustment sequence

1. **Minimally-constrained pass:** fix only one station's position and the network's orientation (hold nothing else). Run the adjustment.
2. **Screen residuals:** flag any baseline whose residual exceeds ~3x the network's median residual — investigate before continuing (see red-flags.md).
3. **Loop closure check:** for every independent loop, confirm misclosure is within the target order/class allowable from Section 1.
4. **Fully-constrained pass:** fix all selected external control (CORS/published marks) to their published coordinates. Run the adjustment.
5. **Extract accuracy statistics:** semi-major/semi-minor axis of the 95%-confidence error ellipse per new station; compute achieved relative accuracy to nearest control (error / baseline distance) and compare against Section 1's tables.
6. **Accept or reject:** any station failing its target classification is re-observed (additional session) rather than accepted with a caveat.

## 6. Ellipsoidal-to-orthometric height conversion

```
h (ellipsoidal, from GNSS/OPUS)     = 312.847 m  [NAD83(2011), epoch 2010.00]
N (geoid undulation, GEOID18 grid)  = -28.912 m
H (orthometric, NAVD88)             = h - N = 312.847 - (-28.912) = 341.759 m
```
Always cite the geoid model name and version in the deliverable. When GEOID2022 becomes the current NGS model for the project's region, re-derive N and H from the new grid rather than reusing the GEOID18 value — the two grids are not offset by a constant.

## 7. Control-mark selection checklist (before fixing any mark in a fully-constrained adjustment)

- [ ] Datasheet pulled by PID, not by local nickname.
- [ ] Realization/epoch confirmed post-2011 National Adjustment (or explicitly time-transformed if older).
- [ ] Superseded/adjustment date reviewed — flag anything not updated in 15+ years for independent verification before trusting.
- [ ] Site visually checked (or recent photo reviewed) for physical disturbance, obstruction, or damage.
- [ ] At least 3 marks selected with geometric spread around the project, not clustered on one side.

## 8. Frame/epoch statement — required on every coordinate deliverable

```
Datum/Frame: NAD83(2011)
Epoch: 2010.00
Geoid model: GEOID18 (v.[date])
Note: current-epoch (2026) live GPS readings at this location will differ from
the values above by approximately [N] cm horizontally due to reference-frame
motion since epoch 2010.00 — this is expected divergence, not a survey error.
```
