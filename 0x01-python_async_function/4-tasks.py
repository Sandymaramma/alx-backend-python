#!/usr/bin/env python3
import asyncio
from typing import List
from random import randint

# Import the task_wait_random function from the local tasks.py file
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    n = 5
    max_delay = 10
    asyncio.run(task_wait_n(n, max_delay))
