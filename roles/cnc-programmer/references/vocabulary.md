# Vocabulary

### Scallop height (cusp height)
The residual ridge height left between adjacent toolpath passes on a curved surface, calculable directly from tool radius and stepover.
**In use:** "Scallop height comes out to 0.0002" at a 0.020" stepover with this ball-nose radius — that's what the print requires, no more."
**Common misuse:** Picking stepover by feel ("small is safe") instead of calculating the actual resulting scallop height against the finish spec, which usually means either missing the spec or wasting cycle time over-finishing.

### Stepover
The lateral distance between adjacent toolpath passes.
**In use:** "Doubling the stepover from 0.010" to 0.020" still meets the finish spec and cuts the finish-pass count in half."
**Common misuse:** Treating a smaller stepover as always "safer," ignoring that unnecessarily small stepover directly and proportionally increases cycle time without improving finish beyond what the print requires.

### Post-processor
Software that translates generic CAM toolpath data into the specific G-code dialect and kinematics of a target machine control.
**In use:** "This program's never run on that machine's post — dry-run it before committing material."
**Common misuse:** Assuming any post-processor produces equivalent code for a given toolpath; a mismatched or outdated post-processor can generate G-code that's syntactically valid but wrong for that specific machine's kinematics.

### Cutter compensation (G41/G42)
A machine control feature that offsets the toolpath by a stored tool radius or diameter value, so the program itself doesn't need to encode the exact tool size.
**In use:** "Offset 12 needs updating — that insert's measuring 0.001" under nominal."
**Common misuse:** Assuming the compensation value entered at the machine automatically matches the actual physical tool, when it's only correct once someone has verified it against the tool's measured dimension.

### Adaptive / high-speed machining (HSM) toolpath
A roughing strategy that maintains constant tool engagement and chip load, rather than the full-width passes of traditional roughing.
**In use:** "Switched the roughing operation to adaptive — same material removal, but the tool's never fully buried like it was before."
**Common misuse:** Assuming any "roughing" toolpath strategy is interchangeable, missing that adaptive strategies specifically target consistent tool load to allow safely higher feed rates that a conventional roughing pass couldn't sustain.

### Dry run / air cut
Running a program on the actual machine with the tool held above the material, or at a safe clearance height, to verify motion before cutting real stock.
**In use:** "Air-cut the whole program first — this post-processor's never been validated on this control."
**Common misuse:** Treating CAM software simulation as equivalent to a machine dry run; simulation doesn't catch machine-specific post-processor errors or control quirks that only surface on the actual hardware.

### Datum (setup reference)
The physical reference surface or feature a machine's coordinate system is zeroed against for a given operation or setup.
**In use:** "Both setups index off the same locating pin — that's what keeps the two operations in agreement."
**Common misuse:** Assuming each setup's datum choice is independent of the others, when inconsistent datums across setups on the same part let positional error stack invisibly between operations.

### Feed rate override
A machine control feature letting an operator scale the programmed feed rate up or down in real time during a cut.
**In use:** "Check the override dial before blaming the program — it's been running at 150% all shift."
**Common misuse:** Assuming the programmed feed rate is always exactly what's cutting, ignoring that an operator's override setting can silently change actual cutting conditions from what was originally programmed.

### Tool offset / tool length compensation
Stored values telling the machine control the actual length and diameter of a specific tool held in a specific position.
**In use:** "Tool 12's offset table entry needs updating to match the insert's actual measured length after the last change."
**Common misuse:** Confusing the tool offset number (its position in the tool changer or table) with the physical dimension values stored under that number — updating the wrong one leaves the actual tool geometry unchanged.

### Rest machining
A toolpath strategy that removes only the material left behind by a previous, larger tool, rather than recutting the entire surface.
**In use:** "Program the finish pass as rest machining off the roughing tool's leftover stock — no need to recut the whole surface."
**Common misuse:** Programming a finishing toolpath across an entire surface with a small tool when rest machining — targeting only the leftover stock from the prior operation — would cut the cycle time significantly.
