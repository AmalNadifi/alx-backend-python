#!/usr/bin/env python3
"""The following script measure the total execution time of
a function"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function to Measure the total execution time of a function
    Args:
        n(int): Number of times to call wait_n
        max_delay(int): the maximum delay in seconds for each call to wait_n
    Returns:
        float: Average time per execution in seconds.
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start_time
    return total_time / n
