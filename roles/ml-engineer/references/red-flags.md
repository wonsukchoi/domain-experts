### A feature engineering step computes statistics (normalization, encoding, aggregates) across the full dataset before splitting into train/test
- **Usually means:** Test-set information is leaking into training via shared preprocessing statistics, inflating offline metrics beyond what production performance will show.
- **First question:** Are all feature statistics (means, encodings, historical aggregates) computed from the training set only, then applied to validation/test/serving data?
- **Data to pull:** Feature engineering pipeline code, the specific point where train/test split occurs relative to statistic computation.

### A validation/test metric looks implausibly strong given the problem's known difficulty
- **Usually means:** This is a common signature of data leakage rather than a genuine modeling breakthrough.
- **First question:** Has the feature pipeline been checked for any statistic or feature computed using information not available at the actual prediction time?
- **Data to pull:** Feature list and their computation logic, specifically checking for use of future or test-set data.

### A model's headline metric is accuracy on a dataset with a known class imbalance
- **Usually means:** Accuracy can be badly misleading on imbalanced data — a model can achieve high accuracy by simply predicting the majority class, masking whether it's actually catching the minority class of interest.
- **First question:** What is the actual class balance, and have precision/recall/F1/AUC-PR been calculated alongside (or instead of) accuracy?
- **Data to pull:** Class distribution in the dataset, confusion matrix for the model's predictions.

### Feature computation logic differs between the training pipeline and the serving pipeline
- **Usually means:** Train-serving skew — the model will see a different input distribution in production than it was trained on, degrading real-world performance in a way offline metrics won't reveal.
- **First question:** Is the exact same code/logic used to compute each feature at training time and at serving time, or are they separate implementations that could have subtly diverged?
- **Data to pull:** Training feature computation code, serving feature computation code, side-by-side comparison for a sample of records.

### A deployed model has no active monitoring for input or prediction distribution changes
- **Usually means:** Performance degradation from data or concept drift could be happening silently, with no alert until a downstream business metric noticeably suffers.
- **First question:** Is input feature distribution and prediction distribution being tracked over time since deployment, and has either shown meaningful drift?
- **Data to pull:** Historical input feature distribution and prediction distribution, compared to the training-time baseline.

### Hyperparameter tuning iterations were run directly against the test set
- **Usually means:** The final reported test metric is no longer an unbiased estimate of production performance, since the model has been indirectly fit to that specific test set through repeated tuning.
- **First question:** Was a separate validation set used for all tuning iterations, with the test set touched only once for the final evaluation?
- **Data to pull:** Tuning process log, number of times the test set was evaluated during development.

### A model's reported performance hasn't been re-evaluated since deployment
- **Usually means:** Any drift or degradation that's occurred since launch is currently invisible, since the last known-good metric may be stale.
- **First question:** When was this model's performance last measured against current production data, and how does it compare to the original reported metric?
- **Data to pull:** Deployment date, most recent production performance evaluation (or its absence).

### A near-duplicate or highly correlated record appears in both the training set and the test set
- **Usually means:** This is a specific, common form of data leakage (record-level leakage) that inflates test performance without the model genuinely generalizing.
- **First question:** Has the dataset been checked for duplicate or near-duplicate records split across train and test (e.g., the same customer's records appearing in both)?
- **Data to pull:** Deduplication/overlap check between train and test sets, keyed on the relevant entity (customer, transaction group, etc.).
