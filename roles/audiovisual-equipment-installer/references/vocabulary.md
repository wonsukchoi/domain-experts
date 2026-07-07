# Vocabulary

### EDID (Extended Display Identification Data)
The block of data a display publishes describing its supported resolutions, timings, and audio capabilities, read by the source device during the HDMI handshake to decide what signal to send.
**In use:** "The room PC's blanking because it's getting the extender's internal fallback EDID instead of the display's real one — pull it with the reader before you touch the cable."
**Common misuse:** Treated as synonymous with "the cable" or "the connection" generally — technicians say "it's an EDID issue" as a catch-all for any handshake problem, including ones that are actually HDCP failures.

### HDCP (High-bandwidth Digital Content Protection)
A content-protection handshake separate from EDID, required at every link in the signal chain (source, any switcher/extender, sink) for protected content to display; one non-compliant device breaks the whole chain.
**In use:** "Check HDCP compliance on the matrix switcher too — it's rated for HDCP 2.2 but the extender downstream of it is only 1.4, and that's the actual break."
**Common misuse:** Conflated with EDID as "the same handshake problem" — they're independent negotiations that happen to produce identical symptoms (blank or flickering screen) when either one fails.

### HDBaseT
A signal-extension standard for carrying HDMI (plus control, Ethernet, and power in some implementations) over Cat5e/Cat6 cable, with distance/bandwidth ceilings that vary by extender class and target resolution.
**In use:** "This run's 140ft, so we need the higher-bandwidth-class extender if the client wants full 4:4:4 chroma at 4K60 — the standard class won't hold it at that distance."
**Common misuse:** Treated as a single fixed spec ("HDBaseT does 100 meters") when the actual distance ceiling depends heavily on the target resolution and chroma subsampling, not a flat number.

### AVoIP (Audio-Video over IP)
Signal distribution over a standard network switch/topology (encoders at the source, decoders at each sink) instead of dedicated point-to-point matrix switching or extension.
**In use:** "For an 18-room building with any-source-to-any-display switching, AVoIP scales better than a giant HDBaseT matrix — the network handles the routing."
**Common misuse:** Proposed by default for every job "because it's the modern approach," even for a single point-to-point run well within passive HDMI or standard HDBaseT range, where it adds cost and network dependency for no functional gain.

### CTS / CTS-I / CTS-D
AVIXA's Certified Technology Specialist credential family: CTS is the general credential, CTS-I adds an installation specialization, CTS-D adds a design specialization.
**In use:** "The programming scope needs a certified Crestron programmer, not just a CTS-I — installation certification doesn't cover writing control logic."
**Common misuse:** Used interchangeably as "the AV certification," obscuring that CTS-I (install) and CTS-D (design) are distinct scopes of practice with different responsibilities — and that control-system programming certifications sit outside all three.

### DISCAS (Display Image Size for 2D Content in Audiovisual Systems)
ANSI/AVIXA V202.01:2016, the current standard methodology for calculating minimum display size from viewing distance, visual acuity assumptions, and content type (basic vs. analytical decision-making content).
**In use:** "Run the DISCAS numbers before you quote a screen size — don't just default to the biggest panel that fits the wall."
**Common misuse:** Confused with the older, simpler "4/6/8 rule of thumb" it superseded and formalized — practitioners often cite the legacy ratio language while meaning the current standard's more detailed methodology, or vice versa.

### NC rating (Noise Criteria)
A single-number rating describing a room's background/HVAC noise level across frequency bands; conference rooms typically target NC-30 to NC-35.
**In use:** "The HVAC diffuser they spec'd puts this room at NC-42 — that's above target and it'll compete with the mics regardless of what audio gear we install."
**Common misuse:** Treated as an AV installer's problem to fix with equipment (better mics, more gain) when an above-target NC rating is a mechanical/HVAC design issue that AV gear can't compensate for.

### RT60 (Reverberation Time)
The time in seconds for sound to decay 60dB after the source stops — the standard measure of how "live" or "dead" a room sounds; conferencing rooms target roughly 0.6–0.8 seconds.
**In use:** "This room measured 1.2 seconds RT60 — that's why the far end says everyone sounds like they're in a shower, not a mic placement problem."
**Common misuse:** Assumed to be fixable by moving or upgrading microphones, when an RT60 problem is a room-treatment (absorption) problem that no amount of mic repositioning fully solves.

### STI (Speech Transmission Index)
A 0–1 scale measuring how intelligible speech is in a room, accounting for reverberation and background noise together; ≥0.6 is considered good for conferencing.
**In use:** "STI came back at 0.5 in that room — borderline. Before we add more mics, let's see if treating the back wall gets it to 0.6."
**Common misuse:** Confused with simple loudness or SPL — a room can be loud enough (adequate SPL) and still have poor STI because of reverberation smearing consonants.

### Nit
A unit of luminance (candela per square meter) used to rate display brightness; higher-ambient-light rooms require higher nit ratings to maintain readable contrast.
**In use:** "At 450 lux ambient we need at least a 500-nit panel — the 350-nit unit they wanted to reuse from the old room will wash out."
**Common misuse:** Treated as directly comparable to a projector's lumen rating without conversion — nits (display luminance) and lumens (projected light output) measure different things and aren't interchangeable specs.

### Lux
A unit of illuminance measuring how much light falls on a surface; the ambient-light reading taken at the screen face to determine minimum display brightness.
**In use:** "Take the lux reading with the blinds in their normal open position during the site survey, not after we've blacked out the room for the demo."
**Common misuse:** Measured under artificial "ideal" conditions (blinds closed, lights dimmed) that don't reflect how the room will actually be used day to day, producing an undersized brightness spec.

### One-touch (control-system scene)
A pre-programmed control-system macro (e.g. a Crestron/Extron/AMX touchpanel button) that sets multiple devices — display power, source routing, audio levels, shades — to a known state with a single user action.
**In use:** "The 'Video Call' one-touch scene needs to also mute the program audio and switch the mic to the far-field array — right now it only handles the display and source."
**Common misuse:** Assumed to be part of the physical installer's scope by default, when it's frequently a distinct deliverable owned by a certified control-system programmer under a separate line item.

### Signal chain / source-sink
The full path a signal travels from origin device (source) through any switching or extension hardware to the display or speaker (sink); diagnosis proceeds by isolating which link in the chain is at fault.
**In use:** "Before we blame the display, let's isolate the chain — swap the source first, since that's the cheapest and fastest test."
**Common misuse:** Skipped in favor of jumping straight to "replace the most expensive component" (usually the display) instead of methodically isolating source, transport, and sink in order of cost to test.

### Hot Plug Detect (HPD)
The physical signal line in HDMI that tells a source a display is connected and ready, triggering the EDID read; a flapping or unreliable HPD signal can cause repeated re-negotiation and visible flicker.
**In use:** "That flicker every few minutes isn't an EDID content problem — the HPD line is bouncing, probably a marginal connector, and it's forcing a re-handshake each time."
**Common misuse:** Overlooked as a distinct failure mode from EDID content mismatches — HPD is a physical/electrical signal, not data, and a bouncing HPD line produces a different repair (reseat/replace the connector) than a data mismatch does.

### Scaler
A device that converts a source's resolution/frame rate to match what the sink or transport requires, used when a source and display (or a source and a distance-limited transport) don't natively agree.
**In use:** "Put a scaler ahead of the HDBaseT extender so everything transmits at a resolution the extender's rated for, instead of hoping the source auto-negotiates down."
**Common misuse:** Treated as a fix for any resolution mismatch, including ones actually caused by EDID misconfiguration — a scaler forces a resolution change but doesn't correct a bad EDID negotiation upstream of it.

### Matrix switcher
A device that routes any of several sources to any of several displays, as opposed to a fixed point-to-point connection; the central hub in rooms or buildings with multiple sources and displays.
**In use:** "With four sources and three displays in this space, we need an 4x3 matrix switcher, not three separate point-to-point runs."
**Common misuse:** Specified at a larger port count than the room needs "for future-proofing" without a concrete plan for the additional sources/displays, adding cost and an extra point of failure in the chain for capacity that may never be used.
