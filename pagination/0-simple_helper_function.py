#!/usr/bin/env python3
"""
Module to compute the index range for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of (start_index, end_index) for pagination.
    
    :param page: The current page number (1-indexed).
    :param page_size: The number of items per page.
    :return: A tuple (start_index, end_index) where the end_index is exclusive.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
