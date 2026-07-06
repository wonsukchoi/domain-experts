### IDOR (Insecure Direct Object Reference)
A vulnerability where an application exposes a direct reference to an internal resource (like a database ID) without verifying the requesting user is authorized to access that specific resource.
**In use:** "Changing the invoice_id in the URL let us pull any customer's invoice — that's a textbook IDOR."
**Common misuse:** Confirming an endpoint requires authentication and assuming that's sufficient, without checking whether it separately verifies the authenticated user's authorization for the specific resource requested.

### Broken access control
The OWASP Top 10 category covering failures to properly enforce what an authenticated user is allowed to do or access, including IDOR, privilege escalation, and missing function-level authorization checks.
**In use:** "Broken access control is consistently the top-ranked OWASP vulnerability category, and this finding is a clear example of it."
**Common misuse:** Treating authentication checks as equivalent to access control, when access control specifically requires verifying authorization for the exact resource or action being requested.

### Threat modeling (STRIDE)
A structured design-time process for identifying potential security threats to a system, commonly using the STRIDE framework (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).
**In use:** "STRIDE analysis at design time flagged that this new API lacked a plan for preventing spoofed requests."
**Common misuse:** Deferring all security consideration to a post-implementation code review or scan, missing the much cheaper opportunity to catch design-level flaws before code is written.

### SAST (Static Application Security Testing)
A security testing method that analyzes source code without executing it, identifying code patterns associated with known vulnerability classes.
**In use:** "SAST flagged a potential SQL injection pattern in this query-building function."
**Common misuse:** Relying on SAST alone, missing runtime and business-logic vulnerabilities it structurally can't detect from static code analysis, and dealing with its characteristically high false-positive rate without additional validation.

### DAST (Dynamic Application Security Testing)
A security testing method that tests a running application by sending it requests and observing its behavior, catching vulnerabilities that only manifest at runtime.
**In use:** "DAST caught a reflected XSS vulnerability that SAST missed because it only shows up when the input actually renders in the browser."
**Common misuse:** Relying on DAST alone, missing vulnerabilities in code paths the test's specific crawl or scan didn't happen to exercise.

### SCA (Software Composition Analysis)
A security testing method that identifies known vulnerabilities in third-party dependencies and open-source libraries used by an application.
**In use:** "SCA flagged a critical vulnerability in one of our dependencies — now we need to check if the vulnerable function is actually reachable."
**Common misuse:** Treating an SCA finding's severity score as the final word on remediation priority, without checking whether the vulnerable code path is actually used in this application.

### CVSS (Common Vulnerability Scoring System)
A standardized scoring system rating a vulnerability's severity based on factors like exploitability and impact, producing a score generally interpreted as low/medium/high/critical.
**In use:** "This is a CVSS 9.8, but that score doesn't account for whether the vulnerable code is actually reachable in our specific application."
**Common misuse:** Prioritizing remediation purely by CVSS score without adjusting for actual reachability and exploitability in this specific codebase, which can materially change the real risk.

### Reachability analysis (dependency vulnerabilities)
The process of determining whether a vulnerable function or code path in a dependency is actually called anywhere in the application's own code, as opposed to simply being present in the dependency.
**In use:** "Reachability analysis showed the vulnerable deserialization method is never called — we only use this library's basic parse function."
**Common misuse:** Treating the mere presence of a vulnerable dependency as equivalent to real exposure, without checking whether the application's code path actually exercises the vulnerable function.

### Context-specific output encoding
The practice of encoding untrusted data differently depending on where it's being output (HTML, JavaScript, SQL query, URL), since each context has different characters and rules that make data "safe."
**In use:** "This value is HTML-escaped for the page body, but it also gets inserted into an inline script tag, which needs JavaScript-specific encoding too."
**Common misuse:** Applying a single generic sanitization function to all output regardless of context, leaving gaps where a different context (like JavaScript or SQL) requires different encoding than the one applied.

### Secure code review
A code review process specifically focused on identifying security vulnerabilities (access control, injection, insecure data handling) rather than general code quality or style.
**In use:** "This secure code review specifically checked for object-level authorization on every endpoint that accepts a resource ID."
**Common misuse:** Treating a general code review as sufficient for security purposes, without specifically checking for the vulnerability classes most relevant to the feature being reviewed.
