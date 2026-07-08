# Vocabulary

Terms of art a photonics technician uses precisely, that a generalist reads as loosely synonymous or as jargon for something more familiar — the kind of misreading that turns a passing measurement into a masked fault, or a real fault into a rejected good part.

## Insertion loss vs. return loss

**Insertion loss** is the optical power lost as light passes *through* a connector, splice, or component — measured in the forward transmission direction. **Return loss** is the power reflected *back* toward the source at that same interface, expressed as a larger negative-dB-magnitude number for a *better* result (less light coming back).

**In use:** "Insertion loss on that mated pair is 0.15 dB, fine — but return loss is only -35 dB against a -50 dB spec, so something's reflecting more than it should." **Common misuse:** treating a good insertion-loss number as evidence the interface is healthy overall — a connector can pass insertion loss cleanly while a contaminated or poorly-angled face reflects well above spec.

## Event dead zone vs. attenuation dead zone

**Event dead zone** is the minimum spacing to resolve two reflective events as separate. **Attenuation dead zone** is the longer minimum distance after any event before loss can be accurately measured there — the two have different lengths, so a feature can clear one and still sit inside the other.

**In use:** "It's past the event dead zone, so the trace shows a bump there — but we're still inside the attenuation dead zone, so don't trust the loss number on it yet." **Common misuse:** treating "past the dead zone" (singular) as one check instead of two separate ones with different lengths.

## Launch cord vs. patch cord

**Launch cord** is a length of fiber inserted between the OTDR and the fiber under test specifically to push the OTDR's own dead zones clear of the first connector so it can be measured accurately. **Patch cord** is any short jumper cable used to connect equipment or route a signal — a generic term with no dead-zone function implied.

**In use:** "That's not just a patch cord for convenience, it's the launch cord — pull it and you lose your ability to read the first connector's loss at all." **Common misuse:** substituting whatever jumper is on hand without checking it's long enough to clear the dead zone at the OTDR's pulse width in use.

## Reflectance vs. return loss

**Reflectance** is the fraction of light reflected at a single specific interface (one connector, one splice), reported as a negative dB value tied to that one point. **Return loss** often describes the cumulative reflected-power figure for an entire link or mated pair, though the two terms get used interchangeably in casual shop talk.

**In use:** "The OTDR's giving us reflectance at each connector individually — don't average those and call it the link's return loss, they're not describing the same thing." **Common misuse:** comparing a single connector's OTDR-reported reflectance against a return-loss spec written for the mated-pair or link-level figure.

## Angled Physical Contact (APC) vs. Ultra Physical Contact (UPC)

**APC** connectors have an 8° angled ferrule end-face that directs reflected light into the cladding instead of back up the core, rated ≥-60 dB return loss. **UPC** connectors have a flat, domed polish with no angle, rated ≥-50 dB. The two are not interchangeable at the mating interface.

**In use:** "Don't hand me a UPC patch to extend this run — the far end's APC, and mating those two will trash both the loss and the return-loss numbers." **Common misuse:** treating APC and UPC as interchangeable "connector types" distinguished only by color-coding (green vs. blue) rather than as physically incompatible mating geometries.

## Zone (IEC 61300-3-35) vs. defect

**Zone** is one of the concentric regions IEC 61300-3-35 defines on a fiber end-face (A: core, B: cladding, C: adhesive, D: contact), each with its own numeric pass/fail thresholds. **Defect** is any specific scratch, pit, chip, or contamination found on the face — its pass/fail status depends entirely on which zone it falls in.

**In use:** "Same 30 µm chip fails in Zone B but might clear in Zone C — read the zone the defect actually sits in before calling it pass or fail." **Common misuse:** applying one threshold (usually the strict, memorable Zone A/core number) to a defect regardless of which zone it's actually located in.

## Fusion splice vs. mechanical splice

**Fusion splice** permanently joins two fiber ends by melting and fusing the glass itself, typically achieving 0.01–0.05 dB loss. **Mechanical splice** aligns two fiber ends inside a mechanical fixture using index-matching gel, with no fusion — typically 0.3–0.5 dB loss, an order of magnitude worse, and remains a physically separable joint rather than a permanent one.

**In use:** "This budget line was sized assuming fusion — swapping in a mechanical splice here isn't a like-for-like substitution, it'll eat most of the margin." **Common misuse:** treating splice type as a matter of technician convenience or tooling availability rather than a budget-critical choice.

## Threshold current vs. operating current

**Threshold current** is the minimum drive current at which a laser diode transitions from spontaneous (LED-like) emission to lasing — the knee point on the L-I curve. **Operating current** is the current the diode is actually driven at in service, set with margin above threshold to hit the specified output power.

**In use:** "Threshold's crept up 12% since the last burn-in baseline — same operating current is now landing us lower on the slope, that's why output power's down." **Common misuse:** reading a drop in output power as an operating-current or driver problem first, without checking whether the diode's own threshold current has shifted.

## Hermeticity vs. leak rate

**Hermeticity** is the qualitative pass/fail property of a package being sealed against moisture/gas ingress. **Leak rate** is the quantitative atm·cc/sec-helium measurement a leak test actually produces against a package-specific GR-468-CORE threshold — the two aren't interchangeable terms for the same fact.

**In use:** "'No leak detected' isn't the same as 'hermetic' until we've confirmed the detector's sensitivity floor is below the spec's required leak rate." **Common misuse:** calling a package "hermetic" off a leak-rate reading without checking whether that reading reflects the spec threshold or just the instrument's floor.

## Human Body Model (HBM) vs. Charged Device Model (CDM)

**HBM** models an ESD event as a charged person discharging through a part on contact. **CDM** models the part itself accumulating charge (e.g., sliding across a surface or a tray) and discharging through a grounded contact — a distinct, typically faster, lower-threshold event unrelated to the handler's body charge. A part can be protected against one mode and still vulnerable through the other.

**In use:** "Wrist strap protects against HBM, but if this part's been sliding around loose in a non-conductive tray, that's a CDM exposure the strap doesn't address." **Common misuse:** treating "ESD-safe" as a single undifferentiated precaution (wrist strap = done) instead of two distinct discharge paths needing different controls.

## Burn-in vs. environmental screening

**Burn-in** runs a part at elevated, specified temperature and current for a stated duration to force infant-mortality failures before shipment. **Environmental screening** (temperature cycling, vibration, shock) verifies a part *tolerates* specified environmental extremes without permanent effect — a pass/fail exposure test, not a time-based failure-forcing process, and passing one says nothing about the other.

**In use:** "Burn-in's done, 168 hours at spec — but that doesn't cover the temp-cycling requirement on this traveler, that's a separate screening step still open." **Common misuse:** treating a completed burn-in as satisfying any stated environmental-screening requirement on the same traveler.

## Cutback measurement vs. OTDR measurement

**Cutback measurement** determines insertion loss by measuring power through the full fiber, then physically cutting it back to a shorter reference length and re-measuring — a destructive, direct power-comparison method independent of any OTDR's dead-zone or backscatter assumptions. **OTDR measurement** infers loss from backscattered light without cutting the fiber, but is subject to those same dead-zone and backscatter-coefficient assumptions.

**In use:** "OTDR says 0.28 dB on that splice, but it's close to the loss budget's edge — confirm it with a cutback or independent power-meter reading before we sign off." **Common misuse:** treating an OTDR-reported loss value as equally authoritative as a cutback or power-meter reading in all cases.
