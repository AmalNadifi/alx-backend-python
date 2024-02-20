#!/usr/bin/env python3
""" The following script is a python module to loop 10 times """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This function loops 10 times

    Args:
        no arguments
    Returns:
        nothing
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
