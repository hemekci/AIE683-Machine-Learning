# Term Project: Research Paper

The project is an original ML study written up as a conference-style research paper. Work alone or in pairs; pairs are expected to deliver proportionally more.

## Components

| Component | Weight | Due | Deliverable |
|---|---|---|---|
| Paper proposal | 10% | Week 5 | 2-page proposal (PDF) |
| Progress report | 15% | Week 10 | Draft paper with preliminary results + code repository |
| Presentation | 15% | Week 13 | 12-minute talk + 3 minutes Q&A |
| Final paper & code | 40% | Finals week | 6–8 page paper (PDF) + reproducible code |

The proposal counts separately (10%); the remaining three components make up the 70% project grade.

## 1. Paper Proposal (2 pages)

- **Problem and motivation:** what question you are asking and why it matters.
- **Related work:** at least 5 relevant papers.
- **Data:** source, size, license, and how you will access it.
- **Method:** baselines and the approach you will compare against them.
- **Evaluation:** metrics and validation strategy.
- **Timeline and risks:** milestones through the final submission, and what you will do if the main plan fails.

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
