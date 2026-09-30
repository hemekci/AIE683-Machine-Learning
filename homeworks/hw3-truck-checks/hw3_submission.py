"""HW3 submission module. The autograder imports exactly these names.

The grader loads the data exactly as the starter does (170 float sensor columns with missing values),
fits build_pipeline() on its own training split, flags trucks with predict_proba(...)[:, 1] >= THRESHOLD
on a held-out split you do not see, and computes the cost per truck (10 per check, 500 per missed failure).
"""
from sklearn.base import BaseEstimator

THRESHOLD: float = 0.5   # TODO: your decision threshold


def build_pipeline() -> BaseEstimator:
    """Return an UNFITTED classifier (preprocessing included) that implements predict_proba."""
    raise NotImplementedError("TODO: build your pipeline")
