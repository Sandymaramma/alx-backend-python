#!/usr/bin/env python3
""" Coroutine async_generator, takes no arguement """
from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generator that yields a random value between 0 and 10 every second,
        10 times. '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()
