#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination for a CSV dataset."""

import csv
from typing import Dict, List


class Server:
    """Server class that paginates a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached CSV dataset without its header row."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                self.__dataset = list(csv.reader(file))[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by each row's original position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                position: row for position, row in enumerate(dataset)
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict:
        """Return a stable page despite deleted rows."""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        indexed_data = self.indexed_dataset()
        assert index < len(indexed_data)
        available_indexes = sorted(
            key for key in indexed_data if key >= index
        )
        page_indexes = available_indexes[:page_size]
        data = [indexed_data[position] for position in page_indexes]
        next_index = (
            available_indexes[page_size]
            if len(available_indexes) > page_size else None
        )
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
