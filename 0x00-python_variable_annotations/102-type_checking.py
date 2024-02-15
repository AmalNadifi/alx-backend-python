#!/usr/bin/env python3
"""
The following script is a function to zoom in on a list of integer
by multiplying each integer by a factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on a list of integers by multiplying each integer by a factor.

    Args:
        lst: A tuple of integers to be zoomed in on.
        factor: An integer factor by which to multiply each integer
        (default is 2).

    Returns:
        A list of integers resulting from
        multiplying each integer in the input tuple by the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
