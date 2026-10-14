# Term Project: Research Paper

The project is an original research study in machine learning or deep learning, written up as a conference-style research paper. It must make an academic contribution: a new or substantially modified method, a new empirical finding, a new dataset or benchmark, or a carefully argued negative result. Applying a known model to a new dataset is not enough on its own. Work alone or in pairs; pairs are expected to deliver proportionally more.

## Components

| Component | Weight | Due | Deliverable |
|---|---|---|---|
| Paper proposal | 10% | Week 5 (22 Oct) | 2-page proposal (PDF) |
| Progress report | 15% | Week 10 (3 Dec) | Draft paper with preliminary results + code repository |
| Presentation | 15% | Week 13 (24 Dec; slides due 23 Dec) | 12-minute talk + 3 minutes Q&A |
| Final paper & code | 40% | Finals week (date TBA) | 6–8 page paper (PDF) + reproducible code |

Deadlines are 23:59 Turkey time on the date shown. The proposal counts separately (10%); the remaining three components make up the 70% project grade.

## 1. Paper Proposal (2 pages)

Two pages plus references in a conference template (NeurIPS, ICML, or IEEE), submitted as a PDF inside a .zip through the [submission portal](https://yunus.hacettepe.edu.tr/~hakanemekci/submit/).

- **Research question and contribution:** the question you are asking, why it matters, and a one-sentence contribution statement: what will be new compared with the closest prior work.
- **Related work:** at least 8 papers, at least 5 of them peer-reviewed. Name the 2–3 closest works and the gap your study fills.
- **Data:** source, size, license, and how you will access it.
- **Method:** strong baselines, the approach you will compare against them, and the ablations you plan.
- **Evaluation:** metrics, a leakage-free validation strategy, and how you will compare models statistically.
- **Timeline and risks:** milestones through the final submission, and what you will do if the main plan fails.
- **Target venue (recommended):** a conference or workshop where the work could be submitted.

**Scope:** the study must use the ML/DL methods of this course (e.g. regularized linear models, tree ensembles, neural networks, model evaluation and selection, interpretation, unsupervised learning, time series, the ML lifecycle).

### Proposal Rubric

| Criterion | Points | What we look for |
|---|---|---|
| Research question and originality | 25 | A clear, testable question and an explicit contribution beyond the closest prior work |
| Related work and positioning | 20 | At least 8 papers (5+ peer-reviewed); the closest works and the gap are named |
| Fit with the course | 10 | Uses the ML/DL methods of this course |
| Method and baselines | 15 | Strong baselines and planned ablations |
| Evaluation design | 15 | Appropriate metrics, leakage-free validation, statistical comparison |
| Data, feasibility and ethics | 5 | Data access and license, compute, ethical issues |
| Timeline and risks | 5 | Realistic milestones and a fallback plan |
| Writing | 5 | Clear, within 2 pages, conference template |

**Minimum bar:** a proposal without a contribution statement and the closest prior work is returned for revision and must be resubmitted within one week.

## 2. Progress Report

A draft of the paper with the introduction, related work, and method written, plus baseline results under a leakage-free validation setup. Include a link to the code repository.

## 3. Presentation

Motivation, method, main results, and limitations. Slides are due the evening before the presentation.

## 4. Final Paper

Use a conference template (NeurIPS, ICML, or IEEE), 6–8 pages excluding references.

Expected sections: Abstract · Introduction · Related Work · Method · Experimental Setup · Results · Discussion & Limitations · Conclusion · References · AI-use statement.

Code must reproduce the main results: fixed random seeds, a `README` with run instructions, and a lock file (`uv.lock`). All experiments are tracked in MLflow, and every number in the paper's result tables must trace back to a run ID.

## Final Paper Rubric

| Criterion | Weight |
|---|---|
| Problem formulation and motivation | 15% |
| Related work and positioning | 10% |
| Methodological soundness | 20% |
| Experimental rigor (baselines, leakage-free validation, statistical comparison) | 20% |
| Analysis and discussion of results and limitations | 15% |
| Writing quality and presentation | 10% |
| Reproducibility & experiment tracking | 10% |
