#!/usr/bin/env python3
"""Converting values to key-and-square tuples."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a string key paired with the square of its numeric value."""
    return (k, float(v ** 2))
