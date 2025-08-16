from dataclasses import dataclass
from typing import Callable
import pandas as pd


@dataclass
class BacktestEngine:
    """Event-driven backtesting engine operating on bar data."""

    data: pd.DataFrame
    signal_fn: Callable[[pd.DataFrame], pd.Series]
    cost_fn: Callable[[pd.Series], float]

    def run(self) -> pd.DataFrame:
        """Iterate over time, generate signals, apply costs, and compute PnL."""
        pnl = []
        positions = 0
        for ts, row in self.data.iterrows():
            sig = self.signal_fn(row.to_frame().T).iloc[0]
            trade_cost = self.cost_fn(sig)
            ret = positions * row['returns']
            positions = sig
            pnl.append(ret - trade_cost)
        return pd.DataFrame({'pnl': pnl}, index=self.data.index)
