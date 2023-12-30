#!/usr/bin/env python3
"""
index_range - functions.
0x00. Python - Variable Annotations
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with hypermedia pagination information.

        Args:
            index (int, optional): The current start index of the return page. Default is None.
            page_size (int, optional): The current page size. Default is 10.

        Returns:
            Dict: A dictionary containing pagination information.
        """
        assert index is None or 0 <= index < len(self.__indexed_dataset), "Index out of range."

        next_index = index + page_size if index is not None else None

        data = [
            self.__indexed_dataset[i]
            for i in range(index, min(index + page_size, len(self.__indexed_dataset)))
        ]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
