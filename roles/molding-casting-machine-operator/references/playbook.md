# Playbook

## Cavity-pressure diagnostic worksheet

Fill when a quality issue persists despite in-spec machine-displayed parameters.

| Field | Value |
|---|---|
| Job | DC-2291, Aluminum Bracket |
| Machine-set injection pressure | 2,000 psi |
| Defect | Intermittent porosity, 1-in-20 X-ray sample rate |
| Cavity pressure sensor data (if available) | 1,200-1,600 psi (inconsistent vs. constant 2,000 psi set) |
| Suspected flow-path restriction location | Shot sleeve fill |
| Shot sleeve fill % (measured) | 60% |
| Shot sleeve fill % (spec minimum) | 70% |
| Root cause | Metering/ladle inconsistency causing sub-spec fill, air entrapment |
| Corrective action | Adjust metering/ladle process to consistently achieve ≥70% fill |
| Verification sample size | 40 parts post-correction |
| Verification result | 0 porosity findings (vs. prior 5% rate) |

## Short-shot/flash adjustment decision table

| Symptom | Adjustment direction | Check after adjustment |
|---|---|---|
| Short shot (incomplete fill) | Increase shot size, injection pressure, or speed | Re-inspect for flash at parting line / vents after adjustment |
| Flash (excess material at parting line) | Decrease shot size, injection pressure, or speed; check clamp tonnage | Re-inspect for short shot / incomplete fill after adjustment |
| Both present in different areas of same part | Likely a mold venting or flow-balance issue, not a simple pressure adjustment | Consider tooling review (venting, gate balance) rather than further process chasing |

**Rule:** never consider a short-shot or flash fix complete until the opposite defect mode has been re-checked on the adjusted setting.

## First-article inspection checklist (new/changed tool)

1. Confirm process parameters set per the job's process sheet, not carried over from a prior job/tool.
2. Run first-article part(s); allow full cool-down before dimensional measurement (not immediately post-ejection).
3. Perform full dimensional inspection against print.
4. Perform visual inspection for short shot, flash, weld line appearance, surface defects.
5. For pressure-critical or structural applications: perform X-ray or equivalent internal inspection on first-article parts.
6. If any check fails, diagnose (process parameter vs. tooling) before re-running first article — do not proceed to production on a failed first article.
7. Document first-article results, including actual achieved process parameters, before releasing the tool/process combination for production quantity.
