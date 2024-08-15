#!/usr/bin/env python3
"""element_length function"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length func"""
    return [(i, len(i)) for i in lst]
