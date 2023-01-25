#!/usr/bin/env python3
""" write an async routine called wait_n that takes in 2 int arguments """

from typing import List
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency."""
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
        delays = sorted(delays)
    return delays
