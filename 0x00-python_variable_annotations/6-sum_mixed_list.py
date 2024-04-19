#!/usr/bin/env python3
"""Complex types annotation"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Mixed list annotation"""
    return sum(mxd_lst)
