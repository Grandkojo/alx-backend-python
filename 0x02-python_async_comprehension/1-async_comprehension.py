#!/usr/bin/env python3
"""Python async comprehensions"""


import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """an async comprehension"""
    rand_numbers = [randNum async for randNum in async_generator()]
    return rand_numbers
