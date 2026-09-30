# Homework Assignments

Four hands-on assignments, 5% each (20% total), about 6–8 hours each. Each one is a realistic applied case: one question, one real dataset, one decision, and at least one obstacle you have to find and fix yourself.

| HW | Out | Due | Case | Topics |
|---|---|---|---|---|
| [HW1](hw1-rent-suggestion/) | Week 3 | Week 5 | Can the rent suggestion launch? | Cleaning, leakage audit, pipelines, regularized linear models |
| [HW2](hw2-call-list/) | Week 5 | Week 7 | Who should the bank call? | Tree ensembles vs. MLP under an equal tuning budget; validation that matches deployment |
| [HW3](hw3-truck-checks/) | Week 7 | Week 9 | Which trucks go to the workshop? | Costs, imbalance, thresholds, nested CV, corrected resampled t-test from MLflow |
| [HW4](hw4-air-quality-service/) | Week 11 | Week 13 | The air-quality alert service | Forecasting, MLflow registry and aliases, serving, drift and anomaly detection, champion/challenger |

## How every homework works

- Start from the starter notebook and the submission-module template in the folder. The starter loads the data and writes the submission files; you write the substantive code.
- All runs are logged to MLflow. Every number you report carries the run ID it came from.
- You submit one zip with fixed file names: the notebook, a small Python module with fixed functions (e.g. `build_pipeline()`), `answers.json` (your findings, reported numbers and a structured decision memo) and your MLflow export. Each README gives the exact list.
- Grading is automated: the grader imports your module, fits your pipeline on its own split, scores it on held-out data you never see, runs leakage and robustness probes, and checks `answers.json` against your MLflow runs. Submissions may also be spot-checked by hand.
- The notebook must contain a Markdown cell titled **AI-use statement** (see the syllabus policy).
