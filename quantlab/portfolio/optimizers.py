import numpy as np
import pandas as pd
from typing import Tuple


def mean_variance(mu: pd.Series, cov: pd.DataFrame, lam: float) -> pd.Series:
    """Solve classic mean-variance optimization."""
    inv_cov = np.linalg.inv(cov)
    w = inv_cov @ mu.values / (2 * lam)
    return pd.Series(w, index=mu.index)
