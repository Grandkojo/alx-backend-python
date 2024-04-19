#!/usr/bin/env python3
"""Floor function using annotation"""


def floor(n: float) -> int:
    """Floor function"""
    if n > 0:
        return int(n)
    return int(n) - 1
