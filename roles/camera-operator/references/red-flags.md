# Red flags

Smell tests an experienced operator (or a DP reviewing dailies) catches fast, before they compound into a scene that can't be cut.

### A "clean" circle take with no operator notes on a complex handheld or Steadicar shot

**Usually means:** either the take really was clean, or the operator didn't distinguish "technically usable" from "matches the other angles" — a common gap on rushed setups where nobody had time to review playback before moving on.

**First question:** "Did you check this against the reverse/reaction shot for line and eyeline before circling it?"

**Data to pull:** the corresponding reverse-angle camera report for the same scene; playback of both angles cut together, not reviewed in isolation.

### Reframe visible in the middle third of a take, on a subject that was blocked and rehearsed

**Usually means:** the operator didn't trust the rehearsed blocking and chased live movement that was actually within normal tolerance, producing visible camera hunt where none was needed.

**First question:** "Was this drift bigger than what we rehearsed, or did the camera react to something that would've self-corrected?"

**Data to pull:** the blocking rehearsal note/mark sheet; compare actual actor position at the reframe moment against the marked position.

### Shutter angle or frame rate changed mid-scene without a script supervisor or DP note

**Usually means:** a rig setting reverted after a battery change, card swap, or crew handoff, and nobody caught it before rolling — the most common source of a motion-blur or frame-rate mismatch discovered only in the edit.

**First question:** "Pull up the camera report for every setup in this scene — do frame rate and shutter angle match across all of them?"

**Data to pull:** camera reports for every setup/take in the scene; metadata embedded in the footage itself (most digital cinema cameras log this per clip) cross-checked against the paper report.

### Framing centers the subject well inside a 16:9 comfort zone but the delivery spec includes a vertical or square crop

**Usually means:** the operator framed to house style for the acquisition ratio without checking the delivery contract, which is common when a crew is used to broadcast-only delivery and the vertical/social requirement was added later or communicated only to the producer.

**First question:** "What's the narrowest aspect ratio this footage needs to survive, and did we frame for that one or for 16:9?"

**Data to pull:** the delivery spec/format contract for the segment; the actual pixel coordinates of the subject against the safe-zone math for the narrowest required crop (see `references/playbook.md`).

### Operator reports "focus was a little soft, but it's probably fine"

**Usually means:** a genuine borderline call that needs a second opinion before the setup strikes, not after — "probably fine" said out loud is itself the signal that it isn't confidently fine.

**First question:** "Can we check it on a bigger monitor or magnify the playback before we move on, while the setup's still up?"

**Data to pull:** the 1st AC's focus chart/distance log for the take; magnified/zoomed playback rather than the on-set monitor at normal size.

### A location or rig setup changed (new terrain, added platform, extended crane reach, rail/road proximity) with no fresh safety meeting

**Usually means:** the crew is treating a materially different physical hazard as a continuation of a previously-cleared setup — the exact failure pattern behind the 2014 on-set fatality of a camera trainee during production of *Midnight Rider*, where a location change (an active rail trestle) proceeded without the rail owner's permission or a hazard-specific safety plan.

**First question:** "Has this exact setup — this platform, this terrain, this proximity to traffic/rail/water — had its own safety meeting, or are we running on this morning's general one?"

**Data to pull:** the day's safety meeting sign-off log; permits for the specific hazard (rail, water, aerial, road closure) if one applies.

### Camera operator is also being asked to pull their own focus on a shallow-depth, long-lens shot

**Usually means:** a budget-driven crew reduction that's quietly merging two jobs with different feedback loops — the operator watches the whole frame, the focus puller watches distance and depth of field; doing both at once degrades whichever one gets less attention in the moment it matters.

**First question:** "On this lens and stop, what's our actual depth of field at the working distance — is this a shot that tolerates being self-pulled?"

**Data to pull:** depth-of-field calculation for the specific lens/T-stop/distance combination; a look at whether previous takes on this setup show focus drift correlating with reframe moments.

### Multiple operators on a multi-cam setup (broadcast, live event) report different read-backs of which side of the line is "correct"

**Usually means:** the 180-degree axis was never explicitly called out loud on comms before the segment started, so each camera position is operating on its own assumption.

**First question:** "Who called the line for this segment, and was it communicated to every camera position before we went live?"

**Data to pull:** the technical director or A2's pre-segment camera-position brief, if one exists; a still frame from each camera position to visually confirm axis agreement.
