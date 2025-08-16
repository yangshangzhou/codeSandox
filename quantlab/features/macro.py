import pandas as pd


def yc_slope_10y2y(curve: pd.DataFrame) -> pd.Series:
    """Computes 10Y-2Y yield curve slope."""
    ten = curve['10Y']
    two = curve['2Y']
    return ten - two
