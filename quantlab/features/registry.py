"""Feature registry to manage available features."""

FEATURES = {}


def register(name: str, fn):
    FEATURES[name] = fn


def get(name: str):
    return FEATURES[name]
