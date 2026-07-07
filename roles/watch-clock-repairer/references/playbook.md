# Playbook

Filled diagnostic tables, test procedures, and templates — populate with the piece in front of you rather than reasoning from scratch each time.

## 1. Timegrapher reading-to-fault table

Baseline expectations, full wind, mechanical automatic movement (adjust down ~10–15% for a small ladies' caliber, up for a marine chronometer-grade caliber):

| Reading | Healthy range | Marginal | Likely fault when out of range |
|---|---|---|---|
| Rate, dial up | ±10 s/day (chronometer-grade); ±20–30 s/day (workhorse) | up to ±60 s/day | escapement adjustment, hairspring poise, or magnetism if far positive |
| Amplitude, horizontal (dial up/down), full wind | 270–310° | 240–269° | mainspring set slightly weak, or lubrication aging |
| Amplitude, horizontal, below 240° | — | — | mainspring/barrel/gear-train lubrication — service before touching escapement |
| Amplitude, vertical (crown up/down/left/right) | within 60–80° of the horizontal reading | 80–100° drop | balance-staff pivot or cap-jewel wear/contamination |
| Amplitude, vertical, drop > 100° from horizontal | — | — | worn/bent staff pivot, dry or damaged cap jewel — do not just re-oil, inspect the staff under the microscope |
| Beat error | < 0.5 ms | 0.5–1.0 ms | acceptable on a vintage riveted-balance caliber; correct only if servicing anyway |
| Beat error | — | 1.0–1.5 ms | worth correcting via collet rotation on any caliber being serviced |
| Beat error | > 1.5–2.0 ms | — | audible/visible asymmetric tick; correct as part of the same service, check hairspring stud position |
| Rate jumps >100 s/day positive with no amplitude change | — | — | magnetism — run through a demagnetizer and re-read before any further diagnosis |

**Reading order:** dial up → dial down → crown down (6, the common "off the wrist overnight" position) → crown up → crown left → crown right. Three positions (dial up, dial down, crown down) catch the large majority of position-dependent faults and are the minimum for any timing complaint; run all six on chronometer-grade or post-authentication work.

## 2. Water-resistance test procedure and pressure/depth table

| Rated depth | Test pressure (bar) | Notes |
|---|---|---|
| 30 m (3 ATM) | 3 bar | splash resistance only — do not immerse regardless of test pass |
| 50 m (5 ATM) | 5 bar | light swimming; not diving |
| 100 m (10 ATM) | 10 bar | swimming/snorkeling |
| 200 m (20 ATM) | 20 bar | recreational diving |
| 300 m+ | 30 bar+ | dive-rated; requires helium escape valve check on saturation-dive pieces |

**Sequence:**
1. **Dry overpressure screen** (Bergeon/Sigma dry tester) at rated pressure before opening the case, to establish a baseline — a case that already fails dry is not worth wet-testing until reworked.
2. **Open case, service, replace gaskets** (crown, case back, pushers/chronograph buttons if present) — always replace on any case opening; gaskets are a consumable, not a reusable part.
3. **Dry test again** post-reassembly at rated pressure.
4. **Wet/condensation test**: warm the case slightly, submerge briefly, then chill rapidly and check the crystal's inner surface for condensation — condensation confirms a leak the dry test can miss (thread deformation, crystal seal).
5. **Log before/after pressures** where a leak was found (e.g., "leaked at 4.3 bar against 6 bar rated, resealed and re-passed at 6 bar") — this is the number that goes in the customer disclosure, not a pass/fail checkbox.

**Never re-certify a printed rating from the dial without a fresh test.** A dial that says "200m" from 1975 is a manufacturing claim about a case that has since been opened an unknown number of times.

## 3. Parts-sourcing decision tree for a discontinued caliber

Applies once OEM supply is confirmed unavailable (check manufacturer/Swatch Group Service Center or brand parts portal first — some houses restrict even in-production parts to authorized centers, which is a different problem than true discontinuation).

1. **Donor movement** — a running or non-running example of the same or a closely related caliber, harvested for the specific part. Typical cost: part price only, plus time to source a donor (days to weeks). Preferred whenever a donor exists, since fit and finish match exactly.
2. **NOS (New Old Stock)** — unused factory parts still in circulation through parts dealers or collector networks. Typical cost: 1.5–3x a hypothetical in-production OEM price, reflecting scarcity. Preferred over a donor only when the donor would need to be destroyed for one part and an NOS source is readily available.
3. **Generic/cross-reference substitute** — a part from a still-produced caliber that shares the dimension (common for ébauche movements like Valjoux, Unitas, and AS families, less common for in-house calibers). Typical cost: comparable to a modern equivalent part, roughly 1x. Always disclosed to the owner in writing — this is the point where "serviced" and "original" diverge.
4. **Custom fabrication** (lathe-turned staff, hand-cut wheel tooth, re-cut jewel seat) — reserved for when none of the above exist. Typical cost: 3–5x the labor of a straightforward part swap, since it includes design-matching, turning, fitting, and finishing. Quote this as its own line item, not folded into "service," so the owner can see why the price jumped.

**Example cost ladder for a single balance staff, illustrative:**

| Source | Parts cost | Added labor |
|---|---|---|
| Donor movement | $15–40 (donor movement) | +0.5 hr to extract |
| NOS | $35–90 | none beyond standard fitting |
| Generic cross-reference | $18–30 | none beyond standard fitting |
| Custom-turned on lathe | $0 (stock steel blank) | +2–3 hrs turning and fitting @ shop labor rate |

## 4. Authentication checklist (vintage/luxury, above the value gate)

Run before quoting, on anything vintage, limited, or plausibly above roughly $5,000–10,000 retail-equivalent:

- **Case/reference/serial consistency**: reference number, serial number, and case-back stamping should match the manufacturer's known production range and each other; a serial that predates the reference's release year is a hard stop.
- **Movement-to-case match**: movement caliber and any signed/engraved details should match what that reference shipped with — an unsigned or wrong-family movement in a signed case is the single most common "franken" tell.
- **Dial originality**: font weight, logo placement, and lume-plot pattern should match known genuine examples for that production year; a crisp reprinted dial on an otherwise 50-year-old case is a redial, not "mint condition."
- **Hands and lume-era consistency**: radium-era, tritium-era, and Super-LumiNova-era lume and hands have known cutoff windows (tritium markings roughly 1963–1998 on most Swiss brands) — hands from the wrong era on an otherwise-period dial indicate parts substitution.
- **Bracelet/strap end-link and clasp date codes**, where present, should be contemporary with or later than the case, never earlier.

Document findings in writing before service begins, whether they clear the piece or raise a flag — an undocumented authentication pass protects nobody if the piece is later disputed.

## 5. Service-quote template

```
Diagnosis: <fault, in plain language, tied to the timegrapher/pressure-test numbers>
Parts:
  <part> — <sourcing tier: OEM / donor / NOS / generic substitute> — $<cost>
  ...
Labor: <hours> hrs @ $<shop rate>/hr — $<cost>
Subtotal: $<sum>
Quoted price: $<rounded, with any margin/contingency noted>
Disclosures: <any generic substitution, authentication finding, or irreversible step (e.g. redial) called out explicitly>
```
