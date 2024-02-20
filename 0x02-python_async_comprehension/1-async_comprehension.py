#!/usr/bin/env python3
""" The following script is a python module to returns
10 random numbers using async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function returns 10 random numbers
    Args:
        no arguments
    Returns:
        10 random numbers
    """
    results = [x async for x in async_generator()]
    return results
