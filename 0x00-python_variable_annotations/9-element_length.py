#!/usr/bin/env python3
"""The following script defines a function to compute the elements
length in an iterable"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Computes the length of elements in an iterable and returns a list of tuples.

    Args:
        lst: An iterable containing sequences whose lengths are to be computed.

    Returns:
        A list of tuples where each tuple contains a sequence
        from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
