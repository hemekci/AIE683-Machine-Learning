"""HW1 submission module. The autograder imports exactly these three names.

The grader loads the listings exactly as the starter does (columns renamed, `rent_amount` removed),
calls load_and_clean() on them, selects FEATURES, fits build_pipeline() on its own training split
with y = log(rent_amount), and scores it on a held-out split you do not see.
"""
import pandas as pd
from sklearn.base import BaseEstimator

# The raw input columns your model uses (after load_and_clean).
FEATURES: list[str] = []  # TODO


def load_and_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the listings. Must keep every row and must not use the target."""
    return df.copy()  # TODO


def build_pipeline() -> BaseEstimator:
    """Return an UNFITTED scikit-learn estimator: X[FEATURES] -> predicted log rent.

    Everything that learns from data (imputation, scaling, encoding, tuning) belongs inside it.
    """
    raise NotImplementedError("TODO: build your pipeline")
