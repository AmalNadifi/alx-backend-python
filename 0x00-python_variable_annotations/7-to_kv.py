#!/usr/bin/env python3
"""
The following script defines a function to convert a Python variable
to a key-value pair."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python variable to a key-value pair.

    Args:
        k: The key in the key-value pair.
        v: The value in the key-value pair, which can be an integer or a float.

    Returns:
        A tuple representing the key-value pair, where the value is squared.
    """
    return k, v ** 2
