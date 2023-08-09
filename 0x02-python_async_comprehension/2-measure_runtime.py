#!/usr/bin/env python3
""" Assignment: Import async_comprehension from 
                the previous file
                
                write a measure_runtime coroutine                 that will execute 
                async_comprehension four times in                 parallel using asyncio.gather
                
                measure_runtime should measure the                total runtime and return it
"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measure the runtime of async_comprehension executed 4 times in
        parallel. '''
    first_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    next_time = time()

    return next_time - first_time
