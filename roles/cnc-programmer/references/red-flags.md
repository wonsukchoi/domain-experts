# Red flags

### CAM simulation looks clean but the program hasn't been dry-run on the actual target machine
- **Usually means:** an unvalidated post-processor/machine combination could produce incorrect G-code the simulation never modeled — wrong rotary axis direction, unexpected feed-override behavior.
- **First question:** has this specific post-processor and machine combination been validated before on a similar part?
- **Data to pull:** the post-processor validation or change log for this machine.

### Finish-pass stepover set well below what the finish spec actually requires (e.g. resulting scallop height under half the allowed maximum)
- **Usually means:** stepover was picked by habit or feel rather than calculated against the actual finish target, adding unnecessary cycle time.
- **First question:** was this stepover calculated against a specific scallop-height target, or defaulted from a prior job?
- **Data to pull:** the program parameter sheet and the part's finish spec.

### Multiple setups on the same part don't share a common physical datum
- **Usually means:** positional error will stack invisibly between setups rather than referencing a consistent zero.
- **First question:** what datum is each setup actually indicating or zeroing off of?
- **Data to pull:** the setup sheet's datum reference for each operation.

### Cutter compensation offset entered at the machine doesn't match the tool's actual measured diameter
- **Usually means:** the part will come out oversized or undersized by exactly the discrepancy between the entered offset and the real tool.
- **First question:** was the offset entered from a measured value, or an assumed catalog nominal?
- **Data to pull:** the tool measurement log compared against the offset table entry.

### Post-processor was recently updated, or the program is running on a machine it wasn't originally posted for
- **Usually means:** untested G-code behavior — feed override handling, rapid move sequencing — that hasn't been validated on this specific control.
- **First question:** what changed in the post-processor or machine control software since this program last ran successfully?
- **Data to pull:** the post-processor version history and the machine control's software version.

### Program cycle time increases significantly (e.g. over 20%) after what looks like a minor parameter tweak
- **Usually means:** an unintended cascading interaction — a stepover reduction propagating through multiple finish passes — rather than the intended small change.
- **First question:** which specific parameter changed, and does it affect more than one operation in the program?
- **Data to pull:** before/after cycle-time estimates and the specific parameter that was edited.

### Toolpath programmed without checking fixture/clamp clearance at every tool orientation used
- **Usually means:** a geometrically valid toolpath on screen that collides with the actual workholding on the machine.
- **First question:** was clearance verified at every tool angle and orientation in the program, not just the nominal one?
- **Data to pull:** the fixture CAD model overlaid with the full toolpath envelope.
