# HW1: Can the Rent Suggestion Launch?

**Out:** Week 3 · **Due:** Week 5 (before the lecture) · **Weight:** 5% · **Expected effort:** 6–8 hours

## Scenario

A rental platform wants to suggest an asking rent when landlords list a flat. A colleague's prototype reports a cross-validated R² of 0.99, and the Head of Product wants to launch. Requirement: typical suggestions within a factor of about 1.5 of the right rent, i.e. **RMSE ≤ 0.40 on log rent**.

**Question:** can the feature launch, and with which model?

## Skills you will practice

- Cleaning a messy real table
- Auditing features for leakage
- Writing one leak-free `Pipeline` with a `ColumnTransformer`
- Comparing regularized linear models against baselines
- Diagnosing a model that fails on part of the data
- Tracking experiments so every number has an MLflow run ID

## Data

10,692 listings from five Brazilian cities (`fetch_openml(data_id=42688)`, loaded by the starter): size, rooms, floor, pets, furniture and monthly costs in BRL. Target: `log(rent_amount)`.

## What you do

1. **Audit.** Reproduce the colleague's score, then find out why it is so high. Decide, with evidence, which inputs a landlord can actually provide.
2. **Fix.** Build a leak-free pipeline and report the honest performance.
3. **Model choice.** Compare baselines, OLS, Ridge and Lasso on the original features and on a richer feature set of your choice (e.g. interactions). You choose and justify the evaluation protocol.
4. **Obstacle.** At least one of your models will behave badly on part of the data. Find the cause and fix it in your cleaning or pipeline.
5. **Launch decision.** Launch, launch with conditions, or not? Account for the uncertainty of your estimate relative to the 0.40 requirement.

## Non-negotiables

- Leakage-free evaluation: everything that learns from data is fitted on training folds only.
- Baselines are reported next to the models, and the key comparison with its variability.
- Every reported number carries its MLflow run ID (experiment `hw1-rent-suggestion`).
- The notebook runs top to bottom with fixed seeds in under 15 minutes on a laptop.

## Submission (one zip, fixed names)

`hw1_<studentID>.zip` containing exactly:

| File | Content |
|---|---|
| `hw1.ipynb` | your notebook (the starter, renamed), with outputs |
| `hw1_submission.py` | `FEATURES`, `load_and_clean(df)`, `build_pipeline()`, as specified in the template |
| `answers.json` | written by the last cell of the starter; field types and allowed values are listed there |
| `mlflow_runs.csv` | exported by the same cell |

`answers.json` holds your findings, your reported numbers with run IDs, and the **launch memo** as structured fields (decision, expected error, main risk, and a ≤150-word justification for the Head of Product). Include a Markdown cell titled **AI-use statement** in the notebook (tools, for what, how you checked the output; "none" is valid).

## Grading (automated)

A grader imports your module, fits `build_pipeline()` on its own training split and scores it on a **held-out split you never see**, and checks `answers.json` against your MLflow export.

| Criterion | Weight |
|---|---|
| Pipeline and evaluation: runs, leak-free, held-out error close to a strong reference, near-chance score on permuted labels | 45% |
| Diagnosis: leak columns and the failing-model cause identified; the fix holds up on corrupted inputs | 25% |
| Decision: expected error matches the held-out error; decision consistent with it | 15% |
| Reproducibility: files and schema valid, reported numbers match their MLflow runs | 15% |

Deductions: missing AI-use statement (−5, checked automatically). Late policy as in the syllabus. Submissions may be spot-checked by hand.
