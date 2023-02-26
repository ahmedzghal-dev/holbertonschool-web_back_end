#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:
You need to keep the same order to pass the checks (Union[Any, None])
"""
from typing import Sequence, List, Tuple, Iterable, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """a function
    takes in a sequence of any type and returns the first element if it exists
    or None if the sequence is empty. """
    if lst:
        return lst[0]
    else:
        return None
