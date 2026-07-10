# Red flags

### Chip color shifts to blue or purple on steel mid-cut
- **Usually means:** excessive heat from a speed/feed setting that's too aggressive, or a dulling tool.
- **First question:** did the color shift gradually across the cut, or suddenly at one point?
- **Data to pull:** current speed/feed setting against the catalog chart, and the tool's change/wear log.

### First article passes 9 of 10 dimensions but fails one repeatedly
- **Usually means:** a fixture or datum setup error specific to that dimension, not general tool wear.
- **First question:** which datum does the failing dimension actually reference?
- **Data to pull:** fixture offset log and the work coordinate system's zero setting for this setup.

### Tight-tolerance part (±0.001" or tighter) measures differently warm versus after cooling
- **Usually means:** thermal expansion not accounted for in the measurement or machining process.
- **First question:** what was the part's actual temperature at the time of measurement versus the reference temperature the spec assumes (commonly 68°F/20°C)?
- **Data to pull:** shop floor temperature log and part temperature at time of measurement.

### Same tool and parameters carried from roughing straight into the finishing pass
- **Usually means:** elevated risk to finish quality and dimensional accuracy from roughing-level chip load in a finish operation.
- **First question:** was the feed rate and depth of cut actually reduced for the finishing pass?
- **Data to pull:** the program's parameter listing broken out by pass.

### Required clearance between mating parts from independent setups is under roughly 0.005"
- **Usually means:** an unverified tolerance stack-up risk across the full dimension chain.
- **First question:** has a stack-up calculation actually been run for this assembly, or is it assumed to work from nominal dimensions?
- **Data to pull:** the tolerance stack-up worksheet, if one exists.

### Nonconforming part dispositioned "use as is" with no engineering sign-off
- **Usually means:** someone accepting a risk they aren't authorized to accept on their own.
- **First question:** whose approval is required for this specific nonconformance category?
- **Data to pull:** the nonconformance report's approval chain.

### Tool run significantly past its rated tool life (e.g. over 150% of catalog life) with no inspection
- **Usually means:** elevated risk of unexpected tool failure mid-cut, or dimensional drift that hasn't been caught yet.
- **First question:** what does the tool's actual usage log show against the catalog's rated life?
- **Data to pull:** the tool usage log compared to the manufacturer's rated tool life for that material and operation.
