#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.
    """
    sum: float = 0.0
    for n in mxd_lst:
        sum += n
    return sum
