# Red flags

### Resist pattern designed at the exact final desired feature dimension with no undercut compensation
- **Usually means:** the actual etched feature will be significantly wider or narrower than intended once undercut is accounted for, especially for fine detail.
- **First question:** what undercut allowance was actually built into the resist design versus the process's known undercut behavior at this depth?
- **Data to pull:** the resist opening dimension compared against the target final dimension and the expected undercut for this etch depth.

### Etch time set or stopped based on visual judgment during the process rather than calculated from a known etch rate
- **Usually means:** over- or under-etching, especially on a new material batch where etch rate may have shifted.
- **First question:** was etch time calculated from depth ÷ rate, and was a test coupon run to verify it?
- **Data to pull:** the calculated etch time compared against the actual time used, and whether a test coupon was run.

### Resist layer accepted as adequate without magnified inspection for pinholes, incomplete cure, or adhesion issues
- **Usually means:** unintended etching at defect locations that only becomes visible after the part is etched.
- **First question:** was the resist actually inspected under magnification before etching began?
- **Data to pull:** the resist inspection record compared against the standard magnified inspection requirement.

### Process parameters (etchant concentration/temperature, or laser power/speed/focus) reused on a new material batch without re-validation
- **Usually means:** the parameters may not produce the same etch rate or result on this specific batch's actual composition or finish.
- **First question:** was a test sample run on this batch before full production?
- **Data to pull:** the material batch/lot number compared against whether a test sample was run.

### A functional engraving (measurement scale, calibration mark) is inspected only for general legibility rather than its specific dimensional accuracy requirement
- **Usually means:** it may look fine but fail the actual functional tolerance it needs to meet.
- **First question:** what does the measured line width, depth, and spacing show against this specific engraving's functional requirement?
- **Data to pull:** measured line width/depth/spacing compared against the specific functional requirement for that engraving's use.

### Closely spaced fine detail lines etched without checking whether combined undercut from adjacent lines would cause them to merge
- **Usually means:** adjacent fine features may bridge together even if each individual line's undercut calculation looks acceptable in isolation.
- **First question:** what's the spacing between adjacent resist openings versus the combined undercut expected from both sides?
- **Data to pull:** spacing between adjacent resist openings compared against combined undercut from both sides.

### A recurring defect pattern (consistent undercut deviation, resist failure location) appears across multiple production runs without being traced to a specific cause
- **Usually means:** a systemic issue — bath concentration drift, resist application equipment — rather than isolated one-off defects.
- **First question:** does the defect occurrence log correlate with a specific process parameter trend over the same period?
- **Data to pull:** the defect occurrence log compared against process parameter logs over the same period.
