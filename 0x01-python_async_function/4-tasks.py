#!/usr/bin/env python3
"""The following script spawns Tasks n times with a
specified delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine spawns wait_random n times with a specified delay
    between each call.
    Args:
        n(int): number of times to spawn wait_random
        max_delay(int): maximum delay between each call
    Returns:
        List(float): list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = awaitasyncio.gather(*tasks)
    results.sort()

    return results
