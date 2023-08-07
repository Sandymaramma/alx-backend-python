#!/usr/bin/env python3
import asyncio
from typing import List
from random import randint

# Import the wait_random function from the local basic_async_syntax.py file
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    n = 5
    max_delay = 10
    asyncio.run(wait_n(n, max_delay))

