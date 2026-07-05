# Information security analyst working vocabulary

Terms an infosec analyst uses precisely and a generalist often blurs together. Format: definition → how a practitioner says it → common misuse.

**MTTD vs. MTTR** — Mean Time to Detect measures initial compromise to detection; Mean Time to Respond/Remediate measures detection to containment (or full eradication, depending on the org's definition — state which). They measure different halves of the same incident and don't average into one number.
In use: "MTTD was 16 hours here — the detection rule existed and even fired, it was just routed to log-only. MTTR from actual detection was under 5."
Misuse: quoting a single blended "response time" that hides whether the problem was detection speed or containment speed — the fix is different for each.

**IOC vs. IOA** — An Indicator of Compromise is evidence something already happened (a known-bad hash, a malicious IP in logs). An Indicator of Attack is behavioral evidence something is happening now, independent of whether the specific tool/hash has ever been seen before.
In use: "We don't have an IOC match on this binary — it's unsigned and unknown — but the IOA is clear: LSASS access from a process that's never touched it before."
Misuse: relying only on IOC matching (known-bad lists) and treating a "no match" result as "clean," which misses any novel or living-off-the-land tooling by design.

**CVSS base, temporal, and environmental score** — Base score reflects the vulnerability's inherent, unchanging severity (exploitability + impact). Temporal score adjusts for real-world factors like exploit maturity and patch availability. Environmental score adjusts for the specific asset's exposure and criticality in your environment. Public CVSS numbers are almost always base score only.
In use: "The published CVSS is 10.0 base — but on our environmental score it's still a 10, because it's internet-facing and Tier-0-adjacent, not a case where exposure would pull it down."
Misuse: treating the published base score as the final, environment-aware priority number without adjusting for whether the asset is actually exposed the way the base score assumes.

**Dwell time** — The elapsed time an attacker has access to an environment before detection, from initial compromise to containment. The single strongest predictor of how much damage an intrusion does.
In use: "Dwell time here was just over 16 hours — that's the number that matters for blast-radius review, not which alert eventually caught it."
Misuse: conflating dwell time with MTTD when the org's IR process has a gap between "detected" and "contained" — dwell time properly runs until containment, not until the first analyst notices.

**Blast radius** — The full set of accounts, hosts, and data actually reached or plausibly reachable by a compromised credential or host, established by evidence (telemetry review), not by the initial alert's scope.
In use: "Blast radius is three hosts confirmed by EDR telemetry, plus the DC exploitation attempt that didn't complete — not just the one mailbox that got the phishing click."
Misuse: reporting blast radius as "the host that alerted" without doing the reachability analysis on that host's or account's actual access.

**Lateral movement** — An attacker moving from an initially compromised host or account to additional systems within the same environment, typically via legitimate admin protocols (SMB, RDP, WinRM) rather than new exploits, which is why it often evades tools looking only for malware.
In use: "This wasn't a new exploit on hosts two and three — it was lateral movement via SMB using the admin credential harvested off host one."
Misuse: assuming lateral movement requires malware or a new vulnerability on each hop; the defining feature is reuse of legitimate access, which is exactly what makes it hard to catch with signature-based tools.

**Living-off-the-land binaries (LOLBins)** — Legitimate, pre-installed OS tools (PowerShell, PsExec, WMI, certutil) repurposed for malicious activity, which evade detection strategies built around flagging known-bad executables.
In use: "No malware dropped anywhere in this chain — it's all PsExec and native Windows tooling, which is why signature-based AV never fired."
Misuse: treating "no malware found" as "nothing malicious happened" — a LOLBins-based intrusion can be more dangerous precisely because it leaves no novel binary to flag.

**Zero trust** — An architecture principle: no user, device, or service is trusted by default based on network location; every request is authenticated and authorized per-session regardless of whether it originates inside or outside the perimeter.
In use: "Moving to per-session service-to-service auth is the zero-trust change that matters here — relabeling the VLAN diagram isn't."
Misuse: using "zero trust" as a marketing label for a network segmentation project that doesn't change any actual authentication behavior between segments.

**Least privilege vs. just-in-time (JIT) access** — Least privilege means an account holds only the permissions it needs for its role, standing. JIT access means even those permissions are granted only for the duration of the specific task, then automatically revoked.
In use: "Least privilege gets this account off the Domain Admins group entirely; JIT would let it request elevated access for a maintenance window and lose it automatically after."
Misuse: implementing least-privilege role scoping and calling the access-control problem solved, while leaving standing (always-on) privileged access that a compromised credential can use at any hour, not just during an approved task window.

**Push bombing / MFA fatigue** — Attacking a target who has valid MFA by repeatedly triggering push-based approval prompts, betting the user eventually accepts one out of annoyance or confusion about which is legitimate.
In use: "The clerk got 11 prompts in 6 minutes and approved the 12th — that's push bombing, not a training failure on her part."
Misuse: framing a push-bombing incident as user error correctable with more training, when the actual fix is protocol-level (number-matching, FIDO2/WebAuthn) since the technique defeats attentive and inattentive users about equally once the prompt count is high enough.

**Tier-0 asset** — A system whose compromise grants control over the broader identity/trust infrastructure (domain controllers, certificate authorities, identity federation servers) — compromising it is equivalent to compromising everything that trusts it.
In use: "This print server is low-value on its own, but it's on the same segment as a Tier-0 domain controller, so its patch SLA gets treated like a Tier-0-adjacent asset, not a print server."
Misuse: scoring an asset's priority purely on its own data sensitivity while ignoring its network adjacency to Tier-0 infrastructure, which is often the more important factor in lateral-movement risk.

**Containment vs. eradication vs. recovery** — Containment stops the intrusion from spreading further (isolate, disable, kill session). Eradication removes the root cause (patch the vulnerability, rotate every touched credential). Recovery returns systems to production on verified-clean evidence. They are sequential and each has its own exit criteria — none of them is "done" just because the next one has started.
In use: "We're contained as of 04:05, but eradication isn't closed until every credential the account touched is rotated, not just the one that got the initial alert."
Misuse: treating containment as if it closes the incident — declaring victory once the obvious host is isolated without completing eradication or verifying recovery.

**Detection engineering** — The discipline of writing, tuning, and retiring detection rules based on measured false-positive/true-positive yield against named techniques, rather than accumulating rules indefinitely.
In use: "Detection engineering here means retuning the impossible-travel rule's velocity threshold, not just adding a new rule on top of one that already wasn't working."
Misuse: treating "we have a detection rule for X" as equivalent to "X is covered," without ever measuring or revisiting that rule's actual signal quality.
