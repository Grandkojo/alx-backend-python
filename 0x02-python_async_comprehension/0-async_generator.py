#!/usr/bin/env python3
"""Python async comprehensions"""


import random
import asyncio


async def async_generator():
    """Async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
