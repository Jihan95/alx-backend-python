#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
from asyncio import gather
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather
    measure_runtime should measure the total runtime and return it.
    """
    s = time.perf_counter()
    await gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())
    return time.perf_counter() - s
