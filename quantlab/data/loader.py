from typing import Iterable, Dict, Any


class DataLoader:
    """Handles batch or streaming ingestion of raw data from configured sources."""

    def __init__(self, sources: Iterable[str]) -> None:
        self.sources = sources

    def fetch(self, start: str, end: str) -> Dict[str, Any]:
        """Pull data from all sources between two timestamps."""
        data: Dict[str, Any] = {}
        for src in self.sources:
            data[src] = self._load_source(src, start, end)
        return data

    def _load_source(self, name: str, start: str, end: str) -> Any:
        """Source-specific logic (placeholder)."""
        raise NotImplementedError
