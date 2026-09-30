# AIE683 Machine Learning

**Hacettepe University, Graduate School of Informatics · Fall 2026**

Instructor: Dr. Hakan Emekci
Lectures: Thursdays 08:40–11:40
Office hours: Thursdays 12:00–13:00 and 16:00–17:00
Email: hakanemekci@hacettepe.edu.tr

This repository holds the course materials: syllabus, weekly slides and notebooks, homework assignments, and project guidelines. The full syllabus is in [syllabus.md](syllabus.md).

## Schedule

| Week | Topic | Materials | Due |
|---|---|---|---|
| 1 | Introduction: ML problem framing, the ML workflow; tooling (uv, Git, MLflow) | [slides](weeks/week01-introduction/) · [PDF](slides-pdf/week01-introduction.pdf) |  |
| 2 | Generalization & validation: nearest neighbors, bias–variance, cross-validation strategies | [slides](weeks/week02-generalization-validation/) · [PDF](slides-pdf/week02-generalization-validation.pdf) |  |
| 3 | Preprocessing, feature engineering, pipelines, data leakage | [slides](weeks/week03-preprocessing/) · [PDF](slides-pdf/week03-preprocessing.pdf) | HW1 out |
| 4 | Linear models: regression, regularization, logistic regression, SVMs | [slides](weeks/week04-linear-models/) · [PDF](slides-pdf/week04-linear-models.pdf) |  |
| 5 | Tree ensembles: decision trees, random forests, gradient boosting | [slides](weeks/week05-tree-ensembles/) · [PDF](slides-pdf/week05-tree-ensembles.pdf) | HW1 due · HW2 out · **Paper proposal** |
| 6 | Neural networks (MLP): backpropagation, regularization, MLPs on tabular data | [slides](weeks/week06-neural-networks/) · [PDF](slides-pdf/week06-neural-networks.pdf) |  |
| 7 | Evaluation: metrics, calibration, imbalanced data, decision thresholds | [slides](weeks/week07-model-evaluation/) · [PDF](slides-pdf/week07-model-evaluation.pdf) | HW2 due · HW3 out |
| 8 | Model selection & experiment tracking: tuning, nested CV, model comparison, MLflow Tracking | [slides](weeks/week08-model-selection-tracking/) · [PDF](slides-pdf/week08-model-selection-tracking.pdf) |  |
| 9 | Interpretation & feature selection: permutation importance, PDP, SHAP | [slides](weeks/week09-interpretation/) · [PDF](slides-pdf/week09-interpretation.pdf) | HW3 due |
| 10 | Unsupervised learning: PCA, t-SNE/UMAP, clustering, mixture models | [slides](weeks/week10-unsupervised/) · [PDF](slides-pdf/week10-unsupervised.pdf) | **Progress report** |
| 11 | Time series forecasting: lag features, time-based CV, boosting vs. classical baselines | [slides](weeks/week11-time-series/) · [PDF](slides-pdf/week11-time-series.pdf) | HW4 out |
| 12 | The ML lifecycle: MLflow Models & Registry, serving, monitoring, drift, anomaly detection, retraining | [slides](weeks/week12-ml-lifecycle/) · [PDF](slides-pdf/week12-ml-lifecycle.pdf) |  |
| 13 | Project presentations |  | HW4 due · **Presentation** |
| Finals | | | **Final paper & code** |

The plan may shift with the pace of the class; changes are announced in class and reflected here.

## Readings

**IMLP** = Müller & Guido, *Introduction to Machine Learning with Python* (course textbook). **AML** = Müller, [*Applied Machine Learning with Python*](https://amueller.github.io/aml/) (free online book).

| Week | Readings |
|---|---|
| 1 | IMLP Ch. 1 · AML: [Introduction](https://amueller.github.io/aml/00-introduction/00-introduction.html) |
| 2 | IMLP Ch. 2 (k-NN), Ch. 5.1 · AML: [Supervised learning](https://amueller.github.io/aml/01-ml-workflow/02-supervised-learning.html), [Data splitting strategies](https://amueller.github.io/aml/04-model-evaluation/1-data-splitting-strategies.html) |
| 3 | IMLP Ch. 3.3, Ch. 4, Ch. 6 · AML: [Preprocessing](https://amueller.github.io/aml/01-ml-workflow/03-preprocessing.html), [Pipelines](https://amueller.github.io/aml/01-ml-workflow/12-pipelines-gridsearch.html) · Kapoor & Narayanan (2023), [Leakage and the reproducibility crisis in ML-based science](https://doi.org/10.1016/j.patter.2023.100804), *Patterns* |
| 4 | IMLP Ch. 2.3.3, 2.3.7 · AML: [Linear regression](https://amueller.github.io/aml/02-supervised-learning/05-linear-models-regression.html), [Linear classification](https://amueller.github.io/aml/02-supervised-learning/06-linear-models-classification.html) |
| 5 | IMLP Ch. 2.3.5–2.3.6 · AML: [Trees](https://amueller.github.io/aml/02-supervised-learning/08-decision-trees.html), [Random forests](https://amueller.github.io/aml/02-supervised-learning/09-random-forests.html), [Gradient boosting](https://amueller.github.io/aml/02-supervised-learning/10-gradient-boosting.html) · Grinsztajn, Oyallon & Varoquaux (2022), [Why do tree-based models still outperform deep learning on typical tabular data?](https://arxiv.org/abs/2207.08815), NeurIPS |
| 6 | IMLP Ch. 2.3.8 · AML: [Neural networks](https://amueller.github.io/aml/02-supervised-learning/11-neural-networks.html) |
| 7 | IMLP Ch. 5.3 · AML: [Evaluation metrics](https://amueller.github.io/aml/04-model-evaluation/10-evaluation-metrics.html), [Calibration](https://amueller.github.io/aml/04-model-evaluation/11-calibration.html), [Imbalanced data](https://amueller.github.io/aml/05-advanced-topics/11-imbalanced-datasets.html) |
| 8 | IMLP Ch. 5.2 · AML: [Parameter tuning & AutoML](https://amueller.github.io/aml/04-model-evaluation/parameter_tuning_automl.html) · Nadeau & Bengio (2003), [Inference for the generalization error](https://doi.org/10.1023/A:1024068626366), *Machine Learning* · Demšar (2006), [Statistical comparisons of classifiers over multiple data sets](https://jmlr.org/papers/v7/demsar06a.html), *JMLR* · [MLflow Tracking docs](https://mlflow.org/docs/latest/ml/tracking/) |
| 9 | IMLP Ch. 4.5 · AML: [Interpretation](https://amueller.github.io/aml/04-model-evaluation/12-interpretation.html), [Feature selection](https://amueller.github.io/aml/05-advanced-topics/12-feature-selection.html) |
| 10 | IMLP Ch. 3.4–3.5 · AML: [Dimensionality reduction](https://amueller.github.io/aml/03-unsupervised-learning/01-matrix-factorization-dimensionality-reduction.html), [Clustering](https://amueller.github.io/aml/03-unsupervised-learning/02-clustering-mixture-models.html) |
| 11 | Hyndman & Athanasopoulos, [*Forecasting: Principles and Practice*, 3rd ed.](https://otexts.com/fpp3/) (free online), Ch. 1, 5, 8 |
| 12 | Sculley et al. (2015), [Hidden technical debt in machine learning systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems), NeurIPS · AML: [Outlier detection](https://amueller.github.io/aml/03-unsupervised-learning/03-outlier-detection.html) · [MLflow Model Registry docs](https://mlflow.org/docs/latest/ml/model-registry/) |

## Assessment

| Component | Weight |
|---|---|
| Paper proposal | 10% |
| Homework assignments (4) | 20% |
| Project & research paper | 70% |

Details: [project/](project/) · [homeworks/](homeworks/)

## Viewing the slides

**PDF:** every week's slides are in [slides-pdf/](slides-pdf/) (one page per slide, including the Backup section at the end).

**HTML (presenter mode):** Slides are [remark.js](https://remarkjs.com) HTML decks. Clone the repository and open `weeks/weekNN-*/index.html` in a browser (an internet connection is needed for fonts and math rendering). Press `P` for presenter notes and `C` to clone the view.

For topics outside the weekly plan (text data, topic models, word embeddings, CNNs, recommender systems), see Andreas Müller's original course materials: [amueller/COMS4995-s20](https://github.com/amueller/COMS4995-s20).

## Environment

```bash
uv sync                  # creates .venv from pyproject.toml
uv run jupyter lab
uv run mlflow ui          # experiment tracking UI at http://127.0.0.1:5000
```

From Week 2 on, every notebook and homework logs its runs to MLflow.

**macOS:** XGBoost and LightGBM need the OpenMP runtime. Install it once with `brew install libomp` ([Homebrew](https://brew.sh)); otherwise importing them fails with `libomp.dylib not found`.

**Slow gradient boosting?** If `HistGradientBoosting*` is unexpectedly slow, limit the thread count before starting Jupyter: `export OMP_NUM_THREADS=2` (the course notebooks already set this in their first cell).

## Textbook

- Andreas C. Müller, Sarah Guido. *Introduction to Machine Learning with Python*. O'Reilly, 2016.
- Supplementary: Hastie, Tibshirani, Friedman. *The Elements of Statistical Learning*, 2nd ed. Springer, 2009 (free online).

## Acknowledgments

This course builds on the openly published work of **Andreas C. Müller**, whom we thank for making it available:

- *Applied Machine Learning* (Columbia University, COMS W4995), Spring 2019 and Spring 2020 editions, slides and notebooks released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/): [amueller/COMS4995-s20](https://github.com/amueller/COMS4995-s20), [amueller/COMS4995-s19](https://github.com/amueller/COMS4995-s19)
- *Applied Machine Learning with Python*, online book: [amueller.github.io/aml](https://amueller.github.io/aml) (linked as reading, not redistributed)
- A. C. Müller, S. Guido. *Introduction to Machine Learning with Python*. O'Reilly, 2016.

The slides were reorganized into this course's weekly plan, updated to current versions of scikit-learn and related libraries, and extended with new material (experiment tracking with MLflow, the ML lifecycle, time series forecasting). Errors introduced in that process are ours.

If you reuse these materials, please keep this acknowledgment.
