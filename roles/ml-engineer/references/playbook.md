# Machine Learning/AI Engineer — Playbook

## Data leakage check and correction (filled example)

| Step | Value |
|---|---|
| Initial (leaky) reported recall | 92% — feature computed using full dataset (including test-set/future transactions) before split |
| Correction applied | Feature recomputed using only data available before each transaction's timestamp (temporal split) |
| **Corrected (true held-out) recall** | **70%** |
| **Leakage-driven inflation** | 92% − 70% = **22 percentage points** |

**Use:** Any time a validation metric looks unusually strong, re-check the feature pipeline for leakage before trusting it — a 22-point gap between leaky and corrected metrics is a large, consequential difference that would have led to false confidence in production readiness.

## Imbalanced classification metric calculation (filled example)

| Component | Value |
|---|---|
| Total transactions | 100,000 |
| Actual fraud (positive class) | 800 (0.8%) |
| True positives | 560 |
| False negatives | 240 |
| False positives | 100 |
| True negatives | 99,100 |
| **Accuracy** | (560+99,100)/100,000 = **99.66%** |
| **Naive baseline accuracy** (predict all "not fraud") | 99,200/100,000 = **99.2%** |
| **Recall** | 560/800 = **70%** |
| **Precision** | 560/660 = **84.8%** |
| **F1** | 2×(0.848×0.70)/(0.848+0.70) ≈ **76.7%** |

**Use:** Always calculate and report recall/precision/F1 alongside accuracy for imbalanced problems — accuracy alone (99.66% vs. 99.2% baseline) makes this genuinely valuable model (70% recall, 84.8% precision) look almost worthless.

## Train-serving skew verification checklist

1. List every feature the model uses.
2. For each feature, identify the training-time computation logic (code path, data source).
3. Identify the serving-time computation logic (code path, data source) for the same feature.
4. Compare both on a sample of real records — do they produce identical values?
5. Flag and fix any discrepancy before deployment; even a small systematic difference can meaningfully degrade production performance.

## Leakage prevention checklist (train/test split)

1. Confirm the split happens before any feature statistic computation (normalization, encoding, historical aggregates).
2. For time-dependent data, confirm a temporal split is used — training data only includes information available before the prediction point.
3. Check for near-duplicate or highly correlated records (e.g., same customer) split across train and test.
4. Confirm feature statistics are computed from training data only, then applied (not recomputed) on validation/test/serving data.

## Drift monitoring setup checklist

1. Establish a baseline input feature distribution and prediction distribution at deployment time.
2. Set up recurring monitoring comparing current production distributions against the baseline.
3. Define a drift threshold (e.g., a statistical distance metric or simple percentage shift) that triggers investigation.
4. Re-evaluate model performance against fresh labeled data periodically, not just at initial deployment.

## Model evaluation findings memo — filled example

> **Fraud Detection Model — Evaluation Findings**
> Initial (leaky) validation recall: 92%, using a feature computed with test-set information included before the split.
> Corrected (temporal-split, leakage-free) held-out evaluation: **Recall 70%, Precision 84.8%, F1 76.7%**, Accuracy 99.66% (vs. 99.2% naive baseline).
> **Finding: Data leakage inflated the initially reported recall by 22 percentage points (92% vs. true 70%). Accuracy alone would have badly undersold the corrected model's real value (99.66% vs. 99.2% baseline looks unimpressive, but recall/precision show genuine business value).**
> **Recommendation: Report recall/precision/F1, not accuracy, as the primary metrics for this imbalanced problem going forward. Verify no other features carry similar temporal leakage before further model iterations.**
