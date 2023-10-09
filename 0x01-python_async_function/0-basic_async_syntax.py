#!/usr/bin/env python3

import asyncio
import random
"""
Waits for a random amount of time between 0 and `max_delay` seconds.

Args:
  max_delay: The maximum delay in seconds.

Returns:
  The amount of time that was waited for in seconds.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    and waits for a random delay between 0 and max_delay
    before returning it.
    """

    # define how long to wait
    delay = random.random() * max_delay
    # sleep for that amount of time
    await asyncio.sleep(delay)
    # return the amount of time waited
    return delay
