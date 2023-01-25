#!/usr/bin/env python3
""" write """

import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehensing returns the 10 random numbers"""
    return [i async for i in async_generator()]
