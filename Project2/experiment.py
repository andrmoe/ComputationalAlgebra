from prime import *
from typing import Callable
from timeit import timeit
from functools import partial


def generic_prime_finder_timer(binary_digits: int, range_size: int, search_func: Callable[[int, int], int]) -> float:
    n_min = 1 << binary_digits
    n_max = n_min + range_size
    return timeit(lambda: search_func(n_min, n_max), number=20)


print(generic_prime_finder_timer(500, 200, find_prime))
print(generic_prime_finder_timer(500, 200, find_prime_trial_division))