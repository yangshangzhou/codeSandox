"""Yahoo Finance data utilities."""

from __future__ import annotations

from typing import Optional

import matplotlib.pyplot as plt
import yfinance as yf


def plot_closing_price(symbol: str, start: Optional[str] = None, end: Optional[str] = None) -> None:
    """Fetch historical data for ``symbol`` from Yahoo Finance and plot the closing price.

    Parameters
    ----------
    symbol:
        The ticker symbol to download, e.g. ``"AAPL"``.
    start:
        Optional start date in ``YYYY-MM-DD`` format. If omitted, Yahoo Finance's
        default is used.
    end:
        Optional end date in ``YYYY-MM-DD`` format. If omitted, the latest
        available date is used.
    """
    data = yf.download(symbol, start=start, end=end)
    if data.empty:
        raise ValueError(f"No data returned for symbol {symbol}")

    ax = data["Close"].plot(title=f"{symbol} Closing Price")
    ax.set_ylabel("Price")
    plt.tight_layout()
    plt.show()
