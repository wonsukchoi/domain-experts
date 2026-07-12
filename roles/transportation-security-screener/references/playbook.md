# Transportation Security Screener — Playbook

## Alarm-resolution table by modality

| Modality | Alarm | Resolution endpoint | Not a resolution |
|---|---|---|---|
| AIT (millimeter-wave) | ATR generic-outline anomaly, one zone marked | Targeted pat-down of the marked zone only | Passenger's explanation of what's in the zone, without a pat-down |
| AIT | Anomaly recurs after pat-down of the marked zone | Alternate resolution: visual inspection / private screening with witness officer, or handheld wand plus visual | A second pat-down attempt of the same zone with no new method |
| WTMD | Single alarm | Full pat-down (SOP-defined coverage), or handheld wand scan of the full body per station protocol | A second unalarmed walk-through with nothing removed |
| WTMD | Alarms, then clears with items removed | Pat-down or wand of the specific area corresponding to the removed item, to confirm no residual cause | Accepting the item removal itself as proof of cause |
| X-ray (carry-on) | Ambiguous image, one angle | Re-scan from a second angle | Passenger's verbal description of contents |
| X-ray (carry-on) | Ambiguous image, persists after second angle | Physical opening and manual search of the flagged area | A third scan from another angle |
| ETD | Positive swab, no corroborating alarm elsewhere | Retest via second swab; check against known false-positive substance list (nitroglycerin medication, fertilizer residue, glycerin-based lotion) | Accepting a stated medical reason without a retest |
| ETD | Positive swab plus a corroborating alarm (AIT/WTMD/X-ray) on the same item or person | Escalate directly to physical search / supervisor notification | Treating the two alarms as independently resolvable |

## Prohibited / restricted item disposition matrix (thresholds as published, verify against current TSA guidance and station SOP)

| Item class | Rule | Standard disposition |
|---|---|---|
| Knives (any fixed or folding blade, any length) | Prohibited from sterile area, no length exception | Offer return-to-airline for checked-bag transport (knives are legal checked); voluntary surrender if declined |
| Scissors | Permitted in carry-on if blade ≤4 in. from the pivot point | Above 4 in.: same disposition as knives |
| Tools (screwdrivers, wrenches, pliers, etc.) | Permitted in carry-on if ≤7 in. long | Above 7 in.: offer checked-bag return or surrender |
| Liquids/gels/aerosols (general) | ≤3.4 oz (100 mL) per container, all containers in one quart-sized bag, one bag per passenger (3-1-1 rule) | Over-limit: offer checked-bag return; declined → surrender |
| Self-defense spray (mace/pepper spray) | Checked baggage only, ≤4 fl oz (118 mL), safety mechanism required — never permitted in carry-on regardless of size | ≤4 fl oz: offer checked-bag return. >4 fl oz: prohibited outright, no checked-bag path from the checkpoint — surrender only |
| Firearms (any, loaded or unloaded) | Prohibited from carry-on and checkpoint entirely; only transportable via airline's checked-firearm declaration process, never through the checkpoint | Always a reportable find — notify supervisor and airport law enforcement immediately; never a simple surrender-and-continue |

Numbers above are the published general-public thresholds current as of this writing; TSA revises specific items periodically, and detailed alarm-resolution sequencing is Sensitive Security Information (SSI) not reproduced here — station SOP is the operative authority in any real screening.

## Multi-alarm / escalation checklist

Use when two or more alarms fire on the same passenger or property in one screening:

1. Resolve each alarm independently to its own physical endpoint first — don't let one alarm's plausible clearance lower the scrutiny applied to the other.
2. After both are resolved, evaluate them together: do the findings corroborate, contradict, or independently confirm separate issues (as in a knife find plus an unrelated over-limit liquid)?
3. Compare the passenger's original podium/verbal declaration of contents against what was actually found. A mismatch on one item is common and usually innocent; a mismatch paired with two or more significant finds crosses most stations' threshold for supervisor notification.
4. If either finding is independently illegal to possess, a reportable weapon class (firearms, explosives), or the passenger's responses show a pattern beyond ordinary rules-unfamiliarity (e.g., providing a false identity detail, not just a wrong guess about a spray's ounce limit), escalate to airport law enforcement — this is outside TSO disposition authority.
5. Log both alarms, both resolutions, and the disposition decision together in one incident entry — a split record across two entries makes the pattern invisible to the next reviewer or TIP calibration pass.
6. If queue pressure is high when the multi-alarm case occurs, route the next arriving passengers to an open lane rather than compressing the resolution steps for the passenger already in progress.
