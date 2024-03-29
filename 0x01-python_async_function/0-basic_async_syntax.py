#!/usr/bin/env python3
"""The following script is a coroutine that delays
a certain amount of time and returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random float
    between 0 and max_delay

    Args:
        max_delay(int, optional): The maximum delay to return
    Returns:
        float: the random delay waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
