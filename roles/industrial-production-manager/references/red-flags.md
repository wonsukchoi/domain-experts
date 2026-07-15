# Red flags — what a production manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A capacity investment proposed for the most visible or most recently problematic station without a bottleneck analysis
- **Usually means:** the fix may target the wrong station — improvement anywhere except the actual constraint doesn't increase total line output.
- **First question:** "What's each station's actual capacity, and where is WIP inventory piling up?"
- **Data to pull:** per-station capacity/throughput data, WIP inventory levels between each station pair.

### Work-in-progress inventory accumulating steadily in front of a specific station
- **Usually means:** that station is very likely the actual bottleneck — WIP piling up immediately upstream of a station is close to a direct signature of it being the system's limiting step.
- **First question:** "How fast is WIP growing in front of this station, and does its rated capacity match the line's actual total output?"
- **Data to pull:** WIP levels and growth trend by station, each station's rated capacity versus observed line output.

### A schedule-pressure decision that reduces a documented safety margin
- **Usually means:** safety is being treated as one negotiable factor among several rather than the categorical first filter it should be — the potential consequence isn't comparable to a throughput or cost tradeoff.
- **First question:** "Does this decision reduce a safety margin, and if so, why is it being weighed against schedule at all?"
- **Data to pull:** the specific safety protocol or margin in question, the schedule pressure driving the proposed change.

### Rising overtime hours or chronic understaffing sustained for multiple consecutive weeks with output holding steady
- **Usually means:** fatigue-driven defect and incident rate increases typically show up with a lag — steady output now doesn't mean the workforce capacity is actually sustainable.
- **First question:** "What's the overtime/understaffing trend over the last 6-8 weeks, and has defect or incident rate been checked against it with an appropriate lag?"
- **Data to pull:** overtime hours trend, defect rate and safety incident rate over the same period with a lagged comparison window.

### A quality defect being caught at final inspection or after shipment with no upstream detection point identified
- **Usually means:** quality control investment is weighted too late in the process — the same defect caught at its point of origin would have cost a fraction as much to address.
- **First question:** "Could this defect have been caught earlier in the process, and if so, why wasn't it?"
- **Data to pull:** the defect's point of creation versus point of detection, cost comparison between early and late detection for this defect type.

### A process improvement claimed with no documented standard work baseline to compare against
- **Usually means:** it's not possible to reliably distinguish a genuine improvement from normal process variation without a consistent baseline.
- **First question:** "What was the documented standard process before this change, and how is the 'improvement' being measured against it?"
- **Data to pull:** the standard work documentation (or its absence) for the process in question, the before/after data being used to claim improvement.

### Equipment or line performance reported on a single metric (speed) with no composite (OEE) view
- **Usually means:** an apparent improvement on one dimension (speed) may be masking a tradeoff on another (defect rate, uptime) that only a composite metric would reveal.
- **First question:** "What's this equipment's OEE (availability × performance × quality), not just its speed?"
- **Data to pull:** availability, performance, and quality rate components for the equipment/line in question.

### A recurring quality or safety incident addressed with a one-off fix rather than a documented root-cause analysis
- **Usually means:** the underlying systemic cause likely remains unaddressed, and the incident is likely to recur.
- **First question:** "Has a 5 Whys or fishbone analysis been done on this, or was it treated as a one-off to route around?"
- **Data to pull:** incident recurrence history, any documented root-cause analysis for this or a similar prior incident.
