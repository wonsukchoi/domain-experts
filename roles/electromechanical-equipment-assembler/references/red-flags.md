# Red flags

### A shaft coupling or mechanical interface assembled "by eye" without a direct alignment measurement
- **Usually means:** misalignment beyond spec could exist while still passing an initial functional (power-on) test.
- **First question:** has alignment been directly measured with a dial indicator or equivalent, or only confirmed by the device running?
- **Data to pull:** alignment measurement if performed, the interface's specified maximum misalignment.

### Fasteners tightened without a calibrated torque tool
- **Usually means:** either under-torque (vibration loosening risk) or over-torque (stripped threads/cracked housing risk) could be present undetected.
- **First question:** was a calibrated torque wrench/driver used to the specified value, or was tightening done "until it feels secure"?
- **Data to pull:** the fastener's torque specification, actual torque applied if measured.

### Wire routing verified only in the equipment's static, assembled-at-rest position
- **Usually means:** the routing may not account for the actual range of motion/vibration the equipment will experience in service.
- **First question:** has wire routing been checked through the equipment's full range of motion, or only its resting position?
- **Data to pull:** the equipment's range of motion specification, routing verification method used.

### A functional test limited to a single cold power-on check, with no break-in or thermal cycling test performed where specified
- **Usually means:** a marginal connection or component that only fails after thermal cycling wouldn't be caught.
- **First question:** does this equipment's test plan specify a break-in or thermal cycling test, and was it performed?
- **Data to pull:** the specified test plan, actual tests performed.

### A device malfunction diagnosed and "fixed" without distinguishing electrical from mechanical root cause
- **Usually means:** the actual root cause (which could be in either domain) may not have been correctly identified before a fix was attempted.
- **First question:** were both electrical (continuity, connections) and mechanical (alignment, binding) causes checked, or was one assumed without verification?
- **Data to pull:** the diagnostic steps taken, the specific fix applied and its rationale.

### A field failure occurring well after shipping, on equipment with rotating or moving mechanical components
- **Usually means:** possible accumulated damage from a misalignment or under-torque condition present since assembly but undetected by initial testing.
- **First question:** does the failure mode (bearing wear, vibration-related) suggest an alignment or torque issue from assembly?
- **Data to pull:** the failure mode/pattern, original assembly's alignment and torque verification records if available.

### A recurring field failure pattern correlating with a specific assembly line, shift, or technician
- **Usually means:** a systematic assembly practice issue (torque technique, alignment verification skipped) rather than random component variation.
- **First question:** does the failure pattern correlate with a specific assembly source, or does it appear randomly distributed?
- **Data to pull:** failure traceability data by assembly source, any process audit findings for that source.

### A wire showing insulation wear or damage at a point corresponding to the equipment's range of motion
- **Usually means:** routing didn't adequately account for motion/vibration exposure at that specific point.
- **First question:** does the wear location correspond to a flex point or contact point in the equipment's range of motion?
- **Data to pull:** wear location, equipment's motion range and routing path at that location.

### A torque specification applied uniformly across different fastener sizes/materials without checking each one's actual spec
- **Usually means:** different fasteners in the same assembly may have different torque requirements, and a single value applied to all may be wrong for some.
- **First question:** does each fastener type/size in this assembly have its own specified torque value, and was each applied correctly?
- **Data to pull:** the assembly's fastener specification list, torque values actually applied per fastener type.

### An assembly returned for rework with no re-verification of alignment/torque after the rework
- **Usually means:** the specific issue that prompted rework may have been addressed, but other parameters (alignment, torque) disturbed during rework weren't re-checked.
- **First question:** was full alignment/torque re-verification performed after rework, or only the specific reworked area addressed?
- **Data to pull:** rework record, post-rework verification results.
