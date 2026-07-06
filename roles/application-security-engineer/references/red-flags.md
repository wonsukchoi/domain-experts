### An endpoint accessing a resource by ID checks authentication but not object-level authorization
- **Usually means:** This is a broken access control / IDOR vulnerability — any authenticated user can potentially access any other user's data by changing the ID.
- **First question:** Does this endpoint verify the authenticated user actually owns or has permission for the specific resource ID being requested, or only that they're logged in?
- **Data to pull:** Endpoint's authorization logic, a test request using a different user's credentials against another user's resource ID.

### A new feature or system design skips threat modeling and goes straight to implementation
- **Usually means:** Security flaws that would have been cheap to catch and fix at design time may instead surface in code review or, worse, in production.
- **First question:** Has a threat model (e.g., STRIDE) been run for this design before implementation began?
- **Data to pull:** Design documentation, existing threat model (or its absence).

### Security testing relies on only one tool type (only SAST, or only DAST, or only SCA)
- **Usually means:** A specific class of vulnerability the other tool types would catch is likely going undetected.
- **First question:** Which vulnerability classes does the current tooling combination actually cover, and which classes (business logic flaws, dependency vulnerabilities, runtime-only issues) are structurally outside its detection capability?
- **Data to pull:** Current security tooling stack, known coverage gaps for each tool type in use.

### A dependency vulnerability is prioritized purely by its CVSS score
- **Usually means:** Remediation effort may be misallocated if the vulnerable code path isn't actually reachable in this application, while a lower-scored but reachable vulnerability gets deprioritized.
- **First question:** Is the specific vulnerable function/code path actually called anywhere in this codebase?
- **Data to pull:** Reachability analysis for the flagged vulnerability, comparison against other flagged vulnerabilities' reachability status.

### User input is sanitized with a single generic function applied before storage, rather than context-specific encoding at each output
- **Usually means:** The same value can be safe in one output context (HTML) and still exploitable in another (JavaScript, SQL, URL) if encoding isn't applied specifically at each sink.
- **First question:** Is output encoding applied specifically at each output context (HTML, JS, SQL, URL), or is a single sanitization pass relied on universally?
- **Data to pull:** Input handling and output encoding logic for each context this data is rendered or used in.

### A security finding is reported with only a tool-generated severity label and no exploitability context
- **Usually means:** The reported severity may not reflect this application's actual risk without checking reachability and real-world exploitability.
- **First question:** Has this finding been validated for actual exploitability in this specific application, or is it being reported as-is from the scanning tool?
- **Data to pull:** Tool's raw finding, any manual reachability/exploitability validation performed.

### A code review for a feature touching user-owned data doesn't include a test using a different, lower-privileged account
- **Usually means:** The authorization boundary for this feature hasn't actually been tested — only the happy path for the intended user has been verified.
- **First question:** Has this feature been tested by attempting access as a different account than the one it was designed for?
- **Data to pull:** Test coverage for this feature's authorization logic, results of a cross-account access attempt.

### A threat model or security review was conducted once at launch and never revisited as the feature evolved
- **Usually means:** New attack surface introduced by subsequent changes may not have been assessed since the original review.
- **First question:** What has changed in this feature/system since its last threat model or security review, and has that change been separately assessed?
- **Data to pull:** Change history since the last security review, current threat model's last-updated date.
