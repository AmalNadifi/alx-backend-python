#!/usr/bin/env python3
"""The following script is a python module that measures the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function executes async_com 4 times

    Args:
        nothing
    Returns:
        the total execution time required for each task
    """
    start_time = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end_time = time.perf_counter()
    return (end_time - start_time)
