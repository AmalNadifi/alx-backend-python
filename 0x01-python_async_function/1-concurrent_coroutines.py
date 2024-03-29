#!/usr/bin/env python3
"""The following script spawns wait_random n times with a
specified delay between each call."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that spawns wait_random
    n times with the specified max_delay.

    Args:
        n(int): number of times to spawn wait_random
        max_delay(int): maximum delay between each call
    Returns:
        List(float): List of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
