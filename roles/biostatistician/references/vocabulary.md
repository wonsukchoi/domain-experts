# Vocabulary

### Intention-to-treat (ITT)
Analysis of all randomized patients according to their assigned group, regardless of whether they completed, adhered to, or crossed over from the assigned treatment.
**In use:** "ITT keeps the dropouts in the denominator on their assigned arm — that's what preserves the balance randomization gave us."
**Common misuse:** Treating "modified ITT" (excluding some randomized patients, e.g. those never dosed) as equivalent to true ITT — the exclusion criteria for mITT need their own justification and can reintroduce the exact bias ITT is meant to prevent.

### Per-protocol analysis
Analysis restricted to patients who completed the trial according to the protocol as assigned, excluding major deviations and dropouts.
**In use:** "Per-protocol is our pre-specified sensitivity analysis for this non-inferiority trial, not the primary — ITT stays primary."
**Common misuse:** Presenting per-protocol as the primary analysis in a superiority trial specifically because it shows a larger effect than ITT — the divergence itself is often the signal of a dropout-related confound.

### Estimand
A precise description of the treatment effect being estimated, including the population, the endpoint, and how intercurrent events (dropout, rescue medication, treatment switch) are handled — formalized in ICH E9(R1).
**In use:** "We need to specify the estimand before picking a method — a 'treatment policy' estimand ignores rescue medication use, a 'hypothetical' estimand asks what would have happened without it, and they can give different answers from the same data."
**Common misuse:** Choosing a statistical method first and only implicitly defining the estimand afterward — the estimand should drive method choice, not the reverse.

### Censoring (right-censoring)
A patient's true event time is unknown because they exited the study (end of follow-up, dropout, or trial end) before the event occurred, but it's known the event hadn't happened by that point.
**In use:** "These 40 patients are right-censored at 12 months — they hadn't had the event yet when the trial ended, we don't know if or when they would."
**Common misuse:** Treating censored observations as missing data to be dropped or as if the event happened at the censoring time — both discard the "survived at least this long" information censoring actually encodes.

### Kaplan-Meier estimator
A non-parametric method for estimating the survival function from time-to-event data that properly accounts for right-censoring.
**In use:** "The Kaplan-Meier curves separate around month 4 — that's when the treatment effect on time-to-event starts showing up."
**Common misuse:** Reading the tail of a Kaplan-Meier curve as precise when very few patients remain at risk there — wide, unstable estimates at the tail are a sample-size artifact, not necessarily a real late-stage effect.

### Proportional hazards assumption
The assumption underlying the Cox model that the ratio of hazards between groups is constant over the entire follow-up period.
**In use:** "The Schoenfeld residual test rejects proportional hazards here — the treatment effect is stronger early and fades, so a single hazard ratio misrepresents it."
**Common misuse:** Reporting a Cox model hazard ratio without ever checking whether the proportional-hazards assumption actually holds for the data.

### Data Safety Monitoring Board (DSMB)
An independent committee, unaffiliated with the trial sponsor's efficacy analysis, that reviews unblinded interim safety (and sometimes efficacy) data and can recommend continuing, modifying, or stopping a trial.
**In use:** "The DSMB requested an ad hoc adjudication of the bleeding events — that's outside the pre-scheduled interim, triggered by the magnitude of the imbalance."
**Common misuse:** Assuming a DSMB only acts when a formal statistical stopping boundary is crossed — DSMBs are chartered to exercise clinical judgment on safety signals below that threshold too.

### Alpha-spending function
A pre-specified schedule for how much of the total trial-wide significance level is used at each interim analysis, so the cumulative Type I error rate across all looks stays at the nominal level.
**In use:** "Under the O'Brien-Fleming spending function, the interim look only gets α≈0.001 — that conservatism is intentional so the final analysis retains most of the total alpha."
**Common misuse:** Running repeated interim looks against a flat nominal threshold (e.g. checking p<0.05 at every monthly data pull) without a spending function, which inflates the true trial-wide false-positive rate well above the stated level.

### Gatekeeping procedure (hierarchical testing)
A pre-specified order for testing multiple endpoints such that a later endpoint is only tested (at full alpha) if an earlier one in the hierarchy achieved significance, controlling the family-wise error rate without a Bonferroni-style alpha split.
**In use:** "Endpoint 2 only gets tested if endpoint 1 succeeds — that's the gatekeeping order specified in the SAP, and it's why we didn't have to split alpha three ways up front."
**Common misuse:** Testing all secondary endpoints in parallel at the nominal 0.05 threshold while calling it "hierarchical" without actually enforcing the pass-through condition between them.

### Non-inferiority margin
The pre-specified maximum acceptable amount by which a new treatment's effect can be worse than an active comparator's, while still being considered "not meaningfully worse."
**In use:** "The margin is set at 1.5x the historical placebo-adjusted effect of the active comparator, per the FDA's fixed-margin method — it's not an arbitrary number."
**Common misuse:** Setting a wide margin specifically to make an underpowered or weaker-effect study pass as non-inferior, rather than deriving it from the historical evidence of the active comparator's own effect size.
