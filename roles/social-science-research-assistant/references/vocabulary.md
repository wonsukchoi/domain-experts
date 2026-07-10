# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Inter-rater reliability vs raw agreement

- **Definition:** raw percent agreement is just the fraction of items two coders scored the same; inter-rater reliability (Cohen's kappa, Krippendorff's alpha) corrects for the agreement expected by chance given the category base rates.
- **Practitioner usage:** "We're at 75% raw agreement, but kappa is only 0.52 because with 12 unevenly-sized categories, chance agreement alone is already close to 50%."
- **Common misuse:** reporting raw percent agreement as "reliability." With enough categories or a skewed base rate, raw agreement can look reassuring while the chance-corrected statistic is mediocre — the whole point of kappa/alpha is to strip out the part of agreement that's just chance.

## Exempt (IRB) vs no oversight

- **Definition:** "exempt" is a formal IRB determination that a specific protocol category (per 45 CFR 46.104) doesn't require full board review — it is still a determination the IRB makes, not a status the researcher declares.
- **Practitioner usage:** "This survey is minimal-risk and anonymous, so it's likely exempt category 2 — but I still need the IRB to make that call before we start recruiting."
- **Common misuse:** treating "exempt" as "no submission needed." Self-certifying exemption without an IRB determination on file is itself a compliance problem at almost every US institution, even when the underlying research really would have qualified.

## De-identified vs anonymized

- **Definition:** de-identified data has had direct identifiers removed but a key or crosswalk may still exist somewhere that could re-link it to a person; anonymized data has no key anywhere — the link is permanently severed.
- **Practitioner usage:** "This export is de-identified, not anonymized — the study-ID crosswalk still lives with the PI so we can send follow-up wave 2 invites."
- **Common misuse:** calling a spreadsheet "anonymized" because the name column was deleted, when a linked ID system elsewhere in the lab can still re-associate every row with a real person.

## Protocol deviation vs protocol violation

- **Definition:** a deviation is an unintended, generally minor departure from the approved protocol (a missed signature line, a slightly reworded reminder email); a violation is willful, or serious enough to affect participant rights, safety, or data integrity.
- **Practitioner usage:** "That's a deviation — report it within the standard window and note the corrective action. If it turns out someone skipped consent entirely, that's a violation and needs to go up immediately."
- **Common misuse:** using the terms interchangeably, which matters because the reporting timeline and severity classification differ — downgrading a violation to a "deviation" to make the paperwork lighter is itself a compliance problem.

## Convenience sample vs probability sample

- **Definition:** a convenience sample is whoever was reachable and willing (a subject pool, a social-media call for participants); a probability sample is drawn so every member of the target population has a known, nonzero chance of selection.
- **Practitioner usage:** "This is a convenience sample from the intro-psych subject pool — we can describe the effect within this sample, but we can't claim it generalizes to the broader population without a probability-based replication."
- **Common misuse:** presenting findings from a convenience sample (very common in lab research) with population-level generalization language ("Americans believe...") that the sampling method can't support.

## Attrition vs non-response

- **Definition:** attrition is participants who enrolled and then dropped out before a later wave or timepoint; non-response is people who were invited but never responded or enrolled at all.
- **Practitioner usage:** "Non-response at recruitment was 40%, typical for this channel; attrition after wave 1 is the number I'm actually worried about, since that's people we already have baseline data on."
- **Common misuse:** blending the two into one "dropout rate," which hides whether the problem is getting people in the door or keeping them through the study — the fixes for each are different (channel/incentive vs. burden/retention).

## Systematic review vs literature review

- **Definition:** a systematic review follows a documented, replicable search-and-screening protocol (search strings, databases, inclusion/exclusion criteria, a PRISMA-style flow of hit counts at each stage); a literature review or narrative review is a curated synthesis without that documented, reproducible pipeline.
- **Practitioner usage:** "This is a narrative background review for the intro, not a systematic one — I picked the most-cited and most-relevant papers, I didn't run a documented search protocol."
- **Common misuse:** calling any literature summary "systematic" without the documented search strategy behind it — reviewers and methods sections will ask for the search log, and there isn't one.

## Double data entry

- **Definition:** two people independently enter the same source data into separate files, then the files are diffed to catch transcription errors — as opposed to single entry with a spot-check of a small percentage.
- **Practitioner usage:** "Paper surveys always get double-entered here; the discrepancy rate tells us whether the form itself is confusing, not just whether one person made a typo."
- **Common misuse:** treating single-entry-plus-spot-check as equivalent quality control — a spot-check only catches errors in the rows it happens to sample, while double entry catches every discrepancy in the whole batch.

## Certificate of Confidentiality

- **Definition:** a US federal protection (NIH-issued for federally funded research, extendable to non-federal studies collecting identifiable sensitive information) that lets researchers refuse to disclose identifiable research data even under a subpoena.
- **Practitioner usage:** "We have a Certificate of Confidentiality on this substance-use study, so if there's ever a legal demand for identifiable data, we're protected from being compelled to hand it over."
- **Common misuse:** assuming it grants blanket data-sharing immunity or protects against mandatory-reporting obligations (child abuse, imminent harm) — it specifically covers compelled legal disclosure of identifiable research data, not every disclosure scenario.

## Coder drift

- **Definition:** the gradual, usually unconscious shift in how a coder applies category definitions over the course of a long coding project, even after passing an initial reliability check.
- **Practitioner usage:** "We passed IRR at the start, but I want a mid-project spot-check — six weeks in, drift is common even with a codebook everyone agreed on."
- **Common misuse:** treating a reliability check passed at the start of coding as valid for the entire project. A single pilot check certifies the codebook and the coders' initial calibration, not their calibration eight weeks and 400 items later.

## Master crosswalk / key file

- **Definition:** the single file linking study ID codes back to participant identities, kept separate from response data and access-restricted.
- **Practitioner usage:** "Only the PI and I have access to the crosswalk — everyone else on the team works with study-ID-only data."
- **Common misuse:** treating the crosswalk as just another lab file backed up wherever convenient, rather than the single highest-sensitivity document in the study, requiring its own restricted storage and access log.
