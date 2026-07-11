# Advanced-testing playbook

Load this when running a dye study, biometry, advanced OCT/field, or assisting a procedure — filled protocols, not descriptions of them.

## 1. Fluorescein / ICG angiography protocol

### Dye identity and contraindication check (do this first, every time)

| Reported history | Relevant to FFA (fluorescein sodium)? | Relevant to ICGA (contains sodium iodide)? |
|---|---|---|
| "Iodine allergy" / "shellfish allergy" | No — fluorescein has no iodine | Yes — genuine relative contraindication |
| Prior reaction to IV contrast (CT/MRI) | Weak signal at best | Weak signal at best (different compound) |
| Documented prior fluorescein reaction | Yes — direct history | Not directly, but raises general dye-reactivity concern |
| Documented prior ICG reaction | Not directly | Yes — direct history |
| Pregnancy | Relative contraindication — physician decision | Relative contraindication — physician decision |
| Severe hepatic impairment | Not typically relevant | Yes — ICG is hepatically cleared, physician decision |

### Dosing (adult, weight-based)

- **FFA:** 7.5 mg/kg of 10% fluorescein sodium, IV push over 5–10 seconds, typically drawn from a 500 mg/5 mL vial (round to nearest half-vial; a 60–90 kg adult reconciles to roughly 450–675 mg, i.e., about one vial).
- **ICGA:** 0.5 mg/kg (max ~25 mg per injection, repeatable), reconstituted with the manufacturer-supplied aqueous solvent — never with a solvent containing iodine-sensitive additives beyond what's supplied.

### Severe-reaction rates (know these before consenting a patient, don't understate them)

| Study | Mild (nausea/vomiting) | Moderate (urticaria/syncope) | Severe (bronchospasm/laryngeal edema) | Death |
|---|---|---|---|---|
| FFA (Yannuzzi 1986, n≈220,000) | ~2.9% | ~0.5% | ~1:1,900 | ~1:222,000 |
| ICGA (Hope-Ross 1994, n≈1,226) | ~0.15% | ~0.2% | ~1:1,900 (similar order) | rare, case-report level |

### Pre-injection sequence

1. Confirm order: which eye(s), FFA only, ICGA only, or both, and why (CNV, diabetic macular edema, vascular occlusion, etc.).
2. Run the contraindication table above against the *specific* dye(s) ordered — not a blanket "any dye allergy" gate.
3. If a genuine contraindication surfaces for one dye but not the other, flag the ordering ophthalmologist before proceeding with either — do not silently substitute or silently proceed.
4. Confirm IV access, patent line, and resuscitation equipment/epinephrine location known before injecting — every time, not only for flagged-risk patients.
5. Inject at the stated rate; document any patient-reported sensation (warmth, nausea, flushing) at the time it occurs, not retrospectively.
6. Watch injection site through the first 30–60 seconds for extravasation (localized pain, swelling, or a sudden bright hyperfluorescent spot at the IV site instead of a vascular pattern).

## 2. Biometry technique and correction

### Technique comparison

| Technique | Corneal contact? | Typical error vs. true axial length | When to use |
|---|---|---|---|
| Optical (PCI/OCT-based) | No | Reference standard, ~0.01–0.03mm repeatability | First choice unless media too opaque to obtain signal |
| Immersion ultrasound (Ossoinig) | Minimal (fluid-coupled) | ~0.1mm | Dense cataract/vitreous opacity blocking optical biometry |
| Contact (applanation) ultrasound | Direct probe contact | Underestimates by ~0.1–0.33mm from corneal compression | Last resort — only when immersion setup unavailable |

### Fellow-eye discordance check

- Axial length difference between eyes >0.3 mm with no history of trauma, prior refractive/cataract surgery, or documented anisometropia → **remeasure with immersion or optical technique before the reading reaches an IOL calculation.**
- If discordance persists after remeasurement with the higher-fidelity technique, document it as a true finding, not an artifact, and note the technique used for both eyes side by side.

## 3. OCT / visual field reliability gate

| Test | Reliability metric | Below-threshold action |
|---|---|---|
| Cirrus OCT | Signal strength <6/10 | Rescan; if unattainable (documented stable cataract/vitreous opacity), file with an explicit "signal strength ceiling due to [cause]" note |
| Spectralis OCT | Quality (Q) score in vendor's "poor" band | Same as above |
| Humphrey visual field (SITA) | Fixation losses ≥20%, or false-positive/false-negative ≥33% | Flag unreliable, offer repeat before comparing to baseline for progression |

Never let downstream software's "possible progression" (e.g., Guided Progression Analysis flags) get forwarded without confirming the flagged visit's own reliability indices meet threshold — a flagged progression built on an unreliable field is not a finding.

## 4. Procedure-assist site verification sequence

1. Read the laterality and procedure directly off the **signed consent form** — not the schedule, not the surgeon's verbal statement alone.
2. Independently confirm the marked eye (if site-marking protocol is used) matches the consent before draping.
3. State the laterality and procedure aloud during the surgical time-out as an independent participant, not a passive attendee.
4. Set up and confirm instrument/imaging equipment specific to the ordered procedure before the surgeon begins.
5. Document the technical portion of the note (equipment used, settings, any technical complication) separately from the surgeon's clinical narrative — do not draft or imply a diagnostic or outcome assessment.

## 5. Supervising a COA/COT — review order

1. Pull the trainee's flagged and discordant studies from the day/week first, not the routine-normal ones.
2. For each, ask them to state *why* it was flagged (or why it wasn't, if it should have been) before discussing the device operation.
3. Spot-check one routine-normal study per session to confirm normal-looking results weren't normal-looking-because-mis-acquired.
4. Log recurring misses (e.g., repeatedly missing signal-strength checks) as a training-plan item, not a one-off correction.
