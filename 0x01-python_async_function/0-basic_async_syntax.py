#!/usr/bin/env python3
"""Python async functions"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async wait random function"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
