#!/usr/bin/env python3
"""Duck Typing"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck Typing"""
    if lst:
        return lst[0]
    else:
        return None
