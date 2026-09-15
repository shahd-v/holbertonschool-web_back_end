#!/usr/bin/env python3
"""Creating typed multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its argument by multiplier."""
    def multiply(value: float) -> float:
        """Multiply a floating-point value by the captured multiplier."""
        return value * multiplier
    return multiply
