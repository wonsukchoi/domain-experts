### Offline-first architecture
An app design approach that treats local, on-device data as the primary source of truth for the user experience, syncing to a server when connectivity is available rather than requiring it for every action.
**In use:** "This app is offline-first — users can create and edit tasks with no connectivity, and changes sync when they're back online."
**Common misuse:** Building an app that assumes continuous connectivity, then bolting on offline support later without a real conflict resolution strategy for data edited both offline and elsewhere.

### Whole-record last-write-wins
A naive sync conflict resolution strategy where the most recently synced version of an entire record overwrites any prior version, regardless of which specific fields each version actually changed.
**In use:** "The whole-record last-write-wins approach is what silently dropped the title edit when the phone's due-date-only edit synced later."
**Common misuse:** Applying this strategy to records that are commonly edited on different fields by different clients, causing silent data loss on fields the later-syncing client never touched.

### Field-level merge
A sync conflict resolution strategy that tracks modification timestamps per field (rather than per record), allowing edits to different fields from different clients to merge without one overwriting the other.
**In use:** "Field-level merge preserved both the title and due-date edits since they touched different fields."
**Common misuse:** Assuming field-level merge alone resolves all conflicts, when two clients editing the exact same field still require an explicit conflict-resolution rule or user prompt.

### App store review
The review process both Apple's App Store and Google Play require before a new app version becomes available to users, which can take days and can result in rejection for specific policy violations.
**In use:** "This release includes a new payment flow, so we need extra review buffer given Apple's specific guidelines on that."
**Common misuse:** Treating app store review as a formality with predictable, instant turnaround, rather than a real scheduling risk that varies by platform, feature set, and current policy enforcement.

### Background execution limits
OS-enforced restrictions on how much processing an app can perform while not in the foreground, including iOS's background execution time limits and Android's Doze mode/battery optimization.
**In use:** "This background sync job needs to respect Android's Doze mode restrictions or it'll get silently deferred for hours."
**Common misuse:** Writing background/long-running code assuming it can run continuously, without accounting for the platform's actual, documented background execution constraints.

### App lifecycle
The sequence of states an app or screen passes through (foreground, background, suspended, terminated) and the callbacks a developer can hook into to save or restore state at each transition.
**In use:** "We need to save the in-progress form data at the 'will resign active' lifecycle callback, not assume the process stays alive."
**Common misuse:** Failing to handle a specific lifecycle transition (backgrounding, configuration change, process death) explicitly, causing state loss under conditions that don't appear during a quick, uninterrupted manual test.

### Configuration change (Android)
An event (most commonly device rotation) that can cause an Android activity to be destroyed and recreated, requiring explicit state preservation to avoid data loss.
**In use:** "Rotating the device mid-form triggered a configuration change that wiped the unsaved input, since state wasn't preserved across it."
**Common misuse:** Testing only in a fixed orientation, missing bugs that only manifest when a configuration change destroys and recreates the current screen.

### Device fragmentation
The wide variation in hardware, screen sizes, and OS versions across real-world devices (especially pronounced on Android), meaning a single test device doesn't represent the full range of conditions the app will actually run under.
**In use:** "This crash only happens on devices running an older OS API level — our test matrix didn't include that combination."
**Common misuse:** Testing exclusively on one high-end device or emulator, missing crashes or behavioral differences specific to older, lower-spec, or less common device/OS combinations.

### Conflict resolution UI
An explicit user-facing prompt asking the user to choose between conflicting versions of the same data, used when automatic merge rules aren't sufficient to resolve a genuine same-field conflict.
**In use:** "When both clients edit the due date differently, we show a conflict prompt letting the user pick which value to keep."
**Common misuse:** Silently applying an automatic rule (like last-write-wins) to a genuine same-field conflict without surfacing it to the user, when the conflict may need human judgment to resolve correctly.
