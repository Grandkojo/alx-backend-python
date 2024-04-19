#!/usr/bin/env python3
"""Duck typing an iterable object"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Determnes the length of the element"""
    return [(i, len(i)) for i in lst]
