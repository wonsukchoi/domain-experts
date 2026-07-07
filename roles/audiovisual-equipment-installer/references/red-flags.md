# Red Flags

### Display works from a laptop input but shows blank/flicker from the permanently installed PC on the same run
- **Usually means:** EDID mismatch (extender or switcher passing a fallback/cached table instead of the display's native EDID), then an HDCP compliance break somewhere in the chain.
- **First question:** "Does a second source device at the same wall plate behave the same way?"
- **Data to pull:** Handheld EDID reader capture of the currently-negotiated EDID vs. the display's native EDID; extender's EDID-mode setting (internal vs. pass-through).

### Signal run measured or estimated beyond ~130ft (40m) while still speccing 4K60 4:4:4 over standard HDBaseT
- **Usually means:** Transport/extender class doesn't actually support full-chroma 4K60 at that distance; the "it displayed an image" test at commissioning used a lower-bandwidth test pattern or resolution than production content.
- **First question:** "What's the extender's rated distance at the exact resolution and chroma subsampling this room will actually run?"
- **Data to pull:** Extender manufacturer's distance/bandwidth class spec sheet; commissioning test log showing the resolution/chroma actually used during acceptance.

### Passive HDMI cable run over ~15ft (5m) carrying 4K60 4:4:4
- **Usually means:** Passive copper is being pushed near or past its reliable signal-integrity range; an image that "looks fine" at commissioning is a marginal pass, not a clean one.
- **First question:** "Was this tested with the actual production source and resolution, or a lower-bandwidth signal generator?"
- **Data to pull:** Cable certification/category rating; a re-test at full production resolution with a protocol analyzer, not just a visual check.

### Farthest viewer seated beyond 6x the image height in a room used for spreadsheets, CAD, or fine text
- **Usually means:** Display was sized to available wall space or budget rather than to the room's actual seating depth and content type.
- **First question:** "What's the farthest seat from the screen, and what will people actually be reading off it?"
- **Data to pull:** Room floor plan with seating layout; content samples (font size, detail level) planned for the room.

### Ambient lux reading at the screen face above 300 lux with a display spec'd under 500 nits
- **Usually means:** Brightness was spec'd to a standard conference-room panel default without a light-meter reading, or the reading was taken with blinds closed rather than in worst-case (open) condition.
- **First question:** "Was the lux reading taken with the shades in their most-open realistic position?"
- **Data to pull:** Light-meter reading log with time of day and shade position noted; display's nit spec sheet.

### Room's measured RT60 above 0.8 seconds in a dedicated conferencing/huddle room
- **Usually means:** Hard surfaces (glass, drywall, exposed ceiling) with no absorptive treatment; acoustics were not designed, only defaulted to whatever finish materials the architect chose.
- **First question:** "Was acoustic treatment part of the original scope, or added after the room sounded bad on a call?"
- **Data to pull:** RT60/STI measurement log; room finish schedule (ceiling tile type, wall material, floor covering).

### Distributed ceiling speakers spaced wider than ~2x the mounting height above ear level
- **Usually means:** Speaker layout followed the ceiling tile grid or architectural symmetry instead of coverage math, producing dead zones between speakers.
- **First question:** "Was speaker spacing calculated from mounting height, or laid out to match the ceiling grid?"
- **Data to pull:** Reflected ceiling plan with speaker locations; mounting height above the seated ear-height plane.

### Control-system one-touch scenes deployed with no separate sign-off from a certified programmer
- **Usually means:** The installer wrote or modified control logic outside their certification scope, or the SOW never named who owns programming acceptance.
- **First question:** "Who is the certified programmer of record for this system, and did they test every scene?"
- **Data to pull:** SOW scope-of-work section defining install vs. programming responsibility; scene-by-scene test log with the programmer's sign-off.

### No documented commissioning/verification checklist delivered at handoff
- **Usually means:** Acceptance testing was informal ("it powered on, demo worked") rather than a documented pass across every input, resolution, and control scene.
- **First question:** "Can you show me the commissioning checklist that was signed off before this room went live?"
- **Data to pull:** Commissioning checklist (or its absence); punch-list/closeout documentation from the project file.

### Speaker/microphone setup produces audible echo or "hollow" sound reported only by the far end of a video call
- **Usually means:** Acoustic echo cancellation (AEC) misconfiguration or a microphone pickup pattern mismatched to the room's reverberation, not a defect audible to people physically in the room.
- **First question:** "Has this been reproduced from the far end's perspective, or only judged by how the room sounds in person?"
- **Data to pull:** Far-end recording of a test call; mic placement diagram and pickup pattern spec vs. measured RT60.

### No labeled as-built cable/rack documentation delivered to the client
- **Usually means:** Documentation was treated as optional once the room demoed successfully, leaving the next service call to re-discover the signal chain from scratch.
- **First question:** "Is there a rack elevation and cable-label map in the client's own files, not just the installer's?"
- **Data to pull:** As-built rack elevation diagram; cable label schedule cross-referenced against the physical labels in the rack.

### Screen or rack installed with no service loop or access path for future cable reseating
- **Usually means:** Cable was pulled tight to the minimum length needed at install, with no slack for a future connector reseat or a display swap without re-pulling cable.
- **First question:** "Is there a service loop behind the display, or is this cable pulled drum-tight?"
- **Data to pull:** Photos of the cable dressing behind the display/rack; installation standard used (if any) for minimum slack.
