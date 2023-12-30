#!/usr/bin/env python3
"""
index_range - functions.
0x00. Python - Variable Annotations
"""


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
