# Vocabulary

Terms generalists conflate that a booth keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse to avoid.

### DCP vs. digital file

A **DCP (Digital Cinema Package)** is a specific, standardized package of encrypted, JPEG2000-encoded image and PCM audio files plus XML metadata (CPL, PKL, ASSETMAP), built to the DCI/SMPTE spec for theatrical playback on certified servers. A generic "digital file" (a ProRes master, an MP4 screener) is not interchangeable with it and won't play on a cinema server without conversion.

**In use:** "We got sent a ProRes screener instead of the DCP — that's not a swap-in, it needs to go through mastering first."

**Common misuse:** treating any digital movie file as "basically the same as a DCP" because both are non-film. The encryption, encoding, and playback-certification chain are what make a DCP specifically theatrical.

### KDM vs. certificate

A **KDM (Key Delivery Message)** is the encrypted key, generated per-server and per-title, with a stated validity window, that unlocks a specific DCP for playback on one piece of hardware. A **certificate** is the server/IMB's own cryptographic identity (tied to its serial number) that the KDM is issued against — swap the hardware, and the old KDM no longer matches.

**In use:** "The KDM's fine, the problem is it was cut against the old IMB's certificate before the swap."

**Common misuse:** treating "we have the KDM" as sufficient without checking it matches the currently installed server's certificate and hasn't passed its validity window.

### Interop vs. SMPTE (DCP packaging standards)

**Interop** was the earlier, pre-standardization DCP packaging format used industry-wide before the formal SMPTE DCP standard (the ST 429 series) was finalized and widely adopted. Most current releases are SMPTE-packaged; Interop still turns up on older or independently mastered content.

**In use:** "This festival short came in as Interop — check the server supports it before assuming it'll ingest like everything else this week."

**Common misuse:** assuming every DCP a booth receives uses the same packaging standard; a server or workflow tuned only for SMPTE packages can choke on an Interop DCP without warning.

### Foot-lambert vs. lumens

**Lumens** measure total light output from the projector as a source. **Foot-lamberts (fL)** measure luminance actually reflected off the screen toward the audience — the number that accounts for screen size, throw distance, screen gain, and losses in the optical path. A projector's rated lumens tells you almost nothing about whether the screen is calibrated correctly.

**In use:** "It's rated at 30,000 lumens, but screen center is only reading 10.8 fL — check the lens and iris before assuming the lamp's the problem."

**Common misuse:** citing a projector's lumen rating as evidence a screen is bright enough, instead of measuring the actual foot-lambert reading at the screen.

### Changeover vs. platter

A **changeover** is the classic dual-projector technique of switching between two running projectors at a reel break, cued by marks on the film, so the audience never sees a break. A **platter system** eliminates changeovers by splicing all reels into one continuous loop run from a single large horizontal platter, at the cost of extra handling stress on the print during buildup.

**In use:** "This print's too fragile for the platter — we're running it as a changeover instead."

**Common misuse:** assuming platter presentation is strictly an upgrade over changeover in every case; for fragile or archival prints, changeover's lower handling stress makes it the better choice despite needing a second trained operator.

### Frame rate vs. refresh rate

**Frame rate** is how many unique frames of content exist per second (24fps standard; 48fps/HFR for specific masters). **Refresh rate** (or shutter rate) is how many times the projector actually flashes light through the image per second, which can be a multiple of the frame rate (triple-flashing 24fps content to 72Hz reduces flicker; 3D systems often run at higher effective rates to alternate left/right eye images).

**In use:** "Content's still 24fps — we're just running triple-flash for flicker, don't confuse that with an HFR master."

**Common misuse:** assuming a projector "running at 144Hz" means the content itself is a high-frame-rate master, rather than the same 24 or 48fps content flashed multiple times per unique frame.

### Aspect ratio: flat vs. scope

**Flat (1.85:1)** and **scope/anamorphic (2.39:1, sometimes labeled 2.35:1 on older prints)** are the two dominant theatrical aspect ratios, requiring different masking (and, for anamorphic film prints, a different lens) to present correctly. A title shown in the wrong masking either loses picture information or shows unintended black bars.

**In use:** "Tonight's title is scope — reset the masking before house-open, the last show in this room was flat."

**Common misuse:** trusting the automation's carried-over masking preset instead of verifying it against the specific title being shown that day.

### ISDCF naming convention

The **ISDCF (Inter-Society Digital Cinema Forum)** naming convention is the standardized filename structure encoding a DCP's title, rating, language, aspect ratio, audio format, resolution, and territory into the package name itself — the first thing a booth reads to sanity-check a package before ingest.

**In use:** "The filename says '_51_2K_US' — that's a 5.1 mix, 2K, US territory version; check that's actually what's booked before we ingest the wrong region's cut."

**Common misuse:** ingesting a DCP without reading its ISDCF-coded filename against the booking sheet, which is how a wrong-region or wrong-rating version slips through undetected until showtime.

### Atmos bed vs. objects

In a **Dolby Atmos** mix, the **bed** is the traditional fixed-channel audio (typically 7.1 or 9.1) that plays through the room's standard channel layout; **objects** are discrete sound elements with metadata that route dynamically to individual overhead and surround speakers based on the room's actual speaker map. A room without Atmos-capable processing and speaker layout plays only the bed, not the objects.

**In use:** "This room's not Atmos-equipped — it'll play the 7.1 bed fine, we're just not getting object placement."

**Common misuse:** assuming any DCP labeled "Atmos" requires special handling to play at all; a non-Atmos room plays the embedded bed mix without failure, it just doesn't render the object layer.

### Ghosting/crosstalk (3D)

**Ghosting**, or crosstalk, is the visible double-image artifact in 3D projection where the left- and right-eye images aren't being fully separated — light meant for one eye leaks into the other. It's a system synchronization or polarization fault, not a property of the 3D content itself.

**In use:** "Ghosting's showing up across the whole house, not just off-angle seats — that's the filter wheel, not a seating issue."

**Common misuse:** dismissing ghosting complaints as normal 3D eye strain or seating-angle artifacts without checking whether the pattern is house-wide (system fault) versus isolated to extreme side seats (a genuine viewing-angle limitation).
