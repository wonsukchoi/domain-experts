# Red flags

### Reject rate exceeds the mail-type's 30-day baseline by more than 2 percentage points, even under the contractual ceiling
- **Usually means:** a print-quality issue concentrated in one mailer batch, or a genuine OCR/barcode-read drift.
- **First question:** does the spike concentrate in one mailer batch or permit number?
- **Data to pull:** reject sample pull grouped by mailer batch/permit.

### Jam frequency exceeds roughly 2 per hour sustained over a shift
- **Usually means:** feed-mechanism wear, or a batch of damaged/overstuffed mail pieces rather than a one-off.
- **First question:** are the jams clustering at the same machine station or component?
- **Data to pull:** jam error-code log broken out by machine station.

### REC keying queue backlog exceeds what the shift can clear
- **Usually means:** reject volume has outpaced downstream manual-keying capacity, risking delivery delay.
- **First question:** what's driving the elevated reject volume feeding the queue?
- **Data to pull:** REC queue depth trend versus its historical average.

### Mixed-class trays arrive at a single-class machine's induction point
- **Usually means:** a culling failure upstream, since letters and flats require physically different sorting equipment.
- **First question:** where in the culling process did class separation fail?
- **Data to pull:** culling station assignment log for the affected trays.

### Throughput runs below rated speed by more than 15% with low reject and jam counts
- **Usually means:** a calibration or speed-setting error, not a mail-quality problem.
- **First question:** what speed setting is the machine actually running at right now?
- **Data to pull:** machine speed/setting log compared against rated specification.

### Nonmachinable-surcharge volume rises with no change in size/rigidity acceptance policy
- **Usually means:** the acceptance unit is letting noncompliant mail through rather than a shift in mail composition.
- **First question:** where did this mail enter the system — retail counter or bulk acceptance?
- **Data to pull:** acceptance unit intake logs for the affected period.

### Same error code recurs on a specific machine more than a handful of times per week
- **Usually means:** a specific component needs preventive maintenance, not routine operator clearing.
- **First question:** how many times has this exact code appeared on this machine in the past 30 days?
- **Data to pull:** maintenance ticket history filtered by machine and error code.

### Operator overrides an OCR-suggested reject to force a piece through sortation
- **Usually means:** a well-intentioned override that risks a misdelivery if the underlying address confidence was genuinely low.
- **First question:** was the override logged, and does the piece's confidence score actually justify forcing it through?
- **Data to pull:** override log with the associated OCR confidence scores.
