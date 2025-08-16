import pandas as pd
from dataclasses import dataclass


@dataclass
class RegimeModel:
    """Hidden Markov or similar regime detection."""

    n_states: int = 3

    def fit(self, features: pd.DataFrame) -> None:
        """Estimate regimes from feature history."""
        pass

    def predict(self, features: pd.DataFrame) -> pd.Series:
        """Return inferred regime for each observation."""
        return pd.Series(index=features.index)
