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
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
