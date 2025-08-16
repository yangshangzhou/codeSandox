# QuantLab

## Introduction
QuantLab is a macro cross-asset quantitative research and trading framework. It
provides a modular pipeline covering data ingestion, feature engineering, alpha
models, signal generation, portfolio construction, risk management, backtesting
and execution. The framework targets multi-asset workflows such as equities,
rates, FX and crypto, enabling research from macro regime analysis to strategy
deployment.

## Installation
```bash
# create virtual environment then install in editable mode
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Usage
```python
import pandas as pd
from quantlab.features.macro import yc_slope_10y2y
from quantlab.backtest.engine import BacktestEngine

# sample data
curve = pd.DataFrame({'10Y': [0.03, 0.032], '2Y': [0.025, 0.027]})
print(yc_slope_10y2y(curve))

# simple backtest
prices = pd.DataFrame({'returns': [0.01, -0.005]}, index=pd.date_range('2020', periods=2))
engine = BacktestEngine(prices, lambda df: pd.Series([1], index=df.index), lambda s: 0.0)
print(engine.run())
```

## Roadmap
- Expand data connectors for macro and market sources.
- Implement additional factors and alpha models.
- Add portfolio optimizers and risk controls.
- Build FastAPI services and dashboards for live monitoring.

## License
This project is licensed under the [MIT License](LICENSE).
