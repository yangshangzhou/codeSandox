from typing import Any, Dict


class BrokerAPI:
    """Unified interface for live trading endpoints."""

    def __init__(self, credentials: Dict[str, str]) -> None:
        self.credentials = credentials

    def submit_order(self, symbol: str, qty: float, side: str, order_type: str = "market") -> Any:
        """Send an order to the broker."""
        raise NotImplementedError
