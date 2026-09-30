# HW3: Which Trucks Go to the Workshop?

**Out:** Week 7 · **Due:** Week 9 (before the lecture) · **Weight:** 5% · **Expected effort:** 6–8 hours

## Scenario

A truck manufacturer logs 170 anonymized sensor readings per truck. Failures of the air pressure system (APS) are rare (under 2% of trucks) but expensive. Sending a truck for a check costs 10; missing a failing truck costs 500 (the costs of the IDA 2016 Industrial Challenge). A data scientist on the team says "our boosted model is clearly better than logistic regression, look at the cross-validation scores". The fleet maintenance manager wants a rule for which trucks to call in.

**Question:** which model and decision threshold minimize the expected cost, and is the "better" model really better?

## Skills you will practice

- Choosing a metric that matches a business cost
- Handling heavy class imbalance and missing values in a pipeline
- Tuning a decision threshold without touching the test data
- Nested cross-validation with one MLflow run per outer fold
- Comparing two models with the corrected resampled t-test on scores pulled from MLflow

## Data

APS Failure at Scania Trucks, `fetch_openml(data_id=41138)`, loaded by the starter: 76,000 trucks, 170 numeric sensor features with about 8% missing values, 1,375 failures.

## What you do

1. **Metric.** Work out what "do nothing" and "check everything" cost, and choose how to select and evaluate models.
2. **Compare** at least logistic regression and one tree ensemble with nested cross-validation (tuning inside, one MLflow run per outer fold with the fold scores logged).
3. **Test the claim.** Pull the per-fold scores back from MLflow and compare the two models with a paired t-test and the corrected resampled t-test. Do this for the ranking metric *and* for the cost.
4. **Obstacle.** The default decision rule is badly wrong for this problem. Find out how wrong, and fix it without using the test set.
5. **Decision.** Model, threshold, expected cost and savings per truck for the manager.

## Non-negotiables

Leakage-free evaluation · a baseline (the trivial policies) · the corrected test on the key comparison · every reported number has its MLflow run ID (experiment `hw3-truck-checks`) · the notebook runs top to bottom with fixed seeds in under 20 minutes on a laptop (subsample for nested CV if needed).

## Submission (one zip, fixed names)

`hw3_<studentID>.zip` containing exactly:

| File | Content |
|---|---|
| `hw3.ipynb` | your notebook (the starter, renamed), with outputs and a Markdown cell titled **AI-use statement** |
| `hw3_submission.py` | `THRESHOLD` and `build_pipeline()` as in the template |
| `answers.json` | written by the starter's last code cell; types and allowed values are listed there |
| `mlflow_runs.csv` | exported by the same cell; must contain the outer-fold runs you cite |

The memo to the maintenance manager is part of `answers.json` (decision, expected savings, main risk, ≤150-word justification).

## Grading (automated)

The grader fits your pipeline on its own split, applies your threshold to trucks you never see, and recomputes your statistical tests from the fold runs in your MLflow export.

| Criterion | Weight |
|---|---|
| Pipeline and decision rule: runs, held-out cost close to a strong reference, far below the trivial policies, chance-level on permuted labels | 45% |
| Statistical comparison: fold runs traceable and paired, p-values reproduce, conclusion matches the evidence | 15% |
| Diagnosis of the obstacle: cost at the default rule, threshold, metric choice | 15% |
| Decision: expected cost matches the held-out cost; savings and decision consistent | 10% |
| Reproducibility: files and schema valid, reported numbers match their MLflow runs | 15% |

Deductions: missing AI-use statement (−5, checked automatically). Late policy as in the syllabus. Submissions may be spot-checked by hand.
