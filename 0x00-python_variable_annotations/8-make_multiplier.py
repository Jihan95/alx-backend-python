#!/usr/bin/env python3
"""a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(n: float) -> Callable[[float], float]:
    """
    a type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier.
    """
    def func(x: float) -> float:
        """multiplier func"""
        return x * n
    return func
