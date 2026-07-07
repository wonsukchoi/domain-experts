# Playbook

Diagnostic and repair protocols run in the shop, with the actual thresholds and step sequences used — not descriptions of what a protocol should contain.

## 1. Intake diagnostic sequence

Run in this order on every unit before opening a case, regardless of the customer's stated symptom:

1. **Pull the actuation count** from the body's diagnostic menu (Canon: service-mode shutter count; Nikon: MyMenu shutter-count add-in or third-party reader like ShutterCount) or the most recent frame's EXIF `MakerNote` shutter-count tag. Log it against the model's rated durability.
2. **Blank-frame test shot at a working aperture** (e.g., f/5.6, focused to infinity, aimed at an evenly lit blank wall or overcast sky) — establishes a baseline exposure and banding check at everyday settings.
3. **Blank-frame test shot stopped down to f/16–f/22**, same target, slightly defocused — the dust-diagnostic shot. At this aperture, sensor debris renders as sharp small dark spots; anything larger, soft-edged, or crescent-shaped is more likely aperture-blade debris or a rear-element issue, not sensor dust.
4. **Resolution-chart shot sequence** (USAF 1951 or an ISO 12233 chart) at three distances — close (min. focus), mid (~3m), far (~15m+) — for any focus complaint, before assuming AFMA will fix it.
5. **Lens-swap isolation**: repeat step 3 with a second, known-clean lens on the same body. If the spot pattern persists in the same frame position, the fault is sensor-side. If it disappears or moves, it's lens- or mirror-path-side.

## 2. Shutter actuation-count decision tree

| Actuation ratio (count ÷ rated life) | Symptom present? | Action |
|---|---|---|
| < 50% | No | Note baseline, no action |
| < 50% | Banding/irregular sound | Bench-test curtain timing — early failure, treat as a components defect, not wear |
| 50–80% | No | Advise customer of ratio, no repair needed yet |
| 50–80% | Banding/irregular sound | Bench-test curtain timing; replace if timing is out of spec |
| 80–95% | No | Recommend pre-emptive shutter replacement for professional/event use; optional for casual use |
| 80–95% | Banding/irregular sound | Replace shutter unit — do not attempt a partial fix (e.g., cleaning/lubricating curtain rails) at this ratio; wear is systemic at this point |
| > 95% | Any | Replace shutter unit or retire body; repair-only quotes above this ratio should flag "high near-term re-failure risk" in writing to the customer |

**Curtain-timing spec check:** measure first- and second-curtain travel time on the shutter-timing rig; compare against the manufacturer service-manual tolerance (typically ±0.3ms for full-frame focal-plane shutters in this class). A single curtain reading outside tolerance while the other reads in spec confirms a mechanical (not electronic) shutter fault.

## 3. Sensor-dust vs. lens-contamination isolation

1. Run the f/16–f/22 test shot (intake step 3).
2. Run the lens-swap test (intake step 5).
3. Cross-reference spot shape:

| Spot appearance | Likely source | Next step |
|---|---|---|
| Sharp-edged, small, round, same position across lenses | Sensor surface (dust) | Sensor clean (dry blower first, wet swab if unresolved) |
| Same position, doesn't clear with sensor clean | Sensor surface (adhered debris or scratch) | Inspect under sensor loupe at magnification; scratch requires sensor-glass or full sensor-assembly replacement quote, not a cleaning fee |
| Soft-edged, position shifts with aperture change | Aperture-blade debris in the lens | Disassemble lens aperture unit, clean blades |
| Position changes when lens is rotated | Rear lens element contamination | Clean rear element; check for oil migration from aperture-blade lubricant (common in older zoom lenses) |
| Cloudy/hazy across whole frame, not discrete spots | Fungus or internal haze | Full lens disassembly and element cleaning, or decline if fungus has etched the coating — quote replacement |

## 4. Autofocus calibration and collimation procedure

1. **Constant-vs-variable offset test**: shoot the resolution chart at 3 distances (intake step 4). Record the focus-point offset in AF micro-adjustment units (Canon/Nikon AFMA range: typically ±20 steps) at each distance.
2. **If the offset is the same sign and roughly the same magnitude at all three distances**: this is a constant electronic offset — correct with AF micro-adjustment / AF fine-tune, applying the measured value.
3. **If the offset changes sign between near and far, or differs by more than ~2 chart-line pairs across the frame (corner vs. center)**: this is not correctable by AFMA. Escalate to a collimation bench check:
   - Mount the lens on an optical bench with an autocollimator.
   - Measure flange focal distance against the mount's factory spec (tolerance typically ±0.01–0.03mm depending on mount).
   - If out of tolerance, correct with shim adjustment at the mount or internal element spacer, then re-shoot the 3-distance chart test to confirm the offset is now flat and near zero before returning AFMA to its default (0).
4. **Never leave both an AFMA correction and an uncorrected mechanical offset in place simultaneously** — AFMA masks the symptom at one tested distance while leaving the underlying spacing wrong at every other distance, which reads to the customer as "sometimes still front-focuses."

## 5. Image-stabilization (IS/VR) fault isolation

1. Power the lens/body and listen for noise **while IS is engaged and the shutter is half-pressed** — a soft rattle here with the lens powered off but the same silence when powered on is normal lock-pin engagement noise, not a fault.
2. If buzzing, grinding, or a rhythmic tick is present **while IS is actively engaged and stabilizing**, that indicates motor or bearing wear in the floating IS group — this is the actual fault condition.
3. Check for an IS error code on the body (e.g., Canon's "Err 2x" family) — cross-reference the code against the service manual before assuming a full IS-unit swap; some codes point to a contact/flex-cable fault correctable without replacing the mechanical assembly.
4. Only quote a full IS-unit replacement once step 2's noise-while-active condition and a matching service-manual error code both confirm mechanical wear — a flex-cable reseat is a $40–60 fix; an IS-unit swap is typically $250–400 in parts and labor.

## 6. Parts-sourcing decision tree (discontinued models)

1. **Check OEM parts portal first**, by exact part number from the service manual — not by model name alone, since part numbers change across minor revisions.
2. **If unavailable, check age since discontinuation.** Under ~7 years post-discontinuation, OEM parts are frequently still findable through secondary authorized-parts distributors — check those before declaring the part unobtainable.
3. **If OEM and secondary-distributor stock are both exhausted, source a donor unit** — a non-functional body/lens of the same model, purchased for the specific working part needed (shutter unit, IS assembly, mount ring), from used-camera-parts marketplaces.
4. **If no donor units are listed for sale anywhere in the applicable market, that is the point to tell the customer repair isn't viable** — quote a replacement body/lens recommendation instead of an open-ended "we'll keep looking" that stalls the customer's decision.
5. **Log the part's source** (OEM new, secondary distributor, donor take-off) on the service record — a donor-sourced part carries its own unknown wear history and should be disclosed to the customer as such, not represented as equivalent to new stock.
