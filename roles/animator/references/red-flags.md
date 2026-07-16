# Animator — Red Flags

### A coverage or background shot is receiving a dedicated polish pass
- **Usually means:** the tier assignment was skipped or ignored, and hours are being spent on secondary action/overlap the story doesn't need for that shot.
- **First question:** what tier was this shot assigned, and does the current pass match it?
- **Data to pull:** the shot-tier tracker's assigned tier versus the shot's logged pass status.

### Spline pass started before blocking was formally approved
- **Usually means:** a director's pose or staging note is about to turn into a full re-block-and-re-spline instead of a cheap blocking tweak.
- **First question:** has this shot's blocking been signed off, and by whom, before spline work began?
- **Data to pull:** the shot-tracking database's approval timestamp against the spline pass's start time.

### A dialogue or lip-sync-critical shot was animated straight-ahead
- **Usually means:** the motion has likely drifted off the fixed sync target the line reading or sound cue requires.
- **First question:** does the shot's key timing land on the same frames as the dialogue track's phoneme/beat marks?
- **Data to pull:** the animation curve's key frames against the dialogue track's waveform or lip-sync chart.

### A rig control clips, gimbal-locks, or can't reach a required pose in more than 5 shots
- **Usually means:** this is no longer a per-shot workaround territory — it's a rig-team fix that a corrective blend shape on each shot won't scale to.
- **First question:** how many shots have hit this same control failure, and is a rig fix already scheduled?
- **Data to pull:** the rig-workaround log, filtered by control name and failure type.

### A director's revision note uses timing language ("too slow," "snaps," "doesn't land") but the animator re-poses the shot
- **Usually means:** the note was a spacing/graph-editor problem, not a pose problem, and re-posing risks introducing a new error while leaving the actual complaint unaddressed.
- **First question:** does the note describe a hold/ease/spacing issue or a silhouette/staging issue?
- **Data to pull:** the revision-note triage log's classification field (pose vs. timing) for this note.

### A batch's logged hours-per-shot are being averaged across tiers
- **Usually means:** the next block's schedule estimate will be wrong in both directions — overbidding background shots and underbidding hero shots.
- **First question:** is the hours-per-shot log broken out by tier, or is it one blended average?
- **Data to pull:** the production tracker's hours-logged field, grouped by tier rather than by shot count alone.

### More than a third of a batch's shots are upgraded from coverage to hero tier after one review round
- **Usually means:** the initial tier classification was wrong, or the story cut changed enough that the schedule built against the old tier split is no longer valid.
- **First question:** what changed between the original tier assignment and this review — story cut, director notes, or both?
- **Data to pull:** the shot-tier tracker's tier-change history against the edit/cut version it was reviewed under.

### A shot marked "polish complete" has no secondary-action or overlap keys on any non-primary control
- **Usually means:** the shot was marked done at spline-clean quality but logged as if the polish pass happened.
- **First question:** which controls beyond the primary body/face rig have keys, and when were they added?
- **Data to pull:** the animation curve editor's keyed-control list for the shot, checked against the tier-appropriate pass definition.

### A mocap-sourced shot was shipped without a cleanup pass on foot contact or hand/prop contact
- **Usually means:** captured data's foot sliding or contact drift wasn't corrected, and it will read as weightless or physically wrong on review.
- **First question:** was a contact-lock pass run on this shot's feet and any prop/hand interactions?
- **Data to pull:** the mocap cleanup checklist for the shot, specifically the contact-lock field.
