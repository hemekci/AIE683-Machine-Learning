"""HW4 submission module. The autograder imports exactly these four names.

The grader builds the hourly frame exactly like feed.load_hourly() (clean data) and checks:
make_features (horizon, no look-ahead), build_pipeline (accuracy on a grader time window),
create_app (serving contract) and detect_drift (on grader-generated samples).
"""
import pandas as pd
from fastapi import FastAPI
from sklearn.base import BaseEstimator


def make_features(df: pd.DataFrame) -> pd.DataFrame:
    """Input: hourly frame as returned by feed.load_hourly() (DatetimeIndex).
    Output: one row per forecast origin t (same DatetimeIndex), numeric feature columns computed from data
    available at time t only, plus a column "target" = pm2.5 at t + 24 h (NaN where unknown)."""
    raise NotImplementedError("TODO: make_features")


def build_pipeline() -> BaseEstimator:
    """Return an UNFITTED regressor for make_features(...) without the "target" column (NaN may occur)."""
    raise NotImplementedError("TODO: build_pipeline")


def create_app(model) -> FastAPI:
    """Serve a FITTED model (fitted on a DataFrame, so model.feature_names_in_ exists).

    POST /predict with {"rows": [{<feature>: number or null, ...}, ...]}
    returns {"predictions": [float, ...]} in the same order; invalid requests return HTTP 422."""
    raise NotImplementedError("TODO: create_app")


def detect_drift(reference: pd.DataFrame, current: pd.DataFrame) -> dict:
    """Both inputs are hourly frames with the columns of feed.load_hourly().
    Return at least {"drift": bool, "features": [names of drifted columns]}."""
    raise NotImplementedError("TODO: detect_drift")
