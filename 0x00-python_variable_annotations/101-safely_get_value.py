#!/usr/bin/env python3
"""Defines a method to safely retrieve a value from a dictionary."""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely gets value from a dictionary.
    
    Args:
        dct: The dictionary to retrieve the value from.
        key: The key whose value is to be retrieved.
        default: The default value to return if the key is not found.
        
    Returns:
        The value corresponding to the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
