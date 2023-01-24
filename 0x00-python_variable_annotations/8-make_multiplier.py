#!/usr/bin/env python3
""" Write a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that multiplies
a float by multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that returns another function that multiplies x by
    the passed variable"""

    def my_fun(x: float) -> float:
        """a Callable function that returns a float"""
        return x * multiplier

    return my_fun
