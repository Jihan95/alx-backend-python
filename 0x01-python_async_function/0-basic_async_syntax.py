#!/usr/bin/env python3
"""an asynchronous coroutine wait_random """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ an async coroutines that awaits random delay and returns it"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
