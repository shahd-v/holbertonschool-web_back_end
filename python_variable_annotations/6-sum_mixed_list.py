#!/usr/bin/env python3
"""Summing a list containing integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the floating-point sum of mixed numeric values."""
    return float(sum(mxd_lst))
