# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Vulnerability scan vs. penetration test

- **Definition:** a vulnerability scan is automated detection of known-signature issues (Nessus/Qualys/Burp against a CVE and misconfiguration database); a penetration test is a human simulating an adversary — manually verifying, chaining, and proving business impact, with scanning as one input among several.
- **Practitioner usage:** "The client bought a pentest but scoped 4 hours — that's a scan with a signature on it, not a pentest; there's no time in that budget to manually chain anything."
- **Common misuse:** using the terms interchangeably in a statement of work, which lets a vendor deliver an unverified scanner export and still invoice for a "penetration test."

## Rules of Engagement (RoE)

- **Definition:** the signed document defining exact scope, testing window, authorized test types, data-handling constraints, and emergency contacts for an engagement — the legal and operational boundary of the test.
- **Practitioner usage:** "That subdomain resolves to the same IP range, but it's not in the RoE's scope table — I'm emailing the client for a scope amendment before I touch it, not assuming it's covered."
- **Common misuse:** treating the RoE as boilerplate to sign quickly rather than the actual authorization boundary; testers who "go a little outside scope because it was obviously related" have no legal cover for that decision, RoE or not.

## CVSS base score vs. environmental score

- **Definition:** the base score reflects a vulnerability's intrinsic severity, environment-agnostic; the environmental score reweights it using the specific client's declared Confidentiality/Integrity/Availability Requirements (CR/IR/AR) for the affected asset.
- **Practitioner usage:** "Base score is 9.8, but this is an internal dev sandbox with synthetic data and CR/IR/AR all set to Low for this client — environmental comes out closer to 6."
- **Common misuse:** reporting the base score to executives as if it were the client-specific risk — the base score alone doesn't know whether the asset holds real financial data or throwaway test fixtures.

## False positive (scanner context)

- **Definition:** a scanner alert that doesn't reproduce under manual verification — the signature matched, but the underlying condition either doesn't exist or isn't exploitable as flagged.
- **Practitioner usage:** "62 flagged, 14 confirmed — a 77% false-positive rate this run, mostly the WAF's rate-limiting tripping the time-based blind-SQLi heuristic."
- **Common misuse:** treating a scanner's confidence label ("Critical") as equivalent to a human tester's confirmation; scanners don't know the difference between a real 3-second SQL delay and a WAF throttle producing the same timing signature.

## Red team vs. penetration test

- **Definition:** a penetration test is scoped to find and enumerate as many exploitable weaknesses as time allows within an agreed surface; a red team engagement is scoped to a specific objective (reach this data, avoid detection) and measures whether the target's detection and response worked, not just whether a hole exists.
- **Practitioner usage:** "This is a red team engagement, not a pentest — we're not reporting every vulnerability we see, we're reporting whether the SOC caught us reaching the objective, and how long it took."
- **Common misuse:** using "red team" as a fancier synonym for "pentest" in a proposal — the deliverables and success criteria are structurally different, and selling one as the other under-delivers whichever was actually purchased.

## Purple team

- **Definition:** a collaborative exercise where the offensive tester and the defensive (blue) team work together in real time, mapping each technique attempted to whether detection fired, to close instrumentation gaps rather than just prove exploitability.
- **Practitioner usage:** "We're running this as purple team — after each MITRE ATT&CK technique I run, the blue team confirms in Slack whether their SIEM alerted, so we fix detection gaps same-day instead of finding out from a report next month."
- **Common misuse:** calling any pentest with a debrief call "purple team" — the defining feature is real-time technique-by-technique detection feedback, not a closing meeting.

## Zero-day vs. n-day

- **Definition:** a zero-day is a vulnerability with no vendor patch available at time of use; an n-day is a vulnerability with a patch already published that the target simply hasn't applied yet.
- **Practitioner usage:** "This isn't a zero-day — it's a 90-day-old CVE with a patch the client's change-control process hasn't gotten to yet. That's a patch-cadence finding, not a novel-research one."
- **Common misuse:** calling any exploit that "wasn't publicly known to the client" a zero-day; the overwhelming majority of real-world compromises use n-days against unpatched systems, and conflating the two overstates the sophistication required.

## Proof of Concept (PoC) exploit

- **Definition:** the minimum working demonstration that a vulnerability is exploitable and what impact it produces — deliberately not weaponized beyond what's needed to prove and reproduce the finding.
- **Practitioner usage:** "The PoC reads one seeded test record to prove the injection works; I'm not writing the version that dumps the whole table, that's not what proving the finding requires."
- **Common misuse:** treating "no PoC" as acceptable evidence for a Critical finding, or conversely building a fully weaponized exploit when a single reproducible request would prove the same point with less risk to the target.

## Privilege escalation: vertical vs. horizontal

- **Definition:** vertical privilege escalation gains a higher permission level (user → admin); horizontal privilege escalation gains access to another account/resource at the same permission level (user A's data as user B).
- **Practitioner usage:** "This IDOR is horizontal — any authenticated user can read any other user's invoices by changing the ID parameter, no admin access needed."
- **Common misuse:** calling any unauthorized access "privilege escalation" — an IDOR that exposes peer data without gaining any new privilege level is horizontal, and conflating it with vertical escalation misstates what an attacker gains.

## Attack surface

- **Definition:** every point where an attacker could interact with a system — not just the URLs a client lists, but everything a crawl, DNS enumeration, and third-party dependency review actually discovers.
- **Practitioner usage:** "The client's scope doc lists 12 endpoints; the crawl found 47. That gap is the actual attack surface question for this engagement, and it's the first thing in the report."
- **Common misuse:** equating "attack surface" with "the list of pages in the sitemap" — undocumented, deprecated, or third-party-embedded endpoints are routinely a large fraction of what's actually reachable.

## Lateral movement

- **Definition:** the post-foothold process of moving from an initially compromised host to other systems in the network, typically to reach higher-value targets (domain controller, database server) than the entry point.
- **Practitioner usage:** "Foothold was a phished laptop; lateral movement via cached domain-admin credentials in LSASS got us to the DC in under two hours — that's the finding, not the phishing email itself."
- **Common misuse:** treating the initial foothold as the headline finding when the lateral-movement path to a crown-jewel system is what actually establishes business impact.

## Get-out-of-jail-free letter

- **Definition:** the client-signed authorization letter a tester carries (physically, for on-site engagements, or on file) proving the testing activity is authorized, protecting against computer-crime statutes that don't distinguish authorized testing from an actual attack by default.
- **Practitioner usage:** "Keep the letter on hand for the whole engagement window — if the client's own SOC or law enforcement flags the traffic, that's what stops this from becoming a real incident response."
- **Common misuse:** assuming a signed contract alone covers this — the letter needs to specifically address the testing activity and dates, not just a generic services agreement.

## Scope creep

- **Definition:** testing activity that extends beyond the RoE's defined boundary, whether from technical curiosity, an incorrectly assumed exclusion, or a target that "looked related."
- **Practitioner usage:** "That third-party-embedded iframe isn't ours to test even though it's on the same page — flagging it to the client as an out-of-scope observation, not testing it."
- **Common misuse:** rationalizing scope creep as thoroughness; it's a scope-change conversation with the client, not a unilateral judgment call by the tester.
