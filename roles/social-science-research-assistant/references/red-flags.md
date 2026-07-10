# Red Flags

Smell tests for coding, IRB compliance, and data handling. Format per flag: what it usually means, the first question to ask, the check to run.

## Inter-rater reliability computed on a hand-picked subsample

- **Usually means:** the subsample was chosen from items the coders already discussed or from early, easier-to-code responses — not drawn randomly, so the reliability number doesn't represent the harder cases still to come.
- **First question:** "How was the subsample selected — random draw from the full dataset, or the first N items, or ones we'd already looked at together?"
- **Data to pull:** the sampling script or manual selection log; re-draw a genuinely random subsample if the original wasn't, and recompute before trusting the number.

## Kappa or alpha below the pre-registered threshold, but coding continued anyway

- **Usually means:** deadline pressure won over the checkpoint. The whole batch coded after the failed check is now unreliable, not just the disputed items.
- **First question:** "What was the pre-registered threshold, and who decided to proceed despite the pilot missing it?"
- **Data to pull:** the confusion matrix from the pilot subsample to find which category pairs drove the disagreements; stop further coding until the codebook is revised and a fresh pilot clears the bar.

## Recruitment or consent wording that deviates from the approved script

- **Usually means:** someone improvised — "clarified" a confusing line, added a sentence for context, or trimmed the script to save time in a rushed session.
- **First question:** "Is this exact wording what's in the approved IRB protocol on file?"
- **Data to pull:** the approved recruitment/consent document from the IRB system; if the wording differs, this is a protocol deviation and needs to be logged and reported per the institution's timeline, not just corrected going forward.

## No-show or attrition rate running well above the recruitment plan's assumption

- **Usually means:** the incentive is miscalibrated, the recruitment channel is underperforming, or the study burden (length, number of waves) is higher than participants tolerate — not usually a one-off unlucky week.
- **First question:** "What was the planned rate, what's the actual rate over the last two weeks, and how much of the funded window is left?"
- **Data to pull:** enrollment and attrition logs by week and by recruitment channel; flag to the PI while there's still runway to adjust incentive, channel, or timeline.

## A "de-identified" dataset still carries a re-identification path

- **Usually means:** direct identifiers (name, email) were dropped, but indirect ones (zip code, birthdate, a rare demographic combination, verbatim quotes long enough to be searchable) remain and can re-identify in combination.
- **First question:** "Which variables in this file, combined, could narrow down to one person?"
- **Data to pull:** the full variable list against the de-identification checklist; coarsen or drop the offending combination before the file leaves the lab.

## Continuing review or annual IRB renewal date has passed with data collection still active

- **Usually means:** the renewal wasn't tracked against the protocol's actual expiration, or a submission was filed late and is still pending.
- **First question:** "What's the current approval expiration date, and is a new enrollment happening after it?"
- **Data to pull:** the IRB system's approval status page; halt new enrollment and new data collection immediately if lapsed — data already collected under a valid approval doesn't need to be discarded, but nothing new can be collected until reapproved.

## Codebook with no version history despite weeks of active coding

- **Usually means:** ambiguous-case decisions were made verbally and never logged, so the coding rules in a coder's head have quietly diverged from what's on paper.
- **First question:** "When was the codebook last updated, and can you point to the log entry for the last edge-case decision made?"
- **Data to pull:** the codebook's revision history; if there isn't one, treat the current data as suspect and run a fresh reliability check on a random subsample before trusting anything coded since the last known-good version.

## A "systematic" literature review with no documented search strategy

- **Usually means:** the label is aspirational — the actual process was ad hoc browsing that can't be reproduced or defended in a methods section.
- **First question:** "What were the exact search strings, databases, and date range used, and can I see the hit counts at each screening stage?"
- **Data to pull:** the search log; if none exists, either reconstruct and document it before calling it systematic, or relabel it as a narrative/scoping review, which has a lower bar.

## Incentive payment records stored in the same file as survey responses

- **Usually means:** convenience during data collection — it was easier to add a mailing-address column to the response spreadsheet than set up a separate system.
- **First question:** "Is participant payment information (address, W-9, gift card codes) in the same file as their response data, joinable by anything other than a study ID?"
- **Data to pull:** the response file's column list; split payment info into a separate file linked only by study ID, with the crosswalk restricted to the PI or one designated RA.

## Double-entry discrepancy rate above ~1% on a batch, with only the flagged rows corrected

- **Usually means:** the entry process itself is producing systematic errors (ambiguous source handwriting, a confusing form layout) that the diff tool only partially catches, since it can only flag rows where the two entries disagree — not rows where both entrants made the same mistake.
- **First question:** "What's the discrepancy rate on this batch, and was the whole batch re-verified against source or just the flagged rows?"
- **Data to pull:** the diff report with the discrepancy count and rate; re-verify the full batch against the original source documents if the rate is above roughly 1%.
