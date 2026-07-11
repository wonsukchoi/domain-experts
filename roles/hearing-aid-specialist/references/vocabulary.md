# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

### Real-ear measurement (REM) vs. first-fit

- **Definition:** REM is a probe-microphone measurement of what the device actually delivers at the patient's own eardrum; first-fit is the manufacturer software's initial programming based on the audiogram and population-average acoustics.
- **Practitioner usage:** "First-fit gets us in the ballpark; I don't call a fitting done until the REM curve is within tolerance of target."
- **Common misuse:** treating first-fit output as the finished fitting because "the software already applied the prescriptive formula." The formula's math is right; the assumption about this patient's ear canal acoustics is a population average, and it's frequently wrong by more than the ±5 dB tolerance.

### OSPL90 vs. MPO

- **Definition:** OSPL90 (Output Sound Pressure Level for a 90 dB SPL input) is the electroacoustic spec-sheet measurement per ANSI/ASA S3.22, taken in a standardized 2cc coupler. MPO (maximum power output) is the programmed real-world output ceiling set in the fitting software for this patient.
- **Practitioner usage:** "The spec sheet's OSPL90 tells me the device's ceiling in a coupler; MPO is what I actually programmed against this patient's loudness-discomfort level."
- **Common misuse:** quoting a device's OSPL90 as if it describes what the patient will experience — it describes coupler output, not real-ear output, which is exactly why REM exists.

### RECD (Real-Ear-to-Coupler Difference)

- **Definition:** the measured difference in dB between output in a real ear canal and output in a standard 2cc coupler, used to convert coupler-based measurements to real-ear-equivalent values, especially for small or atypical canals (pediatric fittings).
- **Practitioner usage:** "Her canal RECD ran higher than the age-average default, so the coupler-based verification would have under-predicted her real-ear output by several dB if I hadn't measured it individually."
- **Common misuse:** using an age-average RECD table value when an individual RECD measurement is feasible and the canal is atypical — the average exists for cases where individual measurement genuinely isn't possible, not as a shortcut of convenience.

### REAR, REIG, REUR, REOR

- **Definition:** REAR (real-ear aided response) — output with the device on, measured in dB SPL. REIG (real-ear insertion gain) — REAR minus REUR, i.e., the gain the device adds. REUR (real-ear unaided response) — the ear canal's natural resonance with no device present. REOR (real-ear occluded response) — output with the device off but physically in the ear.
- **Practitioner usage:** "REAR matched target within tolerance across the board, but I still check REUR at intake so I know this patient's canal has more natural 2700 Hz resonance than average — it changes how I read the REIG curve later."
- **Common misuse:** treating REIG as interchangeable with REAR when comparing to target; some verification systems and prescriptive formulas specify targets in one or the other, and comparing REIG measurements against REAR targets (or vice versa) produces a false pass or fail.

### Occlusion effect

- **Definition:** the perceived boost in low-frequency loudness of one's own voice caused by sealing the ear canal, because bone-conducted vocal energy that would normally escape through an open canal reflects back off the sealed device/shell.
- **Practitioner usage:** "That 'talking in a barrel' complaint with normal low-frequency hearing is classic occlusion effect — I'll open the vent before I touch the gain."
- **Common misuse:** treating every own-voice complaint as a gain problem and turning down output, when the actual fix is almost always mechanical (larger vent, more open dome/shell), not electrical.

### Feedback margin

- **Definition:** the headroom, in dB, between a device's maximum stable gain before audible feedback and the gain actually programmed for the patient at a given frequency.
- **Practitioner usage:** "We're sitting at about 6 dB of margin at 3 kHz — that's why it whistles when she cups her hand near the ear; I need at least 10 before I call this stable."
- **Common misuse:** relying entirely on the device's feedback-cancellation algorithm to mask an insufficient margin instead of fixing the underlying cause (vent size, shell fit, or excessive high-frequency gain) — cancellation reduces audible artifact, it doesn't create margin that isn't there.

### Venting (open vs. closed/occluded)

- **Definition:** the diameter of the acoustic vent (or absence of one) in a custom shell or dome, controlling how much low-frequency sound and internal own-voice energy escapes rather than being reflected back into the canal.
- **Practitioner usage:** "Low frequencies are near-normal here, so I'm starting with a large-vent open dome — a closed fit would occlude and she'd complain about her own voice by the second sentence."
- **Common misuse:** picking vent size purely by hearing-loss severity chart lookup without factoring in feedback risk at that gain level — larger vents reduce occlusion but also reduce the feedback margin available at high gain, and the two considerations trade off against each other.

### Compression ratio / knee point

- **Definition:** in a wide-dynamic-range-compression device, the knee point is the input level at which the device switches from linear gain to compressed gain; the compression ratio describes how much output increases per dB of additional input above the knee.
- **Practitioner usage:** "I lowered the knee point so soft speech at 45 dB SPL still gets full gain, since that's below where the compression used to kick in."
- **Common misuse:** discussing "gain" as a single number when a modern device applies different effective gain at different input levels — a device can be simultaneously "too loud" for loud sounds and "too soft" for quiet ones at the same nominal gain setting, and the fix is a knee-point or ratio change, not a blanket volume change.

### OTC vs. prescription hearing aid

- **Definition:** under the FDA's 2022 rule (effective Oct. 17, 2022), OTC hearing aids are sold without a professional fitting to adults 18+ who perceive their loss as mild to moderate; prescription devices require a licensed fitter and are not restricted to that severity range.
- **Practitioner usage:** "Given her mild, symmetric, self-perceived loss and no red flags, OTC is a legitimate option to discuss alongside a professionally fit device — it's not automatically the wrong answer just because it's cheaper."
- **Common misuse:** assuming OTC status means "not a real hearing aid" or, in the other direction, steering every OTC-eligible patient toward a professional fitting regardless of preference or budget — the category exists by regulatory design, not as a lesser product tier.

### Bundled vs. itemized (unbundled) pricing

- **Definition:** bundled pricing folds device cost, fitting, verification, and a period of follow-up visits into one all-in price; itemized pricing prices the device and each service separately.
- **Practitioner usage:** "I quote itemized so when she needs a battery-door repair in year two, she can see exactly what that costs instead of feeling like she's being billed twice for something she thought was already covered."
- **Common misuse:** assuming bundled pricing is inherently the "generous" option — it can obscure how much of the total is device margin versus service, which is precisely the information a price-sensitive patient needs to trust the recommendation.

### Adaptation / acclimatization period

- **Definition:** the interval, typically 2–4 weeks, during which a new hearing-aid user's perception of amplified sound (including their own voice and environmental sounds) shifts toward "normal" as the auditory system and brain adjust.
- **Practitioner usage:** "I tell every new user to expect their own voice to sound odd for the first couple of weeks — but a directional complaint like 'too sharp' isn't acclimatization, that's a fitting-verification question."
- **Common misuse:** using "give it time to adjust" as a catch-all response to any complaint, including ones (sound-quality shifts that track a specific frequency band, feedback, occlusion) that are measurable fitting problems and won't resolve with time alone.

### Air-bone gap

- **Definition:** the difference in dB between air-conduction and bone-conduction hearing thresholds at the same frequency; a gap indicates a conductive component to the loss, since bone conduction bypasses the outer/middle ear.
- **Practitioner usage:** "There's a 20 dB air-bone gap at 500 and 1000 Hz on the left — that's above the referral threshold, so amplification isn't the first move here."
- **Common misuse:** reading only the pure-tone average severity label ("moderate loss") and skipping the air-bone gap check entirely — two patients with an identical PTA can have completely different underlying pathology and correct next steps.
