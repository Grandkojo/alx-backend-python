#!/usrbin/env python3
"""Python async comprehensions"""


import random
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """an async comprehension"""
    rand_numbers = [randNum async for randNum in async_generator()]
    return rand_numbers
