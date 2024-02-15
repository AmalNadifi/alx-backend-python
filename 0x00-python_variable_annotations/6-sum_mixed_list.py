#!/usr/bin/env python3
"""
Defines a function to calculate the sum of numbers in a mixed list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of numbers in a mixed list.

    Args:
        mxd_lst: A list containing integers and floats.

    Returns:
        The sum of all the numbers in the list as a float.
    """
    return sum(mxd_lst)
