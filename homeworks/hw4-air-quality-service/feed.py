"""Data access for HW4, as provided by the (fictional) data-engineering team. Do not modify.

load_hourly()           -> hourly history 2010-01-01 .. 2014-12-31 (DatetimeIndex, one row per hour)
production_batches()    -> the 2014 production feed, one DataFrame per ISO week, exactly as the
                           monitoring system received it
"""
import base64
import json

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml

COLUMNS = ["pm2.5", "DEWP", "TEMP", "PRES", "cbwd", "Iws", "Is", "Ir"]
_FEED = "eyJzdGFydCI6ICIyMDE0LTA2LTAxIiwgIm9wcyI6IFtbIlRFTVAiLCAxLjgsIDMyLjBdXX0="


def load_hourly() -> pd.DataFrame:
    """US Embassy Beijing PM2.5 (µg/m³) and weather, hourly. pm2.5 has gaps (NaN)."""
    raw = fetch_openml(data_id=42891, as_frame=True).frame
    idx = pd.to_datetime(dict(year=raw.year, month=raw.month, day=raw.day, hour=raw.hour))
    df = raw[COLUMNS].copy()
    df.index = pd.DatetimeIndex(idx, name="time")
    df["cbwd"] = df["cbwd"].astype(str)
    return df.astype({"DEWP": float, "TEMP": float, "PRES": float, "Iws": float, "Is": float, "Ir": float})


def production_batches(hourly: pd.DataFrame | None = None) -> list[pd.DataFrame]:
    """2014 as received in production, split into weekly batches (Monday to Sunday)."""
    df = (load_hourly() if hourly is None else hourly).loc["2014-01-01":].copy()
    cfg = json.loads(base64.b64decode(_FEED))
    after = df.index >= pd.Timestamp(cfg["start"])
    for col, a, b in cfg["ops"]:
        df.loc[after, col] = np.round(df.loc[after, col] * a + b, 1)
    return [g for _, g in df.groupby(df.index.to_period("W-SUN"))]
