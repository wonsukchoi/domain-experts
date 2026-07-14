# Vocabulary

### Surface speed (SFM)
The actual linear speed at which a workpiece's surface moves past the cutting tool, measured in surface feet per minute, which depends on both spindle RPM and workpiece diameter and determines optimal cutting conditions.
**In use:** "Same RPM, but the diameter dropped from two inches to one — surface speed is now half what it was, not the same as before."
**Common misuse:** Treating spindle RPM as the parameter that determines cutting conditions — RPM alone doesn't determine surface speed, since surface speed also depends on workpiece diameter, and holding RPM constant across different diameters produces different surface speeds at each.

### Runout (workpiece)
The amount a workpiece deviates from true rotation around its intended axis when chucked, measured with a dial indicator, representing an error source independent of tool condition or program accuracy.
**In use:** "Checked runout before starting — point-oh-oh-eight inches, well within our point-oh-oh-one spec... wait, that's actually outside spec, need to re-chuck."
**Common misuse:** Assuming a correctly programmed toolpath guarantees a correctly formed part — if the workpiece itself isn't centered accurately in the chuck (has runout), even perfect tool programming produces an eccentric or out-of-round result.

### Chatter (turning)
Vibration during a turning operation, often caused by insufficient workpiece rigidity (a high length-to-diameter ratio) or cutting parameters exceeding what the setup can support without vibrating, producing a characteristic wavy surface defect.
**In use:** "That wavy surface pattern is chatter from this long, thin shaft flexing — reducing depth of cut and adding a steady rest."
**Common misuse:** Assuming chatter always traces to tool sharpness or machine condition — workpiece rigidity itself (determined by its length-to-diameter ratio) is a common, distinct cause requiring reduced parameters or additional support, not a tool or machine fix.

### Length-to-diameter ratio (turning)
The ratio between a workpiece's unsupported length and its diameter, a key factor in how prone the workpiece is to chatter/deflection during turning, analogous to reach-to-diameter ratio in boring operations.
**In use:** "Ten-to-one length-to-diameter on this shaft — that's well into the range where we need a steady rest, not standard parameters."
**Common misuse:** Applying standard cutting parameters regardless of a workpiece's length-to-diameter ratio — a long, slender workpiece flexes under cutting load in a way a short, stubby one doesn't, requiring reduced parameters or added support specifically because of this ratio.

### Tool nose radius
The radius of a cutting tool's tip, which affects surface finish independently of feed rate — a larger nose radius can produce a smoother finish at a given feed rate than a smaller one.
**In use:** "Finish issue traces to the tool nose radius, not feed rate — swapping to a tool with a larger radius for this operation."
**Common misuse:** Assuming feed rate is the only parameter affecting surface finish — tool nose radius and cutting speed both interact with feed rate to determine the actual resulting finish, and a finish problem can trace to any of these, not feed rate by default.

### Steady rest / tailstock support
Auxiliary supports used to stabilize a long workpiece during turning, reducing deflection and chatter risk for high length-to-diameter ratio parts.
**In use:** "Adding a steady rest mid-length on this shaft — without it, the unsupported span is going to chatter at any reasonable cutting speed."
**Common misuse:** Treating support fixtures as optional convenience items rather than a functional requirement for workpieces exceeding a certain length-to-diameter ratio — beyond a certain ratio, standard turning parameters simply aren't achievable without additional support regardless of operator skill.

### In-process dimensional monitoring
Measuring a critical turned dimension at intervals during a production run, rather than relying on tool condition inspection or end-of-run checks alone, to catch tool-wear-driven dimensional drift.
**In use:** "Checking this diameter every twenty parts — tool wear on a turning operation shows up as dimension drift before it's visually obvious on the insert."
**Common misuse:** Relying on visual tool inspection to judge whether dimensions are still accurate — turning tool wear can produce measurable dimensional drift before it's visually apparent, making periodic direct measurement of the actual part dimension the more reliable check.

### Feed rate (turning, interacting parameter)
The rate at which the cutting tool advances along the workpiece per revolution, one of several parameters (along with cutting speed and tool nose radius) that together determine surface finish, rather than the sole determinant.
**In use:** "We adjusted feed rate first, but the finish issue was actually the nose radius — feed rate alone wasn't the whole story."
**Common misuse:** Treating "slower feed rate improves finish" as a universal rule applicable regardless of other parameters — feed rate interacts with cutting speed and tool nose radius, and a finish problem isn't always solved (and can sometimes be worsened, similar to chip-load-and-burning dynamics in other machining contexts) by adjusting feed rate alone.
