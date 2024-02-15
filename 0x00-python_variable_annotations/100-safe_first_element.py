#!/usr/bin/env python3
"""The following script defines a function
to safely retrieve the first element of a sequence."""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function returns the first element of a sequence
    or None if the sequence is empty.

    Args:
        lst: A sequence from which to retrieve the first element.

    Returns:
        The first element of the sequence if it's not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
