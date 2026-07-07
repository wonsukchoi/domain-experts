# Sound Engineering Technician — Vocabulary

### LUFS (Loudness Units Full Scale)
A standardized measurement of perceived loudness integrated over program duration, per ITU-R BS.1770.
**In use:** "This mix reads -16 LUFS integrated — two units under Spotify's -14 target, so it'll get turned up on playback if we don't fix it here."
**Common misuse:** treating LUFS as interchangeable with dBFS peak level. LUFS measures perceived loudness over time; dBFS measures the instantaneous signal level of a single sample. A mix can have a low peak dBFS and still read too loud in LUFS if it's dense and sustained.

### True peak (dBTP)
An oversampled peak measurement that estimates inter-sample peaks a standard sample-peak meter can't see, per ITU-R BS.1770 Annex 2.
**In use:** "Sample peak reads -0.3 dBFS but true peak hit +0.6 dBTP — that'll clip on any device doing sample-rate conversion."
**Common misuse:** assuming a clean sample-peak reading means the file won't clip on playback. Reconstruction filters in D/A conversion or lossy encoding can produce inter-sample peaks well above what the sample-peak meter shows.

### Gain staging
Setting signal level at each point in the chain to maximize signal-to-noise ratio while leaving headroom against clipping.
**In use:** "The hiss isn't a plugin problem — it's a gain-staging problem, the preamp was set 15 dB too low and we made it up later with track gain."
**Common misuse:** treating gain staging as a one-time setting at the start rather than a property that must hold at every stage — a single under- or over-driven stage anywhere in the chain degrades the whole signal.

### Headroom
The margin, in dB, between a signal's current level and the point at which it clips.
**In use:** "Leave 6 dB of headroom on the mix bus before the mastering stage, not right up against 0 dBFS."
**Common misuse:** confusing headroom with loudness — a mix with generous headroom isn't automatically quiet in LUFS terms; the two are related but not the same measurement.

### Crest factor / PLR (peak-to-loudness ratio)
The difference, in dB, between a signal's peak level and its average (loudness) level — a proxy for how much dynamic range survives in the mix.
**In use:** "Crest factor dropped to 4 dB after that last limiter stage — we're past the point where more limiting buys us perceptible loudness."
**Common misuse:** treating "lower crest factor" as an unconditional goal. Below roughly 6 dB, additional limiting mostly destroys transient detail rather than adding perceived loudness — it's a stopping signal, not a target to minimize.

### Signal-to-noise ratio (SNR)
The ratio between the desired signal level and the noise floor, set primarily at the earliest analog gain stage.
**In use:** "SNR was fixed the moment we set the preamp gain — nothing downstream can recover what wasn't captured cleanly at the mic."
**Common misuse:** believing downstream noise reduction (plugins) restores SNR lost upstream. Noise reduction removes noise at the cost of some signal quality; it doesn't recreate the SNR a properly gain-staged recording would have had.

### Phantom power
48V DC supplied through an XLR cable to power condenser microphones.
**In use:** "Check phantom power is engaged before troubleshooting a dead condenser mic — dynamic mics don't need it and can be damaged by some non-standard implementations."
**Common misuse:** assuming all mics need phantom power, or leaving it on when patching in ribbon mics that can be damaged by an unbalanced phantom-power feed.

### Polar pattern
The directional sensitivity of a microphone — cardioid (front-focused), omnidirectional (all directions equally), figure-8 (front and back, rejecting sides), among others.
**In use:** "Switch to omni for that room recording — cardioid's proximity effect is exaggerating the low end at this close distance."
**Common misuse:** picking a polar pattern purely by mic model reputation rather than by what the specific recording situation (room sound desired or not, background noise, multiple sources) requires.

### Proximity effect
The bass boost that occurs as a directional (cardioid or figure-8) microphone gets closer to its source.
**In use:** "That boomy low end isn't an EQ problem — it's proximity effect from the vocalist working the mic too close."
**Common misuse:** correcting proximity effect with a permanent EQ cut instead of addressing mic distance, which then under-represents the low end if the performer's distance varies during the take.

### 3:1 rule
A mic-placement guideline: a second microphone should be positioned at least three times its own distance-to-source away from any other mic capturing the same source, to avoid audible comb filtering when summed to mono.
**In use:** "We're violating 3:1 on the drum overheads — that's the phasey snare, not an EQ issue."
**Common misuse:** applying the rule mechanically past two mics on one source, or treating it as a hard requirement rather than a fast heuristic — deliberate multi-mic blending sometimes accepts controlled phase interaction as a creative choice.

### Limiter ceiling
The maximum output level a limiter is permitted to pass, set to leave true-peak margin against clipping downstream.
**In use:** "Set the limiter ceiling to -1 dBTP, not 0 — we need margin for the streaming platform's re-encode."
**Common misuse:** setting the ceiling at exactly 0 dBFS, leaving no margin for inter-sample peaks or downstream lossy re-encoding, both of which can push the actual playback level over true digital full scale.

### Momentary / short-term / integrated loudness
Three time windows for LUFS measurement: momentary (400ms), short-term (3s), and integrated (the full measured program).
**In use:** "Momentary loudness spikes to -8 LUFS on that chorus, but integrated across the whole track we're still at -15 — within spec."
**Common misuse:** checking only momentary or short-term loudness and declaring compliance, when most delivery specs are written against integrated loudness across the full program.

### Comb filtering
Frequency-dependent cancellation and reinforcement caused by summing two versions of the same signal with a small time offset between them.
**In use:** "That hollow, phasey tone on the drum bus is comb filtering from the overhead pair — not something an EQ move can fix."
**Common misuse:** attempting to fix comb filtering with EQ, which cannot repair a timing-domain problem — the fix is repositioning mics, phase-aligning in the DAW, or accepting/using the effect deliberately.

### De-essing
Frequency-selective compression targeting sibilant consonants (typically 4-8 kHz) to reduce harshness without dulling the whole vocal.
**In use:** "Run a de-esser at 6.5 kHz before the main compressor — sibilance gets exaggerated if it hits the compressor first."
**Common misuse:** using a broadband high-shelf EQ cut to tame sibilance, which dulls the whole vocal's brightness instead of targeting only the sibilant transients.
