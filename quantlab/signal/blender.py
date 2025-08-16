import pandas as pd
from typing import Dict


def weighted_blend(alphas: Dict[str, pd.Series], weights: Dict[str, float]) -> pd.Series:
    """Combine alpha streams with static weights."""
    df = pd.DataFrame(alphas)
    w = pd.Series(weights)
    return df.mul(w).sum(axis=1)
