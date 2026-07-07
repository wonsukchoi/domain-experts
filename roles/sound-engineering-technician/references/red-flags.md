# Sound Engineering Technician — Red Flags

### True peak exceeds -1 dBTP after a flat gain increase
- **Usually means:** gain was applied without engaging a true-peak limiter first; second most likely, the limiter's lookahead/ceiling setting is misconfigured.
- **First question:** was a true-peak limiter engaged before or after the gain change was applied?
- **Data to pull:** true-peak meter log across the full program, limiter ceiling and lookahead settings.

### Integrated LUFS reading is off the platform target by more than its stated tolerance
- **Usually means:** the source mix was never loudness-normalized to spec, or the wrong loudness window (momentary/short-term instead of integrated) was used to check compliance.
- **First question:** which loudness measurement (momentary, short-term, or integrated) was actually read when calling the mix "done"?
- **Data to pull:** full-program integrated LUFS log, not a spot-check from one section.

### Mono-summed level drops more than 3 dB compared to the stereo sum
- **Usually means:** phase cancellation between two mic sources or a stereo-widening plugin creating out-of-phase content.
- **First question:** does the drop appear across the whole spectrum or concentrated in a frequency band (pointing to a specific mic pair or plugin)?
- **Data to pull:** mono-compatibility A/B measurement, phase-correlation meter reading.

### Noise floor sits above -60 dBFS during intentionally quiet passages
- **Usually means:** gain staged too low at an early analog stage (preamp under-driven, later gain applied to compensate) or a ground/interference issue introduced mid-chain.
- **First question:** at which signal-chain stage does the noise floor first appear, checked with input muted at each stage?
- **Data to pull:** stage-by-stage noise-floor measurement (mic → preamp → interface → DAW track).

### Crest factor (peak-to-loudness ratio) below roughly 6 dB
- **Usually means:** cascading limiters/compressors chasing loudness past the point of diminishing perceptual return, destroying transient detail.
- **First question:** how many limiting/compression stages are in the chain, and what is the combined gain reduction across all of them?
- **Data to pull:** crest factor or PLR (peak-to-loudness ratio) measurement, gain-reduction metering per stage.

### Comb-filtered, hollow tone that persists after EQ adjustment
- **Usually means:** two mics (or a mic and a strong reflection) capturing the same source with a path-length difference violating the 3:1 rule.
- **First question:** does the hollow tone disappear when one of the suspected mic sources is muted?
- **Data to pull:** mic-placement distances relative to source and to each other.

### Audio/video sync drift greater than one frame over the program length
- **Usually means:** clock mismatch between recording devices that weren't jam-synced or locked to a common timecode source.
- **First question:** what is the frame offset measured at the start of the recording versus at the end?
- **Data to pull:** timecode logs or waveform sync-marker comparison at both ends of the recording.

### Sibilance or harshness spike more than 6 dB above the surrounding spectrum in the 4-8 kHz range
- **Usually means:** proximity to the mic on sibilant consonants without de-essing, or a bright mic/preamp combination pushed too hot.
- **First question:** does the spike correlate with specific phonemes (s, sh, t sounds) or is it constant across all speech?
- **Data to pull:** spectral analysis of the flagged passage, de-esser threshold/reduction settings if already applied.

### Delivery file fails an automated platform QC loudness gate
- **Usually means:** the file was measured against the wrong spec (e.g. checked against streaming target but delivered to a broadcast partner), or measured on a representative excerpt instead of the full program.
- **First question:** which exact spec (platform, target, tolerance) was the file checked against before submission?
- **Data to pull:** the platform's official technical delivery spec document, full-program loudness log used for the pre-delivery check.

### Preamp gain set so high that input clipping occurs before any plugin is engaged
- **Usually means:** gain staged for a quiet moment in the source material without headroom for its loudest transient.
- **First question:** what is the loudest transient in the source, and was the preamp gain set against that peak or against the average level?
- **Data to pull:** input-stage clip indicator log, peak level of the loudest moment in the source material.
