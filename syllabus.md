# AIE683 Machine Learning — Syllabus

**Hacettepe University, Graduate School of Informatics · Fall 2026**
**Instructor:** Dr. Hakan Emekci · hakanemekci@hacettepe.edu.tr
**Lectures:** Thursdays 08:40–11:40
**Office hours:** Thursdays 12:00–13:00 and 16:00–17:00
**Language of instruction:** English

## Course Description

This is a graduate course on machine learning with an emphasis on doing it rigorously and running it in practice. It covers the foundations of statistical learning; the main model families (linear models, tree ensembles and gradient boosting, neural networks); the practice of evaluating, tuning, comparing and interpreting models; unsupervised learning; and time series forecasting. Machine learning is treated as a living process rather than a one-off notebook: experiments are tracked with MLflow throughout the term, and the final weeks cover the ML lifecycle of registering, serving, monitoring and retraining models. Students carry out an empirical ML study and write it up as a research paper.

## Prerequisites

- Programming in Python
- Linear algebra, probability, and statistics at the undergraduate level

## Learning Outcomes

By the end of the course, students will be able to:

1. Explain the core concepts of statistical learning: generalization, the bias–variance trade-off, overfitting, and regularization.
2. Build end-to-end ML pipelines in Python, from preprocessing through model selection.
3. Choose algorithms suited to a given problem and data type, and justify the choice.
4. Evaluate models rigorously with appropriate metrics, resampling, and statistical comparison.
5. Recognize and avoid common pitfalls of applied ML, such as data leakage and distribution shift.
6. Track, version, deploy and monitor models across the ML lifecycle using MLflow.
7. Design, run, and report an ML study as a research paper.

## Weekly Schedule

| Week | Topic |
|---|---|
| 1 | Introduction: ML problem framing, the ML workflow; tooling (uv, Git, MLflow) |
| 2 | Generalization & validation: nearest neighbors, bias–variance, cross-validation strategies |
| 3 | Preprocessing, feature engineering, pipelines, data leakage |
| 4 | Linear models: regression, regularization, logistic regression, SVMs |
| 5 | Tree ensembles: decision trees, random forests, gradient boosting |
| 6 | Neural networks (MLP): backpropagation, regularization, MLPs on tabular data |
| 7 | Evaluation: metrics, calibration, imbalanced data, decision thresholds |
| 8 | Model selection & experiment tracking: tuning, nested CV, model comparison, MLflow Tracking |
| 9 | Interpretation & feature selection: permutation importance, PDP, SHAP |
| 10 | Unsupervised learning: PCA, t-SNE/UMAP, clustering, mixture models |
| 11 | Time series forecasting: lag features, time-based CV, boosting vs. classical baselines |
| 12 | The ML lifecycle: MLflow Models & Registry, serving, monitoring, drift, anomaly detection, retraining |
| 13 | Project presentations |

## Assessment

| Component | Weight | Due |
|---|---|---|
| Paper proposal | 10% | Week 5 |
| Homework assignments (4 × 5%) | 20% | Weeks 5, 7, 9, 13 |
| Project & research paper | 70% | Progress report Week 10; presentation Week 13; final paper in finals week |

There is no written exam. See [project/](project/) for the project components and rubric.

## Textbook

- Andreas C. Müller, Sarah Guido. *Introduction to Machine Learning with Python*. O'Reilly, 2016.

Supplementary:

- Hastie, Tibshirani, Friedman. *The Elements of Statistical Learning*, 2nd ed. Springer, 2009.
- James, Witten, Hastie, Tibshirani, Taylor. *An Introduction to Statistical Learning with Applications in Python*. Springer, 2023.

## Policies

- **Late submissions:** 10% per day, up to 3 days; not accepted after that.
- **Academic integrity:** Submitted work is checked for plagiarism. Copied work receives 0 for everyone involved. Cite all external sources.
- **Use of AI assistants:** Allowed. Each submission must state how AI tools were used; you are responsible for the correctness of everything you submit.
- **Attendance:** Follows Hacettepe University graduate regulations.

## Acknowledgments

The lecture materials build on Andreas C. Müller's openly published *Applied Machine Learning* course (Columbia University, CC0). See the [README](README.md#acknowledgments) for full credits.

*This syllabus may be updated as the term progresses; the version in this repository is authoritative.*
