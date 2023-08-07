#!/usr/bin/env python3

import asyncio
from typing import List
from time import time
from random import randint


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Return execution time for wait_n given `n` and `max_delay`. '''
    time_0 = time()
    run(wait_n(n, max_delay))
    time_1 = time()
    elapsed_time = time_1 - time_0
    return elapsed_time / n
