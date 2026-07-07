# Red flags

Smells a journey-level sheet metal worker catches reviewing a shop drawing or a field install, before the next trade covers it up.

## 1. Gauge called out from shop stock, not the pressure-class/dimension table

**Usually means:** the fabricator matched what's already on the truck rather than looking up the SMACNA table for the actual longest dimension and pressure class — often invisible until the duct oil-cans in service or fails a hanger-load check.

**First question:** "What pressure class and longest dimension is this segment, and what table row does that put it in?"

**Data to pull:** the mechanical schedule's pressure class for that segment, actual fabricated dimensions, and the SMACNA gauge table row those two numbers land on.

## 2. Mid-project pressure-class change with no gauge/leakage re-check downstream

**Usually means:** late-added reheat coils, a fan upsize, or a VAV terminal box addition pushed a run from low- to medium-pressure, but the ductwork already fabricated or ordered downstream was sized to the original low-pressure spec.

**First question:** "Which duct segments are downstream of this change, and were any of them already fabricated to the old pressure class?"

**Data to pull:** revised mechanical schedule pressure classes by segment, fabrication/purchase order dates versus the design-change date, gauge and seal-class table lookups for the new pressure class.

## 3. Duct shown continuous through a fire-rated wall or floor line with no damper symbol

**Usually means:** the architectural life-safety plan and the mechanical duct routing were drawn independently and never reconciled — a coordination gap, not a deliberate exception, in the large majority of cases.

**First question:** "Is this wall/floor line rated on the life-safety plan, and if so, where's the damper?"

**Data to pull:** architectural life-safety plan rating for every wall/floor the duct run crosses, mechanical drawing damper schedule, any documented IBC 717 exception signed off by the code official.

## 4. Failed leakage test fixed by "add more mastic everywhere"

**Usually means:** the actual defect is an unsealed joint or seam type the specified seal class required, not an insufficient quantity of sealant — blanket re-sealing without diagnosis often fails the retest too.

**First question:** "Which joints and seams on this run are unsealed relative to the seal class (A/B/C) actually specified?"

**Data to pull:** the seal-class specification for the segment, a joint-by-joint sealing checklist against that spec, the leakage-test report showing where the failure margin sits relative to the CL formula's allowable F.

## 5. Transition or offset fitting built visibly steeper than practice (near 45° or more)

**Usually means:** the crew traded fitting length for turbulence and static-pressure loss to save material or fit a tight space, usually without flagging the pressure-drop consequence to whoever owns the fan's static-pressure budget.

**First question:** "What's the per-side angle on this fitting, and what run length would the ≤20°/15° guideline actually require here?"

**Data to pull:** as-built fitting dimensions and angle, available clear run in the field, whether the mechanical contractor's static-pressure budget for this run has any margin for the added loss.

## 6. Hanger spacing carried over from a smaller duct size

**Usually means:** the crew used a spacing habit from prior work rather than checking the table against this duct's actual perimeter and gauge — larger-perimeter duct sags or fails a support point under its own weight plus insulation.

**First question:** "What's this duct's perimeter, and what does the hanger table call for at that perimeter and gauge?"

**Data to pull:** actual duct perimeter and gauge, current hanger spacing as installed, SMACNA hanger-spacing table row for that perimeter.

## 7. Round-to-rectangular or other unlike-shape transition laid out "by eye"

**Usually means:** the fitting was cut without a triangulation pattern, producing an approximate rather than a true developed surface — visible as puckering, poor seam fit, or a fitting that doesn't sit flush at both ends.

**First question:** "Was this fitting laid out from a triangulated pattern, and can I see the pattern development?"

**Data to pull:** the shop pattern or CNC nesting file for the fitting, the fit-up at both connection points before final seaming.

## 8. Duct necked down through an obstruction "since CFM is unchanged"

**Usually means:** the fix solved the spatial clearance problem without checking the velocity increase, which raises friction rate roughly with velocity^1.9 and can push noise past NC targets near a downstream terminal.

**First question:** "What's the velocity through the necked section, and how close is it to the nearest diffuser or VAV inlet?"

**Data to pull:** original and post-fix cross-sectional area and velocity, distance to the nearest terminal device, the static-pressure budget margin for the run.

## 9. Fire damper installed with no accessible inspection/reset panel

**Usually means:** the damper itself was specified and installed correctly, but the access requirement (an inspection door sized and located per the damper's listing) was missed — a code and future-maintenance failure that's invisible until an inspector or a fire-alarm test finds it.

**First question:** "Where's the access panel for this damper, and is it sized to the listing's access requirement?"

**Data to pull:** the damper's UL listing access requirements, ceiling/wall access panel locations on the reflected ceiling plan, photos of the installed condition before ceiling close-up.

## 10. Combination fire/smoke damper location with only a fire-rated (non-smoke) damper installed

**Usually means:** the wall was correctly identified as fire-rated but its additional status as a smoke barrier was missed, so a UL 555 fire damper went in where UL 555S combination rating was required.

**First question:** "Is this wall also shown as a smoke barrier on the life-safety plan, not just fire-rated?"

**Data to pull:** the life-safety plan's smoke-barrier designations layered against fire-rating designations, the damper's actual listing versus the wall's full rating requirement.
