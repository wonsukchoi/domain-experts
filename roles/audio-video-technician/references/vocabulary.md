# Vocabulary

Terms of art generalists reliably misuse on a live-event AV crew. Format per term: definition, how a practitioner actually uses it, the common misuse.

### EDID (Extended Display Identification Data)

Handshake data a display sends a source describing which resolutions, formats, and color spaces it supports.
**In use:** "The wall's showing nothing — check the EDID before you touch the cable, the scaler probably grabbed the wrong resolution off a bad handshake."
**Common misuse:** assuming any "no signal" symptom is a cable or connector fault. A clean cable carrying a rejected handshake produces the identical black screen as a dead cable.

### HDCP (High-bandwidth Digital Content Protection)

An encryption handshake between HDMI/DisplayPort devices that gates whether protected content is allowed to display.
**In use:** "That's an HDCP failure, not EDID — we're getting a black screen only on the protected source, the unprotected slides display fine through the same path."
**Common misuse:** conflating HDCP failures with EDID failures. They have different signatures (HDCP fails selectively on protected content; EDID fails on everything) and different fixes (an HDCP-compliant repeater vs. an EDID emulator).

### Genlock / house sync

A reference signal distributed to multiple video devices so they share a common timing reference and can be cut between cleanly.
**In use:** "Feed house sync to both cameras before we build the switcher inputs, or we'll get a glitch on every cut."
**Common misuse:** assuming a clean picture on each individual monitor means the devices are in sync with each other — genlock failures often look fine per-source and only surface as a glitch at the switch point.

### Word clock

The digital-audio equivalent of genlock: a shared timing reference that keeps multiple digital audio devices sample-aligned.
**In use:** "Put everything on the house word clock, not each unit's internal clock, or we'll get clicks by the second set."
**Common misuse:** skipping a shared word clock on a multi-device digital rig because it "worked without it" during a short bench test — clock drift is cumulative and often doesn't show up until well into a long show.

### Latency budget

The cumulative delay a signal accrues from source to output, tracked deliberately in frames (video) or milliseconds (audio) rather than treated as a single unknown.
**In use:** "We're at six frames of video latency before we even get to the wall — budget the audio delay against that number, don't just nudge it by ear."
**Common misuse:** treating lip sync as one delay knob to twist until it "looks right," instead of computing each device's contribution and setting the delay to a calculated target.

### IMAG (Image Magnification)

A live camera feed of a presenter or performer, projected on screens so a large room can see them clearly — distinct from a program or broadcast feed, which may include switched graphics, replay, or multiple camera cuts.
**In use:** "IMAG only needs one clean, low-latency camera path — save the multi-camera switching complexity for the broadcast feed, they have different jobs."
**Common misuse:** designing IMAG and broadcast/program feeds as if they're the same signal path with the same latency and redundancy requirements — IMAG prioritizes minimum latency for live perception; broadcast prioritizes production value and can tolerate more processing delay.

### HDBaseT

A protocol for extending HDMI-class audio/video signals, plus control and often power, over a single Cat5e/6 cable up to roughly 100 meters.
**In use:** "That run's too long for passive HDMI — put HDBaseT transmitters/receivers on both ends and it'll clear the whole building."
**Common misuse:** treating HDBaseT as "just a longer HDMI cable." It's a distinct transport with its own handshake behavior, bandwidth ceiling, and failure modes — it doesn't inherit HDMI's exact troubleshooting playbook.

### Intermodulation (IM)

Unwanted RF products created when two or more wireless transmitters' frequencies mix together, producing interference on a third frequency that no single transmitter is actually using.
**In use:** "That dropout isn't external interference — it's a third-order IM product from our own six wireless channels, we need to re-coordinate."
**Common misuse:** assuming RF interference always comes from an external source. A tech's own multi-channel wireless rig is frequently the interference source, and coordination software exists specifically to catch this before the show.

### Hot backup vs. cold backup

Hot: a redundant signal path that's live, framed/leveled, and continuously monitored, ready for an instant cut. Cold: a redundant path that exists in the rack but is only powered up and configured at the moment of failure.
**In use:** "That's a cold backup right now — we need it hot before doors, or the cutover will take 45 seconds we don't have."
**Common misuse:** calling a system "redundant" because a spare unit is physically present, without distinguishing whether it's actually ready for an instant cut or would need to be powered and framed live during a failure.

### Scaler / frame-buffer latency

The processing delay added by any device that must fully receive and reconstruct a video frame before passing it downstream — switchers, scalers, and wall/projector processors all add this.
**In use:** "Every scaler in this chain is another frame of delay — three hops means we're already at three frames before the wall processor adds its own."
**Common misuse:** assuming a "digital" signal path is instantaneous. Digital video processing is frame-quantized, and each hop adds a measurable, summable delay.

### NDI (Network Device Interface) vs. SDI

NDI carries video over a standard IP network; SDI carries it over dedicated coax with no shared network dependency.
**In use:** "NDI's fine for this corner-case camera, but the main program feed stays on SDI — I'm not putting the show on a network switch I don't control."
**Common misuse:** treating NDI as a drop-in SDI replacement without accounting for the network's bandwidth, switch quality, and potential congestion from unrelated traffic — an IP network failure mode is different from a dedicated coax run's failure mode.

### Dante

A protocol for carrying multichannel digital audio over a standard IP network, requiring specific switch configuration (QoS, PTP clocking) to perform reliably.
**In use:** "Confirm the switch supports Dante's QoS requirements before we trust it with 64 channels — a consumer switch will drop packets under load."
**Common misuse:** assuming any network switch will carry Dante audio reliably just because it has enough ports and bandwidth on paper — without proper QoS and clock configuration, it will glitch under load in ways that are hard to trace back to the switch.

### Show file / cue sheet

A single-page document freezing every configurable setting (RF frequencies, delay values, patch assignments) as the agreed baseline before doors open.
**In use:** "Don't touch anything after we freeze the show file — if something breaks live, we diagnose against that document, not against memory."
**Common misuse:** relying on memory or verbal handoff between crew shifts instead of a written, frozen document — the value of a show file is precisely that it's checkable during a live failure when nobody has time to reconstruct settings from recollection.
