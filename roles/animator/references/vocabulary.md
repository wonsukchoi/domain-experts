# Animator — Vocabulary

### Blocking
The stepped, pose-to-pose pass that establishes a shot's key poses and their rough timing, held at hard/stepped interpolation so no in-between motion is visible yet — the pass a director approves before any smoothing work begins.
**In use:** "Blocking's up for review — don't touch spline until staging is signed off."
**Common misuse:** Treated as a rough draft that can be skipped or rushed through, when it's actually where the acting choice and timing get locked; errors here compound through every later pass.

### Spline
The pass that converts stepped blocking keys into smooth, continuous motion by interpolating between them (named for the spline/curve interpolation in the graph editor), producing the first version of the shot that actually moves rather than snapping between poses.
**In use:** "It's splined but not polished yet — the arcs are still rough on the reach."
**Common misuse:** Confused with the final pass; a spline-clean shot is a legitimate, shippable tier for coverage work, not an unfinished hero shot.

### Polish
The final pass adding secondary action, overlap, follow-through, and finishing detail on top of an approved spline — the tier reserved for shots that carry story weight, not applied by default to every shot in a batch.
**In use:** "This is a Tier 1 shot, budget it for a full polish pass, not just spline-clean."
**Common misuse:** Assumed to be a fixed percentage of every shot's timeline rather than a tier decision made per shot based on story function.

### Pose-to-pose
An animation approach that plans key poses first, then fills in the timing and in-betweens — the default for dialogue and story-beat-critical motion because it locks the timing a specific line or cut needs to land on.
**In use:** "Keep this pose-to-pose — the punchline has to land exactly on frame 48."
**Common misuse:** Assumed to be the only correct method for all animation, when organic secondary motion (hair, cloth, chaotic elements) often reads better built straight-ahead.

### Straight-ahead
An animation approach that animates frame by frame in sequence from the start of a shot to the end, without pre-planned key poses — produces looser, more organic motion but is prone to drifting off a fixed timing target.
**In use:** "Do the tail straight-ahead over the locked body keys — it doesn't need to hit a specific frame."
**Common misuse:** Used on a dialogue-critical primary layer where a specific frame (a lip-sync beat, a hit cue) has to be hit, causing sync drift that then has to be manually corrected.

### Graph editor / spacing
The curve-editing interface (in Maya, Blender, and similar tools) that controls the rate of change between keyframes — the actual home of a shot's timing, since two shots with identical key poses can read completely differently depending on how the curve eases in and out of each key.
**In use:** "The pose is right — just ease the graph editor curve out slower on the anticipation before the hit."
**Common misuse:** Ignored in favor of adjusting keyframe positions or adding new poses, when most "timing feels wrong" notes are actually spacing-curve problems solvable without touching a single pose.

### Gimbal lock
A rig control failure where two of a joint's three rotation axes align and collapse a degree of freedom, causing the joint to snap, flip, or become impossible to rotate cleanly through a required pose.
**In use:** "The shoulder gimbal-locks past 90 degrees of rotation — flag it for a corrective before we spline the reach."
**Common misuse:** Misdiagnosed as an animator error (a bad key) rather than a rig control limitation, leading to repeated manual workarounds instead of a corrective fix.

### Corrective (blend shape / driven key)
A targeted fix layered onto a rig to resolve a specific pose failure — a sculpted shape or a driven-key relationship triggered at a problem angle — used instead of a full re-rig when the failure is isolated to a small number of shots.
**In use:** "Add a corrective at 90 degrees of elbow bend so the sleeve stops clipping through the forearm."
**Common misuse:** Applied shot-by-shot indefinitely even after the same failure recurs across many shots, when recurrence past a handful of shots is the signal to fix the rig itself.

### Secondary action
Motion that supports and enriches a primary action without competing with it for attention — a character's hand gesture while talking, cloth settling after a stop.
**In use:** "Add secondary action on the coat hem after the landing — it's a Tier 1 shot, it can carry the extra beat."
**Common misuse:** Added to every shot regardless of tier, or added so prominently it upstages the primary action it's meant to support.

### Anticipation
A small preparatory motion, contrary to or preceding a main action, that telegraphs the action to the audience before it happens (a wind-up before a punch, a crouch before a jump).
**In use:** "Give it two more frames of anticipation before the jump — right now it reads as popping into the air."
**Common misuse:** Confused with a delay or pause; anticipation is a directional counter-motion, not just added time before the main action starts.

### Contact lock (mocap cleanup)
A cleanup step on captured motion that pins a foot, hand, or prop to a fixed point during contact (a footstep, a handhold) to remove sliding or drift the raw capture data introduces.
**In use:** "The mocap's got foot sliding on both plants — run a contact-lock pass before this ships."
**Common misuse:** Skipped on the assumption raw mocap data is contact-accurate by default; capture volumes routinely introduce sliding that reads as weightlessness if uncorrected.

### Shot tier
A production classification (hero, coverage, background) assigned to a shot based on its story function, determining which pipeline passes (blocking/spline/polish) it receives and its scheduled hours.
**In use:** "That's a Tier 2 shot — blocking and spline only, no dedicated polish pass unless it gets upgraded in review."
**Common misuse:** Treated as fixed for the life of the production rather than something a director's review can upgrade or downgrade as the cut changes.
