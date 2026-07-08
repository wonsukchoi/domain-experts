# Deployment Playbook

Concrete templates and sequences for the four phases: site survey, tag/reader/antenna selection, in-situ matching, pilot monitoring. Numbers are defaults from field practice — deviate consciously and log why in the site file.

## 1. Site-survey checklist (run before quoting hardware)

Walk the facility with a spectrum analyzer, handheld reader, and floor plan. Fill this per zone (a zone = one dock door, one portal, one shelf run):

| Field | Zone A (dock door 4) | Zone B (shelf run 12) |
|---|---|---|
| Ambient RF noise floor (dBm, 902–928 MHz) | −78 dBm | −82 dBm |
| Metal within 1 m of planned antenna position | Steel roll-up door, 0.6 m | Wire shelving, 0.3 m |
| Liquid/moisture sources | None | Sprinkler head overhead |
| Existing 2.4 GHz / Wi-Fi APs within 10 m | 2 (channel 6, 11) | 1 (channel 1) |
| Tag orientation at read point | Random (hand-stacked pallets) | Fixed (conveyor, face-up) |
| Deployment class | Fixed portal | Fixed shelf/cabinet |
| Target read range | 20–30 ft | 3–6 ft |
| Target throughput | 500+ tags/sec | 100–200 tags/sec |
| Regional ceiling | FCC, 4 W EIRP | FCC, 4 W EIRP |

Flag any zone where ambient noise floor is above −70 dBm — that's a candidate for band replanning or added filtering before hardware selection, not a problem to solve with more reader power.

## 2. Tag / reader / antenna selection matrix

Pick the row matching the deployment class from the survey, then check the EIRP math before ordering.

| Deployment class | Read range target | Throughput target | Antenna | Polarization | Reader port power |
|---|---|---|---|---|---|
| Handheld / cycle count | 3–5 ft | 100–200 tags/sec | Integrated handheld | Circular (default) | 20–27 dBm (device-set) |
| Conveyor / fixed orientation | 2–4 ft | 300–500 tags/sec | Panel, 6–8 dBi | Linear | 27–30 dBm |
| Dock door / portal | 20–30 ft | 500+ tags/sec | Panel, 6–9 dBi | Circular (random orientation) | 30 dBm |
| Shelf / cabinet (near-field) | 1–3 ft | 50–100 tags/sec | Near-field/loop | N/A (near-field) | 20–25 dBm |

**EIRP check before ordering:** EIRP(dBm) = reader port power(dBm) + antenna gain(dBi) − cable loss(dB). A 30 dBm reader port with a 9 dBi antenna and 1 dB of cable loss = 38 dBm EIRP ≈ 6.3 W — over the FCC 4 W (36 dBm) ceiling. Drop to a 6 dBi antenna (35 dBm EIRP ≈ 3.2 W) or cut reader power to 27 dBm to clear the limit with margin. For ETSI sites (2 W ERP ≈ 33 dBm ERP, which is roughly 35.16 dBm EIRP-equivalent once the +2.15 dB ERP/EIRP conversion is applied), the same 30 dBm/9 dBi pairing (38 dBm EIRP) clears that ceiling by nearly 3 dB — plan on 6 dBi max or a power cap at 24 dBm.

**Tag selection:** item-level apparel/retail defaults to a Gen2v2-compliant UHF inlay rated for wake-up sensitivity around −18 dBm; case/pallet defaults to a higher-gain tag (rated closer to −20 dBm sensitivity) to survive being buried inside cartons. Tags going on or near metal require a metal-mount variant (spaced dielectric or on-metal-rated inlay) — a standard inlay glued directly to a steel surface commonly loses 50%+ of its rated range.

## 3. EPC / SGTIN-96 tag programming template

Fill and verify before the pilot, not after tags are already applied:

```
GS1 Company Prefix: 0614141 (7 digits, example)
Partition value:     5   → indicates 7-digit company prefix / 5-digit item ref
Item Reference:      12345
Serial:               000001–999999 (per-unit, sequential or random per client policy)

Encoded SGTIN-96 fields:
  Header (8 bit):     00110000  (SGTIN-96)
  Filter value (3 bit): 001      (POS trade item — use 010 for case, 011 for pallet)
  Partition (3 bit):    101      (matches company-prefix length above)
  Company Prefix:      0614141
  Item Reference:       12345
  Serial:               000001
```

Reserved bank: set the access password before the kill password is ever used in production — a tag killed without a set access password can't be selectively killed later without physically re-approaching every unit. TID bank is read-only from the factory; use it for chip-level audit, never as a substitute for the EPC identifier in application logic.

## 4. In-situ antenna matching sequence

Run this at the actual install location, after racking/inventory that will be present in production is in place — bench tuning is provisional only.

1. Mount the antenna at the position and angle specified in the survey.
2. Measure return loss (S11) with a VNA. **Threshold: better than −10 dB is the minimum acceptable; −15 dB or better is the target where achievable.**
3. If S11 is worse than −10 dB (e.g., −7 dB): check distance to the nearest metal/liquid first — move the antenna 0.5–1 m and re-measure before assuming a hardware fault.
4. Place a reference (witness) tag at the antenna's rated maximum range and record baseline RSSI — this becomes the drift baseline for ongoing monitoring, not just a one-time check.
5. Re-measure S11 after final mechanical mounting (brackets, conduit) — mounting hardware itself can detune an antenna by several dB.
6. Log the final S11, reference-tag RSSI, and antenna position/angle in the site file; this is the record you compare against when a future RSSI drift shows up.

## 5. Dead-spot sweep

1. Walk the read zone with a handheld reader in a figure-8 motion, not a single fixed sweep — a fixed orientation misses the cross-polarization blind spots the figure-8 is designed to find.
2. Mark any location where a known-good tag fails to read on 2 of 3 consecutive passes.
3. For each marked dead spot, check in this order (cheapest first): (a) tag physically obstructed by metal/liquid, (b) antenna angle/multipath at that specific point, (c) reader channel-hopping collision with an adjacent zone's reader.
4. Re-test after any fix with the same 3-pass protocol before marking the spot closed.

## 6. Pilot monitoring window

Run 2–4 weeks minimum before go-live sign-off.

| Week | Volume through zone | Target metric | Action if missed |
|---|---|---|---|
| 1 | Full production volume, monitored only | Blended read/accuracy rate vs. contracted floor | Log per-lane breakdown; do not adjust hardware yet — establish the baseline first |
| 2 | Full production volume | Per-lane accuracy within 5pp of week-1 baseline or better | Any lane below floor gets the dead-spot sweep (Section 5) before week 3 |
| 3–4 | Full production volume | Blended accuracy at or above the contracted floor for 5 consecutive operating days | If still short, escalate to a written accuracy-floor renegotiation (see SKILL.md worked example), not further hardware tuning |

Track every accuracy number by lane/zone, never as one blended site number until each lane individually clears its target — a blended number that looks acceptable can hide one lane running at 35% offset by others running above 95%.

## 7. Integration fallback positions (in order)

1. Native ingestion — receiving WMS/ERP accepts RFID read events directly (rare with legacy systems).
2. Middleware/protocol-translation layer reformatting RFID reads into the barcode-shaped event schema the legacy system already expects (the International Paper pattern).
3. Batch file export/import as a last resort when no real-time integration is feasible — accept the latency cost and document it in the SOW so it isn't discovered at go-live.
