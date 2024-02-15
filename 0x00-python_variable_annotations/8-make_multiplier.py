#!/usr/bin/env python3
"""The following script defines a function to create
a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function to multiply a float by a given multiplier
    Args:
        multiplier: The multiplier to be used in the function.

    Returns:
        Result of multiplying a float by the given multiplier.
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by the provided multiplier."""
        return multiplier * number

    return multiplier_func
