# Playbook

## Wheel-dressing-interval overrun calculation (filled example)

Wheel/material combination: manufacturer-suggested redressing interval 60–75 parts. Current part count since last dress: 85.

| Step | Value |
|---|---|
| Manufacturer interval (low end) | 60 parts |
| Manufacturer interval (high end) | 75 parts |
| Current part count | 85 parts |
| Overrun vs. high end | 85 − 75 = 10 parts over |
| Overrun vs. low end | 85 − 60 = 25 parts over |
| Recent Ra readings | 15–17 μin (within 16 μin ± tolerance) |
| Burn check performed? | Not yet — required given overrun regardless of in-spec Ra |

**Action:** Nital etch burn check on the last 10 parts processed since exceeding the high-end interval, then redress the wheel before continuing production.

## Stock removal rate / heat capacity check (filled example)

| Wheel/coolant combination | Documented safe removal rate | Requested production rate | Status |
|---|---|---|---|
| Standard setup, flood coolant | 0.010 in³/min per inch of wheel width | 0.010 in³/min | Within documented safe rate |
| Same wheel, faster feed for rush order | 0.010 in³/min per inch of wheel width | 0.015 in³/min | **50% over documented safe rate — burn risk elevated** |

**Result:** The requested rush-order feed rate is 50% above the documented safe removal rate for this wheel/coolant combination — even though the machine can physically move at that feed rate, the coolant's heat dissipation capacity wasn't validated at that rate. Verify with a test part and burn check before committing the full rush order to this rate.

## Grit progression checklist (filled example)

Final polish target: mirror finish, Ra < 2 μin.

| Step | Grit | Scratch pattern from prior step removed before advancing? |
|---|---|---|
| 1 | 220 | N/A (starting step) |
| 2 | 400 | Yes — 220-grit scratches fully removed before advancing |
| 3 | 600 | Yes — 400-grit scratches fully removed before advancing |
| 4 | 1200 | Yes — 600-grit scratches fully removed before advancing |
| 5 (skipped in naive approach) | ~~800~~ | N/A if skipped |

**Naive shortcut risk:** Jumping from 600 grit directly to 1200 grit (skipping an intermediate 800-grit step) leaves 600-grit scratch depth that 1200 grit's finer abrasive can't fully remove within a reasonable polishing time — producing a surface that looks mirror-finished to the eye but shows residual scratch pattern under magnification or in a critical optical application.
