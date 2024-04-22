#!/usr/bin/env python3
"""Tasks continuation"""


import random
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Multiple async coroutines"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*coroutines)
    return sorted(result)
