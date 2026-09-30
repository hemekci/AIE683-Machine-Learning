# HW2: Who Should the Bank Call?

**Out:** Week 5 · **Due:** Week 7 (before the lecture) · **Weight:** 5% · **Expected effort:** 6–8 hours

## Scenario

A Portuguese bank sells term deposits by phone; about 12% of contacted clients subscribe. The call centre wants a ranked call list. One colleague says "gradient boosting always wins on tabular data", another says "a tuned neural network is just as good". Settle it with a comparison the losing side would accept as fair, then advise the call-centre manager.

**Question:** which model should rank the call list, and what should the manager expect from it?

## Skills you will practice

- Spotting a feature that is not available at decision time
- Building per-family pipelines (encoding, scaling) for trees, linear models and MLPs
- Tuning several model families under an equal budget
- Quantifying uncertainty of a model comparison on a test set
- Checking whether a validation scheme matches deployment
- Logging searches and results to MLflow

## Data

Bank Marketing (Moro, Cortez & Rita, 2014, *Decision Support Systems* 62), `fetch_openml(data_id=1461)`, loaded by the starter: 45,211 clients contacted May 2008 – Nov 2010, 16 attributes (client, contact and previous-campaign information). The rows are in chronological order.

## What you do

1. **Protocol.** Decide which inputs a pre-call model may use, how you split the data, and how you tune. Justify it.
2. **Compare.** A logistic-regression baseline, random forest, `HistGradientBoostingClassifier`, LightGBM or XGBoost, and an MLP, each tuned with the **same number of configurations** (grid or random search). Use ROC AUC and a call-list metric (lift in the top 10%).
3. **Uncertainty.** Evaluate on held-out data once, with an interval for the key difference (a paired bootstrap as in Week 5; the starter provides a helper).
4. **Obstacle.** Check whether your evaluation describes the *next* campaign. Quantify what you find.
5. **Decision.** Which model, and what lift should the manager expect?

## Non-negotiables

Leakage-free evaluation · a baseline · an interval on the key comparison · every reported number has its MLflow run ID (experiment `hw2-call-list`) · the notebook runs top to bottom with fixed seeds in under 20 minutes on a laptop. LightGBM/XGBoost on macOS need `brew install libomp`.

## Submission (one zip, fixed names)

`hw2_<studentID>.zip` containing exactly:

| File | Content |
|---|---|
| `hw2.ipynb` | your notebook (the starter, renamed), with outputs and a Markdown cell titled **AI-use statement** |
| `hw2_submission.py` | `FEATURES`, `CHOSEN_MODEL`, `build_pipeline()` as in the template |
| `answers.json` | written by the starter's last code cell; types and allowed values are listed there |
| `mlflow_runs.csv` | exported by the same cell |

The memo to the call-centre manager is part of `answers.json` (decision, expected lift, main risk, ≤150-word justification).

## Grading (automated)

The grader fits your `build_pipeline()` on its own split and scores it on held-out clients you never see; it also re-runs your pipeline to check your reported findings.

| Criterion | Weight |
|---|---|
| Pipeline and evaluation: runs, leak-free, held-out AUC close to a strong reference, chance-level on permuted labels, all families compared under an equal budget | 55% |
| Diagnosis: leak and the next-campaign obstacle identified and quantified | 15% |
| Decision: expected AUC and lift match the held-out results; interval and decision consistent | 15% |
| Reproducibility: files and schema valid, reported numbers match their MLflow runs | 15% |

Deductions: missing AI-use statement (−5, checked automatically). Late policy as in the syllabus. Submissions may be spot-checked by hand.
