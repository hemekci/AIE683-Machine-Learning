# HW4: The Air-Quality Alert Service

**Out:** Week 11 · **Due:** Week 13 (before the lecture) · **Weight:** 5% · **Expected effort:** 8 hours

## Scenario

A city environment office issues next-day health alerts when fine particulate matter (PM2.5) is forecast to be high. You build the forecasting service end to end: train and track a model, register it, serve it, and run it through 2014 as a production system. Somewhere in the 2014 feed something goes wrong.

**Question:** is the service still trustworthy in 2014, and should the champion model be replaced?

## Skills you will practice

- Building forecasting features that respect what is known at prediction time
- Logging, registering and aliasing a model in MLflow
- Serving a model behind a validated FastAPI endpoint
- Monitoring a production feed with drift tests and an anomaly detector
- Diagnosing a data problem, retraining a challenger, and making a champion/challenger decision

## Data

US Embassy Beijing PM2.5 with weather, hourly 2010–2014 (Liang et al., 2015, *Proc. R. Soc. A* 471), `fetch_openml(data_id=42891)`. Use `feed.py` (do not modify): `load_hourly()` for history and `production_batches()` for 2014 as the monitoring system received it.

## What you do

1. **Forecast** PM2.5 **24 hours ahead** from each hour. The Week 11 pipeline used weather observed at the target time; at 7 pm today, tomorrow's weather has not been observed. Decide what your served model may use, and measure what the difference costs.
2. **Track and register.** Compare against simple baselines on held-out history; log the champion with a signature; register it as `pm25-forecaster` with the alias `champion`.
3. **Serve** it with FastAPI (TestClient is enough), validating input.
4. **Monitor** 2014 week by week: drift tests (KS/PSI) against a sensible reference, an anomaly detector, and the error once the truth arrives.
5. **Obstacle.** Find what goes wrong in the feed, when it starts, and what to do about it.
6. **Retrain and decide.** Train a challenger, register it with the alias `challenger`, compare both on the same fresh data with an interval, and move `champion` only if the evidence supports it.

## Non-negotiables

No look-ahead in features or evaluation · baselines · an interval on the champion/challenger comparison · every reported number has its MLflow run ID (experiment `hw4-air-quality`) · the notebook runs top to bottom with fixed seeds in under 20 minutes on a laptop.

## Submission (one zip, fixed names)

`hw4_<studentID>.zip` containing exactly:

| File | Content |
|---|---|
| `hw4.ipynb` | your notebook (the starter, renamed), with outputs and a Markdown cell titled **AI-use statement** |
| `hw4_submission.py` | `make_features`, `build_pipeline`, `create_app`, `detect_drift` as specified in the template |
| `answers.json`, `registry.json`, `mlflow_runs.csv` | written by the starter's last code cell |

The memo to the environment office is part of `answers.json` (decision, main risk, action, ≤150-word justification).

## Grading (automated)

The grader checks your features for look-ahead by perturbing future data, fits your pipeline on its own time window, calls your API with valid and invalid requests, runs your drift detector on samples with and without a planted shift, and checks your answers against your MLflow runs and registry.

| Criterion | Weight |
|---|---|
| Forecasting pipeline: correct horizon, no look-ahead, accuracy close to a strong reference | 40% |
| Serving and monitoring: valid predictions, 422 on bad input, drift detector right on both samples | 22% |
| Diagnosis: weather assumption, the feed problem and its start | 13% |
| Registry and decision: aliases match the decision; decision consistent with the interval | 10% |
| Reproducibility: files and schema valid, reported numbers match their MLflow runs | 15% |

Deductions: missing AI-use statement (−5, checked automatically). Late policy as in the syllabus. Submissions may be spot-checked by hand.
