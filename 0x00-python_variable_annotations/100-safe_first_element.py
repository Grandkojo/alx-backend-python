#!/usr/bin/env python3
"""Duck typing annotation"""
from typing import List, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of s list"""
    if lst:
        return lst[0]
    else:
        return None
