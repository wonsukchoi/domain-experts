# Intelligence Analyst — Red Flags

### Assessment lists only confirming evidence, zero inconsistencies noted
- **Usually means:** No ACH matrix was actually built — the analyst reasoned toward a conclusion and collected support for it rather than testing it against alternatives.
- **First question:** "What evidence is inconsistent with this hypothesis, and where's the matrix that shows it?"
- **Data to pull:** The underlying ACH worksheet, if one exists; if none exists, that is itself the finding.

### Confidence language applied uniformly across an entire report ("high confidence" on everything)
- **Usually means:** Confidence labeling has become a formality rather than a calibrated judgment — often happens under deadline pressure or when a template default wasn't changed.
- **First question:** "Which specific claims in this report are corroborated by 2+ independent B-or-better sources, and which are single-sourced?"
- **Data to pull:** Source grading sheet for each cited claim.

### A network link chart with more than ~15 nodes and no centrality metrics, only visual clustering
- **Usually means:** The chart is being used for narrative persuasion (it "looks like" a big conspiracy) rather than analytic rigor.
- **First question:** "Which nodes have high betweenness centrality, and has that been checked against degree centrality?"
- **Data to pull:** Raw connection data exportable to a proper network-analysis tool, not just the visual chart.

### A single source graded A1 ("completely reliable, confirmed") on a claim no other source corroborates
- **Usually means:** The reliability grade of the source is being used to inflate the credibility grade of one specific, unconfirmed claim — a scoring error, since the two axes are independent.
- **First question:** "Has any other source, method, or record independently confirmed this specific claim?"
- **Data to pull:** All reporting touching the same claim, regardless of source.

### An analytic consensus formed in a single meeting or review cycle, with no dissent documented
- **Usually means:** Groupthink or anchoring on the first plausible hypothesis raised, especially likely when the group is small or hierarchical.
- **First question:** "Who argued the strongest case against the leading hypothesis, and what did they find?"
- **Data to pull:** Whether a formal devil's-advocacy or red-team pass occurred and what it produced.

### A pattern-match assessment on a rare event type with no base rate stated
- **Usually means:** The analyst is impressed by how well the pattern fits without checking how many false positives that pattern-matching approach would generate given how rare the event actually is.
- **First question:** "Out of all instances where this pattern appeared, how many were actually this event type?"
- **Data to pull:** Historical base-rate data for the event type and the pattern's false-positive rate.

### "Associate of" or "linked to" language used for a contact with no specified nature of contact
- **Usually means:** A link-chart edge (phone call, shared address, financial transfer) has been verbally upgraded to imply criminal association without evidence of what the contact actually was.
- **First question:** "What specifically connects these two nodes, and is there any evidence of shared criminal activity beyond the contact itself?"
- **Data to pull:** The raw record generating the edge (call log, lease, transaction) and any independent evidence of coordinated activity.

### An RFI has been open for multiple review cycles with no named matrix cell it would close
- **Usually means:** The request was made under general "let's get more information" pressure rather than to resolve a specific analytic gap — often a sign the assessment is being delayed rather than improved.
- **First question:** "Which specific hypothesis or evidence cell does closing this RFI actually change?"
- **Data to pull:** The RFI tracker cross-referenced against the live ACH matrix.

### A deviation from an otherwise-consistent pattern (like a single differing MO detail) is used to reject the leading hypothesis outright
- **Usually means:** One inconsistency is being weighted as disqualifying without comparing it against how many inconsistencies the rival hypotheses carry — the correct test is relative, not absolute.
- **First question:** "How many inconsistencies does the alternative hypothesis have, and is it actually fewer?"
- **Data to pull:** The full ACH matrix for all hypotheses, not just the flagged evidence item.

### Missing or unavailable data (a destroyed device, an unreachable witness) is scored as "inconsistent" with a hypothesis
- **Usually means:** Absence of evidence is being treated as evidence of absence — a scoring error that can wrongly tip a matrix toward or away from a hypothesis based on a data gap rather than an actual contradiction.
- **First question:** "Is this cell genuinely inconsistent with the hypothesis, or is it just missing information?"
- **Data to pull:** Whatever would need to exist to actually fill that evidence cell, and whether it's retrievable.
