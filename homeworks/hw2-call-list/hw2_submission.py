"""HW2 submission module. The autograder imports exactly these names.

The grader loads the data exactly as the starter does (original column names, text columns as
pandas 'category'), selects FEATURES, fits build_pipeline() on its own training split and scores
predict_proba(...)[:, 1] with ROC AUC on a held-out split you do not see.
"""
from sklearn.base import BaseEstimator

FEATURES: list[str] = []     # TODO: the input columns your model uses
CHOSEN_MODEL: str = ""       # TODO: one of the family names listed in the starter's answers cell


def build_pipeline() -> BaseEstimator:
    """Return an UNFITTED classifier (preprocessing included) with your chosen, tuned hyperparameters."""
    raise NotImplementedError("TODO: build your pipeline")
