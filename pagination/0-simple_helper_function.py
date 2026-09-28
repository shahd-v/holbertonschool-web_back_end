#!/usr/bin/env python3
"""Helpers for calculating page boundaries."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the inclusive-start, exclusive-end indexes for a page."""
    end_index = page * page_size
    return (end_index - page_size, end_index)
