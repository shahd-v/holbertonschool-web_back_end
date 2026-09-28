#!/usr/bin/env python3
"""Simple server-side pagination for a CSV dataset."""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end offsets for a one-indexed page."""
    end_index = page * page_size
    return (end_index - page_size, end_index)


class Server:
    """Server class that paginates a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached CSV dataset without its header row."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                self.__dataset = list(csv.reader(file))[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the requested slice of the dataset, or an empty list."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
