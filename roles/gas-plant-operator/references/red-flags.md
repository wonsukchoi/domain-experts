# Red flags

### Flow increase on a section with no corresponding weather or scheduled-demand explanation
- **Usually means:** an active leak rather than genuine demand growth.
- **First question:** does current weather (temperature) or a known industrial customer schedule explain the magnitude and timing of the change?
- **Data to pull:** weather-normalized historical demand for this section, industrial customer scheduling log, current SCADA flow/pressure trend.

### Section pressure dropping while flow rises
- **Usually means:** product is leaving the system somewhere other than through metered delivery — a leak signature.
- **First question:** is the pressure drop isolated to one section, or system-wide (which would point to a different cause, like a compressor issue)?
- **Data to pull:** section-by-section pressure trend, compressor station operating status.

### System pressure trending toward MAOP without an active operational reason
- **Usually means:** a control setpoint drift or a downstream restriction (a partially closed valve, an equipment fault) rather than intentional throughput increase.
- **First question:** was this pressure increase a deliberate setpoint change, or has it drifted without an operator action?
- **Data to pull:** setpoint change log, SCADA pressure trend, any recent equipment alarms downstream.

### Odorant concentration verified only at the plant injection point, not at distribution system extremities
- **Usually means:** the monitoring plan hasn't accounted for odor fade over distance, leaving uncertainty about detectability at the far end of the system.
- **First question:** when was odorant concentration last verified at the farthest monitored point in the distribution system?
- **Data to pull:** multi-point odorant monitoring log, distance/pipe material data relevant to fade characteristics.

### A public odor complaint dismissed without a field investigation
- **Usually means:** the complaint was assumed to be normal background odorant without verification.
- **First question:** has a crew physically confirmed gas concentration at the reported location using a combustible gas detector?
- **Data to pull:** complaint log with location and time, crew dispatch and field-reading record.

### Moisture/dew point reading compared against a generic threshold rather than this system's actual operating pressure
- **Usually means:** the hydrate-formation risk assessment doesn't reflect the system's real operating conditions.
- **First question:** what is the actual line pressure and temperature at the point this moisture reading was taken?
- **Data to pull:** moisture/dew point reading, actual line pressure and temperature at that point, hydrate formation curve for those conditions.

### H2S or other gas quality reading approaching its spec limit
- **Usually means:** a change in source gas composition (a new well, a blending change) rather than an instrument drift, though both are possible.
- **First question:** has the source gas mix changed recently, or does the instrument's calibration need verification?
- **Data to pull:** gas chromatograph readings over recent history, source/blending changes, instrument calibration log.

### A proposed procedure deviation for a PSM-covered process, justified as reasonable in the moment
- **Usually means:** a real operational need, but one that requires review against the facility's hazard analysis before proceeding.
- **First question:** has this deviation been routed through management of change (MOC), or is it being executed without that review?
- **Data to pull:** the documented procedure, the facility's MOC log for this or similar deviations.

### A compressor or regulator setpoint adjusted in direct response to a pressure anomaly, without a leak check first
- **Usually means:** the anomaly's cause wasn't confirmed before a corrective action was taken, risking a masked or worsened leak.
- **First question:** was a leak investigated and ruled out before the setpoint was adjusted?
- **Data to pull:** the sequence of actions taken (setpoint change timestamp vs. leak investigation timestamp), leak survey results if performed.

### Repeated small pressure/flow anomalies at the same section over multiple shifts
- **Usually means:** a slow, developing leak or a recurring equipment issue rather than independent, unrelated events.
- **First question:** do the anomalies at this section share a consistent pattern (timing, magnitude, location) across shifts?
- **Data to pull:** historical anomaly log for this section, any prior leak survey or inspection results.
