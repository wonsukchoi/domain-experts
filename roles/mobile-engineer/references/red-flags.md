### A sync design overwrites an entire record based on which client synced most recently
- **Usually means:** Edits to unrelated fields from another client can be silently discarded, a data-loss bug that produces no error and is easy to miss in testing.
- **First question:** Does this record support field-level merge, or does any sync overwrite the whole record based on a single timestamp?
- **Data to pull:** Sync logic implementation, sample scenario with two clients editing different fields.

### A user reports "my change disappeared" with no crash or error
- **Usually means:** This is a classic symptom of a whole-record sync conflict overwrite, not a UI bug or user error.
- **First question:** Were there two clients (offline and online, or two devices) editing this same record around the same time?
- **Data to pull:** Edit timestamps from both clients involved, sync log for this record.

### A release is scheduled with no buffer for app store review turnaround
- **Usually means:** A launch date could be missed for reasons entirely unrelated to code readiness, since review can take days and rejection is possible.
- **First question:** Has the release timeline built in expected review turnaround time, and has the build been checked against current platform guidelines for any new feature (payments, permissions, data collection)?
- **Data to pull:** Current app store review guideline changes relevant to this release, historical review turnaround time for this app.

### Background work assumes continuous execution with no use of platform background task APIs
- **Usually means:** This work will likely be throttled or killed under real-world battery optimization (iOS background limits, Android Doze mode), even though it may work fine during active foreground testing.
- **First question:** Is this background work implemented using the platform's documented background task APIs, and has it been tested under battery-optimization conditions?
- **Data to pull:** Background work implementation, test results under Doze mode/background app refresh disabled.

### App state isn't explicitly saved at the correct lifecycle callback
- **Usually means:** Backgrounding, configuration changes (rotation), or process death could cause silent data loss or a crash under conditions a quick manual test won't trigger.
- **First question:** Has this specific lifecycle transition (backgrounding mid-task, rotation, process death) been tested directly, not just the happy path?
- **Data to pull:** Lifecycle callback implementation for this screen/feature, test results for the specific transition.

### Testing was conducted only on a single device or emulator
- **Usually means:** Real-world crashes or behavior differences on older devices, different OS versions, or different hardware configurations may not have been caught before release.
- **First question:** Has this feature been tested across a representative matrix of device types and OS versions, particularly for Android's fragmentation?
- **Data to pull:** Device/OS test matrix used, crash reports segmented by device/OS version post-release.

### A conflict resolution strategy treats "different fields edited independently" the same as "same field edited twice"
- **Usually means:** Genuine same-field conflicts may not be getting the explicit resolution (rule or user prompt) they need, while safe cross-field merges may be unnecessarily flagged as conflicts.
- **First question:** Does the sync logic distinguish between these two cases, or treat every conflicting sync event identically?
- **Data to pull:** Sync conflict resolution logic, specific field-level modification history for a flagged conflict case.

### Crash reporting isn't segmented by device model or OS version
- **Usually means:** A crash pattern specific to older devices or particular OS versions could be hidden within an aggregate crash rate that looks acceptable overall.
- **First question:** Does the crash reporting tool break down crash rate by device model and OS version, and has that breakdown been checked for concentration in specific segments?
- **Data to pull:** Crash reporting dashboard segmented by device/OS version.
