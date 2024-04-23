#!/usr/bin/env python3
"""Measure runtime"""


import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Parallel comprehension"""
    start_time = time.perf_counter()
    coroutines = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coroutines)
    end_time = time.perf_counter() - start_time
    return end_time
