#!/usr/bin/env python3
"""
This is a pythn 3 asynchronous generator function.
"""
import asyncio
import typing
import random


async def async_generator() -> typing.AsyncGenerator[float, 0]:
    """
    Generates a sequence of 10 random floats between 0 and 10,
    pausing for 1 second between each number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
