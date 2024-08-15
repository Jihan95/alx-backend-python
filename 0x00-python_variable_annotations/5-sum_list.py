#!/usr/bin/env python3
"""a type-annotated function sum_list"""
from typing import List


def sum_list(list: List[float]) -> float:
    """
    a type-annotated function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.
    """
    sum: float = 0.0
    for n in list:
        sum += n
    return sum
