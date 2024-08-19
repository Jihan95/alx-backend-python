#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay
    wait_random will be spwaned n times with the specified max_delay
    """
    delays = []
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    try:
        for task in tasks:
            delays.append(await task)
    except Exception as e:
        for task in tasks:
            task.cancel()
    return delays
