### Data leakage
A modeling error where information from outside the training data (often the test set, or future information not available at prediction time) influences the model, producing offline metrics that don't reflect true production performance.
**In use:** "The 92% recall was leakage-inflated — the feature used transaction history from after the prediction point."
**Common misuse:** Assuming a strong validation metric is trustworthy without checking whether any feature or preprocessing step used information the model wouldn't actually have access to at prediction time.

### Train-serving skew
A mismatch between how a feature is computed during model training versus during production serving, causing the deployed model to see a different input distribution than it was trained on.
**In use:** "Train-serving skew is the likely cause — the serving pipeline computes this feature differently than the training pipeline did."
**Common misuse:** Assuming "similar" feature computation logic between training and serving is sufficient, when even small differences can meaningfully degrade production performance in ways offline evaluation won't catch.

### Class imbalance
A dataset where one class (often the outcome of interest, like fraud or disease) occurs much less frequently than the other(s), which distorts accuracy as a meaningful evaluation metric.
**In use:** "With only 0.8% positive cases, accuracy alone tells us almost nothing useful about this model."
**Common misuse:** Reporting accuracy as the primary metric on an imbalanced dataset without also reporting precision, recall, or another metric that accounts for the imbalance.

### Precision
The proportion of positive predictions that are actually correct (true positives divided by all predicted positives).
**In use:** "Precision of 84.8% means most of what we flag as fraud really is fraud."
**Common misuse:** Reporting precision alone without recall, missing the tradeoff between catching more true positives (recall) and avoiding false alarms (precision).

### Recall
The proportion of actual positive cases that the model correctly identifies (true positives divided by all actual positives).
**In use:** "Recall of 70% means we're catching 70% of actual fraud cases, missing the remaining 30%."
**Common misuse:** Optimizing solely for accuracy without checking recall, potentially missing that a model catches very few of the cases that actually matter (e.g., missing 30% of fraud while still posting a high overall accuracy).

### F1 score
The harmonic mean of precision and recall, providing a single balanced metric when both false positives and false negatives carry meaningful cost.
**In use:** "F1 of 76.7% balances the precision and recall tradeoff for this model."
**Common misuse:** Using F1 as the sole metric when the actual business cost of false positives and false negatives is asymmetric, in which case a weighted metric or examining precision/recall separately may be more appropriate.

### AUC-PR (Area Under the Precision-Recall Curve)
A metric summarizing model performance across all possible classification thresholds, particularly useful for imbalanced classification problems where AUC-ROC can be misleadingly optimistic.
**In use:** "AUC-PR gives a more honest picture of this model's performance than AUC-ROC does, given how rare the positive class is."
**Common misuse:** Defaulting to AUC-ROC for a highly imbalanced problem, where it can look deceptively strong even when precision at operationally relevant thresholds is poor.

### Data drift / concept drift
The phenomenon where the statistical properties of production input data (data drift) or the relationship between features and the target (concept drift) change over time after a model is deployed.
**In use:** "Input feature distributions have shifted meaningfully since launch — that's a data drift signal worth investigating."
**Common misuse:** Assuming a deployed model's performance remains constant indefinitely without actively monitoring for drift, allowing silent performance degradation to go undetected.

### Validation set vs. test set
Two distinct held-out datasets: the validation set is used repeatedly during model development for hyperparameter tuning, while the test set is reserved for a single, final, unbiased performance evaluation.
**In use:** "We're tuning against the validation set only — the test set gets touched exactly once, at the end."
**Common misuse:** Using the same held-out set for both iterative tuning and final evaluation, which causes indirect overfitting to that set and invalidates it as an unbiased estimate.

### Temporal split
A train/test splitting strategy that respects chronological order, ensuring training data only includes information that would have been available before the point in time being predicted.
**In use:** "We switched to a temporal split so the model can't accidentally use future information during training."
**Common misuse:** Using a random (non-temporal) split for time-dependent data, which can allow future information to leak into training and inflate offline performance in a way that won't hold when the model faces genuinely future data in production.
