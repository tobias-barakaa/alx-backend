#!/usr/bin/env python3
"""
index_range - functions.
0x00. Python - Variable Annotations
"""

import csv
import math
from typing import List, Dict, Union


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index is None or (isinstance(index, int) and 0 <= index < len(self.__indexed_dataset)), "Invalid index"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        next_index = index + page_size if index is not None else None
        data = [self.__indexed_dataset[i] for i in range(index, index + page_size) if i in self.__indexed_dataset]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
