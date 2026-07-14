# Red flags

### Fold-line or score-line cracking appearing on converted product
- **Usually means:** paper moisture below the specified range, causing brittleness at fold lines — not necessarily a tooling issue.
- **First question:** has paper moisture been measured directly, or is the diagnosis focused on blade/creasing tool condition?
- **Data to pull:** current moisture reading, tooling condition/sharpness log, ambient humidity conditions.

### Adhesive bond confirmed only by visual presence, not a peel/pull strength test
- **Usually means:** actual bond quality hasn't been verified — visible glue doesn't confirm correct bonding occurred.
- **First question:** has a peel/pull test been performed on a sample from this run, or only a visual check?
- **Data to pull:** bond strength test results if performed, adhesive application parameters (quantity, temperature).

### Web tension held at a single fixed setting throughout a roll's full run
- **Usually means:** tension isn't being adjusted as roll diameter decreases, risking either excessive tension (late in the roll) or insufficient tension (varies by system design).
- **First question:** does the tension control system or manual setting account for changing roll diameter, or is it fixed?
- **Data to pull:** tension setting history across the roll's run, roll diameter at points of any web break/wrinkle.

### Converting speed increased without re-verifying fold/cut/bond quality at the new speed
- **Usually means:** an assumption that a speed increase is dimensionally/quality neutral, when it can interact with moisture or tension conditions.
- **First question:** was a quality check performed at the new speed before full-run commitment, or was the increase assumed safe?
- **Data to pull:** quality check results at the new speed, moisture/tension conditions at time of the speed change.

### A defect rate that worsens as a production run continues
- **Usually means:** a drifting process variable (moisture change, roll diameter/tension shift, ambient condition change) rather than a fixed setup error.
- **First question:** does the defect rate trend upward over the run, or was it present and consistent from the start?
- **Data to pull:** defect rate trend data across the run, any process variable trend data (moisture, tension) over the same period.

### A web break or tear occurring late in a roll's run (near-empty roll)
- **Usually means:** tension not adjusted for the smaller roll diameter, resulting in excessive actual web stress at the same nominal tension setting.
- **First question:** was tension adjusted as the roll diameter decreased, or held at the same setting throughout?
- **Data to pull:** roll diameter at time of break, tension setting history for this roll.

### Incoming paper stock moisture not checked before starting a run
- **Usually means:** an assumption that storage conditions or supplier compliance guarantees in-spec moisture at time of use.
- **First question:** has moisture been measured for this specific lot at the point of use, or only assumed from storage/supplier spec?
- **Data to pull:** current lot's moisture measurement, supplier's stated spec for comparison.

### Adhesive bleed-through or visible residue on finished product
- **Usually means:** excess adhesive quantity or incorrect application temperature, rather than an inherent adhesive quality issue.
- **First question:** does actual adhesive quantity/temperature match the specification for this paper/adhesive combination?
- **Data to pull:** adhesive application settings (quantity, temperature), specification for this combination.

### A machine/tooling adjustment made in response to a quality issue without checking moisture or tension first
- **Usually means:** the actual root cause (a process variable) may not have been checked before a mechanical adjustment was made.
- **First question:** were moisture and tension ruled out before adjusting or replacing tooling?
- **Data to pull:** moisture/tension readings at time of the issue, sequence of diagnostic steps taken.

### A shift handoff not specifying current roll diameter, tension setting, or recent moisture checks
- **Usually means:** the incoming operator lacks the process-variable context needed to anticipate a developing issue (like an approaching low-diameter tension adjustment point).
- **First question:** does the handoff specify roll status and recent moisture/tension data, or just general "running fine"?
- **Data to pull:** the handoff record, current roll/process status.
