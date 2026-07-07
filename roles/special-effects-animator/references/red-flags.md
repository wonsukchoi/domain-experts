# Special Effects Artist/Animator — Red Flags

### Render-farm hours tracking >20% over the shot's allocated budget mid-pipeline
- **Usually means:** simulation resolution or geometry complexity crept upward through iteration without a corresponding budget check, or a background element was built at hero-shot fidelity.
- **First question:** which stage's asset (rig, sim, geometry) grew in complexity since the last budget check, and was it a deliberate decision or scope creep?
- **Data to pull:** per-stage render-time logs and asset version history for the shot.

### A single frame or short frame range taking 3x+ longer to render than the shot's average
- **Usually means:** a localized simulation blowup (interpenetrating geometry, an exploding cloth/fluid solve) or a corrupted cache at that frame.
- **First question:** does the frame's playblast/preview show visibly broken geometry or motion at that range?
- **Data to pull:** per-frame render-time log and a preview render of the flagged frame range.

### Revision-round count exceeding the pre-agreed budget with notes still unconverged
- **Usually means:** early notes were executed literally instead of diagnosed, so the underlying story/timing problem was never actually fixed.
- **First question:** for each round so far, was the note diagnosed to a specific principle (timing, weight, staging) or executed as a literal instruction?
- **Data to pull:** the revision-round log with disposition per note.

### A note repeats across two or more rounds in different words ("make it pop," then "give it more energy")
- **Usually means:** the note is pointing at a real problem that hasn't been correctly diagnosed yet, not that the note-giver is being vague for its own sake.
- **First question:** what specific frame range or beat is the note-giver reacting to when they say this?
- **Data to pull:** a side-by-side playblast of the current version against the previous approved version, viewed with the note-giver present.

### Fur/cloth/fluid simulation cache mismatched against the current geometry or rig version
- **Usually means:** an upstream asset (rig, geometry) was updated after the simulation was cached, and the sim is now running against stale collision geometry.
- **First question:** what is the version timestamp of the simulation cache versus the version timestamp of the geometry/rig it's colliding against?
- **Data to pull:** asset version history for both the simulation cache and the geometry/rig it references.

### A shot approved at previz/blocking stage gets a structural note (staging, camera, story beat) after full animation is underway
- **Usually means:** the approval gate at previz/blocking was treated as informal rather than binding, so downstream work proceeded on an assumption that wasn't actually locked.
- **First question:** was the previz/blocking stage formally signed off, and by whom?
- **Data to pull:** the shot's pipeline approval-gate log.

### Comp requests an AOV pass that wasn't delivered from lighting
- **Usually means:** the lighting stage's render didn't output the full expected pass set, often because a late change to the shot's requirements wasn't communicated back to lighting.
- **First question:** what is the full list of AOV passes the comp script expects, and which ones are actually present in the delivered render?
- **Data to pull:** the shot's AOV pass manifest and the lighting department's render log.

### A "locked" shot has an open revision request against it
- **Usually means:** either the lock wasn't actually communicated/enforced, or the request is being treated as a minor tweak when it's actually a formal reopen with cascading cost.
- **First question:** has the cost of the reopen (recalculated render-hours, and the cascading impact on lighting/comp already built against the locked version) been quoted back to whoever requested the change?
- **Data to pull:** the shot's lock date/version and the render-budget recalculation for the requested change.

### Rig deformation errors (pinching, volume loss) appear only at extreme poses, not in the animator's normal working range
- **Usually means:** the rig was tested and approved within a typical pose range but wasn't validated against the full range of poses the shot actually requires.
- **First question:** does the shot's blocking pass include any pose outside the rig's originally tested range?
- **Data to pull:** the rig's validation test-pose set versus the shot's actual pose range in the animation.

### Render-farm node allocation for this shot was reduced without a corresponding schedule extension
- **Usually means:** nodes were reallocated to a higher-priority shot elsewhere in the production without the downstream schedule impact being recalculated for this shot.
- **First question:** what is the new wall-clock estimate at the reduced node count, and does it still fit the delivery deadline?
- **Data to pull:** current node allocation and the render-budget worksheet recalculated at the new count.
