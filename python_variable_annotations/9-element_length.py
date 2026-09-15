#!/usr/bin/env python3
"""Iterable sequence length helpers."""

from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    """Yield each sequence together with its length."""
    return ((item, len(item)) for item in lst)
