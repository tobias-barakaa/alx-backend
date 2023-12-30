#!/usr/bin/env python3
"""
index_range - functions.
0x00. Python - Variable Annotations
"""
import csv
from typing import List, Dict, Union
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers.")
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATAFILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize instance.
        """
        self.__dataset = None

    def dataset(self) -> List[str]:
        """
        Dataset getter.
        """
        return self.__dataset

    def get_dataset(self) -> List[str]:
        """
        Get dataset.
        """
        if self.__dataset is None:
            with open(self.DATAFILE, "r") as f:
                reader = csv.reader(f)
                dataset = []
                for row in reader:
                    dataset.append(row)
            self.__dataset = dataset[1:]
        return self.__dataset

    @staticmethod
    def get_page(page: int = 1, page_size: int = 10) -> List[str]:
        """
        Get page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        server = Server()
        start, end = index_range(page, page_size)
        return server.get_dataset()[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_info = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_info
