#!/usr/bin/env python3
"""
This is a pythn 3 async comprehension.
"""
import asyncio
import typing
import random


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    random_numbers = [random.choice(async_generator) async for i in range(10)]
    return random_numbers