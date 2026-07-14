# Vocabulary

### Cold solder joint
A soldered connection with insufficient heat or wetting during formation, resulting in higher electrical resistance and reduced mechanical strength while often looking visually similar to a properly formed joint.
**In use:** "That joint's cold — passed continuity but the wetting coverage is way under spec, and it'll likely fail under thermal cycling."
**Common misuse:** Judging a solder joint's quality by whether it currently passes a continuity test — a cold joint can pass initial continuity while still lacking the wetting/mechanical strength needed for long-term reliability under thermal and mechanical stress.

### Wetting angle / fillet coverage
The specific geometric criteria (how completely and smoothly solder flows around and bonds to a joint) defined by workmanship standards like IPC-A-610, used to objectively judge solder joint acceptability.
**In use:** "Two hundred seventy degrees minimum for Class 2 — measuring this joint at one-eighty, that's a reject regardless of how it looks holding the part."
**Common misuse:** Substituting a subjective "looks properly soldered" impression for the standard's specific numeric wetting/coverage criteria — different assemblers' personal standards for "looks fine" vary, which is exactly why the objective standard exists.

### ESD (electrostatic discharge) latent damage
Component damage from static electricity exposure that doesn't destroy the component outright but degrades it in a way that causes premature failure or intermittent behavior later, rather than immediate, obvious failure.
**In use:** "That intermittent fault three months after shipping traces back to ESD exposure during assembly — the component worked fine at first, just not for long."
**Common misuse:** Assuming a component that functions correctly right after assembly is confirmed free of ESD damage — latent ESD damage specifically doesn't show up at initial functional test, only later in service.

### IPC-A-610 / J-STD-001
Industry workmanship standards defining specific, objective acceptability criteria for electronic assembly solder joints and related workmanship, used in place of individual assembler judgment.
**In use:** "We're inspecting to IPC-A-610 Class 2 criteria — that's the actual bar, not whatever looks acceptable to any individual inspector."
**Common misuse:** Treating workmanship standards as general guidelines that experienced assemblers can override with personal judgment — the standards exist specifically to remove that variability and establish an objective, consistent acceptability bar across all assemblers and inspectors.

### Crimp pull test
A destructive or sample-based test measuring the force required to pull a wire out of a crimped terminal, used to verify adequate mechanical/electrical connection beyond what visual inspection can confirm.
**In use:** "Pull test on this sample crimp came back below spec — that's a tooling issue, not something we'd have caught looking at it."
**Common misuse:** Accepting a crimped connection based on visual appearance (does it look properly compressed) rather than actual pull force or crimp height measurement — a visually acceptable-looking crimp can still have insufficient holding force or excessive compression damaging wire strands.

### Crimp height
A precise dimensional measurement of a crimped terminal's compressed height, used as a proxy verification for proper crimp force when pull testing every unit isn't practical.
**In use:** "Crimp height's within spec on this sample — that correlates with adequate pull force without destructively testing every single unit."
**Common misuse:** Skipping crimp height measurement entirely in favor of visual inspection alone — height measurement provides an objective, repeatable proxy for crimp quality that visual inspection cannot reliably replicate.

### Single-point failure (electronic assembly)
The characteristic of electronic assembly defects where one bad joint, damaged component, or inadequate connection can be the sole cause of complete assembly failure, regardless of how correctly the rest of the assembly was performed.
**In use:** "One bad joint out of hundreds is still a complete failure point — this isn't a defect that gets diluted by all the good joints around it."
**Common misuse:** Treating a single suspected defect as a minor concern relative to the overall quality of the assembly — electronic assemblies typically don't average out defects the way some other manufacturing processes might; one genuine defect point is often sufficient for complete failure.

### ESD-safe workstation
A work area equipped with grounding mats, wrist straps, and other controls specifically designed to prevent static electricity buildup and discharge during handling of ESD-sensitive components.
**In use:** "Every ESD-sensitive component on this bench gets handled at the grounded station — no exceptions for 'quick' handling."
**Common misuse:** Treating ESD-safe workstation procedures as necessary only for handling that "feels" risky (a component that's visibly delicate) — ESD sensitivity is a property of the specific component, not something judged by how it looks or how briefly it's handled.

### Workmanship class (IPC standard)
A classification (e.g., Class 1, 2, 3 in IPC-A-610) specifying the required reliability level and corresponding inspection criteria for an assembly, based on its intended application's consequence of failure.
**In use:** "This is Class 3 — aerospace application — so the acceptance criteria are tighter than the Class 2 consumer-product line running next to it."
**Common misuse:** Applying a single workmanship class's criteria uniformly across different products or applications — the appropriate class depends on the specific product's application and consequence-of-failure profile, and using the wrong class's criteria either over- or under-verifies relative to what the application actually requires.
